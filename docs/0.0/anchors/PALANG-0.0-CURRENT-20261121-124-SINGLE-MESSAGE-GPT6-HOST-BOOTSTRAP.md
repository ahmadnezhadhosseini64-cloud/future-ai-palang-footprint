# CURRENT-124 — Single-message GPT-6 host bootstrap

- Status: ACTIVE / LIVING / PACKAGE BUILD PENDING / HOST NOT CONNECTED
- Parent: [CURRENT-123](PALANG-0.0-CURRENT-20261120-123-ISOLATED-HOST-WORKSPACES.md)
- Point: [POINT-0/071](GPT6-RAHM-USER-POINT-0-20261121-071-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-0PLUS.md)؛ 0++ همان ریشهٔ canonical صفر است.
- Input: [IN-114](PALANG-0.0-IN-20261121-114-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md)
- Output: [OUT-113](PALANG-0.0-OUT-20261121-113-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md)
- Event: [EVT-0289](../../architecture/BEHAVIOR-TRACE/EVT-0289-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-2026-11-21.md)
- Time: [TIME-BINDING-EVT-0289](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0289-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-2026-11-21.md)
- Master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Open gates
GitHub authorization/connector at destination, durable private workspace, host identity and owner approval, broker/worker, least-privilege credential, path allowlist, branch protection, negative cross-workspace tests, full state recovery from IN and OUT, clean host import, restart persistence, second-host import, automatic live message capture, idle/background capture, graph/identity/parent/time triage, duplicate IDs, ambiguous parents, CURRENT-065/CURRENT-066 conflict (no winner selected), Issue #20 and Issue #21 remain OPEN / NOT RUN.

## Chain
[POINT-0/071](GPT6-RAHM-USER-POINT-0-20261121-071-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-0PLUS.md) → [IN-114](PALANG-0.0-IN-20261121-114-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md) → [OUT-113](PALANG-0.0-OUT-20261121-113-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md) → [EVT-0289](../../architecture/BEHAVIOR-TRACE/EVT-0289-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-2026-11-21.md) → [CURRENT-124](PALANG-0.0-CURRENT-20261121-124-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md) → [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

- Mirror event: [EVT-0241](../../architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md)
- Mirror time: [TIME-BINDING-EVT-0241](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-2026-10-31.md)

NEXT-051 remains the sole active queue.

## Duplicate-ID reconciliation and canonical handoff
A concurrent alternate file set reused the same POINT-0/071, IN-114, OUT-113, EVT-0289 and TIME-BINDING-EVT-0289 IDs. Those files are marked QUARANTINED_DUPLICATE_ID_NONCANONICAL; the chain linked in docs/0.0/README.md remains canonical. ONE_MESSAGE_HOST_BOOTSTRAP_FA.md is the sole startup prompt in the next canonical ZIP. The superseded SINGLE_MESSAGE file is excluded from the archive. Package 0.4.3 build/read-back remains pending.
