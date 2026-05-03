# Residue library

A library of named, minimal residue patterns. **Reach for one of these before inventing.** Each entry has a stable `id` (used as `source_pattern` in the state file), a one-line intent, applicability hints, the minimal-form description, what it commonly *does not* do, an estimated cost band, and typical contagion neighbours (other residues it tends to share components or assumptions with).

If a residue you need is not in this library, you may add a novel one — but it must still be minimal, cite a `user_stack_facts` entry, and address ≥1 stressor.

## Format

```
### <ID> — <Name>
- Intent: ...
- Applies when: ...
- Minimal form: ...
- Does NOT: ...
- Cost: low | med | high
- Common couplings: <other ids>
```

---

### `circuit_breaker_fallback_cache` — Circuit breaker with fallback cache
- Intent: When a downstream dependency degrades, fail fast and serve a stale-but-correct response from a local cache rather than cascading the failure.
- Applies when: Read paths exist whose data is acceptable to serve slightly stale during partner outages (catalog reads, pricing snapshots, identity lookups).
- Minimal form: Wrap the call site in a circuit breaker; on `OPEN`, return last-good cached value with a `stale: true` marker. No new caching layer if one already exists.
- Does NOT: Replace the dependency, add multi-region redundancy, or hide failures from observability.
- Cost: low
- Common couplings: `read_only_degraded_mode`, `bulkhead`

### `outbox_with_async_reconciliation` — Outbox + async reconciliation
- Intent: Survive downstream-write failures (payment processor, partner API) without data loss.
- Applies when: A user-visible action causes a write to an external system that can fail or be slow.
- Minimal form: Persist the intent to a local outbox table in the same transaction as the user-visible state change; a worker drains the outbox with retries and idempotency keys; reconciliation job catches drift.
- Does NOT: Require a new message broker if the database can serve as the queue.
- Cost: low
- Common couplings: `idempotent_replay`, `dead_letter_quarantine`

### `idempotent_replay` — Idempotent replay
- Intent: Tolerate duplicate or retried operations without producing duplicate effects.
- Applies when: Any external integration that may double-deliver, any retry loop, any worker that may crash mid-job.
- Minimal form: Every mutation accepts an idempotency key; the receiving side records `(key, result)` and returns the recorded result on retry.
- Does NOT: Add distributed locking or global ordering.
- Cost: low
- Common couplings: `outbox_with_async_reconciliation`, `dead_letter_quarantine`

### `dead_letter_quarantine` — Dead-letter quarantine
- Intent: Stop poison messages from blocking a queue and surface them for human review.
- Applies when: Any async worker, any message bus.
- Minimal form: After N retries with exponential backoff, move the message to a dead-letter store with full context; alert on rate, not on each item.
- Does NOT: Auto-fix the underlying error.
- Cost: low
- Common couplings: `idempotent_replay`, `bulkhead`

### `bulkhead` — Bulkhead
- Intent: Isolate failure of one tenant / route / dependency from the rest.
- Applies when: A single noisy tenant or slow dependency can starve resources for everyone (thread pool exhaustion, connection saturation).
- Minimal form: Allocate per-tenant or per-dependency resource pools (threads, connections, rate-limit buckets) so saturation in one cannot drain the others.
- Does NOT: Solve the slow-dependency problem; only contains it.
- Cost: med
- Common couplings: `per_tenant_quota`, `backpressure`

### `read_only_degraded_mode` — Read-only degraded mode
- Intent: Keep the system useful for reads when writes cannot be serviced safely.
- Applies when: Write-path dependency fails (DB primary down, payment processor down) but reads are still safe and valuable.
- Minimal form: A feature-flagged degraded mode disables writes, surfaces a banner to users, queues intents for replay when writes return.
- Does NOT: Require a separate read-only deployment.
- Cost: low
- Common couplings: `circuit_breaker_fallback_cache`, `outbox_with_async_reconciliation`

### `backpressure` — Backpressure
- Intent: Prevent a slow downstream from causing unbounded queue growth and OOM upstream.
- Applies when: Any producer/consumer pair where the producer can outpace the consumer (webhooks, async jobs, ingest pipelines).
- Minimal form: Bounded queue + producer-side rejection or shedding when over watermark; surface the shed in metrics, not silently.
- Does NOT: Fix the slow consumer.
- Cost: low
- Common couplings: `bulkhead`, `dead_letter_quarantine`

### `per_tenant_quota` — Per-tenant quota
- Intent: Stop one customer from consuming the cluster.
- Applies when: Multi-tenant systems where tenant size varies by orders of magnitude.
- Minimal form: Enforce per-tenant rate and resource limits; expose usage to the tenant; fail with a clear error, not silent throttling.
- Does NOT: Replace pricing or commercial conversation.
- Cost: med
- Common couplings: `bulkhead`, `backpressure`

### `shadow_traffic` — Shadow traffic
- Intent: Validate a new path against production load without serving the result.
- Applies when: Replacing a critical component, changing a critical model, migrating a query.
- Minimal form: Mirror live requests to the new path; compare results; do not return them. Sample to keep cost bounded.
- Does NOT: Replace integration tests.
- Cost: med
- Common couplings: none typical.

### `event_sourcing_audit_trail` — Event sourcing audit trail
- Intent: Reconstruct any past state for forensics, regulatory, or dispute resolution.
- Applies when: Disputes, fraud investigations, regulator demands a transaction history.
- Minimal form: Append immutable events to a log alongside the canonical store; read model derives current state. Where event sourcing is too heavy, an append-only audit table suffices.
- Does NOT: Replace the canonical store unless the team is committed.
- Cost: med
- Common couplings: `idempotent_replay`, `outbox_with_async_reconciliation`

### `local_autonomy` — Local autonomy with eventual sync
- Intent: Keep edge devices working when the central control plane is unreachable.
- Applies when: Devices in the field with intermittent connectivity (chargers, kiosks, on-prem agents).
- Minimal form: Edge holds enough state and policy to operate alone for N hours; syncs deltas when connectivity returns; conflict resolution policy is explicit.
- Does NOT: Eliminate the central plane.
- Cost: high
- Common couplings: `outbox_with_async_reconciliation`, `read_only_degraded_mode`

### `alpr_camera_fallback_identity` — Camera / ALPR fallback identity
- Intent: Authenticate / identify when the primary channel (QR code, app, key fob) is unavailable.
- Applies when: Physical kiosks where the primary identity channel can vandalise, peel off, or be unavailable to the user.
- Minimal form: Add a secondary identity channel (camera + plate recognition, NFC, attendant override) that triggers a slower path with a manual reconciliation step.
- Does NOT: Replace the primary channel.
- Cost: med
- Common couplings: `event_sourcing_audit_trail`, `unlock_redundancy`

### `unlock_redundancy` — Unlock redundancy
- Intent: Survive a single point of failure in the unlock / dispense / actuation path.
- Applies when: Physical actuators (charger cable release, locker, gate) where a single firmware/hardware path failure strands users.
- Minimal form: Two independent unlock paths (e.g., normal cloud-driven + local NFC fallback + attendant remote override). Audit logs every override.
- Does NOT: Replace the firmware.
- Cost: med
- Common couplings: `local_autonomy`, `event_sourcing_audit_trail`

### `per_minute_billing_path` — Alternative billing path
- Intent: Survive a regulator or market change that mandates a different billing model.
- Applies when: Billing currently uses a single dimension (per-kWh, per-token, per-call) and external pressure may require another (per-minute, per-session, per-user-flat).
- Minimal form: Record both dimensions on every transaction; switch the billed dimension via configuration. Reconciliation tooling for transitions.
- Does NOT: Build a full billing engine if the existing one can be parameterised.
- Cost: med
- Common couplings: `event_sourcing_audit_trail`, `outbox_with_async_reconciliation`

### `charge_session_observability` — Domain-event observability
- Intent: Investigate disputes and abuse without re-instrumenting under pressure.
- Applies when: Long-lived business processes (charge sessions, multi-step transactions, user journeys) where partial failures are common.
- Minimal form: Emit structured domain events at every state transition with stable IDs; retain for the dispute window; correlate across services.
- Does NOT: Replace operational metrics or traces.
- Cost: low
- Common couplings: `event_sourcing_audit_trail`, `alpr_camera_fallback_identity`

### `feature_flag_kill_switch` — Feature flag kill switch
- Intent: Disable a misbehaving code path without a deploy.
- Applies when: Any new or risky code path; any third-party integration that may degrade.
- Minimal form: A boolean flag at the entry of the path, default-on, with a documented rollback runbook; the flag's existence is the residue, not a flag-management platform.
- Does NOT: Become a long-lived branching mechanism (see watchout: `time/lifecycle` flag rot).
- Cost: low
- Common couplings: `read_only_degraded_mode`

### `key_rotation_dual_accept` — Dual-accept key rotation
- Intent: Survive an emergency credential / cert / key rotation without downtime.
- Applies when: Any system whose secrets must be rotatable on short notice.
- Minimal form: Verifier accepts old + new keys for a defined overlap window; rotation tool publishes new key, waits, then revokes old.
- Does NOT: Replace your secret-management system.
- Cost: low
- Common couplings: none typical.

### `query_capacity_guard` — Query capacity guard
- Intent: Stop a single expensive query from taking down the database for everyone.
- Applies when: User-facing systems with ad-hoc query surfaces (search, analytics) over shared databases.
- Minimal form: Per-query budgets (rows scanned, time, memory); kill on exceed; surface the shed clearly to the user.
- Does NOT: Replace query optimisation.
- Cost: low
- Common couplings: `bulkhead`, `per_tenant_quota`

### `audit_log_immutability` — Audit-log immutability
- Intent: Resist tampering and meet regulatory retention requirements.
- Applies when: Regulated domains (finance, health, energy) and any system where insider threat is in scope.
- Minimal form: Append-only audit table with row-level WORM enforcement (DB feature or external store); periodic integrity hash chain.
- Does NOT: Replace the operational logging stack.
- Cost: med
- Common couplings: `event_sourcing_audit_trail`

### `manual_override_with_review` — Manual override with mandatory review
- Intent: Allow a human to break the rules in a true emergency without making "break the rules" the norm.
- Applies when: Any policy-enforced flow that may need exception handling (refunds, account reactivations, charger force-unlock).
- Minimal form: A break-glass UI guarded by 2-person approval and a mandatory post-hoc review queue.
- Does NOT: Replace the policy itself.
- Cost: low
- Common couplings: `audit_log_immutability`, `event_sourcing_audit_trail`

### `tenant_isolated_blast_radius` — Tenant isolation
- Intent: Stop a tenant-specific defect or attack from contaminating other tenants' data.
- Applies when: Multi-tenant systems with shared storage or shared identity.
- Minimal form: Tenant ID is mandatory at every storage and queue boundary; row-level security at the DB; per-tenant encryption keys for sensitive fields.
- Does NOT: Move to physical isolation.
- Cost: med
- Common couplings: `bulkhead`, `per_tenant_quota`

### `progressive_rollout` — Progressive rollout
- Intent: Catch deploy-induced regressions before they reach all users.
- Applies when: Any deploy that changes user-visible behaviour or load shape.
- Minimal form: Deploy to 1% → 10% → 100% with automated abort on health-metric regression; canary watches a fixed dashboard.
- Does NOT: Replace integration tests.
- Cost: med
- Common couplings: `feature_flag_kill_switch`

### `dependency_freeze_window` — Dependency freeze window
- Intent: Reduce the chance of an upstream dependency change causing an unrelated incident.
- Applies when: Teams with high deploy velocity in a regulated or low-tolerance domain.
- Minimal form: Dependency upgrades are batched into a weekly window with a rollback runbook; emergency CVE patches escape the window with extra review.
- Does NOT: Eliminate dependency churn.
- Cost: low
- Common couplings: `progressive_rollout`

### `runbook_as_code` — Runbook-as-code
- Intent: Survive the loss of an on-call engineer's tacit knowledge.
- Applies when: Any system where 3 a.m. recovery requires multi-step decisions.
- Minimal form: Every alert links to an executable runbook checked into the repo; the runbook explicit on what to verify before each destructive step.
- Does NOT: Replace incident judgement.
- Cost: low
- Common couplings: `manual_override_with_review`

### `stale_data_marker` — Stale-data marker on the user surface
- Intent: When a fallback path serves stale data, the user knows and can decide accordingly.
- Applies when: Any read path with `circuit_breaker_fallback_cache` or eventual-consistency window.
- Minimal form: Surface "as of HH:MM" or "this may be slightly out of date" in the UI when serving stale; suppress in normal operation.
- Does NOT: Replace user education.
- Cost: low
- Common couplings: `circuit_breaker_fallback_cache`, `read_only_degraded_mode`
