# PMRH-TEST-NO-MEMORY-LOSS-001 — Persistent Memory Unavailable / Recovery Regression Test

**Status:** ACTIVE / LIVING / PERMANENT  
**Parent:** PMRH-2026-09-06-001  
**Reference:** 0.0

## Scenario
A valid production is registered while Persistent Memory is unavailable, limited, or cannot be independently read back.

## Required behavior
1. Generate one unique Production ID.
2. Preserve the complete production payload in the canonical Repository / Recovery Pending Store.
3. Set Memory state to `PENDING` or `UNVERIFIED`.
4. Do not claim Memory `VERIFIED`.
5. Make the pending record discoverable by the recovery/excavation path.
6. On restored Memory capability, reconcile the **same Production ID**.
7. Perform Memory WRITE → independent READ-BACK → VERIFY.
8. Close the pending state only after verification evidence exists.

## Failure criteria
- Production exists only in chat text.
- Pending state is not durable/discoverable.
- A new ID is created during recovery.
- Repository success is reported as Memory success.
- Memory is marked verified without read-back.
- Excavation cannot locate the pending record.

## Pass condition
`NO MEMORY → DURABLE PENDING → EXCAVATE → SAME ID → WRITE → READ-BACK → VERIFY → RECONCILE`.
