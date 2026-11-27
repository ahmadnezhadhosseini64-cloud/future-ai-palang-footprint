# قرارداد حاکمیت دو نسخهٔ امن و پل واحد — Future AI / Palang Footprint

- شناسهٔ پایدار: `PALANG-TWO-COPY-GOVERNANCE-CONTRACT-2026-11-26-001`
- وضعیت: ACTIVE / LIVING — نسخهٔ پیشنهادی فقط در محیط کاری مجاز نگهداری می‌شود.
- نقطهٔ مرجع: `POINT-0/GOLDEN` — ریشهٔ واحد و موجود پروژه؛ این قرارداد ریشه یا صف تازه ایجاد نمی‌کند.
- مبنای منبع در این نوبت: `2c1f9fdc308e34b23be64153e8eec2c30f08a859`.

## ۱. مدل پایهٔ قطعی دو نسخه

### کپی ۱ — PROPOSAL / مرجع پیشنهادیِ بدون تغییر
- کپی ۱ یک snapshot دقیق و تغییرناپذیر از منبع اصلی در SHA مبنای ثبت‌شده است.
- کپی ۱ برای مقایسه، مرجع پیشنهاد و اثبات منشأ تغییرات است؛ محل اعمال patch یا اجرای آزمون نیست.
- هیچ میزبان AI، عامل، گردش‌کار یا دستیار حق تغییر فایل، commit، rebase، reset، حذف، جابه‌جایی ref یا اعمال patch در کپی ۱ را ندارد.
- کپی ۱ باید در تمام چرخه با SHA مبنای ثبت‌شده یکسان بماند.

### کپی ۲ — SAFE-TEST / تنها محیط تغییر و آزمون
- کپی ۲ باید از همان SHA دقیق منبع اصلی که کپی ۱ از آن ساخته شده، به‌صورت مستقل ایجاد شود.
- فقط کپی ۲ محل مجاز اعمال تغییر، اصلاح معماری، توسعه، آزمون عملکردی، آزمون رگرسیون، آزمون امنیتی، آزمون منفی و آزمون فشار است.
- هر تغییر در کپی ۲ باید محدود، قابل بازبینی، قابل بازگشت و متصل به شناسهٔ تغییر و SHA مشخص باشد.
- کپی ۲ نباید هیچ remote، credential، workflow token، مسیر push یا مجوزی داشته باشد که بتواند به منبع اصلی، MASTER، CHILD، RAHM یا GOLDEN بنویسد.
- اگر استقلال clone، خصوصی‌بودن محیط یا نبود مسیر نوشتن قابل اثبات نیست، وضعیت باید BLOCKED / NOT VERIFIED ثبت شود؛ شاخهٔ عمومی را نباید معادل محیط خصوصی و مستقل معرفی کرد.

### پل واحد — BRIDGE
- فقط یک پل منطقی/بستهٔ انتقال برای این چرخه وجود دارد؛ پل ریشه، صف یا مخزن معماری تازه نیست.
- پل یک‌طرفه است: کپی ۲ فقط بستهٔ پیشنهاد را به مالک می‌رساند. مالک تنها نقطهٔ انتقال/بازبینی/تصمیم است؛ هیچ کانال برگشتی خودکار یا اتصال نوشتنی کپی ۲ به کپی ۱، MAIN یا MASTER وجود ندارد.
- MAIN و MASTER از دو کپی امن فاصلهٔ ساختاریِ بلند و مرز مالکانه دارند؛ این فاصله با یک مسیر bridge کوتاه و کنترل‌شده توسط مالک جایگزین نمی‌شود و هرگز به میان‌بُر مستقیم تبدیل نمی‌شود. در مدل اجرایی، این مقصدها فقط anchorهای read-only/مقایسه‌ای هستند و هیچ write-target تعریف نمی‌شود.
- پل، patch/diff دقیق کپی ۲ نسبت به کپی ۱، SHA مبنا، SHA پیشنهاد/آزمون، فهرست فایل‌ها، هش‌ها، نتایج آزمون، read-back و وضعیت را حمل می‌کند.
- پل فقط شواهد و پیشنهاد را منتقل می‌کند؛ به‌تنهایی patch را روی کپی ۱ یا منبع اصلی اعمال نمی‌کند.
- هر دریافت‌کننده باید patch و هش‌ها را مستقل بازخوانی و تطبیق دهد؛ عدم تطبیق یعنی توقف fail-closed.
- Issue #161 دفتر تحویل A/B/C است، نه خودِ BRIDGE، نه POINT-0 و نه NEXT.

## ۲. مرز اختیار و ممنوعیت ارتقا

- منبع اصلی `main` و لایه‌های MASTER / CHILD / RAHM / GOLDEN بیرون از محدودهٔ نوشتن میزبان AI هستند.
- نه کپی ۱ و نه کپی ۲ حق نوشتن مستقیم یا غیرمستقیم به منبع اصلی ندارند.
- merge، cherry-pick، fast-forward، push، انتشار، تغییر قواعد حفاظتی، تغییر credential یا هر ارتقای خودکار ممنوع است.
- تأیید یک پیشنهاد به‌تنهایی مجوز اجرای ارتقا نیست. هر اقدام مالکانهٔ بعدی نیازمند دستور صریح، مستقل و مشخص مالک دربارهٔ مقصد و دامنه است.
- هیچ میزبان حق ایجاد PR به منبع اصلی به نام خود را ندارد؛ نتیجه از طریق پل واحد و دفتر تحویل به مالک ارائه می‌شود.

## ۳. چرخهٔ اجباری اجرایی

`RECOVER SOURCE SHA → CREATE COPY 1 SNAPSHOT → CREATE INDEPENDENT COPY 2 → CHANGE COPY 2 ONLY → TEST → STRESS/NEGATIVE TEST → READ-BACK → BUILD ONE BRIDGE → INDEPENDENT VERIFY → OWNER REVIEW`

شرایط عبور:
1. SHA منبع اصلی در لحظهٔ شروع مستقل خوانده شود.
2. کپی ۱ و کپی ۲ از همان SHA دقیق ساخته شوند.
3. عدم تغییر کپی ۱ و منبع اصلی اثبات شود.
4. همهٔ تغییرات فقط در کپی ۲ باشند.
5. آزمون‌ها روی SHA دقیق کپی ۲ اجرا شوند؛ نتیجهٔ SHA قدیمی به SHA جدید تعمیم داده نشود.
6. پل شامل diff، هش، نتایج و read-back باشد.
7. بازبین مستقل پل را از ابتدا تطبیق دهد.
8. تصمیم مالک جداگانه ثبت شود؛ بدون آن چرخه فقط PROPOSAL باقی می‌ماند.

## ۴. وظایف سه موتور

- **A — بازیابی و معماری:** بازیابی مستقل منبع، POINT-0/GOLDEN، CURRENT و تنها NEXT؛ کشف مسئله و تعیین کار بعدی.
- **B — پیاده‌سازی و اعتبارسنجی:** اجرای کار مجاز فقط در کپی ۲، ساخت آزمون‌ها، ثبت نتایج، read-back و آماده‌سازی پل واحد.
- **C — امنیت، تداوم و ممیزی مستقل:** بررسی مستقل مرزهای دسترسی، تطبیق کپی‌ها و پل، آزمون منفی و گزارش شکاف‌ها به A.
- چرخهٔ کاری: `C → A → B → C`. زمان‌بندی روزانهٔ موجود تغییر نمی‌کند؛ ثبت اجرا فقط پس از فعال‌سازی واقعی مجاز است.
- B حق ندارد اجرای زمان‌بندی‌شده یا موفقیت آزمون را بدون رسید واقعی ادعا کند.

## ۵. وضعیت واقعی پیاده‌سازی در این مخزن

- مخزن GitHub در وضعیت مشاهده‌شده عمومی است؛ شاخه‌ها در همان مخزن قرار دارند.
- branch `palang-safe-copy-1-baseline-20261126` snapshot مبنا را نگه می‌دارد و با SHA مبنا برابر است.
- branch `palang-safe-copy-2-test-20261126` شامل تغییرات پیشنهادی است؛ این وضعیت هنوز اثبات نمی‌کند که دو clone مستقل و خصوصی طبق مدل نهایی ساخته شده‌اند.
- بنابراین پیاده‌سازی فعلی، نمونهٔ نسخه‌ای/پیشنهادی است و تا زمان اثبات workspace خصوصی، clone مستقل، مجوزهای فقط‌خواندنی و نبود مسیر push، انطباق کامل با مدل نهایی محسوب نمی‌شود.
- GitHub Actions با `contents: read` به‌تنهایی مرز دسترسی خصوصی یا استقلال clone ایجاد نمی‌کند.
- هیچ ادعای حفاظت مؤثر، محرمانگی، استقلال محیط، اجرای آزمون یا تأیید مالک بدون شواهد read-back مجاز نیست.

## ۶. اصل پایدار

`POINT-0/GOLDEN = SINGLE CANONICAL ROOT`

`COPY 1 = PROPOSAL / IMMUTABLE SOURCE SNAPSHOT`

`COPY 2 = SAFE-TEST / ONLY MODIFICATION & TEST ENVIRONMENT`

`ONE BRIDGE = PATCH + HASHES + EVIDENCE + READ-BACK`

`OWNER = ONLY AUTHORITY FOR ANY LATER PROMOTION`

این قرارداد در شاخهٔ کاری کپی ۲ اصلاح شده است. این تغییر به معنی نوشتن در کپی ۱، main، MASTER، CHILD، RAHM یا GOLDEN نیست.


## ۷. همگامی دائمی دو پیام ورود میزبان

دو ورودی عملیاتی میزبان عبارت‌اند از:
- `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`
- `prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md`

بخش بین نشانگرهای `PALANG-HOST-ENTRY-CURRENT-AUTHORITY-BEGIN/END` باید در هر دو فایل عیناً یکسان باشد. این بخش مرجع جاری است؛ snapshotهای قدیمی پایین‌تر فقط تاریخچه‌اند و نباید بر آن تقدم پیدا کنند. هر تغییر در وضعیت GOLDEN، CURRENT/NEXT، مبنای دو نسخه، Copy 2، پل یا دروازه‌های پذیرش باید در هر دو پیام هم‌زمان بازتاب یابد. آزمون خودکار باید برابری دقیق این بخش را کنترل کند. تغییر هر دو پیام فقط در Copy 2 مجاز است و نتیجه تا اجرای CI روی exact HEAD جدید، تأییدنشده می‌ماند.


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
