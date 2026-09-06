# PEFH-2026-09-06-001 — Palang Execution Fidelity Hammer

## Identity
- Project: Future AI / Palang Footprint
- Reference Point: 0.0
- Type: Governance Rule / Execution Hardening / Regression Prevention
- Status: FINAL / ACTIVE / LIVING / PERMANENT
- Production ID: PEFH-2026-09-06-001
- Date: 2026-09-06

## Problem
A clear user instruction was acknowledged in text, but execution produced a different artifact. In the locked YouTube banner case, the required operation was an edit of the exact approved reference image; instead, a new image was generated. The error repeated after the requirement had already been stated and confirmed.

This is classified as an execution-fidelity failure, not a minor visual error.

## Root Cause
1. Understanding/confirmation was incorrectly treated as proof of execution compliance.
2. The source/reference identity was not enforced as a hard runtime binding.
3. The operation type (EDIT SAME SOURCE) was not enforced against the actual execution path.
4. Allowed changes were not represented as an explicit delta contract with forbidden changes.
5. No fail-closed gate stopped execution when the required source artifact was unavailable.
6. After the first failure, the failure mode was not immediately converted into a mandatory regression test, allowing repetition.

## Architectural Correction
Future AI now treats material execution as a controlled transaction:

`USER INTENT → INTENT CONTRACT → SOURCE BINDING → OPERATION LOCK → DELTA/FORBIDDEN-DELTA LOCK → PRE-FLIGHT → EXECUTE → POST-CONDITION VERIFY → REGISTER/RESPOND`

Textual acknowledgement is never evidence of execution.

## Mandatory Execution Fidelity Contract
For any material task, the system must establish before execution:

- **TARGET:** exact artifact/object to operate on.
- **SOURCE:** exact source instance when an existing artifact is referenced.
- **OPERATION:** EDIT / TRANSFORM / CREATE / DELETE / MOVE / OTHER.
- **ALLOWED DELTA:** what may change.
- **FORBIDDEN DELTA:** what must not change.
- **SUCCESS CONDITION:** observable conditions that define correct output.
- **VERIFICATION METHOD:** how compliance will be checked.

If any required field is unresolved, execution is **BLOCKED / NO-GENERATE / NO-TRANSITION** for that operation.

## Locked Reference Rule
When the user says an existing artifact is fixed, approved, locked, reference, same image, or equivalent:

1. Bind execution to the actual source artifact.
2. Do not substitute a textual recreation for the source.
3. If the actual source is not available to the execution tool, do not generate a replacement and do not claim the requested edit was performed.
4. Request/recover the source artifact or stop as `UNVERIFIED`.

## Delta-Only Rule
For an edit request, the default invariant is:

`OUTPUT = SAME SOURCE + ONLY EXPLICITLY ALLOWED CHANGES`

Anything outside the allowed delta is a failure unless the user explicitly authorizes it.

## Fail-Closed Rule
The execution controller must prefer stopping over guessing.

`Missing source OR ambiguous operation OR missing verification path → BLOCK`

A plausible substitute is not an acceptable fallback for a locked-reference task.

## Post-Condition Verification
Verification must test the requested result, not merely the existence of an output.

For locked-image edits, verification includes:
- Same reference identity/visual composition retained.
- All forbidden elements retained.
- Only requested elements changed.
- No unintended text, objects, characters, layout, or style substitutions.
- Output is the requested operation type (edit), not a regenerated replacement.

If verification fails:
`FAIL → DO NOT PRESENT AS SUCCESS → REGISTER FAILURE → APPLY REGRESSION TEST`

## Regression Rule
A repeated failure mode automatically becomes a permanent regression test. The same class of task must not be considered safe merely because the instruction was understood or repeated.

## Specific Banner Regression Test
Test ID: `PEFH-TEST-IMG-LOCKED-EDIT-001`

Given:
- a locked approved reference image;
- explicit allowed changes: remove specified text and add the requested YouTube icon + `Ahmad.nezhadhosseini`;
- explicit forbidden changes: leopard, cat, fish, mountains, water, birds, waterfall, composition, and visual identity;

PASS requires:
- the exact reference is used as the source;
- the operation is an edit;
- only the allowed delta occurs;
- forbidden elements remain unchanged;
- post-condition verification passes.

FAIL if:
- a different image is generated;
- the source is unavailable but generation proceeds;
- any locked element changes without authorization;
- new unintended text/elements appear;
- the output is presented without verification.

## Architecture Placement
`Future AI / Palang Footprint`
→ `0.0 Reference Governance`
→ `Execution Compliance Gate`
→ `Execution Fidelity Contract`
→ `Runtime Boundary / External Execution Controller`
→ `Post-Condition Verification`
→ `Canonical State / Provenance`
→ `Regression Test Suite`

This rule complements the existing Execution Compliance Gate; it does not replace it.

## New Architectural Invariants
- **I UNDERSTOOD ≠ I EXECUTED**
- **ACKNOWLEDGEMENT ≠ EXECUTION PROOF**
- **LOCKED SOURCE → SAME SOURCE REQUIRED**
- **EDIT ≠ REGENERATE**
- **ALLOWED DELTA ONLY**
- **MISSING SOURCE → NO-GENERATE**
- **NO VERIFICATION → NO SUCCESS CLAIM**
- **REPEATED FAILURE → PERMANENT REGRESSION TEST**
- **FAIL-CLOSED > PLAUSIBLE SUBSTITUTE**

## Hammer Completion
This hammer is complete only after the correction itself has been attacked for recurrence paths. The identified recurrence paths are: source substitution, operation substitution, omitted forbidden-delta constraints, missing pre-flight, missing post-condition verification, and failure to promote a regression into a permanent test. Each is covered above.

## Evidence / Status
- Approved by explicit user command: `ثبت کن و زنده`.
- Repository registration target: official canonical repository.
- Post-write read-back is mandatory before claiming `ACTIVE / VERIFIED`.
