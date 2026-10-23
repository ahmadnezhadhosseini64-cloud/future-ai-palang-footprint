# LAL-20261023-006 — بررسی منفی کاذب سامانهٔ ارزیابی

- Stable ID: PALANG-ARCH-LESSON-AUTOMATED-FALSE-NEGATIVE-INVESTIGATION-2026-10-23-006
- Production ID: LAL-20261023-006
- Version: 1.0.0
- Status: REGISTERED / SOURCE-LINKED / VALIDATION PARTIAL / LIVING
- Source event: [EVT-0035](../../BEHAVIOR-TRACE/EVT-0035-BEHAVIOR-EVALUATOR-FALSE-NEGATIVE-C4-2026-10-22.md)
- Related test: [Behavior Observatory Recovery Test](../../BEHAVIOR-OBSERVATORY/BEHAVIOR-OBSERVATORY-RECOVERY-TEST-2026-10-22-001.md)

## Lesson
خروجی منفی یک ارزیاب خودکار، یافته‌ای برای بررسی است نه حکم قطعی. باید با منبع مستقل مقایسه شود و هم نتیجهٔ اولیه و هم اصلاح آن حفظ شوند.

## Operational rule
On an unexpected automated FAIL, preserve the run, inspect the source of truth, verify the exact criterion, determine whether the failure is a product defect or evaluator false-negative, and append a correction record without deleting the initial result.

## Acceptance criteria
- Initial output and its tested version remain retrievable.
- The source-of-truth comparison is explicit.
- Any criterion change is distinguished from a corrected interpretation.
- A regression test covers the corrected case where practical.

## Evidence boundary
The referenced incident and recovery test document the prior case. No new evaluator test was run by creating this lesson; runtime validation remains scoped to its actual test evidence.
