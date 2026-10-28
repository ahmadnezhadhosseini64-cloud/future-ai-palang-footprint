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
