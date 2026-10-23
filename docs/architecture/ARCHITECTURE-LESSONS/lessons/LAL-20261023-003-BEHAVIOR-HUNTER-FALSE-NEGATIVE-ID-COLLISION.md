# LAL-20261023-003 — شکارچی رفتار، منفی کاذب و یکتایی شناسه

- Stable ID: PALANG-ARCH-LESSON-BEHAVIOR-HUNTER-FALSE-NEGATIVE-ID-COLLISION-2026-10-23-003
- Production ID: LAL-20261023-003
- Version: 1.0.0
- Status: REGISTERED / SOURCE-LINKED / RUNTIME OPEN / LIVING
- Source of truth: [EVT-0103](../../BEHAVIOR-TRACE/EVT-0103-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22.md)
- Related inbox: [INBOX-20261022-002](../../LIVE-INBOX/entries/INBOX-20261022-002.md)
- Governing master: [CMIND](../../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)

## Lesson
ثبت‌کردن یک خروجی به‌تنهایی تضمین نمی‌کند که کاندیدهای معماری از آن کشف شده باشند. شکارچی باید دو مسیر مکمل داشته باشد: ثبت تعامل و کشف رفتار. برخورد شناسه و منفی کاذب باید به‌عنوان رخداد حفظ شوند.

## Operational rule
قبل از write، یکتایی شناسه و تبار را بررسی کن؛ سپس ورودی/خروجی را برای کاندیدهای معماری ارزیابی کن و هر کاندید را OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN برچسب بزن. اگر ممیزی منفی داد، آن را با منبع واقعی تطبیق بده و نتیجهٔ اولیه و اصلاح‌شده را هر دو نگه دار.

## Acceptance criteria
- تست یکتایی شناسه پیش از ثبت وجود دارد.
- مسیر کشف رفتار از مسیر ثبت تعامل جدا و قابل‌آزمون است.
- خطاهای false-negative و اصلاح آن‌ها حذف نمی‌شوند.
- بازیابی از IN یا OUT به رویداد، نسخه، شاهد و شکاف ممکن است.

## Evidence boundary
EVT-0103 records the incident and required architecture. Issue #20 remains OPEN for runtime implementation, schema validation and cold-start recovery; this lesson is not proof that a background hunter is running.
