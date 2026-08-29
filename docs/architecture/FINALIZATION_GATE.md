# Finalization Gate

The architecture may be called finalized only when all applicable mechanisms are implemented and all required acceptance tests have evidence. Until then, status is `IMPLEMENTATION_REQUIRED` or `PROVEN` only per evidence.

## Non-negotiable checks
- Production boundary and detection exist.
- Every material production has stable identity/trace.
- Durable Pending exists for unavailable destinations.
- Pending drain is automatic on valid opportunities.
- Reconciliation is idempotent.
- Verification precedes completion claims.
- Detection safety net exists.
- Watchdog surfaces stale/failed/degraded control-plane state.
- Human approval is respected.
- Interrupted operations are resumable.
- Cross-layer state cannot be inferred from one layer.
- Memory↔Repository is not marked automatic/proven without a real capability and end-to-end evidence.

## Claim discipline
No document, workflow, or assistant response may convert `DESIGNED`, `IMPLEMENTED`, or `NOT_PROVEN` into `PROVEN` without evidence from the acceptance suite.
