# Portable Living Master Reference — POINT-0/GOLDEN

- Version / نسخه: 1.7.95
- Package version: 0.5.1 candidate (same stable package ID and canonical ZIP filename)
- Current chain: POINT-0/GOLDEN → IN-130 → OUT-129 → EVT-0309 → TIME-BINDING-EVT-0309 → CURRENT-140 → NEXT-051
- Canonical root: one existing POINT-0 root; this file is a portable pointer, not a second master.
- Governing source: ../../docs/architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md
- Golden baseline: ../../docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md
- Current checkpoint: ../../docs/0.0/anchors/PALANG-0.0-CURRENT-20261122-140-GOLDEN-BASELINE.md
- Sole active queue: ../../docs/0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md
- Reference Index: ../../docs/REFERENCE_INDEX.md

## Governing host and RAHM rules

1. Every host has PUBLIC READ ONLY access to the canonical master. No host may write to any master branch, create a master PR, or use a broker, worker, token, App or intermediary to route host-originated writes into the master.
2. Each host works only in its own isolated runtime and, if owner-provisioned, its own private repository. No host may access another host's workspace.
3. RAHM is central, private, owner-only and outside every host workspace. Hosts have no read/write/admin/token/App access to RAHM.
4. Only the owner can command monitoring, inspect accessible host sources, export and redact selected material, and place it into private RAHM.
5. Promotion is owner export → private RAHM → reconciliation/validation → trusted bot-authored PR to CHILD → owner review/approval. CHILD is not MASTER.
6. A new host is not ACTIVE until identity, isolated workspace, connector scope, persistence and acceptance receipt are independently verified.
7. Historical snapshots and old host-intake instructions are evidence only; they cannot override POINT-0/GOLDEN or reopen settled decisions by themselves.

## Current operational status

- Main is protected by active Ruleset 27814009; approval count is still 0 and Code Owner review is OFF.
- Private RAHM repository and Promotion GitHub App are NOT CONFIGURED.
- No real host is registered or ACTIVE.
- Package v0.5.1 is a candidate; it is not verified until the exact-main Portable RAHM Conformance run succeeds.
- Clean-host import, independent recovery, second-host isolation and restart persistence remain OPEN / NOT RUN.

