# LAL-20261023-012 — Visible status is part of resumable architecture

- Stable ID: PALANG-LESSON-STATUS-TRANSPARENCY-RESUMABLE-EXECUTION-2026-10-23-012
- Production ID: LAL-20261023-012
- Version: 1.0.0
- Status: REGISTERED; read-back pending
- Source: [EVT-0114](../../BEHAVIOR-TRACE/EVT-0114-STATUS-TRANSPARENCY-AND-RESUMABLE-EXECUTION-2026-10-23.md)
- Input/output: [IN-025](../../../0.0/anchors/PALANG-0.0-IN-20261023-025-STATUS-AND-VISIBLE-CONTINUATION.md) / [OUT-025](../../../0.0/anchors/PALANG-0.0-OUT-20261023-025-STATUS-AND-VISIBLE-CONTINUATION.md)
- Current point 0: [CURRENT-023](../../../0.0/anchors/PALANG-0.0-CURRENT-20261023-023-USER-CHECKPOINT-AND-CONTINUATION.md)
- Next checkpoint: [NEXT-025](../../../0.0/anchors/PALANG-0.0-NEXT-20261023-025-SOURCE-RULE-TEST-CROSSWALK-AND-COLD-START.md)
- Master: [ULCG](../../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md)

## Lesson

A user must be able to distinguish working, blocked, finished and not started from visible evidence. Silence is not a reliable progress signal and must not be described as background execution. Each work unit should produce a small, durable milestone: what changed, where it is recorded, what was read back, which test ran, what remains open, and the next deterministic action.

## Operational rules

1. State the work state before lengthy execution and after each meaningful milestone.
2. Continue the existing queue and preserve previous checkpoints; do not let a new input erase the old workstream.
3. Register each material IN/OUT pair, event, source, rule, version, time binding and parent/next edge.
4. Separate source retrieval, rule extraction, semantic adjudication, implementation, read-back, validation, merge and runtime proof as distinct statuses.
5. Do not claim automatic capture or background execution without runtime evidence.
6. A successful candidate-branch audit is not a successful audit of the final main HEAD.
7. If an operation fails or a tool returns no result, expose that limitation and retain the failure evidence.

## Acceptance criteria

- IN-025 and OUT-025 are independently retrievable and cross-linked.
- EVT-0114 and LAL-20261023-012 are present in their registries.
- The master, source map, queue, initial-model master, reference index and 0.0 registry link to this event without replacing CURRENT-023 or NEXT-025.
- Structural CI checks required files and link IDs.
- Read-back and applicable audit evidence are recorded; open runtime/historical gates remain open.
