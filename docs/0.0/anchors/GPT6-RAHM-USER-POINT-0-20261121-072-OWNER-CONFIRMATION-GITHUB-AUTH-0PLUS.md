# POINT-0/072 — اتصال آسان و خواندنی میزبان جدید به GitHub (0++)

- Parent: canonical POINT-0/071; 0+ و 0++ فقط نشانگر روی همان ریشهٔ canonical هستند، نه ریشهٔ جدید.
- Input: IN-115
- Output: OUT-114
- Event: EVT-0291
- Time binding: TIME-BINDING-EVT-0291
- Current: CURRENT-125
- Sole active queue: NEXT-051
- Status: PROPOSED / HOST-INTAKE BRANCH / NOT MERGED / READ-ONLY TARGET / HOST ACCEPTANCE NOT RUN
- Deferred: owner phrase/password gate and any write authorization remain OPEN for a later design phase.

## هدف فعلی
هر میزبان جدیدی که سند مادر یا ZIP را دریافت می‌کند، چون مخزن فعلاً PUBLIC است، بتواند بدون ورود به حساب از طریق نشانی رسمی GitHub به مخزن دسترسی خواندنی پیدا کند؛ connector رسمی اختیاری است:
https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## مسیر اتصال
1. میزبان ابتدا دریافت عمومی مخزن را بدون ورود امتحان کند.
2. اگر دریافت عمومی به‌علت محدودیت ابزار یا تغییر visibility ممکن نبود، علت را اعلام کند؛ اگر مخزن خصوصی شد، کاربر را به رابط رسمی GitHub OAuth هدایت کند.
3. پس از دسترسی خواندنی، شاخهٔ main و SHA واقعی را ثبت کند.
4. HEAD SHA، سند مادر، آخرین Release pointer، ZIP و receipt را بازیابی و تطبیق دهد.
5. اگر connector، مجوز یا مخزن در دسترس نیست، وضعیت دقیق BLOCKED / NOT CONNECTED / NOT VERIFIED ثبت شود؛ موفقیت جعل نشود.

## مرز فعلی
- این مرحله فقط کشف connector، راهنمای اتصال رسمی و خواندن/بازیابی مخزن است.
- نوشتن به مخزن، اجرای تغییرات، دسترسی main و broker خارج از دامنهٔ فعلی‌اند.
- عبارت «احمد نژادحسینی» و طراحی هر نوع password/owner-confirmation gate برای مرحلهٔ بعد OPEN / DEFERRED می‌ماند؛ این عبارت در این مرحله نه درخواست می‌شود و نه credential محسوب می‌شود.
- PUBLIC بودن مخزن یعنی محتوا برای عموم قابل مشاهده است؛ امنیت محیط مقصد با «مستقل بودن» فرض نمی‌شود و هیچ دسترسی نوشتنی داده نمی‌شود.
- سند مادر و ZIP هر دو باید همین مسیر read-only را مستقل توضیح دهند.

## تحویل
این پیشنهاد در همان شاخهٔ host-intake ثبت می‌شود. سند مادر هدف v1.7.79 و منبع بسته هدف 0.4.4 باقی می‌مانند. ZIP canonical هنوز بازسازی/تأیید نشده و میزبان مستقل هنوز آزموده نشده است.

## لنگر زمانی
زمان commit نهایی این شاخه باید پس از آخرین تغییر از GitHub استخراج شود؛ زمان مشاهده یا زمان پیام کاربر جایگزین آن نیست.

## Cross-index and extraction registration

- Canonical 0.0 latest-chain index: [docs/0.0/README.md](../README.md).
- Reference index: [docs/REFERENCE_INDEX.md](../../REFERENCE_INDEX.md).
- Behavior-trace index: [BEHAVIOR-TRACE index](../../architecture/BEHAVIOR-TRACE/README.md).
- Architecture integration queue index: [INTEGRATION-QUEUE index](../../architecture/INTEGRATION-QUEUE/README.md).
- RAHM export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json).
- Package manifest source version: 0.4.4; canonical ZIP rebuild and exact receipt remain PENDING.
- This is a proposal-branch registration; main merge and independent-host read-only acceptance remain OPEN / NOT RUN.
