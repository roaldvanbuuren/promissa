from common import row, uk_gov
J = "United Kingdom"
G = "https://www.gov.uk/government/"
R = []
def add(*a, **k):
    a = list(a); a[3] = uk_gov(a[4]); R.append(row(*a, **k))

# --- Sunak government (2023 to 4 Jul 2024)
add("UK-001", J, "HM Treasury / DSIT", None, "2023-03-15", "Exascale supercomputer and AI Research Resource",
    "Invest in the region of £900 million to build an exascale supercomputer and set up an AI Research Resource.",
    "compute", 900_000_000, "GBP", "in the region of £900 million", "initial investments from 2023; end date not stated",
    G+"publications/spring-budget-2023/spring-budget-2023-html",
    notes="Umbrella for the Edinburgh exascale system (UK-003) and the AI Research Resource (UK-004). Subject to business case process.",
    more_urls=[G+"news/government-commits-up-to-35-billion-to-future-of-tech-and-science"])
add("UK-002", J, "DSIT", None, "2023-04-24", "Foundation Model Taskforce (later Frontier AI Taskforce)",
    "Provide £100 million of start-up funding for a taskforce on safe and reliable foundation models.",
    "institute", 100_000_000, "GBP", "£100 million initial start-up funding", "not stated",
    G+"news/initial-100-million-for-expert-taskforce-to-help-uk-build-and-adopt-next-generation-of-safe-ai",
    notes="Announced as additional to UK-001. Renamed Frontier AI Taskforce in 2023; AI Safety Institute followed.",
    more_urls=[G+"news/industry-and-national-security-heavyweights-to-power-uks-frontier-ai-taskforce"])
add("UK-003", J, "DSIT", None, "2023-10-09", "Exascale computer at the University of Edinburgh",
    "Build a national exascale supercomputer at the University of Edinburgh.",
    "compute", None, "GBP", "no amount stated (described as part of the £900 million)", "not stated",
    G+"news/game-changing-exascale-computer-planned-for-edinburgh", part_of="UK-001",
    notes="Official page gives no Edinburgh-specific amount. Press (Computer Weekly, UKTN, TechRepublic) later reported £800 million; not used as the amount here.")
add("UK-004", J, "DSIT / UKRI", None, "2023-11-01", "AI Research Resource, first phase",
    "Launch the first phase of a national AI Research Resource (Isambard-AI in Bristol, Dawn in Cambridge).",
    "compute", 300_000_000, "GBP", "£300 million", "not stated",
    "https://www.ukri.org/news/300-million-to-launch-first-phase-of-new-ai-research-resource/",
    counted=False, part_of="UK-001",
    notes="Relationship to the £900 million umbrella is disputed in sources (one reports AIRR 'tripled from £100m to £300m'); see gaps.md. Not added to totals.",
    more_urls=["https://silicon.co.uk/cloud/server/ai-safety-summit-2023-uk-to-invest-225m-for-ai-supercomputer-537233"])
add("UK-005", J, "DSIT / University of Bristol", None, "2023-11-01", "Isambard-AI supercomputer, Bristol",
    "Fund the Isambard-AI supercomputer at the University of Bristol.",
    "compute", 225_000_000, "GBP", "£225 million", "not stated",
    "https://bristol.ac.uk/news/2023/november/supercomputer-announcement.html",
    counted=False, part_of="UK-004", tier="institution",
    more_urls=["https://www.cnbc.com/2023/11/01/uk-to-invest-273-million-in-turing-ai-supercomputer.html"])
add("UK-006", J, "DSIT / DHSC", None, "2023-10-29", "AI in life sciences and healthcare mission",
    "Fund a £100 million mission to accelerate AI in life sciences and healthcare.",
    "funding programme", 100_000_000, "GBP", "£100 million", "not stated",
    G+"news/new-100-million-fund-to-capitalise-on-ais-game-changing-potential-in-life-sciences-and-healthcare")
add("UK-007", J, "HM Treasury / DSIT", None, "2023-11-22", "Further AI Research Resource funding (Autumn Statement 2023)",
    "Add £500 million of further funding for the AI Research Resource.",
    "compute", 500_000_000, "GBP", "£500 million (as reported)", "not stated",
    "https://www.computerweekly.com/news/366599760/Labour-axes-13bn-AI-funding-promised-by-the-Conservatives",
    basis="press_reported", counted=False, tier="press",
    notes="Press-reported only; primary Autumn Statement text not retrieved. Reported as shelved in August 2024. See gaps.md.",
    more_urls=["https://www.techrepublic.com/article/uk-government-ai-funding-scrapped/"])
# --- Starmer government
add("UK-008", J, "DSIT / DfE", None, "2025-06-09", "TechFirst skills programme",
    "Invest £187 million in tech and AI skills across schools, graduates, experts and local businesses.",
    "skills", 187_000_000, "GBP", "£187 million", "not stated",
    G+"news/pm-launches-national-skills-drive-to-unlock-opportunities-for-young-people-in-tech")
add("UK-009", J, "DSIT", None, "2025-06-09", "Industry partnership to train 7.5 million workers in AI skills",
    "Partner with industry so that 7.5 million UK workers gain essential AI skills by 2030.",
    "skills", None, "GBP", "no amount stated", "to 2030",
    G+"news/pm-launches-national-skills-drive-to-unlock-opportunities-for-young-people-in-tech")
add("UK-010", J, "DSIT", None, "2025-06-09", "Twenty-fold expansion of the AI Research Resource",
    "Provide over £1 billion to expand AI Research Resource compute twenty-fold by 2030.",
    "compute", 1_000_000_000, "GBP", "over £1 billion", "by 2030",
    G+"publications/uk-compute-roadmap/uk-compute-roadmap", counted=False, part_of="UK-011",
    notes="Announced by the Prime Minister at London Tech Week; amount as restated in the Compute Roadmap (17 Jul 2025).",
    more_urls=["https://www.computerweekly.com/news/366625856/UK-government-recommits-to-Edinburgh-supercomputer-plan-with-750m-funding-pledge"])
add("UK-011", J, "DSIT / UKRI", None, "2025-07-17", "Compute Roadmap: up to £2 billion of public compute to 2030",
    "Invest up to £2 billion in public compute infrastructure between 2025 and 2030.",
    "compute", 2_000_000_000, "GBP", "up to £2 billion", "to 2030",
    G+"publications/uk-compute-roadmap/uk-compute-roadmap",
    notes="Roadmap states its £1bn, £750m and milestone figures overlap and must not be added.")
add("UK-012", J, "DSIT / HM Treasury", None, "2025-06-11", "National supercomputer at the University of Edinburgh (restored)",
    "Provide up to £750 million for a new national supercomputer at the University of Edinburgh.",
    "compute", 750_000_000, "GBP", "up to £750 million", "system planned online 2027",
    G+"news/scotland-to-host-uks-national-supercomputer-as-chancellor-confirms-750-million-investment",
    counted=False, part_of="UK-011", reannounces="UK-003",
    notes="Revives the Edinburgh exascale project shelved in August 2024. Treated as a re-announcement of UK-003 (judgement call; see README).")
add("UK-013", J, "DSIT / British Business Bank", None, "2025-06-11", "Sovereign AI Unit",
    "Back UK AI companies through a Sovereign AI Unit funded with up to £500 million.",
    "funding programme", 500_000_000, "GBP", "up to £500 million", "Spending Review 2025 period",
    G+"publications/uk-compute-roadmap/uk-compute-roadmap",
    more_urls=[G+"publications/ai-opportunities-action-plan-one-year-on/ai-opportunities-action-plan-one-year-on"],
    notes="Unit first announced in the AI Opportunities Action Plan; the £500m figure is tied to the Spending Review in the Roadmap.")
add("UK-014", J, "AI Security Institute", None, "2025-01-01", "AI Security Institute Alignment Project",
    "Fund the Alignment Project for AI alignment research with £15 million.",
    "institute", 15_000_000, "GBP", "£15m", "not stated",
    "https://www.aisi.gov.uk/blog/our-2025-year-in-review", precision="year",
    notes="Year-level date only on the cited page.")
add("UK-015", J, "AI Security Institute", None, "2025-01-01", "AI Security Institute Systemic Safety Grants",
    "Fund Systemic Safety Grants of £8 million.", "institute", 8_000_000, "GBP", "£8m", "not stated",
    "https://www.aisi.gov.uk/blog/our-2025-year-in-review", precision="year", counted=True)
add("UK-016", J, "DSIT", None, "2026-01-26", "Dawn supercomputer upgrade, Cambridge",
    "Invest £36 million to expand Dawn's AI capacity sixfold (£16m DSIT, £20m UKRI).",
    "compute", 36_000_000, "GBP", "£36 million", "capacity by spring 2026",
    G+"news/cambridge-supercomputer-set-to-get-6-times-more-powerful-as-government-backs-british-ai-innovation",
    counted=False, part_of="UK-011")
# --- Burnham government: 24 Oct 2026 package
P = G+"news/chancellor-unveils-britains-ambitious-plan-for-ai"
add("UK-017", J, "HM Treasury", None, "2026-10-24", "AI Security Institute additional funding",
    "Provide an additional £120 million to the AI Security Institute.", "institute", 120_000_000, "GBP", "£120 million additional", "not stated", P)
add("UK-018", J, "HM Treasury / Cabinet Office", None, "2026-10-24", "National AI Biosecurity Initiative",
    "Fund a £165 million initiative including an AI Biosecurity Lab and biosurveillance.", "funding programme", 165_000_000, "GBP", "£165 million", "not stated", P)
add("UK-019", J, "Cabinet Office", None, "2026-10-24", "AI Biosecurity Lab",
    "Establish an AI Biosecurity Lab with £100 million of government funding.", "institute", 100_000_000, "GBP", "£100 million", "2027-28 to 2029-30",
    G+"publications/budget-2026-document/budget-2026-html", counted=False, part_of="UK-018",
    more_urls=[G+"news/introducing-the-ai-biosecurity-lab"])
add("UK-020", J, "Cabinet Office", None, "2026-10-24", "AI Biosecurity Lab: OpenAI and Anthropic commitments",
    "OpenAI to provide £100m in compute and credits and Anthropic up to £100m in credits and support to the AI Biosecurity Lab.",
    "partnership", 200_000_000, "GBP", "up to £200 million (company commitments)", "not stated",
    G+"news/introducing-the-ai-biosecurity-lab", basis="company", counted=False, part_of="UK-019",
    notes="Value stated by government; funded by the companies, so not counted as government spending.")
for i,(t,p,a,ty) in enumerate([
 ("National Cyber Shield","Fund a £60 million National Cyber Shield using agentic AI for cyber defence.",60,"funding programme"),
 ("National Exposure and Real-Time Vulnerability (NERV) Centre","Fund a £70 million centre using AI to find cyber vulnerabilities in critical infrastructure.",70,"institute"),
 ("Sovereign AI Fund top-up","Add £60 million to the Sovereign AI Fund with a physical and industrial AI focus.",60,"funding programme"),
 ("Sovereign AI R&D Procurement Scheme","Add £60 million for an AI R&D procurement scheme in health, care and AI security.",60,"funding programme"),
 ("UK Advanced Chip Design Academy","Fund a £18 million chip design academy.",18,"skills"),
 ("AI Challenge Prize","Fund a £15 million AI challenge prize, first award in health.",15,"funding programme"),
 ("AI Economics Institute","Fund an AI Economics Institute with £23 million over three years.",23,"institute"),
 ("Local AI partnerships with Mayoral Strategic Authorities","Provide £30 million for local AI partnerships.",30,"funding programme"),
 ], start=21):
    pe = "three years" if "Economics" in t else None
    add(f"UK-0{i}", J, "HM Treasury", None, "2026-10-24", t, p, ty, a*1_000_000, "GBP", f"£{a} million", pe, P)
add("UK-029", J, "HM Treasury", None, "2026-10-24", "Work on how AI will reshape jobs and industry",
    "Fund £10 million per year of work on how AI will reshape jobs and industry.", "funding programme", 10_000_000, "GBP", "£10m per year", "per year; years not stated", P)
add("UK-030", J, "HM Treasury", None, "2023-03-15", "Manchester Prize for AI research",
    "Award a £1 million prize every year for ten years for progress in critical areas of AI.",
    "funding programme", 10_000_000, "GBP", "£1 million a year for 10 years", "10 years",
    G+"speeches/spring-budget-2023-speech",
    notes="Total of £10 million is 10 x the stated annual £1 million (derived, not separately stated).",
    more_urls=[G+"publications/spring-budget-2023/spring-budget-2023-html"])
