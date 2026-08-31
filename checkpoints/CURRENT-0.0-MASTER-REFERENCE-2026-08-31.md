# Current 0.0 Master Reference — 2026-08-31

Status: ACTIVE / LIVE / RECOVERABLE
Project: Future AI / Palang Footprint
Purpose: Single compact reference for reconstructing the current path and registration state.

## Current position
The project has reached the cross-layer finalization/reconciliation stage. The canonical Repository is the durable reference for project records and deferred reconciliation. Persistent Memory is an applicable destination, but its registration is VERIFIED only after actual Memory read-back.

## What is already established
- Canonical Repository: active and accessible through the authorized GitHub connection.
- Access-blocked finalization/recovery rule: ACTIVE / LIVE / PERMANENT.
- Persistent Memory Deferred Reconciliation Protocol: PMDRP-2026-08-31-001, ACTIVE / LIVE / PERMANENT.
- Final Registration Closure Gate: ACTIVE / LIVE / PERMANENT.
- 0.0 checkpoints exist in `checkpoints/` and are recoverable by exact file retrieval.

## Deferred-registration mechanism
If any required destination cannot be written or verified:
PRODUCTION → PENDING/UNVERIFIED → DURABLE REPOSITORY/RECOVERY → ACCESS RESTORED → RECONCILE SAME PRODUCTION ID → WRITE → READ-BACK → VERIFY → FINALIZE.

Rules:
1. Never lose the record.
2. Never regenerate the Production ID.
3. Never duplicate an already successful registration.
4. Never claim VERIFIED without read-back evidence.
5. Resume from the first unresolved gate.
6. Keep exact continuation path and destination state.
7. Close only after all applicable gates pass.

## Persistent Memory bridge boundary
GitHub can automatically manage the durable Repository/Recovery side. It cannot independently write ChatGPT Persistent Memory without an authorized Memory interface. Therefore, when that interface is unavailable, the Repository is the durable deferred-reconciliation source. When Memory access is actually available, the pending record must be reconciled using the same Production ID, followed by Memory read-back and verification.

## Final closure invariant
NO COMPLETE WITHOUT ALL APPLICABLE GATES VERIFIED.

## Recovery instruction
On return or a new `0.0`: retrieve this file first, then retrieve the applicable protocol and latest checkpoint; verify the actual repository state before making any completion claim. Do not reconstruct from conversational memory alone.

## Primary protocols
- `docs/protocols/ACCESS-BLOCKED-FINALIZATION-RECOVERY.md`
- `docs/protocols/PERSISTENT-MEMORY-DEFERRED-RECONCILIATION-PROTOCOL.md`
- `docs/protocols/PERSISTENT-MEMORY-UNAVAILABILITY-RECOVERY-PROTOCOL.md`
- `docs/protocols/FINAL-REGISTRATION-CLOSURE-GATE.md`
- `docs/protocols/CONNECTION-CHAIN-PROTOCOL.md`

## Evidence boundary
This reference records the architecture and current recovery path. Architecture/design is not itself proof of end-to-end automatic execution. Any claim that automatic Memory reconciliation actually executed requires a real execution event plus recoverable evidence and Memory read-back.
