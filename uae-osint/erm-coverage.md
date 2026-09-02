# Coverage map — sources × residuality model

How the catalogs in this folder update [`residuality-erm-examples/uae.md`](../residuality-erm-examples/uae.md). Assumptions, chaotic nodes, and §7 triggers only. Not a re-run of the 100 stressors.

---

## Load-bearing assumptions

| Assumption | Best public sources | What you can actually see | Still dark |
|---|---|---|---|
| **A1** Dirham USD peg holds | CBUAE statistical bulletin (foreign assets vs monetary base, 70% cover rule); IMF AIV; IFS | Reserve stock, monetary base, bank FX positions, policy-rate import | Intervention tactics, which correspondent is the last one |
| **A2** Fujairah/ADCOP is enough | EIA CAB (1.8 mbpd ADCOP, 1.5 mbpd second line aimed 2027, 42 mb caverns); ADNOC ADCOP page; AIS Fujairah; STEO during a closure | Pipeline *existence*, tanker calls, wartime production drop (4.0→2.4 mbpd Mar–May 2026) | True spare capacity vs nameplate; whether the second line is steel in the ground |
| **A3** Expats keep coming | SCAD/FCSC/DDSE population; MOHRE observatory; ICP product rules; GRC tables; State TIP/HR | Stocks, some nationality/occupation splits, visa-product text | Flight *intent*, critical-role nationality mix, cohort-cancellation risk |
| **A4** AD–Dubai compact holds | Almost nothing official. Infer from CIT fights (MoF/FTA), DIFC recognition cases, dual-hub capex | Public rifts if they happen; GRE credit split | Court-level coordination. C-07 is a residue that cannot be verified from outside |
| **A5** Desal + cooling stay up | EWEC plant list; DEWA; TAQA; ENEC/FANR; EIA generation mix; Copernicus heat; Sentinel plant map | Plants, fuel mix, Barakah share (~25% electricity per ENEC; EIA 2024 gen: gas 71%, nuclear 23%, solar 5%) | Inventory-days of potable water; geographic dispersal; intake common-mode |
| **A6** Orderly succession | Public titles (Khaled; Hamdan); WAM statements | Named heirs | Loyalty maps of security organs. S-66 remains a structural gap |
| **A7** Hydrocarbons remain the fiscal backstop | **IMF AIV fiscal tables** (not FCSC GDP); EIA prices/production; MoF/FTA | Oil vs non-oil *revenue*; production; CIT/VAT path | SWF draw rules; ADIA line items; federal–emirate CIT split |
| **A8** Safe open hub brand | DLD; DP World; Emirates AR; DXB traffic; MoET tourism; FATF status; war-risk commentary (Lloyd's) | Throughput, visitors, property bid, grey-list status | Insurance appetite as a number; sending-state travel advisories as a *system* |
| **A9** Food/imports can be stored or rerouted | MoCCAE strategy docs; AIS/air-cargo; UN Comtrade | Strategy, some trade reroutes | **Tonnes in warehouses.** A9-as-inventory is not public |
| **A10** US security + dollar system | CRS RS21852; State; OFAC; CENTCOM; BIS; FATF | Posture language, designations, grey-list, US claims on UAE banks | Internal de-risking by correspondent banks; actual CENTCOM footprint changes until they are public |

---

## Three chaotic nodes (Step 6)

These are the couplings the ERM file says pull the UAE off the edge of chaos. Watch them as *systems*, not as single series.

### 1. Inhabitability (A5) — C-01, C-16, C-20

**See:** EWEC + DEWA + Etihad Water & Electricity plant rosters; FANR/ENEC for Barakah; EIA electricity mix; Sentinel/OSM for whether desal is one coast-road target set; Copernicus/NCM for wet-bulb and flood; DEWA/DLD after-action on 2024 flood.

**Cannot see:** Days of stored water; whether C-01 geographic bulkhead is real (S-87 algal bloom / S-38 swarm would reveal it).

**Live test:** A strike, a summer blackout, or a desal outage in the press + AIS/satellite on the plant. If operators also leave (A3), C-01 still running does not save the city (cascade 5 in `uae.md`).

### 2. Dollar / US sponsor (A1 + A10) — C-04, C-05, C-09, C-22

**See:** CBUAE bulletin (peg arithmetic); IMF AIV; FATF plenary; OFAC SDN adds of UAE names; BIS locational; CRS/State language on the security relationship.

**Cannot see:** A single US bank's correspondent memo; ADIA custody jurisdictions (S-96 attachability); whether extra-US air defence (C-22) is hardware (SIPRI) or a communiqué.

**Live test:** One OFAC package + a FATF signal + a CRS sentence on CENTCOM is four controls on one sponsor — the overloaded-node symptom.

### 3. Compact and families (A4 + A6) — C-07, C-08

**See:** Almost nothing. WAM, succession titles, a public policy split (tax, visas, foreign policy), DIFC/onshore case law.

**Cannot see:** The residue itself (rehearsed 72-hour charter, loyalty map, Supreme Council standing orders). `uae.md` already flags S-31/S-66/S-99 as structural if pre-commitment is absent. Open sources will not close that flag.

**Do not:** Fill the gap with Telegram rumour.

---

## Control portfolio — what is observable

| Control | Observable from open sources? | How |
|---|---|---|
| C-01 Inhabitability stack | **Partial** | Plant lists and fuel mix yes; stores and dispersal no |
| C-02 Hormuz bypass | **Yes, weakly** | ADCOP + AIS + EIA; second pipeline status is the 2027 question |
| C-03 Food reserve | **No** | Strategy docs only |
| C-04 Peg defence | **Yes** | CBUAE bulletin vs 70% rule; IMF |
| C-05 AML/UBO/correspondents | **Partial** | FATF grade and OFAC list yes; UBO *truth* and correspondent names no |
| C-06 Expat compact | **Partial** | Stocks and visa rules; not caps by nationality on critical roles |
| C-07 Compact council | **No** | |
| C-08 Succession charter | **No** | Titles only |
| C-09 SWF waterfall | **Partial** | Mubadala/ICD IFRS; ADIA ranges; Global SWF AUM; draw rules no |
| C-10 Neutral-hub pause-switches | **After the fact** | MoFA/WAM; trade data lag |
| C-11 Dual-hub aviation/ports | **Yes** | DP World, AD Ports, Emirates, ADS-B |
| C-12 Macroprudential property | **Partial** | DLD + CBUAE credit; developer caps no |
| C-13 Digital degrade-mode | **No** | Outage news only |
| C-14 OT segmentation | **No** | Reverse-orphan: claimed until a campaign proves otherwise |
| C-15 Authentic ruler channel | **Partial** | WAM/official accounts exist; public *pre-knowledge* of the channel is a survey question |
| C-16 Site redundancy + C-UAS | **Partial** | Satellite for dispersal; C-UAS is hardware rumour |
| C-17 Licence/emergency registry | **No** | |
| C-18 Ex-oil fiscal KPI | **Yes, via IMF** | Not via FCSC GDP |
| C-19 Complement-not-clone hub | **Indirect** | DIFC/ADX vs Tadawul; Emirates vs Saudia/Qatar; DLD vs NEOM press |
| C-20 Heat/flood operating mode | **Partial** | NCM + Copernicus + 2024 after-action; wet-bulb kill-switch as labour law is MOHRE/MoH |
| C-21 Knowledge capture | **No** | |
| C-22 Deterrence hedge | **Partial** | SIPRI transfers; CRS language; not a substitute for A10 |

Reverse-orphan watch from `uae.md` still holds: **C-14** and **C-01 dispersal** must be true in wiring and on the map. Satellite can audit dispersal; it cannot audit OT segmentation.

---

## §7 re-run triggers → watch sources

| Trigger in `uae.md` §7 | Watch |
|---|---|
| Succession event or prolonged ruler absence | WAM; official court accounts. Nothing else is reliable. |
| Strike or near-miss on desal, Fujairah, Jebel Ali, Barakah | Reuters/AP first; then AIS, Sentinel, FANR/ENEC, EWEC, DP World |
| Change in US security posture or secondary-sanctions practice | CRS RS21852 updates; State; OFAC SDN; CENTCOM |
| FATF or correspondent-bank action | FATF plenary calendar (possible 5th-round onsite 2026 / plenary Feb 2027); CBUAE; bank press |
| Dubai property drawdown >20% | **DLD monthly/quarterly** — this is the cleanest trigger in the set |
| Labour-corridor suspension | MOHRE; sending-state MFA (India/Pakistan/Philippines); IOM; airport outflows |
| Wet-bulb or flood exceeding 2024 | Copernicus/NCM; DEWA; DLD flood claims |
| Public AD–Dubai policy split | WAM vs Dubai Media Office; FTA/MoF CIT; DIFC case law |
| Loss or freeze of a major SWF custody jurisdiction | OFAC/EU/UK; court dockets (S-96); Mubadala/ICD notes; ADIA will not confirm |

Quarterly baseline (even without a trigger): IMF page → CBUAE latest bulletin → DLD → EIA CAB/STEO → FATF page → SCAD/FCSC GDP vs IMF fiscal.

---

## Do not use for

| Tempting source | Why not |
|---|---|
| FCSC non-oil GDP share as a fiscal fact | A7 is *revenue*. IMF fiscal tables. |
| ADIA Review as a custody/draw map | Ranges, not line items. C-09 unverifiable. |
| Anonymous Gulf Telegram on royal health | A6. WAM or nothing. |
| Global SWF AUM tweet without the table | Order of magnitude only; still not ADIA's number. |
| EIA capacity and ADNOC capacity as the same thing | 4.15 vs 4.85 mbpd in the 2026 CAB. |
| FATF grey-list *exit* (Feb 2024) as a permanent C-05 | Next-round onsite is the live test. |
| World Factbook | Public edition sunset Feb 2026. |
| People-search tools | Out of scope; see OSINT-Tools-Emirates. |

---

## Suggested quarterly pull (two hours)

1. IMF country page — any new AIV or staff concluding statement.
2. CBUAE latest statistics — foreign assets, monetary base, bank FX, credit to real estate.
3. DLD real-estate data — transaction value/volume, off-plan share.
4. EIA UAE CAB or STEO — production, Hormuz language, Fujairah.
5. FATF UAE page + plenary outcome if a plenary week.
6. OFAC SDN — new UAE names.
7. AIS snapshot — Fujairah and Jebel Ali callings vs last quarter.
8. SCAD + FCSC press — population and GDP; *do not* update A7 from these alone.
9. Mubadala/ICD financials if a reporting date passed; ADIA if a new Review.
10. One climate check — Gulf SST / wet-bulb vs last summer.

Write changes into `uae.md` only when a number or a trigger actually moved. This folder stays the source map; the ERM file stays the judgement.
