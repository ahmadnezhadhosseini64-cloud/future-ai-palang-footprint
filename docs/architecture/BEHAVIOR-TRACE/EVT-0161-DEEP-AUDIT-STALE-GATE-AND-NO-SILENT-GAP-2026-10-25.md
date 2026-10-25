# EVT-0161 — Stale Conformance Gate and No-Silent-Gap Correction

- Stable ID: `G6IP-RAHM-EVT-0161-20261025`
- Production ID: `G6IP-EVT-0161`
- Version: 1.0.1
- Status: REGISTERED / READ-BACK REQUIRED; correction run pending.
- Input: [IN-052](../../0.0/anchors/PALANG-0.0-IN-20261025-052-DEEP-AUDIT-NO-SILENT-GAP-AND-EXECUTION.md)
- Output: [OUT-051](../../0.0/anchors/PALANG-0.0-OUT-20261025-051-DEEP-AUDIT-NO-SILENT-GAP-AND-EXECUTION.md)
- Parent checkpoint: [CURRENT-058](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-058-DEEP-EXCAVATION-EXECUTION-RECEIPTS.md)
- Latest checkpoint: [CURRENT-059](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-059-DEEP-AUDIT-AND-CORRECTED-CONFORMANCE.md)
- Active next: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Observation

The repository's latest pre-correction conformance workflow passed its declared checks, but its IN/OUT pointer test referenced an older branch (IN-047 / OUT-046 and CURRENT-054 / NEXT-048) instead of the actual current branch (IN-051 / OUT-050 and CURRENT-058 / NEXT-051). A passing test against a stale branch is not a valid acceptance receipt for the current architecture.

## Cause and correction

- Cause: test fixture/checkpoint references were not advanced when the canonical chain advanced.
- Correction performed: `.github/workflows/rahm-portable-conformance.yml` now references IN-051 / OUT-050 and CURRENT-058 / NEXT-051, and triggers when the current anchors or recovery verifier change.
- Evidence before correction: [run 40130268087](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40130268087), which is historical evidence only and does not prove the corrected workflow.
- Correction commit: `045f5b4e95743de5fefcc163bffc60938fea1d58`.
- Verification: pending fresh conformance run and independent read-back of the run log.

## Architectural learning

A test must assert the current canonical checkpoint, not just any valid historical checkpoint. Add a continuity gate that fails if expected IN/OUT/CURRENT/NEXT references lag the active branch. A successful CI status means only the assertions that actually ran passed; it must never be translated into “the architecture is complete.”

## Behavioral continuity rule

A pause, long processing gap, or subsequent user message must not silently abandon an open task. Preserve the open branch, log the new IN/OUT, state the actual executed step, and return a visible status with the exact resume point. Automatic capture/background behavior remains unverified until a real runtime test proves it.
