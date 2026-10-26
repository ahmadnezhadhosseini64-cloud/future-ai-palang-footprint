# EVT-0201 — MASTER → RAHM → CHILD architecture

- Stable ID: `HAIF-EVT-0201-MASTER-RAHM-CHILD-20261026`
- Production ID: `EVT-0201`
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- User point: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-ARCHITECTURE.md)
- Contract: [MASTER–RAHM–CHILD promotion contract](../../reference/REFERENCE-DOCUMENTS/MASTER-RAHM-CHILD-PROMOTION-AND-INTERACTIVE-HOST-VERIFICATION-2026-10-26-001.md)
- Prior checkpoint: [CURRENT-078](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-078-REVERSIBLE-GRAPH-GAP-COVERS.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Observation
The user clarified the intended hierarchy: the original project is MASTER; the newer initial-model project is RAHM; a result becomes a newborn only after testing, validation and explicit master acceptance.

## Architecture decision recorded
Adopt the hierarchy as the governing design for future work. Keep the MASTER as canonical authority; treat the initial-model package as an isolated RAHM/test surface; use a candidate-to-newborn promotion gate. The RAHM must not overwrite master history or promote itself.

## Evidence boundary
This event records the user's architectural instruction and repository-side documentation work. It does not prove that a separate interactive project environment has been created, imported, restarted, or validated. Those checks require a real destination receipt.

## Required follow-up
- Read back POINT-0/032, this event and the promotion contract.
- Update both master and initial-model mothers plus index/queue/manifest references.
- Run exact-final-SHA audit and portable conformance.
- Keep CURRENT-065/CURRENT-066, EVT-0195 and all uncovered graph/provenance/parent gaps OPEN.
- Continue NEXT-051; do not create NEXT-052.
