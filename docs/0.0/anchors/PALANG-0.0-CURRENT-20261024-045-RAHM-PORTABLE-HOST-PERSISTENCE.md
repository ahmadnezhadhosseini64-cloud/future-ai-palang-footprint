# CURRENT-045 — نقطهٔ ۰.۰ زنده: بستهٔ رحم و اثبات قابلیت میزبان
- Stable ID: G6IP-RAHM-CURRENT-045-20261024
- Production ID: G6IP-CURRENT-045
- Version: 1.0.0
- Status: REGISTERED; package artifact writes have receipts. Full package read-back and integrity reconciliation PENDING.
- Parent: [CURRENT-044](./PALANG-0.0-CURRENT-20261024-044-RAHM-PROJECT-POINT-0.0.md)
- Branch Point 0: [Rahm Point 0](./GPT6-RAHM-PROJECT-POINT-0-2026-10-24-001.md)
- Interaction: [IN-037](./PALANG-0.0-IN-20261024-037-PORTABLE-RAHM-AND-HOST-PERSISTENCE.md) → [OUT-037](./PALANG-0.0-OUT-20261024-037-PORTABLE-RAHM-AND-HOST-PERSISTENCE.md) → [EVT-0145](../../architecture/BEHAVIOR-TRACE/EVT-0145-PORTABLE-RAHM-HOST-CAPABILITY-ARCHITECTURE-2026-10-24.md).
- Portable package directory: [docs/portable/RAHM](../../portable/RAHM/RAHM_BOOT.md)
- Governing HAIF mother: [HAIF mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Inherited architecture mother: [GPT-6 inherited architecture](../../reference/REFERENCE-DOCUMENTS/GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md)
- GPT-6 living master: [GPT-6 living master](../../reference/REFERENCE-DOCUMENTS/GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001.md)
- Next action: [NEXT-043](./PALANG-0.0-NEXT-20261024-043-HOST-PERSISTENCE-BACKGROUND-AND-EXPORT-PROOF.md)

## Current state
The package architecture has been written as eight repository files. The manifest is deliberately draft and its digests are null until computed from exact bytes. Package-wide read-back, integrity checks, JSON validation and tests are pending.

## Capability proof boundary
- Durable repository storage is not host conversational memory.
- Host conversational memory is not a complete durable archive.
- Prompt-response capability is not idle background execution.
- Persistent memory requires unique-marker write, session boundary/restart, retrieval and match evidence.
- Background execution requires an authorized scheduled job to execute while the user is inactive, timestamped logs, durable output and independent read-back.
- No capability can be guaranteed merely by writing a specification; host/provider support and permissions are prerequisites.

## Continuity
Preserve CURRENT-044 and all older anchors. Continue this Rahm branch from CURRENT-045. Main HAIF lineage CURRENT-052 remains a separate preserved branch; reconcile only through explicit mother/index links, never merge or overwrite anchors.
