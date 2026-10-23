# EVT-0120 — Evidence Locator Resolution and Cold Recovery

- Event ID: EVT-0120
- Stable ID: PALANG-EVIDENCE-LOCATOR-RESOLUTION-COLD-RECOVERY-2026-10-23-001
- Production ID: ELRCR-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTATION-IN-PROGRESS
- Parent: EVT-0119
- Current step: TALL-H02 — actual evidence locator resolution and content integrity, not merely URI/path shape validation.
- Next linked gate: fresh-session recovery from an independent 0.0 anchor after the resolver passes.

## Why activated now
EVT-0119 is now CI-verified for the exact GitHub Actions run and artifact recorded there: 20 unit tests passed and both manifests were independently downloaded and inspected. The next known gap is that a syntactically valid locator does not prove the evidence exists or matches an immutable content digest.

## Acceptance criteria
1. Production evidence must carry an explicit content SHA-256 in addition to source/commit provenance.
2. Local repository evidence uses a confined `repo://relative/path` locator; reject absolute paths, parent traversal, missing files, symlinks escaping the repository root, unsupported schemes and digest mismatch.
3. Resolution returns explicit `RESOLVED`, `UNRESOLVED`, `HASH_MISMATCH`, `UNSUPPORTED_LOCATOR`, or `FIXTURE_ONLY`; no unresolved result may be reported as PASS.
4. Fixture-mode records are explicitly skipped as `FIXTURE_ONLY`; they must not masquerade as resolved production evidence.
5. Unit tests cover valid resolution, missing file, path traversal, symlink escape where supported, hash mismatch, unsupported remote locator and fixture-only mode.
6. The GitHub Actions run must pass the complete suite and upload a manifest whose fixture records remain clearly marked as not production evidence.
7. After resolver acceptance, run a separate fresh-session recovery test from an independent 0.0 anchor through event → master → queue → evidence → next action, preserving every prior anchor.

## Current status boundaries
- Previous Behavior Hunter CI run #27: PASS, 20 tests; artifact independently inspected (see EVT-0119).
- Live host-wide IN/OUT capture: OPEN / NOT PROVEN.
- Fresh-session 0.0 recovery: NOT RUN.
- Remote evidence locators: not resolved by the current local resolver; any unsupported external URL must remain UNRESOLVED, never PASS.
- No automatic MASTER mutation; structural promotion requires owner review.
- Do not reopen Dropbox unless the owner explicitly asks.

## Implementation sequence
A. Add a confined local evidence resolver and content SHA-256 gate.
B. Add unit tests for positive, negative and adversarial paths.
C. Add fixture-safe CI manifest generation and inspect the actual run/artifact.
D. Reconcile the test plan, master reference and integration queue with exact run and blob evidence.
E. Start the fresh-session 0.0 recovery test only after A–D are verified.
