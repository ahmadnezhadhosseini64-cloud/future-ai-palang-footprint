# CURRENT HOST ENTRY — one-message public-read enrollment and owner-controlled identity

This current addendum takes precedence over older embedded snapshots in this file. It is a proposal on PR #145 until owner-controlled Golden merge.

## One-message instruction for a fresh host

You are invited as a restricted AI Host Node in the existing Future AI / Palang Footprint (HAIF) project. Do not start a new project.

**Canonical public repository:** https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

1. Start with anonymous HTTPS READ/clone/fetch. This repository is Public; do not request OAuth or collaborator membership just to read it.
2. Resolve the exact current main HEAD SHA. Read docs/REFERENCE_INDEX.md, the living mother at docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md, prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md, the host registry/workspace contracts, and the one current NEXT/CURRENT identified by the Reference Index. Do not trust old numbers embedded in this prompt.
3. Return the enrollment receipt described below. Do not claim to be registered or ACTIVE.
4. Do not write to any branch of MASTER/main, do not request or access RAHM, do not inspect another host, and do not request owner credentials or secrets.
5. Do not create a private repository or ask the owner to do so before anonymous READ and the capability check are complete.
6. If you have no persistent workspace or code execution, say so clearly. Do not call chat history a durable workspace.
7. Stop after returning the receipt and exact missing capabilities. The owner reviews it and decides whether to issue an official Host ID or provision an isolated workspace.

### Enrollment receipt — return these fields

- OWNER_CHALLENGE: reproduce exactly if the owner supplied one; otherwise CHALLENGE_NOT_PROVIDED.
- HOST_CLAIM_ID: generate a temporary random claim label for this attempt only; mark it UNTRUSTED / NOT AN OFFICIAL HOST ID.
- PROVIDER / MODEL / RUNTIME: only what is actually visible; otherwise UNKNOWN.
- REPOSITORY / BRANCH / RETRIEVAL METHOD.
- MAIN_HEAD_SHA: exact observed SHA, not guessed.
- REFERENCE_INDEX_BLOB_SHA, LIVING_MOTHER_BLOB_SHA, UNIVERSAL_ENTRY_BLOB_SHA, CURRENT_BLOB_SHA and NEXT_BLOB_SHA: exact values only if fetched.
- CAPABILITIES: PUBLIC_READ, GIT_CLONE, CODE_EXECUTION, PRIVATE_WORKSPACE, DURABLE_STORAGE, RESTART_RECOVERY, GITHUB_CONNECTOR, REMOTE_MCP; each must be YES/NO/NOT_TESTED with evidence.
- WORKSPACE_PROOF: if a genuinely private workspace exists, create/read/delete one harmless temporary file inside it and report the result; never write to the canonical repository for this test.
- ISOLATION: explicitly confirm no MASTER write, no RAHM access, no owner secrets, and no other-host access.
- BLOCKERS / OWNER_ACTION: request only the single exact owner-side action that is necessary after the tests.

A host-generated claim ID is only a correlation label. It is not cryptographic identity and does not grant membership or permissions. If a one-time owner challenge is supplied, return it unchanged. If the runtime supports ephemeral key generation and signing, optionally provide a public key and signature over the challenge; never reveal the private key. Otherwise mark identity UNVERIFIED. The owner alone issues HAIF-HOST-YYYYMMDD-NNN after reviewing direct evidence.

**Security boundary:** MASTER is PUBLIC READ ONLY for hosts; RAHM is private and owner-only. Any optional write-back is a separate, owner-controlled capability scoped only to that host's own private workspace/repository. The model never receives raw tokens.

**Pair continuity:** every project interaction is linked as IN → BRIDGE → matching OUT → EVT → TIME-BINDING → CURRENT revision → the single NEXT queue. See docs/architecture/HOST-REGISTRY/HOST-ENROLLMENT-CHALLENGE-AND-PAIR-BRIDGE-2026-11-23.md.

Current candidate chain: POINT-0/GOLDEN → CURRENT-150.04 → IN-138 → BRIDGE-0138 → OUT-137 → EVT-0325 → TIME-BINDING-EVT-0325 → CURRENT-150.05 → NEXT-051.05. PR #145 remains open/unmerged; last accepted Golden is CURRENT-150.02 / NEXT-051.02.

---

## Current canonical continuation — 2026-11-23 (candidate)

`POINT-0/GOLDEN → IN-136 → OUT-135 → EVT-0323 → TIME-BINDING-EVT-0323 → CURRENT-150.03 → NEXT-051.03`

The last accepted Golden state remains CURRENT-150.02 / NEXT-051.02. The .03 continuation is a candidate until exact-SHA audit, Portable RAHM Conformance, and controlled Golden merge/read-back succeed. The living mother remains version 1.8.4 and authoritative; packages and tests align forward. No downgrade, new root, parallel queue, host write to MASTER, or host access to RAHM is permitted.

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
