# Residuality Theory — Enterprise-Risk Analysis: Tesla, Inc.

*Method: Barry O'Reilly's Residuality Theory, adapted to enterprise risk per `residuality-enterprise-risk-management.md`. This is a stress-first analysis, not a conventional risk register. Attractors and stressors are in business language; mechanism detail lives in the residue. Catalogue controls referenced by `id` from `residuality/references/residue_library.md`.*

*Analysis date: 2026-07-05. Re-run cadence: quarterly, plus on trigger (see §7).*

---

## 1. Naive operating model

**What Tesla is, described as built — no mitigation theatre.**

### Value chain (where money and goods flow)

```
Raw materials (Li, Ni, Co, graphite, rare earths)
   → Cells (Panasonic / CATL / LG + in-house 4680)
      → Packs + drivetrain + vehicle assembly (Gigafactories: Fremont, Shanghai, Berlin, Texas)
         → Direct sales (no dealers: web + Tesla stores)
            → Delivery + Supercharger network + OTA software + Service
               → Ongoing revenue: FSD subscriptions, service, energy, regulatory credits
```

Parallel businesses share the same brand, capital pool, and management attention:
- **Vehicles** — the volume engine and cash generator.
- **Energy** — Powerwall (residential), Megapack (grid-scale storage), solar. Fast-growing, higher-margin, less brand-dependent.
- **Autonomy / AI** — FSD/Autopilot software, Dojo/AI training compute, robotaxi ambition. The valuation thesis lives here more than in the metal.
- **Charging** — Supercharger network, now opened via NACS (the connector licensed to and adopted by rivals as the North American standard).
- **Optimus** — humanoid-robot ambition; pre-revenue, capital- and attention-hungry.

### Core functions that keep the flow alive
- Battery raw-material procurement and cell supply contracting.
- Gigafactory production lines (four regions, each with regional concentration).
- Vehicle software: OTA delivery pipeline, over-the-air feature enablement/gating.
- Direct-sales order intake and delivery logistics (quarter-end delivery push is structural).
- Supercharger network operation + backend (auth, billing, session management).
- FSD/Autopilot development, validation, and fleet data ingestion.
- Regulatory-credit sales (selling emissions credits to other automakers).
- Service, warranty, and parts (vertically integrated, Tesla-controlled).

### Critical dependencies

**Internal**
- **Elon Musk** as CEO, chief engineer, brand, and capital-markets narrator — single point of concentration across strategy, product, and stock.
- Shanghai Gigafactory — the highest-volume, lowest-cost plant and the export hub for Europe/Asia.
- The shared OTA pipeline — one software channel touches nearly the whole fleet.
- A single valuation narrative: FSD + robotaxi + Optimus justify a multiple no pure automaker earns.

**External**
- Cell suppliers: Panasonic, CATL, LG — concentrated, partly China-based.
- Battery raw materials — geographically concentrated (lithium, nickel, cobalt, graphite, rare earths), much refined in China.
- China — as production base, as end market, and as home to the fiercest competitor (BYD). Triple exposure to one geopolitical variable.
- Regulators — NHTSA (recalls, FSD), EU, China (data, tariffs, market access).
- Regulatory-credit buyers — other automakers who need Tesla's credits *only until they electrify themselves*.
- Semiconductor supply (autonomy computer, ECUs) — much routed through Taiwan.

### Load-bearing assumptions (stated out loud)
1. EV demand keeps growing and Tesla keeps a premium share of it.
2. FSD/robotaxi arrives on a timeline that sustains the valuation multiple.
3. Musk remains available, effective, and a net-positive brand asset.
4. China remains open as base, market, and neutral ground — the plant runs and the market buys.
5. Regulatory credits remain a high-margin revenue line for years.
6. The OTA channel is a strength (feature velocity), not a systemic single point of failure.
7. Cell and raw-material supply scales with volume at acceptable cost.
8. The direct-sales model stays legal in Tesla's major markets.
9. The Supercharger/NACS lead stays a durable moat rather than a commoditized standard.
10. Buyers separate the product from the CEO's politics.

---

## 2. Exhaustive stressor set

66 stressors across all 9 categories, multiple passes each. Novelty 1 (on some register somewhere) → 5 (would not appear in any standard risk register). Black swans (novelty 5) marked ★.

| # | Stressor (one concrete sentence) | Category | Novelty |
|---|---|---|---|
| S-01 | A regulator declares the name "Full Self-Driving" deceptive, bans the term, and orders the feature disabled fleet-wide pending recertification, effective in 30 days. | Regulatory/legal | 4 |
| S-02 | A fatal Autopilot crash triggers a nationwide forced recall disabling driver-assist across the entire fleet via OTA. | Regulatory/legal | 3 |
| S-03 | The US EV tax credit is repealed and the regulatory-credit market collapses as rivals meet emissions targets themselves — a high-margin revenue line evaporates in a quarter. | Regulatory/legal | 2 |
| S-04 | The EU imposes retroactive tariffs on China-built EVs, hitting Shanghai-sourced Model 3 exports to Europe. | Regulatory/legal | 2 |
| S-05 | A cluster of US states enacts dealer-franchise laws forcing Tesla to sell through third-party dealers. | Regulatory/legal | 3 |
| S-06 | China enacts a data-localization law forcing all vehicle and camera data to stay in-country and blocking FSD training-data export. | Regulatory/legal | 3 |
| S-07 | A regulator rules that OTA-locked paid features (unlocking range/acceleration already in the car) are unfair and voids the practice. | Regulatory/legal | 4 |
| S-08 | Right-to-repair law forces Tesla to open diagnostics, parts, and service to third parties, eroding the service-revenue moat. | Regulatory/legal | 3 |
| S-09 | An autonomous-vehicle liability law shifts crash liability from the driver to the manufacturer, exposing Tesla to open-ended tort on every FSD mile. | Regulatory/legal | 4 |
| S-10 | A forced-labor / supply-chain due-diligence law blocks import of components whose material provenance Tesla cannot verify. | Regulatory/legal | 3 |
| S-11 | BYD undercuts Tesla globally with a cheaper, comparable EV and decisively takes the volume crown. | Market/competitive | 2 |
| S-12 | A legacy-automaker-plus-tech partnership ships a genuinely superior Level-4 robotaxi to key US cities first. | Market/competitive | 3 |
| S-13 | EV demand plateaus as buyers revert to hybrids, softening the entire category Tesla bet on. | Market/competitive | 2 |
| S-14 | A price war Tesla itself starts compresses vehicle margins below the level the growth story needs. | Market/competitive | 2 |
| S-15 | Rivals' NACS adoption plus third-party networks commoditize Supercharging and erase the charging moat. | Market/competitive | 3 |
| S-16 | Used-Tesla prices crash, damaging residual values, leasing economics, and new-buyer confidence. | Market/competitive | 3 |
| S-17 | CATL and Fluence win the large grid-storage contracts on price and delivery, stalling Megapack growth. | Market/competitive | 2 |
| S-18 | The brand becomes politically polarized and a measurable buyer segment boycotts over the CEO's public persona. | Market/competitive | 3 |
| S-19 | The insurance industry raises Tesla premiums (repair cost, theft, FSD risk), lifting total cost of ownership and cooling demand. | Market/competitive | 3 |
| S-20 | An Apple/Google-scale entrant ships a software-defined car with a superior digital ecosystem. | Market/competitive | 3 |
| S-21 | A bad OTA update bricks or degrades a large swath of the fleet simultaneously. | Technical/infrastructure | 3 |
| S-22 | The Dojo/AI training-compute program fails to deliver and the FSD capability roadmap stalls for years. | Technical/infrastructure | 3 |
| S-23 | A systemic battery defect with fire risk surfaces across a model year, forcing a physical recall. | Technical/infrastructure | 3 |
| S-24 | The Supercharger backend fails and strands drivers nationwide during a holiday travel peak. | Technical/infrastructure | 3 |
| S-25 | The vehicle cloud backend has a prolonged outage; app-based unlock, climate, and authentication fail across the fleet. | Technical/infrastructure | 3 |
| S-26 | The installed autonomy computer (a specific hardware generation) proves incapable of delivering promised FSD, requiring a mass retrofit. | Technical/infrastructure | 3 |
| S-27 | A robotaxi in commercial operation causes a fatality attributable to the autonomy stack. | Technical/infrastructure | 4 |
| S-28 | Elon Musk becomes unavailable — health, legal, or attention fully diverted to another venture. | Human/organisational | 4 |
| S-29 | Senior autonomy and AI talent departs en masse to a competitor or a well-funded startup. | Human/organisational | 3 |
| S-30 | A unionization drive succeeds at a US Gigafactory, changing labor-cost and flexibility assumptions. | Human/organisational | 2 |
| S-31 | A whistleblower leaks internal data alleging Tesla knew about a safety defect and suppressed it. | Human/organisational | 3 |
| S-32 | A court voids Musk's pay package again and a proxy revolt destabilizes leadership mid-cycle. | Human/organisational | 3 |
| S-33 | The CEO's other companies (X, xAI, SpaceX) entangle Tesla in cross-contamination — an advertiser boycott or scandal bleeds into the Tesla brand. | Human/organisational | 4 |
| S-34 | A security researcher demonstrates remote hijack and unlock of vehicles at scale, and the proof-of-concept goes viral. | Adversarial/abuse | 3 |
| S-35 | Ransomware halts production IT at a Gigafactory for days. | Adversarial/abuse | 2 |
| S-36 | FSD is fooled by adversarial road markings/stickers in a publicized stunt, undermining public trust. | Adversarial/abuse | 4 |
| S-37 | An insider at a supplier or at Tesla exfiltrates battery or autonomy IP to a Chinese competitor. | Adversarial/abuse | 3 |
| S-38 | Coordinated fraud rings exploit referral, warranty, and charging-credit systems at scale. | Adversarial/abuse | 3 |
| S-39 | GPS spoofing/jamming disrupts FSD and fleet navigation across a region. | Adversarial/abuse | 4 |
| S-40 | An earthquake or major disruption at Fremont (California fault zone) halts primary US output. | Physical/environmental | 3 |
| S-41 | Drought and water-permit restrictions constrain Gigafactory Berlin or Texas operations. | Physical/environmental | 3 |
| S-42 | An extreme cold snap publicizes EV range collapse and charging queues, denting the demand narrative. | Physical/environmental | 3 |
| S-43 | A key shipping lane (Red Sea or Panama) closes, spiking delivery times and cost for global vehicle and parts movement. | Physical/environmental | 3 |
| S-44 | A lithium or nickel price spike, or an export restriction from a producing nation, hits cell cost. | Supply-chain/vendor | 2 |
| S-45 | China restricts export of graphite, rare earths, or battery materials as geopolitical leverage. | Supply-chain/vendor | 3 |
| S-46 | A key cell supplier (Panasonic, CATL, or LG) suffers a quality or capacity failure, or renegotiates hard. | Supply-chain/vendor | 2 |
| S-47 | A sole-source tier-2 chip or component fails, idling a production line (a chip-shortage redux). | Supply-chain/vendor | 2 |
| S-48 | A key cell partner is drawn into a competitor's captive supply, shrinking Tesla's allocation. | Supply-chain/vendor | 3 |
| S-49 | The robotaxi launch scales faster than fleet ops can handle — cleaning, charging, incident response, and support are overwhelmed. | Scale/load | 4 |
| S-50 | China grows past a threshold share of production and sales, so one market's swing dominates group results. | Scale/load | 2 |
| S-51 | Optimus and robot ambitions absorb capital and management attention disproportionately, starving the core business. | Scale/load | 4 |
| S-52 | Charging demand at popular corridors outgrows Supercharger capacity as the fleet plus non-Tesla NACS access grows. | Scale/load | 3 |
| S-53 | Grid-interconnection queue backlogs stall Megapack deployments even as orders scale. | Scale/load | 3 |
| S-54 | Early Model S/X battery packs degrade at scale, testing the longevity reputation and warranty reserves. | Time/lifecycle | 3 |
| S-55 | The regulatory-credit line, long treated as incidental, is still load-bearing in the P&L when it structurally lapses. | Time/lifecycle | 3 |
| S-56 | Accumulated "FSD next year" promises mature into legal liability toward customers who prepaid years ago and never received it. | Time/lifecycle | 4 |
| S-57 | A vehicle platform reaches end-of-life with no compelling next-gen mass-market model ready to replace it. | Time/lifecycle | 3 |
| S-58 | Software support for older vehicles becomes uneconomic; abandoned cars sour brand loyalty and resale. | Time/lifecycle | 3 |
| S-59 ★ | A national TV investigation alleges — true or not — that Tesla batteries spontaneously combust in a common everyday scenario, and viral panic spreads regardless of the facts. | Physical/environmental | 5 |
| S-60 ★ | Overnight, the US and China mutually ban each other's auto and tech firms; Tesla loses the China market and Shanghai plant access simultaneously. | Regulatory/legal | 5 |
| S-61 ★ | An AI-generated deepfake of Musk announcing a fake recall or bankruptcy moves the stock and floods service centers before it is debunked. | Adversarial/abuse | 5 |
| S-62 ★ | A rival open-sources a genuinely competitive autonomy stack, collapsing the perceived proprietary premium of FSD. | Market/competitive | 5 |
| S-63 ★ | A competitor reaches solid-state batteries at mass-production scale, making Tesla's cell chemistry a generation behind overnight. | Technical/infrastructure | 5 |
| S-64 ★ | A sovereign state nationalizes or expropriates a lithium concession Tesla's supply plan depends on. | Supply-chain/vendor | 5 |
| S-65 ★ | A class of Tesla solar/energy installations is linked to house fires, triggering a mass-litigation and retailer-recall wave. | Adversarial/abuse | 5 |
| S-66 ★ | A livestreamed fatal crash involving a public figure in a Tesla dominates global media for weeks, fusing the brand with danger in public memory. | Physical/environmental | 5 |

**Diversity check:** 9/9 categories populated; per-category counts — Regulatory 12, Market 10, Technical 7, Human 6, Adversarial 8, Physical 6, Supply-chain 6, Scale 5, Time 5. Black swans (novelty 5): 8 (S-59…S-66), exceeding the ≥6 target.

---

## 3. Attractor + residue per stressor

*Attractor = do-nothing business end-state (business language). Residue = smallest control that survives it (catalogue `id` where one fits). Leans-on = the dependency/assumption the control needs.*

### S-01 — "FSD" name banned, feature disabled pending recertification
- **Attractor:** The headline autonomy feature goes dark, prepaid customers demand refunds, and the valuation thesis that rests on FSD takes a public credibility hit for as long as recertification drags.
- **Residue:** `feature_flag_kill_switch` around each autonomy capability plus a rename-ready product taxonomy, so the feature can be relabelled ("Supervised driver assist") and re-enabled per capability without a fleet rebuild.
- **Leans on:** Features are independently gateable and the underlying function is defensible under a compliant name.

### S-02 — Fatal Autopilot crash forces fleet-wide driver-assist recall
- **Attractor:** Every car loses its flagship differentiator at once; the safety narrative inverts and demand cools across markets until reinstatement.
- **Residue:** `progressive_rollout` + `shadow_traffic` for autonomy releases plus a documented safety-case dossier per feature, so reinstatement is a data-backed regulatory conversation rather than a years-long rebuild.
- **Leans on:** Validation data and disengagement telemetry are retained and defensible to NHTSA.

### S-03 — EV credit repeal + regulatory-credit market collapse
- **Attractor:** A near-pure-margin revenue line disappears in a quarter and reported profitability falls below what the multiple assumes.
- **Residue:** `per_minute_billing_path` thinking applied to revenue mix — do not let credit revenue be load-bearing; carry a costed plan that reaches target margin on vehicles + energy + services alone.
- **Leans on:** Core-product gross margin is independently modeled and monitored, not buried inside blended profit.

### S-04 — EU retroactive tariffs on China-built EVs
- **Attractor:** Shanghai-sourced European volume becomes uncompetitive on price and Tesla cedes EU share to local and Chinese rivals.
- **Residue:** Multi-plant sourcing flexibility — route EU demand to Berlin; a bespoke *production-origin switch* keeping each major market suppliable from more than one plant.
- **Leans on:** Berlin has spare capacity and homologation to absorb redirected EU demand.

### S-05 — US states force third-party dealer sales
- **Attractor:** The direct-sales margin and customer-relationship advantage erodes in affected states; pricing control and data ownership weaken.
- **Residue:** A pre-built franchise-compatible sales wrapper (agency model) that satisfies the letter of dealer law while Tesla keeps price-setting and the customer record.
- **Leans on:** Agency/gallery models are legally accepted as distinct from franchised dealers in the affected states.

### S-06 — China data-localization blocks FSD training-data export
- **Attractor:** The China fleet stops feeding the global autonomy model and China-market FSD forks or stalls, slowing the whole roadmap.
- **Residue:** `tenant_isolated_blast_radius` at the geography level — a China-resident data + training enclave that improves the local model without cross-border transfer.
- **Leans on:** In-region compute and a local model-training pipeline are already stood up in China.

### S-07 — OTA-locked paid features voided as unfair
- **Attractor:** A recurring upsell channel (paid range/acceleration unlocks) is closed and prior sales invite refund and false-advertising claims.
- **Residue:** `per_minute_billing_path` — record the entitlement dimension separately from the hardware so the offering can be re-expressed as a compliant configuration/subscription rather than a paywall on installed capability.
- **Leans on:** Feature entitlements are cleanly separable in billing from the physical hardware sold.

### S-08 — Right-to-repair opens service to third parties
- **Attractor:** The captive, high-margin service and parts stream erodes and out-of-network repairs raise warranty and safety-attribution disputes.
- **Residue:** `event_sourcing_audit_trail` on vehicle service history + certified-parts telemetry, so warranty and liability can be adjudicated even when third parties touch the car.
- **Leans on:** Vehicles emit tamper-evident service/part-provenance events Tesla can read after third-party work.

### S-09 — AV liability shifts from driver to manufacturer
- **Attractor:** Every autonomous mile becomes an open-ended tort exposure and insurers/lawyers reprice Tesla's whole autonomy business.
- **Residue:** `event_sourcing_audit_trail` — immutable per-mile driving-decision logs (the safety case as evidence) plus captive-insurance capital sized to the exposure.
- **Leans on:** Decision logs are retained, tamper-evident, and admissible; Tesla Insurance can absorb the tail.

### S-10 — Forced-labor / provenance law blocks unverifiable components
- **Attractor:** Affected components cannot legally enter key markets and lines stop until provenance is proven.
- **Residue:** `event_sourcing_audit_trail` extended to a battery-material passport — traceable chain-of-custody on high-risk inputs.
- **Leans on:** Suppliers can and will attest material origin down the chain.

### S-11 — BYD undercuts globally and takes the volume crown
- **Attractor:** Tesla loses the mass-market volume story and becomes a premium niche while a rival owns the category economics.
- **Residue:** A costed low-cost-platform option kept warm (design + supply pre-committed) so Tesla can defend an entry price band without inventing a division under fire.
- **Leans on:** A cheaper platform is engineered-ahead, not started only once share is already lost.

### S-12 — Rival ships superior L4 robotaxi first
- **Attractor:** The first-mover robotaxi narrative — a core pillar of the valuation — moves to a competitor and Tesla's autonomy premium compresses.
- **Residue:** `shadow_traffic` fleet-scale validation to compress Tesla's own time-to-credible-L4, plus a fallback business case that stands on driver-assist + vehicle sales without robotaxi primacy.
- **Leans on:** The fleet data advantage is real and convertible into a defensible L4 case.

### S-13 — EV demand plateaus, hybrids resurge
- **Attractor:** Category growth stalls, Tesla's growth multiple looks unjustified, and volume targets are missed for multiple quarters.
- **Residue:** Revenue diversification already in flight — energy + services + software as a de-correlated growth engine when vehicle volume flattens.
- **Leans on:** Energy and software can grow independently of vehicle-unit growth.

### S-14 — Self-inflicted price war crushes margin
- **Attractor:** Volume holds but per-unit economics fall below the growth story's floor and the equity story weakens.
- **Residue:** A margin-floor circuit breaker in pricing governance — cost-per-unit tracked against a hard floor that pauses further cuts.
- **Leans on:** True landed cost per unit is known in near-real-time, not just at quarter close.

### S-15 — NACS adoption + third-party networks commoditize charging
- **Attractor:** The Supercharger moat becomes a shared utility; the differentiation and lock-in it provided fade.
- **Residue:** Reposition Supercharging as a profit center (open-network access fees) rather than a moat — `per_minute_billing_path` billing flexibility across Tesla and non-Tesla users.
- **Leans on:** The network is monetizable per-session across all vehicle brands.

### S-16 — Used-Tesla prices crash
- **Attractor:** Residual values fall, leasing economics break, existing owners feel poorer, and new-buyer confidence in Tesla as a store of value drops.
- **Residue:** A residual-value backstop program (certified pre-owned + buyback floors) sized to stabilize the segment, funded from services.
- **Leans on:** Tesla can absorb resale-price support without breaking the services P&L.

### S-17 — CATL/Fluence win the big grid-storage contracts
- **Attractor:** Megapack loses the large-project pipeline and the energy-growth story slows to the pace of the vehicle business.
- **Residue:** Differentiate Megapack on integrated software + speed-to-deploy rather than cell price; a costed value-add layer (Autobidder, grid services) that competitors can't match on hardware alone.
- **Leans on:** The energy software layer is a genuine, defensible differentiator.

### S-18 — Brand polarizes; a buyer segment boycotts over the CEO
- **Attractor:** A structural slice of demand is lost in specific geographies and demographics, independent of product quality.
- **Residue:** Brand-CEO decoupling — elevate product/sub-brand identity (Model line, Energy) so purchase intent is not hostage to the founder's persona.
- **Leans on:** Product brands can carry demand semi-independently of the founder.

### S-19 — Insurers raise Tesla premiums, cooling demand
- **Attractor:** Total cost of ownership rises, the value proposition erodes at the margin, and price-sensitive buyers defect.
- **Residue:** Tesla Insurance as an in-house price backstop — telematics-priced cover that undercuts third-party premiums for safe drivers.
- **Leans on:** Tesla Insurance has the licensing, capital, and loss data to price competitively at scale.

### S-20 — Apple/Google-scale entrant with a superior car ecosystem
- **Attractor:** Tesla's software-defined-car edge is matched by a company with a deeper consumer ecosystem, and the digital differentiation narrows.
- **Residue:** Keep the OTA + fleet-learning cadence as the moat and integrate (not fight) dominant phone ecosystems where buyers demand it.
- **Leans on:** Tesla's software velocity stays ahead of a slower-moving but deeper-pocketed entrant.

### S-21 — Bad OTA update degrades a large swath of the fleet
- **Attractor:** A single software push turns a fleet-wide strength into a fleet-wide incident overnight; safety, trust, and licence-to-operate all take the hit.
- **Residue:** `progressive_rollout` (1%→10%→100% with automated abort) + `feature_flag_kill_switch` on every risky path; the staged channel is the residue, not a QA promise.
- **Leans on:** Vehicles report health metrics fast enough to abort before the wave reaches everyone.

### S-22 — Dojo/AI compute fails; FSD roadmap stalls for years
- **Attractor:** The autonomy timeline slips indefinitely and the portion of the valuation that rests on it deflates.
- **Residue:** `dependency_freeze_window` on the compute bet — a hedged compute strategy (external accelerators as fallback) so training is not hostage to one in-house program.
- **Leans on:** External compute is procurable at the scale Tesla's models need.

### S-23 — Systemic battery fire-risk defect forces physical recall
- **Attractor:** A physical recall (not fixable OTA) hits cash, floods service capacity, and the fire-safety story dents demand across model years.
- **Residue:** `event_sourcing_audit_trail` on cell provenance + battery telemetry to scope the defect narrowly to affected packs, plus warranty reserve sized to a bounded recall.
- **Leans on:** Battery telemetry can isolate the affected population rather than forcing a blanket recall.

### S-24 — Supercharger backend fails, stranding drivers at peak
- **Attractor:** Drivers are stranded during peak travel, the reliability advantage inverts publicly, and charging trust erodes.
- **Residue:** `local_autonomy` — chargers authorize and dispense on cached local policy for N hours when the backend is unreachable, reconciling billing later.
- **Leans on:** Each charging stall holds enough local state to operate offline and reconcile on reconnect.

### S-25 — Prolonged vehicle-cloud outage breaks app unlock/climate/auth
- **Attractor:** Owners can't reliably access or operate their cars via app, and the connected-car promise looks fragile in headlines.
- **Residue:** `unlock_redundancy` — the physical key card / NFC always works independent of cloud; `read_only_degraded_mode` for app features.
- **Leans on:** Every car ships with a fully offline access path that needs no backend.

### S-26 — Installed autonomy computer can't deliver promised FSD → mass retrofit
- **Attractor:** A hardware generation cannot honor the FSD that customers paid for, forcing costly retrofits and refunds and reopening the "promise vs delivery" wound.
- **Residue:** A hardware-retrofit entitlement policy defined in advance (who gets a free upgrade) so exposure is bounded and pre-provisioned, not litigated ad hoc.
- **Leans on:** The retrofit cost per affected car is known and reserved against.

### S-27 — Robotaxi fatality attributable to the autonomy stack
- **Attractor:** The commercial autonomy business faces suspension, the safety case is challenged in public, and the robotaxi thesis stalls.
- **Residue:** `event_sourcing_audit_trail` (immutable decision logs) + a per-city `feature_flag_kill_switch` to suspend and reinstate the service geographically without killing the whole program.
- **Leans on:** Robotaxi operations are geofenced and independently suspendable per city.

### S-28 — Musk unavailable (key-person shock)
- **Attractor:** Strategy, product direction, and the capital-markets narrative lose their anchor; the stock and morale wobble on the vacuum.
- **Residue:** `runbook_as_code` for succession — a named, rehearsed leadership-continuity plan and a decision-rights map that does not require the founder for day-to-day operation.
- **Leans on:** Deputies with real authority exist and are known to the board and market before the shock.

### S-29 — Mass exodus of autonomy/AI talent
- **Attractor:** The autonomy roadmap loses velocity and institutional knowledge as a cohort leaves for a rival or startup.
- **Residue:** `runbook_as_code` for critical model/pipeline knowledge (documented, not tacit) + retention hooks on the few genuinely irreplaceable individuals.
- **Leans on:** Key knowledge is captured in artifacts, not only in departing heads.

### S-30 — Union drive succeeds at a US Gigafactory
- **Attractor:** Labor cost and scheduling flexibility change structurally at a key plant, compressing the cost advantage.
- **Residue:** Multi-plant production flexibility (the same origin-switch as S-04) to rebalance load, plus early constructive labor engagement.
- **Leans on:** Volume can be rebalanced across plants without breaking delivery commitments.

### S-31 — Whistleblower alleges known-and-suppressed safety defect
- **Attractor:** A credibility and licence-to-operate crisis: regulators, plaintiffs, and press converge on the "they knew" narrative.
- **Residue:** `audit_log_immutability` on safety decisions + a real internal escalation/whistleblower channel, so the record shows issues were surfaced and acted on.
- **Leans on:** Safety concerns are genuinely logged and actioned, not just documented for optics.

### S-32 — Musk pay voided again + proxy revolt destabilizes leadership
- **Attractor:** Governance uncertainty and a possible founder-exit threat overhang the stock and freeze strategic decisions.
- **Residue:** A board-level governance-continuity plan (compensation and retention contingencies pre-agreed) so a court ruling doesn't become an existential cliff.
- **Leans on:** The board has pre-negotiated fallback arrangements that survive a voided package.

### S-33 — CEO's other ventures cross-contaminate the Tesla brand
- **Attractor:** A scandal or boycott at X/xAI/SpaceX bleeds into Tesla demand and reputation through the shared founder.
- **Residue:** Brand-CEO decoupling (same residue as S-18) — firewall Tesla's brand identity and governance from the founder's other entities.
- **Leans on:** Tesla's brand and board can be demonstrably separated from the founder's other companies.

### S-34 — Researcher demos remote hijack/unlock at scale; it goes viral
- **Attractor:** Public confidence in vehicle security collapses and regulators demand answers; the connected-car strength becomes a liability.
- **Residue:** `key_rotation_dual_accept` + rapid OTA security-patch channel — rotate credentials and push a fix fleet-wide fast, with `progressive_rollout` to avoid a bad-patch repeat.
- **Leans on:** Credentials are centrally rotatable and the OTA channel can ship a security fix within days.

### S-35 — Ransomware halts Gigafactory production IT for days
- **Attractor:** A plant stops, quarter-end delivery targets slip, and revenue recognition moves out of the period.
- **Residue:** `runbook_as_code` for IR + air-gapped/immutable backups enabling manual-degraded line operation for a bounded window.
- **Leans on:** Backups are isolated from the production network and lines can run in a degraded manual mode briefly.

### S-36 — FSD fooled by adversarial road markings in a viral stunt
- **Attractor:** Public trust in autonomy safety erodes on a vivid, shareable failure regardless of statistical safety.
- **Residue:** `shadow_traffic` + adversarial-case regression suite so known spoofs are caught pre-release; publish the safety response quickly.
- **Leans on:** Adversarial scenarios feed back into the validation set fast.

### S-37 — Insider exfiltrates battery/autonomy IP to a rival
- **Attractor:** The technical lead — a core justification for the premium — leaks to a competitor and the moat narrows.
- **Residue:** `audit_log_immutability` + `tenant_isolated_blast_radius` on crown-jewel IP (least-privilege, access logging) so exfiltration is detectable and prosecutable and blast radius is bounded.
- **Leans on:** Access to the most sensitive IP is compartmentalized and logged.

### S-38 — Fraud rings exploit referral/warranty/charging-credit systems
- **Attractor:** Margin leaks steadily through abuse of promotional and warranty programs.
- **Residue:** `charge_session_observability` + `idempotent_replay` on credit/referral issuance so abuse patterns are detectable and double-claims are blocked.
- **Leans on:** Credit and referral events are observable and de-duplicated at issuance.

### S-39 — GPS spoofing/jamming disrupts FSD and navigation regionally
- **Attractor:** Autonomy and navigation degrade across a region and the reliability story takes a public hit.
- **Residue:** `read_only_degraded_mode` for autonomy — a safe fallback (supervised manual, sensor-fusion without GPS) when positioning is untrusted.
- **Leans on:** The stack can detect untrusted GPS and degrade safely rather than act on bad position.

### S-40 — Earthquake halts Fremont primary US output
- **Attractor:** US production and quarter deliveries stop for the duration of recovery; revenue slips out of the period.
- **Residue:** Multi-plant production flexibility (origin-switch, same as S-04/S-30) — shift US-market volume to Texas.
- **Leans on:** Texas can absorb Fremont's US volume for the recovery window.

### S-41 — Drought/water restrictions constrain Berlin or Texas
- **Attractor:** A plant's output is capped by water permits and regional volume falls until resolved.
- **Residue:** Water-recycling capacity + permit-headroom monitoring so the plant runs under restriction; rebalance via origin-switch if not.
- **Leans on:** On-site water reuse covers enough of the shortfall to keep the line moving.

### S-42 — Cold snap publicizes range collapse and charging queues
- **Attractor:** A vivid seasonal failure narrative dents the demand story in cold markets.
- **Residue:** Product mitigation already fielded (preconditioning, heat-pump efficiency) + honest range communication; a `stale_data_marker`-style transparency on real-world cold range.
- **Leans on:** The fleet already has cold-weather mitigations to point to and communicate.

### S-43 — Key shipping lane closes, spiking delivery cost/time
- **Attractor:** Global vehicle and parts flow slows, deliveries slip, and landed cost rises across markets.
- **Residue:** Regional build-to-region sourcing (make where you sell) so cars and critical parts don't cross the choked lane; the origin-switch reduces cross-ocean dependence.
- **Leans on:** Each major market is substantially served by a regional plant and regional parts.

### S-44 — Lithium/nickel price spike or export restriction
- **Attractor:** Cell cost rises, vehicle margin compresses, and the cost-leadership story weakens.
- **Residue:** `dependency_freeze_window`-style supply hedging — multi-year offtake contracts + chemistry flexibility (LFP where nickel spikes).
- **Leans on:** Tesla can shift chemistry mix and has contracted volume ahead of spot exposure.

### S-45 — China restricts graphite/rare-earth/battery-material export
- **Attractor:** A material Tesla depends on becomes a geopolitical hostage and cell/motor production is capacity-constrained.
- **Residue:** Ex-China material qualification (second-source refining, synthetic graphite, rare-earth-free motor designs) kept warm as a pre-qualified fallback.
- **Leans on:** Non-China sources are pre-qualified before the restriction, not sourced after.

### S-46 — Key cell supplier quality/capacity failure or hard renegotiation
- **Attractor:** Cell allocation shrinks or costs jump, throttling vehicle output or margin.
- **Residue:** Multi-sourced cells (Panasonic + CATL + LG + in-house 4680) so no single supplier is a chokepoint — a `bulkhead` across cell vendors.
- **Leans on:** Designs accept cells from more than one supplier without re-engineering the pack.

### S-47 — Sole-source tier-2 chip/component fails, idling a line
- **Attractor:** A cheap part stops a whole line and delivery targets slip (the chip-shortage pattern).
- **Residue:** `dependency_freeze_window` + design-for-substitution — pre-qualified alternate parts and firmware-flexible ECUs (Tesla's 2021 chip-swap playbook as standing capability).
- **Leans on:** Firmware can be rewritten to accept substitute chips on short notice.

### S-48 — Cell partner drawn into a competitor's captive supply
- **Attractor:** Tesla's allocation from a shared supplier shrinks as a rival locks it up.
- **Residue:** In-house cell capacity (4680) + multi-sourcing as the strategic hedge against any one partner defecting.
- **Leans on:** In-house cell output can scale to cover a lost external allocation.

### S-49 — Robotaxi scales faster than fleet ops can handle
- **Attractor:** Service quality collapses under load — dirty, uncharged, stranded vehicles — and the robotaxi brand is damaged at launch.
- **Residue:** `per_tenant_quota` / `backpressure` on rollout — cap active robotaxi supply per city to what ops can service, expand only as ops capacity is proven.
- **Leans on:** Fleet-ops capacity is measured and rollout is gated on it, not on demand.

### S-50 — China grows past a threshold share of production and sales
- **Attractor:** One country's political or economic swing can move the whole group's results — concentration risk crystallized.
- **Residue:** Deliberate geographic rebalancing target (cap China's share of group volume) + the origin-switch flexibility to serve markets from elsewhere.
- **Leans on:** Non-China capacity can be grown fast enough to hold China's share below the cap.

### S-51 — Optimus/robotics absorbs capital and attention, starving the core
- **Attractor:** The cash-generating vehicle and energy businesses under-invest while a pre-revenue moonshot consumes the C-suite.
- **Residue:** Ring-fenced capital and management governance — Optimus funded from a bounded envelope with its own P&L, not from core-business oxygen.
- **Leans on:** The board enforces the funding ring-fence against founder enthusiasm.

### S-52 — Charging demand outgrows Supercharger capacity at corridors
- **Attractor:** Queues and wait times at popular corridors erode the reliability advantage as fleet + NACS access grows.
- **Residue:** `per_tenant_quota` / dynamic congestion pricing to shape demand + capacity-led buildout tied to utilization data.
- **Leans on:** Real-time utilization data drives both pricing and buildout priority.

### S-53 — Grid-interconnection backlogs stall Megapack deployments
- **Attractor:** Megapack orders can't be energized on schedule and the energy-growth story slips despite demand.
- **Residue:** Pipeline diversification across grid operators/regions + interconnection-status tracking so revenue isn't hostage to one queue.
- **Leans on:** Deployments are spread across enough jurisdictions to smooth any single backlog.

### S-54 — Early Model S/X packs degrade at scale
- **Attractor:** Longevity reputation is tested, warranty claims rise, and the "batteries last" story is challenged publicly.
- **Residue:** Warranty reserve modeling from fleet degradation telemetry + a battery-refurbishment/replacement pathway priced in advance.
- **Leans on:** Degradation telemetry gives an accurate forward warranty liability.

### S-55 — Regulatory-credit line still load-bearing when it structurally lapses
- **Attractor:** A revenue stream everyone assumed was incidental turns out to be propping up profit, and its disappearance breaks the earnings story.
- **Residue:** Same as S-03 — never let credit revenue be load-bearing; track core-product margin ex-credits explicitly every quarter.
- **Leans on:** Ex-credit profitability is a monitored, governed KPI.

### S-56 — Accumulated FSD promises mature into legal liability
- **Attractor:** Customers who prepaid years ago for undelivered FSD become a class-action and refund liability, and the "promise vs delivery" credibility gap becomes a legal fact.
- **Residue:** A pre-provisioned FSD-entitlement remediation policy (transferable entitlement, refund path, or delivered-capability schedule) bounding the exposure.
- **Leans on:** The prepaid-FSD liability is quantified and reserved, not open-ended.

### S-57 — Platform end-of-life with no next-gen mass-market model ready
- **Attractor:** An aging lineup loses to fresher rivals and there's a demand air-pocket until the next platform ships.
- **Residue:** A rolling platform-refresh cadence with the next mass-market model committed before the current one ages out.
- **Leans on:** Next-gen platform development stays ahead of current-platform decline.

### S-58 — Older-vehicle software support becomes uneconomic; cars abandoned
- **Attractor:** Long-time owners feel abandoned, loyalty and resale suffer, and the "your car improves over time" promise reverses.
- **Residue:** A defined minimum software-support lifetime commitment (a `dependency_freeze_window`-style guarantee) so support isn't silently dropped.
- **Leans on:** A minimum-support horizon is published and honored across model years.

### S-59 ★ — Viral TV allegation of spontaneous battery fires (true or not)
- **Attractor:** Panic-driven demand collapse and dealer-lot-style service surge regardless of the underlying facts; brand fused with danger.
- **Residue:** `event_sourcing_audit_trail` on fire/incident telemetry — pre-existing, credible fleet-safety data to rebut fast + a rehearsed crisis-comms runbook.
- **Leans on:** Real, independently credible fire-rate data exists and can be published within hours.

### S-60 ★ — Overnight mutual US-China auto/tech ban
- **Attractor:** Simultaneous loss of the China market and Shanghai plant access — the single largest concentrated shock to volume, cost, and growth at once.
- **Residue:** The China enclave (S-06) plus geographic rebalancing (S-50) as a standing hedge — no single geography can be allowed to be un-survivable if lost.
- **Leans on:** Ex-China capacity and a China-standalone operation both exist before the ban. **This is the residue Tesla is least able to field today — flag as a structural gap, not a claimed control.**

### S-61 ★ — Deepfake Musk announces fake recall/bankruptcy; markets and service centers react
- **Attractor:** A fabricated announcement moves the stock and floods service centers before it's debunked; trust in official channels is undermined.
- **Residue:** A signed/authenticated official-communications channel (verified announcements only) + `runbook_as_code` for rapid public rebuttal.
- **Leans on:** Customers and markets know and trust a single authenticated Tesla announcement source.

### S-62 ★ — Rival open-sources a competitive autonomy stack
- **Attractor:** FSD's proprietary premium collapses as credible autonomy becomes freely available, and a pillar of the valuation deflates.
- **Residue:** Reposition the moat from the algorithm to the data + fleet + integration — the parts an open-source stack can't replicate — and monetize FSD as a service, not a secret.
- **Leans on:** Tesla's fleet-data and vertical integration remain a defensible edge even when the model is commoditized.

### S-63 ★ — Competitor reaches mass-scale solid-state batteries
- **Attractor:** Tesla's cell chemistry becomes a generation behind overnight; range/cost/charging leadership passes to a rival.
- **Residue:** A pre-qualified next-chemistry option (solid-state R&D + supplier relationships kept warm) so Tesla can fast-follow rather than restart.
- **Leans on:** Tesla has a credible solid-state path in R&D or via a supplier before a rival ships at scale.

### S-64 ★ — Sovereign nationalizes a lithium concession Tesla depends on
- **Attractor:** A planned material supply is expropriated and the cell-cost/volume plan built on it is voided.
- **Residue:** Geographic + chemistry diversification of raw materials (same hedge as S-44/S-45) so no single concession is load-bearing.
- **Leans on:** Material supply is spread across enough jurisdictions that one seizure is absorbable.

### S-65 ★ — Tesla solar/energy installs linked to house fires; mass litigation
- **Attractor:** The energy business faces a retailer-recall and class-action wave, and the fire narrative contaminates the whole brand (vehicles included).
- **Residue:** `event_sourcing_audit_trail` on install/inspection records + a bounded remediation program, scoping liability to affected installs rather than the whole base.
- **Leans on:** Install and inspection records isolate the affected population.

### S-66 ★ — Livestreamed fatal crash of a public figure dominates media for weeks
- **Attractor:** The brand fuses with danger in public memory on an emotionally overwhelming, endlessly replayed event, independent of statistical safety.
- **Residue:** Same as S-59 — pre-existing credible safety data + a rehearsed, empathetic crisis-comms runbook that doesn't argue statistics into grief.
- **Leans on:** A crisis-comms capability exists that can respond within hours, not days.

---

## 4. Deduped control portfolio

The 66 residues collapse into **21 controls**. A handful carry most of the risk.

| Control | Risks covered | Owner-role | Leans on (dependency/assumption) | Notes |
|---|---|---|---|---|
| **C-01 Multi-plant production origin-switch** | S-04, S-30, S-40, S-41, S-43, S-50, S-60 | COO / VP Manufacturing | Each major market is servable from ≥2 plants with spare capacity + homologation | Merged four "shift volume to another plant" residues. Load-bearing for geopolitics *and* physical shocks. |
| **C-02 Staged OTA release + kill switches** (`progressive_rollout`, `feature_flag_kill_switch`, `shadow_traffic`) | S-01, S-02, S-21, S-27, S-34, S-36 | VP Vehicle Software | Fleet reports health fast enough to abort; features independently gateable | The single most load-bearing technical control; touches safety, security, and autonomy. |
| **C-03 Immutable audit / decision-log trail** (`event_sourcing_audit_trail`, `audit_log_immutability`) | S-08, S-09, S-10, S-23, S-27, S-31, S-37, S-59, S-65 | Chief Safety / Legal | Logs retained, tamper-evident, admissible; suppliers attest provenance | Highest-coverage control (9 risks). Evidence base for safety, liability, provenance, forensics. |
| **C-04 Revenue-mix diversification & ex-credit margin KPI** (`per_minute_billing_path` thinking) | S-03, S-13, S-17, S-55 | CFO | Core-product margin modeled independently of credits; energy grows on its own | Merged the "don't let a line be load-bearing" residues across credits and category demand. |
| **C-05 Flexible billing / entitlement dimension** (`per_minute_billing_path`) | S-07, S-15, S-52 | VP Charging / Commercial | Entitlements separable from hardware; network monetizable per-session across brands | |
| **C-06 Multi-source cells + in-house 4680** (`bulkhead`) | S-46, S-48 | VP Battery Supply | Packs accept cells from ≥2 suppliers without re-engineering | |
| **C-07 Raw-material geographic + chemistry diversification** (`dependency_freeze_window`) | S-44, S-45, S-64 | VP Raw Materials | Chemistry mix shiftable (LFP/Ni); ex-China refining pre-qualified | LFP-vs-nickel flexibility is the concrete lever. |
| **C-08 Design-for-substitution + firmware-flexible ECUs** (`dependency_freeze_window`) | S-47 | VP Electrical Eng | Firmware rewritable to accept substitute chips fast | Tesla's real 2021 chip-swap playbook, made a standing capability. |
| **C-09 China data/training enclave** (`tenant_isolated_blast_radius`) | S-06, S-60 | VP China / Data | In-region compute + local training pipeline exist | |
| **C-10 Geographic concentration cap** | S-50, S-60 | CEO / Board strategy | Non-China capacity growable to hold China share below cap | Governance target, not a product; partly aspirational today. |
| **C-11 Offline-capable chargers** (`local_autonomy`) | S-24 | VP Charging | Stall holds local state to auth/dispense offline and reconcile later | |
| **C-12 Offline vehicle access + read-only degraded app** (`unlock_redundancy`, `read_only_degraded_mode`) | S-25, S-39 | VP Vehicle Software | Every car has a fully offline access path; stack degrades safely without GPS | |
| **C-13 Key-person / leadership continuity** (`runbook_as_code`) | S-28, S-29, S-32 | Board / CHRO | Deputies with real authority + captured knowledge exist pre-shock | Covers founder *and* talent-cohort loss. |
| **C-14 Brand-CEO decoupling** | S-18, S-33 | CMO / Board | Product sub-brands carry demand semi-independently of the founder | Partly aspirational — Tesla brand is unusually founder-fused today. |
| **C-15 Warranty-reserve + remediation policy (battery, HW retrofit, FSD entitlement)** | S-23, S-26, S-54, S-56 | CFO / Legal | Telemetry gives accurate forward liability; exposures quantified and reserved | Merged three "bounded, pre-provisioned remediation" residues. |
| **C-16 Security patch + credential rotation** (`key_rotation_dual_accept`) | S-34 | CISO | Credentials centrally rotatable; OTA can ship security fix in days | Couples tightly with C-02 (same OTA channel). |
| **C-17 IR + immutable backups + degraded-manual line** (`runbook_as_code`) | S-35 | CISO / COO | Backups air-gapped; lines can run manual-degraded briefly | |
| **C-18 Crisis-comms + authenticated-channel runbook** (`runbook_as_code`) | S-59, S-61, S-66 | Comms / IR | Credible safety data publishable in hours; trusted authenticated announcement source | Covers reputational black swans; leans on C-03 for the underlying data. |
| **C-19 Rollout-capacity gating** (`per_tenant_quota`, `backpressure`) | S-38, S-49, S-52 | VP Ops / VP Autonomy Ops | Ops capacity measured; rollout/issuance gated on it | Covers robotaxi ops, charging congestion, and fraud-rate abuse. |
| **C-20 Kept-warm strategic options (low-cost platform, next chemistry, next platform, compute hedge)** | S-11, S-22, S-57, S-62, S-63 | Chief Product / Chief Engineer | Fast-follow options engineered-ahead, not started under fire | Merged five "pre-committed fallback capability" residues — the anti-complacency portfolio. |
| **C-21 In-house insurance + residual-value backstop** | S-16, S-19 | VP Financial Products | Tesla Insurance has capital/licensing/loss data to price at scale | |

**Merge history & residual gaps.** C-01, C-04, C-15, C-20 are aggressive merges of same-shape residues wearing different product names — the shrinkage (66 → 21) is the finding. Uncovered on their own: **S-05** (dealer-franchise laws — the agency-model wrapper is a bespoke legal residue owned by General Counsel, not merged), **S-20** (ecosystem entrant — the residue is "keep OTA cadence ahead," a strategic posture more than a control), **S-42** (cold-range — product mitigation already fielded), **S-51** (Optimus ring-fence — a governance discipline owned by the Board), **S-53** (interconnection-queue diversification — owned by VP Energy). These are noted as thin-coverage below.

---

## 5. Contagion / systemic-risk analysis

### Top cascade paths (shared dependency/assumption → controls that fail together)

1. **The OTA channel is one dependency.** C-02 (staged releases), C-16 (security patching), and parts of C-12 (degraded-app behavior) all ride the same over-the-air pipeline. If that pipeline is itself compromised or poisoned (the S-21 / S-34 nightmare combined), the very control meant to contain a bad push is the vector — Tesla's biggest strength and biggest single point of correlated failure are the same channel.

2. **China is one dependency behind four controls.** C-01 (origin-switch assumes non-China plants absorb volume), C-06/C-07 (cell and material supply, much China-refined), C-09 (data enclave), and C-10 (concentration cap) all lean on the same geopolitical variable. An S-60-class US-China rupture fails production flexibility, cell supply, material supply, *and* the China market at once — the deltas below target this first because it is the least-survivable correlated failure.

3. **"Musk is a net-positive, available asset" is one assumption behind three controls.** C-13 (continuity), C-14 (brand decoupling), and the governance target in C-10 all lean on the founder question. An S-28 + S-32 + S-33 cluster (unavailable, governance crisis, cross-contamination) collapses leadership continuity, brand, and strategic decision-making together — and C-14 is only partly real today, so the cushion is thin.

4. **The immutable-log trail (C-03) is a shared upstream for the crisis-comms control (C-18).** C-18's ability to rebut viral safety allegations (S-59, S-61, S-66) *depends on* C-03 having captured credible safety data first. If C-03 is incomplete or not independently credible, C-18 has nothing to publish — two of the reputational black swans lose their only defense simultaneously. A single upstream data-quality failure de-fangs the entire reputational-crisis response.

5. **"Fast-follow options are actually kept warm" is one assumption behind C-20's five risks.** C-20 covers low-cost platform (S-11), compute hedge (S-22), next platform (S-57), open-source autonomy (S-62), and next chemistry (S-63). If the organization is not genuinely engineering these ahead — if they are slideware, not warm options — one strategic-surprise event finds *all five* unfielded. This control's coverage is only as real as the R&D discipline behind it, which is unobservable from the outside.

6. **Quarter-end delivery push is a shared timing assumption.** C-01, C-17, and the production side of the model all lean on hitting quarter-end delivery targets. Any plant-stopping shock (S-35 ransomware, S-40 earthquake, S-43 lane closure) lands hardest at quarter-end and pushes revenue across the reporting boundary — the controls contain the operational damage but not the earnings-narrative damage, which is what actually moves the stock.

7. **Warranty/remediation reserves (C-15) all lean on "telemetry gives accurate forward liability."** If degradation or defect telemetry is wrong or gamed, the battery-recall (S-23), HW-retrofit (S-26), fleet-degradation (S-54), and prepaid-FSD (S-56) reserves are all mis-sized together — a single actuarial-assumption error under-reserves four exposures at once.

### Orphan controls (map to no live risk)
None. Every control in §4 maps to ≥1 live stressor. This is itself a signal — the portfolio was derived from the stressors, so there is no accumulated risk-theatre here (unlike a legacy register). Watch that C-14 (brand decoupling) and C-10 (concentration cap) don't become *reverse* orphans: controls claimed but not actually fielded.

### Under-covered stressors (single-control or thin coverage)
- **S-60 (US-China rupture)** — the black swan with the weakest genuine residue. C-01/C-09/C-10 all *assume* an ex-China capability that is only partially real today. Flagged in §3 as a structural gap, not a claimed control.
- **S-05 (dealer-franchise laws)** — single bespoke legal residue (agency wrapper), owned by General Counsel, no backup.
- **S-51 (Optimus starves the core)** — covered only by a Board-level funding-discipline residue; there is no operational control if governance fails to enforce the ring-fence.
- **S-20 (ecosystem entrant)** — the residue is a strategic posture ("stay ahead"), not a fieldable control. Thinnest coverage in the set.
- **S-53 (interconnection backlogs)** — single control, energy-specific, no redundancy.

---

## 6. Resilience regime verdict

**Verdict: edge of chaos, tilting toward chaotic on its concentration axes.**

Tesla is *not* frozen. It is one of the least over-controlled large enterprises in existence — it runs lean, ships fast, and absorbs novelty with product velocity rather than bureaucratic exception-handling. The stressor set did not need a bespoke exception per event; most stressors mapped onto a small number of genuinely load-bearing, loosely-coupled controls (66 → 21). That shrinkage and the absence of orphan controls are hallmarks of an edge-of-chaos system: few controls, each doing real work.

But two things pull it toward chaotic. First, **concentration**: the contagion analysis shows the *same* dependencies — the OTA channel, China, and the founder — sitting behind clusters of four, four, and three controls respectively. In a chaotic system "one shared dependency shows up in half the coupling matrix"; Tesla has three such dependencies, and each is behind a would-be-systemic cascade. Second, **the valuation narrative is itself a shared assumption** — FSD/robotaxi/Optimus optimism prices the equity, so several otherwise-operational stressors (S-22, S-26, S-56, S-62) transmit straight to the cost of capital, coupling technical delivery to financial survival in a way a normal automaker doesn't experience.

**Three concrete deltas to move it back toward the resilient edge:**

1. **Decouple the China dependency (the single most brittle coupling).** Make C-01/C-09/C-10 real rather than assumed: fund enough ex-China cell, material, and vehicle capacity that losing China is survivable-with-pain, not existential. This is the delta with the largest resilience payoff because it de-correlates four controls at once. Today it is the residue Tesla is least able to field.

2. **Break the OTA-channel monoculture.** The channel that contains a bad push (C-02) and the channel that ships a security fix (C-16) are the same pipe that could deliver the poison (S-21/S-34). Add an out-of-band rollback/attestation path so the containment control does not share fate with the failure vector — decouple the two ends of the OTA pipeline.

3. **Make brand-CEO decoupling (C-14) an actual, measured program, not a claimed control.** It currently leans on an assumption ("product carries demand independent of the founder") that the polarization stressors (S-18, S-33) directly attack, and it is one of two controls at risk of being reverse-orphans. Elevating product/sub-brand identity so demand survives a founder shock is the cheapest of the three deltas and addresses the human-dependency cascade.

*Caveat (per playbook): the regime read is a directional heuristic about brittleness, not a predicted incident rate. Re-run quarterly and on trigger.*

---

## 7. Cadence & triggers

- **Re-run cadence:** quarterly.
- **Trigger events forcing a fresh pass regardless of cadence:** any change in Musk's role or availability; a fatal Autopilot/robotaxi incident; a US-China trade or market-access shift; new NHTSA/EU/China AV or data regulation; loss or hard renegotiation of a cell supplier; robotaxi commercial launch; a material move in the regulatory-credit market; entry into a new manufacturing geography; M&A activity.
- **Artefact owner:** Chief Risk Officer (or CFO's office if no CRO), distinct from the individual control owners in §4.

---

## Completeness pass — additional stressors

*Second-pass sweep for stressors the first 66 missed. Same method and template. Numbering continues from S-67; existing content is untouched. Novelty 1 (on some register somewhere) → 5 (would not appear in any standard register). These are deliberately biased toward under-mined Tesla-specific angles — the financial/valuation reflexivity, the energy-business tail, the CEO-as-institution mechanics, and the accounting/insurance internals — plus a few low-novelty items the first pass simply skipped.*

### New stressor set

| # | Stressor (one concrete sentence) | Category | Novelty |
|---|---|---|---|
| S-67 | Foreign-Entity-of-Concern battery-sourcing rules strip Tesla vehicles of the US consumer credit because their cell/material content traces to a Chinese entity, raising the effective sticker price overnight. | Regulatory/legal | 3 |
| S-68 | A safety regulator mandates sensor redundancy (radar/lidar) for driver-assist, invalidating the vision-only bet and forcing a hardware retrofit or feature disablement. | Regulatory/legal | 4 |
| S-69 | The EU AI Act (or an equivalent) classifies FSD as high-risk AI, gating European deployment behind conformity assessment, documentation, and expanded liability. | Regulatory/legal | 3 |
| S-70 | A state attorney general or DMV wins a false-advertising judgment over "Autopilot"/"FSD" marketing, forcing refunds and ad changes and handing other states a template. | Regulatory/legal | 3 |
| S-71 | A flagship-city utility/transport commission denies or revokes the robotaxi operating permit on process grounds before any incident, stalling the launch narrative. | Regulatory/legal | 3 |
| S-72 | A utility regulator slashes net-metering and virtual-power-plant compensation, collapsing the economics that drive residential solar and Powerwall demand. | Regulatory/legal | 3 |
| S-73 | A biometric/data-privacy law (GDPR-style or state) over interior- and exterior-camera footage forces feature disablement and fines and curtails FSD data collection. | Regulatory/legal | 3 |
| S-74 | Chinese nationalist backlash bans Tesla from government and military compounds and a patriotic buy-domestic wave shifts China buyers to BYD, softening the largest market for non-product reasons. | Market/competitive | 3 |
| S-75 | A rate and auto-loan-affordability shock prices mainstream buyers out of EVs, hitting Tesla's volume-dependent model harder than premium rivals. | Market/competitive | 2 |
| S-76 | A cheaper next-generation Tesla cannibalizes Model 3/Y sales and average selling price without adding net new volume, compressing revenue and margin. | Market/competitive | 3 |
| S-77 | Having abandoned "never advertise," Tesla now depends on paid demand generation, and a rising customer-acquisition cost becomes a permanent margin line it never carried before. | Market/competitive | 3 |
| S-78 | A bloc of automakers or a charging network defects from NACS to a rival higher-power standard, fragmenting the standard Tesla championed. | Market/competitive | 3 |
| S-79 | An investigative exposé links Tesla's cobalt/lithium chain to child labor, triggering ESG-fund divestment and contaminating the "clean" brand — independent of any import ban. | Market/competitive | 3 |
| S-80 | A short campaign plus a credit downgrade spikes Tesla's cost of capital and closes the cheap-financing window that funds gigafactory and AI capex. | Market/competitive | 3 |
| S-81 | Tesla Insurance under-prices FSD and repair-cost risk, loss ratios explode, and reserves prove inadequate — the very backstop meant to protect demand becomes a capital hole. | Market/competitive | 4 |
| S-82 | A Megapack grid-storage thermal event/fire triggers a product recall and utilities pause Tesla energy procurement, stalling the energy-growth story. | Technical/infrastructure | 3 |
| S-83 | The in-house 4680 cell ramp stalls on yield, leaving Cybertruck and next-gen cost targets unmet and forcing fallback to external cells. | Technical/infrastructure | 3 |
| S-84 | A statistically real vision-only failure mode (sun glare, fog) is proven and forces operational-domain restrictions on FSD, narrowing where autonomy is allowed to work. | Technical/infrastructure | 3 |
| S-85 | A high-profile Cybertruck-specific defect and recall tarnishes the halo model and the build-quality reputation at once. | Technical/infrastructure | 3 |
| S-86 | A self-inflicted mass layoff of a critical team (e.g., the Supercharger org) guts execution capacity and walks institutional knowledge out the door. | Human/organisational | 3 |
| S-87 | Employees share interior-camera footage and customer PII, and the insider privacy scandal draws regulatory fines and collapses trust in the connected-car promise. | Human/organisational | 3 |
| S-88 | The CEO's formal government/political office creates a conflict-of-interest backlash that costs Tesla fleet and government contracts and invites targeted regulatory scrutiny. | Human/organisational | 4 |
| S-89 | A sharp TSLA decline triggers margin calls on shares Musk pledged as loan collateral, and forced selling accelerates the fall in a reflexive doom loop that also threatens founder control. | Human/organisational | 4 |
| S-90 | Eco-activist arson or sabotage on gigafactory infrastructure (power, water) halts production and raises the standing security cost of every plant. | Adversarial/abuse | 3 |
| S-91 | A typhoon or flood shuts the Shanghai gigafactory and its export port — the highest-volume plant and the export hub — for weeks. | Physical/environmental | 3 |
| S-92 | An activist legal challenge revokes or blocks the Berlin environmental permit over groundwater, capping European capacity and freezing expansion. | Physical/environmental | 3 |
| S-93 | A single-source supplier goes bankrupt (insolvency, not quality), idling a line until it is re-sourced. | Supply-chain/vendor | 2 |
| S-94 | The corporate product-liability and property insurance market hardens against AV makers, and cover becomes unaffordable or unavailable, forcing Tesla to self-insure a tail it cannot fully price. | Supply-chain/vendor | 3 |
| S-95 | As the fleet grows, service-center and mobile-service capacity can't keep up; wait times balloon and owner satisfaction, loyalty, and resale suffer. | Scale/load | 3 |
| S-96 | Built-ahead gigafactory capacity runs well below utilization in a demand air-pocket, and fixed-cost deleverage craters gross margin. | Scale/load | 3 |
| S-97 | A wave of out-of-warranty non-battery build-quality claims (suspension, body) exceeds reserves and reopens the quality reputation. | Time/lifecycle | 3 |
| S-98 | Older Superchargers and connectors need costly retrofit as voltage and standards evolve, a capital drag and an owner-goodwill problem. | Time/lifecycle | 2 |
| S-99 | A "nickel-and-diming" narrative around feature subscriptions (connectivity, monthly FSD) damages loyalty and softens repeat demand. | Time/lifecycle | 3 |
| S-100 | The auditor or SEC forces a restatement of deferred FSD revenue as undelivered performance obligations balloon, an earnings-and-credibility hit. | Time/lifecycle | 3 |
| S-101 | An Optimus demo is exposed as teleoperated, or a robot injures a worker, causing investor whiplash on the AI-narrative premium plus safety-regulatory scrutiny. | Technical/infrastructure | 3 |
| S-102 | A concentrated treasury or digital-asset holding swings reported earnings on mark-to-market and invites scrutiny, adding noise to the equity story. | Market/competitive | 2 |
| S-103 | Residual-value writedowns and lease/loan defaults hit Tesla's own captive-finance book, turning a demand tool into a balance-sheet loss when used values fall. | Market/competitive | 2 |

**Diversity check (new set only):** 9/9 categories populated — Regulatory 7, Market 10, Technical 5, Human 4, Adversarial 1, Physical 2, Supply-chain 2, Scale 2, Time 4. The new pass is deliberately skewed to Regulatory/Market/Financial because that is where the first pass, which leaned Technical/Adversarial, was thinnest — Adversarial and Physical are near-saturated by S-01…S-66 and yield few genuinely-new items here.

### Attractor + residue per new stressor

*Same convention: Attractor = do-nothing end-state; Residue = smallest surviving control (catalogue `id` reused where one fits); Leans-on = the dependency/assumption the control needs.*

#### S-67 — FEOC battery-sourcing strips the consumer credit
- **Attractor:** The effective US price of affected trims jumps by the credit amount overnight, demand for those configs drops, and rivals with compliant sourcing win the price-sensitive buyer.
- **Residue:** `event_sourcing_audit_trail` extended into a battery-material passport with a per-VIN eligibility flag, plus a pre-qualified FEOC-compliant sourcing lane kept warm (same provenance + ex-China hedge as S-10/S-45).
- **Leans on:** Cell and material sourcing can be switched to a compliant lane per market before eligibility bites.

#### S-68 — Sensor-redundancy mandate invalidates vision-only
- **Attractor:** The vision-only fleet is non-compliant for driver-assist/AV, forcing a costly retrofit or feature disablement, and the "cameras are enough" thesis is regulatorily rejected.
- **Residue:** A kept-warm sensor-add option (radar/lidar reintegration path preserved in the platform) + `feature_flag_kill_switch` to degrade to a compliant ODD, with a bounded retrofit-entitlement reserve (as S-26).
- **Leans on:** The platform retains wiring and compute headroom to re-add a sensor without a full redesign.

#### S-69 — EU AI Act classifies FSD as high-risk
- **Attractor:** European FSD rollout is gated behind conformity assessment and documentation, delaying or curtailing European autonomy revenue.
- **Residue:** `event_sourcing_audit_trail` doubling as the AI-Act conformity-evidence base (the safety case *is* the technical documentation) + a per-region `feature_flag_kill_switch` to ship a compliant EU variant.
- **Leans on:** The same decision-logs Tesla already keeps satisfy AI-Act documentation demands.

#### S-70 — State AG false-advertising judgment on autonomy marketing
- **Attractor:** Forced marketing changes and refunds in that state, plus a template other states and plaintiffs copy.
- **Residue:** The rename-ready product taxonomy (same as S-01) + `event_sourcing_audit_trail` on marketing claims versus delivered capability + a pre-provisioned refund path (as S-56).
- **Leans on:** Capability claims are separable and evidence-backed against what shipped.

#### S-71 — Robotaxi permit denied/revoked pre-incident on process grounds
- **Attractor:** Launch slips in a flagship city on procedural grounds, denting the robotaxi timeline that the valuation leans on.
- **Residue:** A multi-jurisdiction launch pipeline so no single city's permit is load-bearing, plus a `runbook_as_code` regulatory-engagement playbook per city.
- **Leans on:** Several cities are in the permitting pipeline in parallel, not one flagship bet.

#### S-72 — VPP/net-metering compensation reversal
- **Attractor:** Residential solar + Powerwall economics break where a regulator cuts export/VPP payments, and residential-energy demand in that market falls.
- **Residue:** Value-stack diversification for residential energy (backup resilience + time-of-use arbitrage + grid services) so the offer isn't hostage to one subsidy; `per_minute_billing_path`-style flexible value accounting.
- **Leans on:** The product has non-subsidy value propositions to fall back on.

#### S-73 — Camera data-privacy law forces feature disablement
- **Attractor:** Interior/exterior camera features are disabled in a jurisdiction with fines, and FSD data collection there is curtailed.
- **Residue:** `tenant_isolated_blast_radius` at the geography level + on-device processing/data-minimization so cameras function without exporting identifiable footage; `feature_flag_kill_switch` per region.
- **Leans on:** Camera features can run on-device without cloud footage export.

#### S-74 — China nationalist backlash shifts buyers to domestic
- **Attractor:** Tesla is banned from sensitive compounds and a patriotic wave moves China buyers to BYD; the single largest market softens for reasons product quality can't fix.
- **Residue:** Localized China brand/ops (China-market identity + the data enclave of S-06) + geographic rebalancing (S-50) so a China share loss is absorbable. **As with S-60, the ex-China absorption capacity is only partly real today — flag as a structural gap, not a fielded control.**
- **Leans on:** Ex-China demand can grow to offset China share loss.

#### S-75 — Rate/affordability shock prices buyers out
- **Attractor:** Financing costs price mainstream buyers out of EVs and the volume-dependent model misses targets across quarters.
- **Residue:** In-house financing/lease flexibility (subsidized APR, cheaper trims) + the kept-warm low-cost platform (S-11) to defend an affordable entry band.
- **Leans on:** Tesla can flex financing terms and actually field a genuinely cheaper model.

#### S-76 — Cheaper next-gen model cannibalizes ASP without net volume
- **Attractor:** A new low-price model steals Model 3/Y sales and cuts average selling price without expanding the market, compressing revenue and margin.
- **Residue:** Deliberate portfolio segmentation + the margin-floor circuit breaker (S-14) tracking blended ASP so trade-down is caught early.
- **Leans on:** The lineup is segmented so a cheaper model grows the market rather than converting existing buyers downward.

#### S-77 — Advertising-dependency reversal raises structural CAC
- **Attractor:** The zero-marketing-cost advantage is gone and a rising customer-acquisition cost becomes a permanent margin line Tesla never carried.
- **Residue:** Treat CAC as a governed KPI with an efficiency floor (don't let paid demand become load-bearing) + reinvest in organic/referral engines.
- **Leans on:** Referral and organic demand channels still exist to fall back on.

#### S-78 — NACS standard fragmentation as rivals defect
- **Attractor:** A bloc of automakers or a network backs a rival higher-power standard, fragmenting the standard Tesla championed and eroding the moat via splintering rather than commoditization.
- **Residue:** Multi-standard/upgradeable Supercharger hardware + per-session monetization across standards (`per_minute_billing_path`); compete on network UX, not connector lock-in.
- **Leans on:** Charging hardware is field-upgradeable to competing standards.

#### S-79 — Child-labor ESG exposé triggers divestment
- **Attractor:** ESG funds divest, cost of capital rises, and the "clean" brand is contaminated by a supply-chain human-rights story — independent of any import ban.
- **Residue:** `event_sourcing_audit_trail` battery-material passport (same as S-10) as an audit-ready rebuttal + the crisis-comms runbook (C-18).
- **Leans on:** Material provenance is genuinely traceable and defensible before the story breaks.

#### S-80 — Cost-of-capital shock closes the cheap-capex window
- **Attractor:** A downgrade or short campaign raises financing cost and closes the cheap-capital window that funds gigafactory and AI capex.
- **Residue:** Capex-staging optionality (phase plant/AI spend so it can slow without breaking) + a liquidity-runway KPI; don't let growth capex assume permanently cheap capital.
- **Leans on:** Capex commitments are stageable, not all-or-nothing.

#### S-81 — Tesla Insurance actuarial blowup
- **Attractor:** The in-house insurer under-prices FSD/repair-cost risk, loss ratios explode, reserves prove inadequate, and the very backstop meant to protect demand (the residue of S-16/S-19) becomes a capital hole.
- **Residue:** Reinsurance/quota-share `bulkhead` capping tail exposure + telematics-priced reserves with a `stale_data_marker`-style loss-development monitor; ring-fence insurance capital from the core P&L.
- **Leans on:** Reinsurance is available and loss development is monitored honestly, not optimistically. *(Note: this is the flip side of the S-19 residue — the control there is the stressor here, a self-reference the portfolio should watch.)*

#### S-82 — Megapack thermal event forces recall; utilities pause procurement
- **Attractor:** A grid-storage fire triggers a product recall and utilities pause Tesla energy procurement, stalling the energy-growth story.
- **Residue:** `event_sourcing_audit_trail` on cell/pack telemetry to scope the defect to affected units + `progressive_rollout`-style staged firmware/hardware fixes + a bounded recall reserve.
- **Leans on:** Pack telemetry isolates the affected population rather than forcing a blanket recall.

#### S-83 — 4680 in-house cell ramp stalls
- **Attractor:** Yield problems leave Cybertruck and next-gen cost targets unmet, forcing fallback to external cells and undercutting the cost-leadership thesis.
- **Residue:** Multi-source cell fallback (`bulkhead`, same as S-46) so 4680 is upside, not a dependency; packs designed to accept external cells.
- **Leans on:** External cells can cover a 4680 shortfall without a pack redesign.

#### S-84 — Vision-only ODD limitation proven, forcing operational restriction
- **Attractor:** A statistically real failure mode (glare, fog) forces operational-domain restrictions on FSD, narrowing where autonomy works and denting the capability story.
- **Residue:** `shadow_traffic` + condition-tagged telemetry to detect ODD limits early + `feature_flag_kill_switch` to restrict autonomy by condition rather than disable wholesale.
- **Leans on:** The stack can detect degraded conditions and self-restrict safely.

#### S-85 — Cybertruck-specific recall tarnishes the halo model
- **Attractor:** A high-profile flagship-model defect damages the halo launch and the build-quality reputation together.
- **Residue:** `event_sourcing_audit_trail` on part provenance to scope the recall + a bounded warranty reserve (C-15) + a staged OTA/hardware fix.
- **Leans on:** Telemetry and provenance scope the defect to affected units.

#### S-86 — Self-inflicted mass layoff guts a critical team
- **Attractor:** Gutting a load-bearing team (e.g., the Supercharger org) stalls a strategic buildout and walks institutional knowledge out the door.
- **Residue:** `runbook_as_code` capture of critical-team knowledge before reorgs + a decision gate requiring a continuity plan before reorganizing a load-bearing team.
- **Leans on:** Critical knowledge is documented, not tacit, before the cut lands.

#### S-87 — Insider leak of cabin footage and customer PII
- **Attractor:** Employees share interior-camera footage and customer PII; a privacy scandal draws regulatory fines and collapses trust in the connected-car promise.
- **Residue:** `tenant_isolated_blast_radius` + least-privilege access + `audit_log_immutability` on footage/PII access so access is minimized, logged, and prosecutable; data-minimization at source.
- **Leans on:** Sensitive footage and PII access is compartmentalized and logged, not broadly available.

#### S-88 — CEO government office creates conflict-of-interest backlash
- **Attractor:** The CEO's formal political role creates a conflict-of-interest backlash — lost government and fleet contracts, targeted regulatory scrutiny, and procurement bans.
- **Residue:** Brand/governance decoupling (C-14) + a conflicts firewall so Tesla's regulatory and procurement standing doesn't ride on the founder's political fortunes.
- **Leans on:** Tesla can demonstrate governance independence from the founder's political activity. *(Partly aspirational — same reverse-orphan risk as C-14.)*

#### S-89 — Pledged-share margin-call doom loop
- **Attractor:** A sharp TSLA decline triggers margin calls on shares Musk pledged as collateral; forced selling accelerates the fall in a reflexive loop that also threatens founder control and the narrative at once.
- **Residue:** Board-level pledged-share limits + a disclosed collateral-coverage buffer and a pre-agreed liquidity plan so a drawdown can't cascade into forced selling.
- **Leans on:** The board actually caps and monitors pledged-share leverage before the drawdown.

#### S-90 — Eco-activist arson/sabotage halts production
- **Attractor:** Physical sabotage of plant infrastructure (power, water) halts production and raises the standing security cost of every gigafactory.
- **Residue:** `runbook_as_code` IR for physical infrastructure + redundant/islanded utilities (backup power/water) so a single sabotage point doesn't stop the line; site-hardening.
- **Leans on:** Plants can run on backup utilities through an infrastructure attack for a bounded window.

#### S-91 — Typhoon/flood shuts Shanghai plant and export port
- **Attractor:** The highest-volume plant and export hub is offline for weeks; global volume and quarter deliveries slip hardest because so much rides on Shanghai.
- **Residue:** Multi-plant origin-switch (C-01) to reroute export demand to Berlin + flood-hardening and inventory buffer at Shanghai.
- **Leans on:** Berlin and other plants can absorb Shanghai's export volume for the outage window.

#### S-92 — Berlin environmental permit revoked, capping EU capacity
- **Attractor:** An activist legal challenge revokes or blocks the environmental permit over groundwater, capping European capacity and freezing expansion.
- **Residue:** Origin-switch (C-01) to serve EU from elsewhere short-term + water-recycling/permit-headroom (S-41) and genuine community engagement to defend the license.
- **Leans on:** EU demand can be partly served from other plants while the permit is contested.

#### S-93 — Single-source supplier insolvency idles a line
- **Attractor:** A single-source supplier goes bankrupt and a production line idles until the part is re-sourced.
- **Residue:** `dependency_freeze_window`/design-for-substitution (C-08) + supplier-financial-health monitoring and pre-qualified second sources for single-source parts.
- **Leans on:** Alternate sources are pre-qualified before the insolvency, not scrambled after.

#### S-94 — Product-liability insurance market hardens against AV makers
- **Attractor:** Corporate product-liability/property cover for an AV maker becomes unaffordable or unavailable, and Tesla self-insures a tail it can't fully price.
- **Residue:** Captive-insurance capital sized to the retained tail + `event_sourcing_audit_trail` (the safety case) to argue insurability + a reinsurance `bulkhead`.
- **Leans on:** Tesla can capitalize a captive and the safety data supports acceptable reinsurance terms.

#### S-95 — Service-network saturation as the fleet grows
- **Attractor:** Service and mobile-service capacity can't keep up with fleet growth; wait times balloon and owner satisfaction, loyalty, and resale suffer.
- **Residue:** `per_tenant_quota`/`backpressure`-style capacity-led service planning (gate regional fleet growth on service capacity) + remote-diagnosis/OTA-fix to deflect physical visits.
- **Leans on:** Service capacity is planned against fleet density, not left to lag it.

#### S-96 — Gigafactory overcapacity craters margin via fixed-cost deleverage
- **Attractor:** Built-ahead capacity runs well below utilization in a demand air-pocket and fixed-cost deleverage craters gross margin.
- **Residue:** Flexible-capacity staging (mothball/flex-shift options) + the margin-floor circuit breaker (S-14) monitoring cost-per-unit as utilization drops.
- **Leans on:** Plants can flex output down without stranded fixed cost breaking the P&L.

#### S-97 — Non-battery build-quality warranty under-reserve
- **Attractor:** A wave of out-of-warranty structural/build-quality claims (suspension, body) exceeds reserves and reopens the quality reputation.
- **Residue:** Warranty-reserve modeling from full fleet telemetry (extend C-15 beyond the battery) + a bounded goodwill-repair policy.
- **Leans on:** Non-battery failure telemetry gives an accurate forward liability.

#### S-98 — Charging/vehicle obsolescence retrofit drag
- **Attractor:** Older Superchargers and connectors need costly retrofit as voltage and standards evolve — a capital drag and an owner-goodwill problem.
- **Residue:** Upgrade-designed hardware + a published retrofit/compatibility roadmap (a `dependency_freeze_window`-style commitment) so obsolescence is planned, not sprung.
- **Leans on:** Hardware was designed for field-upgrade rather than replacement.

#### S-99 — Subscription "nickel-and-diming" backlash
- **Attractor:** A backlash narrative around feature subscriptions damages loyalty and NPS and softens repeat demand.
- **Residue:** Transparent value-tiering + keep core function un-paywalled + monitor subscription sentiment as a KPI with a `feature_flag_kill_switch` on unpopular paywalls.
- **Leans on:** Subscriptions are separable from core function and reversible.

#### S-100 — Deferred-FSD revenue restatement
- **Attractor:** The auditor or SEC forces a restatement of deferred FSD revenue as undelivered performance obligations balloon — an earnings-and-credibility hit distinct from the S-56 tort exposure.
- **Residue:** `event_sourcing_audit_trail` tying recognized FSD revenue to delivered-capability milestones + a conservative recognition policy so the liability is transparent, not sprung.
- **Leans on:** Revenue recognition is milestone-tied and defensible to auditors.

#### S-101 — Optimus over-promise exposé / safety incident
- **Attractor:** An Optimus demo exposed as teleoperated, or a robot injuring a worker, causes investor whiplash on the AI-narrative premium plus safety-regulatory scrutiny.
- **Residue:** Honest capability disclosure (don't let Optimus be load-bearing in the valuation before it ships — same discipline as C-04) + hard safety interlocks and `feature_flag_kill_switch` on deployed units + `event_sourcing_audit_trail` for incident forensics.
- **Leans on:** The valuation can survive an Optimus disappointment and deployed units have real safety interlocks.

#### S-102 — Concentrated treasury / digital-asset earnings swing
- **Attractor:** A concentrated treasury or digital-asset holding swings reported earnings on mark-to-market and invites scrutiny, adding noise to the equity story.
- **Residue:** Treasury-concentration limits + segregated reporting so operating results stay legible ex-treasury (the same "don't let a line be load-bearing" discipline as C-04).
- **Leans on:** Treasury risk is capped and reported separately from operations.

#### S-103 — Captive-finance credit losses on the lease/loan book
- **Attractor:** Residual-value writedowns and lease/loan defaults hit Tesla's own captive-finance book, turning a demand tool into a balance-sheet loss when used values fall (the S-16 crash seen from the financing arm).
- **Residue:** Residual-value reserves + the CPO/buyback backstop (S-16) sized to protect the lease book + an underwriting-quality KPI.
- **Leans on:** The finance arm reserves for residual and default risk against realistic used-value scenarios.

### Notes on the completeness pass

- **Mapping to the existing control portfolio (§4):** most new residues fold into controls that already exist — the material-passport variants (S-67, S-79) into **C-03**; the retrofit/reserve variants (S-68, S-85, S-97) into **C-15**; the origin-switch variants (S-91, S-92) into **C-01**; the "don't let a line be load-bearing" variants (S-77, S-80, S-100, S-102) into **C-04**; the per-region kill-switch/conformity variants (S-69, S-73, S-84) into **C-02**; the decoupling variants (S-88) into **C-14**. Genuinely *new* controls this pass surfaces: a **pledged-share leverage cap** (S-89), an **insurance reinsurance/reserve-monitor** (S-81, S-94), a **capacity-led service/plant flex discipline** (S-95, S-96), and a **treasury-concentration limit** (S-102). These are the additions worth wiring into §4 on the next full re-run.
- **Contagion note:** S-81 is a self-reference worth flagging — Tesla Insurance is the *residue* for S-16/S-19 and the *stressor* in S-81, so a single actuarial-assumption error both fails the backstop and creates a new hole. S-89 (pledged shares) and S-80 (cost of capital) couple the founder-dependency cascade to the financial-reflexivity cascade the original §5 did not connect: a founder shock and a stock shock now share a transmission path.

*This completes the second pass. See the closing judgement at the head of the delivering message.*
```
