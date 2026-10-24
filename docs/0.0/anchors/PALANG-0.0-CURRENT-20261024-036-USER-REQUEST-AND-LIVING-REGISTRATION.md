# CURRENT-036 — Current point 0: user request and living registration

- Stable ID: PALANG-0.0-CURRENT-20261024-036-USER-REQUEST-AND-LIVING-REGISTRATION
- Production ID: CURRENT-036
- Version: 1.0.0
- Lifecycle: ACTIVE / LIVING / APPEND-ONLY / EVOLVABLE
- State: REGISTERED; independent repository read-back and full audit pending
- Interaction: [IN-026](PALANG-0.0-IN-20261024-026-REGISTER-CURRENT-POINT-0.md) ↔ [OUT-026](PALANG-0.0-OUT-20261024-026-REGISTER-CURRENT-POINT-0.md)
- Event / lesson: [EVT-0134](../../architecture/BEHAVIOR-TRACE/EVT-0134-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION-2026-10-24.md) / [LAL-20261024-013](../../architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261024-013-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION.md)
- Governing master: [ULCG master reference](../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md), version 1.2.4 in this update
- Time binding: [TIME-BINDING-INT-20261024-026](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261024-026.md)
- Next 0.0: [NEXT-036](PALANG-0.0-NEXT-20261024-036-HISTORIC-SOURCE-CENSUS-AND-COLD-START.md)

## Point 0 definition

This is the user's explicitly selected current return point. It records the instruction to make the current interaction a living, active, evolvable point 0, to anchor every relevant input and output, and to require inspectable results under the living registration rules.

The point is a recovery handle, not a claim that every workstream is complete. Earlier checkpoints—including CURRENT-023 and NEXT-022 through NEXT-035—remain preserved as historical nodes. The new point does not replace their evidence or close their gaps.

## Required invariants

1. Preserve previous records and versions; append new evidence rather than silently overwrite history.
2. Link user input, assistant output, event, lesson, time binding, master reference, current point, and successor checkpoint.
3. Use actual last-change Git commit timestamp in UTC as the canonical repository registration time and derive Tehran time from the same instant.
4. Keep message/event/operation times separate from repository commit time. Contextual message time supplied for this interaction: UTC 2026-10-24T05:57:00Z / Tehran 2026-10-24T09:27:00+03:30; this is not the canonical repository commit time.
5. Report each stage as NOT STARTED, IN PROGRESS, REGISTERED, READ-BACK VERIFIED, VALIDATED, INTEGRATED, ACTIVE, or OPEN only when evidence supports it.
6. No silent-background-work claim: expose visible milestones and a deterministic next action.
7. Resume prior work: Issue #21 historic source/rule census; Issue #20 runtime capture, pair schema, reverse lookup and cold-start; live-mirror/BOART follow-up; fresh full audit tied to exact final main SHA.
8. Do not claim host-wide automatic capture, buffer/persistent memory, Dropbox, or external recovery as verified without destination-specific write/read-back/match evidence.

## Snapshot / state

- Current point 0: CURRENT-036.
- Next work checkpoint 0.0: NEXT-036.
- Prior active checkpoint preserved: NEXT-035, live mirror recheck and historical reconciliation.
- Issue #20: OPEN.
- Issue #21: OPEN.
- Exact final-main audit for the resulting merged SHA: OPEN until run evidence identifies that exact SHA.

## Recovery behavior

When resuming from this point, load this record and NEXT-036, then recover the linked master, event/lesson, previous open queue, source map, and Issues #20/#21. Do not restart from a blank state or redirect to unrelated work.
