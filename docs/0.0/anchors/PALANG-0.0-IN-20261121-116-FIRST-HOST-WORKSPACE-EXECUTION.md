# IN-116 — تکمیل معماری اجرایی میزبان اول و تثبیت نقطهٔ ۰++

- Parent point: POINT-0/072; continuation anchor: POINT-0/073 (0++; no independent root)
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

## مسیر دریافت سند مادر متنی
میزبان متن مادر ارسالی را می‌خواند، نشانی canonical و شناسهٔ سند را استخراج می‌کند، main HEAD و SHA واقعی را از GitHub عمومی می‌خواند، سپس متن ارسالی را با نسخهٔ canonical مخزن و manifest تطبیق می‌دهد. هر اختلاف نسخه/محتوا باید صریح گزارش شود؛ هیچ‌یک بی‌صدا جایگزین یا ادغام نمی‌شود. snapshot محلی فقط پس از تعیین revision معتبر به commit و digest مشخص pin می‌شود.

## معیار خروج
قرارداد، سند مادر، دستورالعمل میزبان، manifest و cross-indexها باید به همین زنجیره متصل و read-back شوند. ادغام main، بازسازی ZIP، اجرای آزمون مستقل و اثبات قفل فنی تا دریافت شواهد باز می‌مانند.
