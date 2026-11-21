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

## Subsequent package verification

- Package 0.4.7 verified by workflow 44920781712 on main SHA 06f7fe5a00ea507b1930ffe8a74bc03caf1ff059.
- 19 files; 256684 bytes; 24/24 extracted tests PASS; ZIP CRC, source-byte read-back, exact artifact-ID download, paired master 1.7.86 byte match and artifact round-trip PASS.
- Inner ZIP SHA-256: a8a34580722573aaef247acbf9d7edf1d97a80025c49d510f07a1479da4f0a05. Durable release tag haif-latest-verified refreshed.
- Old direct artifact REST curl failure remains historical; PR #73 replaced it with actions/download-artifact@v4 and the corrected run passed.
- Master advances to 1.7.87; next package target 0.4.8 awaits a fresh exact-main receipt.

## Evidence boundary
بستهٔ 0.4.6 روی source commit 0d27972ac4d45349a85551f52e3b969ee581f843 ساخته شده؛ main در ثبت این نقطه 6ab35232404e2c5d37d48698db5d02821681b126 است. مقایسهٔ Git نشان می‌دهد اختلاف پس از build فقط سه commit مستنداتی/رسید است؛ دو commit Evidence Gate و receipt و هم‌ارزی منبع در gate اجرا شده است. استخراج artifact و اجرای مجدد 24 آزمون از فایل ZIP دانلودشده نیز PASS شد. این، package verification است؛ نه clean-host acceptance.


## Latest package verification — internal 0.4.8

- Workflow 44921364797 succeeded on source/current main SHA 680a1f788a50e38da4b71768f8291dde0eeeaa31.
- Package identity and canonical ZIP filename unchanged; internal version 0.4.8; 19 files; 257102 bytes; 24/24 extracted tests PASS.
- CRC, source-byte read-back, exact artifact-ID download, paired living master 1.7.87 byte match, downloaded artifact round-trip and durable release publication PASS.
- Inner ZIP SHA-256: 1e1bbab0c7acb0975b77176abc5c38f7e7097cfe8cf67b17153ffe1db4da65a6.
- Package 0.4.7 and its receipt remain preserved as the previous verified version. Independent-host acceptance remains OPEN / NOT RUN.
