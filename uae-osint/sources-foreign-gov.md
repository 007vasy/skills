# Foreign government and IGO sources

Cross-checks on UAE official numbers. Use these before a figure from [sources-uae-gov.md](sources-uae-gov.md) enters the ERM file.

---

## Macro and fiscal (best first document)

### IMF — UAE country page and Article IV

- **Country page:** https://www.imf.org/en/countries/are
- **2025 Article IV:** https://www.imf.org/en/publications/cr/issues/2025/12/08/united-arab-emirates-2025-article-iv-consultation-press-release-staff-report-and-statement-572397  
  Country Report 2025/327, Board date 1 Dec 2025, published 8 Dec 2025. Also on eLibrary: https://www.elibrary.imf.org/view/journals/002/2025/327/article-A001-en.xml
- **Jul 2026 staff visit:** https://www.imf.org/en/news/articles/2026/07/17/pr26250-united-arab-emirates-imf-staff-concludes-visit (7–16 Jul 2026; 2026 AIV still ahead)
- **2025 mission close:** https://www.imf.org/en/news/articles/2025/10/02/pr-25326-united-arab-emirates-imf-staff-completes-2025-article-iv-mission
- **Good for:** Consolidated fiscal (hydrocarbon vs non-hydrocarbon revenue — the A7 test FCSC GDP cannot do); growth; credit/property flags; peg assessment; AML/CFT paragraph; data-adequacy grades (2025 AIV: FSI “A”, external sector raised D→C). Staff explicitly exclude SWF investment income from some fiscal ratios — read the footnotes.
- **Cadence:** Annual AIV (UAE is on the annual cycle). Interim staff visits.
- **Access:** Open PDF. Country page sometimes blocks scrapers; use the publications URL.
- **Bias / gap:** Staff are talking to the authorities; the report is not an investigation. SWF internals remain estimated. Property-risk language is macroprudential, not DLD-granular.
- **ERM hook:** A1, A7, C-04, C-12, C-18. **Start every quarterly re-run here.**

Related: IMF IFS, BOP, Fiscal Monitor aggregates via https://data.imf.org and World Bank Data360 mirrors.

### World Bank

- **WDI / Data360:** https://data.worldbank.org (UAE country) and https://data360.worldbank.org
- **Worldwide Governance Indicators:** https://www.worldbank.org/en/publication/worldwide-governance-indicators
- **Global Gas Flaring Tracker:** https://www.worldbank.org/en/programs/gasflaringreduction/global-flaring-data (UAE 15th-largest flarer in 2025, ~48 Bcf — EIA cites this)
- **Good for:** Comparable series (reserves, trade, population); governance scores as a *trend*, not a truth; flaring.
- **Bias / gap:** Many WDI series for the UAE are FCSC/CBUAE with a lag. Do not treat WGI as an OSINT sensor.
- **ERM hook:** Background series; S-09 carbon/flaring colour.

### Bank for International Settlements (BIS)

- **URL:** https://www.bis.org/statistics/index.htm — locational banking, consolidated banking, correspondent-banking overlays in research papers
- **Good for:** Cross-border claims *on* the UAE and UAE-bank foreign positions. Closest public proxy for correspondent-bank exposure (S-01/S-23).
- **Cadence:** Quarterly locational.
- **Access:** Open tables. No bank-level names.
- **Bias / gap:** Cannot see a single US correspondent cutting UAE names overnight. Direction and concentration only.
- **ERM hook:** A10 / C-05 multi-correspondent residue as a *system* statistic.

---

## Energy, Hormuz, power

### EIA — UAE Country Analysis Brief (primary energy OSINT)

- **HTML:** https://www.eia.gov/international/content/analysis/countries_long/United_Arab_Emirates/
- **PDF:** https://www.eia.gov/international/content/analysis/countries_long/United_Arab_Emirates/UAE.pdf
- **Last updated:** 28 Jul 2026
- **Chokepoints:** https://www.eia.gov/international/analysis/special-topics/World_Oil_Transit_Chokepoints
- **Hormuz LNG note:** https://www.eia.gov/todayinenergy/detail.php?id=65584
- **OPEC-exit note:** https://www.eia.gov/todayinenergy/detail.php?id=67804
- **Good for (facts the brief actually carries, Jul 2026):**
  - Ninth-largest liquids producer in 2025; left OPEC 1 May 2026
  - ADNOC claimed capacity 4.85 mbpd vs EIA 2025 estimate 4.15 and IEA ~4.3
  - ADCOP 1.8 mbpd to Fujairah; **second 1.5 mbpd bypass pipeline aimed 2027**
  - Fujairah underground storage 42 mb (2023); leased storage in Korea, Japan, India
  - **Mar 2026 Hormuz effective closure:** UAE crude+condensate 4.0 mbpd → ~2.4 mbpd Mar–May 2026
  - Dolphin pipeline from Qatar 3.2 Bcf/d; UAE still a net gas importer
  - Barakah 5.6 GW, unit 4 commercial Sep 2024; gas still ~71% of generation (2024)
  - Refining 1,249 kb/d (Ruwais 817, Jebel Ali 210, Fujairah cluster the rest)
- **Cadence:** CAB irregular (years between full rewrites; this one is current). STEO monthly for production during a war.
- **Access:** Open. Excel figure data linked from the HTML.
- **Bias / gap:** US government energy shop; Vortexa trade flows underneath the export charts. Will not give ADNOC OT posture or true spare capacity inside the fence.
- **ERM hook:** A2 / C-02 (and the “bypass of the bypass”), A5 power mix, A7, S-47, S-50 (Dolphin), S-44 (Fujairah as single point — second pipeline is the 2027 residue).

### IEA

- **Country:** https://www.iea.org/countries/united-arab-emirates
- **Oil Market Report:** monthly (capacity/production estimates EIA cites)
- **Good for:** Oil-market production vs capacity; gas; power. Independent of both ADNOC and EIA.
- **Access:** Some OMR content is subscriber.
- **ERM hook:** Triangulate ADNOC vs EIA capacity claims.

### OPEC Annual Statistical Bulletin

- **URL:** https://www.opec.org/annual-statistical-bulletin.html
- **Good for:** Reserves (ASB 2026: 120 bn bbl crude, 297 Tcf gas — EIA cites these). Historical production.
- **Bias / gap:** UAE departed OPEC 1 May 2026. Treat ASB as a statistical leftover, not as a policy affiliation. Quota politics no longer bind ADNOC.
- **ERM hook:** Reserves; A7 resource stock.

### Energy Institute Statistical Review of World Energy

- **URL:** https://www.energyinst.org/statistical-review
- **Good for:** LNG destination mix (EIA uses 2025 Review: India 54% of UAE LNG in 2024).
- **ERM hook:** S-09 destination switch; gas trade.

---

## AML, tax, sanctions, trade rules

### FATF / MENAFATF

- **FATF UAE page:** https://www.fatf-gafi.org/en/countries/detail/%C3%89mirats-arabes-unis.html
- **2020 Mutual Evaluation:** https://www.fatf-gafi.org/en/publications/Mutualevaluations/Mutualevaluationoftheunitedarabemiratesuae-reportandannexes.html
- **Follow-up / grey-list:** Grey-listed 4 Mar 2022; removed 23 Feb 2024 (“no longer subject to increased monitoring”).
- **5th round:** FATF calendar lists FATF–MENAFATF; last eval Apr 2020; possible onsite Jun 2026; possible plenary discussion Feb 2027 (dates on the assessments calendar — treat as scheduled, not done).
- **MENAFATF:** https://www.menafatf.org
- **Good for:** Whether C-05 is believed by the club that correspondent banks listen to. MER is still the best public map of UAE ML/TF *typologies* (gold, hawala, free zones, TF).
- **Cadence:** Plenary three times a year; MER once a round.
- **Access:** Open PDFs.
- **Bias / gap:** A clean FATF grade is not the same as UBO truth in every free zone (S-03, S-36, S-81). Next-round onsite is the live trigger.
- **ERM hook:** S-03, C-05, S-18, S-36, S-81. **Watch plenary weeks.**

### OECD (tax / Pillar 2)

- **URL:** https://www.oecd.org — Inclusive Framework, CbCR, harmful-tax lists
- **Good for:** Whether 9% CIT + 15% top-up is enough (S-02/S-75). UAE as IF member, not as a secrecy jurisdiction *in OECD language* — language can move.
- **ERM hook:** S-02, S-75, C-18.

### European Union

- **Tax list / non-cooperative jurisdictions:** Council conclusions (search “EU list of non-cooperative jurisdictions”)
- **CBAM:** https://taxation-customs.ec.europa.eu — carbon border adjustment on ADNOC barrels/products (S-09)
- **Good for:** Blacklist risk and carbon-border cost as *European legal facts*, not UAE press.
- **ERM hook:** S-02, S-09, C-05/C-18.

### OFAC / US Treasury

- **SDN and sanctions programs:** https://ofac.treasury.gov/sanctions-programs-and-country-information
- **Sanctions search:** https://sanctionssearch.ofac.treas.gov
- **Good for:** UAE-based names designated for Iran, Russia, Sudan/RSF, etc. Secondary-sanctions *theory* (S-01) becomes a *list* here.
- **Cadence:** Event-driven; CRS RS21852 tracks the political overlay.
- **Access:** Open. SDN is machine-readable.
- **Bias / gap:** Designation is not the same as a correspondent cut. Many UAE firms live in the grey of “not designated, de-risked anyway.”
- **ERM hook:** S-01, S-71, A10 / C-05.

### UN Comtrade / UNCTAD

- **Comtrade:** https://comtradeplus.un.org — UAE merchandise trade by partner and HS
- **UNCTAD:** investment and maritime reviews
- **Good for:** Re-export machine (Jebel Ali) as partner-level trade; India/China/Iran/Russia weights.
- **Bias / gap:** UAE entrepôt trade inflates gross flows; net is a different story. Gold and “confidential” chapters distort.
- **ERM hook:** A8, S-17 (India bypass), S-36 gold.

---

## US, UK, EU policy and security

### US Department of State

- **UAE country / NEA:** state.gov country pages (Investment Climate Statement, Human Rights Report, Trafficking in Persons)
- **Good for:** ICS = business-climate and legal-system colour (DIFC/ADGM, labour, expropriation). TIP: UAE Tier 2 for a long run (CRS: 14th consecutive year in 2025). HRR: the Freedom House / State list of restrictions (expression, association, transnational repression).
- **Cadence:** Annual reports.
- **Access:** Open.
- **Bias / gap:** US policy document. Labour and rights facts are real; they are also a bilateral lever. Not a substitute for MOHRE stocks.
- **ERM hook:** A3 (expat compact as seen from sending-state partners), A10 political weather, S-72/S-98.

### Congressional Research Service — RS21852

- **URL:** https://www.congress.gov/crs-product/RS21852
- **Title:** *The United Arab Emirates (UAE): Issues for U.S. Policy*
- **Good for:** One-stop US-policy brief: security relationship, Sudan/RSF allegations, Abraham Accords, human rights, SWF (cites Global SWF), Factbook-style facts. Updated (Jan 2026 edition indexed).
- **Cadence:** CRS updates when Congress needs it.
- **Access:** Open on congress.gov.
- **Bias / gap:** Written for members, not for a risk register. Footnotes are the OSINT.
- **ERM hook:** A10 / C-22, S-08, S-67, S-71.

### CENTCOM

- **AOR page:** https://www.centcom.mil/CENTCOM-AOR/United-Arab-Emirates/
- **Good for:** Presence as a public fact; posture language. Not order-of-battle.
- **ERM hook:** S-67 (umbrella withdrawal) — you will read this in *absence*, not in a press release.

### CIA World Factbook

- **Sunset:** CIA announced the public World Factbook sunset (Feb 2026). Do not cite as a living source. Historical snapshots remain in libraries. CRS still cited it in RS21852.
- **Replacement:** State / CRS / FCSC / IMF.

### UK FCDO

- **Travel advice / country:** gov.uk UAE pages
- **Good for:** British legal-community and travel-risk colour; DIFC English-law product is partly a UK-facing export.
- **ERM hook:** S-04/C-19; travel advice is a weak A8 sensor.

---

## Nuclear, climate, food, people

### IAEA

- **URL:** https://www.iaea.org — UAE country and Barakah-related peer reviews (IRRS, OSART when published)
- **Good for:** Whether FANR/ENEC meet the international nuclear club. Incident reporting if it ever happens.
- **ERM hook:** S-21, S-63.

### World Nuclear Association (not a government; listed here as the standard public technical brief)

- **URL:** https://world-nuclear.org/information-library/country-profiles/countries-t-z/united-arab-emirates.aspx
- **Good for:** Unit history, type (APR-1400), capacity. Cross-check ENEC.
- **ERM hook:** C-01 nuclear slice.

### Copernicus / NOAA / WMO

- **Copernicus Climate:** https://climate.copernicus.eu — ERA5 heat, wet-bulb derived products
- **NOAA:** heat indices; Gulf SST
- **WMO:** extreme-event attribution
- **Good for:** S-40/S-69 wet-bulb as *physics*, not as a municipal press release. 2024 Dubai flood as a climate-class event vs a drainage event (pair with DLD/DEWA).
- **Cadence:** Daily reanalysis; annual state-of-climate.
- **Access:** Open.
- **ERM hook:** A5, C-20, S-40, S-41, S-69.

### UN DESA Population / ILO / IOM

- **UN DESA:** https://population.un.org — international migrant stock (lagged)
- **ILOSTAT / IOM:** labour and migration
- **Good for:** Expat share as a UN number (~88–90% is the usual range — confirm vintage). Sending-state corridors.
- **Bias / gap:** Lagged; UAE census/SCAD is more current for *counts*. UN is better for *comparability*.
- **ERM hook:** A3, S-48, S-83, S-98.

### FAO / food-security indexes

- Import dependence (~85%+ of calories is the usual cited range — always check the vintage and whether it is calories, tonnage, or value).
- **ERM hook:** A9 / C-03. Strategic *reserve tonnes* remain a UAE-side dark spot.

---

## Shipping and aviation (public official / IGO)

### IMO / EMSA

- **IMO GISIS:** casualty, port-state control
- **EMSA:** European maritime safety (war-risk adjacent)
- **Good for:** Formal casualty and PSC, not live AIS (that is OSINT).
- **ERM hook:** S-51 insurance; S-33/S-38 after an attack.

### ICAO / IATA (traffic aggregates)

- Hub-rank and safety. DXB/AUH monthly detail is still better from airport press + OAG.

---

## Reading order against UAE official sources

| Question | UAE official | Foreign check |
|---|---|---|
| Is oil still the fiscal backstop? | FCSC GDP (misleading), MoF (partial) | **IMF AIV fiscal tables** |
| Can oil leave if Hormuz is shut? | ADNOC ADCOP page | **EIA CAB + STEO + AIS** |
| Is the peg defensible? | CBUAE bulletin | IMF AIV + IFS reserves |
| Will correspondent banks stay? | CBUAE/FTA AML PDFs | **FATF plenary + OFAC SDN + BIS** |
| Is Dubai property a crash? | **DLD** | IMF property/credit paras, CBUAE |
| Is Barakah a grid single point? | ENEC/EWEC | EIA generation mix, IAEA |
| Is the US still the sponsor? | MoFA | **CRS RS21852 + State + CENTCOM** |
