# NEXT-045 — ۰.۰ بعدی: آزمون شکارچی رفتار و بستن شکاف‌ها با شاهد
- Stable ID: G6IP-RAHM-NEXT-045-20261024
- Production ID: G6IP-NEXT-045
- Version: 1.0.0
- Status: OPEN / IN PROGRESS; individual tests remain NOT RUN until executed
- Parent: [CURRENT-047](./PALANG-0.0-CURRENT-20261024-047-BEHAVIOR-HUNTER-LIVING-ANCHOR.md)
- Event: [EVT-0147](../../architecture/BEHAVIOR-TRACE/EVT-0147-BEHAVIOR-HUNTER-LIVING-RULE-AND-CHECKPOINT-2026-10-24.md)

## Ordered work; do not mark complete without evidence
1. Fetch IN-039, OUT-039, EVT-0147, CURRENT-047 and NEXT-045 after writes; compare IDs, versions, parent/next links and exact key rule.
2. Update and fetch the HAIF mother, both GPT-6 living masters, Reference Index and integration queue.
3. Add a machine-readable Behavior Hunter rule/test binding to the architecture only after locating the canonical schema/path; avoid duplicate IDs and do not overwrite existing branches.
4. Run JSON Schema validation with one valid and one invalid interaction-pair fixture; record validator and exact results.
5. Compute SHA-256 from exact exported bytes and reconcile the export manifest; never confuse Git blob SHA-1 with SHA-256.
6. Audit relative links, stable-ID collisions, duplicated content and contradictory statuses; preserve findings as open records.
7. Run behavior-hunter regression tests: detect task drift; distinguish documented vs implemented vs read-back-verified vs runtime-active; retain a failure with reason and recovery action; restart from IN and from OUT.
8. Run durable-memory restart, idle background execution, clean-host and independent second-host tests only if an authorized runtime/host is available. Otherwise mark BLOCKED / UNSUPPORTED with reason and required prerequisite, not PASS.
9. Reconcile each completed test into the event, this queue, CURRENT and all living mothers by write → read-back → match.

## Acceptance and status vocabulary
- REGISTERED: repository write returned success.
- READ-BACK VERIFIED: post-write fetch returned matching content.
- VALIDATED: reproducible test evidence passes.
- INTEGRATED: required architecture/mother/index/queue links and read-backs match.
- ACTIVE / LIVING: only for a process actually running or a governing document maintained by explicit updates; never imply unattended background capture without runtime evidence.
- NOT RUN / BLOCKED / FAIL remain open until the stated recovery path is completed.

## Immediate restart instruction
Start here after returning to the project. Do not detour to Dropbox unless the user explicitly reopens that branch. Keep CURRENT-046 and earlier lineage intact.