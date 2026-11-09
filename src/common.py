"""Shared helper for building commitments.json rows. One module per jurisdiction."""
GOV_UK = {  # government in office, by date range (inclusive start)
    "UK": [("2022-10-25", "Sunak government"), ("2024-07-05", "Starmer government"), ("2026-07-20", "Burnham government")],
}

def uk_gov(date):
    g = None
    for start, name in GOV_UK["UK"]:
        if date >= start:
            g = name
    return g

def row(id, jur, body, gov, date, title, promised, type, amount, cur, amount_text, period, url, *,
        basis="public", counted=True, part_of=None, reannounces=None, tier="official",
        precision="day", notes=None, more_urls=None):
    """basis: public | mobilisation | company | press_reported | none
       counted: whether the row enters the 'promised' total (False for children, re-announcements,
       mobilisation targets and company-funded amounts, so nothing is counted twice)."""
    if amount is None:
        amount_text = amount_text or "no amount stated"
        basis = "none"
        counted = False
    return dict(id=id, jurisdiction=jur, body=body, government_in_office=gov, date_announced=date,
                date_precision=precision, title=title, promised=promised, type=type,
                amount_as_stated=amount_text, amount=amount, currency=cur if amount is not None else None,
                period=period or "not stated", source_url=url, source_tier=tier,
                amount_basis=basis, counted_in_totals=counted, part_of=part_of,
                reannounces=reannounces, notes=notes, more_urls=more_urls or [])
