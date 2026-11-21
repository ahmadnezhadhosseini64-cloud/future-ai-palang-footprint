# EVT-0292 — تکمیل معماری FIRST_HOST و محیط کاری محدود

- Parent event: EVT-0291
- Point: POINT-0/072 (0++)
- Input: IN-116
- Output: OUT-115
- Host role: FIRST_HOST / HOST-001
- Authentication gate: OPEN / DEFERRED
- Contract: [FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md)
- Event time: PENDING exact final commit metadata.
- Exact user-message timestamp: UNKNOWN / UNVERIFIED.

## رفتار و تصمیم
میزبان اول به‌عنوان عامل اجرای محدود تعریف شد، نه مدیر مخزن. دسترسی مخزن فقط‌خواندنی است. اجرای وظایف فقط در workspace مشخص و واقعاً provision شده، بر اساس task authorization و allowlist مالک مجاز است. ابزار/مقصد تأییدنشده، مسیر خارج از workspace، افزایش خودسرانهٔ مجوز و هرگونه write-back به مخزن ممنوع است.

## زنجیرهٔ به‌روزرسانی
POINT-0/072 (0++) → IN-116 → OUT-115 → EVT-0292 → TIME-BINDING-EVT-0292 → CURRENT-126 → NEXT-051.

## مسیر سند مادر و workspace
متن مادر ارسالی مالک، ورودی bootstrap است. میزبان main HEAD و نسخهٔ canonical را بازیابی و با متن مقایسه می‌کند؛ اختلاف‌ها را آشکار ثبت می‌کند؛ snapshot محلی را به revision معتبر pin می‌کند؛ و فقط taskهای مالک‌تعریف‌شده را در workspace خصوصی و محدود اجرا می‌کند. هیچ خروجی به مخزن برنمی‌گردد.

## وضعیت شواهد
قرارداد و cross-referenceها روی شاخهٔ پیشنهاد ثبت می‌شوند. main integration، canonical ZIP rebuild/receipt، technical enforcement و independent-host acceptance تا آزمون و receipt واقعی NOT VERIFIED / NOT RUN می‌مانند.
