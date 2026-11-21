# CURRENT-126 — POINT-0++ / تکمیل معماری محیط کاری میزبان اول

- Parent point: POINT-0/072 (0++ continuation; no competing root).
- Input: [IN-116](PALANG-0.0-IN-20261121-116-FIRST-HOST-WORKSPACE-EXECUTION.md).
- Output: [OUT-115](PALANG-0.0-OUT-20261121-115-FIRST-HOST-WORKSPACE-EXECUTION.md).
- Event: [EVT-0292](../../architecture/BEHAVIOR-TRACE/EVT-0292-FIRST-HOST-WORKSPACE-EXECUTION-2026-11-21.md).
- Time binding: [TIME-BINDING-EVT-0292](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0292-FIRST-HOST-WORKSPACE-EXECUTION-2026-11-21.md).
- Previous checkpoint: CURRENT-125.
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Host identity: FIRST NEW HOST / FIRST_HOST / HOST-001.
- Authentication gate: OPEN / DEFERRED.
- Repository: READ-ONLY; write/delete/branch/PR/merge/release/admin DENIED.
- Workspace: owner-defined, explicitly provisioned, task-allowlisted execution only.
- Workspace-to-repository writeback: DENIED.
- Contract: [FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md).
- Status: POLICY DOCUMENTED ON PROPOSAL BRANCH / READ-BACK PENDING / MAIN NOT MERGED.
- Living master update: PENDING.
- Starter instructions/bootstrap update: PENDING.
- Index/manifest update: PENDING.
- Canonical ZIP rebuild/hash/receipt: PENDING.
- Technical enforcement: NOT VERIFIED.
- Independent-host acceptance: NOT RUN.
- Exact user-message time: UNKNOWN / UNVERIFIED.

## Scope
FIRST_HOST reads the canonical GitHub repository and executes only owner-defined tasks in the explicitly provisioned workspace. The host cannot change its own scope, add tools or destinations, request secrets in chat, or write back to the repository. The owner updates the canonical repository; the host retrieves changes read-only.

## Preserved open gates
All prior unresolved graph, identity, parent, time, clean-host, persistence, recovery and NEXT-051 tasks remain open. This checkpoint does not close or replace them.
