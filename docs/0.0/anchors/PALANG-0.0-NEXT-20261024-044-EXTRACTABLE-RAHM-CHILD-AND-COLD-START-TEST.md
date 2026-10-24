# NEXT-044 — آزمون بستهٔ قابل استخراج و بازیابی در میزبان تازه

- Stable ID / شناسهٔ پایدار: `PALANG-NEXT-EXTRACTABLE-RAHM-CHILD-COLD-START-2026-10-24-044`
- Production ID / شناسهٔ تولید: `G6IP-NEXT-044`
- Version / نسخه: `1.0.0`
- Status / وضعیت: OPEN / PENDING TEST; not passed.
- Current checkpoint / نقطهٔ جاری: [CURRENT-051](./PALANG-0.0-CURRENT-20261024-051-REPOSITORY-EXCAVATION-REVIVAL.md); historical recovery lineage includes [CURRENT-047](./PALANG-0.0-CURRENT-20261024-047-FOUNDATIONAL-GOVERNANCE-AND-RECOVERY.md)
- Living mother / سند مادر زنده: [NPFAP v1.1.6](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md); historical versions remain preserved.
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
- [ ] Current chain CURRENT-051 and IN-044 / OUT-043 / EVT-0151, parent CURRENT-050 and its IN-043 / OUT-042 / EVT-0150 lineage, NPFAP v1.1.6, discovery engine v1.1.0, and NEXT-044 are recovered and matched.
- [ ] Historical CURRENT-047 and its IN-040 / OUT-039 / EVT-0147 chain, parent CURRENT-046, and NPFAP v1.0.9 are also preserved and recoverable.
- [ ] Preserve the historical IN-038 / OUT-038 / EVT-0146 chain and its links.
- [ ] Broken-link, missing-file, duplicate, contradiction, and partial-import cases are handled without silent data loss.
- [ ] The exact next action and all unresolved gaps survive restart.
- [ ] Results are read back from the destination and linked into the mother/index.

## Boundary / مرز
This is a test plan, not evidence of a successful export or recovery. Exportability, fresh-host adoption, recovery, and unattended execution remain unverified until the test is run and recorded.

## Living excavation addendum — current target reconciliation — 2026-10-24

- Excavation event / رویداد خاک‌برداری: [EVT-0151](../../architecture/BEHAVIOR-TRACE/EVT-0151-REPOSITORY-EXCAVATION-LIVING-STATE-RECONCILIATION-2026-10-24.md).
- Current acceptance target / هدف پذیرش جاری: [CURRENT-050](./PALANG-0.0-CURRENT-20261024-050-NEW-PROJECT-ARCHITECTURE-STATUS.md), [IN-043](./PALANG-0.0-IN-20261024-043-NEW-PROJECT-ARCHITECTURE-STATUS-AND-LIVING-ANCHOR.md), [OUT-042](./PALANG-0.0-OUT-20261024-042-NEW-PROJECT-ARCHITECTURE-STATUS-AND-LIVING-ANCHOR.md), [EVT-0150](../../architecture/BEHAVIOR-TRACE/EVT-0150-NEW-PROJECT-ARCHITECTURE-STATUS-2026-10-24.md), [NPFAP v1.1.4](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md), and [Reference Index](../../REFERENCE_INDEX.md).
- Historical lineage / تبار تاریخی: CURRENT-047, IN-040, OUT-039, EVT-0147 and NPFAP v1.0.9 remain preserved and must still be represented in the export as historical context; they are no longer the sole/current acceptance target.
- Updated mandatory checks: export the current CURRENT-050 chain and living mother; compare IDs, paths, versions and hashes; preserve CURRENT-047 and earlier chains; test fresh-context reconstruction and negative cases; report failures and unresolved gates without promoting untested states.
- Current repository excavation found this task's original target stale. This additive correction does not claim export, import, fresh-host reconstruction, second-project integration, or unattended execution has passed.
- Status remains OPEN / NOT RUN until a verifiable export artifact and independent fresh-context recovery evidence are read back and matched.
