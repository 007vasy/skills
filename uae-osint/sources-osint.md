# Investigative and technical OSINT

Public sources that are not UAE ministries and not foreign statistical offices. Use these to test whether official claims are *inventory* (ships at berth, tanks in a cavern, a judgment on a docket) or *strategy decks*.

People-lookup (phones, plates, Getcontact, yellow pages) is **out of scope**. The existing list is [paulpogoda/OSINT-Tools-Emirates](https://github.com/paulpogoda/OSINT-Tools-Emirates). This file is for the enterprise in `uae.md`.

---

## Corporate, courts, beneficial ownership

### ADGM public registers / FSRA

- **URL:** https://www.adgm.com/public-registers
- **Good for:** Live entity search in Abu Dhabi's English-law free zone; FSRA notices. Confirm a name exists, is licensed, or was fined.
- **ERM hook:** C-05, C-19, S-04.

### DIFC Courts / DFSA

- DIFC Courts judgments (difccourts.ae); DFSA enforcement.
- **BAILII UAE recent decisions:** https://www.bailii.org/recent-decisions-ae.html — English-language mirror of some UAE-related common-law decisions.
- **ERM hook:** S-04 (onshore recognition failure will show up as a *case*, not as an MoJ press release), S-74.

### ADX / DFM listed-company filings

- Abu Dhabi Securities Exchange and Dubai Financial Market — financials for ADNOC listed subs, TAQA, FAB, Emirates NBD, Emaar, AD Ports, etc.
- **Good for:** The IFRS slice of GREs and banks. Pillar 3 / concentration notes for S-93 (one developer too big for the banks).
- **ERM hook:** C-12, S-80, S-95.

### OpenSanctions

- **URL:** https://www.opensanctions.org
- **Good for:** Combined OFAC/UN/EU/UK lists plus PEPs. Search UAE entities and vessels.
- **Cadence:** Continuous.
- **Access:** Open; bulk commercial.
- **ERM hook:** S-01, S-71, C-05. Pair with OFAC primary.

### OCCRP — Dubai Unlocked

- **URL:** https://www.occrp.org/en/project/dubai-unlocked
- **Good for:** Investigative property-ownership dataset (the 2024 leak project). Who actually holds Dubai real estate among PEPs and sanctioned persons — the DLD open-data portal will not tell you this.
- **Cadence:** Project dataset; not a live feed.
- **Access:** OCCRP journalism + dataset access per their terms.
- **Bias / gap:** Snapshot, not a register. Do not treat as current UBO.
- **ERM hook:** S-36, S-55, S-89, C-05/C-12.

### ICIJ (historical)

- Panama / Pandora / other leaks with UAE incorporations. Historical typology for S-36, not a 2026 sensor.

### Manhom

- **URL:** https://manhom.com
- **Good for:** Arabic-first biographies of public Arab business and political figures (~240k). Change-tracking on profiles.
- **Bias / gap:** Not official. Use for *public* role maps, not for private family trees. Stay on public figures.
- **ERM hook:** Thin colour on C-08 (named heirs are already public); do not use for S-66 speculation.

---

## Sovereign-wealth tracking

### Global SWF

- **URL:** https://globalswf.com
- **Good for:** AUM league tables and annual spend (the numbers `uae.md` already uses: ADIA ~$1.2tn, ICD, Mubadala, ADQ). 2025 spend: Mubadala ~$32.7bn, ADIA ~$12.9bn, ADQ ~$10.9bn. AI spend ranking.
- **Cadence:** Annual report + deal database (some paid).
- **Access:** Headline rankings free; full database paid.
- **Bias / gap:** Estimates. ADIA does not confirm AUM. Use for *order of magnitude and relative spend*, not for C-09 ring-fence proof.
- **ERM hook:** A7 / C-09, S-58, S-30 vs PIF.

### IFSWF

- **URL:** https://www.ifswf.org
- **Good for:** Santiago Principles self-reporting (ADIA). Governance claims, not portfolios.

---

## Physical sensors — ships, planes, plants

### AIS (MarineTraffic, VesselFinder, IMO GISIS as backup)

- **Good for:** Tanker and container calls at **Fujairah**, **Jebel Ali**, Khalifa, Khor Fakkan. Hormuz transits. Whether A2 is working *this week*.
- **Cadence:** Live.
- **Access:** Free map with limits; historical is paid (Lloyd's List Intelligence, Kpler, Vortexa — EIA already uses Vortexa).
- **Bias / gap:** AIS spoofing in the Gulf is a known problem in wartime. Pair with SAR satellite if a call matters.
- **ERM hook:** A2 / C-02, S-16, S-47, S-51 (if ships stop calling, insurance or fear did it).

Watch boxes: Strait of Hormuz TSS; Fujairah offshore anchorage; Jebel Ali approach; ADCOP terminal.

### Flightradar24 / ADS-B / OAG

- **Good for:** DXB/AUH/DWC movements; groundings (fog, drone, GPS-denial — S-97); sixth-freedom connectivity as a network, not a slogan.
- **Cadence:** Live.
- **Access:** Free live; OAG schedules paid.
- **ERM hook:** S-15, S-43, S-97, C-11.

### Satellite imagery

- **Sentinel-2 / Sentinel-1 (Copernicus):** free, 5–12 day optical / SAR — desal plants, Fujairah tanks, flood extents (2024 replay), construction.
- **Landsat**
- **Planet / Maxar:** paid, higher cadence — for a specific plant or terminal.
- **Google Earth** historical slider: slow-change (reclamation, Palm, new desal).
- **Good for:** C-01 geographic dispersal *as a map*. Are desal clusters actually on one coast road (S-38/S-87 common-mode)?
- **ERM hook:** A5 / C-01 / C-16, S-41, S-44, S-45 (reclamation).

### OpenStreetMap / Makani

- OSM for plant and port footprints; Makani for official Dubai geo-address. Combine with Sentinel.

---

## Energy and maritime commercial (paywalled, load-bearing)

These are not “nice to have.” For barrels, war-risk, and spare capacity they beat press.

| Source | What you buy | ERM hook |
|---|---|---|
| **MEES** (Middle East Economic Survey) | Weekly GCC energy politics; EIA already cites it | A2, A7, OPEC-exit, Fujairah |
| **Energy Intelligence** | ADNOC capacity vs EIA/IEA triangulation | A2 capacity claims |
| **S&P Global Commodity Insights / Platts** | Murban, Dubai/Oman benchmark, Fujairah products | A7 price, S-09 |
| **Argus** | Same family | A7 |
| **Lloyd's List / LLI** | Calls, casualties, war-risk commentary | S-51, S-16 |
| **Kpler / Vortexa** | Cargo flows (EIA used Vortexa for 2022–25 UAE crude exports) | A2 live |
| **Rystad** | Upstream and gas-exporter timeline | S-50 net-gas-exporter claim |

If you can afford one: **MEES + AIS**. If two: add **Vortexa/Kpler**.

---

## Conflict, arms, unrest

### SIPRI Arms Transfers Database

- **URL:** https://armstrade.sipri.org
- **Good for:** Public arms imports/exports (US, France, etc.). Deterrence hedge (C-22) as hardware, not communiqués.
- **Cadence:** Annual.
- **ERM hook:** C-22, S-67.

### ACLED

- **URL:** https://acleddata.com
- **Good for:** Recorded political violence. UAE domestic events are sparse; regional (Yemen, Sudan, Gulf tanker attacks) is the relevant set.
- **ERM hook:** S-33/S-35/S-38 as *regional* context, not a Dubai crime dashboard.

### IISS Military Balance (paid)

- Force structure. Complement to SIPRI.

---

## Labour and demography (repackagers)

### GRC — Gulf Labour Markets and Migration

- **URL:** https://gulfmigration.grc.net
- **Good for:** Clean tables built from MOHRE/FCSC open data (e.g. private-sector labour by occupation). Citation trail back to the ministry Excel.
- **Bias / gap:** Not fresher than MOHRE; often *clearer*. Vintage lags.
- **ERM hook:** A3, S-48, S-29.

### GLMM / EUI working papers

- Historical demography (De Bel-Air and successors). Use for structure (citizen/expat ratio politics — S-83), not for 2026 counts (use SCAD/DDSE).

---

## News that functions as a sensor (not a source of truth)

Use for *event detection*, then go back to an official or IGO series.

| Outlet | Why |
|---|---|
| **WAM** | Official statements; C-15 authentic channel |
| **The National** (Abu Dhabi) | Closest to AD policy language |
| **Gulf News / Khaleej Times** | Dubai operating colour |
| **Reuters / Bloomberg / AP** | Sanctions, Hormuz, GRE credit |
| **Enterprise (enterpriseam.com)** | GCC deal and SWF spend tracking; often cites Global SWF |
| **Ahram / Iranian / Indian English press** | Sending-state and neighbour frames for S-48/S-98/S-33 |

Social media: Gulf official accounts (rulers' courts, CBUAE, ADNOC) are C-15 sensors. Do not take royal-health or succession rumour from anonymous accounts into the ERM file (A6 dark on purpose).

---

## Climate / flood / heat (technical)

- **Copernicus ERA5** — heat, humidity; derive wet-bulb.
- **UAE NCM / NCMW** (National Centre of Meteorology) — official rainfall, haboob, cloud-seeding. Pair 2024 flood with DLD/DEWA after-action, not with NCM seeding claims alone.
- **Municipal drainage reports** post-2024 — whether C-20 is drills or a PDF.

---

## Tenders (capital formation, not gossip)

From the Emirates tools list; useful for *what the state is actually building*.

- MoF Digital Procurement Platform — https://mof.gov.ae/government-procurement-operations/
- Abu Dhabi Government Procurement Gate — https://adgpg.gov.ae
- Digital Dubai tenders — https://www.digitaldubai.ae/tenders
- TenderUAE aggregator — https://www.tenderuae.com

**ERM hook:** C-01/C-02 capex as tenders (second desal, second pipeline, rail) vs press-release capacity.

---

## What not to do

- Do not build resident dossiers (phones, plates, school records).
- Do not treat Telegram “Gulf intel” channels as a source.
- Do not scrape UAE Pass–gated registries.
- Do not estimate ADIA line items from deal press and call it C-09.
- Do not use GDP-share tweets as a fiscal fact.

For plates, WHOIS, yellow pages, and vehicle APIs: [OSINT-Tools-Emirates](https://github.com/paulpogoda/OSINT-Tools-Emirates).
