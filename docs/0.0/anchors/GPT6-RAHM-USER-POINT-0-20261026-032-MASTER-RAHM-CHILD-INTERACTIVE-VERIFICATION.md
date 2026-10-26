# POINT-0/032 — اتصال MASTER / RAHM / CHILD و راستی‌آزمایی محیط تعاملی

- Anchor ID: `GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION`
- Stable ID: `HAIF-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION-20261026-032`
- Production ID: `HAIF-P032`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Project: Future AI / Palang Footprint / HAIF
- Parent: [POINT-0/031](./GPT6-RAHM-USER-POINT-0-20261026-031-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md)
- Previous checkpoint: [CURRENT-078](./PALANG-0.0-CURRENT-20261026-078-REVERSIBLE-GRAPH-GAP-COVERS.md)
- Input: [IN-067](./PALANG-0.0-IN-20261026-067-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION.md)
- Output: [OUT-066](./PALANG-0.0-OUT-20261026-066-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION.md)
- Event: [EVT-0201](../../architecture/BEHAVIOR-TRACE/EVT-0201-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION-2026-10-26.md)
- Current checkpoint: [CURRENT-079](./PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md). Do not create NEXT-052.

## قصد کاربر و معماری
پروژهٔ اصلی نقش MASTER را دارد: قواعد، داده‌های رفتاری، الگوهای معماری، تاریخچه، منشأ و شواهد پذیرفته‌شده. مدل اولیه/پروژهٔ جدید نقش RAHM را دارد: دریافت کنترل‌شدهٔ بستهٔ مستر، بازسازی، آزمون، ثبت خطاها و پرورش نامزدها. نسخه‌ای که معیارهای پذیرش روشن را گذرانده و شواهدش قابل بازخوانی است به‌عنوان CHILD نسخه‌دار برای بازبینی مستر پیشنهاد می‌شود.

`MASTER → RAHM → OBSERVATION → TEST → EVIDENCE → CHILD CANDIDATE → MASTER REVIEW → ACCEPT / REVISE / REJECT`

- MASTER مرجع قواعد پذیرفته‌شده است؛ RAHM آزمایشگاه است و اجازهٔ بازنویسی خاموش مستر را ندارد.
- RAHM بسته‌ای با manifest، شناسهٔ commit، نسخه و digest مشخص وارد می‌کند.
- بازسازی باید فقط از بسته ممکن باشد: شناسه‌ها، زنجیرهٔ والد، رویدادها، شواهد، خطاها، شکاف‌های OPEN و اقدام بعدی.
- قبولی CI به‌تنهایی پذیرش معماری توسط MASTER نیست؛ بازبینی و تصمیم ثبت‌شده نیز لازم است.
- خطاها، ردها، اصلاح‌ها و نسخه‌های قبلی حفظ می‌شوند؛ هیچ فایل یا شناسه‌ای برای پاک‌کردن تعارض حذف یا حدسی بازشماری نمی‌شود.
- درپوش شکاف فقط COVERED / DEFERRED است؛ شکاف زیرین OPEN / ACTIVE / LIVING می‌ماند.
- مخزن و محیط تعاملی/میزبان مستقل دو مقصد جدا هستند. موفقیت CI واردسازی واقعی در پروژهٔ تعاملی را اثبات نمی‌کند.

## کارهای واقعی و مرز اثبات
مخزن رسمی `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint` روی شاخهٔ `main` بازخوانی شد. مدل اولیهٔ موجود در `docs/architecture/مدل اولیه AI/` و بستهٔ RAHM موجود هستند؛ پروژهٔ موازی جدید ساخته نمی‌شود. این نقطه قرارداد پذیرش و مسیر آزمون مستقل را تعریف می‌کند؛ تا دریافت رسید مستقیم از مقصد تعاملی، آزمون آن NOT RUN / NOT VERIFIED می‌ماند.

## معیار پذیرش محیط تعاملی
- [ ] استخراج بسته از SHA مشخص و ثبت manifest/digest.
- [ ] واردسازی در محیط پروژهٔ تعاملی/میزبان مجاز؛ ثبت نام واقعی میزبان، مدل، نسخه و قابلیت‌ها.
- [ ] بازسازی بدون تکیه بر حافظهٔ گفت‌وگوی قبلی.
- [ ] تطبیق شناسه‌ها، روابط، نسخه‌ها، رویدادها، evidence refs و تمام شکاف‌های باز.
- [ ] آزمون منفی: digest دست‌کاری‌شده و fixture نامعتبر رد شوند.
- [ ] بازیابی IN-only و OUT-only به وضعیت canonical یکسان و حفظ همهٔ شکاف‌های باز.
- [ ] بازخوانی مستقل از مقصد و مقایسه با منبع.
- [ ] ثبت نتیجهٔ خام و تصمیم مستر؛ فقط سپس CHILD candidate برای پذیرش بررسی شود.

## منابع موجود
- [مدل اولیه — README](../../architecture/مدل%20اولیه%20AI/README.md)
- [سند مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- [صف مدل اولیه](../../architecture/مدل%20اولیه%20AI/صف%20گام‌های%20بعدی%20و%20موارد%20باز.md)
- [سند مادر قابل‌حمل RAHM](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- [قرارداد راه‌اندازی RAHM](../../portable/RAHM/RAHM_BOOT.md)
- [دفتر پوشش‌های برگشت‌پذیر شکاف‌ها](../../architecture/BEHAVIOR-TRACE/GAP-COVER-REGISTER-2026-10-26.md)

## موارد باز
داوری موردبه‌مورد برخورد شناسه‌ها و EVT؛ روابط والد مبهم؛ منشأ ناقص و گراف تاریخی؛ ممیزی دقیق HEAD نهایی و digest؛ واردسازی در محیط تعاملی و میزبان دوم؛ بازیابی پس از restart؛ حافظهٔ پایدار و اجرای پس‌زمینه؛ Buffer / Persistent Memory / Library / Dropbox. بدون شاهد مستقیم هیچ‌کدام بسته نمی‌شوند.

## ادامه
از CURRENT-079 و صف موجود NEXT-051 ادامه بده. پس از نوشتن، همهٔ فایل‌ها و پیوندها را بازخوانی کن؛ سپس ممیزی و بستهٔ portable را روی SHA دقیق اجرا کن. اگر مسیر واقعی مجاز محیط تعاملی در دسترس شد، آزمون مستقل را انجام بده. NEXT-052 نساز.