from common import row
J = "European Union"
C1, C2 = "von der Leyen Commission I", "von der Leyen Commission II"
R = []
def add(id, body, gov, *a, **k): R.append(row(id, J, body, gov, *a, **k))
IP = "https://ec.europa.eu/commission/presscorner/api/files/document/print/en/"
add("EU-001", "European Commission", C2, "2025-02-11", "InvestAI initiative",
    "Mobilise €200 billion of investment in AI in Europe.", "funding programme", 200_000_000_000, "EUR",
    "€200 billion to mobilise", "not stated",
    "https://digital-strategy.ec.europa.eu/en/news/eu-launches-investai-initiative-mobilise-eu200-billion-investment-artificial-intelligence",
    basis="mobilisation", counted=False,
    notes="A target to mobilise public and private capital, not a stated public commitment. Commission funding comes from existing programmes (Digital Europe, Horizon Europe, InvestEU). Excluded from the promised total.",
    more_urls=["https://ec.europa.eu/commission/presscorner/detail/en/ip_25_467"])
add("EU-002", "European Commission / EIB", C2, "2025-02-11", "InvestAI fund for AI gigafactories",
    "Mobilise €20 billion through a new European fund to finance AI gigafactories.", "gigafactory", 20_000_000_000, "EUR",
    "€20 billion to mobilise", "not stated", "https://ec.europa.eu/commission/presscorner/detail/en/ip_25_467",
    basis="mobilisation", counted=False, part_of="EU-001",
    notes="Press release says four gigafactories; the April 2025 AI Continent Action Plan says up to five; the July 2026 call says up to seven.",
    more_urls=["https://commission.europa.eu/topics/competitiveness/competitiveness-coordination-tool-projects/ai-gigafactories_en"])
add("EU-003", "EuroHPC Joint Undertaking / European Commission", C1, "2024-12-10", "First seven EuroHPC AI Factories",
    "Set up seven AI Factories with €1.5 billion of combined national and EU funding.", "compute", 1_500_000_000, "EUR",
    "€1.5 billion (half funded by the EU)", "not stated", IP+"ip_24_6302/IP_24_6302_EN.pdf")
add("EU-004", "EuroHPC Joint Undertaking / European Commission", C2, "2025-03-12", "Second wave of six AI Factories",
    "Set up six more AI Factories with around €485 million of national and EU investment.", "compute", 485_000_000, "EUR",
    "around €485 million", "not stated", "https://digital-strategy.ec.europa.eu/en/node/13476/printable/pdf",
    notes="Selection date of 12 March 2025 taken from Commission press release IP/25/1013.",
    more_urls=[IP+"ip_25_1013/IP_25_1013_EN.pdf"])
add("EU-005", "EuroHPC Joint Undertaking / European Commission", C2, "2025-10", "Third wave of six AI Factories",
    "Set up six more AI Factories with over €500 million of joint EU and Member State investment.", "compute", 500_000_000, "EUR",
    "over €500 million", "not stated",
    "https://digital-strategy.ec.europa.eu/en/news/eu-expands-network-ai-factories-strengthening-its-ai-continent-ambition",
    precision="month", notes="Amount is a floor ('over'). Exact day not shown on the page retrieved.")
add("EU-006", "EuroHPC Joint Undertaking", C2, "2025-10-13", "Thirteen AI Factory Antennas",
    "Fund 13 AI Factory Antennas with around €55 million from the EU, matched by participating states.", "compute", 55_000_000, "EUR",
    "around €55 million (EU share)", "not stated",
    "https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en")
add("EU-007", "European Commission", C2, "2025-10", "AI Factories and Antennas: over €2.6 billion committed",
    "Total of over €2.6 billion committed by the EU and participating countries to AI Factories and Antennas.", "compute", 2_600_000_000, "EUR",
    "over €2.6 billion", "not stated",
    "https://digital-strategy.ec.europa.eu/en/news/eu-expands-network-ai-factories-strengthening-its-ai-continent-ambition",
    counted=False, precision="month", notes="Aggregate of EU-003 to EU-006; not added again.")
add("EU-008", "European Commission", C2, "2025-02-11", "'€10 billion' AI Factories support (as first described)",
    "Existing support for AI Factories of €10 billion, co-financed by the EU and Member States.", "compute", 10_000_000_000, "EUR",
    "€10 billion", "2021-2027", "https://ec.europa.eu/commission/presscorner/detail/en/ip_25_467",
    counted=False, notes="Later Commission pages describe €10 billion as total EuroHPC supercomputing plus AI Factories investment for 2021-2027, so it is not an AI-only figure. See gaps.md.",
    more_urls=["https://digital-strategy.ec.europa.eu/en/policies/ai-factories"])
add("EU-009", "EuroHPC Joint Undertaking / European Commission", C2, "2026-07-30", "AI Gigafactories call for tenders",
    "Support up to seven AI Gigafactories with up to €10 billion of EU and national funding, expected to unlock at least €20 billion of private investment.",
    "gigafactory", 10_000_000_000, "EUR", "up to €10 billion (EU and national)", "two phases; bulk from the 2028-2035 budget framework",
    IP+"ip_26_1708/IP_26_1708_EN.pdf",
    notes="Call page says only part is covered by the current budget framework and 'the bulk' comes from the next MFF (2028-2035), which is not yet adopted. Implements EU-002; the EU share is up to €100m + €400m per project (lot 1, four projects) and €200m + €800m (lot 2, three projects).",
    more_urls=["https://www.eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en"])
add("EU-010", "European Commission", C2, "2025-10-08", "Apply AI Strategy",
    "Mobilise around €1 billion from existing EU funding programmes to speed AI adoption in key sectors.", "funding programme", 1_000_000_000, "EUR",
    "around €1 billion", "not stated", IP+"ip_25_2299/IP_25_2299_EN.pdf",
    notes="Drawn from existing programmes, so partly overlaps with other lines.")
add("EU-011", "European Commission", C2, "2025-10-08", "AI in Science Strategy: compute for researchers",
    "Provide €600 million from Horizon Europe to expand compute access for science, including access to AI Gigafactories.", "compute", 600_000_000, "EUR",
    "€600 million", "not stated",
    "https://luxembourg.representation.ec.europa.eu/actualites-et-evenements/actualites/commission-launches-two-strategies-speed-ai-uptake-european-industry-and-science-2025-10-08_en",
    tier="official", notes="Republication of the Commission press release. Possible overlap with EU-012 not resolved; see gaps.md.")
add("EU-012", "European Commission", C2, "2025-11-03", "RAISE pilot (Resource for AI Science in Europe)",
    "Fund the RAISE pilot with €107 million under Horizon Europe.", "funding programme", 107_000_000, "EUR",
    "€107 million", "Horizon Europe Work Programme 2026-27",
    "https://digital-strategy.ec.europa.eu/en/news/commission-launches-resource-ai-science-europe",
    notes="The strategy document COM(2025) 724 says €108 million; the launch press release says €107 million. See gaps.md.")
add("EU-013", "EuroHPC Joint Undertaking", C1, "2024-09-09", "Alice Recoque exascale supercomputer (France)",
    "Procure a second European exascale supercomputer, hosted in France, with a total acquisition budget of €354.8 million, half from the EU and half from France, the Netherlands and Greece.", "compute", 354_800_000, "EUR",
    "€354.8 million total (EuroHPC 50%, Jules Verne consortium 50%)", "acquisition, delivery, installation and maintenance",
    "https://www.eurohpc-ju.europa.eu/new-call-procure-european-exascale-supercomputer-alice-recoque-2024-09-09_en",
    notes="Filed under the EU because EuroHPC owns the system; the French, Dutch and Greek shares are not separated in the source, so they are not repeated in the national ledgers. Other figures for the same system differ: the June 2024 hosting-agreement release says total cost of ownership above €544 million, and the November 2025 releases say €554 million over five years of operation. See gaps.md. Hosting agreement signed 18 June 2024; contract with Eviden announced 18 November 2025.",
    more_urls=["https://www.eurohpc-ju.europa.eu/contract-signed-alice-recoque-europes-new-exascale-supercomputer-2025-11-18_en",
               "https://www.genci.fr/actualites/press-release-signature-hosting-agreement-second-european-exascale-supercomputer-alice"])
add("EU-014", "European Commission / European Investment Bank", C2, "2025-10-22", "Commission and EIB Group memorandum on financing AI gigafactories",
    "Cooperate on EIB Group financing for AI gigafactories alongside the InvestAI fund.", "gigafactory", None, None, None, "not stated",
    "https://www.eib.org/en/press/all/2025-491-eib-group-and-european-commission-join-forces-to-finance-ai-gigafactories",
    part_of="EU-002", tier="institution",
    notes="Memorandum of understanding. The source states no amount.")
