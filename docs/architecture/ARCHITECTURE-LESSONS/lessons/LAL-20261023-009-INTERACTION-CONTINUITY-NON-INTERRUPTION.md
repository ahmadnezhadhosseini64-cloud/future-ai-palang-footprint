# LAL-20261023-009 — Interaction continuity and non-interruption

- Stable ID: PALANG-LESSON-INTERACTION-CONTINUITY-NON-INTERRUPTION-2026-10-23-009
- Production ID: LAL-20261023-009
- Version: 1.0.0
- Status: ACTIVE / LIVING / SOURCE-LINKED; automated enforcement NOT PROVEN
- Source: user instruction recorded in [EVT-0111](../../BEHAVIOR-TRACE/EVT-0111-INTERACTION-CONTINUITY-NON-INTERRUPTION-2026-10-23.md)
- Governing master: [ULCG v1.1.0](../../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md)
- Prior lesson: [LAL-20261023-008](./LAL-20261023-008-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md)
- Prior checkpoint: [NEXT-022](../../../0.0/anchors/PALANG-0.0-NEXT-20261023-022-HISTORIC-SOURCE-GRAPH-EXCAVATION.md)
- Next checkpoint: [NEXT-023](../../../0.0/anchors/PALANG-0.0-NEXT-20261023-023-CONTINUITY-AND-OPEN-WORK.md)

## Lesson

Conversation continuity is an architectural property, not a conversational courtesy. A new user input creates a new node and a possible new branch of work, but it does not automatically supersede the active branch. The system must load the last verified checkpoint, restore the open-work queue, capture the new IN/OUT pair, classify the delta, link it to prior state, reconcile both tracks, execute the next unblocked action and publish a verifiable checkpoint.

## Operational obligations

1. Before starting new work, retrieve the last verified checkpoint and enumerate open work that remains relevant.
2. Preserve prior incomplete actions, errors, negative results, failed tests and source conflicts.
3. Register each material input and output with independent IDs, provenance and event/master linkage.
4. Connect predecessor/successor, source/rule/component/test/evidence/gap and next-action edges explicitly.
5. Keep parallel workstreams distinct when their acceptance criteria differ. Here, historical source census (#21) and runtime/cold-start acceptance (#20) remain independent and open.
6. Reprioritize only on explicit user direction or evidence-backed dependency; record the reason and preserve the prior state.
7. Do not claim automatic capture, background execution, read-back, validation or integration without the corresponding proof.
8. Use canonical repository commit time in UTC and derive Tehran time from the same instant; keep exact message time UNKNOWN if unavailable.
9. Verify the master, index, map, queue and checkpoint by read-back and compare them before marking the integration complete.

## Acceptance test candidates

- Given an active open checkpoint and a new input, the next-work state still contains both the prior open task and the new task.
- Reverse lookup from either IN or OUT resolves the paired anchor, event, master, related rules, prior checkpoint, open issues, evidence and successor.
- Replaying registration is idempotent and does not duplicate or overwrite existing canonical records.
- Cold-start reconstructs both the prior open-work queue and the new input's connected graph.
- CI verifies required continuity links and fails on missing predecessor or successor edges.

## Current test state

- Governance text and cross-links: registered on the update branch; final read-back pending.
- Fresh structural audit on final reconciled HEAD: OPEN.
- Runtime pair-ledger schema validation, reverse lookup and cold-start: OPEN under Issue #20.
- Historic source census and semantic reconciliation: OPEN under Issue #21.
