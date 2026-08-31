# Persistent Memory Deferred Reconciliation Protocol

ID: PMDRP-2026-08-31-001
Status: ACTIVE / LIVE / PERMANENT OPERATIONAL RULE

## Purpose
When a production record is created but Persistent Memory cannot be written or cannot be read back and verified, the record must not be lost and must not be falsely marked complete.

## Rule
1. Preserve the same Production ID and complete payload in the durable Repository/Recovery Pending Store.
2. Mark the Persistent Memory layer `UNVERIFIED` (or `PENDING`) until real read-back verification is available.
3. Treat the Repository/Recovery record as the authoritative deferred-reconciliation source for the missing Memory registration.
4. When Persistent Memory becomes available, the reconciliation process must automatically or at the first valid execution opportunity retrieve eligible pending records, write the same record, perform read-back/verification, and transition the Memory state to `VERIFIED`.
5. Reconciliation is idempotent: never create a duplicate Production ID; if the record already exists, verify and reconcile rather than duplicate it.
6. If automatic execution cannot reach Persistent Memory, retain the record as `PENDING/UNVERIFIED` and retry at the next valid opportunity. Never claim completion without evidence.
7. Every successful reconciliation must leave auditable evidence linking the original Production ID, deferred state, execution attempt, destination, read-back, and final verification.

## Boundary
GitHub Actions can automatically manage the Repository/Recovery side, but cannot independently write ChatGPT Persistent Memory unless a real authorized Memory interface is available. Therefore the architecture must expose the pending item and make it recoverable; Memory `VERIFIED` is asserted only after actual Memory read-back.

## Operational Flow
PRODUCTION → MEMORY WRITE UNAVAILABLE/UNVERIFIED → DURABLE PENDING RECORD → ACCESS RESTORED → AUTOMATIC/FIRST-VALID-OPPORTUNITY RECONCILIATION → MEMORY WRITE → READ-BACK → VERIFY → MEMORY VERIFIED → PENDING CLOSED

## Integrity Gate
No Record → No Transition.
No Read-back → No VERIFIED claim.
Same Production ID → No Duplicate.
