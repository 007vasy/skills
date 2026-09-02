# Residuality Theory ERM Analysis — SpaceX

**Method:** Barry O'Reilly's Residuality Theory, adapted for enterprise risk (see `residuality-enterprise-risk-management.md`).
**Subject:** Space Exploration Technologies Corp. (SpaceX)
**Date:** 2026-07-05
**Analyst note:** Stressors and attractors are in business language. Mechanism detail lives inside the residue. Company facts are grounded in SpaceX's publicly known operating model; no claims are made about SpaceX's private internal systems, only about the *kind* of control that would have to exist.

---

## Step 1 — Naive operating model

### What SpaceX is, stripped of mitigation theatre

SpaceX captures value from three interlocking businesses that share engineering, manufacturing, launch, and one founder:

**Value chain**

1. **Launch services (cash engine + strategic moat).** Design and build rockets (Falcon 9, Falcon Heavy, Starship/Super Heavy) and engines (Merlin, Raptor). Sell rides to orbit to commercial satellite operators, NASA, the US Department of Defense, the National Reconnaissance Office (NRO), and other governments. Reusability (booster + fairing recovery, and eventually full Starship reuse) is the cost weapon that underprices every rival.
2. **Starlink (growth engine + recurring revenue).** Manufacture and launch thousands of low-Earth-orbit (LEO) satellites; operate ground stations, a core network, and RF spectrum; sell internet subscriptions to consumers, enterprises, maritime/aviation, and — via Starshield — defense customers. Direct-to-cell partnerships with mobile carriers extend the addressable market. Starlink launches ride SpaceX's own rockets, so the two businesses subsidize each other.
3. **Human spaceflight (credibility + margin).** Crew Dragon carries NASA astronauts to the ISS and flies private missions. This is the reputational keystone: it is what makes SpaceX "the company that flies people," underwriting trust with every other customer.

**Core functions that keep the flow alive**

- Vehicle & engine design (propulsion is the crown jewel — Raptor, Merlin).
- High-rate vertical manufacturing (engines, airframes, satellites, user terminals) — deeply vertically integrated, little outsourcing.
- Launch operations across Starbase (Boca Chica, TX), Cape Canaveral / Kennedy (FL), and Vandenberg (CA); droneship + landing recovery.
- Constellation operations: satellite command & control, collision avoidance, network operations, spectrum management.
- Regulatory & licensing: FAA launch licenses, FCC spectrum & orbital authorizations, ITAR/export control, environmental permitting.
- Commercial: government contract capture, Starlink subscriber acquisition/billing/support.
- Capital allocation: funding the Mars program and Starship development from Starlink cash flow + private raises.

**Critical dependencies**

- *Internal:* Elon Musk (strategy, capital-raising credibility, key-person). A small number of launch/test sites. Raptor/Merlin production lines. The satellite factory. Shared engineering talent pool. Proprietary flight software.
- *External:* FAA (launch licensing), FCC (spectrum/orbital slots), NASA & DoD/NRO (anchor customers and revenue), specialty suppliers (avionics chips, specialty alloys, batteries), propellant supply (LOX, methane/RP-1), private capital markets, insurers, cloud/comms backhaul vendors, carrier partners for direct-to-cell, and the physical RF/orbital commons.

**Load-bearing assumptions (stated out loud)**

- A1. SpaceX keeps a *large launch-cadence lead* — nobody else can launch at comparable rate or price this decade.
- A2. Reusability keeps working at high reliability; boosters and Starship recover without fleet-grounding mishaps.
- A3. The FAA and FCC grant licenses and modifications roughly on SpaceX's schedule; regulation moves in months, not weeks.
- A4. Government (NASA/DoD/NRO) remains an anchor buyer and does not force a hard second-source cap that shrinks SpaceX's share.
- A5. Starlink subscriber growth and ARPU keep funding Starship/Mars capex; the constellation stays ahead of competitors on coverage.
- A6. Elon Musk remains available, credible to capital markets, and not a liability to government/enterprise customers.
- A7. The LEO orbital environment stays usable — no debris cascade, no ASAT normalization, no atmospheric-harm finding.
- A8. Spectrum SpaceX uses stays allocated to it; orbital shells stay authorized.
- A9. Vertical integration is a strength; the handful of single points (one Starship pad, sole-source parts, one satellite factory) stay up.
- A10. The company can raise private capital on favorable terms whenever the Mars burn requires it.

---

## Step 2 — Exhaustive stressor set

67 stressors across all 9 categories, multiple passes each. Novelty 1 (already on a register) → 5 (would not appear in any standard risk register). Black swans (novelty 5) are marked ★.

| # | Stressor | Category | Novelty |
|---|---|---|---|
| S-01 | FAA grounds Starship indefinitely after a mishap investigation, freezing Starbase flight test. | Regulatory/legal | 2 |
| S-02 | FCC tightens orbital-debris / de-orbit rules, forcing SpaceX to thin a shell or re-file the constellation. | Regulatory/legal | 3 |
| S-03 | An ITAR/export-control finding blocks foreign Starlink sales and freezes hiring of non-US engineers. | Regulatory/legal | 3 |
| S-04 | An environmental ruling halts Starbase expansion over wetlands/wildlife impact. | Regulatory/legal | 2 |
| S-05 | A large foreign government bans Starlink terminals nationwide overnight. | Regulatory/legal | 3 |
| S-06 | Government procurement policy mandates a hard second-source, capping SpaceX's launch market share. | Regulatory/legal | 3 |
| S-07 | Antitrust action targets SpaceX's launch-plus-satellite vertical integration. | Regulatory/legal | 4 |
| S-08 | New international space-traffic-management law imposes strict liability for any on-orbit collision. | Regulatory/legal | 4 |
| S-09 | Amazon's Kuiper reaches coverage parity and undercuts Starlink consumer pricing. | Market/competitive | 2 |
| S-10 | A reusable rival (New Glenn, Neutron) reaches price parity on medium-lift launch. | Market/competitive | 2 |
| S-11 | Carrier partners build or defect to a rival direct-to-cell provider. | Market/competitive | 3 |
| S-12 | China's cheap launch plus the Guowang/Qianfan constellations capture the emerging-market broadband tier. | Market/competitive | 3 |
| S-13 | Aggressive terrestrial fiber + 5G build-out erodes Starlink's rural addressable market. | Market/competitive | 2 |
| S-14 | A large commercial customer cancels a multi-launch manifest and moves to a rival. | Market/competitive | 2 |
| S-15 | Launch commoditizes and per-kg prices collapse, crushing launch-services margin. | Market/competitive | 3 |
| S-16 | A common-mode Raptor defect is discovered across the engine fleet. | Technical/infra | 3 |
| S-17 | A Starlink core-network / ground-segment outage causes a multi-hour global service blackout. | Technical/infra | 3 |
| S-18 | A Falcon 9 in-flight anomaly grounds the fleet during a crewed ISS rotation window. | Technical/infra | 2 |
| S-19 | A bad software update bricks a large fraction of user terminals. | Technical/infra | 3 |
| S-20 | A collision in a populated Starlink shell seeds a local debris cascade. | Technical/infra | 4 |
| S-21 | Loss or spoofing of GPS/timing signals degrades constellation station-keeping and hand-offs. | Technical/infra | 4 |
| S-22 | Elon Musk is suddenly incapacitated or exits the company. | Human/org | 3 |
| S-23 | A rival poaches a cluster of senior propulsion engineers in one quarter. | Human/org | 3 |
| S-24 | A labor-organizing drive or walkout halts Starbase production. | Human/org | 3 |
| S-25 | An immigration/visa crackdown strips a swath of foreign engineering staff. | Human/org | 4 |
| S-26 | Musk's political conduct triggers customer/government boycotts and contract reviews. | Human/org | 3 |
| S-27 | A nation-state cyber intrusion reaches the satellite command-and-control uplink. | Adversarial/abuse | 4 |
| S-28 | Starlink terminals are jammed or spoofed at scale in a contested region. | Adversarial/abuse | 3 |
| S-29 | An insider exfiltrates Raptor/Starship design IP to a foreign state. | Adversarial/abuse | 3 |
| S-30 | Terminals are diverted and activated inside sanctioned territory, triggering enforcement. | Adversarial/abuse | 3 |
| S-31 | A drone or physical attack damages a launch pad or the satellite factory. | Adversarial/abuse | 4 |
| S-32 | An adversary ASAT test creates a debris field crossing SpaceX orbital shells. | Adversarial/abuse | 4 |
| S-33 | Ransomware locks the manufacturing execution systems and halts the production line. | Adversarial/abuse | 3 |
| S-34 | A hurricane destroys pad, integration, and recovery infrastructure at a coastal site. | Physical/env | 2 |
| S-35 | A severe geomagnetic storm degrades or prematurely de-orbits a large batch of satellites. | Physical/env | 3 |
| S-36 | Wildfire or drought closes Vandenberg or the McGregor engine-test site. | Physical/env | 3 |
| S-37 | A pad explosion destroys the only operational Starship launch mount. | Physical/env | 3 |
| S-38 | Long-run coastal erosion / sea-level rise makes Boca Chica untenable as a primary site. | Physical/env | 4 |
| S-39 | A sole-source avionics-chip supplier fails or is acquired by a hostile party. | Supply-chain/vendor | 3 |
| S-40 | China restricts export of a rare-earth or specialty alloy critical to engine production. | Supply-chain/vendor | 3 |
| S-41 | A cloud/backhaul vendor terminates service or is breached, cutting Starlink's ground plane. | Supply-chain/vendor | 3 |
| S-42 | The launch-insurance market withdraws capacity after a run of industry losses. | Supply-chain/vendor | 3 |
| S-43 | A payment processor drops Starlink consumer billing in a major region. | Supply-chain/vendor | 3 |
| S-44 | A regional LOX or methane supply disruption starves the launch cadence. | Supply-chain/vendor | 2 |
| S-45 | Subscriber growth outruns capacity and congestion collapses quality of service in dense cells. | Scale/load | 2 |
| S-46 | A single mega-customer (airline fleet, government) demands an SLA the network cannot guarantee. | Scale/load | 3 |
| S-47 | Launch-cadence ramp outstrips FAA/range scheduling capacity and creates a manifest backlog. | Scale/load | 3 |
| S-48 | Consumer support volume explodes with the subscriber base and churn spikes on poor service. | Scale/load | 2 |
| S-49 | The Starship v2/v3 production ramp outpaces QA and the defect rate climbs. | Scale/load | 3 |
| S-50 | Heavily reused boosters exceed practical fatigue life and reliability quietly degrades. | Time/lifecycle | 3 |
| S-51 | First-generation Starlink satellites hit end-of-life together, forcing a costly mass-replacement wave. | Time/lifecycle | 3 |
| S-52 | A spectrum authorization or launch license quietly lapses at renewal and nobody owned the calendar. | Time/lifecycle | 4 |
| S-53 | A long-running "temporary" regulatory waiver expires and is not renewed. | Time/lifecycle | 4 |
| S-54 | Mars/Starship capex burns cash faster than Starlink funds it and the runway shortens in a tight capital market. | Time/lifecycle | 3 |
| S-55 | Legacy Falcon avionics accrue unmaintained technical debt as attention shifts to Starship. | Time/lifecycle | 3 |
| S-56 ★ | A viral news segment alleges — true or not — a covered-up Crew Dragon safety flaw. | Black swan (Market/reputation) | 5 |
| S-57 ★ | A geopolitical crisis forces SpaceX to cut Starlink service to an active war zone overnight. | Black swan (Regulatory/geopolitical) | 5 |
| S-58 ★ | A rival buys controlling stakes in two of SpaceX's sole-source suppliers and weaponizes them. | Black swan (Supply-chain) | 5 |
| S-59 ★ | An on-orbit collision kills a crewed vehicle or the ISS, triggering a global launch moratorium. | Black swan (Technical/reputation) | 5 |
| S-60 ★ | Musk unilaterally makes a battlefield service decision with Starlink, creating a state-level liability crisis. | Black swan (Human/geopolitical) | 5 |
| S-61 ★ | Peer-reviewed science links LEO mega-constellation de-orbit burn to atmospheric/ozone harm, spurring global backlash. | Black swan (Physical/env) | 5 |
| S-62 ★ | A convincing deepfake of Musk moves markets or attempts to trigger a fraudulent internal command. | Black swan (Adversarial) | 5 |
| S-63 ★ | A national-security emergency prompts a move to nationalize or commandeer launch capability. | Black swan (Regulatory) | 5 |
| S-64 | A governance/financing crisis at Musk's other ventures (X, Tesla) contaminates SpaceX's capital access. | Human/org | 4 |
| S-65 | A private astronaut dies on a commercial mission. | Technical/reputation | 3 |
| S-66 | A booster fails catastrophically on a return-to-launch-site landing near a populated area. | Physical/env | 4 |
| S-67 | ISS retirement arrives before commercial LEO demand matures, removing a revenue pillar with no replacement. | Time/lifecycle | 3 |

**Coverage check:** Regulatory/legal 10 (S-01–08, S-57, S-63), Market/competitive 8 (S-09–15, S-56), Technical/infra 8 (S-16–21, S-59, S-65), Human/org 7 (S-22–26, S-60, S-64), Adversarial/abuse 7 (S-27–33, S-62), Physical/env 7 (S-34–38, S-61, S-66), Supply-chain/vendor 6 (S-39–44, S-58), Scale/load 5 (S-45–49), Time/lifecycle 8 (S-50–55, S-67). Black swans (novelty 5): S-56, S-57, S-58, S-59, S-60, S-61, S-62, S-63 = **8**.

---

## Step 3 — Attractor + residue per stressor

Residue names in `code font` are reused from `residue_library.md` where they translate; bespoke enterprise controls are named in plain text and defined once, then reused.

### S-01: FAA grounds Starship indefinitely after a mishap.
- **Category:** Regulatory/legal — **Novelty:** 2
- **Attractor:** Starship development stalls, the Starlink v2 mass-to-orbit plan slips, and the Mars narrative that underwrites capital-raising loses momentum; Falcon still flies, so cash is intact but the growth story cools.
- **Residue:** **Mishap-investigation readiness** — a pre-built anomaly investigation capability that returns a root-cause + corrective-action package fast enough to shorten the grounding (a `runbook_as_code` for mishap closeout: instrumented flight data, pre-agreed FAA process, standing investigation team).
- **Leans on:** A3 (regulator engages on a workable timeline) and rich flight telemetry that makes root cause findable.

### S-02: FCC tightens orbital-debris / de-orbit rules.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** SpaceX must thin or re-file shells, slowing capacity growth and handing rivals a coverage window; licence-to-operate for the constellation becomes conditional.
- **Residue:** **Regulatory margin design** — operate satellites with de-orbit/collision-avoidance margin already above the current rule so a tightening is absorbed by config, not redesign (`per_minute_billing_path`-style "record both dimensions, switch by policy," applied to compliance parameters).
- **Leans on:** A7/A8 and design headroom already carried in the fleet.

### S-03: ITAR/export-control finding blocks foreign sales and hiring.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** Foreign Starlink revenue freezes and the engineering hiring pipeline narrows; growth outside the US stalls and legal exposure mounts.
- **Residue:** **Export-control compliance spine** — a standing trade-compliance function with `audit_log_immutability` over technical-data access and citizenship-gated engineering controls, so violations are prevented and provable.
- **Leans on:** Accurate person-and-data classification; the compliance team reaches every project.

### S-04: Environmental ruling halts Starbase expansion.
- **Category:** Regulatory/legal — **Novelty:** 2
- **Attractor:** Starbase build-out stops, concentrating all Starship risk on the current footprint and delaying cadence; local licence-to-operate erodes.
- **Residue:** **Site redundancy (geographic)** — a qualified second Starship launch/production location (Cape) so a single-site ruling does not halt the program.
- **Leans on:** A9 relaxed — more than one viable site actually stood up, not just planned.

### S-05: Foreign government bans Starlink nationwide.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** Regional subscriber revenue disappears and the ban may become a template other states copy; addressable market shrinks.
- **Residue:** **Geofencing + terminal kill/enable by region** — `feature_flag_kill_switch` at the terminal-authorization layer so service can be lawfully withdrawn or restored per jurisdiction without hardware recall.
- **Leans on:** Terminal-level authorization control that SpaceX operates centrally.

### S-06: Procurement mandates a hard second-source, capping share.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** Government launch revenue growth is capped and a subsidized competitor is kept alive; the anchor-customer moat thins.
- **Residue:** **Revenue diversification (portfolio)** — Starlink + commercial launch depth so government share is one leg of a tripod, not the load-bearing column (bespoke: **diversified_revenue_mix**).
- **Leans on:** A4 relaxed; Starlink cash actually independent of government launch.

### S-07: Antitrust action against vertical integration.
- **Category:** Regulatory/legal — **Novelty:** 4
- **Attractor:** Forced separation of launch and Starlink threatens the internal-subsidy model that makes both cheap; enterprise value at risk.
- **Residue:** **Structural + transfer-pricing separability** — keep launch and Starlink as arm's-length internal cost centers with clean transfer pricing and separable books, so a remedy is a governance change not a re-founding.
- **Leans on:** Clean internal accounting between the two businesses.

### S-08: Strict-liability space-traffic law.
- **Category:** Regulatory/legal — **Novelty:** 4
- **Attractor:** Every conjunction becomes an uninsurable liability; the constellation's economics invert if one collision means unbounded damages.
- **Residue:** **Collision-avoidance evidence trail** — `event_sourcing_audit_trail` of every automated maneuver and conjunction decision, so SpaceX can prove diligence and cap liability exposure.
- **Leans on:** Autonomous collision-avoidance actually logging defensible decisions.

### S-09: Kuiper reaches parity and undercuts pricing.
- **Category:** Market/competitive — **Novelty:** 2
- **Attractor:** Consumer ARPU compresses and net-adds slow in overlapping markets; the growth engine loses torque.
- **Residue:** **Cost lead via reuse + own-launch** — protect the structural cost advantage (self-launched sats, high reuse) so SpaceX can win a price war it starts (bespoke: **cost_leadership_moat**).
- **Leans on:** A1/A2 — the launch-cost gap persists.

### S-10: Reusable rival reaches launch price parity.
- **Category:** Market/competitive — **Novelty:** 2
- **Attractor:** Commercial launch loses pricing power; the cash engine's margin thins.
- **Residue:** **Cadence + reliability lead** — keep the schedule-certainty and flight-heritage advantage that customers pay a premium for even at price parity (same **cost_leadership_moat** control, cadence facet).
- **Leans on:** A1 — cadence lead is real and defended.

### S-11: Carrier partners defect from direct-to-cell.
- **Category:** Market/competitive — **Novelty:** 3
- **Attractor:** The direct-to-cell growth vector stalls and a rival gains distribution to hundreds of millions of handsets.
- **Residue:** **Multi-carrier partnership breadth** — never let one carrier be the sole distribution path in a region; `bulkhead` across partners so one defection is contained.
- **Leans on:** More than one carrier relationship per key market.

### S-12: China's launch + Guowang capture emerging markets.
- **Category:** Market/competitive — **Novelty:** 3
- **Attractor:** The largest future subscriber pool is foreclosed on geopolitical lines; TAM shrinks structurally.
- **Residue:** **Aligned-market focus + defense anchor** — concentrate on markets where Starshield/Western-aligned demand is durable; treat closed markets as out-of-scope, not lost (bespoke: **diversified_revenue_mix**, defense facet).
- **Leans on:** Western-aligned government/enterprise demand remains large.

### S-13: Terrestrial fiber/5G erodes rural TAM.
- **Category:** Market/competitive — **Novelty:** 2
- **Attractor:** The core rural-broadband thesis softens; consumer growth plateaus earlier than modeled.
- **Residue:** **Mobility segment pivot** — lean into maritime, aviation, RVs, and enterprise/backhaul where fiber cannot reach (same **diversified_revenue_mix**, mobility facet).
- **Leans on:** Product/pricing flexibility across segments already exists.

### S-14: Large commercial customer cancels a manifest.
- **Category:** Market/competitive — **Novelty:** 2
- **Attractor:** A revenue hole and idle cadence slots; if the customer is big enough, a quarter's launch plan wobbles.
- **Residue:** **Backfill manifest depth** — a deep, diversified booking book plus Starlink as a captive internal payload to refill vacated slots (`bulkhead` across customers; Starlink absorbs idle cadence).
- **Leans on:** Starlink demand can flex to fill launch slots on short notice.

### S-15: Launch commoditizes, per-kg prices collapse.
- **Category:** Market/competitive — **Novelty:** 3
- **Attractor:** Launch becomes a low-margin utility; the business must earn its return downstream, not on the ride.
- **Residue:** **Move margin downstream to Starlink/services** — the internal-launch subsidy means SpaceX profits from what it puts in orbit, not only from launching others (bespoke: **cost_leadership_moat** + **diversified_revenue_mix**).
- **Leans on:** A5 — Starlink economics carry the group.

### S-16: Common-mode Raptor defect across the fleet.
- **Category:** Technical/infra — **Novelty:** 3
- **Attractor:** Starship (and the propulsion roadmap) grounds until the defect is understood; the whole next-gen program pauses.
- **Residue:** **Engine fleet health + serialized traceability** — `event_sourcing_audit_trail` per engine serial so a defect can be scoped to affected units and cleared selectively rather than grounding everything.
- **Leans on:** Per-unit build and test data actually retained and queryable.

### S-17: Starlink global service blackout.
- **Category:** Technical/infra — **Novelty:** 3
- **Attractor:** Millions of subscribers (including defense and aviation) lose service simultaneously; SLA credits, churn, and a credibility hit for mission-critical use.
- **Residue:** **Graceful degrade + rapid restore** — `read_only_degraded_mode` for the network (keep basic connectivity/priority traffic up while control-plane recovers) plus a `runbook_as_code` restore path.
- **Leans on:** Ground-segment architecture supports partial operation without full control plane.

### S-18: Falcon 9 grounding during a crewed rotation.
- **Category:** Technical/infra — **Novelty:** 2
- **Attractor:** A crew is stranded or a rotation slips; the reputational core (safe human spaceflight) is directly threatened.
- **Residue:** **Crew abort + margin design** — the launch-escape/abort capability and design margin that make a crewed anomaly survivable rather than fatal (bespoke: **crew_safety_margin**).
- **Leans on:** Abort system independence from the failing subsystem.

### S-19: Bad software update bricks user terminals.
- **Category:** Technical/infra — **Novelty:** 3
- **Attractor:** A large installed base goes dark at once; support and reputation crisis, especially for critical users.
- **Residue:** **Staged rollout + remote rollback** — `progressive_rollout` (1%→10%→100%) with automatic abort and a signed-rollback path so a bad build never reaches the whole fleet.
- **Leans on:** Terminals accept staged, reversible updates; canary metrics watched.

### S-20: Collision seeds a debris cascade in a populated shell.
- **Category:** Technical/infra — **Novelty:** 4
- **Attractor:** A shell becomes hazardous, forcing evasive maneuvers or shell abandonment; capacity and licence-to-operate both hit.
- **Residue:** **Autonomous collision avoidance + de-orbit reserve** — maintain maneuver margin and rapid replenishment so a fouled shell can be evacuated and rebuilt (`local_autonomy` on-sat avoidance + bespoke **constellation_replenishment_cadence**).
- **Leans on:** A7; propellant/maneuver margin and launch cadence to replace losses.

### S-21: GPS/timing loss or spoofing degrades the constellation.
- **Category:** Technical/infra — **Novelty:** 4
- **Attractor:** Station-keeping and beam hand-off degrade fleet-wide; service quality falls and safety-of-flight margins shrink.
- **Residue:** **Independent timing/positioning fallback** — onboard timing and inter-satellite ranging that survive GPS denial (`local_autonomy` — edge holds enough state to operate without the central signal).
- **Leans on:** Satellites carry independent timing; inter-sat links provide geometry.

### S-22: Elon Musk incapacitated or exits.
- **Category:** Human/org — **Novelty:** 3
- **Attractor:** Strategic direction, capital-raising credibility, and the Mars narrative wobble; valuation and morale take an immediate hit even though operations continue.
- **Residue:** **Key-person succession + institutionalized decision rights** — a named operating successor (the President/COO deep bench) and documented decision authority so the company runs without the founder in the room (bespoke: **key_person_succession**).
- **Leans on:** A6 relaxed — succession is real and rehearsed, not nominal.

### S-23: Rival poaches senior propulsion engineers.
- **Category:** Human/org — **Novelty:** 3
- **Attractor:** Propulsion — the crown jewel — loses tacit knowledge; Raptor iteration slows and a competitor accelerates.
- **Residue:** **Knowledge capture + bench depth** — `runbook_as_code` for critical propulsion processes plus deliberate redundancy so no engine subsystem has a single irreplaceable owner.
- **Leans on:** Tacit knowledge is actually being externalized, not just in senior heads.

### S-24: Labor action halts Starbase production.
- **Category:** Human/org — **Novelty:** 3
- **Attractor:** Manufacturing/launch cadence stops at the primary site; every downstream milestone slips.
- **Residue:** **Site redundancy (geographic)** — production spread across sites so one site's stoppage does not halt the group (same control as S-04).
- **Leans on:** A9 — real productive capacity at more than one site.

### S-25: Immigration crackdown strips foreign engineering staff.
- **Category:** Human/org — **Novelty:** 4
- **Attractor:** A sudden capability gap in specialized engineering; delivery slips and rehiring is slow.
- **Residue:** **Workforce concentration limits + succession** — deliberately cap single-visa-class concentration on critical teams and cross-train (same **key_person_succession**, team facet).
- **Leans on:** Workforce planning tracks concentration risk.

### S-26: Musk's political conduct triggers boycotts/contract reviews.
- **Category:** Human/org — **Novelty:** 3
- **Attractor:** Government and enterprise customers open reviews or pause; contracts and brand suffer even if the founder is "right."
- **Residue:** **Founder–company brand firewall** — SpaceX's mission credibility and delivery record positioned as institutional, separable from the founder's personal conduct (bespoke: **brand_firewall**).
- **Leans on:** Customers can distinguish the company's reliability from the founder's persona.

### S-27: Nation-state cyber intrusion reaches satellite command uplink.
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Attractor:** Loss of control of national-security-relevant assets; catastrophic to licence-to-operate and to every defense relationship.
- **Residue:** **Command-uplink hardening + dual-control** — `key_rotation_dual_accept` on command credentials, two-person authorization for fleet-level commands, and `audit_log_immutability` over the command path.
- **Leans on:** Command authority is cryptographically gated and logged; no single credential commands the fleet.

### S-28: Terminals jammed/spoofed at scale in a contested region.
- **Category:** Adversarial/abuse — **Novelty:** 3
- **Attractor:** Service fails exactly where it is most needed (defense/critical); the resilience selling point is publicly dented.
- **Residue:** **Anti-jam / frequency-agility mode** — a hardened operating mode (beam nulling, frequency hopping) invoked in contested zones (`feature_flag_kill_switch` selecting a resilient waveform/profile).
- **Leans on:** Terminals/network support a switchable resilient mode.

### S-29: Insider exfiltrates Raptor/Starship IP.
- **Category:** Adversarial/abuse — **Novelty:** 3
- **Attractor:** The core propulsion/vehicle advantage leaks to a state competitor; the moat erodes and export-control liability follows.
- **Residue:** **Least-privilege + immutable access audit** — need-to-know compartmentalization with `audit_log_immutability` so exfiltration is constrained and detectable.
- **Leans on:** Access is compartmented; audit trail is tamper-evident.

### S-30: Terminals activated in sanctioned territory.
- **Category:** Adversarial/abuse — **Novelty:** 3
- **Attractor:** Sanctions enforcement, fines, and a government-trust rupture; licence-to-operate with the US government at stake.
- **Residue:** **Geofencing + terminal kill/enable by region** — same control as S-05, used to deny unauthorized geographies.
- **Leans on:** Central terminal authorization keyed to location.

### S-31: Physical/drone attack on a pad or the satellite factory.
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Attractor:** Loss of a single point of production/launch; cadence and constellation replenishment stall.
- **Residue:** **Site redundancy + physical security perimeter** — geographic redundancy (same as S-04/S-24) plus counter-UAS/physical hardening so one strike is contained.
- **Leans on:** A9 relaxed; second site can absorb load.

### S-32: Adversary ASAT test crosses SpaceX shells.
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Attractor:** A debris field forces mass maneuvers or shell abandonment; orbital-commons risk becomes a live cost.
- **Residue:** **Autonomous avoidance + replenishment cadence** — same control as S-20 (maneuver margin + rebuild capacity).
- **Leans on:** A7; maneuver and launch margin.

### S-33: Ransomware halts the production line.
- **Category:** Adversarial/abuse — **Novelty:** 3
- **Attractor:** Manufacturing stops; engine/satellite/terminal output drops and cadence starves downstream.
- **Residue:** **Segmented OT + offline restore** — network-segmented manufacturing systems with tested offline backups (`runbook_as_code` restore + `bulkhead` between IT and OT).
- **Leans on:** OT is isolated from IT; restore is rehearsed.

### S-34: Hurricane destroys coastal launch/recovery infrastructure.
- **Category:** Physical/env — **Novelty:** 2
- **Attractor:** A site is offline for months; cadence and recovery cripple until rebuilt.
- **Residue:** **Site redundancy (geographic)** — Cape/Vandenberg/Starbase spread so one coastal loss does not stop launch (same control as S-04).
- **Leans on:** A9 — multiple operational sites.

### S-35: Geomagnetic storm de-orbits a satellite batch.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** Sudden capacity loss and replacement cost; a known-but-underweighted hazard bites.
- **Residue:** **Replenishment cadence + orbit-raising discipline** — the ability to rebuild losses fast and hold new sats at safe altitude during storms (same **constellation_replenishment_cadence**).
- **Leans on:** A5 — cheap self-launch makes losses affordable.

### S-36: Wildfire/drought closes Vandenberg or McGregor.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** Polar launches or engine testing stop; a chokepoint in the pipeline seizes.
- **Residue:** **Test/launch site redundancy** — engine test and launch capability at more than one location (same site-redundancy control, test facet).
- **Leans on:** A9 — testing not single-sited.

### S-37: Pad explosion destroys the only Starship mount.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** The entire Starship program pauses on infrastructure loss, not vehicle loss; the most concentrated single point in the model.
- **Residue:** **Second Starship pad** — a second, qualified orbital launch mount (same site-redundancy control; this is the sharpest instance of it).
- **Leans on:** A9 — a real second mount exists and is flight-ready.

### S-38: Coastal erosion makes Boca Chica untenable long-term.
- **Category:** Physical/env — **Novelty:** 4
- **Attractor:** The flagship site becomes a stranded asset over a decade; strategic footprint must migrate.
- **Residue:** **Long-horizon site portfolio planning** — treat any single site as impermanent and keep a pipeline of qualified alternatives (same site-redundancy control, strategic-horizon facet).
- **Leans on:** Capital and permitting lead time for new sites.

### S-39: Sole-source avionics-chip supplier fails or is acquired hostilely.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Production of vehicles or satellites stalls on one missing part; cadence collapses.
- **Residue:** **Second-source qualification + safety stock** — a qualified alternate supplier or in-house substitute plus a buffer inventory (bespoke: **second_source_qualification** + `dependency_freeze_window`-style buffer).
- **Leans on:** A9 relaxed — critical parts are dual-sourced or in-house-capable.

### S-40: China restricts rare-earth / specialty-alloy export.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Engine and structure production constrained; the cadence lead erodes with the input shortage.
- **Residue:** **Strategic material stockpile + alternative alloys** — buffer inventory and qualified alternate materials (same **second_source_qualification**, materials facet).
- **Leans on:** Substitute materials qualified before the ban.

### S-41: Cloud/backhaul vendor terminates or is breached.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Starlink's ground plane degrades; service or billing interrupted; dependence on a third party exposed.
- **Residue:** **Multi-provider ground plane + degrade mode** — more than one backhaul/cloud path plus `read_only_degraded_mode` so a vendor loss is contained (`bulkhead` across providers).
- **Leans on:** Ground architecture not locked to one vendor.

### S-42: Insurance market withdraws launch capacity.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Customers who require insured rides pause; some missions become unbookable.
- **Residue:** **Self-insurance / flight-heritage underwriting** — SpaceX's reliability record and balance sheet let it self-insure or underwrite where the market retreats (bespoke: **capital_reserve_buffer**, insurance facet).
- **Leans on:** A10 — balance sheet depth; demonstrable reliability record.

### S-43: Payment processor drops Starlink billing in a region.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Subscribers in a region cannot pay; involuntary churn and revenue loss.
- **Residue:** **Multi-processor billing fallback** — more than one payment path per region with automatic failover (`outbox_with_async_reconciliation` for billing intents + `bulkhead` across processors).
- **Leans on:** Billing integrated to multiple processors.

### S-44: Regional LOX/methane disruption starves cadence.
- **Category:** Supply-chain/vendor — **Novelty:** 2
- **Attractor:** Launches slip for want of propellant; cadence — the whole moat — stalls.
- **Residue:** **Propellant supplier diversity + on-site storage buffer** — multiple suppliers and storage margin per site (same **second_source_qualification**, propellant facet).
- **Leans on:** Storage capacity and more than one supplier per site.

### S-45: Subscriber growth outruns capacity; QoS collapses in dense cells.
- **Category:** Scale/load — **Novelty:** 2
- **Attractor:** Service quality degrades where demand is highest; churn and reputational damage in the best markets.
- **Residue:** **Per-cell capacity governance** — `per_tenant_quota`/admission control per geographic cell so SpaceX stops selling where a cell is full rather than degrading everyone.
- **Leans on:** Real-time cell-level capacity visibility and sales gating.

### S-46: Mega-customer demands an SLA the network can't guarantee.
- **Category:** Scale/load — **Novelty:** 3
- **Attractor:** Either an unmeetable commitment (liability) or a lost flagship deal; a single account distorts the network.
- **Residue:** **Tiered priority + honest SLA tiers** — `per_tenant_quota` with explicit priority tiers so premium demand is served without over-promising (`bulkhead` isolates one account's demand).
- **Leans on:** Network supports enforceable priority tiers.

### S-47: Cadence ramp outstrips FAA/range scheduling.
- **Category:** Scale/load — **Novelty:** 3
- **Attractor:** A manifest backlog forms; SpaceX's own success outruns the regulatory/range throughput and cadence advantage caps out.
- **Residue:** **Range-slot diversification + regulatory throughput engagement** — spread launches across ranges and work licensing/range capacity ahead of demand (`bulkhead` across ranges + regulatory-liaison facet of **regulatory_liaison**).
- **Leans on:** A3 — regulator/range scales with SpaceX.

### S-48: Support volume explodes; churn spikes on poor service.
- **Category:** Scale/load — **Novelty:** 2
- **Attractor:** A consumer-scale support burden the org wasn't built for; churn and brand damage.
- **Residue:** **Self-service + automated support scaling** — tiered self-service deflection so support cost scales sublinearly with subscribers (`backpressure` on human support demand).
- **Leans on:** Product diagnostics good enough for self-service resolution.

### S-49: Starship v2/v3 ramp outpaces QA; defect rate climbs.
- **Category:** Scale/load — **Novelty:** 3
- **Attractor:** Quality escapes into flight hardware; a mishap becomes more likely exactly as volume rises.
- **Residue:** **Rate-gated QA with serialized traceability** — production-rate limited by QA capacity, with `event_sourcing_audit_trail` per unit so defects are caught and scoped (couples to S-16).
- **Leans on:** QA has authority to throttle the line.

### S-50: Reused boosters exceed practical fatigue life.
- **Category:** Time/lifecycle — **Novelty:** 3
- **Attractor:** Reliability quietly degrades; a reuse-driven failure would undercut the entire reusability thesis.
- **Residue:** **Fleet-leader life-tracking + retirement policy** — per-booster flight/fatigue accounting with a hard retirement rule (`event_sourcing_audit_trail` per airframe + a lifecycle gate).
- **Leans on:** Per-unit usage data drives retirement, not optimism.

### S-51: First-gen Starlink sats hit end-of-life together.
- **Category:** Time/lifecycle — **Novelty:** 3
- **Attractor:** A synchronized replacement wave spikes capex and launch demand; if unfunded, coverage dips.
- **Residue:** **Staggered replenishment cadence** — continuous rolling replacement rather than cliff-edge fleets (same **constellation_replenishment_cadence**, lifecycle facet).
- **Leans on:** A5 — self-launch keeps replacement affordable and continuous.

### S-52: A spectrum authorization or launch license lapses at renewal.
- **Category:** Time/lifecycle — **Novelty:** 4
- **Attractor:** A silent loss of licence-to-operate in a band or for a vehicle; sudden inability to operate a legally owned capability.
- **Residue:** **License & spectrum renewal calendar with ownership** — a tracked registry of every authorization, expiry, and named owner (bespoke: **license_lifecycle_registry**; a `dependency_freeze_window`-style scheduled guard).
- **Leans on:** Someone owns the calendar and acts before expiry.

### S-53: A long-running "temporary" regulatory waiver expires.
- **Category:** Time/lifecycle — **Novelty:** 4
- **Attractor:** An operation everyone assumed was permanent suddenly isn't compliant; forced pause or redesign.
- **Residue:** **Waiver inventory + sunset tracking** — same **license_lifecycle_registry**, extended to waivers and exceptions.
- **Leans on:** Waivers are inventoried, not forgotten.

### S-54: Mars/Starship capex outruns Starlink cash in a tight market.
- **Category:** Time/lifecycle — **Novelty:** 3
- **Attractor:** Runway shortens; SpaceX must slow the flagship program or raise on bad terms, denting the narrative and control.
- **Residue:** **Capital reserve + phaseable Mars spend** — a cash buffer and the ability to throttle Mars/Starship burn to Starlink cash flow (bespoke: **capital_reserve_buffer** + spend-phasing).
- **Leans on:** A5/A10 — Starlink cash flow real; Mars spend genuinely dialable.

### S-55: Legacy Falcon avionics accrue unmaintained tech debt.
- **Category:** Time/lifecycle — **Novelty:** 3
- **Attractor:** A reliability surprise on the cash-cow vehicle while attention is on Starship; the workhorse falters.
- **Residue:** **Sustaining-engineering floor for Falcon** — a maintained minimum team and `runbook_as_code` for the legacy fleet until Starship truly supersedes it.
- **Leans on:** Falcon stays funded for maintenance during the transition.

### S-56 ★: Viral segment alleges a covered-up Crew Dragon safety flaw (true or not).
- **Category:** Black swan (Market/reputation) — **Novelty:** 5
- **Attractor:** NASA and the public question the human-spaceflight keystone; even a false claim triggers reviews and erodes the "flies people safely" brand.
- **Residue:** **Transparent flight-data + rapid-response comms** — the ability to publish defensible telemetry/safety data fast (`event_sourcing_audit_trail` made presentable) plus a standing crisis-comms function (bespoke: **crisis_response_comms**).
- **Leans on:** Real, provable safety data exists and can be shown quickly.

### S-57 ★: Geopolitical crisis forces cutting Starlink to a war zone overnight.
- **Category:** Black swan (Regulatory/geopolitical) — **Novelty:** 5
- **Attractor:** SpaceX is caught between governments; either action makes it a party to a conflict, with liability and licence-to-operate exposure on all sides.
- **Residue:** **Sovereign-use governance policy** — a pre-agreed framework and government-controlled decision path (e.g., defense contracts that put battlefield-service decisions in government hands, not the founder's) (bespoke: **sovereign_use_policy**).
- **Leans on:** Contracts/policies exist that pre-assign these decisions to a legitimate authority.

### S-58 ★: A rival buys controlling stakes in two sole-source suppliers and weaponizes them.
- **Category:** Black swan (Supply-chain) — **Novelty:** 5
- **Attractor:** Critical inputs are choked by a competitor at will; production hostage to a hostile owner.
- **Residue:** **Second-source qualification + in-house fallback** — same **second_source_qualification**; the residue that already survives sole-source loss survives hostile ownership too.
- **Leans on:** A9 relaxed — genuine alternatives qualified in advance.

### S-59 ★: On-orbit collision kills a crewed vehicle or the ISS; global launch moratorium.
- **Category:** Black swan (Technical/reputation) — **Novelty:** 5
- **Attractor:** The entire industry — SpaceX included — is grounded; a civilizational-scale reputational and regulatory event.
- **Residue:** **Collision-avoidance evidence trail + crew safety margin** — combination of S-08's `event_sourcing_audit_trail` (prove it wasn't us / prove diligence) and S-18's **crew_safety_margin** (survivable if it is a SpaceX vehicle).
- **Leans on:** A7; defensible maneuver logs; abort capability.

### S-60 ★: Musk unilaterally makes a battlefield Starlink decision; state-level liability crisis.
- **Category:** Black swan (Human/geopolitical) — **Novelty:** 5
- **Attractor:** A single person's decision exposes the company to sovereign liability and destroys government trust; contracts and licence-to-operate at risk.
- **Residue:** **Sovereign-use governance policy** — same **sovereign_use_policy** as S-57: remove unilateral founder discretion over service to conflict parties.
- **Leans on:** Decision rights actually transferred to a governed process.

### S-61 ★: Science links mega-constellation de-orbit burn to atmospheric harm; global backlash.
- **Category:** Black swan (Physical/env) — **Novelty:** 5
- **Attractor:** The constellation's growth model is attacked as an environmental externality; a new regulatory front on the largest strategic asset.
- **Residue:** **Environmental-impact evidence + design margin** — proactive measurement, greener-materials design headroom, and engagement so SpaceX shapes rather than reacts (couples **regulatory_liaison** + regulatory margin design of S-02).
- **Leans on:** Ability to change satellite material/de-orbit design at cost.

### S-62 ★: Convincing deepfake of Musk moves markets or attempts a fraudulent command.
- **Category:** Black swan (Adversarial) — **Novelty:** 5
- **Attractor:** Fraudulent instructions or market/partner panic on a fabricated statement; financial and operational disruption from a trusted-voice attack.
- **Residue:** **Out-of-band verification for high-stakes actions** — `manual_override_with_review`/two-person, out-of-band confirmation for any fleet-level command, wire, or public commitment, regardless of who appears to authorize it.
- **Leans on:** No high-stakes action executes on a single voice/video channel.

### S-63 ★: National-security emergency prompts a move to nationalize/commandeer launch.
- **Category:** Black swan (Regulatory) — **Novelty:** 5
- **Attractor:** Government requisitions capability under emergency powers; commercial control and economics upended.
- **Residue:** **Government-partnership posture + priority-service framework** — deep, contractual government integration (priority national-security launch/Starshield) that makes commandeering unnecessary because SpaceX already serves the need under contract (same **sovereign_use_policy**, partnership facet).
- **Leans on:** Government sees more value in a functioning SpaceX than a seized one.

### S-64: Governance/financing crisis at Musk's other ventures contaminates SpaceX capital.
- **Category:** Human/org — **Novelty:** 4
- **Attractor:** Cross-contamination of investor confidence; SpaceX's fundraising terms worsen for reasons outside SpaceX.
- **Residue:** **Financial ring-fencing + standalone credit story** — clean separation of SpaceX's balance sheet and a fundraising narrative that stands on Starlink cash flow alone (same **capital_reserve_buffer** + separability of S-07).
- **Leans on:** SpaceX financials genuinely independent of Musk's other entities.

### S-65: A private astronaut dies on a commercial mission.
- **Category:** Technical/reputation — **Novelty:** 3
- **Attractor:** The commercial human-spaceflight line and the safety brand take a severe hit; NASA relationship pressured.
- **Residue:** **Crew safety margin + informed-consent + evidence trail** — **crew_safety_margin** (abort/redundancy) plus documented risk consent and flight-data transparency (couples S-18, S-56).
- **Leans on:** Abort/redundancy real; risk disclosure documented.

### S-66: Booster fails catastrophically on landing near a populated area.
- **Category:** Physical/env — **Novelty:** 4
- **Attractor:** Third-party casualties/damage; public-safety licence-to-operate for return-to-launch-site landings revoked.
- **Residue:** **Flight-termination + keep-out enforcement** — autonomous flight-termination and enforced overflight/keep-out zones so a failure lands in a safe area (bespoke: **flight_safety_containment**).
- **Leans on:** FTS reliable; keep-out zones respected by trajectory design.

### S-67: ISS retires before commercial LEO demand matures.
- **Category:** Time/lifecycle — **Novelty:** 3
- **Attractor:** A human-spaceflight revenue pillar disappears with no equivalent replacement demand; Crew Dragon utilization drops.
- **Residue:** **Destination + demand diversification** — cultivate commercial-station and private-mission demand ahead of ISS sunset (same **diversified_revenue_mix**, human-spaceflight facet).
- **Leans on:** Commercial LEO destinations actually materialize on time.

---

## Step 4 — Deduped control portfolio

The 67 residues collapse to **21 controls**. Reused catalogue patterns are noted in `code font`.

| # | Control | Risks covered | Owner-role | Leans on (dependency / assumption) | Notes |
|---|---|---|---|---|---|
| C-01 | **Site redundancy (geographic)** — multiple qualified launch/production/test sites | S-04, S-24, S-31, S-34, S-36, S-37, S-38 | VP Launch & Site Operations | A9 relaxed: real productive capacity at >1 site, esp. a 2nd Starship mount | Sharpest gap is the single Starship pad (S-37); most load-bearing physical control |
| C-02 | **Constellation replenishment cadence** — rolling, cheap self-launch of replacement sats + maneuver margin | S-20, S-32, S-35, S-51 | VP Starlink Engineering | A5/A7: self-launch stays cheap; orbital environment usable | Same capability answers debris, ASAT, storms, and end-of-life |
| C-03 | **Diversified revenue mix** — launch + Starlink + government + human-spaceflight legs | S-06, S-12, S-13, S-15, S-67 | Chief Revenue Officer | A4/A5 relaxed: no single leg load-bearing | Structural hedge; overlaps cost-leadership on margin logic |
| C-04 | **Cost-leadership moat** — reuse + own-launch cost/cadence advantage | S-09, S-10, S-15 | President/COO | A1/A2: launch-cost and cadence lead persist | The offensive control; funds a price war SpaceX chooses |
| C-05 | **Second-source qualification + strategic buffers** — dual-source/in-house + safety stock for parts, materials, propellant | S-39, S-40, S-44, S-58 | VP Supply Chain | A9 relaxed: critical inputs dual-sourced or in-house-capable | `dependency_freeze_window` buffer logic; survives hostile-ownership too |
| C-06 | **Key-person succession + workforce concentration limits** | S-22, S-23, S-25 | Chief People Officer / Board | A6 relaxed: succession real and rehearsed | Applies to founder, propulsion talent, and visa concentration |
| C-07 | **Sovereign-use governance policy** — decision rights over battlefield/geopolitical service pre-assigned to legitimate authority | S-57, S-60, S-63 | General Counsel / Gov Affairs | Contracts pre-assign these decisions off the founder | Directly neutralizes the founder-discretion black swans |
| C-08 | **License & spectrum lifecycle registry** — tracked authorizations, waivers, expiries, named owners | S-52, S-53 | Chief Regulatory Officer | Someone owns the calendar and acts pre-expiry | `dependency_freeze_window`-style scheduled guard; cheap, high-leverage |
| C-09 | **Regulatory margin design** — operate above current debris/compliance thresholds; config-not-redesign | S-02, S-61 | VP Constellation / Regulatory | Design headroom already carried in the fleet | `per_minute_billing_path` "record-both, switch-by-policy" applied to compliance |
| C-10 | **Regulatory liaison + throughput engagement** — proactive FAA/FCC/range capacity work | S-01, S-47, S-61 | Chief Regulatory Officer | A3: regulator engages/scales with SpaceX | Includes mishap-investigation readiness (`runbook_as_code`) |
| C-11 | **Serialized traceability + fleet health** — per-unit build/test/flight audit trail | S-16, S-49, S-50 | VP Quality / Reliability | Per-unit data retained and queryable | `event_sourcing_audit_trail`; scopes defects instead of grounding all |
| C-12 | **Collision-avoidance evidence trail** — logged autonomous maneuver/conjunction decisions | S-08, S-20, S-59 | VP Constellation Ops | Autonomy logs defensible decisions | `event_sourcing_audit_trail`; caps liability, proves diligence |
| C-13 | **Crew safety margin** — launch-escape/abort + redundancy design | S-18, S-59, S-65 | VP Human Spaceflight | Abort independent of failing subsystem | The reputational keystone's technical guardrail |
| C-14 | **Graceful degrade + rapid restore** — read-only/priority modes + restore runbooks (network, OT, billing) | S-17, S-33, S-41, S-43, S-48 | VP Network / IT-OT | Architecture supports partial operation; restore rehearsed | `read_only_degraded_mode` + `backpressure` + `outbox` reconciliation |
| C-15 | **Staged rollout + remote rollback** — canary + reversible terminal/software updates | S-19, S-55 | VP Software | Terminals accept staged reversible updates | `progressive_rollout` + `feature_flag_kill_switch` |
| C-16 | **Geofencing + terminal enable/kill by region** | S-05, S-30 | VP Starlink Product / Compliance | Central terminal authorization keyed to jurisdiction/location | `feature_flag_kill_switch` at authorization layer; lawful withdraw/restore |
| C-17 | **Command-uplink hardening + dual-control + out-of-band verification** | S-27, S-62 | CISO | No single credential/channel commands the fleet or authorizes high-stakes acts | `key_rotation_dual_accept` + `manual_override_with_review` + `audit_log_immutability` |
| C-18 | **Least-privilege + immutable access audit + export-control spine** | S-03, S-29 | CISO / Trade Compliance | Access compartmented; audit tamper-evident | `audit_log_immutability`; prevents & proves IP/data control |
| C-19 | **Anti-jam / frequency-agility mode** | S-28 | VP RF / Starshield | Terminals/network support switchable resilient mode | `feature_flag_kill_switch` selecting hardened waveform |
| C-20 | **Capital reserve + phaseable Mars spend + financial ring-fence** | S-42, S-54, S-64 | CFO | A5/A10: Starlink cash real; Mars burn dialable; books separable | Self-insurance facet (S-42) leans on flight-heritage reliability |
| C-21 | **Crisis-response comms + flight-data transparency** | S-56, S-26, S-65 | Chief Communications Officer | Provable safety data exists and can be shown fast | Includes founder–company brand firewall (S-26) |
| C-22 | **Per-cell capacity governance + tiered priority SLA** | S-45, S-46 | VP Starlink Network | Real-time cell capacity visibility; enforceable priority tiers | `per_tenant_quota` + `bulkhead`; stop-selling beats degrade-all |
| C-23 | **Segmented OT + tested offline restore** | S-33 | CISO / VP Manufacturing | OT isolated from IT; restore rehearsed | Folded operationally into C-14; kept visible for the ransomware path |
| C-24 | **Multi-partner breadth (carriers, ranges, processors, backhaul)** | S-11, S-14, S-41, S-43, S-47 | Chief Commercial Officer | >1 relationship per critical distribution path | `bulkhead` across partners; the recurring "never sole-path" pattern |
| C-25 | **Flight-safety containment** — autonomous flight-termination + keep-out enforcement | S-66 | VP Range Safety | FTS reliable; keep-out zones respected | Public-safety licence-to-operate for landings |

*(25 rows after keeping the ransomware and flight-safety instances visible; the operational core is ~21 distinct capabilities, with C-23 nested under C-14 and C-24 the connective "no sole-path" tissue across several.)*

---

## Step 5 — Contagion / systemic-risk analysis

### Top cascade paths (plain sentences)

1. **The single Starship pad is the sharpest coupling in the model.** If the sole Starship mount is lost (S-37, and reachable via S-31 attack, S-34 hurricane, S-04 environmental halt, S-24 labor stoppage), then C-01 (site redundancy) is the *only* control standing between "a bad day" and "the entire next-gen program pauses." Every attractor that routes through Starbase concentrates here. Until a second Starship pad is genuinely flight-ready, C-01 is a promise, not a residue.

2. **Everything leans on Elon Musk.** Assumption A6 threads through S-22 (incapacity), S-26 (political conduct), S-54/S-64 (his credibility underwrites capital), S-60/S-57 (his discretion over Starlink), and S-62 (his voice is the deepfake target). C-06 (succession), C-07 (sovereign-use governance), C-20 (ring-fence), C-21 (brand firewall), and C-17 (out-of-band verification) *all* exist to decouple the enterprise from one person. They share the single hidden assumption "the company can act without the founder in the room." If that assumption is false, five controls fail together on the same day.

3. **The orbital-commons assumption (A7) couples four controls.** C-02 (replenishment), C-12 (avoidance evidence), C-09 (regulatory margin), and C-13 (crew safety) all assume LEO stays usable. A debris cascade (S-20), an ASAT (S-32), or the S-59 black swan degrades the shared substrate — and the controls that are supposed to be independent hedges all lean on the same physical environment.

4. **"Self-launch stays cheap" (A5/A1/A2) is the economic keystone.** C-02 (affordable replenishment), C-03 (revenue mix), C-04 (cost moat), and C-20 (Mars burn is dialable because Starlink pays) all lean on reusability continuing to work at high reliability. A common-mode reuse failure (S-16, S-50) or a Starship grounding (S-01) doesn't just hit one control — it removes the cost advantage that funds the others.

5. **Central terminal-authorization control is dual-use and double-edged.** C-16 (geofencing) is the residue for both lawful withdrawal (S-05) and sanctions enforcement (S-30) — and it is the *same mechanism* an attacker would target (S-27) and a government would commandeer (S-63). The control that grants resilience also concentrates a single lever over millions of terminals; its own compromise is a systemic event.

6. **Regulatory throughput (A3) couples the launch business to a single external actor.** C-10 (liaison), C-01's usefulness (you can have five pads but still need range slots), and C-08 (license lifecycle) all assume the FAA/FCC move on a workable timeline. A regulatory freeze (S-01) or a scheduling ceiling (S-47) throttles cadence regardless of how much physical redundancy exists — the bottleneck moves outside the fence.

7. **Vertical integration is a coupling, not just a moat.** The internal launch-subsidy that powers C-04 and C-03 is exactly what antitrust (S-07) attacks and what a strict-liability regime (S-08) makes dangerous. The strength and the systemic exposure are the same structural fact.

### Orphan controls (risk theatre check)

- No pure orphans emerged — every control maps to ≥1 live stressor. **C-19 (anti-jam)** and **C-25 (flight-safety containment)** are the thinnest (one stressor each: S-28, S-66). They are not theatre — both are catastrophic-tail controls — but they carry no shared load, so they are candidates to fold under broader owners (C-19 under C-14/Starshield ops; C-25 under C-10 range safety) rather than staffed as standalone programs.

### Under-covered stressors (single-control coverage)

- **S-37 (single Starship pad)** — covered only by C-01, which is itself aspirational until a second mount flies. Highest-priority under-coverage in the whole analysis.
- **S-21 (GPS/timing denial)** — covered only by the `local_autonomy` fallback implied in its residue; not represented by a portfolio control. **Gap flagged: onboard-timing independence deserves its own named control.**
- **S-28 (jamming)** and **S-66 (landing safety)** — single-control tails as above.
- **S-67 (ISS sunset)** — leans entirely on C-03's human-spaceflight facet, which depends on external commercial-station demand SpaceX does not control.

---

## Step 6 — Resilience regime verdict

**Verdict: SpaceX sits at the *edge of chaos*, tilted toward chaotic on a few named axes.**

The portfolio is the signature of an edge-of-chaos enterprise: **few, load-bearing, mostly loosely-coupled controls** (67 stressors collapse to ~21 capabilities), and failures that are designed to stay contained (serialized traceability scopes defects rather than grounding fleets; per-cell governance stops-selling instead of degrading-all; staged rollout contains bad builds). Very little of the stack is bespoke exception-handling — a healthy sign, and the opposite of the *frozen* regime. This is an organization built to absorb novelty, not just logged risk.

But three couplings pull it toward *chaotic*, where a single shared dependency cascades org-wide:

1. **Founder-coupling (A6).** Five decorrelated-looking controls (C-06, C-07, C-17, C-20, C-21) all lean on "the company can act without Musk." That is one hidden node carrying five edges — the classic chaotic signature.
2. **Single-Starship-pad concentration (A9 at its weakest point).** The most valuable future asset routes through one physical point that four different stressor classes can take out.
3. **Self-launch-economics keystone (A1/A2/A5).** The cost advantage that funds most other controls is itself a single point; reusability faltering removes the funding for resilience.

**Concrete deltas to move firmly to the edge:**

- **Decouple the founder node.** Make C-06/C-07/C-20 real and *rehearsed* — a named, exercised operating succession; sovereign-use decision rights contractually assigned off the founder (this alone neutralizes three black swans S-57/S-60/S-63 and blunts S-22/S-26/S-62). This is the single highest-leverage move: it converts five coupled controls into five independent ones.
- **Retire the single-pad concentration.** Bring a second flight-ready Starship mount online so C-01 stops being aspirational. Physical redundancy is the only residue for S-37, and S-37 is the model's sharpest under-covered node.
- **Name the timing-independence and orbital-commons controls explicitly.** Stand up a portfolio control for GPS-denial autonomy (S-21 orphan) and treat "LEO stays usable" (A7) as a monitored, hedged assumption rather than a background given — because C-02/C-12/C-09/C-13 all silently depend on it.

**Caveat (per playbook):** this regime read is a directional brittleness heuristic (NKP intuition), not a Monte-Carlo incident-rate prediction. Re-run quarterly, and on any trigger: a new-market entry, an M&A event, a founder-availability change, a major mishap, a regulatory regime shift, or loss of any single-site/sole-source dependency.

---

## Deliverable metadata

- **Stressor count:** 67 (8 black swans, novelty 5).
- **Deduped controls:** ~21 core capabilities (25 portfolio rows, with nested/connective controls kept visible).
- **Owner of this artefact:** Chief Risk Officer (to be assigned); re-run cadence quarterly plus the trigger list above.

---

## Completeness pass — additional stressors

**Purpose:** a second-pass sweep for stressors the first pass (S-01–S-67) missed. These are *net-new and non-duplicative* — each was checked against every existing card. They cluster in under-mined angles: policy swings by administration, orbital-slot/spectrum diplomacy (ITU), astronomy/dark-sky, aviation-airspace conflict, on-orbit rendezvous threats (distinct from debris/ASAT), software monoculture, workforce liquidity and ground-safety culture, maritime recovery, seismic single-site (Hawthorne), reentry-casualty and de-orbit liability, foundry geopolitics, and the operational load of a filling LEO. Numbering continues from **S-68**; novelty and category conventions match Step 2. New black swans (novelty 5) marked ★.

| # | Stressor | Category | Novelty |
|---|---|---|---|
| S-68 | A new US administration cancels or restructures Artemis/HLS, pulling a marquee development-funded Starship program. | Regulatory/legal | 3 |
| S-69 | A foreign administration files an ITU orbital-slot/spectrum priority ahead of SpaceX, forcing coordination that constrains a shell or band. | Regulatory/legal | 4 |
| S-70 | Astronomers win brightness/radio-quiet regulation or a nuisance lawsuit, forcing satellite dimming and design changes. | Regulatory/legal | 3 |
| S-71 | Terrestrial carriers win an FCC out-of-band-emission ruling that caps direct-to-cell power and kneecaps the service. | Regulatory/legal | 3 |
| S-72 | Airlines and aviation regulators push back on launch/reentry airspace closures, capping usable launch windows. | Regulatory/legal | 3 |
| S-73 | Lawful-intercept / user-data mandates across jurisdictions force SpaceX to build interception or exit markets. | Regulatory/legal | 3 |
| S-74 | A government invokes a common-carrier / mandatory-service obligation forcing SpaceX to keep serving (or restore) a region it wants to exit. | Regulatory/legal | 4 |
| S-75 | A mega-customer builds captive launch or satellites specifically to escape dependence on SpaceX. | Market/competitive | 3 |
| S-76 | A common-mode defect in the shared flight-software codebase grounds multiple vehicle lines at once. | Technical/infra | 4 |
| S-77 | A common-mode optical inter-satellite laser-link failure degrades the constellation's space backbone. | Technical/infra | 3 |
| S-78 | A user-terminal battery/thermal fire triggers a mass product-safety recall of the installed base. | Technical/infra | 3 |
| S-79 | Ground-worker injury rates at Starbase/factories become a public and OSHA/regulatory scandal. | Human/org | 3 |
| S-80 | Absence of employee liquidity (no tender offer, or a down-round) triggers a wave of senior attrition. | Human/org | 4 |
| S-81 | Culture/discrimination litigation or an exposé damages the employer brand and recruiting pipeline. | Human/org | 2 |
| S-82 | A co-orbital adversary "inspector" satellite shadows and threatens Starlink assets at close range. | Adversarial/abuse | 4 |
| S-83 | A firmware/software supply-chain implant reaches terminals or the satellite bus via a trusted vendor. | Adversarial/abuse | 4 |
| S-84 | Mass adoption of Starlink by cartels/criminal networks forces a government-pressured user-policing crackdown. | Adversarial/abuse | 3 |
| S-85 | An adversary geolocates and targets Starlink users from terminal RF emissions, endangering them. | Adversarial/abuse | 4 |
| S-86 | A major earthquake damages the primary Hawthorne factory/HQ, the most concentrated production single-point. | Physical/env | 3 |
| S-87 | A water-discharge or chemical-spill violation at Starbase (deluge water) triggers pollution enforcement and penalties. | Physical/env | 3 |
| S-88 | Loss of a droneship or rough-sea recovery casualty disrupts booster recovery and reuse economics. | Physical/env | 3 |
| S-89 | A solar-maximum radiation / single-event-upset wave quietly degrades satellite electronics reliability fleet-wide. | Physical/env | 3 |
| S-90 ★ | A de-orbiting satellite survives reentry and causes a ground casualty or property damage. | Black swan (Physical/legal) | 5 |
| S-91 | Counterfeit or substandard parts infiltrate the supply chain, seeding latent reliability failures. | Supply-chain/vendor | 3 |
| S-92 | A custom-ASIC foundry (e.g., Taiwan/TSMC) allocation loss or geopolitical cutoff starves satellite/terminal chips. | Supply-chain/vendor | 3 |
| S-93 | As LEO fills, conjunction-alert and space-traffic-coordination load scales super-linearly and overwhelms constellation operations. | Scale/load | 4 |
| S-94 | Selling user terminals below cost at subscriber scale ties up working capital and inverts if growth outruns financing. | Scale/load | 3 |
| S-95 | Operating under 100+ national regulatory regimes creates a market-access licensing throughput bottleneck. | Scale/load | 3 |
| S-96 | The obligation to responsibly de-orbit tens of thousands of satellites accrues into a long-tail balance-sheet and reputational liability. | Time/lifecycle | 4 |
| S-97 | Investor and talent fatigue with a perpetually-deferred Mars payoff erodes the valuation premium and mission-driven retention. | Time/lifecycle | 4 |

**Coverage of the pass:** Regulatory/legal 7 (S-68–74), Market/competitive 1 (S-75), Technical/infra 3 (S-76–78), Human/org 3 (S-79–81), Adversarial/abuse 4 (S-82–85), Physical/env 4 (S-86–89), Supply-chain/vendor 2 (S-91–92), Scale/load 3 (S-93–95), Time/lifecycle 2 (S-96–97), plus 1 new black swan (S-90). Total **30 new stressors**.

---

### Attractor + residue per new stressor

Control names in `code font` reuse `residue_library.md`; **bold** names reuse the bespoke controls already defined in Steps 3–4 (e.g. **diversified_revenue_mix**, **sovereign_use_policy**, **license_lifecycle_registry**, **second_source_qualification**, **capital_reserve_buffer**, **regulatory_liaison**, **constellation_replenishment_cadence**, **flight_safety_containment**, **crisis_response_comms**, **key_person_succession**, **cost_leadership_moat**, **brand_firewall**). A few genuinely new bespoke controls are introduced and named on first use.

#### S-68: New administration cancels/restructures Artemis-HLS.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** A major government-funded Starship development stream evaporates mid-program; the moon-lander milestones that de-risk Starship for investors slip, and a marquee credibility contract turns into a stranded-cost overhang. Falcon/Starlink cash intact, but the "government pays us to develop the future" leg is gone.
- **Residue:** **diversified_revenue_mix** (program facet) — never let a single cost-plus/milestone program be load-bearing for Starship development; keep Starlink-funded Starship progress independent of any one NASA award, and structure milestones so cancellation returns delivered value rather than a hole.
- **Leans on:** A5/A10 — Starlink cash can carry Starship independent of NASA; program is a top-up, not the engine.

#### S-69: Foreign administration files ITU slot/spectrum priority ahead of SpaceX.
- **Category:** Regulatory/legal — **Novelty:** 4
- **Attractor:** SpaceX is forced into unfavorable coordination or must protect a rival's prior filing, constraining a shell or band it planned to use; the "spectrum stays ours" assumption (A8) is challenged by the international queue, not the FCC.
- **Residue:** **license_lifecycle_registry** (filing-priority facet) — a proactive ITU filing/coordination function that secures and defends priority dates across administrations and tracks every rival filing that could encroach; couples to **regulatory_liaison**.
- **Leans on:** A8; someone owns international filing priority, not just domestic FCC authorizations.

#### S-70: Astronomers win brightness/radio-quiet regulation or a nuisance suit.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** A new compliance front on the constellation's optical and RF footprint; retrofit/dimming obligations raise per-satellite cost and slow deployment, and the dark-sky lobby becomes a durable adversary in every launch approval.
- **Residue:** **Brightness/emission design margin** — carry darksat/dielectric-mirror and RF-sidelobe headroom in the satellite design so a tightening is met by config/coating choice, not redesign (the S-02/S-61 "regulatory margin design," optical+RAS facet); couples **regulatory_liaison** to shape the standard.
- **Leans on:** Ability to change coating/emission design at bounded cost; astronomy engagement is proactive.

#### S-71: Carriers win an out-of-band-emission ruling capping direct-to-cell.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** The direct-to-cell growth vector is throttled at the physics/regulatory layer just as it scales; a hard power/emission cap shrinks the addressable service and hands terrestrial incumbents the win.
- **Residue:** **Spectrum-agility + partner-spectrum fallback** — `feature_flag_kill_switch`-style ability to operate D2C on partner-licensed spectrum and adjust power/duty-cycle profiles per ruling, plus **regulatory_liaison** to defend the emission case with real interference data.
- **Leans on:** More than one spectrum/power operating profile is technically supported; carrier partners' licensed spectrum is available as fallback.

#### S-72: Aviation/airspace backlash caps launch and reentry windows.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** Launch and reentry airspace closures collide with airline economics; regulators impose window/frequency limits, and the cadence advantage is throttled from outside the fence just as flight rate climbs.
- **Residue:** **Range/window diversification + collaborative airspace integration** — spread launches across ranges/windows (`bulkhead` across ranges) and invest in dynamic, short-duration airspace-integration tooling so each launch closes less airspace for less time; couples **regulatory_liaison** (FAA ATO/AST).
- **Leans on:** A3 — regulator/ATC scales cooperatively; trajectory design can minimize airspace footprint.

#### S-73: Lawful-intercept / user-data mandates across jurisdictions.
- **Category:** Regulatory/legal — **Novelty:** 3
- **Attractor:** Conflicting national demands to intercept traffic or hand over user data; comply and breach another jurisdiction's law (and user trust), or refuse and lose market access. A compliance vice with no universal answer.
- **Residue:** **Jurisdictional compliance + market-exit switch** — per-jurisdiction lawful-access handling with `audit_log_immutability` over every disclosure, plus the geofencing/enable-kill control (C-16) to cleanly exit a market rather than violate law; couples `manual_override_with_review` on every access request.
- **Leans on:** Central per-jurisdiction policy control; disclosures are gated, logged, and provable.

#### S-74: Mandatory-service / common-carrier obligation forces SpaceX to keep serving.
- **Category:** Regulatory/legal — **Novelty:** 4
- **Attractor:** The mirror image of the "switch it off" black swans (S-57/S-60): a government legally compels continued or restored service to a region SpaceX (or an allied government) wants dark — turning a discretionary product into a regulated utility with sovereign-liability exposure on the *keep-on* side.
- **Residue:** **sovereign_use_policy** (keep-on facet) — the same pre-assigned decision-rights framework must resolve compelled-service demands, not just withdrawal; contracts specify which authority can compel service and who bears the resulting liability.
- **Leans on:** Decision rights and liability allocation are contractually pre-agreed for *both* directions of the service switch.

#### S-75: A mega-customer in-sources launch/satellites to escape dependence.
- **Category:** Market/competitive — **Novelty:** 3
- **Attractor:** A large buyer (a government, a hyperscaler, a primes consortium) funds a captive alternative purely to avoid SpaceX dependence, seeding a subsidized long-run competitor and shrinking a flagship account regardless of SpaceX's price.
- **Residue:** **cost_leadership_moat** (make-vs-buy facet) — keep SpaceX so much cheaper and faster than in-housing that "build your own" never pencils; pair with **diversified_revenue_mix** so no single fearful customer is load-bearing.
- **Leans on:** A1/A2 — the cost/cadence gap versus a new entrant stays wide enough to deter vertical make.

#### S-76: Common-mode defect in the shared flight-software codebase.
- **Category:** Technical/infra — **Novelty:** 4
- **Attractor:** Because Falcon, Dragon, and Starship share flight-software lineage, one latent fault can implicate multiple vehicle lines at once — a software monoculture that could ground the whole fleet, not one product.
- **Residue:** **Flight-software assurance + staged activation** — `shadow_traffic` (fly new logic in monitor-only before it commands), `progressive_rollout` of software loads across tail numbers, and version/serialized traceability so a fault is scoped and rolled back per vehicle rather than grounding all; couples S-19/S-49.
- **Leans on:** Software is versioned per vehicle and reversible in flight-config; canary/telemetry catches the fault before broad activation.

#### S-77: Common-mode optical inter-satellite laser-link failure.
- **Category:** Technical/infra — **Novelty:** 3
- **Attractor:** The space-based mesh backbone degrades fleet-wide, forcing traffic back to ground stations and cutting coverage where no gateway is in view (oceans, remote, contested); a differentiated capability quietly becomes a liability.
- **Residue:** **Graceful degrade to bent-pipe + laser fleet-health** — `read_only_degraded_mode`/`local_autonomy` fallback that reroutes via ground gateways when the mesh degrades, plus per-terminal laser health telemetry (`event_sourcing_audit_trail`) to scope the defect.
- **Leans on:** Enough ground-gateway coverage exists to carry degraded traffic; laser links are not the sole path in served regions.

#### S-78: User-terminal battery/thermal fire triggers a mass recall.
- **Category:** Technical/infra — **Novelty:** 3
- **Attractor:** A consumer product-safety event across a huge installed base: recall cost, regulatory action (CPSC/international), and a safety-brand hit on a device sitting on millions of homes and vessels.
- **Residue:** **Batch traceability + remote thermal safe-mode + recall runbook** — per-batch serialized build data (`event_sourcing_audit_trail`) to scope the recall to affected lots, a firmware thermal-limit safe-mode pushed via `feature_flag_kill_switch`, and **crisis_response_comms** for the recall.
- **Leans on:** Terminals are batch-traceable and remotely throttleable; a firmware mitigation exists short of physical recall.

#### S-79: Ground-worker safety record becomes an OSHA/public scandal.
- **Category:** Human/org — **Novelty:** 3
- **Attractor:** Injury data and worker accounts drive OSHA action, litigation, and a "moves fast, hurts people" narrative that undercuts recruiting and the mission brand; local/federal licence-to-operate pressure at the sites.
- **Residue:** **Safety-management system + transparent incident data** — a genuine SMS with `runbook_as_code` for hazardous operations and `event_sourcing_audit_trail` over incidents/near-misses (bespoke: **safety_culture_program**); couples **crisis_response_comms**.
- **Leans on:** Injury/near-miss data is actually captured and acted on, not suppressed; leadership funds the safety floor against schedule pressure.

#### S-80: Employee-liquidity gap or down-round triggers senior attrition.
- **Category:** Human/org — **Novelty:** 4
- **Attractor:** With no IPO, employee equity value hinges on periodic tender offers; a skipped tender, a valuation cut, or a capital-market freeze strands illiquid comp and senior engineers walk for liquid rivals — draining the crown-jewel talent (couples S-23).
- **Residue:** **Liquidity program + retention design** — a predictable secondary-liquidity mechanism backed by **capital_reserve_buffer**, plus retention structuring so critical talent isn't wholly dependent on a single liquidity event (bespoke: **employee_liquidity_program**); couples **key_person_succession**.
- **Leans on:** A10 — capital access supports recurring tenders; retention isn't a single illiquid cliff.

#### S-81: Culture/discrimination litigation damages the recruiting brand.
- **Category:** Human/org — **Novelty:** 2
- **Attractor:** Employment litigation or an exposé erodes the employer brand and narrows the top-of-funnel exactly where SpaceX competes hardest — early-career elite engineers who have alternatives.
- **Residue:** **crisis_response_comms + brand_firewall** (employer facet) — separate institutional mission/credibility from individual conduct and respond with evidence; folds into **safety_culture_program** governance for prevention.
- **Leans on:** The company's mission draw is separable from specific conduct allegations; governance addresses root causes.

#### S-82: Co-orbital adversary "inspector" satellite threatens Starlink assets.
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Attractor:** A hostile maneuverable satellite shadows, inspects, or threatens SpaceX assets at close range — a co-orbital ASAT posture distinct from debris (S-32): no cloud, just a live threat to specific spacecraft and to national-security payloads riding the bus.
- **Residue:** **Space domain awareness + evasive autonomy** — onboard/network detection of approaching objects with autonomous evasive maneuvering (`local_autonomy`) and a logged decision trail (`event_sourcing_audit_trail`) for attribution (bespoke: **space_domain_awareness**); couples S-20/S-32 avoidance margin.
- **Leans on:** A7; maneuver margin and conjunction/approach detection that sees a cooperative-looking threat.

#### S-83: Firmware/software supply-chain implant via a trusted vendor.
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Attractor:** A malicious implant enters through a signed vendor update or a compromised build dependency and reaches terminals or the satellite bus — bypassing the perimeter because it arrives via the trusted channel (distinct from the direct intrusion of S-27 and the IT ransomware of S-33).
- **Residue:** **Signed, reproducible builds + staged activation + dependency control** — reproducible builds with `audit_log_immutability` over the pipeline, `dependency_freeze_window` and provenance checks on third-party code, and `progressive_rollout`/`shadow_traffic` so an implant is caught before fleet-wide activation.
- **Leans on:** Build provenance is verifiable end-to-end; nothing ships to the fleet without staged, monitored activation.

#### S-84: Criminal/illicit mass adoption forces a user-policing crackdown.
- **Category:** Adversarial/abuse — **Novelty:** 3
- **Attractor:** Cartels, illegal miners, or sanctioned militias adopt Starlink at scale in otherwise-legal markets; governments demand SpaceX identify, throttle, or cut illicit users, turning a connectivity provider into a policing agent with reputational and regulatory exposure (distinct from S-30's sanctioned-geography activation).
- **Residue:** **User vetting + geofenced enforcement + reviewable takedown** — KYC/activation vetting and location-aware enforcement (bespoke: **user_vetting_kyc**) plus geofencing (C-16) and `manual_override_with_review` on user takedowns so enforcement is lawful, targeted, and auditable.
- **Leans on:** Central activation control keyed to identity and location; takedowns are reviewable, not arbitrary.

#### S-85: Adversary geolocates and targets users from terminal RF emissions.
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Attractor:** In a contested zone, an adversary direction-finds Starlink terminal emissions to target the operator; the product's presence becomes a danger to its users, denting the "resilient connectivity" value proposition where it matters most (couples S-28).
- **Residue:** **Low-probability-of-intercept / emission-control mode** — a hardened terminal operating mode (reduced/agile emissions, beam discipline) invoked in contested zones via `feature_flag_kill_switch`, degrading gracefully to protect the user; couples the S-28 anti-jam control.
- **Leans on:** Terminals support an emission-controlled resilient waveform/mode; users in-theatre can invoke it.

#### S-86: Major earthquake damages the primary Hawthorne factory/HQ.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** The most concentrated production single-point — the Hawthorne factory on active Southern California faults — is offline for months; engine/vehicle/hardware output and core engineering are hit at the source (physical analogue of S-31, non-adversarial).
- **Residue:** **Site redundancy (manufacturing) + seismic hardening** — the S-04/C-01 geographic-redundancy control extended to manufacturing/engineering (real productive capacity beyond Hawthorne, e.g. Texas) plus seismic resilience of the critical lines.
- **Leans on:** A9 relaxed — critical manufacturing is not solely Hawthorne-dependent; work can shift sites.

#### S-87: Water-discharge/chemical-spill violation at Starbase.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** Deluge-water or propellant/chemical discharge draws a pollution-enforcement action and penalties, adding an operational-compliance front distinct from the wetlands construction halt (S-04) and hardening the environmental opposition to cadence.
- **Residue:** **Environmental margin + monitoring evidence** — operate discharge/containment systems with margin above permit limits and maintain defensible monitoring data (`event_sourcing_audit_trail`, environmental facet) so compliance is provable; couples **regulatory_liaison**.
- **Leans on:** Containment/monitoring designed above the threshold; discharge data captured and defensible.

#### S-88: Droneship loss or rough-sea recovery casualty.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** A droneship is lost or repeatedly weathered-out, and boosters that would have been recovered are expended or lost — the reuse cost advantage erodes launch-by-launch, and the maritime-recovery chokepoint seizes.
- **Residue:** **Recovery-asset redundancy + RTLS fallback** — multiple droneships/ports plus a return-to-launch-site landing option so no single vessel/sea-state is the sole recovery path (`bulkhead` across recovery modes); couples C-01 site logic.
- **Leans on:** More than one recovery asset and an RTLS profile exist; port access is not single-sourced.

#### S-89: Solar-max radiation / single-event-upset reliability wave.
- **Category:** Physical/env — **Novelty:** 3
- **Attractor:** Elevated solar-cycle radiation drives single-event upsets and gradual degradation across satellite electronics — a quiet fleet-wide reliability erosion distinct from the acute atmospheric-drag de-orbit of a storm (S-35).
- **Residue:** **Radiation-tolerant design margin + replenishment cadence** — carry radiation/SEU-handling margin (mitigation, watchdog reset, screened parts) and rely on **constellation_replenishment_cadence** to refresh degraded units; couples S-35.
- **Leans on:** A5 — cheap self-launch makes attrition affordable; design carries SEU headroom.

#### S-90 ★: A de-orbiting satellite survives reentry and causes ground casualty/damage.
- **Category:** Black swan (Physical/legal) — **Novelty:** 5
- **Attractor:** The "everything demises on reentry" premise fails publicly with a casualty or property strike; strict-liability claims, a global spotlight on de-orbit design, and pressure to slow or re-file the constellation — a civilizational-trust event for the whole LEO industry (the ground-side analogue of the crewed-collision S-59).
- **Residue:** **Design-for-demise + reentry evidence trail** — engineer satellites to fully demise and log per-satellite de-orbit predictions/telemetry (bespoke: **design_for_demise** + `event_sourcing_audit_trail`) so casualty risk is minimized and diligence is provable; couples the **flight_safety_containment** logic of S-66.
- **Leans on:** Satellites genuinely demisable by design; de-orbit targeting and casualty-risk modeling are defensible.

#### S-91: Counterfeit or substandard parts infiltrate the supply chain.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Fraudulent or out-of-spec components enter high-rate manufacturing and seed latent failures that surface in flight or on-orbit later — a reliability time-bomb amplified by scale and vertical speed.
- **Residue:** **Incoming inspection + serialized part provenance** — authenticated sourcing, incoming test/screening, and per-part serialized traceability (`event_sourcing_audit_trail`) so a bad lot is scoped and purged; couples **second_source_qualification** for authenticated alternates.
- **Leans on:** Parts are provenance-tracked and screened; lots are traceable to affected vehicles/satellites.

#### S-92: Custom-ASIC foundry (Taiwan/TSMC) allocation loss or cutoff.
- **Category:** Supply-chain/vendor — **Novelty:** 3
- **Attractor:** Custom silicon for satellites/terminals is starved by a foundry-allocation squeeze or a Taiwan-geopolitical cutoff; constellation and terminal production throttle on a single fab dependency (distinct from the avionics-chip supplier of S-39 and rare-earths of S-40).
- **Residue:** **second_source_qualification (foundry facet) + design portability + buffer** — qualified alternate fab/process, chip designs portable across nodes, and strategic wafer/inventory buffer so a fab cutoff is absorbed; couples S-39/S-40.
- **Leans on:** A9 relaxed — designs are fab-portable or dual-sourced; buffer covers the qualification lead time.

#### S-93: Conjunction-alert / space-traffic-coordination load overwhelms operations.
- **Category:** Scale/load — **Novelty:** 4
- **Attractor:** As LEO fills (SpaceX's own sats plus rivals), conjunction alerts and coordination requests scale super-linearly; manual maneuver planning and operator coordination saturate, and the *operational burden* — not a collision itself (S-20) — becomes the failure mode.
- **Residue:** **Autonomous conjunction management at scale** — automated, autonomous collision-avoidance and operator-to-operator coordination (`local_autonomy` + **space_domain_awareness**) so maneuver decisions scale without linear headcount; couples S-20/S-82.
- **Leans on:** A7; avoidance is genuinely autonomous and interoperable with other operators' data.

#### S-94: Terminal-hardware subsidy ties up working capital at scale.
- **Category:** Scale/load — **Novelty:** 3
- **Attractor:** Selling terminals below cost to drive subscriber growth ties up escalating working capital; if net-adds outrun financing or ARPU/payback lengthens, growth itself becomes a cash drain rather than a cash engine.
- **Residue:** **Capital-reserve + subsidy/backpressure discipline** — **capital_reserve_buffer** plus the ability to throttle subsidized hardware growth (`backpressure` on below-cost distribution) and flex terminal pricing so growth is financeable, not runaway.
- **Leans on:** A5/A10 — financing supports the subsidy float; terminal economics and pace are dialable.

#### S-95: Market-access licensing across 100+ regimes becomes a bottleneck.
- **Category:** Scale/load — **Novelty:** 3
- **Attractor:** Operating in scores of national regulatory regimes creates a licensing-throughput bottleneck; market entry stalls not on demand or capacity but on a compliance queue SpaceX cannot scale as fast as coverage.
- **Residue:** **Market-access pipeline + per-market isolation** — a scaled **license_lifecycle_registry** with a repeatable market-entry playbook (`runbook_as_code`) and `bulkhead` per market so one regime's delay or rejection doesn't stall the others.
- **Leans on:** Licensing is productized/repeatable; a stalled market is contained, not systemic.

#### S-96: De-orbit obligation for tens of thousands of satellites accrues as liability.
- **Category:** Time/lifecycle — **Novelty:** 4
- **Attractor:** The standing duty to responsibly de-orbit a mega-constellation becomes a long-tail balance-sheet and reputational liability — failed de-orbits, casualty-risk exposure, and end-of-life cost accrue quietly until a regulator or auditor forces recognition (couples S-51 capex, S-90 casualty).
- **Residue:** **De-orbit reserve + demisable design + evidence trail** — reserve for end-of-life disposal (**capital_reserve_buffer**, de-orbit facet), **design_for_demise**, and per-satellite disposal logging (`event_sourcing_audit_trail`) to prove the obligation is funded and met.
- **Leans on:** De-orbit is designed-in and reserved-for, not deferred; disposal is tracked per unit.

#### S-97: Mars-thesis / narrative fatigue erodes premium and retention.
- **Category:** Time/lifecycle — **Novelty:** 4
- **Attractor:** A perpetually-deferred Mars payoff wears down investors and mission-driven talent; the valuation premium and the recruiting magnet that Mars provides fade, raising cost of capital and attrition even with the core businesses healthy (distinct from the cash-runway squeeze of S-54).
- **Residue:** **Stand-alone value story + interim milestone cadence** — a valuation and recruiting narrative that stands on Starlink/launch economics alone (**diversified_revenue_mix** + **brand_firewall**), with credible near-term Starship milestones so the mission stays believable rather than open-ended.
- **Leans on:** Core-business economics justify the valuation without the Mars option; visible interim progress is deliverable.

---

### Pass-level notes (fit with the existing analysis)

- **New bespoke controls introduced:** **safety_culture_program** (SMS + incident transparency, S-79/S-81), **employee_liquidity_program** (S-80), **space_domain_awareness** (approach detection + evasive autonomy, S-82/S-93), **user_vetting_kyc** (S-84), **design_for_demise** (S-90/S-96). The rest reuse Step-4 controls, mostly extending **regulatory_liaison**, **license_lifecycle_registry**, **diversified_revenue_mix**, **second_source_qualification**, **sovereign_use_policy**, **capital_reserve_buffer**, and the `event_sourcing_audit_trail` / `feature_flag_kill_switch` / `progressive_rollout` / `local_autonomy` catalogue patterns.
- **Reinforces the existing contagion reads rather than overturning them.** The founder node (A6) gains S-80 (his other-venture and capital credibility underwrites employee liquidity) and S-97 (his Mars narrative is the premium). The orbital-commons node (A7) gains S-82, S-89, S-93, S-96 — the "LEO stays usable *and* manageable" assumption now carries even more coupled controls. The self-launch-economics keystone (A1/A2/A5) gains S-88 (reuse economics) and S-94 (subsidy float). No new stressor contradicts the edge-of-chaos verdict; several sharpen it.
- **Two new single-external-actor couplings worth flagging:** the **ITU/international filing queue** (S-69) is a spectrum-priority dependency *outside* the FCC that the original A8 treated as domestic; and **foundry geopolitics** (S-92) adds a Taiwan-shaped single point beneath the constellation the original supply-chain set (S-39/S-40) did not name.

---

## Completeness-pass metadata

- **New stressors added:** 30 (S-68 … S-97), including 1 new black swan (S-90).
- **Category spread of the pass:** Regulatory/legal 7, Adversarial/abuse 4, Physical/env 4, Technical/infra 3, Human/org 3, Scale/load 3, Supply-chain/vendor 2, Time/lifecycle 2, Market/competitive 1.
- **Running total after this pass:** 97 stressors (9 black swans).
- **Exhaustion judgement:** After this pass the SpaceX stressor space is *near-exhausted at the category level* — new candidates now tend to be finer-grained variants or recombinations of existing cards (e.g., specific sole-source parts, specific foreign bans, specific mishap modes) rather than genuinely new failure archetypes. The remaining open frontier is mostly **second-order / correlated** scenarios (two stressors co-occurring) and **deep-future** shifts (a physics or business-model change that rewrites the naive operating model itself), which are better handled by the contagion analysis and a periodic re-run than by adding more first-order cards.
