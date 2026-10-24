# NEXT-042 — بستهٔ رحم، آزمون پذیرش و انتقال میان میزبان‌های AI

- Stable ID: `G6IP-RAHM-NEXT-042-20261024`
- Production ID: `G6IP-NEXT-042`
- Version: 1.0.0
- Status: OPEN / NOT RUN
- Parent: [CURRENT-044 — Rahm Point 0.0](./PALANG-0.0-CURRENT-20261024-044-RAHM-PROJECT-POINT-0.0.md)
- Point 0: [G6IP Rahm Point 0](./GPT6-RAHM-PROJECT-POINT-0-2026-10-24-001.md)
- Governing HAIF mother: [HAIF mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Inherited architecture mother: [GPT6 inherited architecture](../../reference/REFERENCE-DOCUMENTS/GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md)
- GPT-6 living master: [GPT-6 living master](../../reference/REFERENCE-DOCUMENTS/GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001.md)

## Goal
Create a self-contained portable Rahm package that allows an AI host to understand the architecture, declare its capabilities, preserve the current state and evidence, perform the documented tests it can support, and report unsupported operations honestly.

## Required deliverables
1. `RAHM_BOOT.md`: host startup contract, role, rules, status vocabulary, and first-response checklist.
2. `RAHM_ARCHITECTURE.md`: Master → Rahm → Validation → Child → Master lifecycle and feedback loops.
3. `HOST_CAPABILITY_MANIFEST.json`: declared host capabilities; distinguish provided, unavailable, and untested.
4. `INTERACTION_PAIR_SCHEMA.json`: schema for IN/OUT, observation, hypothesis, evidence, failure, correction, user feedback and lineage.
5. `EVIDENCE_LEDGER.md`: source, timestamp, repository commit, hashes where available, status and unresolved gaps.
6. `CONFORMANCE_TESTS.md`: measurable positive and negative cases.
7. `EXPORT_MANIFEST.json`: exact paths, versions, IDs, integrity digests and dependencies.
8. `RECOVERY_AND_ROLLBACK.md`: fresh-host recovery, no-silent-overwrite, version rollback and open-gap preservation.

## Minimum conformance tests
- Fresh host can explain the mission and current checkpoint from the package alone.
- Host distinguishes instruction from evidence and proposal from approved change.
- UTC commit time and Tehran equivalent are not invented; unknown user-message times remain unknown.
- Missing file, broken link, duplicate ID, contradictory evidence, partial import and unavailable tools produce explicit failures/open gates.
- IN/OUT pairs link to events, current checkpoint, mother and next action.
- Host capabilities are declared, not assumed; background execution and persistent memory are never claimed without proof.
- A new Child candidate is not promoted to Master without acceptance criteria, evidence, review and read-back.
- Export manifest matches exact artifact paths and integrity digests.
- Repeat test after restart and compare recovered state with the original evidence ledger.

## Cross-host protocol
First run in a clean GPT-6 context. Then select an independently available second AI host and run the same package and test cases. Record host name/version, date, provided files, tool capability, outputs, failures and evidence. Do not claim all AI hosts are compatible from one successful test.

## Pass criteria
Every mandatory case is either PASS with retained evidence or explicitly FAIL/UNSUPPORTED; no silent data loss; IDs/versions/links match; current checkpoint and next action survive restart; and the test can be independently repeated. Unsupported features may be reported, but cannot be falsely marked PASS.

## Status
This is an execution plan only. Package creation, integrity digests, runtime behavior capture, GPT-6 clean-context recovery and second-host test remain NOT RUN until independently evidenced.
