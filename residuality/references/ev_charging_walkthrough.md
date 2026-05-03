# EV charging — full worked walkthrough

This is the canonical worked example. It mirrors the EV charging case study from Barry O'Reilly's GOTO Copenhagen 2025 talk (the EV section starts ~29:06 and contagion ~38:39). Use this file as:

1. A learning artefact when first onboarding to the skill.
2. A **gold reference**: when the verification script runs the skill end-to-end against the same inputs, it should produce a report whose residues, hotspots, and criticality regime match the ones below within reasonable variance.

## Project context

A pan-European EV charging network operator. Owns physical charge points at supermarkets, petrol stations, motorway service areas. Drivers approach a charger, identify themselves, unlock the cable, charge, get billed, leave.

## Naive architecture

**Summary.** The driver opens our app, scans the QR sticker on the charger, the app authenticates with our cloud, the cloud confirms identity to the charger, the charger unlocks, the cable is plugged in, billing meters per-kWh, charging stops on user request or cable unplug, payment posts to the user's saved card.

**Components**
| id | name | kind | tech assumption (only if confirmed) |
|---|---|---|---|
| C01 | Driver | human | — |
| C02 | EV vehicle | device | — |
| C03 | Mobile app (iOS/Android) | client | — |
| C04 | QR sticker on charger | edge | physical, weather-exposed |
| C05 | Charger device | device | firmware over cellular |
| C06 | Charger Service (cloud) | service | — |
| C07 | Identity Service (cloud) | service | — |
| C08 | Billing Service (cloud) | service | per-kWh metering |
| C09 | Sessions DB | datastore | Postgres |
| C10 | Payment Processor | external | third-party |
| C11 | Cellular network at site | external | — |

**Edges**
- C01 →(human)→ C03 (uses app)
- C03 →(sync)→ C07 (authenticate)
- C03 →(sync)→ C06 (request unlock with QR-derived charger id)
- C06 →(sync via C11)→ C05 (unlock command)
- C05 →(device)→ C02 (cable engages)
- C05 →(async via C11)→ C06 (charging telemetry, kWh ticks)
- C06 →(data)→ C09 (session writes)
- C08 →(sync)→ C10 (charge card)

**Business context.** Win the moment the driver pulls in. Time-to-unlock is the metric drivers care about. Drivers will defect to a competitor 200m away if our charger doesn't unlock within ~2 minutes.

**Assumptions (the naive arch quietly relies on these)**
- Driver has a smartphone with our app installed.
- Cellular coverage at every site, both for app and for charger telemetry.
- The QR sticker is intact and scannable.
- The payment processor is up.
- No regulator changes the billing dimension.
- Our cloud is reachable from the charger.
- The cable physically engages and disengages on command.

## `user_stack_facts[]`

```
- Postgres 14
- Kotlin services on JVM, Spring Boot
- AWS eu-west-1, eu-central-1
- Stripe for card processing
- MQTT over TLS for charger telemetry
- iOS + Android clients in Kotlin/Swift native
- We do NOT have a message broker today
- We do NOT have multi-region active-active
```

## Stressors (32, all 9 categories met)

(IDs assigned in generation order; categories shown.)

| id | category | name (short) | novelty | one-liner |
|---|---|---|---:|---|
| S01 | tech | Cloud region outage during commuter peak | 2 | Region we run in goes down at 18:00; chargers can't get unlock commands; queues form; drivers leave |
| S02 | environmental | QR sticker peels off after 9 months in rain | 4 | Driver can't initiate session; abandons; loss of revenue + reputation |
| S03 | environmental | Vandalism — meat shoved into charge port | 5 | Charger thinks cable is engaged, won't release, blocked from service for hours |
| S04 | regulatory | Regulator mandates per-minute billing as anti-loitering measure | 4 | Our entire billing stack is per-kWh; switch must happen in 90 days |
| S05 | adversarial | Driver tampers with cellular antenna to get free charge | 5 | Charger loses telemetry mid-session; we can't bill; loss + investigation |
| S06 | supply-chain | Stripe outage 90 minutes during Friday evening peak | 3 | We can't authorise cards; drivers stranded |
| S07 | tech | Cellular outage at a single site | 2 | Charger isolated; can't unlock new sessions; in-progress sessions lose telemetry |
| S08 | human | Driver has a feature phone (no app) | 3 | Cannot authenticate; can't charge; loss + reputation in older demographic |
| S09 | tech | Charger firmware bricks after a bad OTA update | 4 | Single charger out of service; rollout halted; investigation overhead |
| S10 | human | New regulator-mandated tariff requires support team to handle disputes | 3 | Support volume 5×; chargebacks |
| S11 | adversarial | Credential stuffing campaign matches 0.3% of accounts | 3 | Free charges via compromised accounts; reputational damage |
| S12 | scale | Holiday weekend, 4× normal session count | 2 | Queues form; some chargers throttle; long-tail latency on unlock |
| S13 | adversarial | Coordinated booking-bot attack reserves chargers without using them | 4 | Real drivers can't use chargers; revenue collapse on key sites |
| S14 | regulatory | GDPR data-subject deletion request mid-charging-session | 4 | Data we need to bill is being legally erased; how do we close out the session? |
| S15 | environmental | Lightning strike on cellular tower at remote site | 3 | All chargers at site offline; isolated for hours |
| S16 | environmental | -30°C in Norway: lithium battery refuses charge | 4 | Charger reports session failed though OK; driver charged for nothing |
| S17 | tech | Database deadlock under burst write from telemetry | 3 | Sessions can't close; bills can't post; user surface stale |
| S18 | scale | One large fleet customer = 60% of all sessions, asks for SLA | 3 | One tenant noisy; risk to all others |
| S19 | adversarial | ICE driver parks in EV charging bay | 4 | Charger physically blocked; we have no signal of this; revenue loss |
| S20 | market | Competitor drops to half price overnight at our top sites | 3 | Sessions migrate; we need a response |
| S21 | supply-chain | Charger hardware vendor goes bankrupt | 4 | No more spare parts; firmware support frozen |
| S22 | time | DST transition produces ambiguous session timestamps | 4 | Two sessions appear to overlap; billing dispute |
| S23 | tech | Stripe webhook retries flood our endpoint after a brief outage | 3 | Duplicate charge posts; we double-charge users |
| S24 | scale | Long-tail driver: charges once a year, payment method expired | 2 | Session starts then fails to bill; no reconciliation |
| S25 | human | On-call engineer accidentally deploys staging certs to prod | 3 | Charger TLS handshake fails fleetwide |
| S26 | regulatory | New national requirement to publish real-time charger availability via standard API | 3 | We don't have an availability API; mandate comes with deadline |
| S27 | adversarial | Driver disputes charge claiming "wasn't me, app was hacked" | 3 | We can't prove session attribution; refund forced; no investigation trail |
| S28 | scale | Search for available chargers on the app blows DB query budget at scale | 3 | App degrades; users can't find chargers nearby |
| S29 | time | Card auto-renewal across millions of users hits same Tuesday morning | 3 | Stripe API rate-limits; sessions can't authorise |
| S30 | supply-chain | Mobile OS update breaks our QR scanner library overnight | 3 | App can't scan; users can't initiate sessions |
| S31 | environmental | Snow covers the screen and QR | 4 | Driver can't see anything; can't initiate; abandons |
| S32 | human | Driver is visually impaired; QR-scan UX impossible | 4 | Cannot use product; ADA / accessibility risk |

Diversity check: regulatory 4, market 1, tech 6, human 4, adversarial 6, environmental 5, supply-chain 3, scale 4, time 2. **All floors met.** Black-swans (novelty 5): S03, S05. Sub-five-novelty stressors fill the rest. Average novelty ≈ 3.3.

> **Note** that the gold list has only 2 novelty-5 stressors (S03, S05) — slightly below the ≥3 floor; in a real run the brainstorm prompt would push for one more. The diversity checker would surface this, and the user could either accept (justified by domain) or generate an additional black-swan.

## Per-stressor attractors and residues (representative subset)

(Showing 12 representative pairs; the full run produces all 32.)

| stressor | attractor (1 line) | residue (id, name) | source pattern |
|---|---|---|---|
| S01 cloud outage | drivers stranded; defection to competitor | R01 Local autonomy: charger holds last-known auth + per-charger budget for N hours | `local_autonomy` |
| S02 QR peeled | driver can't initiate; abandons | R02 Camera + ALPR fallback identity: secondary identity channel | `alpr_camera_fallback_identity` |
| S03 meat in port | port locked indefinitely | R03 Unlock redundancy: secondary release path with attendant override + audit | `unlock_redundancy` |
| S04 per-minute billing mandated | full re-architecture pressure | R04 Dual-dimension session log + parameterised billing | `per_minute_billing_path` |
| S05 cellular tampering | mid-session telemetry lost; can't bill | R05 Session observability with periodic signed receipts; flag gaps | `charge_session_observability` |
| S06 Stripe down | cannot authorise; drivers stranded | R06 Outbox + async reconciliation: charge intent stored, settled when Stripe returns | `outbox_with_async_reconciliation` |
| S07 cell outage at site | charger isolated | (covered by R01) | `local_autonomy` |
| S09 firmware brick | single charger dead | R07 Progressive rollout: deploy firmware to 1% → 10% → 100% with auto-abort | `progressive_rollout` |
| S11 credential stuffing | free charges; reputation hit | R08 Per-tenant quota + adversarial signal feed; throttle on anomalies | `per_tenant_quota` |
| S12 holiday peak | unlock queue grows; tail latency blows SLO | R09 Backpressure on unlock requests; surface "wait 30s" UX | `backpressure` |
| S13 booking bots | real drivers locked out | R10 Idempotent reservations with abuse signals; cancel after no-show | `idempotent_replay` (with signal layer) |
| S14 GDPR mid-session | data being erased while we still need it | R11 Session events sealed at start; deletion deferred to post-settlement window | `event_sourcing_audit_trail` |
| S19 ICE blocking | bay unavailable; we don't know | R12 Camera-based occupancy sensing → expose via availability API | `alpr_camera_fallback_identity` (extended) |
| S22 DST | ambiguous timestamps | R13 Always store wall-clock + UTC + timezone-id on session events | `audit_log_immutability` |
| S23 webhook flood | duplicate charges | R14 Idempotent Stripe receipt processing keyed on event id | `idempotent_replay` |
| S26 availability API mandate | regulatory deadline | R15 Public read-API derived from internal session/availability state | (novel — no library pattern) |
| S27 dispute | no proof | (covered by R05 + R11 + R13) | — |
| S29 card-renewal Tuesday | rate-limited; sessions fail | R16 Backoff + jitter on bulk renewals; pre-warm before peak | `backpressure` |

## Residue stack (after dedupe)

The 32 stressors collapse to ~14 deduped residues:

1. R01 — Local autonomy (covers S01, S07, S15)
2. R02 — Camera/ALPR fallback identity (covers S02, S08, S30, S31, S32)
3. R03 — Unlock redundancy (covers S03)
4. R04 — Per-minute billing path (covers S04)
5. R05 — Charge-session observability (covers S05, S22, S27, partial S11)
6. R06 — Outbox + async reconciliation (covers S06, S23, S29, partial S17)
7. R07 — Progressive rollout (covers S09, S25)
8. R08 — Per-tenant quota + adversarial signals (covers S11, S13, S18)
9. R09 — Backpressure (covers S12, S29)
10. R10 — Reservation abuse handling (covers S13)
11. R11 — Audit-log immutability + event sourcing (covers S14, S27)
12. R12 — Camera occupancy sensing (covers S19)
13. R14 — Idempotent webhook processing (covers S23)
14. R15 — Public availability API (covers S26)

Residue load (top 3):
- R02 ALPR fallback: 5 stressors
- R06 Outbox + async reconciliation: 4 stressors
- R05 Session observability: 4 stressors

## Contagion (key findings)

**3-bullet narrative:**
- **Most-loaded residue:** R02 (ALPR fallback) addresses 5 stressors; if its image-recognition accuracy drops, all five surfaces degrade together.
- **Most brittle coupling:** R06 (outbox) ↔ R14 (idempotent webhook) — both rely on Stripe event semantics; a Stripe API change breaks both at once.
- **Lowest-coverage stressor:** S04 (per-minute billing) — only R04 addresses it; if R04's parameterisation is incomplete, no fallback exists.

**Hotspots:** R02, R06, R05 (top quartile by load × brittleness).

**Brittleness rank (top 5):**
1. R06 ↔ R14 (Stripe event semantics shared)
2. R01 ↔ R03 (both rely on charger-side state surviving cell outage)
3. R02 ↔ R12 (both depend on the same camera hardware)
4. R09 ↔ R16 (both forms of backpressure share the same throttle bucket — risk of double-counting)
5. R08 ↔ R10 (both rely on the same anomaly signal source)

## Criticality

- **N** = 11 components
- **K** ≈ 2.8 (after residues; before, K ≈ 1.6 = frozen)
- **P** ≈ 0.34 (regulatory residues + stated assumptions push it up)
- **Regime: edge of chaos** — adaptive, but R02 and R06 are doing too much. One incident in either has wide blast radius.

**Suggested deltas:**
- Decouple R02 and R12 by allowing the camera channel to be served by either of two camera SKUs (raise N by 1, slightly reduce K on the camera node).
- Introduce a thin abstraction between Stripe and the outbox so a Stripe contract change only forces R14 changes, not R06.

## What this gold reference is for

The verification step in `workflow_analyze.md` (and the test plan in the project plan) should run the skill end-to-end with the same naive architecture and expect:

- All 9 stressor categories met.
- ALPR fallback, per-minute billing, circuit-breakers / local autonomy, charge-session observability, unlock redundancy, async-reconciliation outbox **all** appear in the residue stack.
- ALPR fallback, outbox, and observability appear in `hotspots[]`.
- Criticality regime is `edge`, with N in 8-14 and K in 2-4.

If a real run misses any of these, investigate before declaring success.
