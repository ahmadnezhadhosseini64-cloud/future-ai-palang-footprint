# POINT-0/079 — تفکیک نسخهٔ شدنی از توسعهٔ باز

- Status: ACTIVE / LIVING / OWNER-APPROVED / IMPLEMENTATION-IN-PROGRESS
- Parent: CURRENT-131
- Previous point: POINT-0/078
- Input/output: IN-122 → OUT-121
- Event/time: EVT-0299 → TIME-BINDING-EVT-0299
- Target checkpoint: CURRENT-132
- Sole governing queue: NEXT-051
- Canonical root: POINT-0 (۰.۰؛ این شماره نقطهٔ موازی یا ریشهٔ تازه نیست)

## قصد مالک
نسخهٔ قابل‌تحویل باید آخرین نسخهٔ واقعاً شدنی و اثبات‌شده باشد. هر قابلیت قابل‌اجرا پس از پیاده‌سازی و آزمون به Latest Runnable وارد می‌شود. قابلیت ناقص، وابسته به میزبان، ناممکن در محیط فعلی یا فاقد شاهد حذف نمی‌شود؛ در Development / OPEN / BLOCKED با علت و معیار تبدیل به شدنی باقی می‌ماند.

## قاعدهٔ وابستگی قدیمی
کشف وابستگی قدیمی به‌خودی‌خود مانع نسخهٔ بسته نیست. ابتدا دامنهٔ اثر آن مشخص می‌شود:
- اگر فقط یک قابلیت یا یک مسیر میزبان را محدود کند، همان قابلیت باز می‌ماند و سایر قابلیت‌های مستقلِ اثبات‌شده منتشر می‌شوند.
- اگر آزمون نشان دهد به هسته، صحت داده، امنیت، استخراج، بازیابی یا یکپارچگی بسته آسیب می‌زند، فقط همان انتشار/قابلیت متأثر تا رفع یا جداسازی وابستگی متوقف می‌شود.
- نام، نسخه، منشأ، مصرف‌کنندگان، اثر، workaround و معیار حذف/ارتقا ثبت می‌شوند. وابستگی قدیمی بی‌صدا پاک یا پنهان نمی‌شود.

## زنجیره
POINT-0/077 → CURRENT-130 → POINT-0/078 → IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → POINT-0/079 → IN-122 → OUT-121 → EVT-0299 → TIME-BINDING-EVT-0299 → CURRENT-132 → NEXT-051.

## قاعدهٔ نسخه
- Latest Runnable: فقط قابلیت‌های پیاده‌سازی‌شده و آزموده‌شده با شاهد روی منبع/محیط مشخص.
- Development: قابلیت‌های ناقص، وابسته، میزبان‌محور، فاقد آزمون یا منتظر مجوز.
- Historical: نسخه‌ها، شکست‌ها، وابستگی‌های قدیمی و receiptهای قبلی حفظ می‌شوند.
- Promotion: پس از implementation + positive/negative tests + exact source + receipt/hash + read-back + reconciliation.
- Package identity و نام ZIP canonical ثابت می‌ماند؛ نسخهٔ داخلی فقط با تغییر واقعی و آزمون‌شده بالا می‌رود.

هیچ‌کدام از OAuth مقصد، workspace پایدار، clean-host recovery، restart recovery یا HOST-RECOVERED بدون رسید مستقیم میزبان بسته تلقی نمی‌شود.


## بازیابی و اتصال
- Previous checkpoint: [CURRENT-131](PALANG-0.0-CURRENT-20261121-131-UNIVERSAL-HOST-INITIAL-RUNNABLE.md)
- Input: [IN-122](PALANG-0.0-IN-20261121-122-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Output: [OUT-121](PALANG-0.0-OUT-20261121-121-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Event: [EVT-0299](../../architecture/BEHAVIOR-TRACE/EVT-0299-LATEST-RUNNABLE-OPEN-DEVELOPMENT-2026-11-21.md)
- Time: [TIME-BINDING-EVT-0299](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0299-LATEST-RUNNABLE-OPEN-DEVELOPMENT-2026-11-21.md)
- Current: [CURRENT-132](PALANG-0.0-CURRENT-20261121-132-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
