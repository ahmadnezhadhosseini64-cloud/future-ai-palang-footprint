# NEXT-036 — Historic source census, runtime recovery, and exact-head audit

- Stable ID: PALANG-0.0-NEXT-20261024-036-HISTORIC-SOURCE-CENSUS-AND-COLD-START
- Production ID: NEXT-036
- Version: 1.0.0
- State: ACTIVE / LIVING / OPEN / RESUMABLE
- Parent current point: [CURRENT-036](PALANG-0.0-CURRENT-20261024-036-USER-REQUEST-AND-LIVING-REGISTRATION.md)
- Interaction anchors: [IN-026](PALANG-0.0-IN-20261024-026-REGISTER-CURRENT-POINT-0.md) / [OUT-026](PALANG-0.0-OUT-20261024-026-REGISTER-CURRENT-POINT-0.md)
- Event / lesson: [EVT-0134](../../architecture/BEHAVIOR-TRACE/EVT-0134-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION-2026-10-24.md) / [LAL-20261024-013](../../architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261024-013-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION.md)
- Governing master: ULCG v1.2.4
- Read-back evidence: [VERIFICATION-CHECKPOINT-INT-20261024-026](../../architecture/BEHAVIOR-TRACE/VERIFICATION-CHECKPOINT-INT-20261024-026.md)
- Time binding: [TIME-BINDING-INT-20261024-026](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261024-026.md)

## Why this is the next 0.0

This checkpoint continues the active execution chain. It does not reset or replace NEXT-022 (historic graph excavation), NEXT-025 (source-rule/test crosswalk and cold start), or NEXT-035 (live mirror recheck). It joins those strands under a single resumable queue while preserving each strand's own evidence and acceptance boundary.

## Ordered execution queue

1. **Historic source census — Issue #21 OPEN.** Enumerate repository files and history; reconcile named canonical source families and aliases; extract rules clause-by-clause; record source blob SHA, path, version, provenance and conflict status; do not label the census complete while sources remain unenumerated.
2. **Rule-to-component-to-test mapping.** Extend the current provisional crosswalk beyond its existing five-source batch. For each rule, name the governing component, implementation/guard, test, evidence, and gap. Resolve conflicting source clauses with provenance; do not silently merge.
3. **Runtime behavior hunter / recovery — Issue #20 OPEN.** Validate IN/OUT pairing schema, append-only persistence, reverse lookup from either anchor, restart/cold-start recovery, and destination-specific read-back. Keep host-wide capture NOT PROVEN until an executable test passes.
4. **Live mirror / BOART follow-up.** Preserve NEXT-034/NEXT-035 and their evidence; continue BOART-FOLLOWUP-01 and the uncoached fresh-session recovery gate. Do not rewrite Library content if semantic/source comparison shows no drift.
5. **Exact-main audit.** After this checkpoint is integrated, run the full Living Architecture Audit against the exact final main SHA; store run ID, tested SHA, full step outcomes, and result. Prior candidate-tree PASS does not satisfy this gate.
6. **Read-back and reconciliation.** Re-fetch all artifacts, compare Stable IDs, Production IDs, Version, status, next action, and links. Record mismatches as gaps and repair through append-only updates.
7. **Visible milestone contract.** At every meaningful work unit, state what was written, what was independently read back, which tests passed, which gaps remain, and the next deterministic action. Do not imply work continues during silence.

## Acceptance gates

- G1: Every new interaction has IN, OUT, EVT, lesson, time binding, current/next anchor, master and index links.
- G2: Current point and next checkpoint are discoverable from both master and 0.0 index.
- G3: Audit script checks these new links and required IDs.
- G4: All changed files independently read back and reconciled.
- G5: PR candidate audit passes; final main audit is separately tied to the exact merged SHA.
- G6: Issues #20 and #21 remain OPEN until their own runtime and historical acceptance criteria pass.

## Open boundaries

- Historical census completeness: OPEN.
- Runtime/host-wide interaction capture: NOT PROVEN.
- Cold-start recovery: OPEN.
- Buffer / persistent memory destination: NOT VERIFIED unless independently evidenced.
- Dropbox: OPEN / NOT VERIFIED; do not switch to Dropbox unless the user explicitly reopens that track.
- External end-to-end recovery: NOT RUN.
- Exact-final-main full audit: OPEN until run evidence matches final SHA.
