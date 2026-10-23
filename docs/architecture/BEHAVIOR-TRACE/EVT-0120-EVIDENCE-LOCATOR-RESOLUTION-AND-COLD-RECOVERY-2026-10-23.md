# EVT-0120 — Evidence Locator Resolution and Cold Recovery

- Event ID: EVT-0120
- Stable ID: PALANG-EVIDENCE-LOCATOR-RESOLUTION-COLD-RECOVERY-2026-10-23-001
- Production ID: ELRCR-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTED-IN-REPOSITORY / CI-PASS / ARTIFACT-READ-BACK-VERIFIED / COLD-RECOVERY-NOT-RUN
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
- Remote evidence locators: external URLs remain unsupported and must remain UNRESOLVED, never PASS. One controlled non-fixture local repo:// locator has now resolved successfully in CI; this is a smoke test, not a production test PASS.
- No automatic MASTER mutation; structural promotion requires owner review.
- Do not reopen Dropbox unless the owner explicitly asks.

## Implementation sequence
A. Add a confined local evidence resolver and content SHA-256 gate.
B. Add unit tests for positive, negative and adversarial paths.
C. Add fixture-safe CI manifest generation and inspect the actual run/artifact.
D. Reconcile the test plan, master reference and integration queue with exact run and blob evidence.
E. Start the fresh-session 0.0 recovery test only after A–D are verified.


## Implementation, failure learning, and independent verification — 2026-10-23

### Implemented
- `scripts/behavior-hunter/resolve_evidence_locators.py`: resolves only `repo://relative/path` evidence inside the repository root; rejects traversal, absolute paths, missing files, symlink escapes, unsupported remote schemes and SHA-256 mismatch. It never makes network requests or claims that an external URL resolved.
- Production PASS evidence now requires `content_sha256` in addition to `execution_id` and `source_sha`; digest format is checked by the extractor.
- `tests/behavior-hunter/test_resolve_evidence_locators.py`: added tests for valid resolution, hash mismatch, missing file, traversal, absolute path, symlink escape, unsupported URL, malformed digest, fixture-only behavior and PASS without evidence.
- Workflow now generates `evidence-resolution.json` in explicit fixture mode and uploads it with the other manifests.

### Failure and correction retained as learning evidence
- Runs #32 and #33 failed after the new content-digest requirement exposed an improperly escaped newline in a unit-test source line. Run #34 also failed on the same syntax error. The actual log identified the exact line and `SyntaxError: unexpected character after line continuation character`.
- Corrected the test source in commit `5ea1252580a13ec5e2d2260a502b807ef82db8bc`; the next run #35 passed. This is a real regression lesson: code generation/string edits require syntax validation through CI before declaring the implementation complete.

### Actual CI evidence
- Workflow run [#35](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40001818794).
- Run ID `40001818794`; head SHA `5ea1252580a13ec5e2d2260a502b807ef82db8bc`; run created UTC `2026-10-23T18:15:31Z`, Tehran `2026-10-23T21:45:31+03:30`.
- Job `generate-and-verify`: SUCCESS; **32 tests ran; OK**; candidate manifest generation, architecture-insight generation, evidence-resolution manifest generation and artifact upload all succeeded.
- Artifact ID `12522117128`; uploaded UTC `2026-10-23T18:15:44Z`, Tehran `2026-10-23T21:45:44+03:30`.
- Artifact ZIP SHA-256: `716c34a1ead3d63c4e4c290210e41780fe4a2ce0bd07b66c1056689e5dafa61b`.
- Downloaded and inspected all three files: `architecture-insights.json`, `candidate-tests.json`, `evidence-resolution.json`.
- `architecture-insights.json`: 4 fixture-only demonstration proposals; 0 rejected, 0 duplicates, 0 parse errors; no production promotion.
- `evidence-resolution.json`: 4 records marked `FIXTURE_ONLY`, 0 production resolutions, 0 unresolved errors. This is correct for synthetic fixtures and is **not** evidence that a real production locator has been resolved.
- `candidate-tests.json`: one candidate with `execution_status=NOT_RUN`; the candidate itself was not executed.

### Remaining truth / next active action
- Resolver behavior and security boundaries: CI unit-tested successfully.
- Real production evidence resolution against a real `repo://` evidence item: NOT YET RUN end-to-end; external URLs remain explicitly unsupported.
- Fresh-session recovery from an independent 0.0 through event → master → queue → evidence → next action: NOT RUN.
- Live host-wide ChatGPT IN/OUT capture: OPEN / NOT PROVEN.
- Next: run a controlled non-fixture evidence-resolution case using a real repository file and its SHA-256, then conduct the separate fresh-session 0.0 recovery test. Preserve the failures and all previous anchors.


## Controlled non-fixture locator verification — run #45

- Workflow: [Palang Behavior Hunter run #45](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40002313474).
- Head SHA: `845a905af1639cd1c3302cd53ae04e08ac4bcbb2`; run success, **34 tests ran; OK**.
- Artifact ID `12522836550`; artifact SHA-256 `fc386cf66f30904b2bd0cc3eebb9f48fc0f9aefdba9b5e2919fed80e274336aa`; uploaded UTC `2026-10-23T18:19:19Z`, Tehran `2026-10-23T21:49:19+03:30`.
- Independently downloaded artifact and verified four manifests. In `evidence-resolution-production-smoke.json`, one non-fixture `repo://data/interaction-pairs/evidence/EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt` record returned `RESOLVED`, `content_sha256_verified`, actual digest `1f5fefe857b5a8a5238c897ccb4dd637c1c8c4ecc00594b6aa887b87156bf44b`, 0 unresolved, 0 parse errors.
- The smoke record is intentionally `test_result=NOT RUN`; `evidence_integrity_verified=true` but `production_claim_allowed=false`. It proves local evidence bytes matched their digest, not that the underlying architecture test passed.
- Resolver now separates evidence integrity from permission to claim test PASS. PASS records additionally require execution identity and valid source SHA.
- Active next step: fresh-session 0.0 recovery from the durable checkpoint, verifying anchor → master → queue → EVT-0120 → resolver source/evidence → next action. This cold recovery has not yet been run.
