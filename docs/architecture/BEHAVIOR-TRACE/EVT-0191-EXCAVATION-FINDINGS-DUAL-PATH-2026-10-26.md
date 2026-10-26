# EVT-0191 — Excavation Findings and Dual-Path Continuation

- Stable ID: HAIF-EVT-0191-EXCAVATION-DUAL-PATH-20261026
- Production ID: HAIF-EVT0191-20261026
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/025](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-025-EXCAVATION-FINDINGS-DUAL-PATH.md)
- IN/OUT: [IN-055](../../0.0/anchors/PALANG-0.0-IN-20261026-055-EXCAVATION-FINDINGS-DUAL-PATH.md) / [OUT-055](../../0.0/anchors/PALANG-0.0-OUT-20261026-055-EXCAVATION-FINDINGS-DUAL-PATH.md)
- Time binding: [TIME-BINDING-EVT-0191](./TIME-BINDING-EVT-0191-POINT-0-025-2026-10-26.md)
- Canonical root registration: 2026-10-26T03:52:33Z (UTC) / 2026-10-26 07:22:33 +03:30 (Asia/Tehran), bound to root creation commit fec34b0a6eacc31e8feb8f332e4d7d84540df68c.
- Current: [CURRENT-072](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-072-DUAL-PATH-EXCAVATION.md)
- Remediation queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Event and behavior lesson
The previous excavation described the project usefully but did not advance the repository state. The user accepted the findings and required actual registration and execution. This is a report-only/process failure: explanation is not execution.

A second safeguard was revealed by checking the actual repository: POINT-0/023, IN-053, OUT-053, EVT-0186, CURRENT-070 and later POINT-0/024 / CURRENT-071 already existed for earlier work. Reusing those identifiers would create collisions. The correction is to inspect the live register before allocating IDs, preserve existing records, and allocate POINT-0/025, IN/OUT-055, EVT-0191 and CURRENT-072 for this new event.

## Corrective rule
1. Inspect current root, IN/OUT, event and current checkpoint before numbering.
2. Keep Path A (initial model construction) and Path B (existing graph remediation) both active.
3. Continue NEXT-051 rather than creating a cosmetic successor.
4. Read back every write and compare exact IDs, versions and links.
5. Never claim host integration, persistence or background work without direct evidence.

## Evidence boundary
This event records the instruction and correction. It does not prove that open graph findings or independent-host gates have been resolved.