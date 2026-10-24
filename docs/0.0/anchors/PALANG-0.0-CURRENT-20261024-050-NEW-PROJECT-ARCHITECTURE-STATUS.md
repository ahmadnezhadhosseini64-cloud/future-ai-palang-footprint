# CURRENT-050 — نقطهٔ ۰.۰ جاری: وضعیت معماری پروژهٔ جدید

- Stable ID / شناسهٔ پایدار: `PALANG-CURRENT-NEW-PROJECT-ARCHITECTURE-STATUS-2026-10-24-050`
- Production ID / شناسهٔ تولید: `G6IP-CURRENT-050`
- Version / نسخه: `1.0.0`
- Status / وضعیت: REGISTERED / READ-BACK VERIFIED; exact path and content fetched after write.
- Parent checkpoint / نقطهٔ والد: [CURRENT-049](./PALANG-0.0-CURRENT-20261024-049-LIVE-STATUS-AND-OUTPUT-CONTINUITY.md) — preserved, not replaced.
- Input / ورودی: [IN-043](./PALANG-0.0-IN-20261024-043-NEW-PROJECT-ARCHITECTURE-STATUS-AND-LIVING-ANCHOR.md)
- Output / خروجی: [OUT-042](./PALANG-0.0-OUT-20261024-042-NEW-PROJECT-ARCHITECTURE-STATUS-AND-LIVING-ANCHOR.md)
- Event / رویداد: [EVT-0150](../../architecture/BEHAVIOR-TRACE/EVT-0150-NEW-PROJECT-ARCHITECTURE-STATUS-2026-10-24.md)
- Living mother / سند مادر زنده: [NPFAP](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Discovery architecture / معماری کشف: [Adaptive Discovery v1.1.0](../../../architecture/ADAPTIVE-DISCOVERY-CROSS-PLAYGROUND.md)
- Next action / گام بعدی: [NEXT-044 — export and fresh-context recovery](./PALANG-0.0-NEXT-20261024-044-EXTRACTABLE-RAHM-CHILD-AND-COLD-START-TEST.md)

## Architecture state / وضعیت معماری
The new project architecture is at the foundational, repository-backed stage. It includes a living mother; linked 0.0 checkpoints through CURRENT-049; a behavior/event lineage; Freshness Discovery / Adaptive Discovery; and the Child → Rahm → Master governance rule. CURRENT-050 is an additive continuation of CURRENT-049, not a replacement.

## Canonical rules / قواعد حاکم
- Every meaningful input, output, event, error, correction, test, and status transition gets its own identity, version, evidence, timestamp anchor, prior link, mother link, and next action.
- UTC is the canonical repository timestamp from the actual Git commit; derive Tehran equivalent from that same instant.
- Child proposals remain candidates until Rahm validation and acceptance criteria pass; only then may Master integrate them.
- Writing, read-back, validation, integration, export, and fresh-host recovery are distinct states.
- New information is additive; never silently erase or replace previous 0.0 anchors.

## Open gates / دروازه‌های باز
- NEXT-044: export a verifiable package and test reconstruction in a fresh host/context — OPEN / NOT RUN.
- Second project: canonical repository and mother path not identified; live two-repository integration not claimed.
- Always-on discovery/search, scheduling, notifications, and background automation: NOT VERIFIED.

## Continuity instruction / دستور ادامه
Continue from CURRENT-050. First read back and match IN-043, OUT-042, EVT-0150, CURRENT-050, the living mother, and the reference index. Then execute NEXT-044. Keep unresolved gates visible and preserve all previous checkpoints.