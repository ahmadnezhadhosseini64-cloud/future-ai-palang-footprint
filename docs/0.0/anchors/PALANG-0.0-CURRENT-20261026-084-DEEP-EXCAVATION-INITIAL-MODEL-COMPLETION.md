# CURRENT-084 — Deep Excavation and Initial Model Completion

- Stable ID: HAIF-CURRENT-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-20261026
- Production ID: HAIF-C084
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Chain: [IN-072](./PALANG-0.0-IN-20261026-072-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md) → [OUT-071](./PALANG-0.0-OUT-20261026-071-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md) → [EVT-0206](../../architecture/BEHAVIOR-TRACE/EVT-0206-POINT-0-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-2026-10-26.md)
- Previous execution checkpoint: [CURRENT-083](./PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Existing active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Live repository observations before this checkpoint
- Main was read back at SHA `a406683307d5b90b8302bd40a34801723a8b5c00`.
- `scripts/build_historical_graph_manifest.py` imports both `graph_identifier_roles.metadata_header` and `parent_edge_resolution.resolve_parent_target`.
- Unit tests exist for both helper modules, and the living audit workflow contains explicit unittest and py_compile steps for them. Therefore the earlier CURRENT-083 statement that these helpers were not yet wired into CI is stale and must be reconciled with current receipts.
- Recent workflow receipts on this head include successful Pending Registration Drain, Production Detection Safety Net and Reconciliation Watchdog. These are not a substitute for the living graph audit and portable RAHM conformance.
- The latest known graph-audit baseline from the prior CURRENT-083 is 4 missing local links, 2 unresolved parent edges, 0 ambiguous parent edges, 63 Stable-ID groups, 92 Production-ID groups, 7 Reference-ID groups and 41 event-number groups. Treat these as a historical baseline only, not current counts.

## Path A — executable initial model
- Local runtime and portable RAHM package must build and pass integrity/import/export/recovery tests on the same exact SHA.
- Independent GPT-host import, restart, round-trip, automatic capture, background runtime and durable host persistence are NOT RUN until real destination receipts are supplied.
- MASTER remains governing authority; RAHM is the validation environment; CHILD promotion requires independent evidence and explicit acceptance.

## Path B — repository excavation and graph repair
- Rerun the living graph audit after the identifier parser and parent resolver changes.
- Read the generated audit artifact back; record exact SHA, digest and current counts.
- Review the 4 historical missing-link findings and fix only links whose intended target is evidenced.
- Adjudicate Stable-ID, Production-ID, Reference-ID and event-number groups in small batches, retaining role decisions and source hashes.
- Reconcile CURRENT-065/CURRENT-066 lineage using provenance and consumers, not number ordering.
- Keep unresolved and ambiguous cases OPEN; preserve NEXT-051 and do not create NEXT-052.

## Acceptance gate
CURRENT-084 stays OPEN until the exact-head audit and portable conformance have both completed, their logs/artifacts have been read back, and graph changes are reconciled in the master/index/queue. External-host acceptance remains a separate gate.