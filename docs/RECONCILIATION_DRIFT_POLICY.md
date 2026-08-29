# Reconciliation Drift Policy

Cross-layer drift is never silently ignored.

Possible states include:
- MEMORY_ONLY
- REPOSITORY_ONLY
- SYNC_GAP
- VERSION_CONFLICT
- PENDING
- PARTIAL
- VERIFIED
- RECONCILED

A missing or inaccessible destination is a state, not permission to claim completion. Automatic reconciliation may resolve mechanically safe gaps; authority-sensitive changes remain pending approval.
