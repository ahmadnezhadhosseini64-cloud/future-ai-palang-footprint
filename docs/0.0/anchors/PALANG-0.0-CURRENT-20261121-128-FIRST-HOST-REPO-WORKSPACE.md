# CURRENT-128 — وضعیت جاری محیط کاری میزبان اول

- Status: ACTIVE / LIVING / FIRST-HOST-REPO-WORKSPACE
- Canonical root: POINT-0 (single root); 0++ remains a marker on the same root.
- Parent checkpoint: CURRENT-127
- Point: POINT-0/075
- Input/output: IN-118 → OUT-117
- Event/time: EVT-0294 → TIME-BINDING-EVT-0294
- Sole next queue: NEXT-051
- Main base SHA observed: e267c3f6f9254ef06cef38d2a5b8209a0756e5cd
- Working branch: haif/point-0-075-first-host-repo-workspace

## Three owner tasks
1. Mark this interaction and connect it to the single POINT-0 lineage — recorded in this chain.
2. Hammer-test and adapt the architecture for a real first-host repository workspace — handoff contract and bootstrap updated in this proposal branch.
3. Deliver the first-host startup document and obtain a real acceptance receipt — instructions prepared; actual new-host OAuth, execution, tests and receipt remain OPEN / NOT RUN until the owner starts the new host.

## Access architecture
- READ: authenticated GitHub connector for the canonical repository.
- EXECUTE: isolated host workspace / working checkout with real command and test execution.
- WRITE: host's own branch only, and only if destination GitHub connector actually grants Contents:write and push permission.
- MAIN: no direct host push; use PR and owner/repository policy for merge.
- Credentials: owner authorizes via secure platform UI; never in chat.
- A handoff document cannot itself create OAuth, a new remote model session, persistent storage or platform permissions.

## Verification
- Current assistant's GitHub connector: read access and branch creation/write on the proposal branch were exercised.
- New host connection: OPEN / NOT RUN.
- New host test execution: OPEN / NOT RUN.
- Package rebuild/exact-HEAD receipt: OPEN / NOT VERIFIED.
- 0.0 graph and NEXT-051 remediation: OPEN / LIVING / IN PROGRESS.
- Overall: HANDOFF_PREPARED / FIRST_HOST_NOT_YET_ACCEPTED.

No new root, parallel queue, fabricated timestamp, or inferred PASS is introduced.
