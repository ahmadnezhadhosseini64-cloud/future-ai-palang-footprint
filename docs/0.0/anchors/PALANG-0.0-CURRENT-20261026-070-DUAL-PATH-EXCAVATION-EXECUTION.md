# CURRENT-070 — Dual-Path Excavation Execution

- Stable ID: HAIF-CURRENT-070-DUAL-PATH-EXCAVATION-20261026
- Production ID: HAIF-C070-20261026
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/023](./GPT6-RAHM-USER-POINT-0-20261026-023-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION.md)
- IN: [IN-053](./PALANG-0.0-IN-20261026-053-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION.md)
- OUT: [OUT-053](./PALANG-0.0-OUT-20261026-053-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION.md)
- Event: [EVT-0186](../../architecture/BEHAVIOR-TRACE/EVT-0186-EXCAVATION-FINDINGS-AND-DUAL-PATH-CONTINUATION-2026-10-26.md)
- Previous checkpoint: [CURRENT-069](./PALANG-0.0-CURRENT-20261025-069-PORTABLE-STARTER-ENGINE-AND-GATE-CLOSURE.md)
- Existing remediation queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Operating rule
Path A and Path B are both mandatory. They share the root/event/current state but retain separate acceptance gates. Progress on one never closes or substitutes for the other.

## Path A — initial model construction
- [ ] Fetch latest exact-head workflow runs for portable conformance and Living Architecture Audit; identify tested commit SHA for each.
- [ ] Read latest exact-head run/job/step receipts and confirm manifest digests and package artifact metadata; rerun only where the current revision has changed or evidence is stale.
- [ ] Verify starter/runtime source, tests and portable bundle inventory on that exact revision.
- [ ] Preserve independent AI-host import, second-host import, real host persistence/restart, automatic capture and idle/background execution as OPEN until directly tested in an authorized runtime.

## Path B — existing architecture remediation
- [ ] Rerun current graph audit and retain its raw receipt; do not treat historical collision counts as current counts.
- [ ] Continue item-by-item adjudication of Stable-ID, Production-ID, Reference-ID, event-number collisions, ambiguous parents and ambiguous timestamps.
- [ ] Reconcile CURRENT-065 / CURRENT-066 provenance and consumers; remain AMBIGUOUS/BLOCKED until evidence determines the pointer.
- [ ] Keep Issue #20, Issue #21, BOART-FOLLOWUP-01 and other open findings in NEXT-051 unless evidence justifies a documented destination change.

## Shared integration
- [ ] Update and read back canonical reference index and main integration queue for POINT-0/023, IN-053, OUT-053, EVT-0186 and CURRENT-070.
- [ ] Independently fetch all new artifacts and compare identifiers, version, status and relative links.
- [ ] Update the living master only after locating its canonical path and checking current blob/version; do not guess its path or overwrite a different master.
- [ ] Record actual commit timestamp from Git metadata as canonical repository time in UTC and its equivalent Asia/Tehran time.
- [ ] Reconcile this checkpoint against both paths and latest exact-head receipts.

## Acceptance criteria
- [ ] New root/IN/OUT/event/CURRENT files independently read back with matching content and IDs.
- [ ] Reference index and queue point to the new root/current checkpoint while NEXT-051 remains active.
- [ ] Latest exact-head CI and package evidence is inspected; no stale run is represented as current.
- [ ] Path A and Path B both have a completed, evidenced next action or an explicit blocker.
- [ ] All unresolved host and graph gates remain OPEN; no speculative closure or bulk renumbering.
- [ ] A user-visible milestone is delivered without claiming background execution.

## Status boundary
This checkpoint is OPEN / EXECUTION REQUIRED. The registration write alone does not mean the full acceptance criteria are satisfied.