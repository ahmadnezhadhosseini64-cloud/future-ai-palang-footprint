# OUT-095 — اجرای گام بازیابی مستقل: پروتکل عملیاتی و مرز نتیجه

- Stable ID: HAIF-OUT-095-POINT-058-INDEPENDENT-HOST-RECOVERY-20261028
- Point: [POINT-0/058 (۰+)](./GPT6-RAHM-USER-POINT-0-20261028-058-0PLUS-INDEPENDENT-HOST-RECOVERY.md)
- Input: [IN-096](./PALANG-0.0-IN-20261028-096-POINT-058-INDEPENDENT-HOST-RECOVERY.md)
- Event: [EVT-0233](../../architecture/BEHAVIOR-TRACE/EVT-0233-POINT-058-INDEPENDENT-HOST-RECOVERY-2026-10-28.md)
- Current: [CURRENT-108](./PALANG-0.0-CURRENT-20261028-108-INDEPENDENT-HOST-RECOVERY.md)
- Queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Status: PROTOCOL PREPARED / EXTERNAL EXECUTION OPEN

## Work advanced
The recovery task is now specified as a falsifiable host acceptance test, not a general request to “read the ZIP”. It requires paired artifact delivery, exact identity read-back, reconstruction of the 0+/0.0 chain, negative-control behavior, fresh-session/restart testing, raw evidence preservation, hashing and independent read-back.

## Execution record
- Package source identity remains `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
- Canonical ZIP name remains `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Internal version remains `0.3.8`.
- The previously verified ZIP digest belongs to its own specific build only; it must not be copied onto a rebuilt artifact.
- No independent host response or host export is available in this execution context. Therefore no external-host PASS, restart-persistence PASS, or second-host PASS is recorded.

## Acceptance matrix
| Gate | Required evidence | Status |
|---|---|---|
| Paired ZIP + mother reference delivered to external host | Delivery/session receipt | OPEN |
| Host reconstructs project from artifacts | Raw host answer + read-back | OPEN |
| Exact IDs and chain returned correctly | Comparison record | OPEN |
| Negative control detects missing/altered anchor | Test input/output | OPEN |
| Fresh session/restart recovery | Second-session raw output | OPEN |
| Raw receipt integrity | SHA-256 + independent read-back | OPEN |

## Next action
Use a separate AI host/session with both artifacts. Paste the recovery prompt from CURRENT-108, save the raw response without editing, then add its real hash and a read-back comparison to NEXT-051 evidence. Keep unresolved gates open.


## Exact package receipt — Portable Conformance run 40644166088

- Source commit for this build: `76122145020a5a55e31375dd02c190abadff59bb`.
- Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Internal package version: `0.3.8`; Stable ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
- Size: `101556` bytes; SHA-256: `330f6aab2f2b98959f1155099d20d344b20448cbdceaf2b765dce5a25f842177`.
- Inventory: 13 files, including `LIVING_MASTER_REFERENCE.md` and `INDEPENDENT_HOST_ACCEPTANCE_PROMPT_FA.md`.
- ZIP integrity: PASS; source-byte read-back: PASS; extracted package tests: 23/23 PASS. Downloaded artifact was independently extracted and hashed in this session; digest and byte count matched the workflow receipt.
- Workflow: [Portable Conformance run 40644166088](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40644166088).
- External independent-host acceptance: NOT RUN. This receipt is package/repository evidence only.
