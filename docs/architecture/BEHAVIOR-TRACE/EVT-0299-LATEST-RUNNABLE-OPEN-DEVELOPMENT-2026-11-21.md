# EVT-0299 — آخرین نسخهٔ شدنی و توسعهٔ باز

- Event ID: EVT-0299
- Status: ACTIVE / LIVING / OWNER-APPROVED / REPOSITORY-IMPLEMENTATION
- Date: 2026-11-21
- Point: POINT-0/079 (۰++)
- Input/output: IN-122 → OUT-121
- Parent checkpoint: CURRENT-131
- Result checkpoint: CURRENT-132
- Time evidence: TIME-BINDING-EVT-0299

## Trigger
مالک خواست نسخهٔ شدنی از آخرین نسخهٔ واقعاً اثبات‌شده ساخته شود و قابلیت‌های ناقص/وابسته باز و فعال بمانند. وابستگی قدیمیِ کشف‌شده نباید مانع انتشار قابلیت‌های مستقل شود.

## Action
- ثبت POINT-0/079 در همان ریشهٔ canonical و اتصال به CURRENT-131/NEXT-051.
- تعریف Latest Runnable، Development / OPEN و Historical.
- تعریف روش triage برای وابستگی قدیمی بر اساس دامنهٔ اثر.
- تعریف گام‌های 0.0.1 تا 0.0.9 با معیار پذیرش.
- حفظ بستهٔ canonical 0.4.6 و receipt آن با دامنهٔ source مشخص؛ عدم ادعای پذیرش میزبان مقصد.
- حفظ همهٔ گیت‌های باز و نسخه‌های قبلی.

## Evidence boundary
بستهٔ 0.4.6 روی source commit 0d27972ac4d45349a85551f52e3b969ee581f843 ساخته شده؛ main در ثبت این نقطه 6ab35232404e2c5d37d48698db5d02821681b126 است. مقایسهٔ Git نشان می‌دهد اختلاف پس از build فقط سه commit مستنداتی/رسید است؛ دو commit Evidence Gate و receipt و هم‌ارزی منبع در gate اجرا شده است. استخراج artifact و اجرای مجدد 24 آزمون از فایل ZIP دانلودشده نیز PASS شد. این، package verification است؛ نه clean-host acceptance.
