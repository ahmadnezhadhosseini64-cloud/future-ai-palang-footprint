# IN-116 — تکمیل معماری اجرایی میزبان اول و تثبیت نقطهٔ ۰++

- Parent point: POINT-0/072 — 0++ (continuation/overlay؛ بدون ساخت ریشهٔ موازی)
- Previous checkpoint: CURRENT-125
- Requested outcome: تکمیل قرارداد محیط کاری میزبان اول، جداسازی مجوز مخزن از اجرای وظیفه، اتصال سند مادر/ZIP/راهنمای میزبان به قرارداد واحد.
- Host: FIRST_HOST / HOST-001
- Authentication gate: OPEN / DEFERRED
- Repository: READ-ONLY
- Workspace: OWNER-DEFINED / ALLOWLISTED EXECUTION ONLY
- Owner message timestamp: UNKNOWN / UNVERIFIED؛ زمان commit جایگزین زمان پیام نیست.

## ورودی و خواستهٔ مالک
مالک تأکید کرد نقطهٔ جاری باید ۰++ شود و میزبان اول پس از دریافت متن سند مادر بتواند مخزن را بخواند، محیط کاری تعریف‌شده را به‌روزرسانی کند و فقط در محدودهٔ دسترسی/قفل‌های مالک عمل کند. میزبان حق نوشتن در مخزن ندارد. عبارت‌های زیر بخشی از اصل معماری‌اند:
- HOST IDENTITY: FIRST NEW HOST
- AUTHENTICATION GATE: OPEN / DEFERRED

## تفسیر اجرایی
میزبان دو سطح مجزا دارد: (۱) خواندن مخزن canonical، (۲) اجرای وظایف مالک‌تعریف‌شده در workspace واقعی و محدود. هیچ‌یک به معنی دسترسی آزاد یا write-back نیست. سند مادر نمی‌تواند به‌تنهایی sandbox/ACL بسازد؛ باید قابلیت‌های واقعی پلتفرم آزموده شوند.

## قرارداد مرجع
[قرارداد میزبان اول](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md)

## معیار خروج
قرارداد ایجاد و در اسناد اصلی پیوند داده شود؛ فایل‌ها بازخوانی شوند؛ زمان از commit واقعی ثبت شود. ادغام main، بازسازی ZIP، اجرای آزمون مستقل و اثبات قفل فنی تا دریافت شواهد باز می‌مانند.
