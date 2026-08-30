# Integration Registration Matrix

**ID:** REG-MATRIX-ICG-2026-08-30-001
**Architecture:** ARCH-ICG-2026-08-30-001
**Reference:** REF-ICG-2026-08-30-001
**Status:** ACTIVE / CANONICAL

For every production that enters registration or recovery, the system MUST maintain explicit states for the applicable project layers and reconcile them until closure.

| Layer | Required decision | State | Evidence | Integrated project location | Verification |
|---|---|---|---|---|---|
| Production | REQUIRED | — | — | — | — |
| Reference | REQUIRED / N/A | — | — | — | — |
| Architecture | REQUIRED / N/A | — | — | — | — |
| Canonical Repository | REQUIRED / N/A | — | — | — | — |
| Persistent Memory | REQUIRED / N/A | — | — | — | — |
| Runtime / Playground | REQUIRED / N/A | — | — | — | — |
| Checkpoint / Anchor | REQUIRED / N/A | — | — | — | — |
| Recovery / Pending | REQUIRED when incomplete | — | — | — | — |
| Production Registry | REQUIRED / N/A | — | — | — | — |
| Living Documentation | REQUIRED / N/A | — | — | — | — |
| Evidence | REQUIRED | — | — | — | — |
| Verification | REQUIRED | — | — | — | — |

## Closure rule

The matrix MUST NOT be marked FINAL/PROVEN while any REQUIRED row is PENDING, FAILED, UNAVAILABLE, or lacks the evidence required by the applicable gate.

A recovery record may remain as provenance after successful reconciliation, but closure requires verified integration into the applicable live project locations.
