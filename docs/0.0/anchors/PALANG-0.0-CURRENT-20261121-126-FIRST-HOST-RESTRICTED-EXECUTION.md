# CURRENT-126 — وضعیت معماری POINT-0++ / میزبان اول

- Parent: POINT-0/072 → CURRENT-125.
- Point: [POINT-0/073 / POINT-0++](GPT6-RAHM-USER-POINT-0-20261121-073-FIRST-HOST-RESTRICTED-EXECUTION-0PLUSPLUS.md).
- Input: [IN-116](PALANG-0.0-IN-20261121-116-FIRST-HOST-EXECUTION-BOUNDARY.md).
- Output: [OUT-115](PALANG-0.0-OUT-20261121-115-FIRST-HOST-EXECUTION-BOUNDARY.md).
- Event: [EVT-0292](../../architecture/BEHAVIOR-TRACE/EVT-0292-POINT-0PLUSPLUS-FIRST-HOST-RESTRICTED-EXECUTION-2026-11-21.md).
- Time binding: [TIME-BINDING-EVT-0292](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0292-FIRST-HOST-RESTRICTED-EXECUTION-2026-11-21.md).
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Contract: [FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md).
- Host: FIRST NEW HOST / FIRST_HOST / HOST-001.
- Authentication gate: OPEN / DEFERRED.
- Repository: PUBLIC / READ-ONLY.
- Workspace: owner-defined, explicitly provisioned, allowlisted execution only.
- Repository write/delete/commit/push/branch/PR/merge/release/settings/permission changes: DENIED.
- Workspace-to-repository writeback: DENIED.
- Master, bootstrap, host instructions, starter manifest and RAHM export manifest: updated on proposal branch; read-back required.
- Main integration: NOT MERGED.
- Canonical ZIP rebuild/hash/receipt: PENDING.
- Technical enforcement: NOT VERIFIED.
- Independent-host acceptance: NOT RUN.
- Exact user-message timestamp: UNKNOWN / UNVERIFIED.

## معیار پذیرش
Read succeeds; write attempt to canonical repository is denied; workspace boundary is enforced; allowlisted task runs; unapproved task/tool/destination is denied; workspace cannot write back; owner-published update is retrieved; verifiable receipt records source SHA, policy version, task ID and result.

## وضعیت
POLICY DESIGNED / SOURCE REGISTERED ON PROPOSAL BRANCH / MAIN NOT MERGED / ZIP NOT REBUILT / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN.
