# Current 0.0 Master Reference — 2026-08-31

Status: ACTIVE / LIVE / RECOVERABLE
Project: Future AI / Palang Footprint
Owner: Ahmad Nezhadhosseini
Location: Iran, Gonbad-e Kavus
Purpose: Single compact reference for reconstructing the current path and registration state.

## Current position
The project has reached the cross-layer finalization/reconciliation stage. The canonical Repository is the durable reference for project records and deferred reconciliation. Persistent Memory is an applicable destination, but its registration is VERIFIED only after actual Memory read-back.

## What is already established
- Canonical Repository: active and accessible through the authorized GitHub connection.
- Access-blocked finalization/recovery rule: ACTIVE / LIVE / PERMANENT.
- Persistent Memory Deferred Reconciliation Protocol: PMDRP-2026-08-31-001, ACTIVE / LIVE / PERMANENT.
- Final Registration Closure Gate: ACTIVE / LIVE / PERMANENT.
- Capability Validation Before Action: CVBA-2026-08-31-001, ACTIVE / PERMANENT.
- Universal Rule Inheritance & Invocation Gate: URIG-2026-08-31-001, ACTIVE / LIVING / PERMANENT.
- 0.0 checkpoints exist in `checkpoints/` and are recoverable by exact file retrieval.

## Universal execution inheritance
Rules existing only as documentation are not sufficient. Every applicable new command, production, document, checkpoint, protocol, rule, principle, test, evidence record, recovery record, or architecture element must resolve and inherit the applicable canonical rules before execution is considered complete.

**Rule exists ≠ Rule invoked ≠ Rule verified.**

The short command `ثبت کن` means: resolve and apply all applicable governing rules, then execute the traceable registration workflow.

The command `0.0` means: retrieve the canonical 0.0 reference first, resolve applicable rules, create the required timestamped connection/checkpoint record, and only then continue.

## 0.0 mandatory timestamp gate
Every invocation of `0.0` must produce, at minimum:
- 0.0 ID
- Date
- Exact local time
- IANA timezone name and UTC offset
- Country/city and location-status
- Previous 0.0/checkpoint/reference when applicable
- Current state
- Continuation Anchor
- Rule-resolution status
- Verification status

A 0.0 record missing Date, Exact Local Time, or Timezone is INCOMPLETE and cannot be marked VERIFIED or COMPLETE.

Operational validation of this requirement requires a real invocation test with recoverable evidence and read-back.

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

## Capability validation before action
No action may be promised as currently executable merely because the capability normally exists. For tool-, connector-, runtime-, quota-, permission-, or interface-dependent actions, current capability must be validated before claiming availability. If unavailable, report the limitation before claiming execution. After execution, verify the result using the strongest applicable evidence.

The same rule applies to registration: “ثبت” is a traceable workflow, not a simple write. Identify the correct Production ID and canonical destination, preserve provenance, write/update, read back, verify, reconcile cross-layer state where applicable, and report unresolved gates. For image generation, current image-generation availability must be validated before promising that generation can be performed.

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
- `docs/protocols/CAPABILITY-VALIDATION-BEFORE-ACTION.md`
- `docs/protocols/RULE-INHERITANCE-AND-INVOCATION-GATE.md`

## Evidence boundary
This reference records the architecture and current recovery path. Architecture/design is not itself proof of end-to-end automatic execution. Any claim that automatic Memory reconciliation actually executed requires a real execution event plus recoverable evidence and Memory read-back.

The 0.0 timestamp rule is also not considered operationally proven merely because it is documented; it requires an actual invocation test that checks Date + Exact Local Time + Timezone by read-back.
