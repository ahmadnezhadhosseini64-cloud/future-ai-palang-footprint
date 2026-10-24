# LAL-20261024-013 — Current point 0 and living registration

- Stable ID: PALANG-LESSON-CURRENT-POINT-ZERO-LIVING-REGISTRATION-2026-10-24-013
- Production ID: LAL-20261024-013
- Version: 1.0.0
- State: REGISTERED; rule-to-test verification pending
- Source event: [EVT-0134](../../BEHAVIOR-TRACE/EVT-0134-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION-2026-10-24.md)
- Input/output: [IN-026](../../../0.0/anchors/PALANG-0.0-IN-20261024-026-REGISTER-CURRENT-POINT-0.md) / [OUT-026](../../../0.0/anchors/PALANG-0.0-OUT-20261024-026-REGISTER-CURRENT-POINT-0.md)
- Current/next anchors: [CURRENT-036](../../../0.0/anchors/PALANG-0.0-CURRENT-20261024-036-USER-REQUEST-AND-LIVING-REGISTRATION.md) / [NEXT-036](../../../0.0/anchors/PALANG-0.0-NEXT-20261024-036-HISTORIC-SOURCE-CENSUS-AND-COLD-START.md)

## Rule

Every explicit user-designated point 0 must be preserved as an append-only return node, and the next work unit must be anchored as a distinct 0.0 checkpoint. The new node must join—not replace—the existing history and open queue.

## Operational obligations

1. Preserve prior checkpoints and evidence; never silently overwrite or reset them.
2. Pair each interaction's input and output with independent stable IDs and cross-links.
3. Bind canonical repository timestamps to actual Git commit metadata (UTC first; Tehran derived from the same instant).
4. Maintain a living master and register links in the 0.0 index, behavior trace, lesson registry, source map, integration queue and initial-model master.
5. Use structural audit to enforce discoverability; read back all changed files independently.
6. State test scope honestly; registration alone does not prove runtime capture, cold-start recovery or external destination persistence.
7. Every response/work unit must expose visible status and a deterministic next action.

## Test obligations

- Static graph: every required artifact exists and references CURRENT-036, NEXT-036, IN-026, OUT-026, EVT-0134 and LAL-20261024-013.
- Reverse lookup: start from IN-026 and OUT-026 and recover the same event/master/current/next graph.
- Cold-start: resume from NEXT-036 without relying on conversational context; record exact evidence.
- Exact-head audit: after merge, run full audit on the exact final main SHA.
- Historical and runtime acceptance remain separate gates under Issues #21 and #20.

## Status

Governance rule is registered. CI enforcement, read-back, final-main audit and runtime recovery are separate evidence gates; do not conflate them.
