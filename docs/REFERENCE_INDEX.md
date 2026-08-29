# Reference Index

**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** ACTIVE  
**Last Verified:** 2026-08-29

## Canonical References

| ID | Document | Role | Status |
|---|---|---|---|
| SRC-2026-08-29-001 | `docs/STABLE_RETRIEVAL_CORE.md` | Stable external retrieval contract | VERIFIED / ACTIVE |
| RRT-2026-08-29-001 | `docs/RETRIEVAL_RUNTIME.md` | Operational retrieval sequence | VERIFIED / ACTIVE |
| EGE-2026-08-29-001 | `docs/EVIDENCE_GATE.md` | Independent execution evidence contract | PROVEN / ACTIVE / CLOSED / PASS |
| CHK-2026-08-29-001 | `docs/CHECKPOINT.md` | Current verified checkpoint | VERIFIED / ACTIVE |
| REF-GITHUB-2026-08-29-001 | Repository access reference | GitHub connection and repository access | VERIFIED / ACTIVE |

## Evidence Gate Proof

The Evidence Gate requirement E2 + E3 + E4 is verified by successful `Evidence Gate - Independent Execution Test` workflow execution. The latest verified run is **Run #7**, triggered by push to `main` at commit `c557be1cbfb518eb7066d0b15b4bf52fed2de5e9`. The run completed with `success` and produced an inspectable GitHub Actions trace.

## Consistency State

The canonical recovery documents are synchronized to the current verified state:

- Stable Retrieval Core = **VERIFIED / ACTIVE**.
- Retrieval Runtime = **VERIFIED / ACTIVE**.
- Evidence Gate = **PROVEN / ACTIVE / CLOSED / PASS**.
- Checkpoint = **VERIFIED / ACTIVE**.
- The obsolete `NOT YET PROVEN` Evidence Gate state is no longer canonical.
- The obsolete `actions/checkout@v4` warning is historical evidence only; the active workflow uses `actions/checkout@v5`.

## Rule

This index is a navigation layer, not a substitute for the referenced evidence. Each status must be supported by the underlying repository artifact or an explicit verification result.

## 0.0

At `0.0`, retrieval precedes response: retrieve the canonical source, verify its state, reconcile contradictions, report evidence boundaries, then continue.
