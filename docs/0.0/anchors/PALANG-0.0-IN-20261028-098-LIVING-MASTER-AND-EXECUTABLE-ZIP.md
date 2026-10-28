# IN-098 — ورودی: اجرای واقعی سند مادر و ZIP به‌جای گزارش صرف

- Stable ID: HAIF-IN-098-LIVING-MASTER-EXECUTION-20261028
- Point: [POINT-0/060](./GPT6-RAHM-USER-POINT-0-20261028-060-LIVING-MASTER-AND-EXECUTABLE-ZIP.md)
- Output: [OUT-097](./PALANG-0.0-OUT-20261028-097-LIVING-MASTER-AND-EXECUTABLE-ZIP.md)
- Event: [EVT-0237](../../architecture/BEHAVIOR-TRACE/EVT-0237-POINT-060-LIVING-MASTER-AND-EXECUTABLE-ZIP-2026-10-28.md)
- Current: [CURRENT-110](./PALANG-0.0-CURRENT-20261028-110-LIVING-MASTER-AND-EXECUTABLE-ZIP.md)
- Active queue: NEXT-051 only; no NEXT-052.
- User-message time: UNKNOWN / UNVERIFIED.
- Status: REGISTERED; repository persistence must be confirmed by post-write read-back.

## Input
User correction: prior assistant replies appeared to be reports rather than actual development of the living master and the ZIP with the capabilities the project intends to deliver.

## Operational acceptance criteria
- Living master must be updated from current repository evidence, not from stale summaries.
- Existing canonical starter ZIP must be rebuilt in place from its source folder; do not create a parallel package.
- Included LIVING_MASTER_REFERENCE.md must be byte-consistent with the master source used for that same build.
- Record actual archive SHA-256, byte count, file inventory and extracted test results from the workflow artifact, not inferred values.
- Run current-main audit and portable conformance against the exact same candidate SHA.
- External-host import and restart recovery require direct host evidence; keep OPEN until received.
- All collision history and 0+ highlights remain preserved.


## Current recovery links (continuity contract)
- Checkpoint: [CURRENT-110](./PALANG-0.0-CURRENT-20261028-110-LIVING-MASTER-AND-EXECUTABLE-ZIP.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living master: [canonical living master](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Host recovery protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md](../../reference/REFERENCE-DOCUMENTS/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)

These links preserve repository-level recoverability only. External-host import, negative-control, restart, persistent memory, Buffer, Dropbox, automatic capture and background execution remain OPEN / NOT VERIFIED until direct evidence exists.
