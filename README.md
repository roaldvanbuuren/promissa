# Promissa

A sourced public ledger of AI commitments made by governments, set against evidence of what was actually delivered.

Jurisdictions: United Kingdom, European Union, France, Germany, Italy, Netherlands. Period: 1 January 2023 to 9 November 2026.

Status: Steps 1 to 3 are done (commitments, delivery evidence, EUR values). The site is not started.

## Data rules

- One row is one public commitment by a government or its agencies, with a source URL. No source URL means no row.
- Official sources first, then institutions (state-owned bodies, recipients), then reputable press.
- An amount is only what a source states. If none is stated the row says "no amount stated". Nothing is estimated.
- `counted_in_totals` marks rows that enter the promised total. Child rows (`part_of`), re-announcements (`reannounces`), mobilisation targets, company-funded amounts, press-only figures and aggregates are listed but not summed, so nothing is counted twice.
- Not counted by scope: private company investment announcements, general digital budgets with no AI line, party manifesto pledges.
- Original amount and currency are kept. EUR values (`amount_eur`, `amount_evidenced_eur`) use the ECB reference rate on the announcement date; if none was published that day (weekend, TARGET closing day) the last earlier rate is used. Rates are cached in `rates.json`.
- `delivery.json` has a `rollup` block: evidenced amounts are attributed to the nearest counted commitment via `part_of`, so a facility's evidence counts toward its programme. Nothing is capped; flags mark where evidenced exceeds promised.
- "No evidence found" is not "not delivered". Step 2 keeps them apart, and a commitment with no row in `delivery.json` is "not checked", a third state.
- `amount_evidenced` is only an amount a cited source states for what was delivered, allocated or awarded. It is often a budget or a contract total, not spending, and it understates delivery because sources often state no amount.

## Files

| File | What |
|---|---|
| `commitments.json` | Step 1 output |
| `rates.json` | ECB reference rates used for every non-EUR announcement date, with the rule and the source |
| `delivery.json` | Step 2 output: evidence of delivery, for the commitments that were checked |
| `gaps.md` | Sources that failed, items not added, conflicting figures, judgement calls |
| `build_commitments.py` | Merges `src/*.py`, validates, writes `commitments.json`, prints counts |
| `build_rates.py` | Writes `rates.json` from the ECB daily history (needs `pip install CurrencyConverter`) |
| `normalise.py` | Adds EUR values to `commitments.json` and `delivery.json` |
| `build_all.py` | Runs all four builders in order |
| `build_delivery.py` | Reads `src/delivery_rows.py`, validates against `commitments.json`, writes `delivery.json` |
| `src/` | One module per jurisdiction, with the row for each commitment |

## Run

```
pip install CurrencyConverter
python3 build_all.py
```

The script exits with an error if a row has no source URL, an unknown type, a broken `part_of` or `reannounces` link, an amount without a currency, a date outside the period, or a counted row that is a child or re-announcement.
