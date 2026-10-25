# POINT-0/014 — Automatic Continuity, Recovery and Living Registration

- Stable ID: G6IP-POINT-0-014-20261025
- Production ID: G6IP-POINT-0-014
- Version: 1.0.0
- Status: REGISTERED; parent-surface reconciliation and execution gates remain explicit.
- Previous checkpoint: [CURRENT-064](./PALANG-0.0-CURRENT-20261025-064-NEXT-EXECUTION-AND-GAPS.md)
- Chain: POINT-0/014 → IN-058 → OUT-057 → EVT-0167 → CURRENT-065
- Living mother: [HAIF Initial Model Master Reference](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Active next: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Current overlay manifest: [CURRENT-065-OVERLAY-MANIFEST](../../portable/RAHM/CURRENT-065-OVERLAY-MANIFEST.json).
- Canonical index: [REFERENCE_INDEX](../../REFERENCE_INDEX.md).
- Integration queue: [INTEGRATION-QUEUE](../../architecture/INTEGRATION-QUEUE/README.md).
- Auxiliary live mirror evidence: [EVT-0170](../../architecture/BEHAVIOR-TRACE/EVT-0170-LIVE-MIRROR-SYNC-RECHECK-2026-10-25.md).
- Current-chain audit failure, preserved for correction: [EVT-0171](../../architecture/BEHAVIOR-TRACE/EVT-0171-CURRENT-065-CHAIN-RECOVERY-FAILURE-2026-10-25.md).

## Preserved user request

“نقطه ۰ کن و باقی کارا و مواردی ک باید بدی رو ۰.۰ کن. نگم بهت نیاز ب چیا داری دیگه ثبت و زنده قابل استخراج و بازیابی و بروزرسانی سند مادر زنده و ...”

## Operational interpretation

This is a new Point 0 for the current interaction. The assistant is expected to apply the established registration/recovery protocol without asking the user to restate the known requirements. The next 0.0 checkpoint must carry unfinished actions, evidence requirements and open gaps forward. This record does not imply background activity between turns or capabilities that have not been executed.

## Invariants

1. Preserve all previous checkpoints; do not overwrite CURRENT-064 or older anchors.
2. UTC is canonical for repository registration, taken from the actual last-change commit timestamp; derive Tehran time from the same instant.
3. Preserve input, output, event, parent links, versions, repository evidence and recovery route.
4. Apply write → independent read-back → hash/link reconciliation → status classification.
5. Distinguish REGISTERED, READ-BACK VERIFIED, TEST EXECUTED, TEST PASSED, INTEGRATED and ACTIVE/LIVING.
6. Automatically carry forward known open work; do not ask the user to repeat known constraints and do not create placeholder NEXT tasks to simulate progress.
7. A repository record is not proof of durable memory, another host, background automation or an external storage target.

## Required acceptance gates

- [ ] All five chain records read back from the repository.
- [ ] Mother, index, integration queue and both portable manifests reconciled.
- [ ] Runtime tests executed on the exact revision and output retained.
- [ ] Clean export/import and recovery test executed with matching chain head.
- [ ] Existing NEXT-051 graph audit continued, occurrence by occurrence.
- [ ] CI receipt and exact-byte digests obtained from real workflow artifacts.
- [ ] Independent-host and restart persistence only marked verified after direct tests.
