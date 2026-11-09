from common import row
J = "France"
R = []

# Governments by date (head of government). Dates are appointment dates.
GOV_FR = [("2022-05-16", "Borne government"), ("2024-01-09", "Attal government"),
          ("2024-09-21", "Barnier government"), ("2024-12-13", "Bayrou government"),
          ("2025-09-10", "Lecornu government")]
def fr_gov(date):
    g = None
    for start, name in GOV_FR:
        if date[:10] >= start:
            g = name
    return g

def add(id, body, date, *a, **k):
    R.append(row(id, J, body, fr_gov(date if len(date) > 7 else date + "-15"), date, *a, **k))

PR23 = "https://presse.economie.gouv.fr/16062023-942-france-2030-emmanuel-macron-annonce-un-effort-sans-precedent-de-la-france-en-intelligence-artificielle/"
add("FR-001", "Secrétariat général pour l'investissement (France 2030)", "2023-06-16", "IA-Cluster call for research and training hubs",
    "Fund 5 to 10 world-class AI research and training hubs with €500 million from France 2030.", "institute",
    500_000_000, "EUR", "€500 million", "not stated", PR23,
    notes="Announced at VivaTech 2023. Nine winners and €360 million awarded on 21 May 2024 (see delivery.json, not repeated here).")
add("FR-002", "Bpifrance for the State (France 2030)", "2023-06-16", "Call for projects: digital commons for generative AI",
    "Fund shared datasets and test bases for generative AI through a €40 million call for projects run by Bpifrance.", "funding programme",
    40_000_000, "EUR", "€40 million", "not stated", PR23)
add("FR-003", "GENCI / CNRS", "2023-06-16", "Jean Zay supercomputer power increase",
    "Increase the computing power of the Jean Zay supercomputer and open it more widely to AI development.", "compute",
    None, None, None, "not stated", PR23,
    notes="The press release gives no amount. GENCI's 2024 annual report says the Jean Zay extension was financed by France 2030 in response to a presidential announcement of 'May 2023', which differs from the 16 June 2023 date of the press release. See gaps.md.",
    more_urls=["https://www.genci.fr/sites/default/files/brique/fichier/12-2025/VF%20GENCI-RA2024_EN_BD5%20dble.pdf"])
add("FR-004", "Bpifrance for the State (France 2030)", "2024-04-04", "Call for projects: accelerating generative AI use in the economy",
    "Open a France 2030 call for projects, run by Bpifrance, for consortia of generative AI developers and users.", "funding programme",
    None, None, None, "not stated", "https://presse.economie.gouv.fr/?p=128022",
    notes="The release states no amount for the call.")
add("FR-005", "Presidency / Secrétariat général pour l'investissement", "2024-05-21", "National AI strategy: nearly €2.5 billion from France 2030",
    "Dedicate nearly €2.5 billion of France 2030 to AI under the national AI strategy.", "funding programme",
    2_500_000_000, "EUR", "nearly €2.5 billion", "cumulative since 2018",
    "https://www.info.gouv.fr/actualite/france-2030-lia-comme-un-accelerateur-et-un-differentiateur-dinnovation",
    counted=False,
    notes="Cumulative envelope that includes the 2018 to 2022 first phase (about €1.5 billion) and amounts already announced in FR-001 and FR-002. The sources do not split it into new and earlier money, so it is listed but not added to the promised total. Official pages disagree on phase 2: €1 billion (entreprises.gouv.fr) and €1.5 billion (presse.economie.gouv.fr, 4 April 2024). See gaps.md.",
    more_urls=["https://www.enseignementsup-recherche.gouv.fr/fr/france-2030-l-ia-comme-un-accelerateur-et-un-differentiateur-d-innovation-96213",
               "https://www.economie.gouv.fr/actualites/strategie-nationale-intelligence-artificielle"])
add("FR-006", "Presidency", "2025-02", "AI Action Summit: €109 billion of investment in AI in France",
    "Announce an investment of €109 billion in AI in France.", "funding programme",
    109_000_000_000, "EUR", "€109 billion", "not stated",
    "https://www.enseignementsup-recherche.gouv.fr/fr/intelligence-artificielle-de-quoi-parle-t-91190",
    precision="month", basis="mobilisation", counted=False,
    notes="The source states the headline figure without a public and private split. Treated as a mobilisation figure and kept out of the promised total until a breakdown of the public share is found. See gaps.md.")
