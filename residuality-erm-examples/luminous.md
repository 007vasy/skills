# Residuality Theory — Enterprise-Risk Analysis: Luminous

*Method: Barry O'Reilly's Residuality Theory, adapted to enterprise risk per `residuality-enterprise-risk-management.md`. This is a stress-first analysis, not a conventional risk register. Attractors and stressors are in business language; mechanism detail lives in the residue. Catalogue controls referenced by `id` from `residuality/references/residue_library.md`.*

*Company: Luminous — a hardware/robotics startup automating the **field installation of PV modules at utility-scale (ground-mount) solar farms** using robotic arms / autonomous machines that pick, place, and fasten heavy panels onto racking. Sells into / partners with **solar EPCs and utility-scale developers**. Operates in the **United States and Australia**.*

*Analysis date: 2026-07-05. Re-run cadence: quarterly, plus on trigger (see §7).*

---

## 1. Naive operating model

**What Luminous is, described as built — no mitigation theatre.**

### Value chain (where money and machines flow)

```
Robotics R&D + hardware engineering (motion planning, perception, gripper, chassis)
   → Machine build (contract-manufactured actuators, reducers, edge-AI compute, sensors, batteries, chassis)
      → Fleet staged + trucked to remote utility-scale solar construction sites (US SW, TX, Australia outback)
         → On-site: robots pick heavy PV modules, place + fasten to racking / single-axis trackers
            → Sold/rented to EPCs & developers as install-as-a-service (per-watt / per-module) or machine lease
               → Ongoing revenue: throughput fees, service contracts, software, fleet uptime
```

The business only earns when three external things line up at once: **a funded utility-scale project exists**, **panels have physically arrived at the site**, and **the machines can operate in that site's conditions**. Break any one and the machine sits idle earning nothing.

### Core functions that keep the flow alive
- Robotics R&D: motion planning, perception/vision AI, gripper design, autonomous navigation over unimproved ground.
- Machine manufacturing and integration (heavily component-dependent — actuators, reducers, compute, sensors, batteries).
- Fleet logistics: staging, trucking, and recovering machines to/from remote sites.
- On-site deployment and operation: supervising operators, safety envelope around live crews.
- Field service and spare parts on remote sites (the machines break where nobody is).
- Commercial: selling per-watt economics to EPCs and developers against a manual-labor baseline.
- Regulatory/compliance interface: tax-credit eligibility, domestic-content, prevailing-wage, jobsite safety, robotics certification.

### Critical dependencies

**Internal**
- The motion-planning + perception stack and the small team that understands it — the core IP and a key-person concentration.
- The gripper/handling system's fit to the module formats and racking/tracker designs actually in the field.
- A capital-intensive balance sheet: machines cost cash to build before they earn, so runway is load-bearing.
- Fleet uptime: revenue is throughput, so a stalled machine is pure burn.

**External**
- **Solar project pipeline** — a downstream function of interest rates, tax-credit policy (US IRA ITC/PTC, domestic-content bonus; Australia LRET/grid-connection), and developer capex appetite.
- **PV module supply** — panels largely from China/SE Asia, exposed to tariffs, anti-dumping duties, and UFLPA forced-labor import bans. No panels on site = no work.
- **Robotics hardware supply** — actuators, precision reducers, edge-AI compute/GPUs, sensors (LIDAR/cameras), batteries. Several are concentrated or sole-source.
- **EPC / developer customers** — likely concentrated in a handful of large firms; each is a big share of revenue.
- **Skilled field labor** — operators to supervise and technicians to repair, both scarce in remote geographies.
- **Regulators & organized labor** — OSHA, robotics-safety standards, prevailing-wage/Davis-Bacon, project-labor agreements, unions.

### Load-bearing assumptions (stated out loud)
1. Utility-scale ground-mount solar keeps getting built at volume in the US and Australia.
2. Tax credits and policy (ITC/PTC, domestic-content, Australian renewable targets) stay supportive on a multi-year horizon.
3. Field labor is expensive and scarce enough that automation beats a manual crew on landed cost per watt.
4. Panels physically arrive at sites on schedule — import policy does not strand the pipeline.
5. Module formats and racking/tracker designs are stable enough that one gripper/handling system fits most of the market.
6. The machines actually hit their promised real-world throughput at utility scale, not just in demos.
7. Critical robotics components remain sourceable at acceptable cost and lead time.
8. Automating construction labor does not trigger disqualifying union/prevailing-wage/political resistance.
9. The company can raise the next capital round before runway runs out.
10. A worker is never seriously harmed by a machine on a live site.

---

## 2. Exhaustive stressor set

64 stressors across all 9 categories, multiple passes each. Novelty 1 (on some register somewhere) → 5 (would not appear in any standard risk register). Black swans (novelty 5) marked ★.

| # | Stressor (one concrete sentence) | Category | Novelty |
|---|---|---|---|
| S-01 | Congress repeals or accelerates the phase-out of the solar ITC/PTC and the utility-scale project pipeline Luminous installs into dries up within a year. | Regulatory/legal | 2 |
| S-02 | The IRA domestic-content bonus rules are read to exclude Luminous's foreign-made actuators and compute, so projects that use its machines lose the bonus credit and drop the machines to keep it. | Regulatory/legal | 4 |
| S-03 | Prevailing-wage / Davis-Bacon rules attached to subsidized projects are interpreted so that robot-installed modules don't count toward required labor hours, making automation a compliance liability on funded jobs. | Regulatory/legal | 4 |
| S-04 | A forced-labor import ban (UFLPA-style) seizes a wave of panels at port, freezing the projects — and there is nothing for the machines to install. | Regulatory/legal | 3 |
| S-05 | New anti-dumping / tariff duties spike imported-module prices, developers pause builds, and the installation pipeline contracts across a construction season. | Regulatory/legal | 2 |
| S-06 | OSHA (or an Australian equivalent) issues an emergency rule requiring certified human exclusion zones and oversight for autonomous heavy machinery on active jobsites, effective in 60 days. | Regulatory/legal | 3 |
| S-07 | A functional-safety certification (ISO-class) becomes mandatory before autonomous machines may operate near workers, and Luminous's fleet cannot be certified in time. | Regulatory/legal | 3 |
| S-08 | A project-labor agreement on a large federally funded solar project contractually mandates union field labor, excluding Luminous's machines from the job entirely. | Regulatory/legal | 3 |
| S-09 | Australia reforms grid-connection queues / marginal-loss-factor treatment and a cohort of utility-scale projects is cancelled, halving Luminous's addressable pipeline in-country. | Regulatory/legal | 3 |
| S-10 | A Buy-America / domestic-manufacturing provision on infrastructure funding requires domestically built equipment, disqualifying Luminous's imported-component machines from the biggest projects. | Regulatory/legal | 3 |
| S-11 | An established construction-equipment OEM ships a competing panel-installation robot at a materially lower price and bundles it with existing dealer/service networks. | Market/competitive | 3 |
| S-12 | A large EPC customer builds the installation automation in-house and stops buying from Luminous, taking its know-how with it. | Market/competitive | 3 |
| S-13 | An interest-rate and capex cycle turns and developers pause utility-scale solar builds for multiple quarters, collapsing demand for installation at any price. | Market/competitive | 2 |
| S-14 | Panel prices crash so far that field labor becomes a small fraction of project cost, and the per-watt ROI case for paying for automation evaporates. | Market/competitive | 3 |
| S-15 | A recession or immigration surge collapses field-labor cost, and a manual crew is suddenly cheaper than renting Luminous's machines. | Market/competitive | 3 |
| S-16 | Luminous's single largest EPC customer, a majority of revenue, does not renew and switches back to manual crews or to a rival. | Market/competitive | 2 |
| S-17 | The dominant tracker/racking vendor co-designs an install-optimised system with a competing robot, and its new standard is incompatible with Luminous's gripper. | Market/competitive | 4 |
| S-18 | Developer capex shifts from ground-mount toward rooftop, C&I, or storage-only projects, structurally shrinking the ground-mount installation market Luminous is built for. | Market/competitive | 3 |
| S-19 | A well-funded install-as-a-service startup undercuts Luminous's per-watt price to win logos and reset the market's price expectation below Luminous's unit economics. | Market/competitive | 3 |
| S-20 | Robot-installed modules are found months later to have micro-cracks from handling stress, and a wave of warranty and performance-degradation claims lands across delivered sites. | Technical/infrastructure | 4 |
| S-21 | The market moves to a larger, heavier next-generation module format and Luminous's machines cannot pick or fasten it without a redesign. | Technical/infrastructure | 3 |
| S-22 | A fleet-wide software update introduces a placement/torque error that ships to every deployed machine at once, damaging panels or racking across multiple live sites. | Technical/infrastructure | 3 |
| S-23 | The central fleet-telemetry / remote-control backend suffers a prolonged outage and machines on remote sites go idle with no way to dispatch or supervise them. | Technical/infrastructure | 3 |
| S-24 | A regional GPS/RTK positioning outage or drift stalls the machines that depend on centimetre-accurate placement, halting install across affected sites. | Technical/infrastructure | 3 |
| S-25 | At true utility scale (thousands of modules a day) the fleet's real-world throughput falls well short of the per-watt economics sold in demos, and the value proposition fails to close. | Technical/infrastructure | 4 |
| S-26 | The perception AI fails on a novel site condition — low-angle glare, red mud, heavy dust — and machines start mis-picking or dropping panels until it is retrained. | Technical/infrastructure | 3 |
| S-27 | The lead who owns the motion-planning / perception stack resigns with two weeks' notice and takes the tacit knowledge of why it works with them. | Human/organisational | 3 |
| S-28 | Field-service technicians who repair machines on remote sites are unhireable at scale and quit, so broken machines sit idle for days waiting on someone who can fix them. | Human/organisational | 3 |
| S-29 | A field worker is seriously injured or killed by a Luminous machine on a live construction site. | Human/organisational | 4 |
| S-30 | The supply of trained operators to supervise the machines cannot keep pace with deployments, capping how many sites Luminous can serve regardless of demand. | Human/organisational | 3 |
| S-31 | A rival robotics lab or a big-tech automation group poaches Luminous's core hardware and controls engineering team in a single hiring raid. | Human/organisational | 3 |
| S-32 | Machines and staged panels are stolen or vandalised on a remote, unsecured overnight site. | Adversarial/abuse | 2 |
| S-33 | Anti-automation activists or aggrieved labor groups physically target and sabotage machines on sites to make automation look unsafe and unwelcome. | Adversarial/abuse | 4 |
| S-34 | A viral video of a Luminous machine dropping or crushing a panel — or a near-miss with a worker — spreads regardless of the underlying facts. | Adversarial/abuse | 3 |
| S-35 | Ransomware locks the fleet-management platform and the whole deployed fleet is un-dispatchable until it is paid or rebuilt. | Adversarial/abuse | 3 |
| S-36 | An overseas rival reverse-engineers a captured or leaked machine and ships a low-cost clone, collapsing Luminous's technical lead. | Adversarial/abuse | 3 |
| S-37 | A security researcher (or attacker) demonstrates remote hijack and bricking of the machines at scale, and the proof-of-concept circulates publicly. | Adversarial/abuse | 4 |
| S-38 | A multi-week extreme-heat event across the US Southwest or the Australian interior forces machines and crews to stop, and the season's install window is lost. | Physical/environmental | 3 |
| S-39 | A dust storm or post-rain mud makes a site impassable to the machines' chassis, stranding a deployment mid-project. | Physical/environmental | 3 |
| S-40 | A wildfire or flash flood destroys a fleet of machines staged on or near a remote construction site. | Physical/environmental | 3 |
| S-41 | A contracted site turns out to have terrain — rock, slope, soft ground — the machines cannot traverse or work on, stranding the deployment and the contract. | Physical/environmental | 3 |
| S-42 | Washed-out or seasonal roads to a remote site cut off machine recovery and spare-parts delivery for weeks. | Physical/environmental | 2 |
| S-43 | A sole-source precision-actuator / harmonic-reducer supplier raises price steeply or cuts Luminous's allocation, throttling machine production. | Supply-chain/vendor | 3 |
| S-44 | An edge-AI compute / GPU shortage stalls machine builds and Luminous cannot field enough units to meet the season's contracts. | Supply-chain/vendor | 2 |
| S-45 | A battery-cell supply constraint (allocation or price spike) delays or raises the cost of every new machine. | Supply-chain/vendor | 2 |
| S-46 | Panels are held indefinitely at port under an import ban and, with the machines idle and ready, Luminous has capacity but nothing to install. | Supply-chain/vendor | 3 |
| S-47 | A critical robotics-component supplier is acquired by a competitor or by a firm that deprioritises Luminous's orders. | Supply-chain/vendor | 3 |
| S-48 | Luminous's contract manufacturer suffers a quality escape or insolvency, and machines ship with a latent defect or stop shipping altogether. | Supply-chain/vendor | 3 |
| S-49 | A single gigawatt-scale project demands ten times the fleet Luminous owns on a fixed construction schedule, straining every logistics, service, and staffing process built for smaller jobs. | Scale/load | 3 |
| S-50 | Rapid multi-site expansion outruns spare-parts and field-service logistics, and fleet uptime collapses across all sites at once. | Scale/load | 3 |
| S-51 | The whole industry's construction season concentrates demand into the same few months and every customer wants machines simultaneously, far exceeding fleet capacity. | Scale/load | 3 |
| S-52 | One customer grows to dominate Luminous's schedule and dictates pricing and priority, and every shared process bends around that one account. | Scale/load | 2 |
| S-53 | A flagship "pilot" deployment runs for years generating goodwill but never converts to a paid, scaled commercial contract, and the reference logo never becomes revenue. | Time/lifecycle | 3 |
| S-54 | The first-generation fleet ages and refurbishment / replacement capex balloons before the machines have paid back their build cost. | Time/lifecycle | 3 |
| S-55 | A tax-credit safe-harbour deadline pulls a wave of projects forward into one year, then a demand cliff follows once the deadline passes. | Time/lifecycle | 3 |
| S-56 | The next funding round has to close in a frozen climate-hardware VC market and Luminous's capital-intensive burn runs the runway down before unit economics are proven. | Time/lifecycle | 3 |
| S-57 | Early-fleet warranty and service obligations mature into a larger-than-reserved liability as the first machines accumulate field hours. | Time/lifecycle | 3 |
| S-58 ★ | A national TV investigation alleges — true or not — that a Luminous machine caused a worker's death or a jobsite fire, and viral panic makes EPCs suspend the machines regardless of the facts. | Human/organisational | 5 |
| S-59 ★ | Overnight, a total US–China solar-module decoupling (mutual bans) strands the entire US utility-solar module pipeline, and there are no panels to install anywhere in Luminous's largest market. | Regulatory/legal | 5 |
| S-60 ★ | A competitor demonstrates a fully autonomous end-to-end solar-farm build — piles, racking, and panels in one integrated system — making Luminous's single-step panel-install robot look obsolete overnight. | Market/competitive | 5 |
| S-61 ★ | A landmark court ruling assigns open-ended manufacturer liability for autonomous-machine jobsite injuries, and product-liability insurance for the fleet becomes unaffordable or unavailable. | Regulatory/legal | 5 |
| S-62 ★ | A public backlash blames grid instability or land-use harm on utility-scale solar and a wave of moratoria freezes new ground-mount approvals, collapsing the market Luminous installs into. | Regulatory/legal | 5 |
| S-63 ★ | An AI-generated deepfake or coordinated hoax showing a machine "going rogue" on a crew floods social media and customer inboxes, triggering contract suspensions before it can be debunked. | Adversarial/abuse | 5 |
| S-64 ★ | A geopolitical rupture closes Luminous's Australian operations overnight (trade or market-access shock), stranding machines, staff, and a whole regional pipeline. | Regulatory/legal | 5 |

**Diversity check:** 9/9 categories populated; per-category counts — Regulatory/legal 14, Market/competitive 10, Technical/infrastructure 7, Human/organisational 6, Adversarial/abuse 7, Physical/environmental 5, Supply-chain/vendor 6, Scale/load 4, Time/lifecycle 5. Black swans (novelty 5): 7 (S-58…S-64), exceeding the ≥6 target.

---

## 3. Attractor + residue per stressor

*Attractor = do-nothing business end-state (business language). Residue = smallest control that survives it (catalogue `id` where one fits). Leans-on = the dependency/assumption the control needs.*

### S-01 — ITC/PTC repeal dries up the project pipeline
- **Attractor:** The funded utility-scale projects Luminous installs into shrink within a year, machine utilisation falls, and a fixed-cost fleet burns cash against a market that stopped building.
- **Residue:** Geographic + segment diversification kept warm — Australia and any un-subsidised utility-solar demand as a de-correlated pipeline so US federal policy is not the single demand switch.
- **Leans on:** Non-US-subsidy demand can absorb enough fleet utilisation to stay above the burn line.

### S-02 — Domestic-content bonus read to exclude the machines
- **Attractor:** Projects drop Luminous to preserve their bonus credit, and using the machines becomes a reason to *lose* subsidy rather than gain efficiency.
- **Residue:** A domestic-content-compliant machine variant kept warm (US-sourced actuators/compute qualified ahead) + evidence that the *installation service* does not affect the module/component content calculation.
- **Leans on:** Machine bill-of-materials can be re-sourced to a compliant lane, and the credit rule actually turns on installed content not install method.

### S-03 — Prevailing-wage rules make automation a compliance liability
- **Attractor:** On subsidised jobs, robot-installed modules stop counting toward required labor hours, so EPCs must choose between Luminous and their tax credit — and they keep the credit.
- **Residue:** Reposition the machines as *labor-augmenting* — operators, technicians, and redeployed crew are counted, compensated at prevailing wage, and documented — so the machine adds throughput without removing qualifying labor hours (`manual_override_with_review`-style hybrid crew).
- **Leans on:** A hybrid human+machine crew model genuinely preserves qualifying labor hours and prevailing-wage compliance.

### S-04 — Forced-labor import ban seizes panels; projects freeze
- **Attractor:** With panels stuck at port, the projects stall and the machines have nothing to install; revenue stops even though the fleet is ready.
- **Residue:** Flexible, cancellable deployment scheduling tied to verified on-site panel availability, plus a diversified project book so one import shock doesn't idle the whole fleet.
- **Leans on:** Deployments can be re-sequenced quickly to projects that do have panels on the ground.

### S-05 — Anti-dumping / tariff duties spike module prices; builds pause
- **Attractor:** Developers pause builds across a construction season and the installation pipeline contracts, cutting utilisation regardless of Luminous's own pricing.
- **Residue:** Same demand-diversification + flexible scheduling as S-01/S-04; a costed plan that keeps utilisation above burn on a thinner pipeline.
- **Leans on:** Enough of the pipeline survives a tariff shock, spread across geographies, to keep the fleet earning.

### S-06 — Emergency jobsite rule mandates exclusion zones / oversight
- **Attractor:** Machines can't operate near live crews without new controls, and deployments halt on active sites until Luminous complies.
- **Residue:** A certified machine-worker safety envelope + `unlock_redundancy`-style independent safe-stop already fielded, so compliance is a documentation exercise, not a redesign.
- **Leans on:** The fleet already has a defensible, certifiable safety envelope and safe-stop path.

### S-07 — Functional-safety certification becomes mandatory
- **Attractor:** Uncertified machines are barred from operating near workers and the fleet is grounded until certification, which can take quarters.
- **Residue:** Safety-case dossier maintained continuously (the certification evidence *is* the operating record) so certification is a fast conversation, not a from-scratch program.
- **Leans on:** Design and telemetry already produce the safety evidence a standard would demand.

### S-08 — PLA mandates union labor, excluding the machines
- **Attractor:** Luminous is contractually locked out of large federally funded projects where a project-labor agreement requires union field labor.
- **Residue:** Constructive organized-labor engagement + the labor-augmenting crew model (S-03) so machines run *alongside* union crews under an agreed arrangement rather than displacing them.
- **Leans on:** Unions will accept a machine that augments and up-skills their members rather than replaces them.

### S-09 — Australia grid-connection reform cancels a project cohort
- **Attractor:** A chunk of the Australian pipeline is cancelled and one of Luminous's two markets contracts sharply, concentrating exposure back onto the US.
- **Residue:** Two-market balance as a deliberate hedge (same diversification residue as S-01) so neither country's policy alone is fatal.
- **Leans on:** The US pipeline can carry the fleet while Australia contracts, and vice versa.

### S-10 — Buy-America equipment rule disqualifies imported-component machines
- **Attractor:** The biggest infrastructure-funded projects require domestically built equipment and Luminous's machines are ineligible for the largest jobs.
- **Residue:** Same domestic-content-compliant variant kept warm as S-02 — a US-assembled machine SKU pre-qualified before the rule bites.
- **Leans on:** A domestically-assembled machine can be stood up from pre-qualified suppliers on the rule's timeline.

### S-11 — Construction-equipment OEM ships a cheaper competing robot
- **Attractor:** A better-capitalised incumbent with dealer and service reach undercuts Luminous on price and support, and Luminous loses deals on total cost and trust.
- **Residue:** Differentiate on throughput + site-condition robustness + service uptime rather than machine price; a costed value case that a hardware-only rival can't match.
- **Leans on:** Luminous's real-world throughput and uptime are a genuine, demonstrable edge, not a demo artefact.

### S-12 — Large EPC builds installation automation in-house
- **Attractor:** A major customer internalises the capability, stops buying, and Luminous loses a big revenue share plus a reference account to a DIY competitor.
- **Residue:** Deep integration + continuous software/throughput improvement that is uneconomic for one EPC to replicate; contractual + IP protection on the crown-jewel stack (`audit_log_immutability` / least-privilege on IP).
- **Leans on:** Luminous's improvement cadence outpaces what a single EPC's internal team can sustain.

### S-13 — Rate/capex cycle pauses utility-solar builds
- **Attractor:** Developers stop building for multiple quarters and demand for installation collapses at any price, stranding a fixed-cost fleet.
- **Residue:** Flexible-cost fleet posture — machine leases/redeployment, variable staffing, and a runway buffer (S-56) so Luminous can idle without dying; demand diversification across geography and segment.
- **Leans on:** Fixed costs can be flexed down through a demand trough without breaking the company.

### S-14 — Panel price crash shrinks the labor-share ROI case
- **Attractor:** With modules nearly free, labor is a small slice of project cost and the savings from automating it no longer justify paying Luminous.
- **Residue:** Reprice on the value drivers that survive cheap panels — schedule certainty, safety, and quality (fewer damaged/mis-installed modules) — not on labor-cost arbitrage alone.
- **Leans on:** Automation has a defensible value beyond labor cost (speed, safety, quality) that customers will pay for.

### S-15 — Field-labor cost collapses; manual is cheaper
- **Attractor:** Cheap, available manual crews undercut the machines and Luminous's core cost argument inverts in affected regions.
- **Residue:** Same value-repricing as S-14 (safety, schedule, quality) + the augmenting-crew model (S-03) so the machine is additive to a cheap crew, not a costlier substitute.
- **Leans on:** There is a value beyond labor cost, and the machine can complement rather than compete with cheap labor.

### S-16 — Largest EPC customer defects
- **Attractor:** A single account that is a majority of revenue leaves, and the top-line drops below the level the fleet and burn assume.
- **Residue:** Deliberate customer-concentration cap + a broadened logo base so no one account can be load-bearing (`per_tenant_quota` thinking applied to revenue, not compute).
- **Leans on:** Enough other customers exist or are winnable to absorb the loss of the largest.

### S-17 — Tracker/racking vendor co-designs with a rival; standard incompatible
- **Attractor:** The dominant racking standard evolves around a competitor's machine and Luminous's gripper no longer fits the systems being built, foreclosing deals.
- **Residue:** Gripper/handling adaptability designed in — a format- and racking-agnostic end-effector kept configurable — plus partnerships with more than one tracker vendor.
- **Leans on:** The handling system can be adapted to new racking geometries without a full machine redesign.

### S-18 — Capex shifts away from ground-mount
- **Attractor:** Developer money moves to rooftop, C&I, or storage-only, and the ground-mount installation TAM Luminous is built for structurally shrinks.
- **Residue:** A kept-warm adjacency option — the handling/automation stack repointed at neighbouring construction-automation tasks — so the company isn't captive to one project type.
- **Leans on:** The core robotics IP transfers to an adjacent automation market without re-founding the company.

### S-19 — Install-as-a-service startup undercuts price
- **Attractor:** A funded rival resets the market's price expectation below Luminous's unit economics to win logos, and Luminous must either bleed margin or lose deals.
- **Residue:** A margin-floor circuit breaker in pricing governance — landed cost per watt tracked against a hard floor that pauses further discounting.
- **Leans on:** True landed cost per installed watt is known in near-real-time, not just at contract close.

### S-20 — Robot handling causes micro-cracks; warranty wave lands late
- **Attractor:** Modules installed months ago degrade or fail, EPCs and developers pursue warranty and performance claims, and Luminous's quality reputation and licence-to-install take a lasting hit.
- **Residue:** `event_sourcing_audit_trail` on every pick/place (force, torque, handling telemetry per module) to scope liability to affected units + a bounded warranty reserve; catch handling stress early via `shadow_traffic`-style monitoring.
- **Leans on:** Per-module handling telemetry is retained and can isolate the affected population rather than implicate every install.

### S-21 — Market moves to a larger/heavier module format
- **Attractor:** Machines can't pick or fasten the new dominant format, and the fleet becomes obsolete for new projects until redesigned.
- **Residue:** Format-agnostic gripper/handling adaptability (same design residue as S-17) engineered ahead of the format shift.
- **Leans on:** The handling system was designed for a range of module sizes/weights, not one.

### S-22 — Fleet-wide software update ships a placement/torque error
- **Attractor:** A single push turns a fleet-wide strength into a fleet-wide incident, damaging panels and racking across multiple live sites at once and inverting the quality story.
- **Residue:** `progressive_rollout` (1 machine → 1 site → fleet with automated abort) + `feature_flag_kill_switch` on risky motion changes + `shadow_traffic` validation before live actuation.
- **Leans on:** Machines report health/quality metrics fast enough to abort before the update reaches the whole fleet.

### S-23 — Fleet telemetry / remote-control backend outage
- **Attractor:** Machines on remote sites go idle with no dispatch or supervision, and paid throughput stops across every connected site during the outage.
- **Residue:** `local_autonomy` — each machine holds enough state and policy to keep installing safely for N hours offline and reconcile telemetry when connectivity returns.
- **Leans on:** Machines can operate a full shift disconnected from the central plane without unsafe behaviour.

### S-24 — Regional GPS/RTK outage or drift stalls placement
- **Attractor:** Machines that depend on centimetre positioning stop across affected sites, and install halts regionally on a hidden shared dependency.
- **Residue:** `read_only_degraded_mode` for positioning — a safe local-reference / on-machine sensing fallback that either continues at reduced precision or stops safely rather than mis-placing.
- **Leans on:** The stack can detect untrusted positioning and degrade safely instead of acting on bad coordinates.

### S-25 — Real-world throughput falls short of demo economics
- **Attractor:** At utility scale the machines don't hit the per-watt numbers sold, customers don't renew, and the entire value proposition and funding thesis fail to close.
- **Residue:** `stale_data_marker`-style honest throughput reporting from live sites + a throughput-improvement roadmap gated on measured data, so pricing and promises track reality, not the demo.
- **Leans on:** Real per-site throughput is measured honestly and the improvement curve is credible.

### S-26 — Perception AI fails on a novel site condition
- **Attractor:** Machines mis-pick or drop panels under glare/dust/mud until retrained, causing damage and stalling affected sites.
- **Residue:** `shadow_traffic` + condition-tagged telemetry to detect novel conditions and self-restrict + `feature_flag_kill_switch` to degrade to supervised/manual on unrecognised conditions.
- **Leans on:** The stack can recognise a condition it can't handle and stop rather than fail confidently.

### S-27 — Motion-planning / perception lead resigns
- **Attractor:** The core IP loses its owner, the roadmap loses velocity, and institutional knowledge of *why the stack works* walks out with two weeks' notice.
- **Residue:** `runbook_as_code` for the critical stack (documented architecture, decision rationale, not tacit) + retention hooks on the few genuinely irreplaceable individuals.
- **Leans on:** Critical knowledge is captured in artefacts, not only in one person's head.

### S-28 — Field-service technician scarcity; machines sit broken
- **Attractor:** Broken machines idle for days on remote sites waiting for scarce technicians, fleet uptime (and therefore revenue) collapses, and customers lose confidence.
- **Residue:** `runbook_as_code` field-service playbooks + remote diagnosis + modular hot-swap design so a lower-skilled on-site operator can restore a machine without a specialist.
- **Leans on:** Common failures are diagnosable remotely and fixable by swapping modules, not by an expert on site.

### S-29 — A worker is seriously injured or killed by a machine
- **Attractor:** A fatality or serious injury triggers a regulatory stop, customer suspensions, and a licence-to-operate crisis that can end the company.
- **Residue:** Certified safety envelope + independent `unlock_redundancy`-style safe-stop + `event_sourcing_audit_trail` (immutable per-machine decision logs) so the safety case is evidenced and incidents are bounded, investigable, and defensible.
- **Leans on:** The machines have a genuine, certifiable safety envelope and tamper-evident decision logs before an incident, not after.

### S-30 — Operator-supply bottleneck caps deployment
- **Attractor:** Luminous can't hire and train supervising operators fast enough, and deployment is capped below demand regardless of how many machines it builds.
- **Residue:** `runbook_as_code` operator training + progressive automation that raises the machine-to-operator ratio so growth isn't hostage to headcount.
- **Leans on:** The machine's autonomy improves fast enough that fewer operators cover more machines over time.

### S-31 — Core engineering team poached in a hiring raid
- **Attractor:** A rival or big-tech lab hires away the hardware/controls core, and Luminous loses roadmap velocity and IP-in-people at once.
- **Residue:** Same `runbook_as_code` knowledge capture as S-27 + IP compartmentalisation (`audit_log_immutability`, least-privilege) + retention on the irreplaceable few.
- **Leans on:** Knowledge and IP are captured and compartmentalised so a team departure doesn't hollow the company.

### S-32 — Machines/panels stolen or vandalised on a remote site
- **Attractor:** Expensive machines and staged panels are lost or damaged overnight, a deployment is set back, and site-security cost becomes a permanent line.
- **Residue:** Site-hardening + machine immobilisation/geofencing + `event_sourcing_audit_trail` (location/tamper telemetry) so theft is deterred, detected, and recoverable.
- **Leans on:** Machines can be remotely disabled/located and sites can be minimally secured overnight.

### S-33 — Activists sabotage machines to discredit automation
- **Attractor:** Targeted sabotage on sites damages machines and produces exactly the "automation is unsafe/unwelcome" narrative, chilling EPC willingness to deploy.
- **Residue:** Same site-hardening + tamper telemetry as S-32 + the crisis-comms runbook (S-58/S-63) to control the narrative + the labor-augmentation posture (S-03/S-08) that reduces the motive.
- **Leans on:** Physical hardening plus a labor-friendly positioning defuses both the act and its narrative.

### S-34 — Viral video of a machine dropping a panel / near-miss
- **Attractor:** A vivid, shareable failure erodes public and customer trust regardless of statistical safety, and EPCs pause deployments to avoid association.
- **Residue:** `runbook_as_code` crisis-comms + pre-existing credible safety/quality data (from `event_sourcing_audit_trail`) to respond within hours with facts.
- **Leans on:** Real, independently credible safety data exists and can be published fast.

### S-35 — Ransomware locks the fleet-management platform
- **Attractor:** The whole deployed fleet is un-dispatchable until the platform is restored, throughput stops across all sites, and customers face a total-service outage.
- **Residue:** `runbook_as_code` IR + immutable/air-gapped backups + `local_autonomy` so machines keep working offline while the platform is rebuilt.
- **Leans on:** Backups are isolated from the platform and machines can run without it for a bounded window.

### S-36 — Rival reverse-engineers and clones the machine
- **Attractor:** A low-cost clone collapses Luminous's technical lead and price premium, turning a moat into a commodity.
- **Residue:** Reposition the moat from the mechanism to the data + fleet-learning + service that a clone can't replicate; `audit_log_immutability` + compartmentalised IP to slow and prosecute copying.
- **Leans on:** Fleet-scale operating data and service are a durable edge even when the hardware is copyable.

### S-37 — Remote hijack/bricking of machines demonstrated at scale
- **Attractor:** Public confidence in fleet security collapses, regulators demand answers, and the connected-machine model becomes a liability.
- **Residue:** `key_rotation_dual_accept` (rotate machine credentials fleet-wide fast) + a rapid security-patch channel with `progressive_rollout` to avoid a bad-patch repeat.
- **Leans on:** Credentials are centrally rotatable and a security fix can ship to the fleet within days without breaking it.

### S-38 — Multi-week extreme heat halts machines and crews
- **Attractor:** The season's install window is lost across a region, throughput and revenue slip out of the period, and contracted schedules are missed.
- **Residue:** Heat-hardened machines (thermal design) + schedule flexibility to shift work to cooler windows/geographies (the two-market, multi-site posture of S-01/S-51).
- **Leans on:** Machines can operate through more heat than crews, and schedule can flex across sites and seasons.

### S-39 — Dust storm / mud makes a site impassable
- **Attractor:** A deployment strands mid-project when the chassis can't move or work, and the contract's schedule and Luminous's uptime suffer.
- **Residue:** Terrain/weather-hardened mobility + a site-condition pre-qualification checklist so unsuitable conditions are known before deploying, and a safe idle-and-resume mode.
- **Leans on:** Sites are condition-screened before deployment and machines can safely wait out weather.

### S-40 — Wildfire/flood destroys a staged fleet
- **Attractor:** A concentrated fleet loss on one site is a direct capital hit and a gap in service capacity for other jobs.
- **Residue:** Fleet insurance sized to catastrophic site loss + not over-concentrating the fleet on one exposed site; rapid-recovery logistics.
- **Leans on:** Insurance and fleet dispersion keep a single-site disaster from being a company-level capital event.

### S-41 — Contracted site's terrain defeats the machines
- **Attractor:** A deployment and its contract are stranded because the machines can't traverse or work the actual ground, and the customer relationship sours.
- **Residue:** Same site pre-qualification checklist as S-39 — a contractual site-suitability gate before commit, plus the augmenting-crew fallback for the un-machinable portions.
- **Leans on:** Site suitability is verified and contracted against before deployment, and humans can cover the gaps.

### S-42 — Washed-out roads strand machines and parts
- **Attractor:** Machine recovery and spare-parts delivery are cut off for weeks, uptime falls, and machines are stuck earning nothing on an unreachable site.
- **Residue:** On-site spares buffer + `local_autonomy` so a temporarily isolated machine keeps working and is serviceable locally until access returns.
- **Leans on:** Enough spares and local-service capability sit on-site to survive an access outage.

### S-43 — Sole-source actuator/reducer supplier price/allocation shock
- **Attractor:** A critical component's cost jumps or allocation shrinks, throttling machine production and raising unit cost below the economics the fleet assumes.
- **Residue:** `bulkhead` across component suppliers + `dependency_freeze_window`/design-for-substitution so no single actuator/reducer vendor is a chokepoint.
- **Leans on:** Machine designs accept components from more than one supplier without re-engineering.

### S-44 — Edge-AI compute / GPU shortage stalls machine builds
- **Attractor:** Luminous can't build enough machines to meet the season's contracts and forgoes revenue it had already won.
- **Residue:** Compute pre-buy/inventory buffer + design-for-substitution across compute options (`dependency_freeze_window`) so builds aren't hostage to one chip.
- **Leans on:** Alternate compute can be qualified and stock buffered ahead of a shortage.

### S-45 — Battery-cell supply constraint
- **Attractor:** Every new machine costs more or ships later, compressing the economics and slowing fleet growth.
- **Residue:** Multi-source cells (`bulkhead`) + chemistry flexibility so a single cell supplier isn't a chokepoint.
- **Leans on:** Machines accept more than one cell source/chemistry without redesign.

### S-46 — Panels held at port; capacity but nothing to install
- **Attractor:** The fleet is ready but idle because panels are stuck upstream, and Luminous burns cost with no throughput to bill.
- **Residue:** Same demand/scheduling flexibility as S-04 — re-sequence the fleet onto projects with panels on the ground; don't let one import lane strand the fleet.
- **Leans on:** A diversified project book means some sites always have panels available to install.

### S-47 — Critical component supplier acquired by a competitor
- **Attractor:** A rival gains control of a key input and can raise Luminous's cost, cut allocation, or cut it off.
- **Residue:** Same multi-source `bulkhead` + pre-qualified second sources as S-43, so no acquired supplier is a single point of control.
- **Leans on:** A second source for each critical component is pre-qualified before the acquisition.

### S-48 — Contract manufacturer quality escape or insolvency
- **Attractor:** Machines ship with a latent defect (a fleet-wide quality bomb) or stop shipping entirely, hitting both delivered-fleet reliability and build capacity.
- **Residue:** Incoming-quality gating + `event_sourcing_audit_trail` on build provenance to scope any defect + a pre-qualified alternate manufacturer.
- **Leans on:** Build provenance is traceable per machine and a second manufacturer can be stood up on the timeline.

### S-49 — Gigawatt project demands 10× the fleet on a fixed schedule
- **Attractor:** A single mega-contract strains logistics, service, and staffing beyond what they were built for, and Luminous either over-commits and fails to deliver or turns down its biggest opportunity.
- **Residue:** `per_tenant_quota` / `backpressure` on commitments — size contracts to proven fleet and ops capacity, expand only as capacity is demonstrated; stage the mega-project.
- **Leans on:** Real fleet and ops capacity is measured and commitments are gated on it, not on the deal's ambition.

### S-50 — Rapid multi-site expansion outruns service/spares logistics
- **Attractor:** Fleet uptime collapses across all sites simultaneously as spares and technicians spread too thin, and every customer's throughput suffers at once.
- **Residue:** Capacity-led expansion (`backpressure`) gating new sites on service/spares readiness + the field-service runbook and modular design of S-28.
- **Leans on:** Expansion is paced against service capacity, not demand alone.

### S-51 — Construction-season demand concentration exceeds fleet
- **Attractor:** Everyone wants machines in the same months, Luminous can't serve them all, and it either disappoints customers or overbuilds a fleet that idles off-season.
- **Residue:** Counter-seasonal geographic balance (US and Australian seasons are offset) + demand-shaping pricing to spread the peak.
- **Leans on:** The two hemispheres' offset seasons and pricing can smooth a single peak.

### S-52 — One customer grows to dominate the schedule and pricing
- **Attractor:** A single account dictates priority and price, every shared process bends around it, and Luminous loses pricing power and resilience to that one relationship.
- **Residue:** Customer-concentration cap + `bulkhead`-style account isolation so one customer's demands don't degrade service or economics for the rest (same residue as S-16).
- **Leans on:** Enough diversified demand exists that no one account has to be accommodated at any cost.

### S-53 — Flagship pilot never converts to paid commercial scale
- **Attractor:** A reference deployment consumes resources and goodwill for years without becoming revenue, and the proof-point never pays back.
- **Residue:** Time-boxed pilots with pre-agreed conversion milestones and commercial terms (a `dependency_freeze_window`-style expiry) so a pilot can't quietly run forever.
- **Leans on:** Pilots carry contractual conversion gates, not open-ended goodwill.

### S-54 — Fleet ages; refurbishment capex balloons pre-payback
- **Attractor:** First-generation machines need costly refurbishment before they've earned back their build cost, and the fleet's unit economics turn negative.
- **Residue:** Fleet-lifecycle reserve modelled from field-hour telemetry + a refurbish-vs-replace policy priced in advance.
- **Leans on:** Field-hour telemetry gives an accurate forward maintenance/refurbishment liability.

### S-55 — Safe-harbour deadline pulls demand forward, then a cliff
- **Attractor:** A rush of projects in one year is followed by a demand cliff, and a fleet scaled to the peak idles after the deadline passes.
- **Residue:** Flexible-capacity posture (lease/redeploy, variable staffing) + counter-cyclical/geographic demand so the fleet isn't sized only to a policy-driven spike.
- **Leans on:** Fleet capacity can flex down after the pull-forward without stranded fixed cost.

### S-56 — Next round must close in a frozen VC market before unit economics prove out
- **Attractor:** Capital-intensive burn runs the runway down before Luminous proves its economics, and it faces a down round, distress sale, or shutdown.
- **Residue:** Runway discipline — staged capex (build fleet as contracts are won, not ahead) + a liquidity-runway KPI + non-dilutive project/asset financing for the fleet.
- **Leans on:** Machine build can be paced to booked demand and the fleet is financeable as a hard asset.

### S-57 — Early-fleet warranty/service liability exceeds reserves
- **Attractor:** Accumulating field hours surface more warranty and service cost than reserved, and a supposed profit line turns into a cash drain.
- **Residue:** Warranty/service reserve modelled from live field telemetry (same reserve discipline as S-20/S-54) + bounded, pre-priced remediation.
- **Leans on:** Field telemetry gives an accurate forward warranty/service liability, not an optimistic guess.

### S-58 ★ — National TV alleges a machine caused a death or fire (true or not)
- **Attractor:** Panic-driven contract suspensions and a licence-to-operate crisis regardless of the facts; the brand fuses with danger and EPCs won't risk association.
- **Residue:** `runbook_as_code` crisis-comms + pre-existing credible safety data (`event_sourcing_audit_trail`) publishable within hours to rebut, plus a rehearsed regulator-engagement path.
- **Leans on:** Real, independently credible safety data exists and a crisis-comms capability can respond in hours, not days.

### S-59 ★ — Overnight US–China module decoupling strands the pipeline
- **Attractor:** With no panels entering the US, the entire utility-solar module pipeline freezes and Luminous's largest market has nothing to install — simultaneous, total demand loss in one geography.
- **Residue:** The two-market hedge (S-01/S-09) plus flexible scheduling (S-04/S-46) as a standing posture; Australia and any domestic-module supply keep some fleet earning. **This is the residue Luminous is least able to field today — flag as a structural gap, not a claimed control.**
- **Leans on:** Non-US-module pipeline (Australia, domestic panels) can absorb enough fleet to survive a US freeze.

### S-60 ★ — Rival demonstrates full end-to-end autonomous solar-farm build
- **Attractor:** An integrated pile-racking-panel system makes Luminous's single-step panel robot look obsolete, and the strategic narrative — and next raise — moves to the competitor.
- **Residue:** A kept-warm full-stack roadmap (extend beyond panel install toward the adjacent steps) so Luminous can fast-follow the integration rather than restart; the adjacency option of S-18.
- **Leans on:** The core IP extends to adjacent build steps, and a full-stack path is engineered-ahead, not started under fire.

### S-61 ★ — Court assigns open-ended manufacturer liability; insurance dries up
- **Attractor:** Every autonomous machine-hour becomes an open-ended tort exposure, product-liability cover becomes unaffordable or unavailable, and the business model becomes uninsurable.
- **Residue:** `event_sourcing_audit_trail` (immutable per-machine decision logs as the safety case / evidence) + captive or reinsured liability capital sized to the retained tail + the certified safety envelope (S-29).
- **Leans on:** Decision logs are admissible and the safety case supports acceptable (re)insurance terms; a captive can be capitalised.

### S-62 ★ — Solar backlash / moratoria freeze new ground-mount approvals
- **Attractor:** A wave of moratoria collapses the ground-mount market Luminous is built to serve, independent of anything Luminous does — the whole TAM contracts.
- **Residue:** The adjacency option (S-18/S-60) — repoint the automation stack at neighbouring construction-automation markets — plus geographic diversification so no single jurisdiction's politics is fatal.
- **Leans on:** The robotics IP transfers to an adjacent market, and not all geographies freeze at once.

### S-63 ★ — Deepfake / hoax of a machine "going rogue" floods media
- **Attractor:** A fabricated "rogue machine" clip triggers contract suspensions and regulator questions before it can be debunked, and trust in Luminous's safety collapses on a lie.
- **Residue:** A signed/authenticated official-communications channel + `runbook_as_code` rapid rebuttal + the credible safety data of S-58 to disprove the fake fast.
- **Leans on:** Customers and regulators know and trust an authenticated Luminous source, and real footage/data can disprove the fake quickly.

### S-64 ★ — Geopolitical rupture closes Australian operations overnight
- **Attractor:** One of two markets, its pipeline, staff, and staged fleet, is lost at once — the largest concentrated geographic shock short of losing the US.
- **Residue:** Geographic diversification with a market-exit/asset-recovery plan so no single country is un-survivable if lost; the US pipeline carries the fleet through an Australia exit (mirror of S-59).
- **Leans on:** The US market can absorb the fleet, and Australian assets/staff can be extracted or written down without breaking the company.

---

## 4. Deduped control portfolio

The 64 residues collapse into **19 controls**. A handful carry most of the risk.

| Control | Risks covered | Owner-role | Leans on (dependency / assumption) | Notes |
|---|---|---|---|---|
| **C-01 Demand diversification (2-market + segment + flexible scheduling)** | S-01, S-04, S-05, S-09, S-13, S-46, S-55, S-59, S-64 | CEO / VP Commercial | Non-US-subsidy and non-single-project-type demand can keep fleet utilisation above burn; deployments re-sequenceable | Highest-coverage demand control (9 risks). The core hedge against policy, import, cycle, and geopolitical shocks. |
| **C-02 Staged fleet software rollout + kill switches** (`progressive_rollout`, `feature_flag_kill_switch`, `shadow_traffic`) | S-22, S-26, S-37, (S-20 detection) | VP Robotics Software | Machines report health/quality fast enough to abort; motion changes independently gateable | The single most load-bearing technical control; touches quality, perception, and security patching. |
| **C-03 Immutable install + safety/decision audit trail** (`event_sourcing_audit_trail`, `audit_log_immutability`) | S-07, S-12, S-20, S-29, S-31, S-32, S-36, S-48, S-58, S-61, S-63 | Chief Safety / Legal | Per-machine, per-module telemetry retained, tamper-evident, admissible | Highest-coverage control overall (11 risks). Evidence base for safety, liability, quality, provenance, IP, and crisis rebuttal. |
| **C-04 Certified machine-worker safety envelope + safe-stop** (`unlock_redundancy`, `manual_override_with_review`) | S-06, S-07, S-29, S-61 | Chief Safety / VP Hardware | Fleet has a defensible, certifiable safety envelope and independent safe-stop | Load-bearing for the existential worker-safety and insurability risks. |
| **C-05 Local autonomy / offline site operation** (`local_autonomy`, `read_only_degraded_mode`) | S-23, S-24, S-35, S-42 | VP Robotics Software | Machines operate a full shift safely disconnected and reconcile on reconnect | Keeps remote-site revenue alive through backend, positioning, cyber, and access outages. |
| **C-06 Format-/racking-agnostic handling adaptability** | S-17, S-21 | VP Hardware / Gripper | Handling system adapts to module sizes and racking geometries without full redesign | Anti-obsolescence for the physical interface to the market. |
| **C-07 Multi-source components + design-for-substitution** (`bulkhead`, `dependency_freeze_window`) | S-43, S-44, S-45, S-47 | VP Supply Chain | Designs accept ≥2 sources per critical component without re-engineering | Merged four component-chokepoint residues. |
| **C-08 Field-service runbook + modular hot-swap design** (`runbook_as_code`) | S-28, S-30, S-42, S-50 | VP Field Operations | Common failures are remotely diagnosable and fixable by swapping modules on site | Uptime is revenue; this is the uptime control. |
| **C-09 Capacity-led deployment gating** (`per_tenant_quota`, `backpressure`) | S-49, S-50, S-51 | VP Field Operations | Real fleet/ops capacity is measured and commitments gated on it | Contains mega-project and expansion overreach. |
| **C-10 Customer-concentration cap + account isolation** (`per_tenant_quota`, `bulkhead`) | S-16, S-52 | VP Commercial | Enough diversified demand that no one account is load-bearing | |
| **C-11 Value-based pricing + margin-floor circuit breaker** | S-11, S-14, S-15, S-19, S-25 | CFO / VP Commercial | Landed cost per watt known in near-real-time; safety/schedule/quality value is real and priceable | Merged the "labor-arbitrage isn't the only value" residues; defends against price wars and the ROI-erosion cases. |
| **C-12 Labor-augmentation crew model + organized-labor engagement** | S-03, S-08, S-15, S-33 | VP Commercial / Public Affairs | A hybrid human+machine crew genuinely preserves qualifying labor hours and defuses union opposition | The political/regulatory-labor residue; also blunts the sabotage motive. |
| **C-13 Domestic-content-compliant machine variant kept warm** | S-02, S-10 | VP Supply Chain / Legal | A US-assembled SKU can be stood up from pre-qualified suppliers on the rule's timeline | Partly aspirational until actually pre-qualified. |
| **C-14 Warranty / fleet-lifecycle reserve modelling** | S-20, S-54, S-57 | CFO | Field telemetry gives accurate forward warranty/maintenance liability | Merged three "bounded, telemetry-priced reserve" residues; leans on C-03. |
| **C-15 Crisis-comms + authenticated-channel runbook** (`runbook_as_code`) | S-34, S-58, S-63 | Comms / Public Affairs | Credible safety data publishable in hours; trusted authenticated announcement source | Covers reputational black swans; leans entirely on C-03 for the underlying data. |
| **C-16 Cyber: credential rotation + IR + immutable backups** (`key_rotation_dual_accept`, `runbook_as_code`) | S-35, S-37 | CISO | Credentials centrally rotatable; backups air-gapped; security fix ships fast | Couples with C-02 (shared fleet-update channel) and C-05 (offline survival). |
| **C-17 Key-person / knowledge continuity + IP compartmentalisation** (`runbook_as_code`, `audit_log_immutability`) | S-12, S-27, S-31, S-36 | CTO / CHRO | Critical knowledge captured in artefacts; crown-jewel IP compartmentalised and logged | Covers founder-engineer loss, team raids, and IP theft/cloning. |
| **C-18 Site pre-qualification + hardening + insurance** | S-32, S-33, S-38, S-39, S-40, S-41 | VP Field Operations | Sites are condition-screened before deploy; machines hardened/immobilisable; catastrophic loss insured | Merged the physical/environmental and site-security residues. |
| **C-19 Runway discipline + kept-warm strategic options** | S-13, S-18, S-53, S-55, S-56, S-60, S-62 | CEO / CFO | Build paced to booked demand; fleet financeable as an asset; adjacency/full-stack options engineered-ahead not slideware | Merged capital-discipline and "kept-warm fallback" residues — the anti-complacency + survival portfolio. |

**Merge history & residual gaps.** C-01, C-07, C-11, C-14, C-18, C-19 are aggressive merges of same-shape residues wearing different product names — the shrinkage (64 → 19) is the finding. Thin/single-control coverage: **S-24** (GPS/RTK — only C-05's degraded-mode; no positioning redundancy), **S-46/S-59** (import freeze — C-01 assumes an alternative pipeline that is only partly real), **S-53** (pilot conversion — a single commercial-discipline residue owned by VP Commercial). These are flagged below.

---

## 5. Contagion / systemic-risk analysis

### Top cascade paths (shared dependency/assumption → controls that fail together)

1. **"A funded project with panels on the ground exists" is one assumption behind the whole revenue side.** C-01 (demand diversification), C-09 (capacity gating), C-11 (pricing), and C-19 (runway) all assume there is *something to install*. An S-01 + S-04/S-46 + S-13 cluster (credit repeal, import freeze, capex trough) removes the projects, the panels, and the financing at once — and no operational control helps when the machines have nothing to install. This is the deepest systemic exposure: Luminous's fate is set upstream of anything it builds.

2. **The immutable audit trail (C-03) is the shared upstream for four other controls.** C-14 (warranty reserves), C-15 (crisis-comms rebuttal), C-04 (safety-case evidence), and the liability defense in S-61 all *depend on* C-03 having captured credible, tamper-evident per-machine and per-module data first. If C-03 is incomplete or not independently credible, the reserves are mis-sized, the crisis response has nothing to publish, the safety case is unprovable, and the insurance argument collapses — a single data-quality failure de-fangs the safety, financial, and reputational defenses together.

3. **The fleet-software / connectivity channel is one dependency behind three controls.** C-02 (staged rollout), C-16 (security patching), and C-05 (offline operation) all ride the same fleet-update and telemetry pipeline. If that pipeline is compromised or poisoned (the S-22 + S-37 nightmare), the very control meant to contain a bad push is the vector — Luminous's fleet-management strength and its single point of correlated failure are the same channel.

4. **Worker safety is one event behind the licence to operate.** C-04 (safety envelope), C-03 (decision logs), C-15 (crisis-comms), and C-12 (labor relations) all converge on S-29 / S-58. A single serious injury cascades into regulatory stop, viral narrative, insurance loss (S-61), and union backlash simultaneously — one physical event triggers the regulatory, reputational, financial, and political failure modes at once. It is the closest thing Luminous has to a single existential trigger.

5. **"Field labor is expensive and automation is welcome" is one assumption behind the commercial case and the political case.** C-11 (value pricing), C-12 (labor-augmentation model), and the prevailing-wage/PLA residues (S-03, S-08) all lean on it. A labor-cost collapse (S-15) plus a prevailing-wage reinterpretation (S-03) attacks both the economic and the political justification for the machines together — the ROI argument and the licence-to-deploy fail on the same shift in labor conditions.

6. **Runway is the shared clock behind every slow-burn control.** C-19 (runway discipline), C-06/C-13/C-19 (kept-warm options), and the whole capital-intensive fleet all lean on "the next round closes." A demand trough (S-13), a throughput shortfall (S-25), and a frozen VC market (S-56) arriving together shorten the clock on every option at once — Luminous can be structurally right about the market and still run out of time to reach it.

7. **Geographic concentration couples policy, import, and geopolitical shocks.** C-01's diversification *assumes* the two markets are genuinely substitutable, but S-59 (US module freeze) and S-64 (Australia closure) show each market carries its own tail. If the ex-market absorption capacity is only partly real — which it is today — then either country's loss is closer to fatal than the diversification story claims.

### Orphan controls (map to no live risk)
None. Every control in §4 maps to ≥1 live stressor — the portfolio was derived from the stressors, so there is no accumulated risk-theatre. Watch that **C-13 (domestic-content variant)** and the ex-market capacity inside **C-01** don't become *reverse* orphans: controls claimed on the slide but not actually fielded when the shock lands.

### Under-covered stressors (single-control or thin coverage)
- **S-59 (US module freeze)** and **S-64 (Australia closure)** — the black swans with the weakest genuine residue. C-01 *assumes* an ex-market pipeline that is only partially real today. Flagged in §3 as a structural gap, not a claimed control.
- **S-24 (GPS/RTK outage)** — covered only by C-05's degraded-mode; there is no positioning redundancy, so machines stop rather than continue when positioning is untrusted.
- **S-53 (pilot never converts)** — a single commercial-discipline residue (conversion gates), owned by VP Commercial, with no backstop if the discipline slips.
- **S-25 (throughput shortfall)** — covered by C-11's honest reporting, but if the throughput curve simply never reaches the promised economics, no control saves the value proposition; it is a thesis risk more than a manageable one.

---

## 6. Resilience regime verdict

**Verdict: edge of chaos, tilting toward chaotic on its demand-concentration and single-event axes.**

Luminous is *not* frozen. It is an early, lean hardware startup that absorbs novelty with engineering and commercial improvisation rather than bureaucratic exception-handling. The stressor set did not need a bespoke exception per event — 64 stressors mapped onto 19 genuinely load-bearing, mostly loosely-coupled controls, and there are no orphan controls. That shrinkage and the absence of risk-theatre are hallmarks of an edge-of-chaos system: few controls, each doing real work.

But three things pull it toward chaotic. First, **upstream demand concentration**: Luminous only earns when a funded project, delivered panels, and workable conditions coincide, and the contagion analysis shows the *same* upstream assumption sitting behind the entire revenue side — a policy/import/capex cluster (S-01/S-04/S-13/S-59) fails C-01, C-09, C-11, and C-19 at once, and no operational control substitutes for having nothing to install. Second, **the single-event safety trigger**: a serious worker injury (S-29/S-58) cascades into regulatory, reputational, insurance, and labor failure simultaneously — one physical event is close to existential, which is the signature of a chaotic coupling. Third, **the runway clock**: as a capital-intensive startup, Luminous can be strategically correct and still be killed by the timing of a frozen raise, coupling technical/commercial delivery directly to financial survival in a way an incumbent doesn't experience.

**Three concrete deltas to move it back toward the resilient edge:**

1. **Make the two-market / alternative-pipeline hedge real, not assumed (the single most brittle coupling).** Fund enough genuine Australian and non-US-subsidy pipeline — and enough scheduling flexibility — that a US policy or import freeze is survivable-with-pain rather than existential. This is the delta with the largest resilience payoff because it de-correlates C-01, C-09, C-11, and C-19 at once. Today it is the residue Luminous is least able to field.

2. **Over-invest in the safety envelope and the audit trail (C-04 + C-03) ahead of scale.** These are the shared upstream for the existential worker-safety cascade *and* the financial/reputational/insurance defenses. A single serious incident is the closest thing to a company-ending event, and every defense against it leans on evidence that must exist *before* the incident. This is the cheapest insurance against the highest-consequence coupling.

3. **Decouple the fleet-software channel from its own failure mode, and pace burn to booked demand.** Add an out-of-band rollback/attestation path so the channel that contains a bad push (C-02) and ships a security fix (C-16) doesn't share fate with the poison vector (S-22/S-37); and hold capex staging tight enough that a demand trough plus a frozen raise (S-13 + S-56) can't run the clock out before unit economics are proven. Together these address the technical-monoculture and runway-clock couplings.

*Caveat (per playbook): the regime read is a directional heuristic about brittleness, not a predicted incident rate. Re-run quarterly and on trigger.*

---

## 7. Cadence & triggers

- **Re-run cadence:** quarterly (aligned to the construction-season and funding cycle).
- **Trigger events forcing a fresh pass regardless of cadence:** any change to US ITC/PTC, domestic-content, or prevailing-wage rules; a new UFLPA/tariff/anti-dumping action on modules; an Australian renewable-policy or grid-connection reform; a new robotics-safety or autonomous-machinery jobsite regulation; any serious safety incident involving a machine; loss or hard renegotiation of a sole-source component supplier; loss of the largest customer; a funding round (raise or failure to raise); entry into a new geography or an adjacent automation market; a competitor shipping integrated full-stack build automation.
- **Artefact owner:** Chief Risk Officer (or the CFO's office if no CRO), distinct from the individual control owners in §4.

---

*Total stressors: 64 (S-01…S-64), 9/9 categories, 7 black swans. 64 residues deduped to 19 controls. Method per `residuality-enterprise-risk-management.md`; catalogue controls per `residuality/references/residue_library.md`.*

---

## Completeness pass — additional stressors

*Second pass (2026-07-06). Goal: find distinct stressor **mechanisms** the first 64 missed — not restatements. Each card names the nearest existing S-number and states the mechanistic difference, so nothing here duplicates §2–§3. Numbering continues from S-65. Same template: Stressor (sentence + category + novelty 1–5), Attractor (do-nothing business end-state), Residue (smallest control, catalogue `id` where one fits), Leans-on. Black swans (novelty 5) marked ★. Catalogue controls and existing C-01…C-19 referenced where the residue folds in; genuinely new control surfaces are flagged in the closing note.*

### S-65 — US interconnection-queue / transmission reform freezes the pipeline
- **Category:** Regulatory/legal — **Novelty:** 3
- **Distinct from:** S-09 (that is *Australian* grid-connection reform) and S-01 (that is the *tax credit*). This is US-side grid **access** — a FERC/RTO interconnection-queue overhaul or a transmission-capacity freeze — killing projects that are otherwise funded and credit-eligible.
- **Attractor:** A cohort of US utility-scale projects can't secure interconnection and are cancelled or deferred for years; the US pipeline Luminous installs into thins independent of subsidy or capex appetite.
- **Residue:** C-01 demand diversification (two-market + segment + flexible scheduling) — re-sequence the fleet onto projects that already hold interconnection agreements; track pipeline by grid-access status, not just award.
- **Leans on:** Enough interconnection-cleared projects exist across geographies to keep utilisation above burn.

### S-66 — Federal public-land leasing / permitting halt after an administration change
- **Category:** Regulatory/legal — **Novelty:** 3
- **Distinct from:** S-01 (tax-credit repeal — a *fiscal* lever). This is **land access and permitting** — a BLM/public-land solar-leasing pause or a NEPA/permitting slowdown under a hostile administration — that strands the large public-land projects even if credits survive.
- **Attractor:** The biggest Western US utility-scale sites, disproportionately on federal land, stop entering construction; a whole tier of large deployments Luminous is built for evaporates.
- **Residue:** C-01 — weight the book toward private-land and Australian projects; keep a pipeline mix that isn't hostage to federal-land permitting.
- **Leans on:** Private-land and ex-US pipeline can carry the fleet through a public-land freeze.

### S-67 — Electrical-licensing / building code requires a licensed human installer
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-06/S-07 (machine *safety* certification). This is **professional licensing of the install act itself** — a code or licensing-board ruling that setting and bonding a module is licensed electrical work only a credentialed human may perform or sign off.
- **Attractor:** The robot legally cannot be the installer of record; every robot-placed module needs a licensed human in the loop or the install is non-compliant, gutting the labor-displacement economics on affected jurisdictions.
- **Residue:** C-12 labor-augmentation crew model — reframe the machine as a tool operated *under* a licensed installer who signs off, with `event_sourcing_audit_trail` producing the per-module compliance record the licensee attests to.
- **Leans on:** A licensed-human-plus-machine crew still beats a manual crew on landed cost per watt, and the licensee will attest to machine-placed work.

### S-68 — US export controls classify Luminous's autonomous-AI robotics as controlled tech
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-10 (Buy-America on *inputs into projects*) and S-59 (Chinese *module* decoupling). Here Luminous's **own** technology — autonomous-navigation AI plus advanced edge compute — is placed under EAR/dual-use export controls, restricting transfer to the Australian operation or the use of controlled chips.
- **Attractor:** The Australian arm can't legally receive the latest stack or compute; the two-market model fractures into two diverging fleets, and the Australian book degrades toward obsolescence.
- **Residue:** A trade-compliance function + an export-classification review of the stack, with a licence-exception/compliant-export variant kept warm (analogue of C-13's kept-warm compliant SKU, applied to tech transfer).
- **Leans on:** A licence or exception path exists to keep the Australian fleet current, and the stack can be partitioned into exportable and controlled layers.

### S-69 — Australian native-title / cultural-heritage ruling halts a contracted site mid-build
- **Category:** Regulatory/legal — **Novelty:** 3
- **Distinct from:** S-41 (physical *terrain* the machines can't traverse) and S-62 (generic *moratoria*). This is Australia-specific **Indigenous land rights** — a native-title determination or sacred-site/cultural-heritage injunction stopping or rerouting work on land already contracted and staged.
- **Attractor:** A staged Australian deployment is frozen or evicted mid-project, the contract stalls, machines sit idle on unusable ground, and the customer relationship sours.
- **Residue:** C-18 site pre-qualification — add a cultural-heritage / native-title clearance gate to the site-suitability checklist before commit, and cancellable deployment scheduling so an idled site releases the fleet elsewhere.
- **Leans on:** Heritage/title status is verifiable before deployment and machines can be re-sequenced off a halted site.

### S-70 — US endangered-species / environmental injunction stops a site mid-build
- **Category:** Regulatory/legal — **Novelty:** 3
- **Distinct from:** S-41 (terrain) and S-62 (moratoria on *new approvals*). This is a **species/environmental** injunction (desert tortoise, sage grouse, wetlands) halting an *already-approved, in-construction* Southwest site.
- **Attractor:** A contracted deployment is stopped by court order mid-build; the fleet on that site is stranded and the schedule slips out of the season.
- **Residue:** C-18 site pre-qualification (environmental-clearance gate) + cancellable scheduling — same residue shape as S-69, screening a different clearance.
- **Leans on:** Environmental clearance is confirmable pre-deployment and the fleet is redeployable off a stopped site.

### S-71 — Customs re-classifies the machines into a higher-duty tariff line
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-05 (tariffs on *modules*) and S-10 (Buy-America on *project equipment*). This is a customs **classification dispute on Luminous's own machines** — a ruling that reclassifies them into a higher-duty HS line, spiking the cost of moving the fleet between the US and Australia (and of importing built units).
- **Attractor:** Every cross-border machine movement carries an unbudgeted duty, the two-market logistics economics deteriorate, and back-duties/penalties land on units already moved.
- **Residue:** A tariff-engineering + binding-ruling strategy (obtain an advance customs classification) + landed-cost modelling that prices duty into fleet-movement decisions; hold fleet regionally to minimise dutiable crossings.
- **Leans on:** A defensible classification exists and regional fleet-holding avoids most dutiable movements.

### S-72 — Lithium-battery dangerous-goods transport rules restrict trucking/shipping the fleet
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-45 (battery *cell supply*) and S-42 (washed-out *roads*). This is **DG transport regulation** — tightened lithium-battery road/air/sea dangerous-goods rules that restrict, slow, or forbid moving the machines' large packs, throttling fleet logistics to remote sites.
- **Attractor:** Machines can't be legally or economically moved to and from remote sites on the season's schedule; deployments slip and recovery costs balloon.
- **Residue:** DG-compliant logistics playbook (`runbook_as_code`) + swappable/de-rated transport-mode battery config (ship the pack below the DG threshold or remove/transport separately) so the fleet stays movable under the rules.
- **Leans on:** Packs can be transport-configured to stay compliant and a certified DG carrier lane exists to each region.

### S-73 — Australian renewable-target rollback cuts LGC value and the pipeline
- **Category:** Regulatory/legal — **Novelty:** 3
- **Distinct from:** S-09 (Australian grid-**connection** reform — a *technical/queue* lever). This is the **subsidy/target itself** — a post-election LRET/large-scale-target rollback or LGC-price collapse — Australia's direct analogue of S-01, which was framed US-only.
- **Attractor:** Australian project economics deteriorate, builds pause, and the in-country pipeline — Luminous's designated hedge against US policy — thins at the same time it is being counted on.
- **Residue:** C-01 two-market hedge, but stress-tested for *correlated* policy retreat — don't assume Australian demand is uncorrelated with US demand; keep segment/non-subsidised demand in the mix.
- **Leans on:** Some Australian (and non-subsidised) demand survives a target rollback; the two markets don't both retreat at once.

### S-74 — Ultra-light / flexible / perovskite modules erode the "too heavy for humans" rationale
- **Category:** Market/competitive — **Novelty:** 4
- **Distinct from:** S-21 (a *heavier* next-gen format the machines can't lift). This is the **opposite direction** — a module technology shift to light, flexible, or perovskite panels a person can carry and place, removing the ergonomic/safety reason to pay for robotic handling.
- **Attractor:** The core value driver ("heavy, dangerous, slow for a manual crew") weakens; manual placement becomes fast and safe, and the automation ROI narrows structurally.
- **Residue:** C-11 value-based pricing — re-anchor on the value that survives light modules (schedule certainty, placement precision, quality, torque/bonding consistency, data) rather than on lift-and-carry labor arbitrage; C-06 handling adaptability for the new form factor.
- **Leans on:** Automation retains a priced advantage in precision/speed/quality even when modules are light enough to hand-place.

### S-75 — Tax-equity / project-finance freeze leaves credits intact but unmonetizable
- **Category:** Market/competitive — **Novelty:** 3
- **Distinct from:** S-01 (credit *repealed*) and S-13 (a *rate/capex* cycle). Here the credit **still exists** but the tax-equity / project-finance market that converts it into cash freezes, so developers can't finance builds.
- **Attractor:** Funded-on-paper projects can't reach financial close, construction starts stall across the book, and installation demand contracts even though policy is unchanged.
- **Residue:** C-01 demand diversification + C-19 runway discipline — pace fleet build to *financially-closed* projects, not announced ones; diversify toward developers with balance-sheet or non-tax-equity financing.
- **Leans on:** Enough projects reach financial close through a tax-equity freeze to keep the fleet earning.

### S-76 — China restricts export of critical robotics inputs as geopolitical leverage
- **Category:** Supply-chain/vendor — **Novelty:** 4
- **Distinct from:** S-43 (a *commercial* price/allocation shock from a supplier) and S-59 (a *module* decoupling). This is a **state export ban on inputs into Luminous's machines** — rare-earth magnets, gallium, precision reducers — used as geopolitical leverage, cutting supply regardless of price or relationship.
- **Attractor:** Machine production stalls on inputs money can't buy; fleet growth halts and existing-fleet spares dry up, capping the business at its current unit count.
- **Residue:** C-07 multi-source components + design-for-substitution (`bulkhead`, `dependency_freeze_window`) extended to **country-of-origin** diversity + a strategic buffer stock of the most export-exposed inputs.
- **Leans on:** Non-China sources or substitutes for the most export-exposed inputs can be qualified, and a buffer bridges the qualification gap.

### S-77 — A competitor bundles installation free as a loss-leader
- **Category:** Market/competitive — **Novelty:** 3
- **Distinct from:** S-19 (a rival *undercutting the per-watt price*). Here a vertically-integrated rival (tracker maker, EPC, or module vendor) gives installation **away for free** as an attachment to sell trackers/modules/EPC services, making standalone install-as-a-service structurally unviable.
- **Attractor:** Customers stop paying for install as a line item because a bundle throws it in; Luminous's entire revenue model — charging for the install — is disintermediated.
- **Residue:** C-11 value-based pricing + C-19 kept-warm strategic options — reposition toward the bundle owners as a supplier/partner (sell the robots or the automation layer into the integrator) rather than competing with free.
- **Leans on:** The integrators would rather buy Luminous's automation than build it, and the robotics layer is sellable into a bundle.

### S-78 — Single satellite-comms provider degrades or politicises the field link
- **Category:** Technical/infrastructure — **Novelty:** 3
- **Distinct from:** S-23 (Luminous's *own* telemetry backend outage) and S-42 (physical *road* access). This is dependence on **one third-party satellite constellation** (Starlink-type) for remote-site connectivity that degrades, deprioritises, or is politically weaponised.
- **Attractor:** Remote-site machines lose their link and supervisory/dispatch capability across every site on that provider at once, throttling throughput on a dependency Luminous doesn't control.
- **Residue:** C-05 local autonomy (machines run a full shift offline) + multi-bearer comms (a second satellite or cellular fallback) so no single constellation is a fleet-wide chokepoint.
- **Leans on:** Machines operate safely disconnected and a second comms bearer can be provisioned at remote sites.

### S-79 — An edge-AI compute chip the fleet is designed around is end-of-lifed
- **Category:** Technical/infrastructure — **Novelty:** 3
- **Distinct from:** S-44 (a compute *shortage* — scarcity). This is **planned obsolescence** — the vendor discontinues/EOLs the exact edge-AI module the fleet is architected on, forcing a redesign and re-validation of the perception/motion stack.
- **Attractor:** New machines can't be built on the proven design and the existing fleet loses spares/replacement compute; a costly re-port and re-certification is forced on Luminous's timeline, not its own.
- **Residue:** C-07 design-for-substitution (`dependency_freeze_window`) applied to compute + a last-time-buy/lifecycle watch on the compute BOM so an EOL is anticipated, not discovered.
- **Leans on:** The stack can be ported to an alternate compute target within an EOL/last-time-buy window.

### S-80 — A third-party AI model / open-source license rug-pull hits the perception stack
- **Category:** Technical/infrastructure — **Novelty:** 3
- **Distinct from:** S-27 (the *key person* who owns the stack) and S-43 (a *hardware* supplier). This is a **software/IP dependency** — a licensed AI model or open-source library in the perception pipeline whose license, terms, or availability changes (relicensing, withdrawal, acquisition).
- **Attractor:** A core software component becomes legally unusable or unmaintained; the perception stack must be reworked under time pressure or ship on a non-compliant dependency.
- **Residue:** A software-BOM / license inventory + design-for-substitution on critical model/library dependencies (own-or-fork the crown-jewel components) so no external license controls the fleet.
- **Leans on:** Critical model/library dependencies can be forked or replaced without re-founding the perception stack.

### S-81 — A work-visa clampdown chokes specialist robotics hiring
- **Category:** Human/organisational — **Novelty:** 3
- **Distinct from:** S-30 (field *operator* supply) and S-31 (a *poaching raid*). This is an **inbound talent-supply policy** shock — an H-1B or Australian skilled-visa clampdown that cuts off the pipeline of specialist robotics/controls engineers Luminous hires from.
- **Attractor:** Roadmap-critical engineering roles go unfilled, R&D velocity slows, and Luminous can't staff the stack that is its moat.
- **Residue:** C-17 knowledge continuity (`runbook_as_code`) + geographic hiring flexibility (build engineering capacity across both the US and Australian entities and remote) so hiring isn't hostage to one visa regime.
- **Leans on:** Critical engineering can be staffed across jurisdictions and knowledge is captured so no single hire is irreplaceable.

### S-82 — A union corporate campaign brands Luminous "the job killer"
- **Category:** Human/organisational — **Novelty:** 3
- **Distinct from:** S-08 (a *contractual* PLA exclusion on one project) and S-33 (physical *sabotage*). This is a **coordinated reputational/political labor campaign** — a union-led corporate campaign framing Luminous as the destroyer of construction jobs, pressuring EPCs, developers, and politicians to shun it across the board.
- **Attractor:** EPCs distance themselves to avoid labor conflict, political support cools, and Luminous is frozen out of deals by association rather than by any single agreement.
- **Residue:** C-12 labor-augmentation model + proactive organized-labor engagement + C-15 crisis-comms — position the machine as up-skilling and reallocating crews (documented) rather than eliminating them, and engage labor before the campaign frames the story.
- **Leans on:** A genuine, evidenced labor-augmentation story exists and unions will engage rather than only oppose.

### S-83 ★ — A safety-system spoof makes a machine operate near a worker
- **Category:** Adversarial/abuse — **Novelty:** 5
- **Distinct from:** S-35 (ransomware — *denial*) and S-37 (remote *bricking* — denial). This is an **integrity attack that causes physical harm** — an attacker feeds falsified perception/exclusion-zone data so a machine believes its work envelope is clear and actuates near a person.
- **Attractor:** A cyber-induced injury or fatality fuses the worst cyber and safety failure modes at once — regulatory stop, criminal/liability exposure, and total loss of trust in the machine's safety case.
- **Residue:** C-04 certified safety envelope with **independent, non-networked** safe-stop (`unlock_redundancy`) + sensor-integrity/attestation on the perception path + `event_sourcing_audit_trail` so a spoof cannot override a hardwired stop and is forensically provable.
- **Leans on:** The final safe-stop is physically independent of the spoofable network path, and sensor integrity is attestable.

### S-84 — Adversarial GPS/RTK spoofing shifts placement systematically
- **Category:** Adversarial/abuse — **Novelty:** 4
- **Distinct from:** S-24 (a *natural* GPS/RTK outage or drift). This is **deliberate spoofing** — an attacker feeds false but plausible positioning so machines mis-place modules systematically across a site before anyone notices.
- **Attractor:** A whole site is installed to wrong coordinates or with cumulative misalignment, triggering rework, warranty exposure, and a quality-reputation hit that a random outage wouldn't cause.
- **Residue:** C-05 `read_only_degraded_mode` for positioning + positioning-integrity cross-checks (multi-constellation / on-machine dead-reckoning consistency) so implausible position jumps trigger a safe stop rather than confident mis-placement.
- **Leans on:** The stack can detect inconsistent/spoofed positioning and stop rather than act on it.

### S-85 — The contract manufacturer steals full design files and clones the machine
- **Category:** Adversarial/abuse — **Novelty:** 3
- **Distinct from:** S-36 (a rival *reverse-engineering a captured/leaked unit* from the outside). This is **trusted-insider theft** — the contract manufacturer, holding complete design files and BOMs, launches its own machine or supplies a rival, skipping the reverse-engineering step entirely.
- **Attractor:** A fast, faithful clone reaches market with Luminous's own drawings, collapsing the technical lead and price premium far quicker than external reverse-engineering could.
- **Residue:** C-17 IP compartmentalisation — split the build so no single manufacturer holds the crown-jewel modules; contractual + `audit_log_immutability` provenance controls; reposition the moat onto fleet data/service (per S-36).
- **Leans on:** The build can be partitioned so no one manufacturer holds enough to clone the whole machine.

### S-86 — A machine crushes a stack of the developer's delivered, uninstalled modules
- **Category:** Technical/infrastructure — **Novelty:** 3
- **Distinct from:** S-20 (latent *micro-cracks* on *installed* modules surfacing as warranty) and S-22 (a *fleet-software* error damaging installed panels). This is a **single mechanical malfunction destroying customer-owned, not-yet-installed inventory** — a pallet/stack of delivered modules crushed at once — a direct property-damage liability, not a warranty claim.
- **Attractor:** Luminous owes the developer for scrapped modules (scarce, long-lead, sometimes irreplaceable in-season), the deployment stalls waiting on replacement panels, and the customer's trust in leaving machines around their inventory drops.
- **Residue:** C-04 safety envelope extended to **material/inventory exclusion zones** + `event_sourcing_audit_trail` to scope the damage event + property-damage insurance sized to on-site module value.
- **Leans on:** Machines maintain a hard envelope around staged inventory and catastrophic material-damage is insured.

### S-87 — Surety/bonding market won't bond a hardware startup
- **Category:** Market/competitive — **Novelty:** 4
- **Distinct from:** S-56 (a *VC-round* freeze) and S-61 (a court-driven *liability-insurance* collapse). This is **surety bonding** — large EPC/developer contracts require performance bonds or parent guarantees, and the surety market won't bond a thin-balance-sheet startup, locking Luminous out of the biggest jobs before delivery risk is even in play.
- **Attractor:** Luminous is disqualified from bidding the largest, most bankable contracts — the ones that would prove the model — purely on bondability, and cedes them to better-capitalised rivals.
- **Residue:** C-19 runway/financing discipline — arrange a surety facility or collateralised bonding line as balance-sheet strengthens; structure contracts (milestone/retention) to reduce required bonding; partner with a bondable prime.
- **Leans on:** A bonding line is obtainable as the balance sheet matures, or a bondable prime will front the contract.

### S-88 — Insurers add an autonomous-equipment exclusion or exit the class
- **Category:** Supply-chain/vendor — **Novelty:** 4
- **Distinct from:** S-61 (a *court ruling* that makes cover unaffordable via an open-ended tort tail). Here there is **no legal trigger** — insurers/reinsurers simply lose appetite and add an autonomous-heavy-equipment exclusion or withdraw from the class, so Luminous (or its EPC customers for jobs using it) can't get builder's-risk/GL coverage.
- **Attractor:** Uninsured (or uninsurable) machines can't be deployed on jobsites that mandate coverage; the fleet is grounded by underwriting appetite, not by any incident or ruling.
- **Residue:** C-04 safety case as the underwriting argument + a captive/self-insured retention and reinsurance panel diversification (per S-61's residue) so coverage doesn't ride on one market's appetite.
- **Leans on:** The safety evidence supports at least one viable market or a capitalisable captive; a retention is affordable.

### S-89 — A major developer's bankruptcy leaves unpaid receivables and clawback risk
- **Category:** Time/lifecycle — **Novelty:** 3
- **Distinct from:** S-16 (largest customer *defects / doesn't renew* — a demand loss). This is **counterparty insolvency** — a developer files for bankruptcy owing Luminous for completed work, with the risk that recent payments are clawed back as preferences.
- **Attractor:** A block of earned revenue converts to an unsecured claim in a bankruptcy queue, cash already received is exposed to clawback, and Luminous's runway takes a hit it can't control.
- **Residue:** Counterparty-credit / receivables discipline — credit-check developers, milestone/progress billing so exposure never runs far ahead of cash, retention limits, and (where available) credit insurance or liens on the installed work.
- **Leans on:** Billing can stay ahead of exposure and developer creditworthiness is assessable before large receivables accrue.

### S-90 — A sharp AUD depreciation shrinks the Australian book and whipsaws the hedge
- **Category:** Market/competitive — **Novelty:** 2
- **Distinct from:** S-09/S-73 (Australian *policy* shocks). This is pure **currency risk** — an AUD slide that shrinks the AUD-denominated Australian revenue in USD terms and distorts the two-market economics independent of any policy or demand change.
- **Attractor:** The Australian book — counted on as the US hedge — is worth materially less in reporting terms, and cross-border cost/revenue mismatches erode margin unpredictably.
- **Residue:** A treasury/FX-hedging policy — natural hedging (match AUD costs to AUD revenue) plus forward cover on the net exposure so currency swings don't distort the hedge's value.
- **Leans on:** Net FX exposure is measurable and hedgeable at acceptable cost.

### S-91 — A dispute over who owns the as-built installation data blocks the data moat
- **Category:** Market/competitive — **Novelty:** 4
- **Distinct from:** S-36 (a *clone* of the machine) and S-20 (using *telemetry* to scope warranty). This is a **data-ownership/contract dispute** — the EPC, developer, or asset-owner claims the as-built data (torque, geolocation, module serials, fleet-learning signals) is theirs, blocking Luminous from using it as a moat and demanding hand-over.
- **Attractor:** The fleet-learning data advantage Luminous is repositioning its moat onto (per S-36) is contractually contested; it can't freely improve the stack from field data and may have to surrender it to customers or rivals.
- **Residue:** Data-rights terms in every contract (Luminous retains a licence to aggregate/learn from de-identified operating data) + a clear data-ownership schedule — settle the rights before deployment, not in dispute.
- **Leans on:** Customers will grant a learning-data licence as a deal term, and the value split is negotiable up front.

### S-92 ★ — A rival's autonomous robot kills a worker and the whole category is clamped
- **Category:** Regulatory/legal — **Novelty:** 5
- **Distinct from:** S-29/S-58 (a *Luminous* machine causes / is alleged to cause harm). This is **category contagion** — a *competitor's* autonomous jobsite robot kills someone, and regulators/insurers/EPCs impose a blanket moratorium on the entire autonomous-construction-machinery class, sweeping in Luminous for an incident it did not cause.
- **Attractor:** Luminous is grounded by association — a category-wide suspension it can't fix with its own safety record — losing revenue and deployments over another company's failure.
- **Residue:** C-04 + C-03 differentiated safety case (evidence that Luminous's envelope/record is distinguishable) + industry-standards engagement / trade-association safety leadership so a category clamp can be reopened for demonstrably-safer operators; C-15 crisis-comms.
- **Leans on:** Luminous's safety case is credibly *distinguishable* from the category, and a route exists to be re-permitted ahead of laggards.

### S-93 — A patent-infringement injunction grounds the fleet as the alleged infringer
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-36/S-85 (others *copying Luminous's* IP). Here **Luminous is the alleged infringer** — a competitor or non-practising entity wins a preliminary injunction on a core gripper/motion/perception patent, barring Luminous from operating or shipping pending trial.
- **Attractor:** The fleet is legally enjoined mid-season, revenue stops, and Luminous faces a forced settlement/royalty or a costly design-around under litigation pressure.
- **Residue:** A freedom-to-operate (FTO) program — clearance searches on the crown-jewel mechanisms, design-around options kept warm, and a defensive patent/prior-art position — so an infringement claim meets a prepared defence, not a scramble.
- **Leans on:** FTO was done ahead of scale and a design-around or invalidity defence exists for the core mechanisms.

### S-94 — An extreme-heat outdoor-work labor law reshapes the field-labor economics (double-edged)
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-38 (extreme heat physically *halting* machines and crews). This is a **heat-safety labor law** — a mandated ban or heavy restriction on human outdoor work above a temperature threshold. It *could* favour automation (humans barred, machines run), but Luminous still needs human supervisors/technicians on site who are equally barred, and the machines have their own thermal ceiling — a two-edged regulatory shift.
- **Attractor:** In the ambiguous case, the law strands both crews and the humans Luminous's machines depend on, and if the machines can't yet run fully unattended in heat, the promised automation tailwind fails to materialise while the labor market reprices.
- **Residue:** C-12 labor-augmentation posture repriced on the new law + a push toward higher machine-to-supervisor autonomy (per S-30) and heat-hardened unattended operation, so the law becomes a tailwind rather than a wash.
- **Leans on:** Machine autonomy and thermal design mature fast enough to operate with minimal on-site humans in heat.

### S-95 — Regional wet-season / winter dormancy idles the fleet beyond the hemispheric offset
- **Category:** Time/lifecycle — **Novelty:** 2
- **Distinct from:** S-51 (demand *concentration into a peak*) and S-55 (a *policy-deadline* cliff). This is the **trough side** — extended regional wet-season or winter dormancy where sites can't be worked and the offset US/Australian seasons don't fully fill the gap.
- **Attractor:** The fleet sits idle for months in the off-season, fixed costs run against zero throughput, and unit economics suffer from low annual utilisation.
- **Residue:** C-19 flexible-cost posture (lease/redeploy, variable staffing) + counter-seasonal geographic scheduling (per S-51) + off-season use for refurbishment/redeployment so idle months are planned, not stranded.
- **Leans on:** Fixed costs flex down in the trough and off-season time has a productive use.

### S-96 — A machine install error ignites a live-DC jobsite fire destroying a completed array section
- **Category:** Physical/environmental — **Novelty:** 3
- **Distinct from:** S-58 (a *media allegation* of a fire, true or not, causing panic) and S-20 (latent *micro-crack* degradation). This is an **actual capital-loss fire** — a machine mishandling live DC / damaged wiring ignites and destroys a completed array section, halting the site.
- **Attractor:** A real fire causes direct property loss, a site stop-work, an investigation, and a warranty/liability claim for the destroyed section — a physical-damage event, not a reputational one.
- **Residue:** C-04 safety envelope extended to **electrical/arc hazards during install** + `event_sourcing_audit_trail` to scope the event + property-damage cover; procedural sequencing so machines don't actuate on energised strings.
- **Leans on:** The machine's operating sequence avoids energised-string hazards and arc-fault conditions are detectable/stoppable.

### S-97 — A systemic hardware defect forces a full fleet recall and stand-down
- **Category:** Technical/infrastructure — **Novelty:** 3
- **Distinct from:** S-22 (a bad *software push* — recallable by rollback). This is a **physical recall** — a discovered systemic hardware safety defect (structural, gripper-retention, battery) that requires grounding and physically retrofitting the entire fleet, halting all revenue during the stand-down.
- **Attractor:** Every machine is pulled from service for a hardware fix; revenue stops fleet-wide for the recall duration and customers' schedules are disrupted at once.
- **Residue:** C-08 field-service + modular design so a retrofit is a field swap not a factory return + `event_sourcing_audit_trail` build provenance to scope the affected units + a recall-reserve so a stand-down isn't a runway event.
- **Leans on:** The defect is fixable in the field by module swap and provenance data bounds the affected population.

### S-98 — A right-to-repair / interoperability mandate forces the service moat open
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-12 (an *EPC choosing* to build automation in-house). This is a **regulatory-forced opening** — a right-to-repair or interoperability mandate requiring Luminous to publish service interfaces, parts, and diagnostics so customers or third parties can maintain the machines, eroding the service-and-uptime revenue stream.
- **Attractor:** Third parties can service the fleet, the recurring service/uptime margin Luminous's model leans on shrinks, and the moat migrates from proprietary service to something anyone can supply.
- **Residue:** C-11/C-17 moat repositioning — shift durable value onto fleet-learning data, software improvement, and throughput guarantees that an open-service rule doesn't touch; price service competitively rather than as a lock-in.
- **Leans on:** Enough of Luminous's value survives outside proprietary service (data, software, uptime SLAs) to remain a business.

### S-99 — An Australian data-residency law bars centralising as-built / geospatial data offshore
- **Category:** Regulatory/legal — **Novelty:** 4
- **Distinct from:** S-91 (*who owns* the data) and S-23 (a telemetry *outage*). This is **data-residency/sovereignty regulation** — an Australian law requiring as-built and high-resolution geospatial data to remain in-country, conflicting with Luminous's centralised fleet-learning cloud.
- **Attractor:** Luminous can't legally pool Australian field data into its global learning loop or must stand up separate in-country infrastructure, fragmenting the data moat and raising cost.
- **Residue:** Regional data-architecture (in-country storage with de-identified/aggregated cross-border learning where permitted) + a data-residency compliance posture designed in, so the fleet-learning loop degrades gracefully rather than breaking.
- **Leans on:** The learning loop can run on de-identified/aggregated data that residency rules permit to cross borders.

### S-100 — A pandemic / biosecurity restriction stalls both deployment and manufacturing
- **Category:** Physical/environmental — **Novelty:** 2
- **Distinct from:** S-38 (extreme *heat*) and S-28 (technician *scarcity*). This is a **biosecurity/travel-and-workforce** shock — a pandemic or biosecurity lockdown that simultaneously restricts field crews traveling to remote sites and halts contract-manufacturing of machines.
- **Attractor:** Deployment and fleet build stall at once; the season's installs slip and the pipeline of new machines dries up on a shock that hits both ends of the value chain.
- **Residue:** C-05 local autonomy (fewer humans needed on site) + C-07 supply-chain resilience (multi-source, buffer stock) so a workforce/travel shock degrades throughput rather than stopping it.
- **Leans on:** Machines run with minimal on-site humans and buffered supply bridges a manufacturing pause.

---

### Completeness-pass closing note

**36 new stressors added: S-65…S-100.** Categories added to: Regulatory/legal ×15 (S-65, S-66, S-67, S-68, S-69, S-70, S-71, S-72, S-73, S-92, S-93, S-94, S-98, S-99), Market/competitive ×6 (S-74, S-75, S-77, S-87, S-90, S-91), Supply-chain/vendor ×2 (S-76, S-88), Technical/infrastructure ×4 (S-78, S-79, S-80, S-97), Human/organisational ×2 (S-81, S-82), Adversarial/abuse ×3 (S-83, S-84, S-85), Physical/environmental ×2 (S-96, S-100), Time/lifecycle ×2 (S-89, S-95), plus S-86 (Technical). Two new black swans (★): S-83 (spoof-to-harm) and S-92 (category contagion), with S-93 a near-swan.

**Fold into the existing C-01…C-19 portfolio (no new control needed):**
- **C-01 demand diversification** absorbs S-65, S-66, S-70(partly), S-73, S-75 — the new *upstream demand-kill* mechanisms (interconnection, permitting, tax-equity, correlated Australian policy) are new *stressors* but the same *residue*. Their arrival **reinforces** the §5 finding that the whole revenue side rides one assumption, and shows C-01 must now hedge against *correlated* policy retreat (S-73) and grid-access/finance-close gating, not just credit and tariffs.
- **C-04 safety envelope** stretches to cover S-83, S-86, S-96 (material/electrical exclusion zones and an integrity-resistant independent safe-stop) — a scope extension, not a new control.
- **C-05, C-07, C-08, C-11, C-12, C-17, C-18, C-19** each pick up several new stressors within their existing remit (see cards): C-05 (S-78, S-84, S-100), C-07 (S-76, S-79, S-100), C-08 (S-97), C-11 (S-74, S-77, S-98), C-12 (S-67, S-82, S-94), C-17 (S-80, S-81, S-85, S-98), C-18 (S-69, S-70), C-19 (S-75, S-87, S-95).

**Genuinely new control surfaces this pass surfaces (candidate C-20…C-26 — not in the original portfolio):**
- **Treasury / FX hedging** (S-90) — no financial-markets control existed; the two-market model carries a currency exposure the first pass didn't name.
- **Counterparty-credit & receivables discipline** (S-89) — milestone billing, credit checks, liens/credit insurance; distinct from the *demand*-loss control C-10.
- **Surety / bonding facility** (S-87) — bondability as a *bid prerequisite* is a financing surface neither C-19 (runway) nor C-04 (insurance) covers directly.
- **Trade / export-controls & customs compliance** (S-68, S-71, S-72) — a trade-compliance function governing tech-transfer, machine classification, and DG transport; only partly touched by C-13.
- **Data-rights & data-residency architecture** (S-91, S-99) — contractual data-ownership terms plus regional data architecture protecting the fleet-learning moat; distinct from C-03 (which is about *capturing* evidence, not *owning/localising* it).
- **Freedom-to-operate / IP-defence** (S-93) — the mirror of C-17: C-17 protects Luminous's *own* IP; nothing defended against Luminous being the *alleged infringer*.
- **Industry-standards / category-safety leadership** (S-92) — proactive standards-body engagement so a category-wide clamp can be reopened for a demonstrably-safer operator; a new institutional surface beyond C-15 crisis-comms.

**Regime verdict — does Step 6 still hold? Yes, and the completeness pass reinforces it rather than moving it.** The verdict remains **edge of chaos, tilting chaotic**, on the same three axes. The new stressors deepen exactly the couplings §5 already named: (1) the *upstream demand-concentration* coupling gains several new failure modes (interconnection S-65, permitting S-66, tax-equity S-75, correlated Australian policy S-73) that all fail C-01 the same way — the single most brittle coupling is now demonstrably even more multiply-triggered; (2) the *single-event safety* coupling gets worse with S-83 (cyber-induced harm) and S-92 (harmed by a *rival's* incident), extending the existential trigger beyond Luminous's own control; and (3) the *runway/financial-fragility* clock gains genuinely new surfaces — FX (S-90), receivables (S-89), and bonding (S-87) — that the first pass under-weighted, arguing the financial-fragility axis deserves equal billing with demand-concentration and safety in the §6 deltas. No new stressor contradicts the verdict or reveals an orphan control; the finding is that the *financial-controls* corner of the portfolio (treasury, credit, bonding, trade-compliance) is the thinnest genuinely-new surface and the natural target for the next control-build.

**Exhaustion judgement:** after this pass the Luminous stressor space is **close to exhausted at the level of distinct mechanisms** — the remaining unlisted events are mostly *recombinations* of the ~100 mechanisms now on the board (e.g. two shocks arriving together) rather than new mechanisms, which is the point at which further enumeration yields correlations to analyse in §5 rather than new cards.

---

*Completeness pass total: +36 stressors (S-65…S-100), 9/9 categories, +2 black swans. Grand total: 100 stressors (S-01…S-100), 9 black swans. Method per `residuality-enterprise-risk-management.md`; catalogue controls per `residuality/references/residue_library.md`.*
