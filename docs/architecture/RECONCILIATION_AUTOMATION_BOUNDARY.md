# Reconciliation Automation Boundary

Automation may execute only capabilities actually exposed to it. It may not infer access to ChatGPT persistent memory from repository access, connector presence, or prior successful operations.

## Allowed automatic actions
- Detect repository-side production candidates.
- Create/maintain traceable repository-side records when the execution capability permits.
- Detect and report Pending/Gap/Conflict states.
- Retry idempotently when the required destination capability is available.
- Verify repository-side artifacts by read-back.
- Run watchdog and safety-net checks.

## Capability-gated actions
- Any write to ChatGPT persistent memory.
- Any read of ChatGPT persistent memory.
- Any Memory↔Repository reconciliation.

These require an actual exposed capability and evidence. If unavailable, the state remains `NOT_AVAILABLE`/`UNVERIFIED`/`PENDING` and must not be represented as automatic or proven.
