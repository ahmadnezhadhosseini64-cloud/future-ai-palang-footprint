# Integration Completion Gate — Enforcement Contract

**ID:** ARCH-ICG-ENF-2026-08-30-001
**Gate:** ARCH-ICG-2026-08-30-001
**Status:** ACTIVE / ENFORCEMENT CONTRACT

## Enforcement requirement

A registration/reconciliation operation MUST NOT be considered complete merely because a recovery file, reference file, or single destination was written.

The operation must establish, for each applicable destination, both:

1. the destination's actual registration/integration state; and
2. evidence and verification sufficient to support that state.

## Integration targets

Where applicable, reconciliation MUST propagate the production into the project's live structures, including Reference/Registry, Architecture placement, Living Documentation, Checkpoint/Continuation state, and other designated runtime or project locations.

## Closure gate

`CLOSE` is permitted only when all applicable required integration states are successfully evidenced and verified. Otherwise the production remains `PENDING` or `INCOMPLETE` and its recovery/reconciliation path remains active.

## Anti-archive-only invariant

`RECOVERY FILE EXISTS` does not imply `PROJECT INTEGRATED`.

`REFERENCE FILE EXISTS` does not imply `PROJECT INTEGRATED`.

`SINGLE DESTINATION WRITE` does not imply `REGISTRATION COMPLETE`.

Only verified cross-layer integration may satisfy the gate.
