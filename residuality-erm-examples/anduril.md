# Residuality Theory — Enterprise-Risk Analysis: Anduril Industries

> Method: `residuality-enterprise-risk-management.md` (O'Reilly's Residuality Theory, adapted to ERM). Control names in `code font` are drawn from `residuality/references/residue_library.md`; bespoke controls are named in plain italics. Business language in stressors and attractors; mechanism lives in the residue.
>
> Analyst framing note: this is an outside-in analysis built on Anduril's *publicly known* operating model (defense hardware + Lattice software, private capital, fixed-price commercial model, US DoD / CBP / AUKUS customers, ITAR regime, Arsenal manufacturing). It invents **no** classified specifics. Where a control would touch classified detail, the residue is stated at the unclassified business level.

---

## Step 1 — Naive operating model

### Value chain (how money and value flow)

1. **Self-funded R&D** — private venture/growth capital funds product development *ahead* of a contract. This is the core inversion of the prime model: Anduril builds first, sells second.
2. **Productisation** — R&D converges into catalogue products: Lattice OS (command & control, sensor fusion, autonomy backbone), and hardware (Ghost/Anvil drones, Sentry towers, Roadrunner/counter-UAS interceptor, Dive-LD undersea, Fury/CCA, Barracuda).
3. **Manufacturing (Arsenal)** — in-house, software-defined, high-rate manufacturing designed to be re-taskable across products.
4. **Sell fixed-price** — sold to customers at a firm fixed price, contrasting with cost-plus primes (Lockheed, RTX, Northrop). Anduril carries the cost and schedule risk in exchange for margin and speed.
5. **Deploy & sustain** — fielded systems (border towers, drones, C2 nodes) operate in customer environments, often connectivity-constrained, adversarial, or classified; Anduril provides software updates and sustainment.
6. **Capture the next program** — reputation + installed base + Lattice lock-in feed the next competitive win and the next capital raise.

### Core functions that keep the flow alive

- **Product R&D and autonomy/AI engineering** (the crown jewels; talent-bound).
- **Lattice platform engineering and operations** (the software spine that unifies the hardware line and creates switching cost).
- **Arsenal manufacturing and supply chain** (turns designs into deliverable units at rate).
- **Government capture / BD / program management** (wins and runs the contracts).
- **Export & security compliance** (ITAR/EAR, facility clearances, personnel clearances, classified program handling) — the *licence to operate*.
- **Capital markets / finance** (funds the self-funded model; must reach profitability before capital patience expires).

### Critical dependencies

**Internal:** founder/key-person leadership and vision (Palmer Luckey + founding team); a concentrated pool of elite autonomy/AI engineers; the Lattice codebase; the Arsenal production capability; the security-clearance workforce.

**External:** US DoD budget and appropriations (dominant customer / near-monopsony); CBP and allied governments (UK, Australia via AUKUS); advanced compute silicon (GPUs / edge AI chips, ultimately TSMC-fabbed and Nvidia-designed); rare-earth magnets and battery cells (China-concentrated); commercial cloud for non-classified workloads; the political/regulatory permission to build and export lethal autonomy; private capital markets.

### Load-bearing assumptions (stated plainly, no mitigation)

- **A1.** Defense budgets stay large and tilt toward autonomy/software; the strategic threat environment persists.
- **A2.** The US and allies permit building and exporting increasingly autonomous (including lethal) systems.
- **A3.** Capital stays patient enough to fund self-funded R&D until product margins compound.
- **A4.** Advanced compute, magnets, and cells remain purchasable at needed volume and price.
- **A5.** Elite autonomy talent keeps choosing Anduril over primes, big tech, and their own startups.
- **A6.** Fixed-price bids remain profitable — Anduril's cost/schedule estimates hold across multi-year programs.
- **A7.** Lattice remains the integrating layer customers standardise on (switching cost holds).
- **A8.** Key persons (esp. Palmer Luckey) remain both present and a net-positive brand asset.
- **A9.** ITAR/clearance compliance is maintained perfectly enough to avoid debarment — a single catastrophic breach is existential.
- **A10.** Arsenal can scale rate fast enough to meet whatever program Anduril wins.

---

## Step 2 — Exhaustive stressor set

Novelty: 1 = already on any competent defense-contractor risk register; 5 = would not appear in any standard risk register (black swan). 66 stressors across all 9 categories, multiple passes each.

### Regulatory / legal
| # | Stressor | Nov |
|---|---|---|
| S-01 | An ITAR/EAR audit finds an export-control breach on a shipment to an allied government; the State Department opens a debarment proceeding. | 2 |
| S-02 | A new administration issues policy deprioritising lethal autonomous weapons and mandating human-in-the-loop certification for any targeting function. | 3 |
| S-03 | Congress extends cost-accounting and DCAA-style audit obligations to large fixed-price defense suppliers, eroding the commercial-pricing advantage. | 3 |
| S-04 | DOJ/FTC blocks Anduril's planned acquisition of a specialist sensor/autonomy firm on national-security-competition grounds. | 3 |
| S-05 | AUKUS export-license reform stalls in one partner's parliament; UK/Australia deliveries are frozen pending re-authorisation. | 3 |
| S-06 | A US state (or the EU) passes drone-surveillance privacy law restricting Sentry-tower deployment near populated border areas. | 3 |
| S-07 | A foreign customer government is sanctioned or designated mid-contract, making further delivery or support illegal overnight. | 3 |
| S-08 | New AI-safety regulation requires third-party certification and explainability evidence for any autonomous targeting decision before fielding. | 4 |

### Market / competitive
| # | Stressor | Nov |
|---|---|---|
| S-09 | A prime undercuts Anduril on a flagship fixed-price bid by cross-subsidising from cost-plus scale, winning a program Anduril treated as core. | 2 |
| S-10 | A newly-capitalised defense-tech entrant leapfrogs Anduril on a marquee autonomy program. | 3 |
| S-11 | DoD budget priorities swing hard toward shipbuilding and traditional munitions, away from software-defined C2 and small autonomy. | 3 |
| S-12 | Cheap, mass-produced adversary drones make Anduril's higher-cost interceptors economically indefensible (cost-per-kill inverts). | 4 |
| S-13 | A large software/space incumbent (e.g., a Palantir- or SpaceX-scale player) expands directly into Anduril's C2 and autonomy lane. | 3 |
| S-14 | A DoD software factory / government program stands up an in-house C2 layer intended to displace Lattice as the integrating platform. | 3 |
| S-15 | Commercial and open-source autonomy stacks commoditise Ghost-class capability, collapsing hardware margins. | 3 |
| S-16 | A key allied nation elects to build sovereign capability and cancels planned Anduril imports. | 3 |

### Technical / infrastructure
| # | Stressor | Nov |
|---|---|---|
| S-17 | Lattice suffers a platform outage during a live operational deployment, degrading a customer's active mission picture. | 2 |
| S-18 | An autonomy model misclassifies a target in the field, producing a fratricide or civilian-harm incident attributed to Anduril software. | 4 |
| S-19 | A cyber intrusion exfiltrates Lattice source code and program-sensitive data. | 3 |
| S-20 | A publicised field trial shows a flagship product defeated in a GPS/comms-denied environment. | 3 |
| S-21 | A corrupted or poisoned training-data pipeline silently degrades performance across the deployed autonomy fleet. | 4 |
| S-22 | A bad firmware/software update bricks or disables deployed Sentry towers across a whole border sector at once. | 3 |
| S-23 | The commercial cloud region hosting non-classified Lattice workloads suffers a multi-day outage during a demand spike. | 2 |

### Human / organisational
| # | Stressor | Nov |
|---|---|---|
| S-24 | Palmer Luckey exits abruptly (health, dispute, or forced departure), removing the primary vision-and-brand figure. | 3 |
| S-25 | A competitor or a wave of spin-out startups poaches a critical cluster of autonomy/AI engineers in one quarter. | 2 |
| S-26 | A cleared insider is arrested for espionage, triggering a facility-wide security stand-down. | 4 |
| S-27 | An internal ethics revolt (Maven-style walkout) over a lethal-autonomy contract goes public. | 4 |
| S-28 | Explosive headcount growth dilutes engineering rigor; defect and integration-failure rates climb across products. | 2 |
| S-29 | A founder/board rift over strategy or an acquisition splits leadership publicly. | 3 |
| S-30 | The security-clearance workforce can't be staffed fast enough; a newly-won classified program stalls for lack of cleared people. | 3 |

### Adversarial / abuse
| # | Stressor | Nov |
|---|---|---|
| S-31 | A nation-state APT establishes persistent, undetected access inside Anduril's engineering network. | 3 |
| S-32 | An adversary recovers a downed Anvil/Ghost/Barracuda intact and reverse-engineers the autonomy and anti-jam approach. | 4 |
| S-33 | An adversary learns to spoof or blind Sentry sensor fusion, defeating fielded towers en masse without physical contact. | 4 |
| S-34 | A departing insider retains live credentials/access and leaks capability to press or a foreign service. | 3 |
| S-35 | A hardware implant is discovered in a foreign-sourced component already inside shipped products. | 4 |
| S-36 | A coordinated disinformation campaign falsely attributes a civilian-massacre to Anduril systems, engineered to go viral. | 4 |
| S-37 | A customer uses an Anduril system in an operation that draws credible war-crime allegations, associating the brand with it. | 4 |

### Physical / environmental
| # | Stressor | Nov |
|---|---|---|
| S-38 | A fire or industrial accident halts a primary Arsenal manufacturing line. | 2 |
| S-39 | A major earthquake disables California HQ / core engineering site for weeks. | 3 |
| S-40 | Extreme weather (hurricane/heatwave) simultaneously degrades field-deployed towers across a border region. | 2 |
| S-41 | A port or air-cargo closure blocks outbound hardware exports to allied customers at a delivery milestone. | 3 |
| S-42 | Regional grid failure / wildfire forces a prolonged shutdown of a manufacturing and test site. | 2 |
| S-43 | A drone flight-test range is lost (encroachment, airspace revocation, accident) stalling the whole test pipeline. | 3 |

### Supply chain / vendor
| # | Stressor | Nov |
|---|---|---|
| S-44 | Advanced-compute (GPU/edge-AI) allocation is cut by the fab/designer, starving autonomy hardware of its brains. | 3 |
| S-45 | China imposes a rare-earth magnet / gallium export ban, halting drone-motor and sensor production. | 3 |
| S-46 | A critical sub-tier vendor is acquired by a prime competitor who then deprioritises Anduril's orders. | 3 |
| S-47 | A battery-cell supplier ships a latent quality defect that grounds a deployed drone fleet on safety grounds. | 3 |
| S-48 | Cross-strait tension disrupts a Taiwan-dependent component or contract-manufacturing node. | 3 |
| S-49 | Tightened US export controls on AI chips inadvertently block Anduril from equipping *allied* deployments. | 4 |
| S-50 | A commercial software/PLM/cloud vendor Anduril's engineering depends on suffers a supply-chain compromise (SolarWinds-style). | 3 |

### Scale / load
| # | Stressor | Nov |
|---|---|---|
| S-51 | Anduril wins a mega-program (e.g., large CCA/Fury or Barracuda buy) requiring ~100× current output; Arsenal cannot ramp in time. | 3 |
| S-52 | A shooting war creates surge demand that overwhelms production, spares, and field-support capacity at once. | 3 |
| S-53 | The DoD grows past a threshold share of total revenue, giving a single monopsony customer decisive pricing and priority leverage. | 2 |
| S-54 | Multiple allied deployments go live simultaneously, straining a support organisation built for a handful of programs. | 2 |
| S-55 | A single Lattice tenant/program scales its data and node count far beyond design assumptions, degrading the platform for all tenants. | 3 |

### Time / lifecycle
| # | Stressor | Nov |
|---|---|---|
| S-56 | A multi-year fixed-price contract signed pre-inflation is now structurally loss-making to deliver. | 3 |
| S-57 | A "temporary" classified authorisation / interim security waiver quietly lapses and nobody owns the renewal. | 4 |
| S-58 | A government shutdown / prolonged continuing resolution delays contract payments and new-start funding, straining cash. | 2 |
| S-59 | Private-capital appetite for late-stage defense unicorns cools before Anduril reaches self-sustaining margins; a down-round looms. | 3 |
| S-60 | A flagship multi-year program is cancelled at a milestone (Nunn-McCurdy-style breach or reprioritisation), erasing an expected revenue pillar. | 3 |
| S-61 | An early fielded product line reaches obsolescence with no funded upgrade path, and installed-base customers churn. | 3 |
| S-62 | An IPO/liquidity event is attempted into a hostile market, forcing valuation and governance concessions that constrain the model. | 3 |

### Black swans (novelty 5 — would not appear in any standard risk register)
| # | Stressor | Nov |
|---|---|---|
| S-63 | A viral video — real or convincingly deepfaked — shows an "Anduril" autonomous drone killing civilians, and the global public treats it as true within hours. | 5 |
| S-64 | A sudden geopolitical de-escalation / peace settlement collapses the near-term threat narrative and with it the political case for surging autonomy spend. | 5 |
| S-65 | An international treaty banning lethal autonomous weapons systems gains unexpected US signature, criminalising the core product roadmap. | 5 |
| S-66 | Palmer Luckey becomes personally politically radioactive (unrelated scandal or partisan flashpoint), and the founder-brand flips from asset to liability across customers and recruits. | 5 |
| S-67 | An agentic autonomy failure in a live multi-domain *exercise* — a swarm behaving in an unanticipated emergent way — is witnessed by allied officials and leaks. | 5 |
| S-68 | A domestic mass-casualty event caused by a hijacked commercial drone triggers a blanket US moratorium on autonomous airborne systems, sweeping in Anduril's products regardless of fault. | 5 |
| S-69 | An allied host government is overthrown and the new regime nationalises or seizes Anduril's in-country subsidiary, inventory, and IP. | 5 |

**Stressor count: 69** (target 55–70 met; 7 black swans at novelty 5, target ≥6 met).

---

## Step 3 — Attractor + residue per stressor

> Reminder: attractor = do-nothing business end-state (revenue / customers / licence-to-operate / reputation). Residue = *smallest* control that survives it. A control that requires re-founding a division is a second attractor, not a residue.

### S-01 — ITAR/EAR breach found; debarment proceeding
- **Category:** Regulatory / legal · **Novelty:** 2
- **Attractor:** Debarment removes the *licence to operate*; every government contract and export line freezes at once — an extinction-class outcome, not a fine.
- **Residue:** *Export-compliance pre-clearance gate* — a mandatory, logged trade-control check on every shipment/technical-data transfer before release, with a voluntary-self-disclosure playbook that converts a breach into a survivable regulatory event. Reuses `manual_override_with_review` (two-person release with mandatory post-hoc review) and `audit_log_immutability` (the compliance record regulators trust).
- **Leans on:** A9 — that compliance is treated as existential and the audit trail is genuinely tamper-evident.

### S-02 — Policy deprioritises lethal autonomy; human-in-loop mandate
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** The autonomy roadmap loses political permission; revenue reprices around slower, supervised systems and the growth thesis stalls.
- **Residue:** *Human-on-the-loop configurable autonomy* — every autonomous decision path is gated by a configurable supervision mode (`feature_flag_kill_switch` on the autonomous-engagement path) so the same product ships compliant under either policy without a redesign.
- **Leans on:** A2, and that autonomy is architected as a *supervisable* mode, not hard-wired.

### S-03 — Cost-accounting/audit extended to fixed-price suppliers
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** The commercial-pricing advantage over cost-plus primes erodes; margins and the speed narrative that justifies valuation compress.
- **Residue:** *Dual-basis cost accounting* — record both a commercial price and an auditable cost basis on every program from day one, so a regulatory switch is a configuration change, not a rebuild. Reuses `per_minute_billing_path` (alternative billing dimension recorded on every transaction).
- **Leans on:** A6, and finance systems that can carry both bases without re-platforming.

### S-04 — Antitrust blocks a strategic acquisition
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A capability Anduril intended to buy stays with a rival or the open market; a roadmap gap that was going to be closed by M&A reopens.
- **Residue:** *Build-vs-buy optionality* — maintain a costed internal-build fallback for any capability being acquired, so a blocked deal degrades to "slower and in-house," not "capability lost." (bespoke; leans on the self-funded-R&D muscle Anduril already has.)
- **Leans on:** A3, A5 — capital and talent to execute the internal fallback.

### S-05 — AUKUS export license stalls; UK/AU deliveries frozen
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A signed allied revenue stream freezes indefinitely; the AUKUS growth story loses credibility with investors and other allies.
- **Residue:** *In-country delivery footprint* — enough local subsidiary presence (manufacture/integrate/support inside the partner nation) that value can be delivered under domestic authority when cross-border transfer is blocked. Reuses `local_autonomy` (the edge — here a national entity — keeps operating when the central transfer path is unreachable).
- **Leans on:** A2 and the partner keeping a legal path for domestic delivery.

### S-06 — Drone-surveillance privacy law restricts tower deployment
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** The CBP/border installed base becomes partly unlawful to operate; a deployed-revenue line and a reference customer are jeopardised.
- **Residue:** *Privacy-mode configuration* — on-device data-minimisation and geofenced sensing togglable per jurisdiction (`feature_flag_kill_switch` per sensor policy), so a legal change is a config push, not a hardware recall.
- **Leans on:** Sensing policy being software-configurable on fielded units.

### S-07 — Foreign customer sanctioned mid-contract
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** Delivery and support to that customer become instantly illegal; stranded inventory, unpaid milestones, and reputational contamination by association.
- **Residue:** *Sanctions kill-switch clause + license-contingent milestones* — contracts structure payment and delivery around export-license validity so a designation legally suspends, not breaches, the deal. Reuses `feature_flag_kill_switch` (contractual off-switch) and `audit_log_immutability`.
- **Leans on:** A9 and contracts written with the off-switch pre-negotiated.

### S-08 — AI-safety cert required before fielding autonomy
- **Category:** Regulatory / legal · **Novelty:** 4
- **Attractor:** Fielding new autonomy stalls behind a certification queue Anduril can't yet satisfy; time-to-field advantage evaporates.
- **Residue:** *Assurance-evidence pipeline* — continuously generate the test/eval, provenance, and decision-log evidence a certifier will demand, as a by-product of development. Reuses `event_sourcing_audit_trail` (immutable decision/provenance trail) and `shadow_traffic` (validate the new model against real conditions before it serves).
- **Leans on:** A2 and evidence generation being designed-in, not bolted-on.

### S-09 — Prime undercuts a flagship fixed-price bid
- **Category:** Market / competitive · **Novelty:** 2
- **Attractor:** A core program is lost to a cross-subsidised incumbent; the "we win on price and speed" thesis takes a public dent.
- **Residue:** *Lattice lock-in + installed-base pull* — price the platform's integration value so the incumbent's unit-price win still leaves the customer on Anduril's software spine. (bespoke; the switching cost *is* the moat.)
- **Leans on:** A7 — Lattice remains the standard customers integrate on.

### S-10 — Funded entrant leapfrogs a marquee program
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** Anduril loses the innovation-leader perception it recruits and raises capital on; a signature win goes to a rival.
- **Residue:** *Portfolio breadth (no single-program dependence)* — a product catalogue wide enough that losing one program is a setback, not a crisis. Reuses `bulkhead` (isolate one program's failure from the whole book).
- **Leans on:** A1, A3 — sustained multi-line R&D funding.

### S-11 — Budget swings to ships/munitions, away from software C2
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** Demand for the software-and-small-autonomy core softens for years; growth reprices to the new spending mix.
- **Residue:** *Product-mix optionality* — maintain hardware/munitions-adjacent lines (e.g., interceptors, undersea, expendables) so revenue can follow whichever budget line swells. Reuses `per_minute_billing_path` pattern applied to *revenue lines* — record capability against multiple budget categories, pivot by configuration of go-to-market.
- **Leans on:** A1 and a genuinely re-taskable product/manufacturing base.

### S-12 — Cheap adversary drones invert cost-per-kill
- **Category:** Market / competitive · **Novelty:** 4
- **Attractor:** The interceptor value proposition collapses economically; customers stop buying expensive defeats of cheap threats.
- **Residue:** *Low-cost-effector line* — a deliberately cheap, mass-manufacturable counter-mass product so Anduril competes on the same cost curve as the threat. (bespoke; leans on Arsenal's re-taskability — this is a product decision, kept minimal by using existing manufacturing, not a new division.)
- **Leans on:** A10 — Arsenal can produce cheap effectors at mass.

### S-13 — Software/space incumbent enters C2/autonomy lane
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** A scale player with cheaper capital and existing DoD footprint competes Lattice's integrating role; platform pricing power erodes.
- **Residue:** *Hardware+software bundling* — Anduril's owned hardware line is the wedge a pure-software rival can't match; sell the vertically-integrated stack, not the software alone.
- **Leans on:** A7 and continued hardware differentiation.

### S-14 — DoD software factory tries to displace Lattice
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** The customer becomes the competitor at the integration layer; Lattice's strategic centrality and lock-in weaken.
- **Residue:** *Open-interface interoperability* — Lattice exposes standard interfaces so it remains the best node inside a government mesh rather than the thing being replaced. Reuses `local_autonomy` (Anduril's products keep full value even inside someone else's C2).
- **Leans on:** A7 partially relaxing — value must survive *not* being the sole integrator.

### S-15 — Open-source autonomy commoditises Ghost-class hardware
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** Commodity competitors erode drone hardware margins; a product line becomes a low-margin race.
- **Residue:** *Move value up the stack* — margin migrates to Lattice, autonomy, and sustainment where commoditisation is slower. (bespoke; leans on A7.)
- **Leans on:** A7 — the software layer holds value as hardware commoditises.

### S-16 — Ally builds sovereign capability, cancels imports
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** An allied revenue stream is lost to domestic industrial policy; the export-growth thesis narrows.
- **Residue:** *In-country partnership/co-production* — participate in the sovereign build as the technology partner rather than the excluded importer. Reuses the `local_autonomy` / in-country-footprint pattern (see S-05).
- **Leans on:** A2 and willingness to license/co-produce.

### S-17 — Lattice outage during a live deployment
- **Category:** Technical / infrastructure · **Novelty:** 2
- **Attractor:** A customer loses its operational picture during a real mission; trust in the platform's dependability — the whole selling point — is damaged.
- **Residue:** `local_autonomy` — fielded nodes hold enough state and policy to keep operating for N hours without the central plane, syncing on reconnect, with a `read_only_degraded_mode` mission-picture fallback.
- **Leans on:** Edge devices designed to survive disconnection; A7.

### S-18 — Autonomy misclassifies; fratricide/civilian-harm incident
- **Category:** Technical / infrastructure · **Novelty:** 4
- **Attractor:** A lethal error is attributed to Anduril's software; licence-to-operate and the moral case for autonomy — the political permission the whole company runs on — are threatened.
- **Residue:** *Engagement-authority interlock* — the autonomous kill/engage path is gated behind a configurable human authority and a hard `feature_flag_kill_switch`, with `event_sourcing_audit_trail` capturing every decision for accountability. This is both a safety control and the evidence that survives the inquiry.
- **Leans on:** A2 and the decision path being genuinely interruptible and logged.

### S-19 — Lattice source code exfiltrated
- **Category:** Technical / infrastructure · **Novelty:** 3
- **Attractor:** The crown-jewel IP and any embedded classified detail leak; competitive moat and security accreditation both take a hit.
- **Residue:** `audit_log_immutability` + `key_rotation_dual_accept` — tamper-evident access logging to scope the breach fast, and dual-accept credential/cert rotation to slam doors without downtime; a pre-agreed disclosure path to program security offices.
- **Leans on:** A9 and secrets being rotatable on short notice.

### S-20 — Publicised failure in GPS/comms-denied trial
- **Category:** Technical / infrastructure · **Novelty:** 3
- **Attractor:** The core "works in contested environments" claim is publicly falsified; competitive credibility and pipeline confidence drop.
- **Residue:** `local_autonomy` (denied-environment autonomy is a design requirement, tested before demos) + *pre-briefed test-narrative playbook* so a bad trial is framed as iteration, not failure.
- **Leans on:** Autonomy genuinely functioning without GPS/comms.

### S-21 — Poisoned training pipeline silently degrades the fleet
- **Category:** Technical / infrastructure · **Novelty:** 4
- **Attractor:** Deployed autonomy quietly gets worse across the installed base; the failure surfaces as field incidents before anyone links them, compounding reputational harm.
- **Residue:** `shadow_traffic` + *model-provenance gate* — every model candidate is validated against live-representative data before promotion, with signed data/model lineage (`event_sourcing_audit_trail`) so poisoning is caught and traceable.
- **Leans on:** Training data provenance being tracked and validated.

### S-22 — Bad update bricks Sentry towers across a sector
- **Category:** Technical / infrastructure · **Novelty:** 3
- **Attractor:** A border sector goes blind at once; the customer's operational trust and Anduril's sustainment reputation are hit simultaneously.
- **Residue:** `progressive_rollout` + `feature_flag_kill_switch` — updates canary to 1%→10%→100% with automated abort, and a one-switch rollback; `local_autonomy` keeps towers running on last-good config during rollback.
- **Leans on:** Fielded units supporting staged, reversible updates.

### S-23 — Cloud region outage during a demand spike
- **Category:** Technical / infrastructure · **Novelty:** 2
- **Attractor:** Non-classified Lattice services degrade during peak use; SLA and confidence damage.
- **Residue:** `circuit_breaker_fallback_cache` + `read_only_degraded_mode` with a `stale_data_marker` — serve last-good data and read-only function through the outage rather than cascading a hard failure.
- **Leans on:** Read paths tolerant of brief staleness.

### S-24 — Palmer Luckey exits abruptly
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** The primary vision-and-brand figure vanishes; recruiting pull, capital narrative, and customer confidence all wobble at once.
- **Residue:** *Key-person succession + distributed public bench* — a named succession plan and a deliberately multi-headed public leadership bench so the brand isn't single-threaded. Reuses `runbook_as_code` philosophy (critical tacit knowledge externalised) applied to leadership continuity.
- **Leans on:** A8 relaxing gracefully — brand not permanently fused to one person.

### S-25 — Cluster of autonomy engineers poached in a quarter
- **Category:** Human / organisational · **Novelty:** 2
- **Attractor:** Core R&D velocity drops; the talent-advantage thesis (A5) is directly challenged.
- **Residue:** *Knowledge-resilience + retention lock* — critical designs documented (`runbook_as_code`), plus equity/retention structures so no single team's exit halts a program.
- **Leans on:** A3, A5.

### S-26 — Cleared insider arrested for espionage
- **Category:** Human / organisational · **Novelty:** 4
- **Attractor:** A facility-wide security stand-down and loss of government trust; classified programs freeze pending review — a licence-to-operate event.
- **Residue:** *Insider-threat program* — continuous-evaluation monitoring, least-privilege access, and `audit_log_immutability` so scope is provable and the accreditation survives.
- **Leans on:** A9 and least-privilege being real, not nominal.

### S-27 — Public ethics walkout over a lethal-autonomy contract
- **Category:** Human / organisational · **Novelty:** 4
- **Attractor:** Internal dissent becomes an external reputational and recruiting problem; the mission-alignment that Anduril recruits on is publicly contested.
- **Residue:** *Values-explicit hiring + ethics review board* — a stated ethical framework and a real internal review gate so employees self-select in and dissent has a channel short of a walkout. (bespoke; minimal — a governance body, not a restructure.)
- **Leans on:** A5 and leadership genuinely engaging the framework.

### S-28 — Hypergrowth dilutes engineering rigor
- **Category:** Human / organisational · **Novelty:** 2
- **Attractor:** Defect and integration-failure rates rise across products; the quality reputation that justifies fixed-price risk-taking erodes.
- **Residue:** `progressive_rollout` + *design-review gates* — staged fielding and mandatory review checkpoints so scaling headcount can't silently ship regressions.
- **Leans on:** A6 — quality discipline scales with headcount.

### S-29 — Founder/board rift splits leadership publicly
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** Strategic paralysis and a public governance story that spooks customers and capital.
- **Residue:** *Governance charter with tie-break authority* — pre-agreed decision rights and an independent board mechanism so disputes resolve internally, not in the press.
- **Leans on:** A8 and a functioning board.

### S-30 — Can't staff clearances fast enough; program stalls
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** A won classified program can't start; revenue slips and the customer questions delivery capacity.
- **Residue:** *Cleared-talent bench + facility-clearance depth* — maintain a pipeline of in-process clearances and sponsor early, so staffing a new program draws on a bench (`bulkhead` for people — spare cleared capacity ring-fenced from BAU).
- **Leans on:** A9 and clearance throughput.

### S-31 — Nation-state APT persistent in the network
- **Category:** Adversarial / abuse · **Novelty:** 3
- **Attractor:** Sustained IP and program exfiltration; discovery triggers a trust and accreditation crisis.
- **Residue:** `audit_log_immutability` + `key_rotation_dual_accept` + least-privilege segmentation (`bulkhead`/`tenant_isolated_blast_radius`) so an intrusion is contained and scoped, not total.
- **Leans on:** A9 and real network segmentation.

### S-32 — Adversary reverse-engineers a recovered airframe
- **Category:** Adversarial / abuse · **Novelty:** 4
- **Attractor:** A capability edge is neutralised; the customer's confidence in fielded superiority drops and the roadmap must sprint ahead.
- **Residue:** *Anti-tamper + capability compartmentation* — sensitive autonomy/anti-jam logic is protected (anti-tamper, on-capture zeroization) so a recovered unit yields little. Reuses `key_rotation_dual_accept` (recovered keys are already dead).
- **Leans on:** Hardware designed with capture as an expected event.

### S-33 — Adversary learns to spoof Sentry sensor fusion
- **Category:** Adversarial / abuse · **Novelty:** 4
- **Attractor:** Fielded towers can be defeated remotely at scale; the surveillance value proposition collapses for a whole customer base.
- **Residue:** *Rapid model/sensor-fusion update loop* — the ability to push counter-spoofing model updates fleet-wide fast (`progressive_rollout` + `feature_flag_kill_switch`), turning a static target into a moving one.
- **Leans on:** Field-updatable perception stack; connectivity for updates.

### S-34 — Departing insider retains live access, leaks capability
- **Category:** Adversarial / abuse · **Novelty:** 3
- **Attractor:** Sensitive capability reaches press or a foreign service; reputational and security-trust damage.
- **Residue:** *Automated deprovisioning + access recertification* — offboarding revokes all access same-day; `audit_log_immutability` proves the timeline. Reuses `key_rotation_dual_accept`.
- **Leans on:** A9 and identity/access hygiene actually enforced.

### S-35 — Hardware implant found in a shipped component
- **Category:** Adversarial / abuse · **Novelty:** 4
- **Attractor:** Deployed products are suspect; a recall/re-certification wave and customer-trust collapse across the affected line.
- **Residue:** *Component provenance + trusted-supplier attestation* — traceable bill-of-materials and trusted-foundry sourcing for security-critical parts (`event_sourcing_audit_trail` on the BOM) so scope is bounded and defensible.
- **Leans on:** A4 and provenance being tracked at the part level.

### S-36 — Engineered disinformation blames Anduril for a massacre
- **Category:** Adversarial / abuse · **Novelty:** 4
- **Attractor:** The public and possibly customers act on a false attribution within hours; licence-to-operate is threatened faster than facts can travel.
- **Residue:** *Provenance-backed rapid-response comms* — `event_sourcing_audit_trail` of actual system decisions makes fast, evidence-based rebuttal possible; a pre-built crisis-comms playbook executes it in hours, not days.
- **Leans on:** Verifiable decision logs and a standing comms capability.

### S-37 — Customer's use draws credible war-crime allegations
- **Category:** Adversarial / abuse · **Novelty:** 4
- **Attractor:** The brand is associated with an atrocity by proximity; recruiting, allied sales, and political permission all take damage.
- **Residue:** *End-use vetting + contractual use restrictions* — customer/end-use screening and contract terms constraining use, with an off-switch clause (`feature_flag_kill_switch`) as leverage. (bespoke; a policy+contract control, not a division.)
- **Leans on:** A2 and enforceable end-use terms.

### S-38 — Fire halts a primary Arsenal line
- **Category:** Physical / environmental · **Novelty:** 2
- **Attractor:** Production stops; delivery milestones slip and fixed-price penalties/cash timing bite.
- **Residue:** *Multi-site / re-taskable manufacturing* — Arsenal's software-defined re-taskability means another line can pick up critical output; `runbook_as_code` for line-transfer. (Minimal because it uses Arsenal's *existing* re-taskability, not a new plant.)
- **Leans on:** A10 and genuine multi-line/site redundancy.

### S-39 — Earthquake disables California HQ/engineering
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** Core engineering and leadership capacity is offline for weeks; roadmap and delivery slip.
- **Residue:** *Distributed engineering + remote-work continuity* — geographically distributed sites and a tested work-from-anywhere plan (`runbook_as_code` for BCP) so no single campus is a single point of failure.
- **Leans on:** Distributed footprint and secure remote access within accreditation limits.

### S-40 — Extreme weather degrades towers across a region
- **Category:** Physical / environmental · **Novelty:** 2
- **Attractor:** A border region loses coverage simultaneously; customer operational impact and sustainment-cost spike.
- **Residue:** `local_autonomy` + *graceful degradation + rapid field-service* — towers ride out and self-report; a surge field-service plan restores coverage. Reuses `read_only_degraded_mode` for partial-capability operation.
- **Leans on:** Hardware environmental hardening.

### S-41 — Port/air-cargo closure blocks exports at a milestone
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** A delivery milestone is missed for logistics reasons; payment timing and allied-customer confidence suffer.
- **Residue:** *Multi-modal / multi-route logistics* — pre-qualified alternate shipping routes/modes so a single node closure reroutes rather than halts. Reuses `bulkhead` (route isolation).
- **Leans on:** Alternate routes pre-cleared for export.

### S-42 — Grid/wildfire shutdown of a manufacturing+test site
- **Category:** Physical / environmental · **Novelty:** 2
- **Attractor:** Prolonged production and test outage; schedule slip on multiple programs.
- **Residue:** *Site resilience (backup power) + load-shift to alternate site* — critical lines carry backup power; overflow shifts to another Arsenal node. Same residue family as S-38.
- **Leans on:** A10 and site redundancy.

### S-43 — Flight-test range lost
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** The whole airborne-product test pipeline stalls; certification and delivery timelines slip across products.
- **Residue:** *Multi-range access + simulation-first validation* — pre-arranged alternate ranges plus heavy sim/`shadow_traffic`-style validation to reduce live-range dependence.
- **Leans on:** Sim fidelity and range agreements.

### S-44 — Advanced-compute allocation cut
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** Autonomy hardware loses its brains; production of AI-bearing products throttles and the roadmap slows.
- **Residue:** *Multi-source silicon qualification + strategic buffer stock* — qualify more than one compute source and hold a buffer for critical parts. Reuses `dependency_freeze_window` thinking (batch and buffer critical-dependency changes) plus a bespoke second-source qualification.
- **Leans on:** A4 and designs portable across compute vendors.

### S-45 — Rare-earth / gallium export ban
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** Motor and sensor production halts; the hardware line stops at the raw-material level.
- **Residue:** *Strategic material stockpile + non-China qualification* — buffer inventory and qualified alternate-geography suppliers for magnet/gallium-class inputs.
- **Leans on:** A4 and alternate sources existing at volume.

### S-46 — Sub-tier vendor acquired by a prime, deprioritised
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** A critical input's priority is now controlled by a competitor; supply reliability and cost are hostage.
- **Residue:** *Dual-source + in-license/insource option* — a qualified second source and the right/ability to insource a critical part. Reuses the build-vs-buy optionality residue (S-04).
- **Leans on:** A4 and a qualified alternative existing.

### S-47 — Battery-cell defect grounds a drone fleet
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** A fielded fleet is grounded on safety; customer availability and Anduril's sustainment reputation drop together.
- **Residue:** *Batch traceability + rapid recall/rotation* — lot-level `event_sourcing_audit_trail` on cells so only affected units ground, plus a qualified alternate cell to swap in. Reuses `key_rotation_dual_accept` pattern applied to a physical component swap.
- **Leans on:** Lot traceability and a second cell source.

### S-48 — Cross-strait tension disrupts a Taiwan-dependent node
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** A critical component or contract-manufacturing node goes dark; broad production exposure.
- **Residue:** Same *multi-source + buffer* residue as S-44/S-45, plus geographic diversification of critical nodes.
- **Leans on:** A4 and non-Taiwan qualification.

### S-49 — AI-chip export controls block allied deployments
- **Category:** Supply chain / vendor · **Novelty:** 4
- **Attractor:** Anduril can't equip *allied* deployments with the compute they need; allied revenue and AUKUS credibility hit by its own government's rules.
- **Residue:** *Export-tier product variants* — pre-designed compliant configurations at multiple performance tiers so an allied deployment ships with an authorised variant, not nothing. Reuses `feature_flag_kill_switch` (capability tiering by license).
- **Leans on:** A2 and modular compute that supports tiered variants.

### S-50 — Compromise of a commercial software/PLM/cloud vendor
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** A trusted tool becomes an attack vector into engineering; potential IP loss and accreditation impact.
- **Residue:** `dependency_freeze_window` + vendor-SBOM attestation — batch and vet third-party updates, with `audit_log_immutability` to scope any compromise.
- **Leans on:** A9 and vendor supply-chain visibility.

### S-51 — Win a mega-program; Arsenal can't ramp
- **Category:** Scale / load · **Novelty:** 3
- **Attractor:** The signature win becomes a delivery failure; fixed-price penalties, reputational damage, and the "we can scale" thesis all break.
- **Residue:** *Capacity-reservation + surge-manufacturing plan* — pre-planned rate-ramp playbooks and reserved supplier capacity so a big win triggers a rehearsed ramp, not an improvisation. Reuses `runbook_as_code` (the ramp is pre-scripted) and `backpressure` (accept/sequence demand against real capacity).
- **Leans on:** A10 and supplier capacity being reservable ahead of need.

### S-52 — Wartime surge overwhelms production and support
- **Category:** Scale / load · **Novelty:** 3
- **Attractor:** Demand exceeds every shared process at once; the company under-delivers at the moment of maximum strategic and reputational stakes.
- **Residue:** `backpressure` + *prioritisation policy* — explicit demand-sequencing so scarce output goes to the highest-priority mission, surfaced transparently to customers rather than silently failing.
- **Leans on:** A10 and a governance rule for allocation.

### S-53 — DoD crosses a threshold share of revenue (monopsony)
- **Category:** Scale / load · **Novelty:** 2
- **Attractor:** A single customer gains decisive pricing and schedule leverage; margins and independence compress toward the prime model Anduril was built to escape.
- **Residue:** *Customer/geography diversification target* — a managed ceiling on any single customer's revenue share, fed by allied and adjacent-market sales. Reuses `per_tenant_quota` thinking applied to *revenue concentration*.
- **Leans on:** A1, A2 — allied demand exists to diversify into.

### S-54 — Simultaneous allied deployments strain support org
- **Category:** Scale / load · **Novelty:** 2
- **Attractor:** Support quality degrades across programs at once; SLA breaches and reputational erosion in multiple countries.
- **Residue:** `bulkhead` — per-program/per-region support pools so one deployment's surge can't starve the others; in-country support presence (ties to S-05).
- **Leans on:** Support capacity that scales with the installed base.

### S-55 — One Lattice tenant scales past design, degrades all
- **Category:** Scale / load · **Novelty:** 3
- **Attractor:** A noisy mega-program degrades the platform for every other customer; multi-tenant trust erodes.
- **Residue:** `per_tenant_quota` + `bulkhead` + `query_capacity_guard` — per-tenant resource limits and isolation so one program can't consume the platform.
- **Leans on:** A7 and tenant isolation being enforced at every boundary.

### S-56 — Multi-year fixed-price contract now loss-making
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** A signed program bleeds cash to deliver; margin thesis and cash runway both suffer.
- **Residue:** *Economic-price-adjustment clauses + portfolio cross-subsidy* — inflation/EPA clauses in new fixed-price deals, and a portfolio wide enough (`bulkhead`) that one loss-maker doesn't sink the book. For legacy deals, a renegotiation/de-scope playbook.
- **Leans on:** A6 and pricing discipline on new contracts.

### S-57 — "Temporary" classified authorisation lapses unowned
- **Category:** Time / lifecycle · **Novelty:** 4
- **Attractor:** A program silently loses its legal authority to operate; work must stop until re-authorised — an unforced licence-to-operate hit.
- **Residue:** *Authorisation registry with expiry ownership* — every waiver/authorisation has a named owner, an expiry, and an alert. Directly reuses `dependency_freeze_window`/lifecycle-tracking discipline plus `audit_log_immutability`.
- **Leans on:** A9 and someone owning the registry.

### S-58 — Shutdown / continuing resolution delays payments
- **Category:** Time / lifecycle · **Novelty:** 2
- **Attractor:** Contract cash slows while costs continue; the self-funded model's cash cushion is tested.
- **Residue:** *Cash-runway reserve + credit facility* — a deliberate liquidity buffer sized to absorb an appropriations gap without cutting R&D. (bespoke; a treasury policy.)
- **Leans on:** A3 — access to capital/credit on standby.

### S-59 — Capital appetite cools before profitability; down-round looms
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** The self-funded R&D engine loses fuel before margins compound; growth and valuation reprice sharply downward.
- **Residue:** *Path-to-profitability optionality* — the ability to throttle R&D burn toward cash-generative product lines on demand, so survival never depends on the next raise. Reuses `read_only_degraded_mode` philosophy for the business — shed growth spend, keep the core alive.
- **Leans on:** A3 relaxing gracefully — a profitable core exists to fall back to.

### S-60 — Flagship program cancelled at a milestone
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** An expected revenue pillar disappears; guidance, capacity plans, and capital narrative all take the hit.
- **Residue:** *Portfolio breadth + convertible capacity* (`bulkhead`) — no single program is load-bearing, and manufacturing capacity is re-taskable to the next program.
- **Leans on:** A10 and genuine product/program diversification.

### S-61 — Early product line obsoletes with no upgrade path
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** Installed-base customers churn as their systems age out; sustainment revenue and reference accounts decay.
- **Residue:** *Modular upgrade architecture + planned sustainment roadmap* — hardware/software modularity so fielded systems get funded refresh paths rather than dead-ending. (bespoke; a product-lifecycle discipline.)
- **Leans on:** A7 and designed-in modularity.

### S-62 — Hostile-market IPO forces value/governance concessions
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** A liquidity event on bad terms imposes short-term-earnings pressure and governance constraints that undermine the long-horizon self-funded model.
- **Residue:** *Liquidity-timing optionality + dual-class/patient-capital structure* — the ability to defer public listing and secondary structures so employees/investors get liquidity without a forced IPO. (bespoke; a capital-structure choice.)
- **Leans on:** A3 — patient private capital remains available.

### S-63 — Viral (possibly deepfaked) "Anduril kills civilians" video
- **Category:** Adversarial / abuse (black swan) · **Novelty:** 5
- **Attractor:** The public — and possibly customers and recruits — treat it as true within hours; licence-to-operate is threatened at internet speed before facts arrive.
- **Residue:** *Provenance-backed rapid-response comms* (as S-36) — verifiable decision logs (`event_sourcing_audit_trail`) plus a standing crisis-comms + deepfake-forensics playbook that can rebut in hours. This is the *same* residue as S-36 and S-18's audit trail — a key convergence.
- **Leans on:** Verifiable logs and a standing comms capability believed by the public.

### S-64 — Sudden peace / de-escalation collapses the threat narrative
- **Category:** Market / competitive (black swan) · **Novelty:** 5
- **Attractor:** The political case for surging autonomy spend evaporates; multi-year demand and the growth thesis reprice down hard (A1 breaks).
- **Residue:** *Dual-use / adjacent-market pivot optionality* — capabilities (autonomy, sensing, C2, manufacturing) that have non-conflict applications (border, disaster response, critical-infrastructure, commercial autonomy) so demand can partly follow peacetime uses. Reuses the product-mix optionality residue.
- **Leans on:** Genuinely dual-use technology and go-to-market willingness.

### S-65 — US signs a treaty banning lethal autonomous weapons
- **Category:** Regulatory / legal (black swan) · **Novelty:** 5
- **Attractor:** The core lethal-autonomy roadmap becomes illegal; a whole product category and its growth thesis are erased (A2 breaks).
- **Residue:** *Supervised-autonomy + non-lethal-line pivot* — the human-on-the-loop interlock (S-02/S-18) means most products ship compliant as supervised systems, and non-lethal lines (surveillance, C2, undersea, logistics) carry revenue. Same interlock residue, exercised to its limit.
- **Leans on:** Autonomy architected as supervisable, and a viable non-lethal portfolio.

### S-66 — Palmer Luckey becomes personally politically radioactive
- **Category:** Human / organisational (black swan) · **Novelty:** 5
- **Attractor:** The founder-brand flips from asset to liability; customers, allies, and recruits distance themselves and the narrative capital inverts (A8 breaks).
- **Residue:** *Key-person succession + distributed public bench* (as S-24) — an institutional identity and multi-headed leadership so the company can be separated from any one person's reputation.
- **Leans on:** A8 relaxing — the brand can survive de-coupling from its founder.

### S-67 — Emergent agentic swarm failure in a live allied exercise
- **Category:** Technical / infrastructure (black swan) · **Novelty:** 5
- **Attractor:** Allied officials witness autonomy behaving unpredictably; trust in Anduril's autonomy safety — the foundation of every future sale — is shaken, and it leaks.
- **Residue:** *Bounded-autonomy envelope + hard kill-switch* — autonomous behaviour is constrained to a tested operating envelope with a `feature_flag_kill_switch` and geofence/behaviour limits, plus `event_sourcing_audit_trail` to explain what happened. Same interlock family as S-18.
- **Leans on:** A2 and autonomy being genuinely bounded and interruptible.

### S-68 — Domestic drone atrocity triggers blanket autonomy moratorium
- **Category:** Regulatory / legal (black swan) · **Novelty:** 5
- **Attractor:** A moratorium sweeps in Anduril's products regardless of fault; the domestic market for autonomous airborne systems freezes overnight (A2 breaks broadly).
- **Residue:** *Portfolio breadth beyond airborne autonomy + supervised-mode compliance* — undersea, C2, sensing, and supervised configurations keep revenue alive through a category-specific ban. Reuses portfolio-breadth (`bulkhead`) and the supervision interlock.
- **Leans on:** Product diversity across domains and supervisable modes.

### S-69 — Allied host government overthrown; subsidiary nationalised
- **Category:** Physical / environmental (black swan) · **Novelty:** 5
- **Attractor:** In-country inventory, facilities, and IP are seized by a hostile successor regime; a national revenue stream and sensitive technology are lost at once.
- **Residue:** *Sovereign-risk hedging + IP/asset compartmentation* — limit what any single in-country subsidiary holds (capability compartmentation, remote-kill/zeroization for sensitive systems — reuses `key_rotation_dual_accept` and anti-tamper from S-32), plus political-risk insurance so the financial loss is survivable.
- **Leans on:** A2 and sensitive capability not being fully resident in any one country.

---

## Step 4 — Deduped control portfolio

The 69 residues collapse to **22 controls**. Several are the same control wearing different names (the human-on-the-loop *interlock* covers S-02/S-18/S-65/S-67; the *in-country footprint* covers S-05/S-16/S-54; *multi-source+buffer* covers S-44/S-45/S-48). Shrinkage from 69 → 22 is the finding: a handful of controls carry most of the resilience.

| # | Control | Risks covered | Owner-role | Leans on (dependency / assumption) | Notes |
|---|---|---|---|---|---|
| C-01 | **Export/trade-compliance pre-clearance gate** (`manual_override_with_review` + `audit_log_immutability`) | S-01, S-05, S-07, S-49, (S-65) | Chief Compliance / Trade-Control Officer | A9; tamper-evident audit trail | The licence-to-operate keystone. Also the sanctions off-switch. |
| C-02 | **Human-on-the-loop autonomy interlock + kill-switch** (`feature_flag_kill_switch` + `event_sourcing_audit_trail`) | S-02, S-18, S-33, S-65, S-67, (S-68) | VP Autonomy / Safety Engineering | A2; autonomy architected as supervisable & interruptible | Carries the most existential-severity risks. Both a safety control and the evidence trail. |
| C-03 | **Provenance-backed rapid-response comms + crisis playbook** (`event_sourcing_audit_trail`) | S-18, S-36, S-37, S-63, (S-67) | Chief Communications Officer + Legal | Verifiable decision logs; standing comms capability | The counter to internet-speed reputational attacks incl. deepfakes. |
| C-04 | **Dual-basis / auditable cost accounting** (`per_minute_billing_path`) | S-03, S-56 | CFO | A6; finance systems carry both price and cost basis | Survives a regulatory pricing-model switch as config, not rebuild. |
| C-05 | **Build-vs-buy / insource optionality** | S-04, S-46 | Chief Strategy Officer | A3, A5; self-funded-R&D muscle | Blocked deal or captured vendor degrades to "slower, in-house." |
| C-06 | **In-country delivery & support footprint** (`local_autonomy` for national entities) | S-05, S-16, S-54, (S-69) | Head of International | A2; partner nation allows domestic delivery | Also the sovereign-risk vehicle (with C-19). |
| C-07 | **Per-jurisdiction privacy/sensor policy config** (`feature_flag_kill_switch`) | S-06 | Product / Legal | Software-configurable sensing on fielded units | Config push, not recall, when law changes. |
| C-08 | **Assurance-evidence pipeline** (`event_sourcing_audit_trail` + `shadow_traffic`) | S-08, S-21 | VP Test & Evaluation | Evidence generated as a by-product of dev | Feeds certification *and* catches poisoned models. |
| C-09 | **Lattice lock-in / vertical bundling / value-up-the-stack** | S-09, S-13, S-14, S-15 | Chief Product Officer | A7; hardware+software differentiation | The commercial moat; note weakening if A7 relaxes. |
| C-10 | **Portfolio / product-mix breadth** (`bulkhead`) | S-10, S-11, S-53, S-56, S-60, S-64, S-68 | CEO / Portfolio governance | A1, A3, A10; re-taskable base | Highest-load control after C-02; the diversification backbone. |
| C-11 | **Low-cost effector line (cost-curve match)** | S-12 | Chief Product Officer | A10; Arsenal mass-manufacture | Product decision, kept minimal via existing manufacturing. |
| C-12 | **Edge / local autonomy + degraded-mode** (`local_autonomy` + `read_only_degraded_mode` + `stale_data_marker`) | S-17, S-20, S-22, S-23, S-40 | VP Platform / Edge Engineering | Devices survive disconnection; read paths stale-tolerant | Also the denied-environment credibility proof. |
| C-13 | **Security foundation: immutable audit + dual-accept rotation + segmentation** (`audit_log_immutability` + `key_rotation_dual_accept` + `bulkhead`/`tenant_isolated_blast_radius`) | S-19, S-26, S-31, S-34, S-50 | CISO | A9; least-privilege & segmentation are real | Scopes and contains breaches; underpins accreditation. |
| C-14 | **Progressive rollout + design-review gates** (`progressive_rollout` + `feature_flag_kill_switch`) | S-22, S-28, S-33 | VP Engineering / Release | Fielded units support staged, reversible updates | Catches regressions before fleet-wide harm. |
| C-15 | **Key-person succession + distributed public bench** (`runbook_as_code` applied to leadership) | S-24, S-29, S-66 | Board / Chief People Officer | A8 relaxing gracefully | De-single-threads the founder-brand. |
| C-16 | **Knowledge-resilience + retention/ethics governance** (`runbook_as_code` + ethics board) | S-25, S-27, S-28, S-30 | Chief People Officer | A3, A5; leadership engages the ethics framework | Talent-advantage protection; ethics board covers walkout risk. |
| C-17 | **Anti-tamper + capability compartmentation** (`key_rotation_dual_accept` on-capture) | S-32, S-35, S-69 | VP Hardware Security | Hardware designed with capture as expected | Recovered/seized units yield little. |
| C-18 | **Insider-threat + automated deprovisioning** (continuous eval + `audit_log_immutability`) | S-26, S-34 | CISO / Security | A9; least-privilege enforced | Overlaps C-13; kept separate for the human-monitoring dimension. |
| C-19 | **Multi-source qualification + strategic buffer stock** (`dependency_freeze_window` + second-source) | S-35, S-44, S-45, S-46, S-47, S-48, S-49 | Chief Supply-Chain Officer | A4; alternate sources exist at volume; part-level provenance | Heaviest supply-chain-side control; also lot traceability for recalls. |
| C-20 | **Manufacturing/site resilience + surge-ramp playbook** (`runbook_as_code` + `backpressure` + multi-site) | S-38, S-39, S-42, S-43, S-51, S-52, S-54 | Head of Arsenal / Ops | A10; site redundancy & reservable supplier capacity | Re-taskability is the minimal enabler; ties to C-10. |
| C-21 | **Multi-modal logistics + range redundancy** (`bulkhead`) | S-41, S-43 | Head of Logistics | Alternate routes/ranges pre-cleared | Reroute vs. halt. |
| C-22 | **Treasury: cash-runway reserve + capital-structure & profitability optionality** (`read_only_degraded_mode` for the business) | S-58, S-59, S-62 | CFO / Board | A3; a profitable core to fall back to | Survives appropriations gaps and capital-market cold spells without cutting the core. |

Plus one lifecycle-hygiene control folded into ownership rather than a standalone row: **authorisation/lifecycle registry with expiry ownership** (S-57, S-61) — reuses `dependency_freeze_window` + `audit_log_immutability`; owner: Program Security / Product Lifecycle. Listed here so it is not orphaned. **Per-tenant isolation** (S-55) is folded into C-13's `bulkhead`/`tenant_isolated_blast_radius` at the Lattice layer (`per_tenant_quota` + `query_capacity_guard`).

---

## Step 5 — Contagion / systemic-risk analysis

### Shared-dependency map (the hidden couplings)

- **A2 "we are permitted to build/export lethal autonomy"** is the single most shared assumption. It underpins C-01, C-02, C-06, and the black-swan cluster S-02/S-08/S-37/S-65/S-68. If A2 breaks broadly, four controls degrade *at once* and the roadmap-level attractors converge.
- **A9 "compliance/security is maintained"** underpins C-01, C-13, C-18, and the lifecycle registry. A single catastrophic breach (S-01, S-26, S-31) can trip the licence-to-operate for *all* government business simultaneously — the debarment cascade.
- **A10 "Arsenal can scale/re-task"** underpins C-10, C-11, C-20. A physical hit to manufacturing (S-38/S-39/S-42) or a supply shock (via C-19's dependency) plus a mega-win (S-51) can collide: the scaling thesis and the diversification thesis lean on the *same* re-taskable base.
- **A7 "Lattice remains the integrating standard"** underpins C-09 and C-12's value narrative. Erosion (S-14) weakens both the moat and the migration of margin up-stack (S-15).
- **`event_sourcing_audit_trail` / decision-log verifiability** is a shared *component* under C-02, C-03, C-08. If those logs are ever shown to be incomplete or forgeable, the safety interlock's accountability, the crisis-comms rebuttal, and the certification evidence all lose credibility together.
- **A3/A5 capital + talent** jointly feed C-05, C-10, C-15, C-16, C-22. A capital winter (S-59) that also triggers talent flight (S-25) hits R&D velocity, diversification, and succession funding at once.

### Top cascade paths (plain sentences)

1. **The debarment cascade.** One catastrophic compliance/security failure (an ITAR breach S-01, an espionage arrest S-26, or an APT exfiltration S-31) trips A9 and, through C-01/C-13/C-18, freezes *every* government contract and export line simultaneously — the fastest path to extinction, and the reason these controls are the keystones.
2. **The permission collapse.** A single vivid autonomy-harm event (real S-18, faked S-63, or emergent S-67) feeds a policy/treaty reaction (S-02→S-65/S-68), breaking A2 and degrading C-01, C-02, and C-06 together while the crisis-comms control C-03 is racing the clock. Safety-interlock and comms lean on the *same* audit trail — if that trail is doubted, both fail at once.
3. **The manufacturing collision.** A mega-win (S-51) arrives while a physical hit (S-38/S-42) or a supply ban (S-45/S-48) constrains the *same* re-taskable Arsenal base (A10) that C-10, C-11, and C-20 all lean on — the diversification story and the scaling story fail in the same quarter.
4. **The capital-talent winter.** A funding cold spell (S-59) and a talent raid (S-25) co-occur (both lean on A3/A5), simultaneously slowing R&D (C-05), thinning the portfolio's renewal (C-10), and defunding succession/retention (C-15/C-16) — a slow but broad cascade.
5. **The single-customer squeeze.** DoD concentration (S-53) plus an appropriations gap (S-58) plus a program cancellation (S-60) all trace to the same monopsony dependency; C-10 and C-22 must both hold, and they lean on allied demand (A2) and patient capital (A3) respectively — if those relax together, diversification and runway fail in tandem.
6. **The supply-chain chokepoint.** Advanced compute, magnets, and Taiwan-node components (S-44/S-45/S-48/S-49) all concentrate on A4; C-19 is a single control carrying seven risks. If A4 breaks structurally (a genuine China/Taiwan rupture), C-19's buffers deplete and multiple hardware lines stop together.
7. **The provenance-trust break.** If decision/BOM logs are ever shown forgeable, C-02 (accountability), C-03 (rebuttal), C-08 (certification), and C-17/C-19 (provenance) all lose their evidentiary basis at once — a quiet but wide coupling through a shared component.

### Overloaded controls (carry too much)

- **C-02 (autonomy interlock)** and **C-10 (portfolio breadth)** carry the most existential-severity risks; **C-19 (multi-source+buffer)** carries the most supply risks; **C-20** the most physical/scale risks. These four are the load-bearing walls — invest disproportionately in their robustness and independence.

### Under-covered stressors (thin coverage — one control deep)

- **S-12 (cost-per-kill inversion)** rests solely on C-11; if the low-cost line isn't real, there is no fallback.
- **S-58/S-59/S-62 (cash/capital)** rest on C-22 alone — a single treasury control against three distinct capital shocks.
- **S-61 (product obsolescence)** rests on the lifecycle-registry/modularity discipline only.
- **S-64 (peace outbreak)** rests on dual-use pivot optionality (inside C-10) that is largely untested — the hardest black swan to pre-provision.

### Orphan controls (risk theatre check)

No pure orphans emerged — the dedupe was driven from live stressors. The closest to theatre is any *standalone* insider-threat tooling (C-18) that duplicates C-13 without adding the human-monitoring dimension; if C-18 ever becomes pure log-duplication, merge it into C-13. Flag: **`per_tenant_quota`/`query_capacity_guard`** exist only for S-55 — legitimate, but keep verifying that Lattice's multi-tenant load actually varies by orders of magnitude, or this control drifts toward theatre.

---

## Step 6 — Resilience regime verdict

**Regime: edge of chaos, leaning toward chaotic on two axes.**

Anduril's naive model is *structurally* well-suited to the edge: few, load-bearing, mostly loosely-coupled controls (22 covering 69 stressors), a re-taskable manufacturing base, a self-funded model that gives strategic optionality, and product breadth that contains most single-program failures. Failures in most categories stay contained — a lost program, a site fire, a poached team, a supply shock each have a real residue and don't cascade org-wide. That is the edge-of-chaos signature.

But two shared dependencies pull it toward **chaotic**: (1) **A9 (compliance/security)** and (2) **A2 (political permission for lethal autonomy)** each sit under a cluster of the highest-severity controls, so a single shock on either axis can trip multiple continuity controls *simultaneously* — the debarment cascade and the permission collapse. A chaotic regime's defining symptom — "one shared dependency shows up in half the coupling matrix" — is partly present here: A2 and A9 between them touch most of the existential-severity paths. It is not frozen (there is little evidence of over-controlled rigidity; if anything the risk is under-provisioned novelty coverage on capital and cost-curve axes).

### Concrete deltas to move toward the edge

1. **Decouple the two existential dependencies from single points of failure.** For A9: treat compliance and insider-threat as independent, redundantly-audited functions so no *single* breach can trip debarment across the whole book — segment government programs so one program's security event contains rather than cascades. For A2: architect *every* product to ship in a supervised/non-lethal configuration as a first-class mode (not an afterthought), so a permission shock degrades revenue rather than erasing the roadmap. This directly weakens cascade paths 1 and 2.
2. **Harden the shared audit-trail component (C-02/C-03/C-08) to be provably tamper-evident and independently verifiable.** Its credibility is a hidden single point of failure under three top controls plus the crisis-comms rebuttal; make its integrity un-disputable (hash-chained, externally anchored) so the provenance-trust break (cascade 7) cannot happen.
3. **Add depth to the two thinnest coverage zones — capital and cost-curve.** C-22 alone against three capital shocks and C-11 alone against cost-per-kill inversion are single-deep. Pre-provision a real low-cost-effector capability and a genuine throttle-to-profitability plan *before* they are needed, converting two brittle single-control zones into contained failures.

### Caveat (per playbook)

The NKP/criticality read is a **heuristic, not a Monte-Carlo simulation** — treat "edge, leaning chaotic on A2/A9" as a directional brittleness signal about *where the correlations concentrate*, not a predicted incident rate. Re-run this analysis on any trigger event: a change of administration or export-control regime, an M&A action, a major security incident, a big program win or loss, or a capital-market shift.

---

## Completeness pass — additional stressors

> A second-pass sweep against the same operating model and assumptions (A1–A10). Every card below is checked *distinct in mechanism* from S-01…S-69 — where a stressor is adjacent to an existing one, the card names the existing number and states the difference explicitly. Numbering continues from **S-70**. Same template: Stressor (business language, category, novelty 1–5), Attractor (do-nothing end-state), Residue (smallest surviving control; catalogue names in `code font`), Leans-on (assumption/dependency). These do **not** replace or renumber anything above.

### S-70 — Foreign investment triggers CFIUS/FOCI; clearances jeopardised
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A foreign limited partner or strategic investor's stake trips a CFIUS review or Foreign Ownership, Control or Influence (FOCI) finding; DCSA imposes a mitigation regime (proxy board / SSA) or, worst case, the facility security clearance is suspended — a licence-to-operate hit sourced from the *cap table*, not operations. (Distinct from S-04 antitrust-blocked M&A and S-59 down-round: this is inbound-capital ownership tripping national-security control, not an acquisition or a valuation event.)
- **Residue:** *Capital-provenance screening + FOCI-ready governance* — every investor is screened for beneficial ownership before the round closes, and the entity is pre-structured so a mitigation instrument (voting trust / proxy holders) can be dropped in without re-papering the clearance. Reuses `event_sourcing_audit_trail` on cap-table provenance and `manual_override_with_review` (a two-person gate on any allocation above a foreign-ownership threshold).
- **Leans on:** A3, A9 — that capital can be raised entirely from screened, clearable sources without starving the self-funded model.

### S-71 — GAO/COFC bid protest freezes a just-won award
- **Category:** Regulatory / legal · **Novelty:** 2
- **Attractor:** A losing incumbent files a Government Accountability Office (or Court of Federal Claims) protest on a program Anduril just won; an automatic stay freezes performance and revenue recognition for up to ~100+ days while the record is litigated — the win converts to a cash-timing and morale drag with a non-zero chance of a re-compete.
- **Residue:** *Protest-hardened proposal discipline* — bids are documented to a defensible evaluation record (traceable requirement-to-response mapping) so a protest is more likely denied on the merits, and program cash plans assume a stay window rather than being surprised by it. Reuses `event_sourcing_audit_trail` (the proposal decision record regulators/judges trust) and portfolio-breadth `bulkhead` (one frozen award can't stall the book).
- **Leans on:** A1, A6 — a pipeline wide enough that a single stayed award is absorbable.

### S-72 — Allied customer re-exports Anduril kit to an unauthorised third party
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** An allied government retransfers or diverts Anduril hardware/technical data to a third country outside the export authorisation; the US treats it as a retransfer violation, and Anduril — as the ITAR licensee — is dragged into the enforcement and the political blowback of "American autonomy showed up where it shouldn't." (Distinct from S-07 customer-sanctioned and S-37 war-crime use: here the *ally's own diversion* creates a US compliance and political exposure that lands on Anduril.)
- **Residue:** *End-use/retransfer covenants + phone-home attestation* — contracts bind the customer to authorised end-use and locations with audit rights, and fielded systems attest their operating region so an unauthorised relocation is detectable. Reuses `feature_flag_kill_switch` (a licence-contingent off-switch tied to authorised geography) and `event_sourcing_audit_trail` (provable notice + attestation trail for the voluntary-disclosure path).
- **Leans on:** A2, A9 — enforceable retransfer terms and location attestation that survive customer pushback.

### S-73 — DoD autonomous-weapons review (DoDD 3000.09 / Article 36) blocks a function
- **Category:** Regulatory / legal · **Novelty:** 4
- **Attractor:** The *existing* US legal-and-weapons review process — DoD Directive 3000.09 senior-review for autonomy, plus the Article 36 legal weapons review — rules a specific autonomous-engagement function non-compliant and refuses to authorise fielding, even though no new law or treaty changed. A capability Anduril built and priced is administratively un-fieldable. (Distinct from S-02 policy shift and S-65 treaty ban: this is the *current* review machinery saying "no" to a specific function, not a change in the rules.)
- **Residue:** *Review-ready autonomy dossier + supervised fallback mode* — every autonomous engagement path ships with the appropriateness/reliability/human-judgment evidence the 3000.09 review demands, and a certified human-on-the-loop mode (the S-02/S-18 interlock) so the product fields *supervised* while the autonomous mode is adjudicated. Reuses `feature_flag_kill_switch` + `event_sourcing_audit_trail`.
- **Leans on:** A2, and autonomy architected as a supervisable, evidence-generating mode from day one.

### S-74 — Primes lobby to re-lock procurement behind entry barriers
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** Incumbents win a quiet policy fight to raise non-price entry barriers — mandatory past-performance minimums, flight-hour/TRL thresholds, cost-realism scrutiny, or a swing back toward cost-plus preference on major programs — that structurally disadvantage a fast, fixed-price non-traditional. The speed-and-price advantage is regulated away at the *rulebook* level. (Distinct from S-03, which extends cost-accounting *audit* obligations; this raises *eligibility* barriers to compete at all.)
- **Residue:** *Track-record accretion + coalition advocacy* — deliberately bank qualifying past-performance and flight hours on smaller/adjacent programs so the barriers are cleared, and participate in the defense-innovation policy coalition that argues the other side. Reuses `event_sourcing_audit_trail` (the verifiable performance record that satisfies a past-performance gate). (bespoke on the advocacy side.)
- **Leans on:** A1 — a steady flow of programs on which to accrue the qualifying record.

### S-75 — False Claims Act (qui tam) suit over misrepresented capability/test results
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A current/former employee files a qui tam suit alleging Anduril overstated a product's tested capability or readiness in a proposal or milestone certification; the False Claims Act's treble damages plus the suspension/debarment overhang turn an aggressive-marketing culture into an existential legal exposure. (Distinct from S-01 export breach and S-27 ethics walkout: this is fraud-against-the-government litigation sourced from internal dissent about *technical honesty*.)
- **Residue:** *Claim-substantiation gate + internal-disclosure channel* — every capability claim in a government-facing document is traceable to test evidence before submission, and a real internal reporting channel gives a would-be relator a path short of a lawsuit. Reuses `manual_override_with_review` (two-person sign-off on capability assertions), `audit_log_immutability`, and the S-08 assurance-evidence pipeline.
- **Leans on:** A6, A9 — that claims are genuinely substantiated and dissent has an internal route.

### S-76 — Congress curtails OTAs / rapid-acquisition pathways
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** Other Transaction Authority, mid-tier acquisition, and commercial-solutions-opening vehicles — the fast lanes Anduril's speed thesis relies on — are curtailed or capped by Congress, forcing programs back onto slow FAR-based, protest-prone contracting. Time-to-contract, a core differentiator, degrades industry-wide against Anduril.
- **Residue:** *Multi-vehicle contracting fluency* — the capture organisation is qualified and rehearsed on FAR-based vehicles as well as OTAs, so a pathway closure reroutes contracts rather than stalling them. Reuses `bulkhead` (no single contracting vehicle is load-bearing) and `runbook_as_code` (the alternate-vehicle capture playbook is pre-scripted).
- **Leans on:** A1 — and a BD org that can win on the slow path when forced.

### S-77 — Government asserts technical-data / IP rights on a fixed-price program
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A customer demands government-purpose or unlimited technical-data rights (DFARS 252.227) to a fixed-price program's designs and interfaces to enable re-compete/second-sourcing; conceding erodes the proprietary Lattice/hardware lock-in the whole commercial model rests on, while refusing risks the award. (Distinct from S-14 DoD software-factory *competition*: this is a *contractual data-rights* attack on the moat, not a rival platform.)
- **Residue:** *Rights-segmented architecture + licensing posture* — the codebase and designs are segmented so a program can be delivered with clearly bounded, negotiated data rights while the crown-jewel autonomy/Lattice core stays proprietary and separately licensed. Reuses `bulkhead` (rights boundary as an isolation boundary) and `event_sourcing_audit_trail` (provable IP provenance to defend the rights assertion).
- **Leans on:** A7 — that value can be delivered without ceding the integrating core.

### S-78 — Spectrum reallocation strips bands the fleet depends on
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** The FCC/NTIA reallocates or auctions mid-band spectrum (e.g., to commercial 5G) that Anduril's datalinks, radars, and drone C2 rely on; fielded systems lose clean access to the frequencies they were designed around, degrading range and resilience across the installed base by regulatory fiat. (Distinct from S-20/S-33 adversarial jamming/spoofing: here it's *lawful* loss of spectrum access.)
- **Residue:** *Software-defined, multi-band radio + spectrum-agility* — the RF stack is frequency-agile and updatable so a reallocation is a re-tune, not a re-design; `progressive_rollout` + `feature_flag_kill_switch` push new band plans fleet-wide, and `local_autonomy` keeps units mission-capable through a comms re-tune.
- **Leans on:** A4 — and RF hardware genuinely re-tunable across bands in software.

### S-79 — Post-quantum crypto mandate (CNSA 2.0) the fielded fleet can't meet by deadline
- **Category:** Regulatory / legal · **Novelty:** 4
- **Attractor:** A mandated migration to post-quantum algorithms (NSA CNSA 2.0 timelines) sets a compliance deadline the deployed fleet's cryptography can't meet in place; non-compliant systems lose accreditation to operate on government networks, and any historically exfiltrated encrypted data is now "harvest-now-decrypt-later" exposed.
- **Residue:** *Crypto-agility + dual-accept algorithm rollover* — the fleet's cryptographic primitives are abstracted behind a swappable interface so a PQC migration is a config-plus-key event, executed with an old+new overlap window. Directly reuses `key_rotation_dual_accept` (algorithm rollover instead of key rollover) plus `progressive_rollout`.
- **Leans on:** A9 — crypto is agile and remotely upgradable within accreditation limits.

### S-80 — Product-liability tort from a US bystander harmed by a fielded/test system
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A US civilian is injured (or property destroyed) by a fielded border system or a test drone crash, and plaintiffs advance a novel autonomous-systems product-liability theory in civil court; discovery pierces proprietary design detail and a verdict sets an adverse precedent for the whole autonomy line. (Distinct from S-18 targeting error, which is a military/licence-to-operate incident; this is domestic civil tort.)
- **Residue:** *Safety-case documentation + liability-limiting contracting* — a maintained design-safety case and hazard log make the "reasonable care" defence provable, and government-contractor-defence positioning plus insurance (see S-103) bound the financial tail. Reuses `event_sourcing_audit_trail` (the incident-reconstruction record) and the S-18 engagement/authority logs.
- **Leans on:** Verifiable safety evidence and defensible contracting posture.

### S-81 — Patent-infringement or trade-secret injunction on autonomy/sensor-fusion IP
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** A competitor or a non-practising entity wins (or credibly threatens) an injunction alleging Anduril's autonomy or sensor-fusion infringes their IP; an injunction could bar shipment of a product line, and even a settlement imposes a royalty tax on the core stack. (Distinct from S-91 trade-secret suits *Anduril* faces over hiring: this is patent/IP infringement targeting the products themselves.)
- **Residue:** *Freedom-to-operate clearance + design-around optionality* — key features carry an FTO analysis and a pre-scoped non-infringing design-around, so an injunction degrades to a patch, not a shutdown. Reuses `feature_flag_kill_switch` (disable the contested path pending a design-around) and the S-04 build-vs-buy optionality muscle.
- **Leans on:** A5 — engineering depth to design around on demand.

### S-82 — Revenue-recognition / EAC restatement on long fixed-price contracts
- **Category:** Regulatory / legal · **Novelty:** 3
- **Attractor:** Percentage-of-completion accounting on multi-year fixed-price programs relies on estimates-at-completion; a cluster of cost overruns forces a downward EAC revision and a restatement, revealing a material weakness in controls right before an IPO or raise — the financial-credibility damage compounds the S-56 cash damage. (Distinct from S-56, which is the *economic* loss on a contract; this is the *accounting-controls* failure that surfaces it badly.)
- **Residue:** *Disciplined EAC governance + early-warning cost telemetry* — program cost-to-complete is re-forecast on a fixed cadence with independent review, so EAC drift is disclosed continuously rather than in a shock restatement. Reuses `event_sourcing_audit_trail` (the auditable cost history) and the S-03 dual-basis cost accounting.
- **Leans on:** A6 — cost/schedule estimates are tracked honestly and early.

### S-83 — Independent operational-test verdict (DOT&E) kills a program of record
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** The statutory Director of Operational Test & Evaluation reports a flagship "not operationally effective / not suitable"; the finding gives Congress and the customer cover to cut the program of record regardless of the fixed-price commercial win. (Distinct from S-20 embarrassing public trial and S-60 budget cancellation: this is the *formal statutory test authority's* verdict, the hardest to spin.)
- **Residue:** *Test-as-you-build + operational-representativeness* — capability is validated continuously against operationally-representative conditions (not just demos) so the formal OT verdict is de-risked before it happens. Reuses `shadow_traffic` (validate against real-representative load before it counts) and the S-08 assurance-evidence pipeline; portfolio-breadth `bulkhead` absorbs a single program loss.
- **Leans on:** A6, A10 — and OT-representative testing being designed-in.

### S-84 — Flagship competitive fly-off lost on technical merit (CCA / Fury)
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** A marquee down-select (e.g., a Collaborative Combat Aircraft / Fury increment) is lost to a prime on *technical* evaluation, not price; a program treated as a growth pillar and a capital-narrative centrepiece goes to a competitor, and the "we out-build the primes" thesis takes a public, on-the-merits dent. (Distinct from S-09 price-undercut and S-10 entrant-leapfrog: here Anduril loses a head-to-head evaluation of its own flagship.)
- **Residue:** *Portfolio breadth + fast-follow re-compete positioning* — no single fly-off is load-bearing (`bulkhead`), and the losing entrant is positioned (Lattice integration, subsystem supply, next-increment bid) to re-enter rather than exit the mission area. Reuses the S-14 open-interface play so Anduril's autonomy still rides inside the winner's aircraft.
- **Leans on:** A1, A7 — breadth to survive the loss and a software wedge back in.

### S-85 — Prime teaming coalition locks Anduril out of a program of record
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** Incumbents form an exclusive teaming arrangement — tying up the specialised suppliers, past-performance, and political support a major program needs — so Anduril is structurally excluded before the competition even runs. The barrier is *coalition*, not price or technology.
- **Residue:** *Counter-teaming + owned critical-path capability* — Anduril assembles its own coalition and, crucially, in-sources the critical subsystems a prime could otherwise lock up, so no competitor can fence off the inputs. Reuses the S-04/S-46 build-vs-buy insource optionality and `bulkhead` (no single teaming partner is decisive).
- **Leans on:** A5, A10 — depth to own the critical path rather than rent it.

### S-86 — NATO/coalition interoperability standard the products fail to certify against
- **Category:** Market / competitive · **Novelty:** 3
- **Attractor:** A NATO STANAG or coalition data-standard interoperability mandate becomes a hard gate for allied procurement, and Anduril's products (or Lattice's interfaces) aren't certified to it; allied sales are foreclosed on a *conformance* basis even where the capability is superior. (Distinct from S-14 open-interface competition and S-16 sovereign-build: this is failing a *standards certification* others meet.)
- **Residue:** *Standards-conformant interface layer + certification pipeline* — Lattice exposes STANAG-conformant adapters and maintains a standing conformance-test/certification process so a new mandate is a certification sprint, not a re-architecture. Reuses `local_autonomy` (products keep full value inside a coalition mesh) and the S-08 evidence pipeline for the conformance artefacts.
- **Leans on:** A7 — value survives conforming to someone else's integration standard.

### S-87 — A commercial AI-model provider's use policy bars military applications
- **Category:** Market / competitive · **Novelty:** 4
- **Attractor:** A foundation-model or commercial-AI vendor whose models Anduril uses for a capability (perception, planning, decision-support, or engineering tooling) tightens its acceptable-use policy to prohibit weapons/military applications, or is pressured to revoke access; a software dependency evaporates on *policy*, not price or export grounds. (Distinct from S-44 compute-allocation and S-49 chip-export: this is model *licensing/use-policy*, upstream of silicon.)
- **Residue:** *Model-portability + owned/open-weight fallback* — capabilities are abstracted behind a model-agnostic interface with a qualified open-weight or in-house-trained fallback, so a provider ban is a model swap, not a capability loss. Reuses the S-04 build-vs-buy optionality and `feature_flag_kill_switch` (cut over to the fallback model without redeploy).
- **Leans on:** A5 — the talent to train/host a substitute, and architecture that doesn't hard-wire one vendor's model.

### S-88 — Union organising drive at Arsenal manufacturing
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** A labour-organising campaign at high-rate Arsenal manufacturing succeeds; work rules, negotiated staffing, and strike risk introduce friction into the software-defined, rapidly re-taskable production model that depends on flexible reallocation of line labour. The manufacturing-agility differentiator meets structured labour.
- **Residue:** *Constructive labour relations + cross-trained flexible workforce* — proactively good pay/conditions and a cross-trained workforce so line re-tasking is a trained-skills matter rather than a contractual fight, with `runbook_as_code` line-transfer procedures that don't depend on any one crew. (bespoke — a people-ops posture, not a restructure.)
- **Leans on:** A10 — that manufacturing re-taskability survives negotiated work rules.

### S-89 — Immigration/visa restriction chokes the non-cleared AI talent pipeline
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** H-1B / visa tightening (or aggressive "US-person" export-control interpretations that create deemed-export friction) cuts off the immigrant engineering talent that the *non-cleared* autonomy/AI research pool leans on; the talent-advantage thesis (A5) is throttled at the border. (Distinct from S-25 poaching and S-30 clearance-staffing: this is the *inflow* of talent restricted by policy.)
- **Residue:** *Talent-geography optionality + deemed-export-clean research zones* — maintain research nodes and roles structured so non-US-person talent can contribute on non-controlled work without deemed-export exposure, and diversify hiring geographies. Reuses `bulkhead` (segregate ITAR-controlled work from open research so the talent pool isn't uniformly gated) and `audit_log_immutability` on access.
- **Leans on:** A5, A9 — a legally clean way to employ global talent on the open-research portion.

### S-90 — Culture drift toward cost-plus-prime bureaucracy
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** As Anduril wins programs of record and scales headcount, process, risk-aversion, and program-management overhead accrete until it behaves like the cost-plus primes it was built to disrupt; the speed-and-risk-appetite that *is* the differentiator quietly erodes — an internal attractor, no external shock required. (Distinct from S-28 hypergrowth quality-dilution: that's defect rate; this is *loss of the operating culture and speed edge*.)
- **Residue:** *Cycle-time as a tracked invariant + small-team autonomy* — treat decision/ship cycle-time as a first-class, dashboarded metric with an owner, and preserve small, empowered product teams so bureaucracy is *measured* and resisted rather than accreting invisibly. Reuses `charge_session_observability` (domain-event telemetry, here on internal decision-to-ship transitions) to make the drift visible. (bespoke governance.)
- **Leans on:** A8 — leadership actively defends the culture as the company scales.

### S-91 — Trade-secret / non-compete litigation over poached engineers
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** A prime or competitor sues Anduril alleging that engineers hired from them brought trade secrets or breached non-competes; discovery, injunctions on specific projects, and the chilling effect on aggressive hiring turn Anduril's talent-magnet strategy into legal exposure. (Distinct from S-25 the poaching *event* and S-81 patent infringement on products: this is misappropriation litigation arising from *inbound* hiring.)
- **Residue:** *Clean-hiring hygiene + provenance walls* — onboarding enforces no-import-of-prior-employer-materials, sensitive hires are walled from directly competing workstreams for a period, and design provenance is logged to prove independent development. Reuses `event_sourcing_audit_trail` (independent-development provenance) and `audit_log_immutability`.
- **Leans on:** A5, A9 — hiring hygiene that survives contact with a fast-growth talent grab.

### S-92 — Broad clearance suspensions/revocations across the cleared workforce
- **Category:** Human / organisational · **Novelty:** 3
- **Attractor:** A government-side adjudication slowdown, a continuous-evaluation policy tightening, or a breach of the security-clearance data system (SF-86-class) causes a *wave* of suspensions/revocations across Anduril's cleared staff at once; classified programs lose cleared bodies faster than they can be replaced. (Distinct from S-26 a single espionage arrest and S-30 not being able to *staff* new clearances: this is systemic loss of *existing* clearances.)
- **Residue:** *Cleared-bench depth + task-portability across cleared/uncleared work* — a ring-fenced spare of in-process and cross-program-cleared staff (`bulkhead` for people, per S-30) plus program work decomposed so uncleared engineering can progress the non-classified fraction during a shortfall.
- **Leans on:** A9 — clearance throughput and a genuine cleared reserve.

### S-93 — Operational ransomware/wiper halts Arsenal production
- **Category:** Adversarial / abuse · **Novelty:** 3
- **Attractor:** A ransomware or wiper attack locks the ERP / manufacturing-execution / PLM systems that run Arsenal; the harm is *availability*, not IP theft — production and shipment stop, milestones slip, and fixed-price cash timing bites, even though no crown-jewel data left the building. (Distinct from S-19 source exfiltration and S-31 APT espionage, which are confidentiality events.)
- **Residue:** *Segmented OT/IT + tested offline restore* — manufacturing operational-technology is segmented from IT (`bulkhead` / `tenant_isolated_blast_radius`), and immutable, tested backups plus a rehearsed restore runbook bound downtime to hours. Reuses `runbook_as_code` (the restore is pre-scripted) and `audit_log_immutability` for scoping.
- **Leans on:** A10 — that production can ride a restore window on segmented, backed-up systems.

### S-94 — New hyperscale factory can't be energised on schedule (grid interconnection)
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** A new high-rate manufacturing megasite (Arsenal-1 class) hits a grid-interconnection queue, a substation lead-time, or a regional power shortfall and cannot draw the megawatts it needs on schedule; the capacity the scaling thesis (and any mega-win, S-51) depends on sits idle for want of power. (Distinct from S-42, which is a *grid-failure outage* of an existing site; this is *initial energisation* of new capacity.)
- **Residue:** *Phased-power siting + on-site generation bridge* — site selection prioritises power availability and interconnection status, and a phased on-site generation/storage bridge lets initial lines run while the grid tie completes. Reuses `runbook_as_code` (the energisation-and-ramp plan is pre-sequenced) and `backpressure` (sequence the ramp to available power).
- **Leans on:** A10 — capacity plans that treat power procurement as a first-class critical path.

### S-95 — Environmental / zoning / permitting blocks a new manufacturing megasite
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** Environmental review, zoning, water/air permits, or organised community opposition delays or blocks a planned megasite; the physical footprint the manufacturing-scale narrative promised investors and customers slips by quarters, decoupling capacity from committed demand.
- **Residue:** *Multi-site optionality + permitting-de-risked siting* — more than one candidate site is advanced in parallel with permitting status as a gating criterion, so a blocked site reroutes to an alternate rather than restarting. Reuses `bulkhead` (no single site is load-bearing) and the S-38/S-42 multi-site re-taskability family.
- **Leans on:** A10 — a siting strategy carrying real optionality, not a single bet.

### S-96 — Fatal industrial or test accident triggers OSHA/criminal exposure and stand-down
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** A worker fatality on a manufacturing line, an energetics/propulsion mishap, or a test-drone crash causing death/injury triggers an OSHA (and possibly criminal-negligence) investigation and a safety stand-down; production and testing halt, and the "move fast" culture is scrutinised as reckless. (Distinct from S-43, which is *losing access* to a range; this is a *casualty event* on-site or on-range.)
- **Residue:** *Safety-management system + range/line safety interlocks* — a documented safety-management system with hard physical interlocks, exclusion zones, and a maintained hazard log bounds both the harm and the liability, and makes a fast, credible return-to-operations case. Reuses `manual_override_with_review` (two-person authority on hazardous operations) and `event_sourcing_audit_trail` (the safety-decision record).
- **Leans on:** A10 — that speed is compatible with a real safety-management system.

### S-97 — Legacy energetics / environmental-remediation liability surfaces
- **Category:** Physical / environmental · **Novelty:** 3
- **Attractor:** Manufacturing and testing of munitions/energetics and use of persistent chemicals (PFAS-class) accrue environmental-remediation and toxic-tort liabilities that surface as regulatory orders or lawsuits; a defense-manufacturing balance-sheet tail the fast-growth narrative didn't price appears. (Distinct from S-96 acute accident: this is chronic contamination/remediation liability.)
- **Residue:** *Designed-out hazardous processes + reserved remediation provision* — prefer lower-liability materials/processes where feasible and carry an accounting provision and monitoring program so a surfacing liability is funded and disclosed, not a shock. Reuses `event_sourcing_audit_trail` (material-use and disposal provenance) and the S-58 treasury-reserve discipline.
- **Leans on:** A4 — availability of lower-liability process alternatives.

### S-98 — Solid-rocket-motor / specialised propulsion supply controlled by a prime
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** Interceptors and effectors need solid rocket motors (or other specialised propulsion) whose US supply is concentrated in a handful of prime-owned producers; a competitor controlling the motor supply can gate or deprioritise Anduril's production of an entire product line. (Distinct from S-46 generic vendor-acquired-by-prime: this is a *structural industry chokepoint* on a specific critical subsystem.)
- **Residue:** *Propulsion second-source + in-house/insource option* — qualify an alternate motor source and hold the design/right to insource propulsion for critical effectors, so a single supplier's priority decision degrades to "slower/in-house," not "line stopped." Reuses the S-04/S-46 build-vs-buy insource optionality and `dependency_freeze_window` buffer thinking.
- **Leans on:** A4, A10 — that an alternate or insourced propulsion path is achievable.

### S-99 — Rad-hard / space-qualified microelectronics scarcity gates the space line
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** The space / on-orbit product ambitions depend on radiation-hardened, space-qualified microelectronics from a thin specialist supplier base with long lead times; a shortage or allocation cut gates the entire space line independent of the commodity-compute supply. (Distinct from S-44 commodity GPU/edge-AI allocation: rad-hard/space-qual is a separate, thinner market.)
- **Residue:** *Rad-tolerant COTS design + qualified second source + buffer* — architect for radiation-tolerant commercial parts with redundancy where mission allows, plus a qualified alternate rad-hard source and strategic buffer for the parts that must be space-grade. Same *multi-source + buffer* residue family as S-44/S-45/S-48.
- **Leans on:** A4 — that a rad-tolerant design path and an alternate source exist at volume.

### S-100 — Counterfeit / substandard parts escape into the delivered fleet
- **Category:** Supply chain / vendor · **Novelty:** 3
- **Attractor:** Counterfeit or substandard commercial components (relabelled chips, out-of-spec parts) enter the supply chain and reach delivered systems; a GIDEP-class alert forces fleet-wide inspection and rework, and field failures traced to the parts damage the reliability reputation that justifies fixed-price risk-taking. (Distinct from S-35 malicious hardware *implant*: this is fraud/quality escape, not a nation-state implant.)
- **Residue:** *Authorised-distributor sourcing + incoming-inspection + lot traceability* — buy critical parts through authorised channels, sample-test incoming lots, and keep lot-level BOM provenance so only affected units are recalled. Reuses `event_sourcing_audit_trail` (lot-level BOM trail, per S-35/S-47) and the S-47 batch-traceability/rotation pattern.
- **Leans on:** A4 — part-level provenance and authorised sourcing actually enforced.

### S-101 — Sustainment / fixed-price warranty tail outgrows the support economics
- **Category:** Scale / load · **Novelty:** 3
- **Attractor:** As the installed base compounds, fixed-price warranty and sustainment obligations accumulate into a long-tail liability; Anduril, carrying the risk it took to win on price, finds the cost of keeping years of fielded systems running eating the margin the up-front sales earned. (Distinct from S-54 support-org *capacity* strain and S-56 a single loss-making contract: this is the *aggregate warranty/sustainment liability* growing with the fleet.)
- **Residue:** *Priced sustainment model + reliability-driven design + warranty reserve* — sustainment is a priced, contracted revenue line (not a giveaway), designs target field-reliability to cap the tail, and a warranty reserve funds the accrued obligation. Reuses `per_minute_billing_path` thinking (sustainment as a first-class billed dimension) and `event_sourcing_audit_trail` (fielded-reliability telemetry that prices the reserve).
- **Leans on:** A6, A7 — that sustainment can be priced and reliability designed-in.

### S-102 — Factory-scale debt hits a covenant breach or refinancing wall
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** Debt raised to fund megasite construction and inventory hits a covenant breach (leverage/liquidity ratio) or a refinancing wall in a higher-rate market; lenders gain leverage over strategy at the moment capital is most needed, independent of the equity market. (Distinct from S-59 equity down-round and S-58 shutdown cash-timing: this is *leverage/credit* risk.)
- **Residue:** *Conservative covenant headroom + laddered maturities* — deliberately hold covenant headroom and stagger debt maturities so no single refinancing date is existential, and pair growth debt with the S-59 throttle-to-profitability optionality. Reuses `read_only_degraded_mode` (business version — shed growth spend to protect covenants) and the S-58 treasury-reserve discipline.
- **Leans on:** A3 — access to credit on non-punitive terms and disciplined leverage.

### S-103 — Product-liability / D&O insurance withdraws or excludes autonomous weapons
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** Insurers add autonomous-weapon or lethal-AI exclusions, or price product-liability and directors-and-officers coverage out of reach; a rising claims/political-risk environment makes the risk-transfer the whole fixed-price, liability-carrying model relies on unaffordable or unavailable. (Distinct from S-80 the *tort* itself: this is the *insurability* of the business model.)
- **Residue:** *Layered risk-financing + captive insurance + contractual liability caps* — diversify insurers, stand up a captive to self-insure the layer the market won't take, and cap liability contractually and via the government-contractor defence. (bespoke — a risk-financing structure.) Reuses the S-80 safety-case evidence to keep the insurable-risk story credible to underwriters.
- **Leans on:** A3 — capital to self-insure the uninsurable layer, and a defensible safety record.

### S-104 — Border-policy reversal defunds the flagship CBP program
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** A political reversal on border enforcement (administration change or appropriations fight) defunds or cancels the CBP Sentry-tower program specifically — an SBInet-style unwind — erasing a deployed-revenue pillar and a flagship reference customer on *domestic-politics* grounds. (Distinct from S-06 privacy-law restriction and S-60 generic milestone cancellation: this is a *border-policy demand collapse* on a named program.)
- **Residue:** *Product-mix + adjacent-mission redeployment* — the same towers/autonomy redeploy to force protection, critical-infrastructure, and allied border missions, so a US-border policy reversal shifts demand rather than destroying it. Reuses portfolio-breadth `bulkhead` and the S-64 dual-use pivot optionality.
- **Leans on:** A1 — adjacent missions exist to absorb the redeployed capability.

### S-105 — Association with domestic immigration enforcement becomes a recruiting/reputation liability
- **Category:** Time / lifecycle · **Novelty:** 3
- **Attractor:** Public backlash to aggressive domestic immigration enforcement makes Anduril's visible role at the border a recruiting, ESG-investor, and brand liability — distinct from any lethal-autonomy concern — narrowing the talent pool and inviting activist and customer pressure. (Distinct from S-27 lethal-AI ethics walkout and S-104 the *funding* of the program: this is *reputational/talent* fallout from the border association.)
- **Residue:** *Mission-framing + values-explicit recruiting + program transparency* — frame and communicate the humanitarian/interdiction dimensions honestly, recruit on explicit values so candidates self-select, and be transparent about what the systems do and don't do. Reuses the S-27 values-explicit hiring + ethics-review residue and the S-36 provenance-backed comms capability.
- **Leans on:** A5 — a talent pool that engages the mission on its stated terms.

### Additional black swans (novelty 5)

### S-106 — Silicon-level root-of-trust flaw/backdoor found across the entire autonomy fleet
- **Category:** Adversarial / abuse (black swan) · **Novelty:** 5
- **Attractor:** A foundational hardware vulnerability or covert backdoor is discovered in the AI/compute silicon common to Anduril's products — not one implant (S-35) but a *class-wide* root-of-trust break; every fielded autonomous system is simultaneously suspect and potentially remotely compromisable, and customers ground the whole fleet at once.
- **Residue:** *Defence-in-depth beyond the silicon root + heterogeneous compute + rapid attestation* — security doesn't rest solely on one silicon root-of-trust; a second, diverse compute source (per S-44) limits monoculture, and remote attestation plus the S-32 zeroization/anti-tamper posture let compromised units be identified and neutralised. Reuses `key_rotation_dual_accept` and `feature_flag_kill_switch` (disable the affected trust path fleet-wide).
- **Leans on:** A4 — genuine compute heterogeneity so one silicon flaw isn't universal.

### S-107 — Fielded autonomy is mass-hijacked and turned on friendly forces
- **Category:** Adversarial / abuse (black swan) · **Novelty:** 5
- **Attractor:** An adversary discovers how to commandeer — not merely blind (S-33) or reverse-engineer (S-32) — Anduril's fielded autonomous systems *at scale*, redirecting them against the forces operating them; the products become a weapon turned on their own users, an event that could end the company's licence to operate overnight.
- **Residue:** *Cryptographic command-authentication + bounded-autonomy envelope + hard kill-switch* — every command path is cryptographically authenticated (no valid authenticator, no action), autonomous behaviour is constrained to a tested envelope, and an independent hard kill/self-safe path defeats a hijack. Reuses the S-18/S-67 bounded-autonomy interlock, `key_rotation_dual_accept`, and `feature_flag_kill_switch`.
- **Leans on:** A2 — and command authentication + autonomy bounding being genuinely un-bypassable.

### S-108 — A counter-autonomy breakthrough makes small autonomous systems categorically obsolete
- **Category:** Market / competitive (black swan) · **Novelty:** 5
- **Attractor:** A physics-level defensive breakthrough — cheap ubiquitous directed-energy, a scalable EW/RF-domination technology, or an equivalent — makes small autonomous air/ground systems categorically defeatable overnight, collapsing the value of an entire product category regardless of Anduril's software edge. (Distinct from S-12 cost-per-kill inversion, which is an *economic* shift; this is a *categorical technical* obsolescence.)
- **Residue:** *Domain-diversified portfolio + capability-not-platform positioning* — value is spread across domains (undersea, space, C2, sensing) and framed as autonomy/integration capability rather than any single vulnerable platform, so a category-killing counter shifts the portfolio's centre of gravity rather than ending it. Reuses portfolio-breadth `bulkhead` and the S-64 dual-use/adjacent-domain pivot optionality.
- **Leans on:** A1, A10 — genuine cross-domain breadth and a re-taskable base to pivot into surviving categories.

---

**Completeness-pass count: 39 new stressors (S-70 … S-108).** Running total across both passes: **108 stressors** (S-01…S-108). Category spread of the new set: Regulatory/legal ×13 (S-70–S-82), Market/competitive ×5 (S-83–S-87), Human/organisational ×5 (S-88–S-92), Adversarial/abuse ×1 (S-93), Physical/environmental ×4 (S-94–S-97), Supply chain/vendor ×3 (S-98–S-100), Scale/load ×1 (S-101), Time/lifecycle ×4 (S-102–S-105), plus 3 new black swans (S-106–S-108).

Most new residues fold into the **existing** deduped portfolio (C-01…C-22) rather than adding controls — e.g. the export/compliance keystone C-01 now also carries S-70/S-72; the autonomy interlock C-02 carries S-73/S-107; build-vs-buy optionality C-05 carries S-81/S-85/S-87/S-98; portfolio breadth C-10 carries S-84/S-104/S-108; treasury/capital C-22 carries S-102/S-103. A handful surface genuinely *new* control surfaces worth adding to the portfolio on a re-run: **crypto-agility / algorithm rollover** (S-79, reusing `key_rotation_dual_accept`), **OT/IT segmentation + tested offline restore** (S-93), **power-first siting + on-site generation bridge** (S-94), **priced-sustainment + warranty reserve** (S-101), and **risk-financing / captive insurance** (S-103). None disturbs the Step 6 verdict: the two existential shared dependencies remain **A9 (compliance/security)** — now further loaded by S-70/S-75/S-92/S-93 — and **A2 (permission for lethal autonomy)** — now further loaded by S-73/S-107.
