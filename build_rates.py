"""Build rates.json: ECB euro foreign exchange reference rates for every announcement date of a non-EUR commitment.

The ECB data API and download files are not reachable from the build environment (shell egress limits; the API
refuses automated fetches). The ECB daily reference rate history (eurofxref-hist) is read from the pip package
CurrencyConverter, which bundles that ECB file. Needs:  pip install CurrencyConverter
Rule: if the announcement date has no ECB rate (weekend or TARGET closing day), use the last earlier day that has one,
and record both dates.
"""
import json, datetime as dt, sys
from currency_converter import CurrencyConverter
import importlib.metadata as md

c = CurrencyConverter()
com = json.load(open("commitments.json", encoding="utf-8"))["rows"]
need = {}
for r in com:
    if r["currency"] and r["currency"] != "EUR":
        need.setdefault(r["currency"], {}).setdefault(r["date_announced"], []).append(r["id"])

out_rates = []
for cur, dates in sorted(need.items()):
    table = c._rates[cur]
    for d, ids in sorted(dates.items()):
        D = dt.date.fromisoformat(d); U = D
        while table.get(U) is None:
            U -= dt.timedelta(days=1)
            if (D - U).days > 10: sys.exit(f"no rate near {d} for {cur}")
        out_rates.append({"currency": cur, "announcement_date": d, "rate_date_used": U.isoformat(),
                          "prior_business_day_used": U != D, "units_per_eur": table[U], "used_by": sorted(ids)})

# spot checks against figures published on ecb.europa.eu and read during the build
checks = {"2023-03-15": 0.87243}
for k, v in checks.items():
    got = c._rates["GBP"][dt.date.fromisoformat(k)]
    assert abs(got - v) < 1e-9, (k, got, v)

out = {
    "project": "Promissa", "file": "rates", "base_currency": "EUR",
    "quote_convention": "units of the currency per 1 EUR, as published by the ECB (five decimals). EUR value = original amount divided by this rate.",
    "source": "ECB euro foreign exchange reference rates (EXR.D.<CCY>.EUR.SP00.A), daily, set around 14:15 CET and published around 16:00 CET",
    "how_read": f"From the ECB daily history bundled in the Python package CurrencyConverter {md.version('CurrencyConverter')} (data runs {c.bounds['GBP'].first_date} to {c.bounds['GBP'].last_date}). The ECB's own download and data API were not reachable from the build environment.",
    "verification": "One date was checked against the ECB's published GBP table for March 2023: 15 March 2023 = 0.87243, equal to the bundled value. Other dates are not independently checked.",
    "rule": "The rate on the announcement date. If the ECB published none that day (weekend or TARGET closing day), the last earlier published rate is used and prior_business_day_used is true. Amounts stated in EUR are not converted.",
    "delivery_rule": "An evidenced amount is converted at the rate of the announcement date of the commitment it counts against (the nearest counted ancestor), so promised and evidenced amounts share one rate. Evidenced amounts on rows that count against no commitment use their own commitment's date.",
    "caveat": "Dates with year-only precision (UK-014, UK-015: 1 January 2025) use the rate of the last published day before, so those two EUR values are indicative.",
    "rates": out_rates,
}
json.dump(out, open("rates.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2); open("rates.json", "a").write("\n")
print(f"rates.json: {len(out_rates)} rates;", sum(r["prior_business_day_used"] for r in out_rates), "use an earlier business day")
