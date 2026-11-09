from common import row
J = "Italy"
R = []

def add(id, body, date, *a, **k):
    R.append(row(id, J, body, "Meloni government", date, *a, **k))

CDP = "https://www.cdpventurecapital.it/en/news.page?contentId=COM34690"
add("IT-001", "CDP Venture Capital (state-controlled investor), with the Ministry of Enterprises and Made in Italy", "2024-04-08",
    "CDP Venture Capital: €1 billion for AI",
    "Dedicate €1 billion of CDP Venture Capital resources to AI: €120 million for technology transfer, €580 million for startups and €300 million for mature companies.", "funding programme",
    1_000_000_000, "EUR", "€1 billion", "2024 to 2028 business plan", CDP, tier="institution",
    notes="CDP Venture Capital is a state-controlled investment company, so the source tier is 'institution', not a ministry. The Prime Minister thanked CDP for the €1 billion in an undated video message (governo.it page could not be loaded; see gaps.md). A later CDP release describes the same €1 billion as a €500 million AI fund plus €500 million of co-investments, a different split.",
    more_urls=["https://www.cdpventurecapital.it/en/news.page?contentId=COM36210"])
add("IT-002", "CDP Venture Capital / OpenAI", "2024-10-02", "CDP Venture Capital and OpenAI memorandum of understanding",
    "Cooperate on AI startup investment, mentoring and university training programmes through CDP Venture Capital's Artificial Intelligence Fund.", "partnership",
    None, None, None, "not stated",
    "https://www.cdpventurecapital.it/en/news.page?contentId=COM36210", tier="institution", part_of="IT-001",
    notes="The memorandum states no value of its own; the €1 billion belongs to IT-001.")
add("IT-003", "Parliament and Government (Law 132/2025, article 23)", "2025-09-17", "AI law authorises up to €1 billion of AI investment",
    "Authorise up to €1 billion of equity and quasi-equity investment in AI, cybersecurity and enabling technologies through the venture capital support fund and CDP Venture Capital.", "funding programme",
    1_000_000_000, "EUR", "up to €1 billion", "not stated",
    "https://innovazione.gov.it/notizie/interventi/intelligenza-artificiale-si-alla-legge-c-e-un-miliardo/",
    reannounces="IT-001", counted=False,
    notes="Legislative authorisation of the same €1 billion. The source does not say whether it is new money; a later Council of Ministers communiqué describes it as a share of the venture capital support fund's resources. Final Senate vote on 17 September 2025 is inferred from the word 'yesterday' in an article dated 18 September 2025.")
