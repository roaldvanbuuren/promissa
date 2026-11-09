"""Build data.json for the site from commitments.json, delivery.json and rates.json. Static; no backend."""
import json, collections
J = lambda p: json.load(open(p, encoding="utf-8"))
C, D, R = J("commitments.json"), J("delivery.json"), J("rates.json")
dl = {r["id"]: r for r in D["rows"]}
rows = C["rows"]
MANUAL = {
    "EU-007": "aggregate of EU-003 to EU-006",
    "EU-008": "total supercomputing and AI Factories budget, not an AI-only line",
    "FR-005": "cumulative envelope that overlaps FR-001, FR-002 and earlier years",
    "DE-006": "cloud, AI and data infrastructure with no AI split",
    "NL-002": "awarded before the period",
}
BASIS = {"mobilisation": "mobilisation target (public and private money)", "company": "funded by a company",
         "press_reported": "press-reported figure only"}
def reason(r):
    if r["counted_in_totals"]: return None
    out = []
    if r["part_of"]: out.append(f"part of {r['part_of']}")
    if r["reannounces"]: out.append(f"re-announces {r['reannounces']}")
    if r["id"] in MANUAL: out.append(MANUAL[r["id"]])
    elif r["amount"] is None: out.append("no amount stated")
    elif r["amount_basis"] in BASIS: out.append(BASIS[r["amount_basis"]])
    return "; ".join(out) or "listed, not counted"
reann_by = collections.defaultdict(list)
for r in rows:
    if r["reannounces"]: reann_by[r["reannounces"]].append(r["id"])
out_rows = []
for r in rows:
    x = dict(r)
    x["not_counted_reason"] = reason(r)
    x["reannounced_by"] = reann_by.get(r["id"], [])
    d = dl.get(r["id"])
    x["delivery"] = None if d is None else {k: d[k] for k in (
        "status", "evidence_type", "summary", "amount_evidenced", "currency", "amount_evidenced_eur",
        "amount_evidenced_basis", "evidence_url", "evidence_date", "date_checked", "more_urls", "see", "notes")}
    out_rows.append(x)

juris = []
for j in ["United Kingdom", "European Union", "France", "Germany", "Italy", "Netherlands"]:
    rs = [r for r in rows if r["jurisdiction"] == j]
    counted = [r for r in rs if r["counted_in_totals"]]
    chk = [r for r in counted if r["id"] in dl]
    ro = [e for e in D["rollup"] if e["jurisdiction"] == j]
    juris.append({
        "name": j, "rows": len(rs), "counted": len(counted), "counted_checked": len(chk),
        "counted_unchecked": len(counted) - len(chk), "listed_not_counted": len(rs) - len(counted),
        "promised_eur": sum(r["amount_eur"] or 0 for r in counted),
        "evidenced_eur": sum(e["evidenced_amount_eur"] for e in ro),
        "flags": [f"{e['commitment_id']}: {f}" for e in ro for f in e["flags"]],
    })
data = {
    "project": "Promissa", "generated_from": ["commitments.json", "delivery.json", "rates.json"],
    "period": C["period"], "last_checked": D["checked"],
    "statuses": D["statuses"], "jurisdictions": juris, "rows": out_rows,
    "rollup": D["rollup"], "rates_note": R["how_read"],
    "stats": {"rows": len(rows), "counted": sum(r["counted_in_totals"] for r in rows),
              "checked": len(dl), "reannouncements": sum(1 for r in rows if r["reannounces"])},
}
with open("data.json", "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=1); f.write("\n")
print("data.json:", data["stats"], f"{len(json.dumps(data))//1024} KB")
