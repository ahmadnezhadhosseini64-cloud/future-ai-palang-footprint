# CURRENT-133 — نقطهٔ ۰++: حفظ تاریخچه و رفع ناسازگاری CI

- Status: ACTIVE / LIVING / REPAIR-COMMITTED / EXACT-HEAD-CI-PENDING / PR-OPEN / ZIP-RELEASE-PENDING
- Parent: CURRENT-132
- Root: POINT-0/077 (0++)
- Chain: CURRENT-132 → IN-123 → OUT-122 → EVT-0299 → TIME-BINDING-EVT-0299 (2026-11-21T14:02:54Z / 2026-11-21T17:32:54+03:30) → CURRENT-133 → NEXT-051
- Sole governing queue: NEXT-051
- PR: #64
- Branch: feat/universal-ai-host-connectivity

## Connected input/output
- Input: [IN-123](PALANG-0.0-IN-20261121-123-CI-FAILURE-PRESERVATION-AND-OWNER-APPROVAL.md)
- Output: [OUT-122](PALANG-0.0-OUT-20261121-122-CI-LINEAGE-REPAIR-AND-PRESERVATION.md)

## Historical preservation
The first portable conformance failure is retained as an immutable historical event: test_engine.py expected CURRENT-131 while the starter README already declared CURRENT-132. See IN-123 and the original failed run 44910997351. This failure is not deleted, overwritten or relabeled as a success.

## Authorized resolution
The test expected chain was corrected to include IN-122, OUT-121, EVT-0298, TIME-BINDING-EVT-0298 and CURRENT-132. The original CURRENT-131 history remains connected.

## Follow-up recurrence and current repair
A later head (c49e3db2332925b85061219505398ee86abe9441) exposed a second stale copy in GPT6_HOST_INSTRUCTIONS.md: test_engine.py expected CURRENT-133 but that file still ended at CURRENT-132. The same stale canonical chain was also absent from the package README. Both files have now been updated additively. The failed run IDs 44912041984 (portable conformance) and 44912042023 (living architecture audit) are preserved as a separate recurrence; they are not erased by the correction. Exact-head CI after these edits is pending.

## Earlier exact passing branch evidence
At commit 9190b0a9c2dcf1db0133bd937be0bb1a81d3624c (UTC 2026-11-21T13:59:24Z; Tehran 2026-11-21T17:29:24+03:30):
- 44911581459 Portable RAHM Conformance and Digest Evidence: SUCCESS.
- 44911581473 Living Architecture Audit: SUCCESS.
- 44911581532 Universal AI Host Contract Tests: SUCCESS.
- 44911581743 Universal AI Host Connectivity Tests: SUCCESS.

## Scope and remaining gates
The earlier exact-head CI success remains valid for commit 9190b0a9c2dcf1db0133bd937be0bb1a81d3624c only. It does not certify later commits. The latest source correction is committed; rerun all workflows at the new exact head before claiming current CI success. PR #64 is not merged. Canonical ZIP rebuild, archive hash/inventory, extraction/read-back and independent clean-host recovery remain separate gates. No OAuth was performed. Sole queue remains NEXT-051.
