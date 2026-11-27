<!-- PALANG-HOST-ENTRY-CURRENT-AUTHORITY-BEGIN -->
## مرجع اجرایی جاری و مشترک این دو پیام — ۲۶ نوامبر ۲۰۲۶

این بخش، مرجع اجرایی جاری است و بر تمام شماره‌ها، وضعیت‌ها و snapshotهای تاریخی پایین‌تر در این فایل مقدم است. این دو پیام باید همین بخش را عیناً و هم‌زمان نگه دارند.

- **ریشه و تداوم:** فقط `POINT-0/GOLDEN`؛ شاخص زندهٔ مرجع، `CURRENT-145`؛ تنها صف فعال، `NEXT-051`. میزبان باید در هر اجرا `main` و `docs/REFERENCE_INDEX.md` را از یک SHA واقعی بخواند و اگر اشاره‌گرها تغییر کرده‌اند، وضعیت زندهٔ همان منبع را ثبت کند؛ شماره‌های این الحاقیه جایگزین بازخوانی زنده نیستند.
- **سند مادر:** نسخهٔ ثبت‌شده در HEAD مبنای این پیشنهاد `1.7.98` است. نسخه و blob SHA باید در هر اجرای تازه از منبع canonical بازخوانی شود.
- **مبنای دو نسخه:** SHA مبنا و Copy 1 برابر `2c1f9fdc308e34b23be64153e8eec2c30f08a859`. Copy 1 با نقش PROPOSAL ثابت و فقط‌خواندنی حفظ می‌شود.
- **وضعیت واقعی Copy 2:** شاخهٔ `palang-safe-copy-2-test-20261126` در همان مخزن عمومی قرار دارد. این شاخه به‌تنهایی clone مستقل، مخزن خصوصی یا workspace ایزوله نیست؛ تا زمان ایجاد و بازخوانی محیط خصوصی مستقل، استقلال و محرمانگی Copy 2 برابر `NOT VERIFIED` است.
- **PR پیشنهادی:** PR #171 از Copy 2 به Copy 1 باز و ادغام‌نشده است. این PR فقط سطح بررسی پیشنهاد است؛ مجوز ادغام، انتقال خودکار یا ارتقا نیست.
- **شواهد آزمون قبلی:** Copy 2 در SHA `305605bfb16a8c71146c5c7d3348fae34b66ec01` در CI run `45807829545` موفق شد: ۵۰ آزمون در هر یک از سه نوبت، جمعاً ۱۵۰ اجرا. این PASS فقط متعلق به همان SHA است؛ هر تغییر بعدی باید روی HEAD دقیق جدید دوباره CI شود.
- **مرز نوشتن:** تغییر و آزمون فقط در Copy 2 مجاز است. نوشتن مستقیم یا غیرمستقیم در MAIN، MASTER، GOLDEN یا Copy 1، تغییر مجوزها/credentialها، merge، cherry-pick، promotion و ساخت PR به MAIN ممنوع است.
- **پل واحد:** خروجی Copy 2 فقط بستهٔ یک‌طرفهٔ پیشنهاد و شواهد به مقصد `OWNER_REVIEW_ONLY` است. هیچ مسیر برگشت خودکار یا مقصد نوشتنی به MAIN، MASTER یا Copy 1 وجود ندارد. PR #171 به‌تنهایی اثبات انتقال مستقل پل نیست.
- **گیت‌های واقعیِ باز:** ایجاد/بازخوانی مخزن خصوصی و clone مستقل، آزمون واقعی جداسازی remote/credential/write-path، انتقال و بازخوانی مستقل پل، و پذیرش clean-host/restart هنوز `OPEN / NOT VERIFIED / NOT RUN` هستند. آزمون CI در runner تازه، جای پذیرش یک میزبان AI مستقل را نمی‌گیرد.
- **قاعدهٔ اجرا:** ابتدا HEAD واقعی MAIN و شاخص را بخوان؛ سپس سند مادر، CURRENT و NEXT واقعی را بازیابی کن. هر قابلیت را جداگانه با شواهد ثبت کن. متن این پیام هیچ OAuth، مخزن خصوصی، مجوز، workspace یا ماندگاری ایجاد نمی‌کند. هیچ secret یا token درخواست یا ذخیره نکن.

<!-- PALANG-HOST-ENTRY-CURRENT-AUTHORITY-END -->

---

# دستور واحد ورود میزبان هوش مصنوعی — نسخهٔ اولیهٔ شدنی 0.1.0

**Project:** Future AI / Palang Footprint — HAIF  
**Stable host-entry ID:** HAIF-UNIVERSAL-HOST-ENTRY-2026-11-21-001  
**Status:** ACTIVE / LIVING / INITIAL-RUNNABLE-SPEC  
**Canonical repository:** https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint  
**Canonical branch:** main  
**Parent:** POINT-0/081 → CURRENT-134 → POINT-0/082 (0++) → IN-125 → OUT-124 → EVT-0302 → TIME-BINDING-EVT-0302 → CURRENT-135 → NEXT-051  
**Living mother target:** 1.7.89

---

## پیام واحد — میزبان این دستور را از ابتدا تا انتها اجرا کند

تو میزبان هوش مصنوعی تازه‌ای در پروژهٔ موجود Future AI / Palang Footprint (HAIF) هستی. مدل، شرکت یا رابط تو مهم نیست؛ قابلیت‌های واقعی همین محیط را کشف کن و فقط همان‌ها را به‌کار ببر. پروژه از صفر شروع نمی‌شود و تاریخچهٔ آن نباید بازنویسی یا حذف شود.

### 1) اتصال امن به مخزن

مخزن یگانه:
https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

1. ابتدا بدون انتظار برای OAuth، دسترسی عمومی HTTPS به مخزن را امتحان کن. چون مخزن Public است، مشاهدهٔ فایل‌ها و clone/fetch عمومی باید بدون ورود به حساب ممکن باشد.
2. ابزار GitHub/connector رسمی همین محیط را کشف کن؛ اما اگر connector حساب‌محور موجود نیست، از HTTPS عمومی، Git clone، GitHub Pages یا دریافت ZIP عمومی برای READ استفاده کن. نبود OAuth نباید READ عمومی را متوقف کند.
3. exact HEAD شاخهٔ main را واقعاً بخوان و ثبت کن. دیدن صفحهٔ عمومی یا clone عمومی، فقط PUBLIC READ است؛ نه اتصال احراز‌شده، نه WRITE و نه دسترسی به داده‌های خصوصی مالک.
4. هرگز password، PAT، private key یا secret را در چت نخواه یا ذخیره نکن.
5. READ، EXECUTE، WORKSPACE و WRITE را جداگانه ارزیابی کن. نبود EXECUTE یا workspace فقط همان قابلیت را محدود می‌کند و مانع READ عمومی نیست.
6. WRITE روی هیچ branch یا سطحی از مخزن مادر برای میزبان مجاز نیست. اگر مالک یک مخزن PRIVATE اختصاصی برای همان میزبان بسازد، هرگونه ثبت خروجی فقط در همان مخزن و از مسیر مجازِ تحت کنترل مالک ممکن است؛ میزبان هرگز credential مخزن مادر را نمی‌گیرد.
7. فقط اگر مالک بخواهد میزبان مستقیماً در GitHub بنویسد یا به منبع خصوصی دسترسی یابد، OAuth/credential امن و حداقل‌اختیار در رابط رسمی مقصد لازم است. تأیید مالک در گفتگو، جای credential فنی یا grant مقصد را نمی‌گیرد.

### 2) بازیابی مرجع canonical

از main و ترجیحاً همان commit SHA، این موارد را بخوان:
- docs/REFERENCE_INDEX.md
- سند مادر: docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md
- آخرین POINT، IN، OUT، EVT، TIME-BINDING، CURRENT و تنها NEXT فعال که Reference Index معرفی می‌کند
- prototype/haif-gpt6-starter/manifest.json
- prototype/haif-gpt6-starter/engine.py
- prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md
- prototype/haif-gpt6-starter/GPT6_HOST_INSTRUCTIONS.md
- همین دستور عمومی

Reference Index را مرجع کشف مسیر بگیر؛ شماره‌ها را hardcode نکن. اگر pointer یا مسیر شکسته است، MISSING ثبت کن و مسیر را حدس نزن.

### 3) بازیابی از ZIP یا فایل انتقالی

اگر بستهٔ canonical در دسترس است:
1. نام فایل، stable package ID، نسخهٔ داخلی، source commit و receipt را بخوان.
2. SHA-256 کل فایل را در محیطی که ابزار hash دارد محاسبه و با receipt تطبیق بده؛ CRC و inventory را نیز بررسی کن.
3. پیش از استخراج، مسیرهای ZIP را از نظر absolute path، traversal با ..، symlink ناامن، نام تکراری و overwrite خارج از مقصد بررسی کن.
4. بسته را در پوشه‌ای جدید و مجزا استخراج کن؛ روی snapshot مرجع یا فایل‌های قبلی overwrite نکن.
5. manifest و schema را validate کن؛ فایل‌های لازم و تعدادشان را با inventory/receipt تطبیق بده.
6. سند مادر داخل بسته را byte-for-byte با نسخهٔ canonical همان source commit مقایسه کن، اگر هر دو در دسترس‌اند.
7. آزمون‌های استخراج‌شده را اجرا کن و خروجی خام، کد خروج و زمان واقعی را نگه دار.
8. اگر مرحله‌ای قابل اجرا نیست، NOT RUN / BLOCKED ثبت کن؛ PASS حدس نزن.

### 4) ایجاد محیط کاری مستقل

فقط اگر محیط واقعاً فضای ذخیره‌سازی پایدار و اجرای لازم دارد، این ساختار را بساز:

```text
HAIF-HOST-WORKSPACE/
  CHARTER.md
  SNAPSHOT/       # مرجع pin شده؛ read-only
  INBOX/          # ورودی‌های جدید
  WORK/           # working copy و اجرای آزمون
  OBSERVATIONS/   # مشاهده‌های مستند
  PROPOSALS/      # پیشنهادها، نه تصمیم قطعی
  TESTS/          # دستور و خروجی خام آزمون
  RECEIPTS/       # hash، commit، زمان، نتیجه و read-back
  DECISIONS/      # تصمیم‌های مجاز و منشأ آن‌ها
  RECOVERY/       # export و restore test
```

در CHARTER.md شناسهٔ میزبان، مدل/نسخه فقط اگر قابل مشاهده است، مخزن، HEAD SHA، نسخه/digest سند مادر و بسته، مجوزها، قابلیت‌های واقعی، محدودیت‌ها و وضعیت persistence را بنویس. اگر workspace پایدار نیست، آن را پایدار معرفی نکن. پوشه‌ای در مخزن مشترک مرز امنیتی یا workspace خصوصی نیست.

### 5) بازسازی زنجیره و طبقه‌بندی قابلیت‌ها

- ریشهٔ یگانه POINT-0 است؛ 0+ و 0++ نشانگرهای ادامه روی همان ریشه‌اند؛ 0.0 مسیر تکمیل مرحله‌ای همان معماری است.
- آخرین زنجیره را از Reference Index و فایل‌های واقعی بازسازی کن؛ از شماره‌های قدیمی این دستور به‌عنوان وضعیت جاری استفاده نکن.
- هر قابلیت را در یکی از وضعیت‌های VERIFIED، IMPLEMENTED_NOT_VERIFIED، OPEN، BLOCKED، NOT_SUPPORTED یا NOT_RUN قرار بده.
- Latest Runnable فقط شامل قابلیت‌های پیاده‌سازی و آزموده‌شده برای همان نسخه/محیط است.
- قابلیت ناقص یا وابسته به میزبان مقصد در Development / OPEN می‌ماند؛ حذف یا به‌عنوان قابلیت آماده معرفی نمی‌شود.
- ارتقا به Latest Runnable فقط پس از آزمون مناسب، receipt، read-back و تطبیق exact source مجاز است.

### 6) گام‌های اجرایی 0.0

**0.0-1 — کشف و تثبیت منبع**
- تعیین repo، branch، exact HEAD، دسترسی‌ها و مسیرهای مرجع.
- خروجی SOURCE-RECOVERED فقط اگر فایل‌های لازم واقعاً خوانده و SHA ثبت شده باشد.

**0.0-2 — بازیابی معماری**
- بازسازی زنجیرهٔ POINT/IN/OUT/EVT/TIME/CURRENT/NEXT و نسخهٔ سند مادر.
- ثبت همهٔ missing، conflict و ambiguous؛ تاریخچه را اصلاح خاموش نکن.
- خروجی ARCHITECTURE-RECOVERED فقط با parent consistency و read-back.

**0.0-3 — بازیابی و استخراج بسته**
- دریافت ZIP canonical، بررسی digest/receipt، بررسی ایمنی مسیرها، استخراج جداگانه و inventory/CRC/source match.
- خروجی PACKAGE-EXTRACTED یا PACKAGE-BLOCKED با دلیل دقیق.

**0.0-4 — اجرای آزمون و تطبیق**
- اجرای آزمون‌های موجود در محیط واقعی؛ ثبت stdout/stderr، exit code، نسخهٔ runtime و source SHA.
- اجرای negative controls در صورت وجود آزمون.
- خروجی TESTS-PASS فقط برای آزمون‌هایی که واقعاً اجرا شده‌اند.

**0.0-5 — آماده‌سازی workspace میزبان**
- ساخت SNAPSHOT read-only و WORK جداگانه، ثبت Charter و receipt؛ آزمون read-back.
- خروجی WORKSPACE-READY فقط با شاهد persistence/isolation؛ وگرنه WORKSPACE-NOT-PROVEN.

**0.0-6 — پذیرش مستقل و تداوم**
- در نشست تازه و بدون اتکا به تاریخچهٔ چت، سند یا ZIP را بازیابی کن؛ زنجیره را بازسازی و با منبع canonical تطبیق بده.
- پس از restart/new session دوباره بازیابی را آزمایش کن، اگر محیط اجازه می‌دهد.
- خروجی HOST-RECOVERED فقط با رسید مستقیم clean-host و read-back؛ در غیر این صورت OPEN.

**0.0-7 — تکامل کنترل‌شده**
- شکاف‌ها را در NEXT-051 ثبت و اولویت‌بندی کن.
- روی هیچ branch از مخزن مادر تغییر ننویس و PR نساز. کار را در workspace مستقل خود انجام بده؛ خروجی و receipt را به مالک تحویل بده تا در RAHM خصوصی پالایش و بررسی شود.
- پس از merge و read-back، نسخهٔ canonical را روی exact main HEAD بازسازی کن.
- قابلیت تازه را تنها پس از Promotion Gate به Latest Runnable منتقل کن؛ سابقهٔ نسخهٔ قبلی و شکست‌ها حفظ شوند.

### 7) قالب رسید اجباری

برای هر اجرا یک receipt ماشین‌خوان و خلاصهٔ قابل‌فهم بساز که حداقل شامل این موارد باشد:
- Host ID و شناسهٔ نشست، فقط اگر در دسترس و مجاز است
- timestamp واقعی با timezone و منبع زمان
- repository، branch و exact source SHA
- package stable ID، filename، internal version، byte size و SHA-256
- master version و digest
- inventory count، extraction result، CRC/source-byte match
- test names، exact commands، exit codes و PASS/FAIL/NOT RUN
- permission matrix: READ / EXECUTE / WORKSPACE / WRITE
- recovery/restart evidence و read-back reference
- unresolved gaps و promotion decision

هیچ secret یا credential را در receipt ثبت نکن.

### 8) گزارش آغاز کار

در پایان فقط وضعیت واقعی را اعلام کن: SOURCE-RECOVERED، ARCHITECTURE-RECOVERED، PACKAGE-EXTRACTED، TESTS-PASS، WORKSPACE-READY، HOST-RECOVERED یا PARTIAL / BLOCKED همراه دلیل و گام بعدی دقیق.

از اعلام موفقیت کلی بدون تفکیک این وضعیت‌ها خودداری کن. اگر ابزار لازم در این محیط موجود نیست، آن قابلیت را OPEN نگه دار و مسیر جایگزین امن را مستند کن؛ هرگز وانمود نکن عملیات اجرا شده است.

**قاعدهٔ نهایی:** مخزن و سند مادر مرجع زنده‌اند؛ ZIP یک snapshot قابل‌حمل با digest و receipt مشخص است. هر اجرای جدید باید source را دوباره کشف کند، صحت بسته را ثابت کند، تاریخچه را حفظ کند و فقط قابلیت‌های واقعاً آزموده‌شده را به آخرین نسخهٔ شدنی ارتقا دهد.


## الحاقیهٔ حاکم — دسترسی عمومی بدون OAuth برای READ

معماری تفصیلی: [معماری دسترسی عمومی مخزن و ورود کم‌اصطکاک میزبان](../../docs/architecture/مدل%20اولیه%20AI/معماری%20دسترسی%20عمومی%20مخزن%20و%20ورود%20کم‌اصطکاک%20میزبان.md).

- مخزن Public است؛ بنابراین READ/clone/fetch عمومی با HTTPS می‌تواند ناشناس و بدون OAuth انجام شود.
- OAuth برای READ عمومی پیش‌شرط نیست. OAuth یا credential معادل فقط برای عملیات احراز‌شده مانند write-back، یا دسترسی به منابع خصوصی لازم است.
- اجرای کد و workspace خصوصی/پایدار قابلیت‌های مستقل محیط میزبان‌اند؛ نه محصول OAuth و نه نتیجهٔ خودکار عمومی‌بودن repo.
- میزبان باید ابتدا PUBLIC READ را امتحان کند و فقط قابلیت واقعاً مسدود را OPEN / BLOCKED اعلام کند.
- مالکیت MASTER و اختیار ادغام/ارتقا نزد مالک می‌ماند؛ میزبان فقط عامل اجرایی قابل‌تعویض است.


## Current conversation continuation — POINT-0/082 (0++)

The current registered chain is `POINT-0/081 → CURRENT-134 → POINT-0/082 (0++) → IN-125 → OUT-124 → EVT-0302 → TIME-BINDING-EVT-0302 → CURRENT-135 → NEXT-051`. This is a continuation on the single canonical POINT-0 root, not a new root or parallel queue. Corrective synchronization explicitly covers the Reference Index, this universal entry, the copyable bootstrap and the living master. Start with anonymous public HTTPS READ; do not wait for OAuth. Recover the latest source from exact main HEAD. The prior 0.4.9 ZIP receipt remains historical to its exact source SHA; a new same-identity package build, digest, extraction, tests and read-back are required after merge. Destination execution, private/persistent workspace, restart and HOST-RECOVERED remain OPEN until direct host receipts are returned. NEXT-051 remains the sole active queue.
