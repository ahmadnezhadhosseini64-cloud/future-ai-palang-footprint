# EVT-0027 — لنگر جامع تعامل و بازیابی دو گردش کاری
- Stable ID: UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20-001
- Production ID: UIAWR-2026-10-20-001
- Event ID: EVT-0027-UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20
- Version: 1.0.0
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
