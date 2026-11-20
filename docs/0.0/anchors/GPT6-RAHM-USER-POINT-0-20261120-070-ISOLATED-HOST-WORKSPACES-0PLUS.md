# POINT-0/070 — محیط‌های کاری مستقل و محصور میزبان‌ها (0+)

- Status: ACTIVE / LIVING / GOVERNANCE REGISTERED / IMPLEMENTATION PARTIAL
- Parent: POINT-0/069 → CURRENT-122
- Input/output: IN-113 → OUT-112
- Event/time: EVT-0288 → TIME-BINDING-EVT-0288
- Living master: سند مرجع مادر مدل اولیه هوش مصنوعی v1.7.75
- Multi-host architecture: v1.1.0
- Sole execution queue: NEXT-051
- Owner authority: احمد پلنگ
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## تصمیم مالک
هر میزبان جدیدی که برای همکاری با پروژه پذیرفته می‌شود باید یک شناسه پایدار و محیط کاری مستقل و محصور داشته باشد. میزبان از snapshot نسخه‌پین‌شدهٔ معماری ما استفاده می‌کند، اما فقط در محیط اختصاصی خودش کار می‌کند. میزبان‌ها به محیط یکدیگر، سند مادر، main، صف اجرایی، workflowها، registry و release دسترسی نوشتن ندارند.

## ساختار محیط
برای هر میزبان پس از احراز هویت و تأیید مالک:
- Host ID: HAIF-HOST-YYYYMMDD-PROVIDER-MODEL-NNN
- Workspace ID: HWS-<HOST-ID>
- Session ID: HSESS-<HOST-ID>-YYYYMMDD-NNNN
- پوشه اختصاصی با CHARTER، INBOX، OBSERVATIONS، PROPOSALS، TESTS، RECEIPTS و DECISIONS ساخته می‌شود.

## جریان
MASTER SNAPSHOT (READ-ONLY) → HOST WORKSPACE → HOST-SCOPED BROKER → QUARANTINE → OWNER MONITORING → CROSS-HOST RECONCILIATION → RAHM → CHILD CANDIDATE → EXPLICIT OWNER APPROVAL → MASTER + CANONICAL ZIP

## مرز حاکمیت و امنیت
- میزبان هیچ‌گاه مستقیماً MASTER یا main را تغییر نمی‌دهد.
- خروجی میزبان داده نامطمئن است و فقط در workspace خودش نگهداری می‌شود.
- ثبت در دفتر دائمی با پذیرش دانش در سند مادر متفاوت است.
- فقط نتیجه‌ای که منشأ، digest، قابلیت بازتولید و آزمون معتبر دارد و مالک صریحاً تأیید کرده، به سند مادر و همان ZIP canonical افزوده می‌شود.
- پوشه‌بندی داخل GitHub به‌تنهایی مرز امنیتی نیست؛ میزبان نباید credential نوشتن مستقیم مخزن بگیرد. broker، allowlist مسیر، credential حداقلی، branch protection و آزمون منفی جداسازی باید واقعی و اثبات شوند.
- اگر جداسازی واقعی در یک مخزن ممکن نباشد، workspace باید در repo/sandbox جدا باشد و فقط پاکت پالایش‌شده از واسط امن وارد مخزن اصلی شود.

## وضعیت واقعی
سه فایل معماری workspace و الگوی منشور در مخزن ثبت شده‌اند. هیچ میزبان خارجی در این نقطه ثبت، provision یا ACTIVE نشده است. broker استقرار‌یافته، محدودیت واقعی دسترسی، branch protection، آزمون cross-workspace denial، اتصال واقعی و receipt end-to-end همچنان OPEN هستند. این نقطه طراحی و ثبت معماری را ثابت می‌کند، نه اتصال زنده را.

## زنجیره
POINT-0/069 → CURRENT-122 → POINT-0/070 → IN-113 → OUT-112 → EVT-0288 → TIME-BINDING-EVT-0288 → CURRENT-123 → NEXT-051.
