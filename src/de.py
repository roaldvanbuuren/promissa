from common import row
J = "Germany"
R = []

GOV_DE = [("2021-12-08", "Scholz government"), ("2025-05-06", "Merz government")]
def de_gov(date):
    g = None
    for start, name in GOV_DE:
        if date[:10] >= start:
            g = name
    return g

def add(id, body, date, *a, **k):
    R.append(row(id, J, body, de_gov(date), date, *a, **k))

BMF = "https://www.bmftr.bund.de/SharedDocs/"
add("DE-001", "Federal Ministry of Education and Research (BMBF)", "2023-08-23", "BMBF AI Action Plan",
    "Invest over €1.6 billion in AI in the legislative period through the BMBF AI Action Plan, almost €500 million of it in 2024.", "funding programme",
    1_600_000_000, "EUR", "over €1.6 billion", "legislative period as stated in 2023",
    BMF + "Pressemitteilungen/DE/2023/08/230823-KI-Aktionsplan.html",
    notes="Presented on 23 August 2023; the full plan was published on 7 November 2023. The BMFTR AI pages (successor ministry) repeat the same sentence for 'the current legislative period' without a date; see gaps.md.",
    more_urls=[BMF + "Pressemitteilungen/DE/2023/11/071123-KI-Aktionsplan.html"])
add("DE-002", "Federal Government (cabinet)", "2025-07-30", "Hightech Agenda Deutschland (AI as one of six key technologies)",
    "Adopt a research and technology agenda that names AI as one of six key technologies, with flagship initiatives for each.", "funding programme",
    None, None, None, "legislative period",
    BMF + "Pressemitteilungen/DE/2025/07/300725-HTA.html",
    notes="The Federal Research Ministry later states at least €18 billion for the whole agenda across all six technologies. No AI share is given, so no amount is recorded here.",
    more_urls=[BMF + "Kurzmeldungen/DE/2025/09/260925-haushalt-26-1-lesung.html"])
add("DE-003", "Federal Ministry for Digital Affairs and State Modernisation (BMDS)", "2026-03-18", "National Data Centre Strategy",
    "Double data centre capacity in Germany and at least quadruple AI and high-performance computing capacity by 2030, through 28 measures.", "compute",
    None, None, None, "to 2030",
    "https://www.bundesregierung.de/breg-de/aktuelles/faq-kuenstliche-intelligenz-2458970",
    notes="Cabinet decision date of 18 March 2026 taken from the Federal Government FAQ. The strategy document is dated March 2026 and states targets, not amounts.",
    more_urls=["https://bmds.bund.de/fileadmin/BMDS/Dokumente/Publikationen/260312_BMDS_Template-RZ-Strategie_V2_barrierefrei_final.pdf"])
add("DE-004", "Federal Ministry for Digital Affairs and State Modernisation (BMDS)", "2026-03-18", "Support for at least one AI gigafactory in Germany",
    "Support the build and operation of at least one AI gigafactory in Germany as a public-private partnership with EuroHPC and the Commission.", "gigafactory",
    None, None, None, "not stated",
    "https://bmds.bund.de/fileadmin/BMDS/Dokumente/Publikationen/260312_BMDS_Template-RZ-Strategie_V2_barrierefrei_final.pdf",
    part_of="DE-003",
    notes="Measure 1 of the strategy. The document describes the gigafactory as a primarily commercial project and states no federal amount. The EU call opened at the end of July 2026 (see EU-009).",
    more_urls=["https://www.bmftr.bund.de/SharedDocs/Kurzmeldungen/DE/2026/07/300726-ai-gigafactories.html"])
add("DE-005", "Federal Government (National High Performance Computing)", "2026-09-18", "New AI compute capacity for National High Performance Computing",
    "Provide €30.7 million to 2030 for new AI compute capacity in the National High Performance Computing network.", "compute",
    30_700_000, "EUR", "€30.7 million to 2030", "to 2030",
    "https://bmds.bund.de/aktuelles/pressemitteilungen/detail/halbjahresbilanz-rechenzentrumsstrategie-wir-setzen-den-fahrplan-zuegig-um",
    notes="Date is that of the press release, the first dated source found; the page does not give a decision date or the budget line.",
    more_urls=["https://www.bundesregierung.de/breg-de/aktuelles/faq-kuenstliche-intelligenz-2458970"])
add("DE-006", "Federal Government", "2026-09-18", "IPCEI projects in cloud, AI and data infrastructure",
    "Make around €3 billion available for European flagship projects (IPCEI) in cloud, AI and data infrastructure.", "funding programme",
    3_000_000_000, "EUR", "around €3 billion", "not stated",
    "https://bmds.bund.de/aktuelles/pressemitteilungen/detail/halbjahresbilanz-rechenzentrumsstrategie-wir-setzen-den-fahrplan-zuegig-um",
    counted=False,
    notes="The figure covers cloud, AI and data infrastructure together with no AI split, so it fails the AI-line test and is not added to the promised total. Date is that of the press release; the page gives no first-announcement date. A 2021 federal report also mentions up to €3 billion for two IPCEI, so the money may predate this statement. See gaps.md.")
