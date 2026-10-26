# CURRENT-084 — Deep Excavation and Initial Model Completion

- Stable ID: HAIF-CURRENT-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-20261026
- Production ID: HAIF-C084
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Chain: [IN-072](./PALANG-0.0-IN-20261026-072-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md) → [OUT-071](./PALANG-0.0-OUT-20261026-071-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md) → [EVT-0206](../../architecture/BEHAVIOR-TRACE/EVT-0206-POINT-0-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-2026-10-26.md)
- Previous execution checkpoint: [CURRENT-083](./PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Canonical time binding: [POINT-0/036 chain time binding](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-POINT-0-036-CHAIN-2026-10-26.md)
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

## Verified audit receipt — prior exact head
- Living Architecture Audit run [40347006195](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40347006195) passed on exact SHA cf877f9a84d767bb6f0f3566b90efe4fd5dcd83c; artifact ID 12661441741, digest sha256:3e937e32efd25bb71db2e471a49f8c7b2961302ce2ee4bb0e514bef824ac2ab8.
- In that run: helper tests passed (5 parent resolver tests and 4 metadata-header tests); compile checks passed; local Markdown links missing = 0; manifest decode errors = 0; unresolved parent edges = 2; ambiguous parent edges = 0.
- Manifest semantic collision classes: 23 Stable-ID groups (1 unreviewed/open), 68 Production-ID groups (66 unreviewed/open), 5 Reference-ID groups (5 open), 41 event-number groups (3 unreviewed/open), 11 exact-content duplicate groups.
- The separate raw graph report still showed 63/92/7/41 raw collision counts and flagged two generated Python bytecode files as decode errors. This revealed that the raw audit was still scanning body references and bytecode unlike the canonical manifest.
- Corrective change on a later commit: scripts/audit_historical_0_0_graph.py now excludes __pycache__/.pyc and derives identifier/parent definitions from the bounded metadata header. This correction is awaiting exact-head rerun; do not mark it validated until that run finishes.

## Acceptance gate
CURRENT-084 stays OPEN until the exact-head audit and portable conformance have both completed, their logs/artifacts have been read back, and graph changes are reconciled in the master/index/queue. External-host acceptance remains a separate gate.