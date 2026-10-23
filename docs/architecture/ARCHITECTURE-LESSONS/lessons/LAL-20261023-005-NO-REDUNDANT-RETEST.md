# LAL-20261023-005 — عدم تکرار آزمون معتبر بدون محرک

- Stable ID: PALANG-ARCH-LESSON-NO-REDUNDANT-RETEST-2026-10-23-005
- Production ID: LAL-20261023-005
- Version: 1.0.0
- Status: REGISTERED / SOURCE-LINKED / LIVING
- Canonical source: [REG-2026-09-03-NO-REDUNDANT-RETEST-001](../../../registrations/REG-2026-09-03-NO-REDUNDANT-RETEST-001.md)
- Rule ID: NO-REDUNDANT-RETEST-2026-09-03-001
- Related master: [CMIND](../../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)

## Lesson
یک آزمون بسته‌شده با نتیجهٔ صحیح و شاهد معتبر، بدون تغییر یا نیاز واقعی نباید دوباره اجرا شود. شواهد موفق معتبر باید بازیابی و استفاده شوند؛ آزمون‌های جدید فقط وقتی اجرا می‌شوند که محرک مشخص وجود داشته باشد.

## Operational rule
TEST → CORRECT RESULT → RECORD → VERIFY → CLOSE → DO NOT REPEAT.
Retest only on material change, deployment, new need, error, regression, contradictory evidence or recovery. Record the trigger and the exact scope retested.

## Acceptance criteria
- Prior run and tested version can be identified.
- The decision to reuse or rerun cites a trigger or explicitly records no trigger.
- A repeated test does not overwrite the previous result.
- New failures become regression evidence.

## Evidence boundary
The canonical registration is the source of truth. This derivative lesson does not replace or duplicate its authority.
