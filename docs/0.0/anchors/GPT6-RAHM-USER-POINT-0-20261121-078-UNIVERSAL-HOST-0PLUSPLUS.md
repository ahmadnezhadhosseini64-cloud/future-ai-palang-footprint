# POINT-0/078 — نقطهٔ ۰++ برای نسخهٔ اولیهٔ شدنی

- Status: ACTIVE / LIVING / OWNER-APPROVED / IMPLEMENTATION-IN-PROGRESS
- Parent: CURRENT-130
- Previous point: POINT-0/077
- Input/output: IN-121 → OUT-120
- Event/time: EVT-0298 → TIME-BINDING-EVT-0298
- Target: CURRENT-131
- Sole queue: NEXT-051

مالک این تعامل را نقطهٔ ۰++ جدید در همان ریشهٔ POINT-0 تعیین کرد. نسخهٔ آماده باید به نسخهٔ اولیهٔ شدنی تبدیل شود و استخراج، بازیابی و تداوم را پوشش دهد. قابلیت‌های ناقص یا اثبات‌نشده حذف نمی‌شوند؛ در Development / OPEN باقی می‌مانند و فقط پس از پیاده‌سازی، آزمون، receipt و read-back به Latest Runnable ارتقا می‌یابند.

## Rules
1. Latest Runnable فقط قابلیت‌های پیاده‌سازی‌شده و آزموده‌شده با شواهد روی منبع مشخص را شامل می‌شود.
2. Development قابلیت‌های ناقص، میزبان‌وابسته یا فاقد آزمون مستقیم را نگه می‌دارد.
3. تاریخچه، شکست‌ها، نسخه‌های قدیمی و digestهای قبلی پاک یا بازنویسی نمی‌شوند.
4. ادغام سند، PASS شدن CI، ساخت ZIP، OAuth، workspace و پذیرش میزبان وضعیت‌های مستقل‌اند.

## Chain
POINT-0/077 → CURRENT-130 → POINT-0/078 → IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → NEXT-051.

OAuth مقصد، workspace پایدار، clean-host recovery، restart recovery و HOST-RECOVERED تا رسید مستقیم OPEN / NOT RUN می‌مانند. NEXT-051 تنها صف فعال است؛ ریشه یا صف موازی ایجاد نکن.
