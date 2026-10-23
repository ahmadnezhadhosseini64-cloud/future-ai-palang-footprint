# LAL-20261023-011 — Visible continuation and resumable work

- Stable ID: PALANG-LESSON-VISIBLE-CONTINUATION-2026-10-23-011
- Production ID: LAL-20261023-011
- Version: 1.0.0
- Status: REGISTERED / LIVING / EVOLVABLE
- Source event: [EVT-0113](../../BEHAVIOR-TRACE/EVT-0113-VISIBLE-CONTINUATION-AND-SOURCE-CLAUSE-EXCAVATION-2026-10-23.md)
- Input/output: [IN-024](../../../0.0/anchors/PALANG-0.0-IN-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md) / [OUT-024](../../../0.0/anchors/PALANG-0.0-OUT-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md)
- Governing master: [ULCG](../../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md)

## Observation

A user can reasonably interpret silence after a promise to continue as stopped work. The assistant must not represent tool activity as unattended background work, and must distinguish what was committed, what was read back, what tests passed, and what remains open.

## Rule

Every material interaction creates a linked graph node and must preserve the prior active queue. The assistant should execute a bounded work unit, publish a durable milestone with evidence, then continue from the same queue. If no tool call is running, do not imply work continues silently.

## Operational consequence

1. Resume from the latest checkpoint and read the open queue before selecting the next action.
2. Keep the current return point, new interaction anchors, and next checkpoint distinct.
3. Record source → rule → component → test → evidence → issue/gap → next action.
4. Test each capability at the scope claimed; static link validation is not runtime/cold-start proof.
5. Preserve failed runs and corrections as separate lineage events.
6. Report UTC repository commit time and the same instant in Tehran time only after the actual commit metadata is retrieved.
7. Keep Issue #20 (runtime/cold-start) and Issue #21 (historic source census) open until their own criteria pass.

## Status boundary

This is an architecture lesson derived from a direct user correction and the observed interaction. It does not prove host-wide automated capture.
