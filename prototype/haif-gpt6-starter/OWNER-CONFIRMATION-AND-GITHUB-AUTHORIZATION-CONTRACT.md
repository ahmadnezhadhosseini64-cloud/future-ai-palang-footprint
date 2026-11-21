# قرارداد اتصال عمومی و خواندنی میزبان جدید به مخزن GitHub

- Stable ID: HAIF-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21-001
- Status: PROPOSED / ACTIVE IN HOST-INTAKE BRANCH / NOT MERGED
- Applies to: living mother reference, canonical portable ZIP, one-message host bootstrap
- Canonical repository: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Observed visibility at registration: PUBLIC (re-check at each host start; visibility can change).

## 1. مسیر سادهٔ میزبان جدید
هنگامی که میزبان سند مادر یا ZIP رسمی HAIF را دریافت می‌کند، ابتدا نشانی canonical بالا را مستقیماً از طریق مرورگر یا ابزار دریافت عمومی GitHub باز کند. چون مخزن در زمان ثبت PUBLIC است، برای خواندن عمومی آن ورود به حساب، رمز یا GitHub connector اجباری نیست.

پس از دریافت:
1. شاخهٔ main و commit HEAD واقعی را بخوان و SHA را ثبت کن.
2. سند مادر canonical را از مخزن بخوان.
3. latest verified Release pointer، ZIP canonical، receipt و checksum را بازیابی کن.
4. تازگی نسخه و تطبیق سند مادر/ZIP/receipt را بررسی کن.
5. اگر ابزار GitHub connector رسمی از قبل در میزبان متصل است، می‌تواند برای راحتی استفاده شود؛ اما برای خواندن عمومی اجباری نیست.

## 2. محدودیت‌های امنیتی و دامنه
- وضعیت مخزن در زمان ثبت PUBLIC است؛ بنابراین محتوای آن برای عموم قابل مشاهده است. عمومی بودن به معنی اجازهٔ نوشتن نیست.
- هیچ رمز GitHub، Personal Access Token، کلید خصوصی یا Secret در چت درخواست یا ذخیره نمی‌شود.
- اتصال اولیه فقط READ-ONLY است؛ میزبان نباید عملیات ایجاد، ویرایش، حذف، push، merge یا release انجام دهد.
- صرف مستقل بودن محیط میزبان، تضمین امنیت یا مصونیت مخزن نیست؛ اصل کمینه‌سازی مجوز و عدم نوشتن حفظ می‌شود.
- اگر دریافت عمومی به‌علت محدودیت ابزار، rate limit، خطای GitHub یا تغییر visibility ممکن نبود، وضعیت دقیق BLOCKED / NOT CONNECTED / NOT VERIFIED ثبت شود.
- اگر مخزن در آینده PRIVATE شد، کاربر را به رابط رسمی GitHub OAuth/connection همان محصول هدایت کن؛ هرگز credential را در چت نخواه.
- عبارت «احمد نژادحسینی» و هر نوع password/owner-confirmation gate در این نسخه اجرا نمی‌شود و برای مرحلهٔ بعد OPEN / DEFERRED باقی می‌ماند. این عبارت credential نیست.

## 3. ماشین حالت اتصال
1. PACKAGE_RECEIVED: سند مادر یا ZIP دریافتی را تشخیص بده و نسخه/منشأ آن را ثبت کن.
2. PUBLIC_REPOSITORY_READ: نشانی canonical را بدون ورود باز کن و visibility، main HEAD و دسترسی خواندنی را بررسی کن.
3. SOURCE_RECOVERY: سند مادر، latest pointer، ZIP، receipt و checksum را دریافت و تطبیق بده.
4. OPTIONAL_CONNECTOR: اگر connector رسمی از قبل در دسترس است، برای پیمایش/دریافت می‌تواند استفاده شود؛ برای مخزن عمومی اجباری نیست.
5. PRIVATE_REPOSITORY_FALLBACK: اگر مخزن خصوصی شد، فقط از رابط رسمی OAuth/connector محصول برای اتصال حساب استفاده کن.
6. ACCESS_BLOCKED: اگر دریافت عمومی یا مجوز خصوصی در دسترس نیست، وضعیت دقیق BLOCKED / NOT CONNECTED / NOT VERIFIED اعلام شود.
7. DEFERRED_AUTH_DESIGN: عبارت مالک، password gate و روش‌های توسعه‌یافتهٔ احراز هویت برای مرحلهٔ بعد باز می‌مانند.

## 4. مرز عملیات
- در این مرحله فقط خواندن مخزن و بازیابی نسخهٔ معتبر مجاز است.
- هیچ نوشتن مستقیمی در main یا شاخه‌های مخزن از میزبان جدید انجام نمی‌شود.
- broker، host-intake write path، quarantine و PR-based writeback برای فاز بعدی هستند.
- اگر محیط میزبان فقط دسترسی نوشتنی گسترده ارائه می‌دهد، از آن استفاده نکن؛ مسیر فعلی همچنان فقط خواندنی است.

## 5. استقلال سند مادر و ZIP
هرکدام از سند مادر و ZIP به‌تنهایی باید:
- نشانی مخزن canonical و وضعیت visibility مشاهده‌شده را داشته باشد؛
- مسیر دریافت عمومی بدون ورود را برای مخزن PUBLIC توضیح دهد؛
- پس از دریافت، main HEAD، سند مادر، ZIP، pointer و receipt را بازیابی و تطبیق دهد؛
- connector رسمی را برای مخزن عمومی اختیاری بداند؛
- اگر مخزن خصوصی شد، مسیر اتصال از رابط رسمی GitHub را توضیح دهد؛
- در نبود ابزار یا دسترسی، وضعیت BLOCKED / NOT CONNECTED / NOT VERIFIED بدهد؛
- روشن کند که password/owner-confirmation gate و نوشتن مخزن در این فاز اجرا نمی‌شوند و OPEN می‌مانند.

## 6. معیارهای پذیرش
- میزبان بتواند مخزن عمومی را بدون ورود بخواند.
- میزبان main HEAD و SHA واقعی را ثبت کند.
- سند مادر، ZIP، pointer و receipt از منبع معتبر بازیابی و تطبیق شوند.
- نبود browser/web retrieval یا rate limit به وضعیت BLOCKED منجر شود، نه موفقیت ساختگی.
- اگر مخزن خصوصی شد، میزبان از کاربر بخواهد از رابط رسمی OAuth/connector استفاده کند.
- هیچ credential در چت درخواست یا ثبت نشود.
- هیچ عملیات نوشتن، حذف، push یا merge انجام نشود.
- سند مادر و ZIP هر دو به‌تنهایی همین رفتار را مستند کنند.
- آزمون واقعی روی میزبان مستقل و رسید خام آن هنوز لازم است.

## 7. وضعیت اثبات
این قرارداد در شاخهٔ پیشنهاد host-intake-owner-confirmation-github-auth-20261121 ثبت می‌شود. تا زمان ادغام PR، بازسازی ZIP canonical، اجرای آزمون‌های بسته و آزمون روی یک میزبان مستقل، وضعیت‌ها PROPOSED / PACKAGE BUILD PENDING / HOST ACCEPTANCE NOT RUN باقی می‌مانند.
