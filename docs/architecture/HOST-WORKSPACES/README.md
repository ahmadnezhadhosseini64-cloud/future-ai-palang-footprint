# محیط‌های کاری مستقل میزبان‌ها — HAIF

- Architecture checkpoint: POINT-0/086 / CURRENT-139
- Governing owner: احمد پلنگ
- Status: WORKSPACE MODEL REGISTERED / NO EXTERNAL HOST ACTIVATED
- Registry: ../HOST-REGISTRY/HOST-REGISTRY.json
- Intake route: OWNER_EXPORT_TO_PRIVATE_RAHM_ONLY; no host intake branch in master
- Sole execution queue: NEXT-051

## هدف
برای هر میزبان AI که پس از شناسایی و تأیید مالک به مخزن متصل می‌شود، یک محیط کاری مستقل، شناسه‌دار، نسخه‌مند و قابل ممیزی تعریف می‌شود. میزبان در این محیط فقط از قراردادها و ابزارهای معماری HAIF استفاده می‌کند؛ داده و خروجی آن به محیط میزبان دیگر یا سند مادر نشت نمی‌کند.

## شناسه‌گذاری
شناسه میزبان پس از احراز هویت و تأیید مالک صادر می‌شود:
`HAIF-HOST-YYYYMMDD-<PROVIDER>-<MODEL>-NNN`
شناسه نشست برای هر نشست مستعار و جداگانه است:
`HSESS-<HOST-ID>-YYYYMMDD-NNNN`
شناسه محیط:
`HWS-<HOST-ID>`
نام مدل یا ادعای میزبان به‌تنهایی هویت معتبر نیست. هیچ میزبان فرضی یا آزمایش‌نشده‌ای در Registry فعال ثبت نمی‌شود.

## ساختار محیط هر میزبان
پس از پذیرش واقعی، برای هر host_id فقط پوشهٔ مختص خودش ساخته می‌شود:
- `HOSTS/<host_id>/CHARTER.md` — هویت، نسخه مرجع، مجوز و محدودیت‌ها
- `HOSTS/<host_id>/INBOX/` — ورودی‌های قرنطینه‌شده
- `HOSTS/<host_id>/OBSERVATIONS/` — مشاهده‌ها و نتایج بدون ارتقای خودکار
- `HOSTS/<host_id>/PROPOSALS/` — پیشنهادهای مستقل
- `HOSTS/<host_id>/TESTS/` — تست‌ها و بازتولیدها
- `HOSTS/<host_id>/RECEIPTS/` — رسیدهای دریافت و read-back
- `HOSTS/<host_id>/DECISIONS/` — تصمیم‌های مالک و وضعیت نهایی

هر میزبان فقط محیط خودش را می‌بیند/استفاده می‌کند، مگر آنچه در مجوزش صریحاً مجاز شده باشد. هیچ پوشهٔ میزبان محل نگهداری مرجع مادر نیست.

## جریان کاری
`MASTER SNAPSHOT (READ-ONLY) → HOST WORKSPACE → HOST-SCOPED INTAKE → QUARANTINE → OWNER MONITORING → CROSS-HOST RECONCILIATION → RAHM TEST → CHILD CANDIDATE → EXPLICIT OWNER DECISION → MASTER`

- میزبان ابتدا فقط snapshot مرجع را با commit، نسخه و digest می‌خواند.
- هر ورودی با host_id، session_id، parent checkpoint، timestamp قابل اثبات یا UNKNOWN، digest و privacy/redaction metadata ثبت می‌شود.
- مشاهده/پیشنهاد در فضای میزبان باقی می‌ماند تا از مسیر intake مجاز و با رسید read-back وارد قرنطینه شود.
- میزبان‌ها حق مشاهده یا دستکاری workspace یکدیگر را ندارند.
- خروجی‌های تأییدنشده، فایل‌های اجرایی، promptها و دستورهای میزبان هرگز به‌عنوان دستور حاکم اجرا نمی‌شوند.
- فقط خروجی‌های راستی‌آزمایی‌شده و مفید، پس از تأیید صریح مالک، به نسخه زنده و بسته canonical اضافه می‌شوند.

## مرز امنیتی مهم
پوشه‌بندی داخل یک مخزن Git به‌تنهایی کنترل دسترسی امنیتی نیست؛ GitHub مجوزهای معمول مخزن را در سطح repository اعمال می‌کند، نه مجوز واقعی per-folder. بنابراین:
1. میزبان AI هرگز credential نوشتن مستقیم مخزن اصلی یا main دریافت نمی‌کند.
2. دریافت فقط از طریق broker/adapter احراز هویت‌شده و allowlist مسیرهای host-scoped انجام می‌شود.
3. هیچ مقصد intake روی شاخه‌های مخزن مادر وجود ندارد. میزبان خروجی را فقط در workspace خودش نگه می‌دارد؛ مالک export پالایش‌شده را به RAHM خصوصی منتقل می‌کند. هر broker آینده فقط می‌تواند به مخزن خصوصی همان میزبان محدود شود و هرگز به master متصل نیست.
4. دسترسی به مخزن اصلی، secrets، workflowها، registry، master و workspace میزبان‌های دیگر برای میزبان ممنوع است.
5. اگر جداسازی واقعی credential/مسیر در GitHub قابل تضمین نباشد، میزبان باید در مخزن خصوصی/مجزای intake یا sandbox جدا اجرا شود و فقط پاکت پالایش‌شده از broker وارد مخزن اصلی شود.
6. branch protection واقعی و credential کم‌اختیار هنوز باید در GitHub تنظیم و با آزمون منفی اثبات شود؛ وجود این سند جایگزین آن نیست.

## چرخه عمر
`PROPOSED → IDENTITY_VERIFIED → WORKSPACE_PROVISIONED → L1_READ_ONLY → L2_PROPOSAL_ONLY / L3_TEST_CONTRIBUTOR → SUSPENDED / REVOKED`
ایجاد پوشه یا شناسه، معادل اتصال زنده نیست. تا زمان رسید واقعی، وضعیت میزبان `NOT_CONNECTED` باقی می‌ماند.

## سیاست حفظ داده
- متن کامل چت پیش‌فرض ذخیره نمی‌شود؛ فقط حداقل خروجی پالایش‌شده و مجاز.
- secrets، tokenها، داده شخصی غیرضروری و payloadهای حساس ممنوع‌اند.
- رویدادها append-only هستند؛ اصلاح/رد با رکورد جدید انجام می‌شود.
- هر تعامل موفق و مجاز در دفتر دائمی IN/OUT ثبت می‌شود؛ هر خروجی ناموفق یا فاقد رسید نیز به‌عنوان شکاف ثبت می‌شود.
- ثبت تعامل با ارتقای دانش به MASTER متفاوت است.

## وضعیت فعلی
در POINT-0/070 مدل محیط مستقل و الگوی ساختار/شناسه ثبت می‌شود؛ هیچ میزبان خارجی در این نقطه فعال یا provision نشده است. اتصال واقعی، broker استقرار‌یافته، محدودیت credential، branch protection و receipt end-to-end همچنان OPEN هستند.


## راه‌اندازی یک‌پیامی میزبان — POINT-0/071

برای میزبان GPT جدید فقط پیام کامل `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md` ارسال می‌شود. پیام، اتصال خواندنی به مخزن رسمی، بازیابی سند مادر و ZIP از latest-verified pointer، اجرای تست‌های بسته و ساخت workspace خصوصی در runtime مقصد را به ترتیب انجام می‌دهد. مجوز OAuth/GitHub یا قابلیت workspace را جعل نمی‌کند؛ در صورت نبود ابزار، BLOCKED/NOT CONNECTED/WORKSPACE_NOT_PERSISTENT ثبت می‌شود.

workspace واقعی باید در sandbox/فضای خصوصی میزبان ایجاد شود. پوشه داخل مخزن مشترک مرز امنیتی نیست. دسترسی میزبان به مخزن اصلی READ-ONLY است و هیچ میزبان حق نوشتن مستقیم main/MASTER را ندارد. Host Registry تا احراز هویت، اجرای آزمون‌ها و تصمیم مالک خالی می‌ماند.


## راه‌اندازی یک‌پیامی میزبان GPT-6 — CURRENT-124

از پیام واحد فارسی ONE_MESSAGE_HOST_BOOTSTRAP_FA.md استفاده می‌شود. میزبان با اتصال رسمی GitHub، آخرین Release و سند مادر را بازیابی و بررسی می‌کند و workspace را در محیط خصوصی/پایدار خودش می‌سازد. پوشه‌بندی در مخزن اصلی مرز امنیتی نیست. میزبان READ-ONLY آغاز می‌کند و تا تأیید مالک PROPOSED می‌ماند. اگر connector یا محیط پایدار در دسترس نیست، BLOCKED / NOT SUPPORTED اعلام می‌شود. ثبت مخزنی فقط از broker مجاز و پس از read-back است.


## ورود یک‌پیامی میزبان — POINT-0/083 / CURRENT-136

- دستور واحد ورود میزبان: [ONE_MESSAGE_MULTI_HOST_ENROLLMENT_FA.md](../../../prototype/universal-host/ONE_MESSAGE_MULTI_HOST_ENROLLMENT_FA.md).
- میزبان تازه فقط PUBLIC READ روی مخزن مرکزی دارد؛ هیچ WRITE یا تغییر branch/PR/issue/release/settings مجاز نیست.
- Host ID و Workspace ID رسمی فقط پس از رسید واقعی و تأیید مالک تخصیص می‌یابند.
- workspace باید در محیط خصوصی خود میزبان provision شود؛ پوشهٔ داخل مخزن مشترک مرز امنیتی نیست.
- پذیرش میزبان، persistence، export، recovery و جداسازی فنی تا رسید مستقیم OPEN می‌مانند.
