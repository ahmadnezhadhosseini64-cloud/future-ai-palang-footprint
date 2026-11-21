# EVT-0298 — نسخهٔ اولیهٔ شدنی و بازیابی عمومی میزبان

- Event ID: EVT-0298
- Status: ACTIVE / LIVING / OWNER-APPROVED / IMPLEMENTATION-IN-PROGRESS
- Date: 2026-11-21
- Point: POINT-0/078 (۰++)
- Input/output: IN-121 → OUT-120
- Parent checkpoint: CURRENT-130
- Result checkpoint: CURRENT-131
- Time evidence: TIME-BINDING-EVT-0298

## Trigger
مالک خواست این تعامل نقطهٔ ۰++ در امتداد ریشهٔ واحد POINT-0 باشد و دستور انتقال میزبان به نسخهٔ اولیهٔ شدنی، عمومی، قابل استخراج و قابل بازیابی تبدیل شود. قابلیت‌های اثبات‌نشده باید باز و در مسیر توسعه بمانند و فقط پس از پیاده‌سازی و آزمون واقعی به آخرین نسخهٔ شدنی ارتقا یابند.

## Action
- تعریف POINT-0/078 و زنجیرهٔ IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → NEXT-051.
- افزودن دستور عمومی میزبان به مخزن.
- تثبیت Latest Runnable و Development و دروازهٔ ارتقای مبتنی بر شواهد.
- تعریف گام‌های 0.0 برای بازیابی، تطبیق، آزمون، پذیرش میزبان و ارتقای قابلیت‌ها.
- حفظ تاریخچه و گپ‌ها؛ عدم ساخت ریشه یا صف موازی.

## Evidence boundary
ثبت مالک و آماده‌سازی سند، به‌تنهایی build تازهٔ ZIP، clean-host، OAuth، workspace پایدار، restart recovery یا HOST-RECOVERED را ثابت نمی‌کند. این موارد تا رسید مستقیم OPEN / NOT RUN باقی می‌مانند.
