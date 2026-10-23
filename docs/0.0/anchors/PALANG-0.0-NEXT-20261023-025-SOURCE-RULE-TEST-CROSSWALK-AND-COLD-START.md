# NEXT-025 — Source-rule-test crosswalk and cold-start recovery

- Stable ID: PALANG-0.0-NEXT-SOURCE-RULE-TEST-CROSSWALK-COLD-START-2026-10-23-025
- Production ID: NEXT-0.0-20261023-025
- Version: 1.0.0
- State: ACTIVE / LIVING / OPEN
- Current return point 0: [CURRENT-023](./PALANG-0.0-CURRENT-20261023-023-USER-CHECKPOINT-AND-CONTINUATION.md)
- Latest interaction: [IN-024](./PALANG-0.0-IN-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md) / [OUT-024](./PALANG-0.0-OUT-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md)
- Event/lesson: [EVT-0113](../../architecture/BEHAVIOR-TRACE/EVT-0113-VISIBLE-CONTINUATION-AND-SOURCE-CLAUSE-EXCAVATION-2026-10-23.md) / [LAL-20261023-011](../../architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-011-VISIBLE-CONTINUATION-AND-RESUMABLE-WORK.md)
- Master: [ULCG](../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md)
- Previous checkpoints preserved: [NEXT-022](./PALANG-0.0-NEXT-20261023-022-HISTORIC-SOURCE-GRAPH-EXCAVATION.md), [NEXT-023](./PALANG-0.0-NEXT-20261023-023-CONTINUITY-AND-OPEN-WORK.md), [NEXT-024](./PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md)
- Issue #21: historic source/rule census — OPEN.
- Issue #20: runtime capture, reverse lookup and cold-start recovery — OPEN.

## Immediate execution order

1. Complete the provisional source-rule-component-test crosswalk for PIATGCG, UIALAC, ICMCRR, H0GLMR and STAR-HCR using their exact fetched blob SHAs and clause headings.
2. Compare the five sources with the first 14 named-source batch and ULCG v1.2.1. Do not declare duplicate/equivalent rules unless source authority, scope, version and exact clauses align.
3. Add deterministic structural assertions for IN-024 / OUT-024 / EVT-0113 / LAL-011 / NEXT-025 and the source-clause matrix.
4. Run the audit against the candidate commit; preserve failure evidence and correct only the proven mismatch.
5. Merge only after applicable checks pass; then fetch the exact final main HEAD and seek a fresh full audit. Do not treat a PR-candidate run as final-main proof.
6. Continue Issue #21's full tree/history census and Issue #20's JSON Schema, IN/OUT reverse lookup and cold-start tests in parallel tracks.

## Completion criteria

- Source blob identities and retrieved contents are recorded.
- Each provisional rule has source clause, component, test/evidence, and open gap.
- All affected indexes and the living master link the new graph.
- Structural CI passes on exact candidate; full audit on final main is separately confirmed.
- Runtime-wide capture and cold-start remain NOT PROVEN until their own tests pass.
