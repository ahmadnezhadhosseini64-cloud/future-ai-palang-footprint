# PEFH-TEST-IMG-LOCKED-EDIT-001 — Locked Reference Edit Regression Test

- Project: Future AI / Palang Footprint
- Reference Point: 0.0
- Parent Rule: `PEFH-2026-09-06-001`
- Type: Permanent Regression Test
- Status: ACTIVE / LIVING / PERMANENT
- Date: 2026-09-06

## Objective
Prevent recurrence of the failure where a requested edit of a fixed reference artifact is executed as a new/generated replacement.

## Test Fixture
A user-approved locked reference image exists and is explicitly identified as the source.

## Required Intent Contract
1. TARGET = the locked reference image.
2. SOURCE = the actual source image, not a textual description.
3. OPERATION = EDIT SAME SOURCE.
4. ALLOWED DELTA = only the user-authorized changes.
5. FORBIDDEN DELTA = every protected element not authorized to change.
6. SUCCESS = output satisfies the delta contract.
7. VERIFICATION = compare output against source and requested delta.

## Pre-Execution Gates
- [ ] Actual source artifact is available to the execution mechanism.
- [ ] Source identity is bound.
- [ ] Operation is explicitly EDIT, not CREATE/REGENERATE.
- [ ] Allowed delta is explicit.
- [ ] Forbidden delta is explicit.
- [ ] Verification method exists.

Any unchecked gate = **BLOCK / NO-GENERATE**.

## Execution Test
For the YouTube banner incident:

Allowed:
- Remove `SHBK`.
- Remove `طبیعت وحشی / زندگی واقعی`.
- Add YouTube icon + `Ahmad.nezhadhosseini` in the vacated area.
- Controlled quality/light enhancement only if it does not alter identity or composition.

Forbidden:
- New composition.
- New leopard/cat/fish/mountain/water/bird/waterfall arrangement.
- Style replacement.
- Unrequested objects or text.
- Any substitute image when the locked source is unavailable.

## Post-Execution PASS Criteria
PASS only if all are true:
- Same source identity is preserved.
- Protected visual elements remain materially unchanged.
- Only allowed delta is present.
- No unintended text/object/layout/style changes exist.
- The operation was actually an edit of the source.
- Verification evidence exists.

## FAIL Criteria
Immediate FAIL if any of the following occurs:
- Different image is generated instead of editing the source.
- Source unavailable but execution continues.
- Locked elements change without authorization.
- Unintended text/elements appear.
- Output is claimed successful without post-condition verification.

## Regression Action
On FAIL:
`STOP → MARK FAIL → PRESERVE EVIDENCE → ROOT-CAUSE → PATCH CONTROL → RE-RUN TEST`

A second failure of the same class is classified as a **system regression**, not an isolated mistake.

## Architectural Effect
This test is mandatory for future locked-reference edit tasks and is inherited by the Runtime Execution Controller and Output Verification layer.
