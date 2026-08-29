# Reconciliation State Machine

`CANDIDATE → CLASSIFIED → TRACED → REGISTER_INTENT → PENDING → CAPABILITY_READY → RECONCILING → EVIDENCE_CAPTURED → VERIFIED → RECONCILED → COMPLETED`

Failure/exception transitions:

- `CANDIDATE → UNCLASSIFIED`
- `RECONCILING → PARTIAL`
- `RECONCILING → FAILED`
- `CAPABILITY_READY → BLOCKED`
- `VERIFIED → CONFLICT`
- `PENDING → STALE`
- any control-plane failure → `CONTROL_PLANE_DEGRADED`

Rules:

1. No state may skip required evidence gates.
2. Pending survives interruption and is removed only after verified reconciliation.
3. Retry uses the stable production ID and is idempotent.
4. A destination's success cannot imply another destination's success.
5. Human-approval items cannot transition to canonical completion without approval evidence.
6. Any ambiguous or undetected candidate remains reviewable.
