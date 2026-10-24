# CURRENT-052 — نقطهٔ ۰.۰ جاری: تداوم معماری و بازیابی

- Stable ID / شناسهٔ پایدار: `PALANG-CURRENT-CONTINUITY-AND-RECOVERY-2026-10-24-052`
- Production ID / شناسهٔ تولید: `G6IP-CURRENT-052`
- Version / نسخه: `1.0.0`
- Status / وضعیت هنگام ایجاد: REGISTERED; read-back pending.
- Parent / نقطهٔ والد: [CURRENT-051](./PALANG-0.0-CURRENT-20261024-051-REPOSITORY-EXCAVATION-REVIVAL.md), preserved.
- Input / ورودی: [IN-045](./PALANG-0.0-IN-20261024-045-CURRENT-052-CONTINUITY-AND-RECOVERY.md)
- Output / خروجی: [OUT-044](./PALANG-0.0-OUT-20261024-044-CURRENT-052-CONTINUITY-AND-RECOVERY.md)
- Event / رویداد: [EVT-0152](../../architecture/BEHAVIOR-TRACE/EVT-0152-CURRENT-052-CONTINUITY-AND-RECOVERY-2026-10-24.md)
- Living mother / سند مادر زنده: [NPFAP](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Discovery architecture / معماری موتور کشف: [Adaptive Discovery](../../../architecture/ADAPTIVE-DISCOVERY-CROSS-PLAYGROUND.md)
- Next gate / گام بعدی: [NEXT-044 — export and fresh-context recovery](./PALANG-0.0-NEXT-20261024-044-EXTRACTABLE-RAHM-CHILD-AND-COLD-START-TEST.md)

## Current architectural rule / قاعدهٔ معماری جاری
Every meaningful input, output, event, error, correction, test, and validation result must receive a stable identity, independent anchor, provenance, evidence, versioned links, UTC-first repository timestamp with Tehran equivalent, status, and next action. New proposals remain Child candidates; Rahm validates evidence and acceptance criteria; Master accepts only validated changes. Historical versions are never silently overwritten.

## Links to the historical 0 / 0.0 chain / پیوند با زنجیرهٔ تاریخی
CURRENT-052 is an additive successor to CURRENT-051. CURRENT-051 already links to CURRENT-050, IN-044, OUT-043, EVT-0151, the living mother, and NEXT-044. Earlier CURRENT-046 and older anchors remain preserved historical branches. This checkpoint does not claim that every historical anchor has been exhaustively enumerated or individually retested; that remains part of repository excavation/recovery.

## Living architecture status / وضعیت معماری زنده
- Living mother baseline at start: NPFAP v1.1.6.
- Discovery engine: Adaptive Discovery / Cross-Playground v1.1.0; architecture-defined, but always-on execution is NOT VERIFIED.
- Second-project repository and mother path: NOT IDENTIFIED; live dual-repository integration remains OPEN.
- Portable export and fresh-context recovery: NEXT-044 OPEN / NOT RUN.
- Dropbox: OPEN / WAITING; not current execution target.

## Next actions / گام‌های بعدی
1. Add this checkpoint to the living mother and reference index without deleting prior entries.
2. Fetch and compare IN-045, OUT-044, EVT-0152, CURRENT-052, mother, index, and NEXT-044; repair only proven link defects additively.
3. Execute NEXT-044: produce a verifiable export artifact, start in a clean host/context, reconstruct the current chain, compare IDs/paths/versions/digests, test negative cases, and record evidence.
4. Identify the canonical second project repository before claiming two-project integration.

## Status boundary / مرز وضعیت
CURRENT-052 is a new repository record, not proof of successful extraction, fresh-host recovery, second-project integration, or always-on runtime. Status can advance only after the relevant independent evidence is committed and read back.