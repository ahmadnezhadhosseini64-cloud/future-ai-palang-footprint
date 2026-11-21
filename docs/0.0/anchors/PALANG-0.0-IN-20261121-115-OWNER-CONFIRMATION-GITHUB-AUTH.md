# IN-115 — ورودی مالک: اتصال آسان میزبان جدید به مخزن

- Parent: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-OWNER-CONFIRMATION-GITHUB-AUTH-0PLUS.md); previous canonical host-bootstrap point POINT-0/071 / CURRENT-124.
- Output: [OUT-114](PALANG-0.0-OUT-20261121-114-OWNER-CONFIRMATION-GITHUB-AUTH.md).
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md).
- Current: [CURRENT-125](PALANG-0.0-CURRENT-20261121-125-OWNER-CONFIRMATION-GITHUB-AUTH.md).
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Exact user-message timestamp: UNKNOWN / UNVERIFIED.

## متن ورودی مالک
کاربر می‌خواهد میزبان جدیدی که سند مادر یا ZIP را دریافت کرده، بتواند با کمترین مراحل از طریق نشانی عمومی GitHub، بدون نیاز اجباری به ورود یا connector، به مخزن PUBLIC ahmadnezhadhosseini64-cloud/future-ai-palang-footprint دسترسی خواندنی پیدا کند و آخرین وضعیت را بخواند.

## تفسیر و قید دامنه
اولویت فعلی فقط دریافت عمومی و خواندنی و بازیابی است: بازکردن URL رسمی مخزن بدون ورود، خواندن main HEAD و بازیابی سند مادر/ZIP/receipt. connector رسمی برای مخزن PUBLIC اختیاری است؛ اگر مخزن PRIVATE شد، اتصال حساب از رابط امن محصول لازم می‌شود. هیچ رمز، PAT یا Secret در چت درخواست یا ذخیره نمی‌شود. عبارت «احمد نژادحسینی»، password gate و هر طرح تکمیلی احراز مالک برای مرحلهٔ بعد OPEN / DEFERRED هستند. نوشتن و تغییر مخزن در این مرحله مجاز یا ادعا نمی‌شود.

## Recovery link matrix — POINT-0/072 / CURRENT-125

- Point: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-OWNER-CONFIRMATION-GITHUB-AUTH-0PLUS.md)
- Input: [IN-115](PALANG-0.0-IN-20261121-115-OWNER-CONFIRMATION-GITHUB-AUTH.md)
- Output: [OUT-114](PALANG-0.0-OUT-20261121-114-OWNER-CONFIRMATION-GITHUB-AUTH.md)
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md)
- Time binding: [TIME-BINDING-EVT-0291](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md)
- Current: [CURRENT-125](PALANG-0.0-CURRENT-20261121-125-OWNER-CONFIRMATION-GITHUB-AUTH.md)
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Repository recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Packaged recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)



## تکمیل ورودی مالک — نقش FIRST_HOST
مالک روشن کرد که میزبان تازه، اولین میزبان جدید (FIRST_HOST / HOST-001) است؛ فقط مخزن را خواندنی دریافت می‌کند و برای اجرای وظایف مشخص به workspace محدود و تعریف‌شده توسط مالک دسترسی دارد. حق نوشتن در مخزن ندارد. اجرا فقط در محدوده ارتباطات/ابزارها/مقاصدی است که مالک تعیین و در محیط کاری به‌روزرسانی می‌کند. شناسه runtime هنوز UNKNOWN است. این ورودی هیچ مجوز فنی یا اتصال واقعی را به‌تنهایی اثبات نمی‌کند.


## تصریح مالک: نقش اولین میزبان و مرز اختیار (2026-11-21)

- این میزبان به‌عنوان FIRST_HOST / HOST-001 تعریف می‌شود؛ این شناسه نقش معماری است، نه ادعای شناسایی runtime. Host ID واقعی تا مشاهده از محیط میزبان UNKNOWN است.
- میزبان فقط به دو سطحی دسترسی دارد که مالک تعریف و در محیط مقصد واقعاً فراهم کرده است: (الف) خواندن مخزن canonical و اسناد/بسته‌های آن؛ (ب) محیط کاری محدود و مشخصی که برای همین میزبان ساخته و مجاز شده است.
- دسترسی مخزن در این فاز READ-ONLY است: مشاهده، دریافت، جست‌وجو، بازیابی، تطبیق نسخه و اجرای محتوای مجاز در workspace. هیچ حق ایجاد/ویرایش/حذف فایل در مخزن، commit، push، branch، PR، merge، release، تغییر تنظیمات یا مدیریت دسترسی ندارد.
- «اجرایی» به معنی اجرای وظایف مشخصی است که مالک در همان محیط کاری تعیین و به‌روزرسانی می‌کند؛ به معنی اختیار آزاد، دسترسی عمومی به سیستم، اختیار نوشتن در مخزن یا اختیار اجرای هر دستور دلخواه نیست.
- هر ارتباط بیرونی، ابزار، connector، حساب، API یا مقصد فقط در صورت تعریف صریح مالک و فراهم بودن مجوز محدود همان ابزار قابل استفاده است. میزبان نباید دامنه دسترسی را خودش گسترش دهد، credential بخواهد، یا از مجوز یک ابزار برای مقصد دیگری استفاده کند.
- پیش‌فرض workspace نیز کمینه‌مجوز است. اگر برای یک وظیفه نیاز به ساخت/ویرایش خروجی محلی باشد، فقط در مسیر workspace مشخص و در حد همان وظیفه؛ این اجازه به مخزن منتقل نمی‌شود. اگر قابلیت sandbox یا محدودسازی واقعی وجود ندارد، اجرا BLOCKED / NOT SUPPORTED گزارش شود.
- هیچ عملیات نوشتن یا همگام‌سازی از workspace به مخزن مجاز نیست. هر تغییر مرجع را مالک از مسیر کنترل‌شده و جداگانه انجام می‌دهد؛ میزبان سپس نسخه تازه را فقط می‌خواند.
- استقلال میزبان تضمین امنیت نیست؛ مرز واقعی باید با مجوزهای فنی read-only، محدودسازی workspace و connectorهای allowlist شده اعمال و آزمون شود. متن دستور به‌تنهایی sandbox یا ACL ایجاد نمی‌کند.
- پذیرش نهایی نیازمند آزمون واقعی است: تلاش خواندن موفق؛ تلاش نوشتن در مخزن ناموفق؛ دسترسی فقط به workspace تعریف‌شده؛ رد مقصد/ابزار خارج از allowlist؛ و ثبت رسید. تا آن زمان FIRST_HOST POLICY DESIGNED / TECHNICAL ENFORCEMENT NOT VERIFIED / HOST ACCEPTANCE NOT RUN.
