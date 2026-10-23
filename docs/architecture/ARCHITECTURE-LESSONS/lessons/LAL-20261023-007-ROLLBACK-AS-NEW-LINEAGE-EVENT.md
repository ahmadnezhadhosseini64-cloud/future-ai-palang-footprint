# LAL-20261023-007 — بازگشت نسخه، رویداد تازه در تبار معماری است

- Stable ID: PALANG-ARCH-LESSON-ROLLBACK-NEW-LINEAGE-EVENT-2026-10-23-007
- Production ID: LAL-20261023-007
- Version: 1.0.2 (path correction + bounded rollback evidence)
- Status: REGISTERED / SOURCE-LINKED / RUNTIME TEST OPEN / LIVING
- Source: [Persistence Continuity / No-Drop Recovery Architecture](../../../../architecture/memory/PERSISTENCE-CONTINUITY-NO-DROP-RECOVERY-ARCHITECTURE-2026-09-29.md)
- Related source: [Memory Persistence Proof / Master Archive Recovery Bootstrap](../../../../architecture/memory/MEMORY-PERSISTENCE-PROOF-MASTER-ARCHIVE-RECOVERY-BOOTSTRAP-2026-09-29.md)
- Governing lesson: [LAL-20261023-001](./LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md)

## Lesson
بازگشت به نسخهٔ سالم نباید نسخهٔ معیوب یا شواهد شکست را پاک کند. بازگشت خودش رویداد تازه‌ای در تبار است که baseline، علت، عملیات بازیابی، آزمون‌های پس از بازیابی و شکاف‌های باقی‌مانده را ثبت می‌کند.

## Operational rule
PRESERVE FAILURE → STOP PROMOTION → NAME VERIFIED BASELINE → RESTORE OR BRANCH → RUN RELEVANT POST-RECOVERY TESTS → RECORD RECOVERY EVENT → RESUME FROM VERIFIED STATE.

## Acceptance criteria
- Baseline commit/version is named and independently retrievable.
- Failed successor and its evidence remain preserved.
- Restore/branch operation and resulting commit are recorded.
- Relevant tests pass after recovery or the residual failure remains OPEN.

## Evidence boundary
The source architecture defines the recovery rule. An end-to-end rollback exercise for the current full project has not yet been run; runtime/global recovery remains OPEN / NOT PROVEN.

## Version 1.0.1 correction record
The initial v1.0.0 relative paths pointed into docs/architecture/memory, but the source files live at repository-root architecture/memory. This successor corrects both paths using four parent traversals. The previous file version and its evidence remain available in Git history; this is a path correction, not a deletion of the original record. A fresh structural audit is still required to confirm all local links on the integrated commit.


## Version 1.0.2 — bounded rollback evidence
A controlled repository branch rollback test has now passed: [EVT-0109](../../BEHAVIOR-TRACE/EVT-0109-CONTROLLED-GIT-ROLLBACK-RECOVERY-TEST-2026-10-23.md). The test restored an isolated branch to a named baseline, verified that the simulated candidate was absent from the restored branch, and verified that the candidate remained available on a separate evidence branch. This validates only the tested Git-ref recovery path; full-project, host/runtime and external-destination rollback remain OPEN / NOT PROVEN.
