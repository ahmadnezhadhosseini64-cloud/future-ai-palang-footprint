# EVT-0107 — چرخهٔ زندهٔ درس‌های معماری، راستی‌آزمایی و بازگشت

- Stable ID: EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23
- Production ID: EVT-0107
- Version: 1.0.0
- Status: REGISTERED / READ-BACK PENDING / INTEGRATION OPEN
- Parent master: [CMIND](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Lesson registry: [ARCHITECTURE-LESSONS](../ARCHITECTURE-LESSONS/README.md)
- Primary lesson: [LAL-20261023-001](../ARCHITECTURE-LESSONS/lessons/LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md)
- Previous route correction: [EVT-0106](./EVT-0106-RESUME-HAIF-EXECUTION-NOT-DROPBOX-2026-10-23.md)
- Related behavioral discovery correction: [EVT-0103](./EVT-0103-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22.md)

## Trigger
کاربر درخواست کرد تمام درس‌ها، اسناد، قواعد و اجزای پروژه دائمی، زنده، پیوسته به‌روز، آزمون‌پذیر، نسخه‌پذیر و قابل بازیابی باشند؛ نسخهٔ جدید نباید روی نسخهٔ قبلی نوشته شود.

## Hard-audit findings
- Existing architecture registry and living architecture file already define version succession and historical retrieval.
- Existing live inbox provides intake/triage for lessons and errors.
- Existing behavior trace records lessons such as missed behavior-hunter detection, identifier collision and path drift.
- Before this event, a dedicated, canonical directory for the complete lesson inventory and its per-lesson lifecycle/verification protocol was not evidenced by the inspected paths.
- Existing structural audit script checks a fixed set of repository paths/IDs; it does not by itself prove runtime lesson enforcement, host-wide capture, or rollback behavior.
- Therefore the architecture is partially present, but end-to-end automatic lesson capture, activation, retesting and rollback are not yet proven.

## Architectural decision
Create a dedicated append-only Architecture Lessons registry; route each material lesson through classification, operational rule, test criteria, real evidence, read-back, reconciliation, activation and revalidation. Preserve every old version and failed attempt. Promote only evidence-backed successors. In case of regression, restore the last verified baseline explicitly, retain the failed version and turn the failure into a regression test.

## Verification boundaries
- Repository artifacts: this event's files must be fetched after write and matched.
- Runtime behavior: no new runtime test was executed in this event.
- Full historic lesson migration: OPEN.
- Automatic collection of every future interaction: OPEN / NOT PROVEN.
- External destinations: NOT ATTEMPTED.
- Do not claim permanent host-level enforcement solely because the repository rule exists.

## Next actions
1. Read back registry, lesson and event; verify IDs and links.
2. Reconcile master, reference index, behavior trace, integration queue, live inbox and 0.0.
3. Add the lesson registry and acceptance gates to the structural audit workflow/script.
4. Inventory and migrate historical lessons with provenance; do not merge duplicates until semantically adjudicated.
5. Implement or verify automated candidate extraction and regression checks under Issue #20.
6. Test restoration from a known-good commit and document the recovery evidence.

## Lesson
A living architecture is not merely a document that says “living”. It must have a versioned state transition, an executable verification gate, immutable history, a recoverable baseline and evidence-driven revalidation. If any of these are absent, the gap remains visible and open.
