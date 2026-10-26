# OUT-060 — Excavation Findings and Dual-Path Execution Decision

- Stable ID: HAIF-OUT-060-EXCAVATION-DUAL-PATH-20261026
- Production ID: HAIF-OUT060-20261026
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Root: [POINT-0/025](./GPT6-RAHM-USER-POINT-0-20261026-025-EXCAVATION-FINDINGS-DUAL-PATH.md)
- Input: [IN-061](./PALANG-0.0-IN-20261026-061-EXCAVATION-FINDINGS-DUAL-PATH.md)
- Event: [EVT-0191](../../architecture/BEHAVIOR-TRACE/EVT-0191-EXCAVATION-FINDINGS-DUAL-PATH-2026-10-26.md)
- Current: [CURRENT-072](./PALANG-0.0-CURRENT-20261026-072-DUAL-PATH-EXCAVATION.md)
- Existing queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Decision
Advance the project through two parallel but separately verified paths.

### Path A — initial model
Inspect exact-head workflow receipts and package integrity; verify current bundle/manifests and recovery acceptance. Keep independent-host import, second host, host persistence, automatic capture and background execution open until directly tested.

### Path B — architecture remediation
Continue NEXT-051. Rerun the graph audit and adjudicate collision groups and ambiguous parent/time edges individually. Reconcile CURRENT-065/CURRENT-066 using provenance and consumer evidence.

### Shared invariants
No arbitrary pointer winner, bulk deletion, speculative renumbering, silent overwrite, or cosmetic NEXT-052. A write is not read-back; read-back is not validation; CI is not independent-host acceptance. Record the exact revision and evidence for every closure.

This output records the decision and work plan; it does not falsely claim all technical gates are already passed.