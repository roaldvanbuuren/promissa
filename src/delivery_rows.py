"""Delivery evidence rows. One row per commitment checked. Rows not listed here were not checked (see gaps.md).

status: delivered | partly delivered | in progress | no evidence found | withdrawn | re-announced
amount_evidenced is only filled when the cited source states an amount for what was delivered, allocated or awarded.
Every URL below was opened or returned by a search in the working session; URLs that failed to load were dropped.
"""
CHECKED = "2026-11-09"
D = []

def d(id, status, evidence_type, summary, url, evidence_date=None, amount=None, cur=None, amount_basis=None,
      more=None, see=None, notes=None):
    D.append(dict(id=id, status=status, evidence_type=evidence_type, summary=summary,
                  amount_evidenced=amount, currency=cur if amount is not None else None,
                  amount_evidenced_basis=amount_basis if amount is not None else None,
                  evidence_url=url, evidence_date=evidence_date, date_checked=CHECKED,
                  more_urls=more or [], see=see, notes=notes))

NAO = "https://www.nao.org.uk/wp-content/uploads/2026/03/DSITs-investment-in-research-infrastructure.pdf"
BRI = "https://www.bristol.ac.uk/research/centres/bristol-supercomputing/articles/2025/isambard-ai-launches-july-2025.html"
OYO = "https://www.gov.uk/government/publications/ai-opportunities-action-plan-one-year-on/ai-opportunities-action-plan-one-year-on"
ROAD = "https://www.gov.uk/government/publications/uk-compute-roadmap/uk-compute-roadmap"
GENCI25 = "https://www.genci.fr/sites/default/files/brique/fichier/07-2026/GB-GENCI-RA2025-200x260-BD_2.pdf"
GENCI24 = "https://www.genci.fr/sites/default/files/brique/fichier/12-2025/VF%20GENCI-RA2024_EN_BD5%20dble.pdf"
NLKB = "https://www.rijksoverheid.nl/documenten/2025/10/13/kamerbrief-honorering-eu-financiering-voor-de-ai-fabriek-in-groningen"

# ---------------- United Kingdom ----------------
d("UK-001", "partly delivered", "facility operating",
  "Isambard-AI in Bristol is operating as part of the AI Research Resource, while the Edinburgh national supercomputer is funded but not yet operating.",
  BRI, "2025-07", more=[NAO, ROAD],
  notes="Components are assessed in UK-003, UK-004 and UK-005. No single amount is recorded because the component figures in the sources overlap with the roughly £900 million.")
d("UK-003", "in progress", "audit report",
  "The Department for Science, Innovation and Technology has allocated £750 million to build the Edinburgh national supercomputer and run it for five years; the National Audit Office reports it is not yet operating and expects a gap after ARCHER2 closes.",
  NAO, "2026-03-13", 750_000_000, "GBP", "departmental allocation including contingency, as reported by the National Audit Office",
  more=[ROAD],
  notes="Evidence for the Edinburgh system is held here once; UK-012 is its re-announcement. The Compute Roadmap says the system is expected online in early 2027, which is a plan, not delivery.")
d("UK-004", "partly delivered", "facility operating",
  "The first phase of the AI Research Resource is running: Isambard-AI launched in July 2025 and Dawn in Cambridge is part of the resource.",
  BRI, "2025-07", more=[OYO],
  notes="The £300 million total is not evidenced. The £225 million for Isambard-AI is recorded under UK-005. Accounts of how this £300 million relates to the £900 million in UK-001 differ (see gaps.md).")
d("UK-005", "delivered", "facility operating",
  "Isambard-AI launched in Bristol in July 2025 with 5,448 NVIDIA superchips and is allocating compute to researchers and companies.",
  BRI, "2025-07", 225_000_000, "GBP", "investment figure stated by the University of Bristol, the host institution; not a ledger line",
  more=["https://www.bristol.ac.uk/news/2025/november/spin-out-supercomputer.html"])
d("UK-008", "in progress", "progress report by the announcing body",
  "The government's one-year report describes £187 million as committed to TechFirst; the report distinguishes committed money from spent money and no spend figure was read.",
  OYO, "2026-01-29")
d("UK-011", "in progress", "progress report by the announcing body",
  "The one-year report states that £2 billion was committed to expand UK compute twentyfold by 2030; the AI Research Resource has launched with a first phase, and no spend figure or contract awards for the later tranches were read.",
  OYO, "2026-01-29", more=[ROAD],
  notes="The Compute Roadmap was first published in July 2025 and last updated on 23 April 2026.")
d("UK-012", "re-announced", "audit report",
  "Re-announcement of the Edinburgh supercomputer first announced in 2023; delivery evidence is recorded once, under UK-003.",
  NAO, "2026-03-13", see="UK-003")
d("UK-013", "in progress", "progress report by the announcing body",
  "The Sovereign AI Unit has provided £8 million of seed funding to the OpenBind structural dataset consortium; the £500 million is a ceiling, and no investment total was found.",
  OYO, "2026-01-29", 8_000_000, "GBP", "seed funding stated in the government's one-year report",
  more=[ROAD])
d("UK-016", "in progress", "progress report by the announcing body",
  "The government confirmed in January 2026 that it will procure a sixfold capacity increase for Dawn in Cambridge by spring 2026; completion was not evidenced.",
  OYO, "2026-01-29")

# ---------------- European Union ----------------
IT4 = "https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-boost-ai-capabilities-it4lia-ai-factory-2026-04-22_en"
d("EU-003", "partly delivered", "grant or contract award",
  "The first AI Factories have offered services since April 2025 on existing systems; contracts for new systems were signed in March 2026 (Germany) and April 2026 (Sweden, Italy).",
  IT4, "2026-04-22", 319_760_000, "EUR",
  "sum of two total budgets stated in signed-contract releases: €290 million (IT4LIA, Italy) and €29.76 million (Mimer, Sweden); each is 50% EuroHPC and 50% national; covers two of the seven factories",
  more=["https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en",
        "https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en"],
  notes="The €1.5 billion headline is not evidenced in full. HammerHAI's system delivery was planned for the second quarter of 2026 and operation for the second half of 2026; no operating date was found.")
d("EU-004", "in progress", "progress report by the announcing body",
  "EuroHPC selected six additional AI Factory sites on 12 March 2025 (Austria, Bulgaria, France, Germany, Poland, Slovenia) and lists 19 AI Factories; no contract values for this wave were read.",
  "https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en", "2025-03-12",
  more=["https://www.eurohpc-ju.europa.eu/ai-factories_en"])
d("EU-005", "in progress", "progress report by the announcing body",
  "EuroHPC lists 19 AI Factories and 13 antennas as being implemented; for the Netherlands, one of the later sites, the Dutch government reports that the EU subsidy was awarded in October 2025. Contracts and values for the other sites in this wave were not checked.",
  "https://www.eurohpc-ju.europa.eu/ai-factories_en", None, more=[NLKB],
  notes="Which sites belong to this wave was not checked site by site.")
d("EU-009", "in progress", "progress report by the announcing body",
  "The call opened on 30 July 2026 with a submission deadline of 12 November 2026; selection is expected in early 2027 and no gigafactory exists yet.",
  "https://www.eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en", "2026-07-30")
d("EU-013", "in progress", "grant or contract award",
  "EuroHPC and the host consortium signed the supply contract with Eviden, announced on 18 November 2025; installation began in 2026 and GENCI expects commissioning in 2027.",
  "https://www.eurohpc-ju.europa.eu/contract-signed-alice-recoque-europes-new-exascale-supercomputer-2025-11-18_en", "2025-11-18",
  354_800_000, "EUR", "total budget for acquisition stated in the contract-signing release (EuroHPC 50%)",
  more=[GENCI25, "https://www-hpc.cea.fr/en/AliceRecoque.html"],
  notes="This is a budget, not the contract price, which the release does not state.")

# ---------------- France ----------------
FR21 = "https://www.enseignementsup-recherche.gouv.fr/fr/france-2030-l-ia-comme-un-accelerateur-et-un-differentiateur-d-innovation-96213"
FRPDF = "https://www.info.gouv.fr/upload/media/content/0001/10/f111886ce0bd3882137dc5eea7222d0f6c0b37b4.pdf"
d("FR-001", "partly delivered", "grant or contract award",
  "A press release of 22 May 2024 names nine winning AI Clusters sharing €360 million from France 2030, against the €500 million originally called.",
  FRPDF, "2024-05-22", 360_000_000, "EUR", "award total stated by the government for the nine winners", more=[FR21],
  notes="The sources read do not say whether the other €140 million was awarded elsewhere or left unawarded. They also do not say whether the clusters are installed.")
d("FR-002", "partly delivered", "grant or contract award",
  "Seven new winners of the generative AI digital commons call were announced in May 2024; the sources read give no award amount.",
  FR21, "2024-05-21", notes="The original call amount of €40 million is not matched to awards.")
d("FR-003", "delivered", "facility operating",
  "GENCI reports that Jean Zay's computing power was quadrupled and the Jean Zay 4 extension inaugurated in May 2025.",
  GENCI25, "2025-05-14", 40_000_000, "EUR",
  "investment of about €40 million stated in GENCI's 2024 annual report for the 2024 Jean Zay extension, funded by France 2030; assumed to be the same extension (moderate confidence)",
  more=[GENCI24])

# ---------------- Germany ----------------
d("DE-001", "in progress", "budget line",
  "The ministry's own summary shows AI budget lines of €427.2 million for 2023 and €483.3 million for 2024 (planned figures); outturn for those years and budget lines for 2025 and 2026 were not found.",
  "https://www.bmftr.bund.de/SharedDocs/Downloads/DE/2023/230823-executive-summary-ki-aktionsplan.pdf", "2023-11",
  910_500_000, "EUR", "sum of planned budget lines for 2023 and 2024, not outturn",
  notes="The sum is arithmetic on two stated figures. It is a budget, not spending.")
d("DE-003", "in progress", "progress report by the announcing body",
  "The digital ministry reports that 25 of the 28 measures had started and four were completed six months after the strategy was adopted.",
  "https://bmds.bund.de/aktuelles/pressemitteilungen/detail/halbjahresbilanz-rechenzentrumsstrategie-wir-setzen-den-fahrplan-zuegig-um", "2026-09-18",
  notes="Self-reported by the ministry responsible for the strategy. No independent check found.")
d("DE-004", "in progress", "progress report by the announcing body",
  "The research ministry states that the EU competition for gigafactory sites opened on 30 July 2026; no German consortium has been selected.",
  "https://www.bmftr.bund.de/SharedDocs/Kurzmeldungen/DE/2026/07/300726-ai-gigafactories.html", "2026-07-30",
  more=["https://www.eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en"])
d("DE-005", "in progress", "progress report by the announcing body",
  "The digital ministry's September 2026 release says €30.7 million flows until 2030 into new AI computing capacity for national high-performance computing; no grant award, contract or operating system was found.",
  "https://bmds.bund.de/aktuelles/pressemitteilungen/detail/halbjahresbilanz-rechenzentrumsstrategie-wir-setzen-den-fahrplan-zuegig-um", "2026-09-18",
  notes="The release restates the commitment. No amount is recorded as evidenced because restating the figure is not evidence of delivery. Not searched: the federal budget plan and Bundestag documents.")

# ---------------- Italy ----------------
d("IT-001", "partly delivered", "progress report by the announcing body",
  "CDP Venture Capital reports more than €300 million of the AI envelope already allocated, supporting about 150 startups and about 20 funds.",
  "https://www.cdpventurecapital.it/en/news.page?contentId=COM52473", "2026-06-12", 300_000_000, "EUR",
  "lower bound stated by CDP Venture Capital (over €300 million); self-reported by the investor",
  notes="A Council of Ministers communiqué seen only as a search snippet gives €313 million in its annexes; the page could not be loaded to confirm.")
d("IT-003", "re-announced", "progress report by the announcing body",
  "The law authorising up to €1 billion in equity and quasi-equity investments through CDP Venture Capital restates the envelope in IT-001; evidence is recorded once, under IT-001.",
  "https://innovazione.gov.it/notizie/interventi/intelligenza-artificiale-si-alla-legge-c-e-un-miliardo/", "2025-09-18", see="IT-001")

# ---------------- Netherlands ----------------
d("NL-001", "partly delivered", "progress report by the announcing body",
  "SURF reported on 26 February 2026 that the language model is fully trained and that ten launching customers get early access in the first quarter, with a wider rollout in the autumn.",
  "https://www.surf.nl/en/news/towards-transparent-fair-and-verifiable-use-of-ai", "2026-02-26",
  more=["https://ventures.tno.nl/portfolio/gpt-nl/"],
  notes="The page does not state a budget, so no amount is recorded. The page does not state the year of the autumn rollout (context points to 2026).")
d("NL-004", "in progress", "progress report by the announcing body",
  "A Cabinet letter to Parliament of 13 October 2025 reports that EuroHPC awarded the EU subsidy (about €71.7 million) against a total investment of about €202.6 million; the expertise centre starts in 2026 and the supercomputer is expected at full capacity in 2027.",
  NLKB, "2025-10-13",
  more=["https://www.tweedekamer.nl/kamerstukken/brieven_regering/detail?id=2025Z22569&did=2025D53584",
        "https://www.surf.nl/en/news/netherlands-gets-ai-factory-european-funding-awarded"],
  notes="The letter gives national and regional money together (about €130.9 million), so the Cabinet's own €70 million is not separated and no amount is recorded.")

# ---------------- added after second pass ----------------
d("UK-017", "in progress", "parliamentary answer",
  "A written parliamentary answer of 12 October 2026 states that the AI Security Institute has been allocated £240 million over the Spending Review period to 2029-30, with 243 staff; this is an allocation, not spending.",
  "https://questions-statements.parliament.uk/written-questions/detail/2026-10-12/33991/", "2026-10-12",
  notes="Whether this allocation includes the additional £120 million in the commitment is not established by the answer, so no amount is recorded against that claim.")
d("UK-009", "in progress", "progress report by the announcing body",
  "The one-year report states that over one million free AI courses have been delivered; the count is of courses, not of people trained, so it cannot be compared with the target of 7.5 million workers.",
  OYO, "2026-01-29",
  notes="No amount is stated for this commitment.")
