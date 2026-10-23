# EVT-0125 — Living architecture update capability

- Event ID: EVT-0125
- Stable ID: PALANG-LIVING-ARCHITECTURE-UPDATE-CAPABILITY-2026-10-23-001
- Production ID: LAUC-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTED-IN-REPOSITORY / CI-VERIFICATION-PENDING / OWNER-GATED
- Parent: EVT-0123
- Related learning loop: [TALL](../BEHAVIOR-OBSERVATORY/TEST-TO-ARCHITECTURE-LEARNING-LOOP-2026-10-23-001.md)
- Prior active gate: [EVT-0124 — fresh-session recovery](./EVT-0124-FRESH-SESSION-RECOVERY-2026-10-23.md)
- Canonical master: [CCCMR](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)
- Queue: [Integration Queue](../INTEGRATION-QUEUE/README.md)

## User directive
«خوب زنده و فعال کن و قابلیت بروزرسانی معماری هم زنده و فعال کن و گام بعدی رو انجام بده و کارایی ک میدونی دیگه نمیخام توضیح بدم خودت دقیق میدونی»

## Capability implemented
- Gate implementation: `scripts/behavior-hunter/architecture_update_gate.py`.
- Regression suite: `tests/behavior-hunter/test_architecture_update_gate.py`.
- Controlled proposal input: `data/interaction-pairs/architecture-update-proposal-fixture.json`.
- CI workflow: `.github/workflows/palang-behavior-hunter.yml` now runs the architecture-update gate and includes its decision manifest in the artifact bundle.
- TALL reference updated to record the implementation and governance boundaries.

## What the gate does
1. Validates the proposal's identity/version, source event/test IDs, observed facts, hypothesis, affected components, evidence, counterexamples, proposed change, required tests, rollback plan, lifecycle state and owner decision.
2. Resolves only repository-local `repo://` evidence paths, confines paths to the repository root and verifies the exact content SHA-256.
3. Blocks missing/mismatched evidence, path traversal, invalid state, missing required tests, unapproved integration and approval-state inconsistencies.
4. Flags protected architecture/master targets for explicit owner review.
5. Emits a machine-readable decision manifest; it does not write or promote changes into MASTER.

## Governance invariant
Architecture updating is now implemented as a controlled proposal-and-validation capability, not as an unrestricted self-modifying architecture. The loop is:
`OBSERVE → ANCHOR → PROPOSE → VERIFY EVIDENCE → TEST IN ISOLATION → OWNER DECISION → EXPLICIT INTEGRATION → REGRESSION → READ-BACK`.
No inferred approval, silent overwrite, or unsupported PASS is permitted.

## Verification boundary
- Unit test coverage is implemented; the current CI run and artifact inspection are pending separate read-back.
- The fixture proposal is illustrative input to validate the gate; it is not a production change or proof that the proposed architecture pattern is universally correct.
- Fresh-session recovery (EVT-0124) remains NOT RUN.
- Host-wide capture, automatic canonical promotion and external persistence remain NOT PROVEN.
- Issue #20 and Issue #21 remain OPEN.

## Next action
Verify the exact CI run after these changes, inspect the `architecture-update-gate.json` artifact and all recovery manifests, then continue the fresh-session recovery gate without pasting this conversation's summary into that separate session. Record the actual first result and compare it with canonical repository sources.
