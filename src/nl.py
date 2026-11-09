from common import row
J = "Netherlands"
R = []

GOV_NL = [("2022-01-10", "Rutte IV government"), ("2023-07-07", "Rutte IV government (caretaker)"),
          ("2024-07-02", "Schoof government"), ("2025-06-03", "Schoof government (caretaker)")]
def nl_gov(date):
    g = None
    for start, name in GOV_NL:
        if date[:10] >= start:
            g = name
    return g

def add(id, body, date, *a, **k):
    R.append(row(id, J, body, nl_gov(date), date, *a, **k))

VIS = "https://www.rijksoverheid.nl/actueel/nieuws/2024/01/18/kabinet-presenteert-visie-op-generatieve-ai"
add("NL-001", "Ministry of Economic Affairs and Climate Policy (EZK) via RVO", "2023-11-02", "GPT-NL open Dutch language model",
    "Contribute €13.5 million from the first Applied Research Facilities funding round to develop GPT-NL, an open Dutch language model.", "funding programme",
    13_500_000, "EUR", "€13.5 million", "not stated", VIS,
    notes="Amount from the Cabinet's January 2024 vision. The date of 2 November 2023 is from the Digital Economy Strategy progress report of March 2025.",
    more_urls=["https://www.tweedekamer.nl/downloads/document?id=2025D10009"])
add("NL-002", "National Growth Fund (AiNed programme)", "2024-01-18", "AiNed programme: €204.5 million for AI knowledge, innovation and application",
    "Make €204.5 million available through the AiNed programme of the National Growth Fund for AI knowledge, innovation and use.", "funding programme",
    204_500_000, "EUR", "€204.5 million", "multi-year (2022 to 2029 per later report)", VIS,
    counted=False,
    notes="Restated by the Cabinet on 18 January 2024. The funds were awarded in earlier Growth Fund rounds (€160.5 million awarded plus €44 million conditionally, per a parliamentary reply), before the period of this ledger, so the row is listed but not counted. A March 2025 progress report gives a total AiNed budget of €189 million for 2022 to 2029, which conflicts with €204.5 million. See gaps.md.",
    more_urls=["https://www.tweedekamer.nl/downloads/document?id=2024D27504",
               "https://rijksoverheid.nl/ministeries/ministerie-van-economische-zaken/nieuws/2024/07/12/groen-licht-voor-vervolg-vijf-lopende-projecten-nationaal-groeifonds"])
add("NL-003", "Cabinet", "2024-01-18", "Government-wide vision on generative AI: national AI validation team",
    "Set up a national government AI validation team to assess available AI applications, alongside the vision on generative AI.", "institute",
    None, None, None, "not stated", VIS,
    notes="The page announces the team without an amount.")
add("NL-004", "Cabinet (Ministries of Economic Affairs and of Defence)", "2025-06-27", "AI factory in Groningen",
    "Contribute €70 million from the Cabinet to an AI factory in Groningen, within a planned total of up to €200 million with €60 million from the region and a €70 million EU co-financing request.", "compute",
    70_000_000, "EUR", "€70 million from the Cabinet (total up to €200 million)", "not stated",
    "https://www.rijksoverheid.nl/actueel/nieuws/2025/06/27/nederland-zet-in-op-200-miljoen-euro-voor-aifabriek-in-groningen",
    notes="Only the Cabinet's own €70 million is counted. The €60 million regional share is not a national government commitment, and the €70 million EU share was a pending request, which would appear in the EU AI Factory rows if granted. The proposal was submitted to EuroHPC on 27 June 2025 subject to parliamentary approval of the budget changes.",
    more_urls=["https://www.rijksoverheid.nl/actueel/nieuws/2025/06/27/defensie-investeert-in-ai-fabriek-in-groningen",
               "https://open.overheid.nl/documenten/21889b96-6b05-4dd2-847b-0a6457522b11/file"])
