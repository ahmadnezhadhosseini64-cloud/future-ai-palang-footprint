# Durable Pending Reconciliation Bridge

Status: IMPLEMENTED_SPECIFICATION / EXECUTION_PROOF_PENDING

## Purpose
Ensure valuable productions are never silently lost when repository write capability is unavailable.

## Contract
1. Every registration-required production receives a stable production_id and trace_id.
2. If repository registration cannot be executed, a durable pending record MUST exist.
3. Every subsequent registration trigger MUST scan and drain eligible pending records automatically; a new user command is not required.
4. Scheduled reconciliation MUST also scan pending records so recovery does not depend on another user command.
5. A pending record may leave PENDING only after real write execution, read-back, identity/content verification, and evidence capture.
6. Retries MUST be idempotent by stable production_id/idempotency key.
7. Interrupted work remains PARTIAL/RESUMABLE until verified complete.
8. Conflicts remain CONFLICT/UNVERIFIED until resolved by the applicable authority rule.
9. No completion claim is permitted without execution evidence.

## Required state machine
NEW -> TRACED -> PENDING -> ELIGIBLE -> WRITE_ATTEMPTED -> READ_BACK_VERIFIED -> RECONCILED

Failure states: BLOCKED, FAILED, PARTIAL, CONFLICT, UNVERIFIED.

## Capability boundary
This bridge can only be declared ACTIVE when an actual runtime has authenticated, writable access to the destination and can produce execution/read-back evidence. A GitHub workflow alone does not constitute access to ChatGPT persistent memory.

## Acceptance requirement
The bridge is PROVEN only after a real end-to-end test demonstrates: destination unavailable -> durable pending -> capability recovery -> automatic pending drain without manual reminder -> write -> read-back -> verification -> idempotent retry -> final reconciled state.
