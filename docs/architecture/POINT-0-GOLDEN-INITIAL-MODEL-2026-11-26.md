# نقطهٔ ۰ طلایی — مدل پایهٔ اولیهٔ معماری دو نسخه و پل واحد

- شناسهٔ رویداد/مدل: `POINT-0-GOLDEN-INITIAL-MODEL-2026-11-26-001`
- ریشهٔ مرجع: `POINT-0/GOLDEN` (همان ریشهٔ موجود؛ بدون ساخت ریشهٔ موازی)
- وضعیت این ثبت: `PROPOSED / ACTIVE-LIVING IN COPY 2`
- تاریخ ثبت: 2026-11-26
- مبنای منبعی که در این نوبت از GitHub بازخوانی شد: `2c1f9fdc308e34b23be64153e8eec2c30f08a859`
- محل این سند: شاخهٔ کاری کپی ۲؛ این سند خودش هنوز در GOLDEN/main پذیرفته یا ادغام نشده است.

## ۰.۱ — تعریف نقطهٔ طلایی

POINT-0/GOLDEN تنها ریشهٔ مرجع و لنگر معماری پروژهٔ Future AI / Palang Footprint است. این مدل پایه، تفسیر اجراییِ مورد تأیید مالک برای جداسازی مرجع، محیط آزمون و پل انتقال است؛ نه یک ریشه، CURRENT یا NEXT جدید.

هر فعالیت باید به همین ریشه و زنجیرهٔ معتبر موجود متصل بماند. شناسه‌های تاریخی حذف یا بازنویسی نمی‌شوند. وضعیت‌های Pending، Blocked، Recovery و Open حفظ می‌شوند تا زمانی که شواهد مستقل برای تغییر وضعیت وجود داشته باشد.

## ۰.۲ — سه جزء ثابت مدل

### A) کپی ۱ — PROPOSAL

کپی ۱ یک snapshot تغییرناپذیر از منبع اصلی در یک SHA دقیق است. نقش آن مرجع مقایسه و سمت مبنای پیشنهاد است؛ نه محیط توسعه و نه محل اجرای آزمون.

شرط پذیرش:
- SHA کپی ۱ دقیقاً برابر SHA مبنای منبع اصلی در شروع چرخه باشد.
- هیچ فایل یا ref در کپی ۱ توسط AI تغییر نکند.
- در پایان چرخه، تطبیق SHA و درخت فایل‌ها با مبنای اولیه انجام شود.

### B) کپی ۲ — SAFE-TEST

کپی ۲ یک clone مستقل از همان SHA مبنا است و تنها محل مجاز برای هرگونه تغییر و آزمون محسوب می‌شود.

فعالیت‌های مجاز:
- اصلاح کد و معماری پیشنهادی؛
- ساخت و اجرای آزمون واحد، یکپارچه، رگرسیون و سازگاری؛
- آزمون منفی، امنیتی و فشار؛
- بازخوانی خروجی‌ها و ثبت هش‌ها؛
- آماده‌سازی patch قابل بازبینی.

شرط پذیرش:
- استقلال clone و منشأ SHA اثبات شود.
- هیچ remote، secret، token یا مجوز نوشتن به منبع اصلی/MASTER/CHILD/RAHM/GOLDEN وجود نداشته باشد.
- هر نتیجهٔ آزمون به SHA دقیق کپی ۲ متصل باشد.
- شکست آزمون، خطا یا کمبود شواهد پنهان یا به موفقیت تبدیل نشود.

### C) پل واحد — BRIDGE

پل واحد تنها بستهٔ انتقال شواهد میان کپی ۲ و سمت مرجع کپی ۱ است. پل یک مخزن، صف یا ریشهٔ معماری جدید نیست.

حداقل محتوای پل:
1. شناسهٔ ثابت مدل و شناسهٔ کار؛
2. SHA مبنای منبع و SHA کپی ۱؛
3. SHA کپی ۲ پیش و پس از تغییر؛
4. patch/diff دقیق و فهرست مسیرها؛
5. SHA-256 یا هش معتبر هر artifact؛
6. فرمان‌ها، محیط و نتایج آزمون؛
7. گزارش آزمون منفی/فشار و محدودیت‌ها؛
8. نتیجهٔ read-back و تطبیق مستقل؛
9. خطرها، روش بازگشت و وضعیت تصمیم مالک.

پل فقط پیشنهاد و شواهد را منتقل می‌کند. هیچ‌گاه به‌صورت خودکار patch را روی کپی ۱ یا منبع اصلی اعمال نمی‌کند.

## ۰.۳ — مرز اختیار

- منبع اصلی `main` و لایه‌های MASTER، CHILD، RAHM و GOLDEN خارج از محدودهٔ نوشتن میزبان AI هستند.
- هیچ‌یک از کپی‌ها مجوز ارتقا یا انتشار به منبع اصلی ندارند.
- merge، cherry-pick، fast-forward، push، انتشار یا تغییر حفاظت‌ها توسط میزبان ممنوع است.
- تأیید محتوای پیشنهاد با اجازهٔ اجرای آن یکی نیست.
- هر اقدام بعدی روی منبع اصلی فقط با دستور صریح و مستقل مالک، برای مقصد و دامنهٔ مشخص، قابل بررسی است.
- میزبان AI حق ایجاد PR به منبع اصلی به نام خود را ندارد؛ نتیجه از طریق پل واحد و دفتر تحویل به مالک ارائه می‌شود.

## ۰.۴ — چرخهٔ اجرایی و اتصال A/B/C

`C → A → B → C`

- **A — بازیابی/معماری:** خواندن مستقل GitHub؛ بازیابی POINT-0/GOLDEN، CURRENT و تنها NEXT؛ تشخیص اختلاف و تعیین ورودی روشن برای B.
- **B — ساخت/آزمون:** اجرای تغییر فقط در کپی ۲؛ اجرای آزمون‌ها؛ ساخت patch و پل؛ read-back و تحویل شواهد.
- **C — امنیت/ممیزی مستقل:** بررسی SHAها، عدم تغییر کپی ۱ و منبع اصلی، استقلال کپی ۲، صحت پل، آزمون منفی و شکاف‌های امنیتی؛ سپس تحویل یافته‌ها به A.

Issue #161 تنها دفتر مشترک رسیدهای اجرایی و handoff سه موتور است. Issue #161 جای POINT-0، CURRENT، NEXT یا BRIDGE را نمی‌گیرد. هر موتور فقط برای فعال‌سازی واقعی خود یک رسید می‌نویسد؛ رسید زمان‌بندی‌شده یا اجرا نشده جعل نمی‌شود.

## ۰.۵ — چرخهٔ اثبات اجباری

`WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS`

برای هر ادعای «انجام شد» باید مدرک قابل بازیابی وجود داشته باشد:
- نوشتن فقط در مسیر مجاز کپی ۲؛
- بازخوانی مستقل همان فایل/commit؛
- تطبیق محتوای دقیق و SHA؛
- بررسی دامنهٔ diff و مرز دسترسی؛
- ثبت اختلاف‌ها و موارد حل‌نشده؛
- اعلام وضعیت واقعی: PASS / FAIL / BLOCKED / NOT RUN / NOT VERIFIED.

مستند شدن یک قابلیت به معنی پیاده‌سازی آن نیست؛ اجرای محلی به معنی اجرای GitHub Actions نیست؛ موفقیت آزمون روی SHA قبلی به SHA جدید تعمیم داده نمی‌شود؛ وجود دو branch در مخزن عمومی به معنی دو clone خصوصی و مستقل نیست.

## ۰.۶ — وضعیت اجرای واقعی در زمان ثبت

- مخزن GitHub در read-back این نوبت عمومی بود.
- کپی ۱ به‌صورت branch snapshot با SHA مبنای `2c1f9fdc308e34b23be64153e8eec2c30f08a859` مقایسه شده است.
- کپی ۲ به‌صورت branch کاری در همان مخزن قرار دارد و ۱۰ commit جلوتر از snapshot مبنا گزارش شده است.
- این ساختار branch-based به‌تنهایی اثبات‌کنندهٔ دو clone مستقل، workspace خصوصی، حذف مسیرهای push یا انزوای دسترسی نیست.
- بنابراین مدل معماری در این سند تعریف شده، اما تحقق کامل محیط مستقل خصوصی و اجرای کامل پل واحد هنوز `NOT VERIFIED / OPEN` است.
- آزمون CI روی آخرین SHA پس از اصلاحات قرارداد و این سند، تا دریافت نتیجهٔ تازه، `PENDING` محسوب می‌شود.
- هیچ تغییری در main، کپی ۱، MASTER، CHILD، RAHM یا GOLDEN انجام نشده است.

## ۰.۷ — شرط عبور از مدل اولیه

مدل تنها زمانی از `PROPOSED` به `VERIFIED` تغییر وضعیت می‌دهد که:
1. مالک workspace خصوصی/مستقل را فراهم یا تأیید کند؛
2. کپی ۱ و کپی ۲ از یک SHA واقعی و یکسان ساخته و read-back شوند؛
3. دسترسی کپی ۲ فقط به محدودهٔ لازم محدود و مسیر نوشتن به منبع اصلی مسدود شود؛
4. آزمون‌های کامل روی SHA دقیق کپی ۲ اجرا شوند؛
5. پل واحد با patch، هش‌ها و شواهد ساخته و مستقل بازبینی شود؛
6. موتور C نتیجه را مستقل ممیزی کند؛
7. مالک تصمیم نهایی را ثبت کند.

## ۰.۸ — فرمول پایه

`POINT-0/GOLDEN → COPY 1 (PROPOSAL) + COPY 2 (SAFE-TEST) → ONE BRIDGE → INDEPENDENT AUDIT → OWNER DECISION`

این سند یک پیشنهاد پایه در کپی ۲ است و تا زمان پذیرش مالک، مرجع اجرایی پذیرفته‌شدهٔ GOLDEN محسوب نمی‌شود.


## OWNER ARCHITECTURE CLARIFICATION — ROLLING SAFE REFERENCE / OWNER-GATED PROMOTION (2026-11-27)

This amendment supersedes earlier wording that made Copy 1 permanently frozen or required workflows to pin a historical SHA forever. Architecture advances continuously under owner control; it is not a static snapshot that becomes stale.

### Authority and progression
- Copy 2 (SAFE-TEST): AI hosts may implement, test, and submit proposals only in an authorized isolated Copy 2 workspace. Proposals target Copy 1, never MAIN.
- Copy 1 (SAFE REFERENCE): evolving secure reference. A PR can be merged here only after the owner personally reviews and approves that specific PR. CI is evidence, not permission. Hosts/automations may not merge, push, commit directly, or change protections/permissions.
- MAIN + MASTER: protected canonical roots. AI/automation cannot write, merge, promote, alter protection, or move refs. Only owner may deliberately promote after explicit review/approval. MAIN is not automatically synchronized from Copy 1.
- Flow: POINT-0/GOLDEN → owner-approved evolving Copy 1 → isolated Copy 2 from current Copy 1 → one evidence bridge/PR to Copy 1 → owner review/merge → Copy 1 advances → owner-only deliberate promotion to MAIN/MASTER.

### Rolling baseline / no stale-pin failures
- Discover live branch heads and active approved checkpoint each run. Old SHAs remain historical evidence, never permanent workflow expectations.
- Each proposal records source/base SHA, test SHA, and destination. CI verifies actual target is Copy 1 and tests the current Copy 1 + proposal merge candidate. If the base advances, report STALE BASE / REVALIDATION REQUIRED as lifecycle state, not a security failure.
- Do not hardcode historical MAIN/Copy 1 SHAs as eternal pins. Baseline changes are expected under owner-controlled progression. Reconcile lineage and re-test current code.
- Test results apply only to exact test SHA; if base advances, revalidate before merge.

### Status semantics
STALE BASE / REVALIDATION REQUIRED is distinct from HARNESS FAILURE, TEST FAILURE, SECURITY FAILURE and CANONICAL FAILURE. Report exact changed refs and SHA pair. Never label normal progression a security failure or hide genuine security failure by updating baselines.

### Owner-control enforcement gate
Owner-gating must be enforced by repository protections and permissions, not prose alone. Branch protection read-back/admin access is unavailable here. MAIN currently reports protected=true via branch metadata; Copy 1 protected=false, a concrete OPEN control gap. Owner must enable required protections/review on Copy 1. No AI may claim owner-gated Copy 1 merges are enforced until read-back confirms it.

### No new root or bridge
This is a living amendment within existing POINT-0/GOLDEN and PR #172; it creates no new root, queue, copy, or bridge.
