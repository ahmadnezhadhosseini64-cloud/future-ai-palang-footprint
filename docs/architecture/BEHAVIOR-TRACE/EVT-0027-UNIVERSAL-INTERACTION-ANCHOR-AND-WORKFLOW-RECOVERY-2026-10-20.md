# EVT-0027 — لنگر جامع تعامل و بازیابی دو گردش کاری
- Stable ID: UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20-001
- Production ID: UIAWR-2026-10-20-001
- Event ID: EVT-0027-UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20
- Version: 1.0.2
- Date: 2026-10-20
- Exact user-message time: UNKNOWN / UNVERIFIED.
- Exact registration time: UNKNOWN / UNAVAILABLE; no exact timestamp source was returned for this write. Do not infer one.
- Project timezone: Asia/Tehran (UTC+03:30)
- Owner: Ahmad Nezhadhosseini / احمد پلنگ
- Status: ACTIVE / LIVING anchor; workflow remediation is in progress and not yet proven successful.
- Full reference: ../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20-001.md

## Input anchor
User requires every relevant input/output to receive an interaction anchor, timestamp governance, documentation, and full recoverable lineage; requests the two failed workflows be genuinely resolved, not just reported.

## Actions actually performed
1. Read GitHub Issue #18 and confirmed it remains OPEN.
2. Read historical runs 39449957651 and 39449956059. Both show completed/failure on commit ebadb73f6f107555b5054714aefab175d2a519bd.
3. Queried jobs via specialized endpoints and direct API; both returned zero jobs. No trustworthy step logs were available to diagnose the historical cause.
4. Requested rerun of failed jobs for each historical run; both returned HTTP 403 “This workflow run cannot be retried”.
5. Changed .github/workflows/automatic-final-registration-proof.yml so upload-artifact uses newline-separated paths evidence/ and provenance/runtime-evidence/. Commit: 2a3398132ca8e196295d2d61bf7c96d12ce7d84c.
6. Changed .github/workflows/main.yml path filters to include docs/**, evidence/** and provenance/** as well as README.md and the workflow itself. Commit: 75f1fff4a42a6fc1465a2164a4d82db30934a95c.
7. These changes are committed to the canonical repository. The two old failed runs remain historical failures. New run success has not yet been verified at this event's creation; Issue #18 stays open.

## Inherited timestamp rule
Use DUAL-TIMESTAMP-AVAILABILITY-RULE-2026-10-20-001 / DTAR-2026-10-20-001. Separate user-message time, registration time, commit time, workflow time, and read-back time. Mark unavailable exact times UNKNOWN / UNAVAILABLE; never invent or backfill.

## Verification and next action
Read back this event and its full reference, then inspect new workflow runs after the two commits. Only close Issue #18 after both workflows have fresh successful runs, real successful jobs, relevant evidence/artifacts inspected, and repository read-back verified. Library, Buffer, Persistent Memory, and Dropbox are not proven updated by this GitHub write.

## Fresh-run verification update (2026-10-20)
- Evidence Gate run 39454138917 failed on commit 14187974765f4d743d3ca05186565ad4c9c0fdaa; API created_at 2026-10-20T16:04:05Z: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39454138917
- Automatic Final Registration Proof run 39454141194 failed on the same commit; API created_at 2026-10-20T16:04:06Z: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39454141194
- Both latest job lists were empty; run-log download returned HTTP 404. Cause remains UNKNOWN / UNVERIFIED; these facts do not prove a YAML parse issue or any other specific cause.
- Therefore the two workflow edits have not resolved the failures. Issue #18 remains OPEN; do not claim closure. Exact current registration time and user-message time remain UNKNOWN / UNAVAILABLE.

## Final acceptance evidence (2026-10-20)
- Root cause 1: heredoc content and closing EOF lines were outside the YAML run block indentation in both workflows, causing runs to fail before jobs/logs were exposed.
- Root cause 2 (Evidence Gate after YAML fix): `evidence_file` was defined in a different shell step; step environments are isolated. Defined it again in the commit step.
- Root cause 3 (Evidence Gate): concurrent commits raced; switched to unique per-run evidence filenames and bounded fetch/rebase/push retries.
- Automatic artifact paths were changed to newline-separated entries.
- Evidence Gate: run 39454598933 PASS / SUCCESS, job evidence-gate and all steps successful: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39454598933
- Automatic Final Registration Proof: run 39454598935 PASS / SUCCESS, job final-proof and all steps successful: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39454598935
- Artifact IDs: Evidence Gate 12280735143 (437 bytes); final proof 12280395438 (4731 bytes).
- Durable evidence read-back: evidence/evidence-gate-39454598933.txt, blob SHA 7d3c9faf411d1c5ff5822f1946c8a57310df734c.
- GitHub API created_at for both successful runs: 2026-10-20T16:07:10Z; Tehran equivalent 19:37:10 +03:30 is derived conversion only.
- Exact user-message timestamp and exact registration timestamp remain UNKNOWN / UNAVAILABLE. Library, Buffer, Persistent Memory and Dropbox are not proven by this repository test.
- Acceptance: both named workflows now PASS / VERIFIED; historical failures remain in history, not erased.
