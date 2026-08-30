# Execution Contract — Integration Completion Gate

**ID:** REF-ICG-EXEC-2026-08-30-001
**Gate:** ARCH-ICG-2026-08-30-001
**Status:** ACTIVE / EXECUTION CONTRACT

For every pending registration that becomes eligible for reconciliation:

1. Retrieve the pending record by its Production ID.
2. Re-evaluate applicable destinations using the Registration Matrix.
3. Perform the actual destination writes/operations.
4. Update the live project structures and living documentation required by those destinations.
5. Record per-destination evidence.
6. Verify the resulting state from the destination itself where possible.
7. Update the shared Registration Matrix and Reference/Registry records.
8. Preserve the recovery record as provenance/audit history when appropriate.
9. Close PENDING only after the Integration Completion Gate passes.
10. If any step fails, retain PENDING/INCOMPLETE with the failure and next reconciliation action.

A file existing in recovery or archive is never sufficient evidence for steps 3–9.
