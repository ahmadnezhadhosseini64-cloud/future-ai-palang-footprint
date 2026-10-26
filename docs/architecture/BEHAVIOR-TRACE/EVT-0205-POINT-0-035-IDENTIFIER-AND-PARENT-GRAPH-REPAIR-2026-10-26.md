# EVT-0205 — POINT-0/035 identifier and parent-graph repair

- Stable ID: HAIF-EVT-0205-IDENTIFIER-PARENT-GRAPH-REPAIR-20261026
- Production ID: EVT-0205
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/035](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- IN/OUT: [IN-071](../../0.0/anchors/PALANG-0.0-IN-20261026-071-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md) → [OUT-070](../../0.0/anchors/PALANG-0.0-OUT-20261026-070-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Current checkpoint: [CURRENT-083](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Time bindings: [IN-071](./TIME-BINDING-IN-071-POINT-0-035-2026-10-26.md) · [OUT-070](./TIME-BINDING-OUT-070-POINT-0-035-2026-10-26.md) · [EVT-0205](./TIME-BINDING-EVT-0205-POINT-0-035-2026-10-26.md).
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Observation and learning
A repeated short event number is not sufficient to establish identity. A reference mentioned inside a body, index, queue or master reference must not automatically be interpreted as a declaration owned by that file. A parent edge must be resolved against the exact source path and the actual candidate paths.

## Corrective implementation
- graph_identifier_roles.py bounds the document metadata region and separates header declarations from body occurrences.
- parent_edge_resolution.py prioritizes an evidence-backed source-specific override and fails closed if that target is absent.
- Regression tests must run in CI; test files existing in the repository alone do not constitute test evidence.

## Error governance
Prior collision-prone paths and mistaken short-ID assumptions remain in history. Corrections are additive, reversible and provenance-backed; no automatic renumbering, deletion, or silent winner selection is permitted.

## Exact-main execution receipt — 2026-10-26

- Tested main SHA: 0d624def0d60cccf5ee2a587e67016fb3fbaf70f.
- Living Architecture Audit: [run 40312206847](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40312206847) — SUCCESS; artifact 12643829714; artifact digest sha256:bae2a153c7fa0416d83572682e4336eab7ae5e7e0585e1a0e66c69f49d34caf8.
- Portable RAHM Conformance: [run 40312206756](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40312206756) — SUCCESS; exact-byte SHA-256 scan PASS; live-reference SHA-256 scan PASS; package build PASS; 178 package files, 127 live references; archive SHA-256 270c4e6800efca881f1c8ff748d262959c2218d5ff2887fee58ca7c9d183af36; artifact 12644733201; evidence artifact 12644069032.
- Regression tests on this SHA: source-specific parent resolution 5/5 PASS; metadata-header identifier-role tests 4/4 PASS; semantic-role decisions 11/11 PASS; pointer discovery 8/8 PASS; starter engine 13/13 PASS; HAIF runtime 4/4 PASS.
- Repository time normalization: 2,869 UTC/Tehran pairs; 0 ambiguous/parse errors; 0 files without repository commit time; PASS.
- Graph result: missing local links 0; unresolved parent edges 2; ambiguous parent edges 0; 63 Stable-ID groups (1 unreviewed/open); 92 Production-ID groups (66 unreviewed/open); 7 Reference-ID groups (5 unreviewed/open); 41 event-number groups (3 unreviewed/open); 11 exact-content duplicate groups.
- These are receipts for SHA 0d624 only. A final rerun is required after the current checkpoint/event receipt updates below. Actual interactive RAHM-host import/restart/round-trip remains NOT RUN.
