# EVT-0298 — نسخهٔ اولیهٔ شدنی و بازیابی عمومی میزبان

- Event ID: EVT-0298
- Status: ACTIVE / LIVING / OWNER-APPROVED / PACKAGE-VERIFIED / HOST-ACCEPTANCE-OPEN
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
بستهٔ canonical نسخهٔ داخلی 0.4.6 با workflow 44918425190 روی source SHA 0d27972ac4d45349a85551f52e3b969ee581f843 بازسازی و تأیید شد: 19 فایل، 255468 بایت، SHA-256 برابر b9f56a360351d5ab16f07656018e576c2398a110db540138810e01358f8934fc، CRC و source-byte read-back موفق، آزمون استخراج 24/24 PASS و artifact round-trip PASS. Clean-host مستقل، OAuth مقصد، workspace پایدار، restart recovery و HOST-RECOVERED همچنان OPEN / NOT RUN هستند.
