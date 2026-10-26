# EVT-0192 — User Request: New Root POINT-0 and Dual-Path HAIF Continuation

- **Stable ID:** HAIF-EVT-0192-POINT-0-DUAL-PATH-CONTINUATION-20261026
- **Production ID:** HAIF-EVT0192-20261026
- **Version:** 1.0.0
- **Status:** REGISTERED / OPEN FOR READ-BACK
- **Root:** [POINT-0/026](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-026-DUAL-PATH-HAIF-CONTINUATION.md)
- **Input:** [IN-062](../../0.0/anchors/PALANG-0.0-IN-20261026-062-DUAL-PATH-HAIF-CONTINUATION.md)
- **Output:** [OUT-061](../../0.0/anchors/PALANG-0.0-OUT-20261026-061-DUAL-PATH-HAIF-CONTINUATION.md)
- **Current checkpoint:** [CURRENT-073](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-073-DUAL-PATH-HAIF-CONTINUATION.md)
- **Previous root:** [POINT-0/025](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-025-EXCAVATION-FINDINGS-DUAL-PATH.md)

## Event
The user explicitly asks to make this conversation a new POINT-0, record next work as 0.0 checkpoints, update the living master reference, and evolve the project architecture around both Path A and Path B while continuing both.

## Architecture decision
Path A and Path B are parallel workstreams under the same HAIF master and canonical graph, not separate projects and not substitutes for each other:
- **A — Portable initial model:** package, schema, conformance, fresh extraction/import, independent authorized host import, and restart/recovery.
- **B — Existing graph recovery:** provenance-preserving inventory, per-occurrence ID adjudication, duplicate/alias classification, ambiguous parent-edge review, timestamp reconciliation, and audit reruns.
- **Shared control plane:** master/child/rahm, event ledger, evidence vault, continuity anchors, typed graph edges, integration queue and independent destination status.
- **Promotion rule:** a change enters Master only after evidence, review and recorded acceptance; otherwise it remains Child/RAHM or OPEN.
- **No silent deletion:** duplicates are represented as aliases or relationships only after evidence; original paths and provenance remain.
- **No numeric winner rule:** IDs and timestamps do not independently establish canonical authority.
- **Destination boundary:** repository writes do not establish Buffer, Library, Dropbox or Persistent Memory writes.

## Learning and error prevention
The previous excavation found that a bounded overlay-recovery pointer and the global project registry pointer can legitimately differ by scope. The scope-aware pointer discovery was fixed and tested as `SCOPED_CONSISTENT`; this closed that specific false-conflict defect, not the semantic graph audit. Future audits must distinguish scope before declaring conflict.

Previous ID-allocation collisions were also caught and repaired before the last verified root. The lesson is to search the live repository for candidate IDs before creating anchors, then fetch written files and run exact-head checks. Do not reuse IDs based on assumptions.

## Last known evidence carried forward
Last verified main SHA was `ab9f96c52473e29f71cd4a00558986a763b0c6fc`; on that SHA, Living Architecture Audit run 40267748505 and Portable RAHM Conformance run 40267748439 both succeeded. These receipts predate this event and are not proof that the new commit passes. Semantic graph status remains REVIEW_REQUIRED; latest recorded open findings include 62 unreviewed Stable-ID groups and 13 ambiguous parent edges.

## Next action
Read back new files; update the 0.0 registry, reference index, integration queue and living masters; then run and inspect fresh checks on the exact resulting main SHA. Continue both paths without closing untested gates.
