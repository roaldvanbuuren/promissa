"""Add EUR values to commitments.json and delivery.json using rates.json. Original amount and currency are kept.
Run after build_commitments.py, build_delivery.py and build_rates.py (build_all.py does this)."""
import json, collections
J = lambda p: json.load(open(p, encoding="utf-8"))
def W(p, o):
    with open(p, "w", encoding="utf-8") as f: json.dump(o, f, ensure_ascii=False, indent=2); f.write("\n")
rates = J("rates.json"); C = J("commitments.json"); D = J("delivery.json")
rt = {(r["currency"], r["announcement_date"]): r for r in rates["rates"]}
com = {r["id"]: r for r in C["rows"]}

def rate_for(cur, date):
    if cur == "EUR": return 1.0, date, False
    r = rt[(cur, date)]; return r["units_per_eur"], r["rate_date_used"], r["prior_business_day_used"]

for r in C["rows"]:
    if r["amount"] is None:
        r.update(amount_eur=None, fx_rate=None, fx_rate_date=None)
    else:
        k, used, _ = rate_for(r["currency"], r["date_announced"])
        r.update(amount_eur=round(r["amount"] / k), fx_rate=k, fx_rate_date=used)

def chain(i):
    o = [i]
    while com[o[-1]]["part_of"]: o.append(com[o[-1]]["part_of"])
    return o
def basis_row(i):
    return next((c for c in chain(i) if com[c]["counted_in_totals"]), i)

for r in D["rows"]:
    if r["amount_evidenced"] is None:
        r.update(amount_evidenced_eur=None, fx_rate=None, fx_rate_date=None, fx_basis_commitment=None)
    else:
        b = basis_row(r["id"]); k, used, _ = rate_for(r["currency"], com[b]["date_announced"])
        r.update(amount_evidenced_eur=round(r["amount_evidenced"] / k), fx_rate=k, fx_rate_date=used, fx_basis_commitment=b)
ev = {r["id"]: r for r in D["rows"]}
for e in D["rollup"]:
    k, used, _ = rate_for(e["currency"], com[e["commitment_id"]]["date_announced"])
    e["promised_amount_eur"] = round(e["promised_amount"] / k) if e["promised_amount"] else None
    e["evidenced_amount_eur"] = sum(ev[c["id"]]["amount_evidenced_eur"] for c in e["contributions"])
    for c in e["contributions"]: c["amount_eur"] = ev[c["id"]]["amount_evidenced_eur"]
    e["fx_rate"], e["fx_rate_date"] = k, used
for o in D["outside_totals"]:
    o["amount_eur"] = ev[o["id"]]["amount_evidenced_eur"]
W("commitments.json", C); W("delivery.json", D)

print(f"{'jurisdiction':16}{'promised EUR m':>16}{'evidenced EUR m':>17}  share")
for j in ["United Kingdom", "European Union", "France", "Germany", "Italy", "Netherlands"]:
    p = sum(r["amount_eur"] for r in C["rows"] if r["jurisdiction"] == j and r["counted_in_totals"] and r["amount_eur"])
    e = sum(x["evidenced_amount_eur"] for x in D["rollup"] if x["jurisdiction"] == j)
    print(f"{j:16}{p/1e6:16,.1f}{e/1e6:17,.1f}  {e/p:5.1%}" if p else j)
