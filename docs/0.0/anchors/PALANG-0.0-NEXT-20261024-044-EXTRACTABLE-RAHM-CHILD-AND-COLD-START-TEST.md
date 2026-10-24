# NEXT-044 — آزمون بستهٔ قابل استخراج و بازیابی در میزبان تازه

- Stable ID / شناسهٔ پایدار: `PALANG-NEXT-EXTRACTABLE-RAHM-CHILD-COLD-START-2026-10-24-044`
- Production ID / شناسهٔ تولید: `G6IP-NEXT-044`
- Version / نسخه: `1.0.0`
- Status / وضعیت: OPEN / PENDING TEST; not passed.
- Current checkpoint / نقطهٔ جاری: [CURRENT-047](./PALANG-0.0-CURRENT-20261024-047-FOUNDATIONAL-GOVERNANCE-AND-RECOVERY.md)
- Living mother / سند مادر زنده: [NPFAP v1.0.9](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Engine / موتور کشف: [Adaptive Discovery v1.1.0](../../../architecture/ADAPTIVE-DISCOVERY-CROSS-PLAYGROUND.md)

## Objective / هدف
Produce a portable, host-independent package that can reconstruct the project's current architecture and continuation state in a fresh AI host or clean context without relying on hidden chat memory.

## Required package / اجزای بسته
- Master and architecture principles, including additive versioning and Child → Rahm → Master validation.
- Current 0.0 anchor and complete IN/OUT/EVT/NEXT lineage with repository URLs, IDs, versions, and commit-based UTC timestamps plus Tehran equivalents.
- Discovery engine protocol, source ledger schema, provenance, finding statuses, contradictions, failed checks, and open gaps.
- Explicit project boundaries, second-project adapter contract, and truthful list of integrations not verified.
- Recovery instructions, acceptance criteria, integrity digests where available, and a deterministic next-action pointer.

## Test protocol / روش آزمون
1. Export the package from the repository at a named commit and record its SHA and contents.
2. Start in a fresh host/context with no assumed access to prior conversation memory.
3. Import/read the package and reconstruct current anchor, mother version, IN/OUT/EVT chain, engine rules, open gates, and next action.
4. Compare every recovered ID, path, link, version, and digest against repository read-back.
5. Run negative cases: missing file, broken link, duplicate ID, contradictory finding, unavailable source, and incomplete import.
6. Record each result with its own timestamp, evidence, failure details, and correction; do not overwrite earlier test results.
7. Pass only if reconstruction is repeatable and all mandatory links and open gates are preserved.

## Acceptance criteria / معیار پذیرش
- [ ] Export artifact exists at a verifiable path and has a recorded integrity digest.
- [ ] Fresh-host reconstruction performed and evidenced.
- [ ] CURRENT-047 and its IN-040 / OUT-039 / EVT-0147 chain, parent CURRENT-046, NPFAP v1.0.9, discovery engine v1.1.0, and NEXT-044 are recovered and matched.
- [ ] Preserve the historical IN-038 / OUT-038 / EVT-0146 chain and its links.
- [ ] Broken-link, missing-file, duplicate, contradiction, and partial-import cases are handled without silent data loss.
- [ ] The exact next action and all unresolved gaps survive restart.
- [ ] Results are read back from the destination and linked into the mother/index.

## Boundary / مرز
This is a test plan, not evidence of a successful export or recovery. Exportability, fresh-host adoption, recovery, and unattended execution remain unverified until the test is run and recorded.