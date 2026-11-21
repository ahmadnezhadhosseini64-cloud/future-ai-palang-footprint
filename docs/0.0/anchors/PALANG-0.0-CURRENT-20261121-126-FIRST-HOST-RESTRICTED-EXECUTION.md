# CURRENT-126 — وضعیت معماری POINT-0++ / میزبان اول

- Point: [POINT-0++ / POINT-0/073](GPT6-RAHM-USER-POINT-0-20261121-073-FIRST-HOST-RESTRICTED-EXECUTION-0PLUSPLUS.md).
- Input: [IN-116](PALANG-0.0-IN-20261121-116-FIRST-HOST-EXECUTION-BOUNDARY.md).
- Output: [OUT-115](PALANG-0.0-OUT-20261121-115-FIRST-HOST-EXECUTION-BOUNDARY.md).
- Event: [EVT-0292](../../architecture/BEHAVIOR-TRACE/EVT-0292-POINT-0PLUSPLUS-FIRST-HOST-RESTRICTED-EXECUTION-2026-11-21.md).
- Time binding: [TIME-BINDING-EVT-0292](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0292-FIRST-HOST-RESTRICTED-EXECUTION-2026-11-21.md).
- Parent checkpoint: CURRENT-125.
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Host role: FIRST_HOST / HOST-001.
- Authentication gate: OPEN / DEFERRED.
- Repository: PUBLIC / READ-ONLY target.
- Workspace: owner-defined, runtime-private, isolated; provisioning NOT VERIFIED.
- Task execution: owner-defined allowlist only.
- Repository write/delete/commit/push/branch/PR/merge/release/settings/permission changes: DENIED.
- Workspace-to-repository writeback: DENIED.
- Main integration: PENDING / NOT MERGED.
- Canonical ZIP rebuild for this source revision: PENDING.
- Technical enforcement: NOT VERIFIED.
- Independent host acceptance: NOT RUN.
- Host status: NOT CONNECTED / NOT ACTIVE until a direct runtime receipt is supplied.
- Preserve CURRENT-065/CURRENT-066 ambiguity, all historical roots and NEXT-051. No NEXT-052 created.

## معیارهای ورود و پذیرش

میزبان باید سند مادر متنی را بخواند، مخزن را بدون credential بخواند، main HEAD را ثبت کند، نسخهٔ canonical را با متن ارسالی مقایسه کند، workspace واقعی را در runtime خصوصی بسازد و فقط taskهای مجاز مالک را اجرا کند. آزمون منفی نوشتن مخزن، مرز workspace، allowlist، عدم writeback، update پس از تغییر مالک و receipt مستقل لازم است.

## وضعیت گیت‌ها

POLICY DESIGNED / SOURCE REGISTERED ON PROPOSAL BRANCH / MAIN NOT UPDATED / ZIP NOT REBUILT / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN.
