# NEXT-038 — گام بعدی: تثبیت نقطهٔ ۰ و سپس نقطهٔ ۰.۰

- Stable ID: `PALANG-NEXT-GPT6-POINT-0-THEN-0.0-2026-10-24-038`
- Production ID: `G6IP-NEXT-038`
- Status: OPEN / ACTIVE / LIVING / NOT EXECUTED
- Parent current: [CURRENT-039](./PALANG-0.0-CURRENT-20261024-039-GPT6-INITIAL-POINT-AND-ZERO-CHAIN.md)
- Pair: [IN-029](./PALANG-0.0-IN-20261024-029-DECLARE-INITIAL-POINT-AND-LINK-ZERO-CHAIN.md) ↔ [OUT-029](./PALANG-0.0-OUT-20261024-029-DECLARE-INITIAL-POINT-AND-LINK-ZERO-CHAIN.md)
- Event: [EVT-0137](../../architecture/BEHAVIOR-TRACE/EVT-0137-GPT6-INITIAL-POINT-ZERO-CHAIN-2026-10-24.md)
- Master: [GPT-6 interactive project living master](../../reference/REFERENCE-DOCUMENTS/GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001.md)

## Ordered execution
### Step A — point 0
1. بازخوانی CURRENT-039، سند مبنای Project Zero و سند مادر.
2. تعریف قرارداد پروژه بر اساس این ریشه: دامنه، مرزهای میزبان، خروجی تعاملی موردنظر، حریم خصوصی، قواعد شواهد، معیارهای پذیرش و وابستگی‌های باز.
3. ساخت پروندهٔ مستقل نقطهٔ ۰ با شناسهٔ یکتا و پیوند به CURRENT-039 و EVT؛ به‌روزرسانی سند مادر بدون حذف تاریخچه.
4. بازخوانی فایل و سند مادر، تطبیق شناسه‌ها/نسخه/پیوندها و ثبت زمان واقعی commit به UTC و معادل تهران.
5. تکمیل نقطهٔ ۰ فقط پس از شواهد معیارهای پذیرش.

### Step B — point 0.0
1. ساخت چک‌پوینت مستقل و قابل‌بازیابی بر مبنای نتیجهٔ تأییدشدهٔ نقطهٔ ۰.
2. ثبت آخرین گام تأییدشده، کار باقی‌مانده، موانع، اقدام بعدی، مسیر شواهد و وضعیت هر مقصد.
3. اتصال نقطهٔ ۰.۰ ↔ نقطهٔ ۰ ↔ CURRENT-039 ↔ IN/OUT ↔ EVT ↔ سند مادر.
4. بازخوانی و تطبیق زنجیره؛ آزمون بازیابی تا اجرای واقعی NOT RUN می‌ماند.

### Step C — behavior tracking
هدف قابل‌مشاهدهٔ کاربر، اقدام دستیار، نتیجهٔ ابزار/مخزن، خطا و اصلاح، بازخورد صریح در صورت وجود و شواهد ثبت شوند. واقعیت از فرضیه جدا باشد؛ ارتقای Child به معماری مادر از دروازهٔ بررسی Rahm عبور کند.

## Acceptance gates
- شناسه‌های یکتا و نسخه؛ همهٔ پیوندها به مسیرهای واقعی مخزن برسند.
- زمان commit واقعی UTC و معادل تهران از همان لحظه.
- بازخوانی و تطبیق دقیق شناسه/محتوا.
- نقطهٔ ۰ و نقطهٔ ۰.۰ دو پروندهٔ مستقل و قابل‌بازیابی باشند.
- هیچ لنگر تاریخی یا مسئلهٔ باز حذف یا بی‌صدا بسته نشود.

## Status boundary
این صف اجراست، نه مدرک اجرا. نقطهٔ ۰: NOT CREATED / NOT RUN. نقطهٔ ۰.۰: NOT CREATED / NOT RUN. نمونهٔ تعاملی و بازیابی سرد: NOT RUN.
