"""Merge the per-jurisdiction modules in src/ into commitments.json and validate the rows.

Run:  python3 build_commitments.py
Fails (non-zero exit) if any rule below is broken.
"""
import json, re, sys, collections
sys.path.insert(0, "src")
import uk, eu, fr, de, it, nl

MODULES = [uk, eu, fr, de, it, nl]
TYPES = {"funding programme", "compute", "institute", "gigafactory", "skills", "tax incentive", "partnership"}
BASES = {"public", "mobilisation", "company", "press_reported", "none"}
TIERS = {"official", "institution", "press"}

rows = [r for m in MODULES for r in m.R]
ids = [r["id"] for r in rows]
errors = []

# unique ids
for i, n in collections.Counter(ids).items():
    if n > 1: errors.append(f"duplicate id {i}")
idset = set(ids)

for r in rows:
    i = r["id"]
    if not re.match(r"^https?://", r["source_url"] or ""): errors.append(f"{i}: no source URL")
    if r["type"] not in TYPES: errors.append(f"{i}: unknown type {r['type']}")
    if r["amount_basis"] not in BASES: errors.append(f"{i}: unknown basis")
    if r["source_tier"] not in TIERS: errors.append(f"{i}: unknown tier")
    if not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", r["date_announced"]): errors.append(f"{i}: bad date {r['date_announced']}")
    if r["date_announced"] < "2023-01-01": errors.append(f"{i}: before period")
    if r["date_announced"][:10] > "2026-11-09": errors.append(f"{i}: after today")
    if (r["amount"] is None) != (r["currency"] is None): errors.append(f"{i}: amount/currency mismatch")
    if r["amount"] is None and (r["counted_in_totals"] or r["amount_basis"] != "none"):
        errors.append(f"{i}: no amount but counted or basis set")
    if r["amount"] is not None and not r["amount_as_stated"]: errors.append(f"{i}: amount without stated text")
    for k in ("part_of", "reannounces"):
        if r[k] and r[k] not in idset: errors.append(f"{i}: {k} -> {r[k]} does not exist")
    if r["counted_in_totals"] and (r["part_of"] or r["reannounces"]):
        errors.append(f"{i}: counted but is a child or re-announcement")
    if r["counted_in_totals"] and r["amount_basis"] != "public":
        errors.append(f"{i}: counted but basis is {r['amount_basis']}")
    if "—" in json.dumps(r, ensure_ascii=False) or "–" in json.dumps(r, ensure_ascii=False):
        errors.append(f"{i}: contains a dash character that the style rules forbid")

if errors:
    print("VALIDATION FAILED"); [print(" -", e) for e in errors]; sys.exit(1)

order = {"United Kingdom": 0, "European Union": 1, "France": 2, "Germany": 3, "Italy": 4, "Netherlands": 5}
rows.sort(key=lambda r: (order[r["jurisdiction"]], r["id"]))

out = {
    "project": "Promissa",
    "file": "commitments",
    "generated": "2026-11-09",
    "period": {"from": "2023-01-01", "to": "2026-11-09"},
    "note": "Not exhaustive. Each row is one public commitment with a source URL. counted_in_totals marks the rows that enter the 'promised' total; child rows, re-announcements, mobilisation targets and company-funded amounts are listed but not summed.",
    "rows": rows,
}
with open("commitments.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2); f.write("\n")

# counts per jurisdiction
print(f"{'jurisdiction':16} {'rows':>5} {'counted':>8} {'with amt':>9} {'no amt':>7} {'promised (counted, EUR)':>26}")
tot = collections.Counter()
for j in order:
    rs = [r for r in rows if r["jurisdiction"] == j]
    c = [r for r in rs if r["counted_in_totals"]]
    na = [r for r in rs if r["amount"] is None]
    eur = sum(r["amount"] for r in c if r["currency"] == "EUR")
    gbp = sum(r["amount"] for r in c if r["currency"] == "GBP")
    s = f"EUR {eur/1e9:,.3f}bn" if eur else ""
    s += f"  GBP {gbp/1e9:,.3f}bn" if gbp else ""
    print(f"{j:16} {len(rs):5d} {len(c):8d} {len(rs)-len(na):9d} {len(na):7d} {s:>26}")
    tot["rows"] += len(rs); tot["counted"] += len(c); tot["noamt"] += len(na)
print(f"{'TOTAL':16} {tot['rows']:5d} {tot['counted']:8d} {'':9} {tot['noamt']:7d}")
print("re-announcements:", [(r['id'], r['reannounces']) for r in rows if r['reannounces']])
