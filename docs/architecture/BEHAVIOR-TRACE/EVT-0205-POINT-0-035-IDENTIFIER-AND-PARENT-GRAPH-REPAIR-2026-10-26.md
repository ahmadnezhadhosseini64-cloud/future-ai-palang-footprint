# EVT-0205 — POINT-0/035 identifier and parent-graph repair

- Stable ID: HAIF-EVT-0205-IDENTIFIER-PARENT-GRAPH-REPAIR-20261026
- Production ID: EVT-0205
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/035](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- IN/OUT: [IN-071](../../0.0/anchors/PALANG-0.0-IN-20261026-071-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md) → [OUT-070](../../0.0/anchors/PALANG-0.0-OUT-20261026-070-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Current checkpoint: [CURRENT-083](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Observation and learning
A repeated short event number is not sufficient to establish identity. A reference mentioned inside a body, index, queue or master reference must not automatically be interpreted as a declaration owned by that file. A parent edge must be resolved against the exact source path and the actual candidate paths.

## Corrective implementation
- graph_identifier_roles.py bounds the document metadata region and separates header declarations from body occurrences.
- parent_edge_resolution.py prioritizes an evidence-backed source-specific override and fails closed if that target is absent.
- Regression tests must run in CI; test files existing in the repository alone do not constitute test evidence.

## Error governance
Prior collision-prone paths and mistaken short-ID assumptions remain in history. Corrections are additive, reversible and provenance-backed; no automatic renumbering, deletion, or silent winner selection is permitted.
