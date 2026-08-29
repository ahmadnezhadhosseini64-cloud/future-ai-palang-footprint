# Reference Index

**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** ACTIVE  
**Last Verified:** 2026-08-29

## Canonical References

| ID | Document | Role | Status |
|---|---|---|---|
| SRC-2026-08-29-001 | `docs/STABLE_RETRIEVAL_CORE.md` | Stable external retrieval contract | VERIFIED / ACTIVE |
| EGE-2026-08-29-001 | `docs/EVIDENCE_GATE.md` | Independent execution evidence contract | PROVEN / ACTIVE / CLOSED / PASS |
| CHK-2026-08-29-001 | `docs/CHECKPOINT.md` | Current verified checkpoint | VERIFIED / ACTIVE |
| REF-GITHUB-2026-08-29-001 | Repository access reference | GitHub connection and repository access | VERIFIED / ACTIVE |

## Evidence Gate Proof

The Evidence Gate requirement E2 + E3 + E4 is verified by the successful `Evidence Gate - Independent Execution Test` workflow run triggered by push to `main` at commit `929d69e`. The run produced a successful `evidence-gate` job and an inspectable GitHub Actions trace.

## Rule

This index is a navigation layer, not a substitute for the referenced evidence. Each status must be supported by the underlying repository artifact or an explicit verification result.

## 0.0

At `0.0`, retrieval precedes response: retrieve the canonical source, verify its state, then continue.
