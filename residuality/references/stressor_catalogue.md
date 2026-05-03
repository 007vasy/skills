# Stressor catalogue

A stocked list of stressor archetypes. Use it for inspiration, not for copy-paste. Every stressor in a real run should be re-cast in the user's specific business and tech context. Diversity rules and minimum counts are enforced by `scripts/stressor_diversity_check.py` against `assets/stressor_categories.json`.

## Diversity rules (enforced)

- Hit every category floor in `assets/stressor_categories.json` (current floors: regulatory 2, market 1, tech 2, human 2, adversarial 2, environmental 1, supply-chain 1, scale 2, time 1 — total minimum **14**).
- Generate **≥30 stressors** for a serious analysis. Below 30 the contagion matrix and criticality estimate are unreliable.
- Average `novelty` ≥ 3.0 across the list. `novelty=1` is "every architect has seen this"; `novelty=5` is "this would not appear in any standard risk register".
- Include **≥3 black-swan / absurd** stressors (`novelty=5`). They are where the theory earns its keep.
- No stressor described purely in tech terms. Always include the business consequence ("payment processor down → we cannot accept new charging sessions and customers leave for the rival station 200m away").

## Categories and archetypes

### Regulatory / legal (floor 2)

- New data-residency rule forces a region split mid-quarter.
- GDPR data-subject deletion request arrives mid-transaction.
- Regulator mandates a new billing model (per-minute instead of per-kWh).
- Export-control reclassification of a dependency.
- Court order to retain data the system was designed to delete.
- Tax authority demands per-line-item invoice with previously unrecorded fields.
- Sanctions list change blocks an existing customer overnight.

### Market / competitive (floor 1)

- Competitor launches at half the price.
- A celebrity mentions the product, demand 50× for 6 hours.
- Incumbent acquires your sole supplier of a critical component.
- New entrant copies the API surface and offers it free.
- Reviewer publishes a comparison that misrepresents a feature; support volume 10×.
- Currency collapse in a top market.

### Technical / infrastructure (floor 2)

- Cloud region outage during a regional sales peak.
- Noisy-neighbour CPU starvation on the multi-tenant DB.
- Language runtime CVE forces an emergency upgrade.
- Schema migration deadlocks behind a long-running transaction.
- DNS provider outage.
- Certificate auto-renewal silently fails the day before expiry.
- Cache stampede after a deploy invalidates the warm set.
- Clock skew across zones breaks monotonic ordering assumptions.

### Human / organisational (floor 2)

- Operator runs the wrong script in production.
- Key engineer leaves; nobody else has touched module X in 18 months.
- Support team cannot reproduce a defect that affects 0.3% of users.
- On-call paged at 3 a.m. misreads runbook step 4.
- Hand-off between teams loses context for an in-flight incident.
- New hire ships a feature that violates a tacit invariant nobody documented.
- A team-wide morale dip during a re-org means deferred upgrades pile up.

### Adversarial / abuse (floor 2)

- Credential stuffing campaign matches 0.1% of accounts.
- Fraudulent identity unlock attempt at a charging station / kiosk.
- Social-engineered support agent issues a refund + access reset.
- Supply-chain dependency takeover (open-source maintainer hands keys to bad actor).
- API scraping operator rebuilds your product on top of your free tier.
- Coordinated review-bombing attached to a fake outage claim.
- Rate-limit-evading distributed bot army.
- Insider threat: ex-employee with stale credentials.

### Physical / environmental (floor 1)

- Sub-zero temperature outside operating range of a deployed device.
- Vandalism with foreign object (the GOTO talk's *meat in the charger* example).
- Lightning strike on the cellular tower serving a remote site.
- Flooding takes out a regional data centre.
- Sticker / QR / label peels off in rain.
- Dust ingress kills a fan in a kiosk.
- ICE vehicle blocks an EV charger; the system has no way to learn this.

### Supply chain / vendor (floor 1)

- Payment processor down for 90 minutes.
- SaaS vendor 10× pricing with 30 days notice.
- Open-source maintainer abandons project; CVE arrives 6 months later.
- Single-source hardware component on 26-week lead time.
- Cloud provider deprecates an API you depend on.
- Identity provider revokes a contract over policy disagreement.

### Scale / load (floor 2)

- Queue contention at peak: producers outpace consumers by 3×.
- One tenant 100× larger than the median tenant.
- Long-tail latency tail blows the p99 SLO.
- Fan-out blowup: one event fans into 10k async jobs that fan into 100k each.
- Search index rebuild takes a week instead of an hour at current data size.
- Aggregation that was O(n) in v1 became O(n²) by year three.
- Webhook target slows down; back-pressure cascades upstream.

### Time / lifecycle (floor 1)

- Leap second event.
- DST transition produces ambiguous timestamps.
- Five years of data accretion makes a once-fast query unviable.
- Domain expires because the renewal email went to a former employee.
- A "temporary" feature flag is still on after 3 years and now nobody knows what it does.
- Token rotation policy change cascades into a fleet-wide re-auth at 09:00 Monday.

## Black-swan / absurd seeds

Use these as inspiration for the mandatory ≥3 black swans. The point is to break tech-only thinking.

- A national news segment alleges a safety issue in your product, true or not.
- The CEO is briefly hospitalised the morning of a fundraise.
- A geopolitical event closes the cloud region you rely on overnight.
- A viral TikTok shows people abusing a feature in a way you never imagined.
- Someone publishes a paper proving your encryption choice has a known weakness.
- A competitor's outage drives 20× sign-ups in 6 hours.
- A government announces an immediate ban on a category your product depends on.

## How to use this file

When the brainstorm prompt fires (see `references/prompt_templates.md`):

1. Generate stressors freely first, in the user's domain.
2. Map each generated stressor to a category from `assets/stressor_categories.json`.
3. Check floors. Where you are short, scan this catalogue for an inspiration in that category and re-cast it for the user's domain — never copy verbatim.
4. Include ≥3 black swans drawn or adapted from the seeds above.
5. Run `scripts/stressor_diversity_check.py` on the JSON list. Address any `missing_categories` or `boring_score` warnings before moving to attractor derivation.
