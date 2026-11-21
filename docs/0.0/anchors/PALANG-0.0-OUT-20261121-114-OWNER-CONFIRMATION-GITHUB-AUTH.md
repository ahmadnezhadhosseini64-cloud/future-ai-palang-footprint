# OUT-114 — خروجی: مسیر آسان اتصال خواندنی میزبان جدید به GitHub

- Point: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-OWNER-CONFIRMATION-GITHUB-AUTH-0PLUS.md).
- Input: [IN-115](PALANG-0.0-IN-20261121-115-OWNER-CONFIRMATION-GITHUB-AUTH.md).
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md).
- Time binding: [TIME-BINDING-EVT-0291](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0291-OWNER-CONFIRMATION-GITHUB-AUTH-2026-11-21.md).
- Current: [CURRENT-125](PALANG-0.0-CURRENT-20261121-125-OWNER-CONFIRMATION-GITHUB-AUTH.md).
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).

## خروجی طراحی‌شده در شاخهٔ پیشنهاد
1. پیام واحد میزبان به مسیر کوتاه دریافت عمومی مخزن بدون ورود را اجرا می‌کند؛ GitHub connector برای این مخزن PUBLIC اختیاری است.
2. اگر دریافت عمومی به‌علت محدودیت ابزار یا خصوصی‌شدن مخزن ممکن نیست، میزبان فقط راهنمای اتصال از رابط رسمی محصول را نشان می‌دهد؛ هیچ credential در چت جمع‌آوری نمی‌کند.
3. پس از اتصال، میزبان دسترسی READ-ONLY به مخزن دقیق و بازیابی HEAD، سند مادر، آخرین ZIP و رسیدها را بررسی می‌کند.
4. قرارداد میزبان، دستورالعمل‌ها، README، manifest و سند مادر دامنهٔ فعلی را به read-only connection محدود می‌کنند.
5. عبارت «احمد نژادحسینی» و طراحی password/owner-confirmation gate به مرحلهٔ بعد موکول و OPEN نگه داشته می‌شوند.

## وضعیت واقعی
- Proposal branch: host-intake-owner-confirmation-github-auth-20261121.
- Main merge: NOT DONE.
- Canonical ZIP rebuild and exact receipt: PENDING.
- Independent-host connector/read-only test: NOT RUN.
- Repository write access, broker, host-intake write path and branch protection: OUT OF SCOPE FOR THIS PHASE / OPEN.
- NEXT-051 remains the sole active execution queue; no parallel queue created.

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
