# Focus biasing

When the user says "focus on security", "we care most about cost", "regulatory lens", or supplies an explicit `--focus` hint, apply this bias on top of the chosen workflow. Focus is a **bias**, not a filter. Category floors from `assets/stressor_categories.json` still apply; bias adds, never removes.

## Supported focus areas

`security | cost | regulatory | performance | safety`

Multiple focus areas may be combined (e.g. `regulatory + safety` for a medical-device platform). Stack their bias tables.

## Bias table — stressor categories

Weights are multipliers applied during stressor brainstorming (Block B). They do not alter the floors; they raise the *target* count above the floor.

| Category       | security | cost | regulatory | performance | safety |
|---|---:|---:|---:|---:|---:|
| regulatory     | 1.5      | 1.0  | 3.0        | 1.0         | 2.0    |
| market         | 0.8      | 1.5  | 1.0        | 1.0         | 0.8    |
| tech           | 1.5      | 1.5  | 1.0        | 2.5         | 1.5    |
| human          | 1.5      | 1.0  | 1.5        | 1.0         | 2.0    |
| adversarial    | 3.0      | 0.8  | 1.5        | 1.0         | 1.5    |
| environmental  | 0.8      | 0.8  | 1.0        | 1.0         | 2.5    |
| supply-chain   | 2.0      | 2.0  | 1.5        | 1.0         | 1.5    |
| scale          | 1.0      | 1.5  | 1.0        | 3.0         | 1.0    |
| time           | 1.0      | 0.8  | 1.5        | 1.5         | 1.0    |

Reading: under `--focus security`, generate roughly 3× as many adversarial stressors as you would under no focus, and 1.5× as many regulatory, tech, human, and supply-chain stressors. Floors still apply for environmental, market, etc.

## Bias table — preferred residue patterns

When more than one library pattern fits, prefer the focus-aligned one.

| Focus       | Preferred patterns |
|---|---|
| security    | `tenant_isolated_blast_radius`, `audit_log_immutability`, `key_rotation_dual_accept`, `manual_override_with_review`, `event_sourcing_audit_trail` |
| cost        | `bulkhead`, `per_tenant_quota`, `query_capacity_guard`, `dependency_freeze_window`, `backpressure` |
| regulatory  | `event_sourcing_audit_trail`, `audit_log_immutability`, `per_minute_billing_path`, `manual_override_with_review`, `runbook_as_code` |
| performance | `circuit_breaker_fallback_cache`, `read_only_degraded_mode`, `bulkhead`, `query_capacity_guard`, `backpressure` |
| safety      | `unlock_redundancy`, `local_autonomy`, `manual_override_with_review`, `alpr_camera_fallback_identity`, `runbook_as_code` |

## Report framing

Under focus, the exec summary opens with the focus framing:

- `security`: "Top adversarial stressors and the residues that contain them."
- `cost`: "Where load and noisy tenants threaten budget, and the bulkheads that hold."
- `regulatory`: "Where regulator changes would force re-architecture, and the residues that absorb them."
- `performance`: "Where load and tail latency cascade, and the residues that decouple."
- `safety`: "Where physical or human stressors threaten the user, and the residues that survive them."

## Hard rules

1. **Bias never reduces a category floor.** A user under `--focus security` who insists on no environmental stressors must still have `environmental ≥ 1`. Surface this to the user explicitly if they push back.
2. **Bias never deletes a residue.** A residue addressing a critical stressor outside the focus area stays in the stack.
3. **Bias is recorded in state.** `state.focus[]` lists the active focus areas. The report shows them in the header so readers know how the analysis was tilted.
