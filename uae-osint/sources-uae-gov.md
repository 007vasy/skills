# UAE government and SOE sources

Official federal, emirate, SOE, SWF, and regulator feeds. Primary numbers; always pair fiscal and energy claims with IMF / EIA ([sources-foreign-gov.md](sources-foreign-gov.md)).

Card format: what it is good for, cadence, access, bias/gap, residuality hook (A# / C# / S# from `uae.md`).

---

## Federal licence

The federation is the currency, the passport, the army, and the brand. These sources describe that layer.

### Official platform of the UAE Government (u.ae)

- **URL:** https://u.ae
- **Publisher:** UAE Government
- **Good for:** Entity map (who owns energy, water, visas, tax), strategy documents (We the UAE 2031, Centennial 2071, Net Zero 2050), open-data index, legal explainers (CIT, golden visa, data protection).
- **Cadence:** Pages dated; open-data index last updated 5 Jun 2026.
- **Access:** Open, bilingual. Strategy PDFs downloadable.
- **Bias / gap:** Narrative of the state. Use to find the *owning entity*, then go to that entity's statistics page for numbers.
- **ERM hook:** Orientation for A4 (federal vs emirate split), A8 (hub brand as a published product), C-17 (strategy/licence registry).

Open-data landing page: https://u.ae/en/about-the-uae/digital-uae/data/open-government-data

### Bayanat (UAE open data portal)

- **URL:** https://bayanat.ae
- **Publisher:** UAE Government (FCSC-heavy)
- **Good for:** Cross-entity dataset search. ~3,500 datasets, ~50 entities, ~8,000 resources (as of Aug 2026). SCAD is one of the largest publishers.
- **Cadence:** Continuous; quality uneven by publisher.
- **Access:** Open download (CSV/XLS/JSON depending on dataset).
- **Bias / gap:** Catalog, not a curated statistical yearbook. Many datasets are operational (facility lists, service counts), not national accounts. Search in Arabic for fuller hits.
- **ERM hook:** First stop before assuming a series does not exist. Feeds C-01 plant lists, C-13 digital-spine inventories.

Sister portals named on u.ae: [Abu Dhabi Data](https://data.abudhabi/), [Ajman Data](https://www.ajman.ae/en/ajman-data), Dubai Pulse (below).

### Federal Competitiveness and Statistics Centre (FCSC)

- **URL:** https://fcsc.gov.ae — stats explorer: https://uaestat.fcsc.gov.ae/en
- **Publisher:** FCSC, Ministry of Cabinet Affairs
- **Good for:** National GDP (production and expenditure, current and constant), population, labour, trade, competitiveness rankings, SDG dashboard. IMF DSBB lists FCSC as the official statistical body; National Summary Data Page lives here.
- **Cadence:** Annual national accounts; press releases on growth (e.g. 2025 GDP +6.2% to AED 1.9tn). No published advance-release calendar (IMF DQAF).
- **Access:** Open; explorer is SDMX-style. Arabic often has more dimensions.
- **Bias / gap:** **Non-oil GDP share is not oil fiscal share.** FCSC will happily report non-oil output near 80% while hydrocarbons still dominate consolidated revenue. Do not use FCSC GDP mix as the A7 test.
- **ERM hook:** Step-1 magnitudes; S-59 / C-18 (must be read *against* IMF fiscal tables).

Open Data Inventory 2024: UAE ranked 9th globally (coverage 74, overall 85) — FCSC is a real statistical office, not a brochure.

### Central Bank of the UAE (CBUAE)

- **URL:** https://www.centralbank.ae
- **Statistics:** https://www.centralbank.ae/en/research-and-statistics/
- **Latest stats:** https://www.centralbank.ae/en/research-and-statistics/latest-statistics/
- **Publisher:** CBUAE
- **Good for:** Monthly *Statistical Bulletin* (banking, monetary, insurance); Balance of Payments; CBUAE balance sheet and foreign assets; Financial Soundness Indicators; working papers. Peg operating facts: CBUAE buys USD at 3.673 and sells at 3.672; Decretal Federal Law 14/2018 requires foreign reserves ≥ 70% of the monetary base.
- **Cadence:** Monthly bulletin (May 2026 bulletin published 28 Jul 2026; Banking Operations Statistics June 2026 on 14 Aug 2026). BoP roughly semi-annual. Annual report (2025 report issued Apr 2026).
- **Access:** Open PDF + XLS. No login.
- **Bias / gap:** Best official window on A1. Does not publish a peg-defence war-chest as a single number; you reconstruct from foreign assets vs monetary base. Correspondent-bank names and SWIFT exposures are absent. Reserve-management FAQ still quotes “around $215bn” — use the *bulletin*, not the FAQ.
- **ERM hook:** A1 / C-04 (peg, FX mismatch), S-19/S-23/S-60/S-68, A10 dollar-system node. IMF 2025 AIV graded CBUAE FSIs “A” and raised external-sector data from D to C.

Rulebook (AML, SoF/SoW): https://rulebook.centralbank.ae — C-05 hygiene as written, not as fielded.

### Ministry of Finance

- **URL:** https://mof.gov.ae
- **Federal budgets:** https://mof.gov.ae/federal-budgets/
- **Government financial statistics:** https://mof.gov.ae/financial-statistics/
- **Procurement (DPP):** https://mof.gov.ae/government-procurement-operations/
- **Good for:** Federal budget documents, GFS, GCC market statistical reports, federal tender digitalisation.
- **Cadence:** Annual budget; GFS periodic.
- **Access:** Open PDFs. Arabic often first.
- **Bias / gap:** Federal budget is not the consolidated UAE fiscal position — Abu Dhabi (and historically Dubai transfers) sit off this page. CIT revenue-sharing (S-07) will not be fully visible here.
- **ERM hook:** C-18 federal slice; S-07 CIT fight; C-09 cohesion envelope for northern emirates.

### Federal Tax Authority (FTA)

- **URL:** https://tax.gov.ae
- **Good for:** CIT (9%) and VAT (5%) rules, EmaraTax platform facts, enforcement press releases (inspection volumes, seized excise). Pillar 2 / 15% multinational top-up as implemented, not as OECD theory.
- **Cadence:** Rule updates as issued; enforcement news irregular.
- **Access:** Open guidance; taxpayer portal is UAE Pass / EmaraTax.
- **Bias / gap:** No public time series of CIT collections by emirate or free zone. S-56 (enforcement quality collapse) and S-94 (CIT plateau) cannot be confirmed from FTA alone — pair with IMF fiscal tables and MoF.
- **ERM hook:** S-02/S-75 (Pillar 2), S-56/S-94, C-18.

### Telecommunications and Digital Government Regulatory Authority (TDRA)

- **URL:** https://www.tdra.gov.ae
- **Open data:** https://www.tdra.gov.ae/en/open-data.aspx
- **.ae WHOIS:** https://tdra.gov.ae/en/aeda/pages/whoislookup and https://www.nic.ae
- **Good for:** UAE Pass as national identity spine, open-data policy, `.ae` domain WHOIS, telecom market stats.
- **Cadence:** Policy as issued; WHOIS on demand.
- **Access:** WHOIS open; some digital-gov stats on Bayanat.
- **Bias / gap:** Will not tell you whether airport/bank edges can admit a person without UAE Pass (C-13 `unlock_redundancy`).
- **ERM hook:** S-20 / C-13 (digital spine as a single door).

### Federal Authority for Identity, Citizenship, Customs and Port Security (ICP)

- **URL:** https://icp.gov.ae
- **Good for:** Visa product rules (golden visa, green visa), identity, customs/port-security press, UAE Pass integration at the border.
- **Cadence:** Product-rule changes; press.
- **Access:** Services are UAE Pass. Public stats on visa stocks are thin — population is FCSC/SCAD; labour is MOHRE.
- **Bias / gap:** Cohort cancellations (S-72) and source-country shares (S-55) are not published as a dashboard.
- **ERM hook:** A3 / C-06, S-06/S-61 (grandfathering), S-72.

### Ministry of Human Resources and Emiratisation (MOHRE)

- **URL:** https://www.mohre.gov.ae
- **Observatory:** https://observatory.mohre.gov.ae/en
- **Statistical reports:** https://www.mohre.gov.ae/en/open-data/statistical-report
- **Good for:** Private-sector labour force by occupation/nationality (Excel), Emiratisation quotas, Labour Market Observatory competitiveness indicators.
- **Cadence:** Statistical reports periodic; observatory updated as indicators refresh.
- **Access:** Open Excel on the statistical-report page. GRC (see OSINT file) republishes older extracts.
- **Bias / gap:** Domestic workers and some free-zone populations have historically been under-counted or split across ICP/free-zone authorities. Nationality mix of *critical functions* (ATC, desal, hospitals) is not published.
- **ERM hook:** A3 / C-06, S-29 (Emiratisation), S-48 (labour-corridor bulkhead).

### Ministry of Economy and Tourism (MoET)

- **URL:** https://www.moet.gov.ae (formerly MoEc — `moec.gov.ae` still redirects in places)
- **Open data:** https://www.moet.gov.ae/en/moec-opendata
- **Company registrars list:** https://www.moec.gov.ae/en/company-registrars-within-the-uae
- **Good for:** Tourism arrivals (when published), SME/licence counts, list of onshore and free-zone registrars, FDI narrative.
- **Cadence:** Open-data refresh uneven; tourism often via press rather than a clean monthly series.
- **Access:** Open. Trade Registry / National Economic Registry are separate (below).
- **Bias / gap:** Tourism source-market mix (S-13/S-55) is better in emirate tourism authorities and Emirates/DXB traffic than here.
- **ERM hook:** A8 hub product; registrar map for C-05 UBO.

### Ministry of Justice

- **URL:** https://www.moj.gov.ae/en/open-data.aspx
- **Court stats (FCSC):** linked from uaestat court statistics
- **Good for:** Onshore court volumes, not judgments. DIFC/ADGM judgments live on those courts' sites.
- **ERM hook:** S-04 (onshore recognition of free-zone judgments) — MoJ will not publish a refusal; watch DIFC/ADGM case law and press.

### Ministry of Climate Change and Environment (MoCCAE)

- **URL:** https://www.moccae.gov.ae/en/open-data.aspx
- **Good for:** Food-security strategy documents, environmental datasets, climate policy.
- **Bias / gap:** Strategic food *reserve tonnes* (A9 as inventory) are not a public time series.
- **ERM hook:** A9 / C-03, S-49, S-100 (brine / marine).

### Ministry of Energy and Infrastructure

- **URL:** via u.ae energy-entities page: https://u.ae/en/information-and-services/environment-and-energy/water-and-energy/energy-entities
- **Good for:** Federal energy-security mandate; map of who actually runs water/power (EWEC/DoE, DEWA, SEWA, Etihad Water & Electricity for the northern four).
- **ERM hook:** C-01 owner map.

### Federal Authority for Nuclear Regulation (FANR)

- **URL:** https://fanr.gov.ae/en
- **Good for:** Licensing, inspection posture, radiation/safeguards. Independent regulator on paper for Barakah.
- **Cadence:** Licence events, annual reports, IAEA-facing publications.
- **Bias / gap:** Incident detail will be tightly managed. Pair with IAEA and ENEC.
- **ERM hook:** S-21 / C-01 nuclear bulkhead — *independent* regulator is the residue; this page is whether that residue exists as an institution.

### Other federal open-data slices

| Entity | URL | Use |
|---|---|---|
| Ministry of Health & Prevention | https://mohap.gov.ae/en/open-data | Hospital/capacity colour for S-70 |
| Ministry of Education | https://www.moe.gov.ae/en/opendata/pages/home.aspx | School seats (S-92) — incomplete |
| FAHR | https://www.fahr.gov.ae/en/opendata/ | Federal HR, not the private-sector labour system |
| WAM (Emirates News Agency) | https://www.wam.ae | Official statements; authentic-channel watch for S-39 / C-15 |

---

## Abu Dhabi — fiscal engine

### Statistics Centre – Abu Dhabi (SCAD)

- **URL:** https://scad.gov.ae
- **Bayaan:** https://scad.gov.ae/web/guest/bayaan
- **Census:** https://census.scad.gov.ae
- **Good for:** Abu Dhabi GDP (incl. hydrocarbon vs non-oil), population (4.14m in 2024, +7.5%), prices, labour, sector accounts. Largest publisher on Bayanat.
- **Cadence:** Quarterly GDP (e.g. Q3 2025 real GDP AED 325.7bn, +7.7% y/y); census cycles.
- **Access:** Open publications; Bayaan is the interactive tool.
- **Bias / gap:** Emirate accounts, not federal. Oil *output* is clearer here than oil *fiscal transfers* to the federation.
- **ERM hook:** AD layer of Step 1; A7 at the emirate that actually owns the oil.

### ADNOC Group and listed subsidiaries

- **Group:** https://www.adnoc.ae
- **ADCOP (Hormuz bypass pipeline):** https://www.adnoc.ae/en/adnoc-pipelines/about-us/who-we-are — ~406 km, Abu Dhabi collection centre → Fujairah; group-stated oil capacity 4.85 mbpd (EIA's 2025 estimate is 4.15; IEA ~4.3 — treat 4.85 as ADNOC's claim).
- **Listed IR (use these; the parent is opaque):**
  - ADNOC Gas — https://adnocgas.ae/en/investor-relations
  - ADNOC Drilling, ADNOC Logistics & Services, ADNOC Distribution — ADX filings
- **Good for:** Production-capacity targets (5 mbpd by 2027), capex envelopes ($150bn 2026–30 per EIA/Energy Intelligence), Fujairah storage (42 mb caverns, 2023), second bypass pipeline (1.5 mbpd, aimed 2027), LNG (Das Island; Ruwais LNG targeting 2028).
- **Cadence:** IR as listed companies (quarterly); group press as issued.
- **Access:** Listed-sub financials are IFRS. Group “facts” are press.
- **Bias / gap:** Capacity ≠ production (OPEC+ then OPEC exit 1 May 2026). Spare-capacity claims are a commercial and political product. OT/SCADA posture (S-25) is not public.
- **ERM hook:** A2 / C-02 (ADCOP 1.8 mbpd + second line), A7, S-09 (carbon intensity), S-25.

### Emirates Nuclear Energy Corporation (ENEC) / Nawah

- **URL:** https://www.enec.gov.ae — Barakah: https://www.enec.gov.ae/barakah-plant/
- **Good for:** Four APR-1400 units, 5.6 GW, unit 4 commercial Sep 2024; ENEC claim ~25% of UAE electricity. Live unit status on the Arabic homepage is more operational than the English overview.
- **Cadence:** Unit events; generation counters.
- **Access:** Open. FANR is the regulator; ENEC is the owner (ADQ family).
- **Bias / gap:** Safety-case detail is not public. Grid-without-Barakah (S-21 residue) lives at EWEC/DoE, not here.
- **ERM hook:** A5 / C-01, S-21, S-63 (decommissioning unfunded — not disclosed).

### Emirates Water and Electricity Company (EWEC)

- **URL:** https://www.ewec.ae (plant roster on the homepage)
- **Good for:** Sole procurer of water and power in Abu Dhabi. Plant list (gas, solar, Barakah, RO desal). Stated ~17.9 GW; “200 million gallons/day new RO by 2026.” Fujairah F3 CCGT (2.4 GW) commercial 2025 — east-coast power, relevant to C-02 geography.
- **Cadence:** Project press; annual planning documents when released.
- **Access:** Open plant pages; no public desal *inventory-days*.
- **Bias / gap:** Geographic dispersal of desal (C-01's actual bulkhead) is not a map with redundancy analysis. Intake common-mode (S-87 algal bloom) will not be admitted here.
- **ERM hook:** A5 / C-01 — the inhabitability stack's procurement layer.

### TAQA (Abu Dhabi National Energy Company)

- **URL:** https://www.taqa.com
- **Good for:** Listed utility; generation, transmission (TRANSCO), desal, international assets. IFRS financials.
- **ERM hook:** C-01 listed expression; fuel-mix bulkhead (S-50 Dolphin).

### ADIA (Abu Dhabi Investment Authority)

- **URL:** https://www.adia.ae/en/publications
- **Reviews:** https://www.adia.ae/en/pr/2024/index.html (2024 Review)
- **Good for:** Annual Review: MD letter, asset-class and geography *ranges* (typically equities 40–50%, FI 20–30%, alts/real assets 25–35%), 20-year and 30-year annualised returns. Board/IC names. IFSWF Santiago Principles reporting.
- **Cadence:** Annual.
- **Access:** Open PDF. No AUM figure from ADIA itself — market estimates (Global SWF) put it ~$1.2tn.
- **Bias / gap:** No line items, no jurisdiction of custody, no drawable vs intergenerational split. C-09 ring-fence cannot be verified here.
- **ERM hook:** A7 / C-09, S-58, S-71, S-96.

### Mubadala Investment Company

- **URL:** https://www.mubadala.com/en/investors/overview
- **Good for:** The *transparent* SWF: annual report, HY and FY consolidated IFRS financials. 2025 report: “Building Value Through Resilience.” Deal flow visible in press (Global SWF: ~$32.7bn deployed 2025, top AI spender).
- **Cadence:** Semi-annual financials; annual report.
- **Access:** Open PDFs.
- **Bias / gap:** Still not ADIA. Domestic industrial-policy assets and G42-class AI sit in this orbit or ADQ's; look through to portfolio companies.
- **ERM hook:** C-09 drawable slice, S-05/S-91 (AI partnerships), S-30 (talent raid).

### ADQ (Abu Dhabi Developmental Holding)

- **URL:** https://www.adq.ae — investors (bond programme): https://www.adq.ae/investors
- **Good for:** Holding company for EWEC, ENEC, AD Ports, Etihad, and a large domestic cluster. GMTN prospectuses and consolidated financials (when released via the bond gate) are the real disclosure — more useful than the marketing site. Ratings typically match Abu Dhabi sovereign (Aa2/AA).
- **Cadence:** Bond-programme updates; FY financials (2024 CFS dated Mar 2025).
- **Access:** Investor docs often behind a “not a US person” gate; LSE RNS PDFs are a workaround.
- **Bias / gap:** Thin compared with Mubadala. L'imad / Crown Prince vehicles are darker still.
- **ERM hook:** C-09 domestic deployment; Etihad Rail (S-82) sits in this orbit.

### Abu Dhabi Global Market (ADGM)

- **URL:** https://www.adgm.com/public-registers
- **Good for:** Public registers of ADGM entities; FSRA enforcement; English-law financial free zone (Abu Dhabi's DIFC analogue).
- **Cadence:** Register is live.
- **Access:** Open search.
- **ERM hook:** C-05 UBO, C-19 legal product, S-04/S-74.

### Abu Dhabi land / spatial

- **MyLand (DMT):** https://myland.dmt.gov.ae
- **SDI:** https://sdi.gov.abudhabi/sdi/
- **Good for:** Cadastral and spatial layers. Some services resident-gated.
- **ERM hook:** Physical plant siting for C-01/C-16 (are desal clusters actually dispersed?).

### AD Ports Group

- **URL:** listed IR on ADX; group site adports.ae
- **Good for:** Khalifa Port, Fujairah-adjacent cargo, economic-zone throughput — Abu Dhabi's half of C-02/C-11.

---

## Dubai — throughput engine

### Dubai Pulse / Data.Dubai / DDSE

- **Pulse:** https://www.dubaipulse.gov.ae
- **Data.Dubai (product page):** https://www.digitaldubai.ae/apps-services/details/data.dubai
- **DSC stats on Pulse:** https://www.dubaipulse.gov.ae/organisation/dubai-statistics-center/service/dsc-statistics
- **Publisher:** Dubai Data and Statistics Establishment (DDSE) under Digital Dubai (the old Dubai Statistics Center lives on as datasets).
- **Good for:** Reference registers under Dubai Data Law; GDP quarterly, CPI, construction-material prices, commercial property price index, buildings. Dubai population (DDSE via Digital Dubai: 4.74m usual residents end-Jul 2026).
- **Cadence:** CPI/GDP datasets updated into 2026 (CPI and quarterly GDP marked 5 Feb 2026 on Pulse).
- **Access:** Open CSV after T&Cs. High-quality structured registers.
- **Bias / gap:** Pulse vs Data.Dubai branding is in flux — same family. Northern-emirate spillover is not here.
- **ERM hook:** DXB layer of Step 1; S-54 population vs utilities.

### Dubai Land Department (DLD)

- **Open data hub:** https://dubailand.gov.ae/en/open-data/
- **Real-estate data:** https://dubailand.gov.ae/en/open-data/real-estate-data/
- **Research / annual reports:** https://dubailand.gov.ae/en/open-data/research/
- **Good for:** Transaction value and volume, rents, project valuations, off-plan vs ready, annual real-estate performance report. Q1 2026: AED 252bn transactions, +31% y/y value, +6% volume. H1 2026 project completions: 104 projects, AED 111bn.
- **Cadence:** Interactive current-year on DLD; history on Dubai Pulse (`organisation/dld`).
- **Access:** Open.
- **Bias / gap:** Best property sensor in the country. Will not give bank concentration by master-developer (S-93) or source-country share of buyers (S-55) as a hard cap series — those need additional slicing or bank disclosures.
- **ERM hook:** S-14 / C-12, S-45, S-54, S-61, S-89.

### DP World

- **Annual report:** https://www.dpworld.com/en/investors/annual-report-2025
- **Good for:** Group TEU (93.4m in 2025) and, crucially, *Jebel Ali* colour in the UAE release (O&D +9% in 2025; vehicles, breakbulk). Port capacity 109m TEU group-wide.
- **Cadence:** Annual + periodic trading updates.
- **Access:** Open PDF.
- **Bias / gap:** Group is global; Jebel Ali is one node. War-risk insurance (S-51) will show up as a callings comment, not a line item.
- **ERM hook:** A8 / C-11, S-16, S-47.

### Emirates Group

- **Annual reports:** https://www.emirates.com/english/about-us/financial-transparency/annual-reports/ (back to 1993–94; 2025–26 report posted)
- **Good for:** Sixth-freedom hub P&L, ASK/RPK, passenger numbers, fuel, geopolitical disruption footnotes. IFRS.
- **Cadence:** Annual (FY to 31 Mar).
- **Access:** Open PDF.
- **Bias / gap:** flydubai and Etihad are separate. Multi-airport bulkhead (C-11) needs Dubai Airports + Abu Dhabi Airports / ADQ as well.
- **ERM hook:** S-15, S-13, S-90 (jet-A).

### Dubai Airports / DXB

- Traffic statistics via Dubai Airports press and DDSE. No single OECD-style monthly dashboard; use press + Emirates traffic + aviation analytics (OAG, see OSINT file).
- **ERM hook:** A8, S-15, S-57, S-97.

### DIFC / DFSA

- **DIFC:** https://www.difc.ae
- **Courts:** judgments on DIFC Courts site; BAILII mirrors some (see OSINT file)
- **Good for:** English-law financial centre: firm counts, courts, DFSA enforcement. The legal product C-19 claims.
- **ERM hook:** S-04, S-74, S-18 (VARA is Dubai, not DIFC — do not conflate).

### VARA (Virtual Assets Regulatory Authority)

- **URL:** https://www.vara.ae (rulebook on the same family)
- **Good for:** VASP licences, enforcement. Whether Dubai's crypto pitch is a supervisor or a logo (S-18 residue).
- **ERM hook:** S-18, C-05/C-19.

### SCA (Securities and Commodities Authority) / DFM / ADX

- Onshore capital-markets regulator and the two exchanges. GRE bond and equity colour; international-investor share (DFM H1 2026: 71% of new investors international).
- **ERM hook:** S-78 (Riyadh IPO calendar), S-80 GRE credit.

### DEWA

- **URL:** https://www.dewa.gov.ae
- **MBR Solar Park:** https://www.dewa.gov.ae/en/about-us/strategic-initiatives/mbr-solar-park
- **Good for:** Dubai power/water, solar build-out, outage/flood operating colour after 2024. Hassyan converted off coal (2022).
- **ERM hook:** A5 Dubai half of C-01, S-41 flood, S-46 grid.

### ICD (Investment Corporation of Dubai)

- **Financials:** https://icd.gov.ae/financial-information/
- **Annual report microsites:** e.g. https://reporting.icd.gov.ae/2024/
- **Good for:** Dubai's SWF/holding company. Audited consolidated statements (2025 CFS posted). Assets AED 1,680bn in 2025; revenue AED 359bn; profit AED 73.4bn. Portfolio: Emirates, dnata, Emaar stake, DDF, EGA (50% with Mubadala), etc.
- **Cadence:** Annual + interim.
- **Access:** Open PDFs — unusually transparent for a Dubai GRE.
- **Bias / gap:** Names are not the sovereign (S-80 residue is to *tell the market that*). ICD financials still read as Dubai Inc.
- **ERM hook:** C-09 Dubai side, S-80/S-95 GRE debt.

### Dubai Holding

- Marketing site plus occasional bond/prospectus disclosure. Thinner than ICD. Treat as ICD's sibling, not a second ICD.

### Dubai Economy and Tourism / DED eServices

- **Licence search:** https://eservices.dubaided.gov.ae (GST home)
- **Good for:** Onshore Dubai trade-licence lookup.
- **ERM hook:** C-05 entity existence; not UBO.

---

## Shared legal-entity and land rails

### UAE Trade Registry Smart Portal

- **URL:** https://traderegistry.ae
- **Good for:** Federal trade-registry applications; **Register of Beneficiaries** exists as a legal object (the FATF residue). Public query depth is limited.
- **Access:** Partially open; beneficial-ownership detail is not a public ICIJ-style dump.
- **ERM hook:** C-05 — UBO *existence* vs UBO *truth*. S-03 FATF.

### National Economic Registry (growth.gov.ae)

- **URL:** https://www.growth.gov.ae/G2C
- **Good for:** Licence numbers, names, registration dates, contacts. Public, no fee.
- **ERM hook:** Entity existence; land/licence overlay.

### Makani (Dubai geo-address)

- **URL:** https://www.makani.ae/desktop/
- **Good for:** Official 10-digit geo-address, spatial search.
- **ERM hook:** Physical siting; flood/desal mapping when combined with satellite.

### Northern emirates (spillover geography, not co-equal engines)

| Source | URL | Use |
|---|---|---|
| Ajman Data | https://www.ajman.ae/en/ajman-data | Small open-data catalog |
| Sharjah SEDD / SEWA | emirate sites | S-84 northern fiscal stress — mostly press, not GFS |
| Ras Al Khaimah / Fujairah ports | port authority sites + AIS | East-coast bypass colour (C-02) |
| Etihad Water & Electricity | u.ae energy-entities | Water/power for Ajman, UAQ, RAK, Fujairah |

Fujairah is strategically load-bearing (oil export + F3 power) even though it is not a fiscal engine. Do not bury it under “northern.”

---

## How to read these against each other

1. **GDP (FCSC/SCAD) vs fiscal (IMF/MoF/FTA).** If they disagree on diversification, IMF fiscal wins for A7.
2. **ADNOC capacity vs EIA production.** Capacity is a target; EIA/STE O is what left the ground, including the Mar–May 2026 Hormuz shut-in (EIA: 4.0 → 2.4 mbpd).
3. **CBUAE reserves vs ADIA Review.** Central-bank FX is the peg tool (C-04). ADIA is the intergenerational stack (C-09). Do not add them.
4. **DLD transactions vs CBUAE credit.** Property heat (S-14) is DLD; whether banks are concentrated (S-93) is CBUAE + listed-bank Pillar 3.
5. **MOHRE vs SCAD/FCSC population.** Jobs vs bodies. A3 needs both.
