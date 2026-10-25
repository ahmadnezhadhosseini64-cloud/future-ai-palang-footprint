# EVT-0169 — Portable Conformance Failures and Root Cause

- Stable ID: HAIF-EVT-0169-PORTABLE-CONFORMANCE-FAILURES-2026-10-25
- Production ID: EVT-0169
- Version: 1.0.0
- Lifecycle: ACTIVE / LIVING / FAILURE-PRESERVED / CORRECTION-IN-PROGRESS
- Related audit failure: [EVT-0168](./EVT-0168-LIVING-ARCHITECTURE-AUDIT-FAILURE-AND-ROOT-CAUSE-2026-10-25.md).
- Related mirror receipt: [EVT-0167](./EVT-0167-LIVE-MIRROR-SYNC-RECHECK-2026-10-25.md).
- Canonical time binding: [TIME-BINDING-EVT-0169](./TIME-BINDING-EVT-0169-PORTABLE-CONFORMANCE-2026-10-25.md).

## Failure A — malformed workflow definition
- Run: [40168432803](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40168432803).
- Tested SHA: `51c94ce571febf1c79e273da598b154adb5d21c1`.
- The workflow run completed immediately with no jobs; GitHub displayed the workflow path as its name.
- Root cause found by independent workflow-file read-back: a literal escaped newline `\\n` was embedded between two `paths:` entries in `.github/workflows/rahm-portable-conformance.yml`, making the workflow definition malformed.
- Correction: the literal sequence was replaced with a real YAML newline and the workflow was read back. The new run 40168541292 started jobs, proving the workflow is now parseable; this is not yet proof of the whole conformance pipeline passing.

## Failure B — duplicate paths across manifest inventories
- Run: [40168541292](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40168541292).
- Tested SHA: `f977f455b25450cd7d26d47609f6b4be80afb82d`.
- Job: `121094475755`.
- Steps passed: local runtime unit tests; valid/invalid interaction-pair schema fixtures; historical CURRENT-062 IN/OUT checkpoint-link recovery.
- Failed step: `Produce exact-byte SHA-256 evidence for manifest inventory`, which raised `DUPLICATE_MANIFEST_PATH_ACROSS_STABLE_AND_LIVE_REFERENCES`. Package build and artifact upload were skipped.
- Independently counted inventory: 51 entries in `files`, 53 in `live_reference_files`; 10 CURRENT-064 interaction-chain paths occurred in both lists. This violates the manifest's own stable-core-plus-live-reference policy.
- Correct reconciliation: retain the 10 mutable CURRENT-064 paths in `live_reference_files` for per-run exact-byte hashing, remove those duplicate entries from stable `files`, preserve the 41 unique stable-core files, and rerun the exact-byte digest scan. Do not mark the package built until the new artifact exists.

## Cross-check with Living Architecture Audit
- Run [40168433786](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40168433786) also failed on the same candidate SHA because the current-chain verifier's required links did not match the actual CURRENT-064 graph.
- Corrections now target POINT-0/013 → IN-057 → OUT-056 → EVT-0166 → CURRENT-064 and its overlay manifest; CURRENT-064's mother/index/queue/manifest links and the three queue runtime paths were repaired.
- The earlier failed runs remain historical evidence. A fresh audit and conformance run must be inspected after the manifest inventory correction.

## Status boundary
- EVT-0167 mirror comparison: PASS within tolerance; no write required.
- Workflow syntax: corrected; subsequent run started.
- Portable digest/package conformance: FAIL at run 40168541292; correction REQUIRED.
- Current IN/OUT reconstruction: a new run is pending; do not infer a pass from the code edit alone.
- External AI-host import, restart persistence, automatic capture and background execution: NOT RUN / NOT VERIFIED.
