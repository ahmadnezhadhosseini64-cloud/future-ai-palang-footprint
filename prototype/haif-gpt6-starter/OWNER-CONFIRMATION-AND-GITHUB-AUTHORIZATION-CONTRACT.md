# قرارداد اتصال خواندنی میزبان جدید به مخزن GitHub

- Stable ID: HAIF-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21-001
- Status: PROPOSED / ACTIVE IN HOST-INTAKE BRANCH / NOT MERGED
- Applies to: living mother reference, canonical portable ZIP, one-message host bootstrap
- Canonical repository: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## 1. تجربهٔ میزبان جدید
هنگامی که میزبان سند مادر یا ZIP رسمی HAIF را دریافت می‌کند و کاربر ادامهٔ پروژه یا اتصال به مخزن را می‌خواهد، باید ابتدا تشخیص دهد آیا اتصال رسمی GitHub در محیط میزبان در دسترس و فعال است یا خیر.

اگر اتصال فعال نیست، میزبان باید کاربر را به رابط رسمی همان محصول برای اتصال/اجازه‌دهی حساب GitHub هدایت کند. پس از بازگشت از فرایند رسمی، میزبان دسترسی خواندنی به مخزن دقیق زیر را آزمایش می‌کند:
ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## 2. محدودیت‌های امنیتی و دامنه
- هیچ رمز GitHub، Personal Access Token، کلید خصوصی یا Secret در چت درخواست یا ذخیره نمی‌شود.
- اطلاعات ورود فقط در رابط رسمی GitHub/محصول میزبان وارد می‌شود.
- اتصال اولیه فقط READ-ONLY است؛ میزبان نباید عملیات ایجاد، ویرایش، حذف، push، merge یا release را انجام دهد.
- صرف مستقل بودن محیط میزبان، تضمین امنیت یا مصونیت مخزن نیست؛ اصل کمینه‌سازی مجوز و عدم نوشتن حفظ می‌شود.
- اگر حساب متصل‌شده یا مجوز خواندن مخزن دقیق قابل اثبات نیست، وضعیت OWNER_ACCOUNT_NOT_VERIFIED یا REPOSITORY_ACCESS_NOT_VERIFIED ثبت می‌شود.
- عبارت «احمد نژادحسینی» و هر نوع password/owner-confirmation gate در این نسخه اجرا نمی‌شود و برای مرحلهٔ بعد OPEN / DEFERRED باقی می‌ماند. این عبارت credential نیست.

## 3. ماشین حالت اتصال
1. PACKAGE_RECEIVED: سند مادر یا ZIP دریافتی را تشخیص بده و نسخه/منشأ آن را ثبت کن.
2. GITHUB_CONNECTOR_CHECK: وجود و قابلیت استفاده از connector رسمی GitHub در میزبان را بررسی کن.
3. USER_GUIDED_AUTHORIZATION: اگر حساب متصل نیست، کاربر را به رابط رسمی محصول هدایت کن؛ هیچ credential را در چت نپرس.
4. REPOSITORY_ACCESS_CHECK: دسترسی خواندنی به مخزن canonical را آزمایش کن.
5. READ_ONLY_RECOVERY: HEAD شاخهٔ main، آخرین pointer/receipt، سند مادر و ZIP را بخوان و freshness/integrity را بررسی کن.
6. ACCESS_BLOCKED: اگر connector، مجوز یا دسترسی موجود نیست، وضعیت دقیق BLOCKED / NOT CONNECTED / NOT VERIFIED اعلام شود.
7. DEFERRED_AUTH_DESIGN: عبارت مالک، password gate و روش‌های توسعه‌یافتهٔ احراز هویت برای مرحلهٔ بعد باز می‌مانند.

## 4. مرز عملیات
- در این مرحله فقط خواندن مخزن و بازیابی نسخهٔ معتبر مجاز است.
- هیچ نوشتن مستقیمی در main یا شاخه‌های مخزن از میزبان جدید انجام نمی‌شود.
- broker، host-intake write path، quarantine و PR-based writeback برای فاز بعدی هستند.
- مجوزهای connector باید تا حد امکان فقط خواندنی و محدود به مخزن موردنیاز باشند.
- اگر محیط میزبان فقط دسترسی نوشتنی گسترده ارائه می‌دهد و امکان محدودسازی/کنترل آن روشن نیست، از عملیات نوشتن استفاده نکن؛ مسیر فعلی همچنان فقط خواندنی است.

## 5. استقلال سند مادر و ZIP
هرکدام از سند مادر و ZIP به‌تنهایی باید:
- نشانی مخزن canonical را داشته باشد؛
- روش بررسی اتصال رسمی GitHub و هدایت کاربر به رابط اتصال میزبان را توضیح دهد؛
- پس از مجوز واقعی، دسترسی خواندنی به مخزن دقیق را بررسی کند؛
- آخرین HEAD، سند مادر، ZIP، pointer و receipt را بازیابی و تطبیق دهد؛
- در نبود connector یا مجوز، وضعیت BLOCKED / NOT CONNECTED / NOT VERIFIED بدهد؛
- روشن کند که password/owner-confirmation gate و نوشتن مخزن در این فاز اجرا نمی‌شوند و OPEN می‌مانند.

## 6. معیارهای پذیرش
- میزبان وجود connector رسمی را درست تشخیص دهد.
- میزبانِ بدون اتصال، راهنمای اتصال از رابط رسمی محصول را ارائه کند.
- پس از اتصال، دسترسی خواندنی به مخزن دقیق اثبات شود.
- میزبانِ بدون مجوز یا با حساب نامنطبق، بازیابی را متوقف و علت را اعلام کند.
- هیچ credential در چت درخواست یا ثبت نشود.
- هیچ عملیات نوشتن، حذف، push یا merge انجام نشود.
- سند مادر و ZIP هر دو به‌تنهایی همین رفتار را مستند کنند.
- آزمون واقعی روی میزبان مستقل و رسید خام آن هنوز لازم است.

## 7. وضعیت اثبات
این قرارداد در شاخهٔ پیشنهاد host-intake-owner-confirmation-github-auth-20261121 ثبت می‌شود. تا زمان ادغام PR، بازسازی ZIP canonical، اجرای آزمون‌های بسته و آزمون روی یک میزبان مستقل، وضعیت‌ها PROPOSED / PACKAGE BUILD PENDING / HOST ACCEPTANCE NOT RUN باقی می‌مانند.
