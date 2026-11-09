"""Build delivery.json from src/delivery_rows.py and validate it against commitments.json.

Run:  python3 build_commitments.py && python3 build_delivery.py
"""
import json, re, sys, collections
sys.path.insert(0, "src")
import delivery_rows

STATUSES = ["delivered", "partly delivered", "in progress", "no evidence found", "withdrawn", "re-announced"]
EVTYPES = {"facility operating", "grant or contract award", "budget line", "audit report",
           "parliamentary answer", "progress report by the announcing body", "search of named sources"}

com = {r["id"]: r for r in json.load(open("commitments.json", encoding="utf-8"))["rows"]}
rows = delivery_rows.D
errors, seen = [], set()

for r in rows:
    i = r["id"]
    if i in seen: errors.append(f"{i}: duplicate")
    seen.add(i)
    if i not in com: errors.append(f"{i}: no such commitment"); continue
    c = com[i]
    if r["status"] not in STATUSES: errors.append(f"{i}: bad status")
    if r["evidence_type"] not in EVTYPES: errors.append(f"{i}: bad evidence type")
    if not re.match(r"^https?://", r["evidence_url"] or ""): errors.append(f"{i}: no evidence URL")
    if r["status"] == "no evidence found" and r["amount_evidenced"] is not None:
        errors.append(f"{i}: 'no evidence found' with an amount")
    if r["status"] == "re-announced":
        if not r["see"] or r["see"] not in com: errors.append(f"{i}: re-announced without a valid 'see'")
        elif c["reannounces"] != r["see"]: errors.append(f"{i}: 'see' does not match commitments.json reannounces")
        if r["amount_evidenced"] is not None: errors.append(f"{i}: re-announced row carries an amount")
    if r["amount_evidenced"] is not None:
        if not r["amount_evidenced_basis"]: errors.append(f"{i}: amount without basis")
        if r["status"] == "no evidence found": errors.append(f"{i}: amount on no-evidence row")
    if r["evidence_date"] and r["evidence_date"] > "2026-11-09": errors.append(f"{i}: evidence date in future")
    # each commitment row's currency should match where both have amounts
    if r["amount_evidenced"] is not None and c["currency"] and r["currency"] != c["currency"]:
        errors.append(f"{i}: currency {r['currency']} differs from commitment {c['currency']}")
    if re.search("[—–]", json.dumps(r, ensure_ascii=False)): errors.append(f"{i}: dash character")

if errors:
    print("VALIDATION FAILED"); [print(" -", e) for e in errors]; sys.exit(1)


# ---- roll-up rule ----
# Evidence amounts are recorded on the row where the source states them. For the per-jurisdiction bar they are
# attributed to the nearest counted ancestor (following part_of), so child evidence (a facility inside a
# programme) is not lost. Rules: re-announced rows carry no amount; if a counted row and its own descendant both
# carry an amount, only the shallower one is used (assumed to overlap); siblings in different branches are added.
# Rows whose chain never reaches a counted row are reported as outside_totals and are not in any bar.
def chain(i):
    out = [i]
    while com[out[-1]]["part_of"]:
        out.append(com[out[-1]]["part_of"])
    return out
amt = {r["id"]: r for r in rows if r["amount_evidenced"] is not None}
rollup = {}
outside = []
for i, r in amt.items():
    ch = chain(i)
    top = next((c for c in ch if com[c]["counted_in_totals"]), None)
    if top is None:
        outside.append({"id": i, "amount": r["amount_evidenced"], "currency": r["currency"]}); continue
    # drop if a shallower row on the path (between i and top inclusive, excluding i) already has an amount
    shallower = [c for c in ch[1:ch.index(top) + 1] if c in amt]
    entry = rollup.setdefault(top, {"commitment_id": top, "jurisdiction": com[top]["jurisdiction"],
                                    "promised_amount": com[top]["amount"], "currency": com[top]["currency"],
                                    "evidenced_amount": 0, "contributions": [], "dropped_overlap": [], "flags": []})
    if shallower:
        entry["dropped_overlap"].append({"id": i, "amount": r["amount_evidenced"], "overlaps_with": shallower[0]}); continue
    if r["currency"] != entry["currency"]:
        entry["flags"].append(f"{i}: currency differs"); continue
    entry["evidenced_amount"] += r["amount_evidenced"]
    entry["contributions"].append({"id": i, "amount": r["amount_evidenced"], "via": "self" if i == top else "descendant"})
for e in rollup.values():
    if e["promised_amount"] and e["evidenced_amount"] > e["promised_amount"]:
        e["flags"].append("evidenced amount exceeds the promised amount (different bases; see the contributing rows)")
rollup = sorted(rollup.values(), key=lambda e: e["commitment_id"])

order = {"United Kingdom": 0, "European Union": 1, "France": 2, "Germany": 3, "Italy": 4, "Netherlands": 5}
rows = sorted(rows, key=lambda r: (order[com[r["id"]]["jurisdiction"]], r["id"]))
out = {
    "project": "Promissa", "file": "delivery", "checked": "2026-11-09",
    "note": "Only commitments listed here were checked. 'no evidence found' means the named sources were searched and nothing was found; it does not mean not delivered. Rows missing from this file were not checked (see gaps.md). Amounts are only what a source states and are often budgets or allocations, not spending.",
    "statuses": STATUSES,
    "rollup_rule": "Evidence amounts are attributed to the nearest counted ancestor via part_of. If a row and its own ancestor both carry an amount, only the shallower is used. Siblings in different branches are added. Re-announced rows carry no amount. Nothing is capped or altered; flags mark where evidenced exceeds promised.",
    "rollup": rollup,
    "outside_totals": outside,
    "rows": rows,
}
with open("delivery.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2); f.write("\n")

cnt = collections.Counter(r["status"] for r in rows)
print("status counts:", {s: cnt.get(s, 0) for s in STATUSES})
print(f"{'jurisdiction':16} {'commitments':>11} {'counted':>8} {'counted+checked':>16} {'unchecked counted':>18} {'evidenced amt (counted)':>26}")
for j in order:
    cs = [c for c in com.values() if c["jurisdiction"] == j]
    cc = [c for c in cs if c["counted_in_totals"]]
    chk = [c for c in cc if c["id"] in seen]
    ev = collections.defaultdict(float)
    for e in rollup:
        if e["jurisdiction"] == j:
            ev[e["currency"]] += e["evidenced_amount"]
    s = "  ".join(f"{k} {v/1e6:,.1f}m" for k, v in ev.items()) or "-"
    print(f"{j:16} {len(cs):11d} {len(cc):8d} {len(chk):16d} {len(cc)-len(chk):18d} {s:>26}")
print("unchecked counted rows:", sorted(c["id"] for c in com.values() if c["counted_in_totals"] and c["id"] not in seen))
