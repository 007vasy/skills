# UAE OSINT / government sources

A catalog of **public, government, and open-source** feeds that can ground an outside-in picture of the UAE. Built to feed quarterly re-runs of [`residuality-erm-examples/uae.md`](../residuality-erm-examples/uae.md) — Abu Dhabi as fiscal engine, Dubai as throughput engine, the federation as licence.

This is a **source catalog**, not a country brief and not a people-search kit. Each entry says what fact it can actually give you, how often it updates, and where it lies.

| File | What it is |
|---|---|
| [sources-uae-gov.md](sources-uae-gov.md) | Federal + emirate official portals, SOEs, SWFs, regulators |
| [sources-foreign-gov.md](sources-foreign-gov.md) | US / UK / EU / IGO statistical and policy sources |
| [sources-osint.md](sources-osint.md) | Investigative, commercial, technical OSINT (AIS, satellite, registries) |
| [erm-coverage.md](erm-coverage.md) | Maps sources → residuality assumptions A1–A10, chaotic nodes, re-run triggers |
| [ai-kg-projects.md](ai-kg-projects.md) | UAE AI program map + stack-ranked KG/satellite analytic products |
| [pitch-stack.md](pitch-stack.md) | Personal pitch stack (Graph Shaman × FedAI / Authority / 80k) |

Catalog compiled August 2026. Portals rename; check the live URL before citing.

---

## Start here (three tiers)

Do not open fifty tabs. These fifteen sources cover most of the operating model.

**Tier 1 — UAE ground truth (official numbers)**

1. [FCSC](https://fcsc.gov.ae) / [UAE Numbers](https://uaestat.fcsc.gov.ae/en) — national accounts, population, competitiveness
2. [Bayanat](https://bayanat.ae) — federal open-data catalog (~3,500 datasets, 50+ entities)
3. [CBUAE latest statistics](https://www.centralbank.ae/en/research-and-statistics/latest-statistics/) — monthly bulletin, BoP, FX reserves, bank FX
4. [SCAD](https://scad.gov.ae) — Abu Dhabi GDP, population, Bayaan
5. [Dubai Pulse](https://www.dubaipulse.gov.ae) / [Data.Dubai](https://www.digitaldubai.ae/apps-services/details/data.dubai) — Dubai official statistics and registers

**Tier 2 — outside-in cross-check (do not skip)**

6. [IMF UAE country page](https://www.imf.org/en/countries/are) — 2025 Article IV (8 Dec 2025) is the best single macro document; Jul 2026 staff visit is the latest colour
7. [EIA UAE Country Analysis Brief](https://www.eia.gov/international/content/analysis/countries_long/United_Arab_Emirates/) — updated 28 Jul 2026; oil, gas, Hormuz, Fujairah, Barakah
8. [FATF UAE page](https://www.fatf-gafi.org/en/countries/detail/%C3%89mirats-arabes-unis.html) — grey-list exit Feb 2024; 5th-round onsite possibly mid-2026

**Tier 3 — live sensors (the operating model as it moves)**

9. [DLD real-estate data](https://dubailand.gov.ae/en/open-data/real-estate-data/) — transactions, rents, off-plan (S-14 / C-12)
10. ADNOC listed-sub investor relations (Gas, Drilling, Logistics, Distribution) — barrels and capex the parent will not itemise
11. [ADCOP / Fujairah pipeline](https://www.adnoc.ae/en/adnoc-pipelines/about-us/who-we-are) + AIS at Fujairah and Jebel Ali — whether A2 is a pipe or a press release
12. [OFAC SDN](https://ofac.treasury.gov) — US secondary-sanctions hits on UAE names
13. [Emirates Group annual reports](https://www.emirates.com/english/about-us/financial-transparency/annual-reports/) + DP World annual report — aviation and Jebel Ali throughput
14. [Mubadala investors](https://www.mubadala.com/en/investors/overview) + [ADIA Review](https://www.adia.ae/en/publications) + [ICD financials](https://icd.gov.ae/financial-information/) — the visible slice of the SWF stack
15. [MOHRE Labour Market Observatory](https://observatory.mohre.gov.ae/en) — the expatriate operating system (A3)

---

## Rules of use

1. **Arabic is often richer.** Many federal and emirate pages publish a fuller Arabic statistical set. If English looks thin, switch language before concluding the number does not exist.
2. **Output ≠ revenue.** FCSC and media will quote non-oil *GDP share* (~79%). The residuality model cares about oil *fiscal share*. IMF Article IV fiscal tables are the correction.
3. **SWF, court, and security internals are dark.** ADIA publishes allocation *ranges*, not line items. Succession loyalty maps, desal inventory-days, and correspondent-bank de-risking memos are not in open sources. Do not invent them — flag the gap, as `uae.md` already does for A4/A6.
4. **Some portals want UAE Pass.** Trade-registry UBO detail, some ICP services, and a few emirate cadastral tools are residency-gated. Note access on the card; do not scrape around the gate.
5. **People-lookup is out of scope.** Phones, plates, Getcontact, yellow-pages person search: see [OSINT-Tools-Emirates](https://github.com/paulpogoda/OSINT-Tools-Emirates). This folder is for the *enterprise*, not for doxxing residents.
6. **Official stats are a product.** Treat FCSC, SCAD, and DLD as primary but politically framed. Always pair with IMF / EIA / FATF before a number enters the ERM file.

---

## How this feeds `uae.md`

- **Step 1 (naive model):** Tier 1 + EIA + IMF for value-chain magnitudes.
- **Step 2–3 (stressors / residues):** Tier 3 sensors and foreign-gov pages for whether a shock is live (Hormuz, FATF, DLD crash, OFAC).
- **Step 7 (cadence):** [erm-coverage.md](erm-coverage.md) maps each re-run trigger to a watch source.

Do not download bulk datasets into this repo. Cite the live URL and the publication date.
