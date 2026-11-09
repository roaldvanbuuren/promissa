# Promissa

A sourced public ledger of AI commitments made by governments, set against evidence of what was actually delivered.

Jurisdictions: United Kingdom, European Union, France, Germany, Italy, Netherlands. Period: 1 January 2023 to 9 November 2026.

Status: Step 1 (commitments) is done. Delivery evidence, EUR normalisation and the site are not started.

## Data rules

- One row is one public commitment by a government or its agencies, with a source URL. No source URL means no row.
- Official sources first, then institutions (state-owned bodies, recipients), then reputable press.
- An amount is only what a source states. If none is stated the row says "no amount stated". Nothing is estimated.
- `counted_in_totals` marks rows that enter the promised total. Child rows (`part_of`), re-announcements (`reannounces`), mobilisation targets, company-funded amounts, press-only figures and aggregates are listed but not summed, so nothing is counted twice.
- Not counted by scope: private company investment announcements, general digital budgets with no AI line, party manifesto pledges.
- Original amount and currency are kept. A EUR value comes in Step 3.
- "No evidence found" is not "not delivered". Step 2 keeps them apart.

## Files

| File | What |
|---|---|
| `commitments.json` | Step 1 output |
| `gaps.md` | Sources that failed, items not added, conflicting figures, judgement calls |
| `build_commitments.py` | Merges `src/*.py`, validates, writes `commitments.json`, prints counts |
| `src/` | One module per jurisdiction, with the row for each commitment |

## Run

```
python3 build_commitments.py
```

The script exits with an error if a row has no source URL, an unknown type, a broken `part_of` or `reannounces` link, an amount without a currency, a date outside the period, or a counted row that is a child or re-announcement.
