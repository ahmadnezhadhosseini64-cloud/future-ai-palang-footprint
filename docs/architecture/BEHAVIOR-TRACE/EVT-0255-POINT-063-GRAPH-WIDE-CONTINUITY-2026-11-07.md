# EVT-0255 — POINT-0/063 graph-wide continuity and anchoring

- Stable ID: HAIF-EVT-0255-GRAPH-WIDE-CONTINUITY-2026-11-07-001
- Event number: EVT-0255
- Root: [POINT-0/063 (0+)](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261107-063-GRAPH-WIDE-CONTINUITY-AND-ANCHORING.md)
- Input: [IN-102](../../0.0/anchors/PALANG-0.0-IN-20261107-102-GRAPH-WIDE-CONTINUITY.md)
- Output: [OUT-101](../../0.0/anchors/PALANG-0.0-OUT-20261107-101-GRAPH-WIDE-CONTINUITY.md)
- Current checkpoint: [CURRENT-114](../../0.0/anchors/PALANG-0.0-CURRENT-20261107-114-GRAPH-WIDE-CONTINUITY.md)
- Sole active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Status: REGISTERED; read-back and full integration pending.

## Event

The user explicitly reasserted the project-wide anchor invariant: all POINT-0, POINT-0.0 and POINT-0+ anchors must connect to one another and to the full historical project graph. This event records the new root and the requirement to preserve, reconcile and navigate the complete graph, including independent input/output, event/time provenance, current checkpoint, living mother, central registries, queue, package/recovery manifests and historical open branches.

## Repository root time anchor

- Root registration commit: `7b55de39c19691a28ae50406e50ee6ddbcd3c4fe`
- Root registration UTC: `2026-11-07T18:13:22Z`
- Asia/Tehran equivalent: `2026-11-07T21:43:22+03:30`
- Provenance: GitHub commit metadata returned by fetch_commit for the exact root registration commit.
- User-message timestamp: UNKNOWN / UNVERIFIED; it is not replaced by the commit timestamp.

## Required project-wide relations

POINT-0/063 → IN-102 + OUT-101 → EVT-0255 → TIME-BINDING-EVT-0255 → CURRENT-114 → NEXT-051.

Also connect the root/checkpoint to POINT-0/062, POINT-0/061 and the complete historical graph through the canonical registry and source-backed cross-links. Preserve ambiguous/colliding branches as open; do not infer a winner.

## Acceptance tests

- G01–G06: graph-wide anchor and link reconciliation.
- T01–T04: UTC-first timestamp and provenance verification.
- H01–H05: continuity, restart, clean-host and independent-host recovery.
- Existing NEXT-051 package, graph, runtime, memory, Dropbox, issue and release gates remain active.

All tests remain OPEN / NOT RUN until direct, inspectable receipts are recorded. Registration of this event is not proof of graph-wide reconciliation or host-level recovery.
