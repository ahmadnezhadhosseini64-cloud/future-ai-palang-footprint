# فرمان حاکم و پیش‌فرض «ثبت کن» — Governing Register Command Binding

## شناسنامه
- **Stable ID:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001` (سند مرجع مادر؛ مرجع اصلی و حاکم)
- **Production ID:** `REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001`
- **Version:** 1.2.0
- **Date:** 2026-10-12
- **Exact Time:** Not recorded by the execution system; intentionally not invented.
- **Timezone:** Asia/Tehran (project timezone; exact execution timestamp not independently captured)
- **Owner:** Ahmad Nezhadhosseini / احمد پلنگ
- **Project:** Future AI / Palang Footprint — آینده AI / ردپای پلنگ
- **Artifact Type:** Command Binding / Architectural Entry Point
- **Status:** REPOSITORY ACTIVE/LIVING GOVERNING ENTRY — repository write + read-back + content match verified; Library copy pending; Buffer and Persistent Memory not independently verified.
- **Canonical Parent:** `docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md`

## 0.1 Finality and living status
این فرمان به‌عنوان **مبنای پیش‌فرض و دائمیِ حاکم برای اجرای «ثبت کن» در پروژه** تعیین شده است. «دائمی/نهایی» در اینجا یعنی قرارداد مرجع جاری است و تغییر آن فقط با نسخه‌گذاری و حفظ تاریخچه مجاز است؛ نه اینکه بتوان بدون شواهد، ماندگاری یا دسترسی همیشگی در هر سامانه‌ای را تضمین کرد. هر بار که این سند بازیابی شود، باید پیش از اجرای ثبت به‌عنوان مرجع حاکم اعمال شود. اگر بازیابی آن در یک محیط ممکن نبود، محدودیت باید صریح گفته شود؛ نباید وانمود کرد سند خوانده شده است.

## 1. Binding decision
از این پس هرگاه کاربر بگوید **«ثبت کن»**، همین سند مرجع مادر با شناسه `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001` مبنای پیش‌فرض و حاکم اجرای فرمان است. کاربر لازم نیست هر بار قواعد را دوباره توضیح دهد یا این سند را مجدداً بفرستد، مشروط به اینکه مرجع از محل پایدار واقعاً قابل بازیابی باشد.

این سند کوتاه فقط نقطه ورود و اتصال معماری است؛ جایگزین سند مرجع مادر یا مجوز حذف جزئیات آن نیست.

## 2. Minimum required execution
برای هر فرمان «ثبت کن»، تا جایی که ابزارها و دسترسی‌های واقعی اجازه می‌دهند:
1. محتوای ارزشمند را حفظ و طبقه‌بندی کن؛ منشأ، زمینه، مسئله/پرسش، یافته‌ها، آزمون‌ها، شواهد، تصمیم‌ها، دلیل تصمیم و اثر معماری را ثبت کن.
2. شناسه پایدار و شناسه تولید را ایجاد یا با حفظ lineage قبلی ادامه بده؛ برای تلاش مجدد، بی‌دلیل شناسه جدید نساز.
3. اگر محتوا معماری‌محور یا قابل استفاده مجدد است، سند مرجع کامل را بساز یا به‌روزرسانی کن و تاریخچه/نسخه‌های قبلی را حفظ کن.
4. مقصدهای واقعی را جداگانه هدف بگیر: مخزن (Repository)، بافر (Buffer)، حافظه پایدار (Persistent Memory) و هر مخزن اسنادی متصل و در دسترس.
5. برای هر مقصد مستقل، چرخه `WRITE → READ-BACK → MATCH → VERIFY` را اجرا کن؛ موفقیت یک مقصد را به مقصد دیگر تعمیم نده.
6. جایگاه سند در معماری، وابستگی‌ها، نسخه، تعارض/جایگزینی، مسیر بازیابی، وضعیت و گام بعدی را ثبت کن.
7. فقط وضعیت پشتیبانی‌شده با شواهد را گزارش بده. اگر مرحله‌ای قابل اجرا نیست، آن را `OPEN/PENDING` یا «پودینگ» نگه دار و مانع، آخرین وضعیت پایدار، قابلیت موردنیاز، گام بعدی و اشاره‌گر بازیابی را بنویس.

## 3. Hard constraints
- قصد اجرا یا پاسخ موفق ابزار به‌تنهایی اثبات بازیابی و تطبیق نیست.
- وجود/خواندن فایل در مخزن، ثبت در بافر یا حافظه پایدار را اثبات نمی‌کند.
- هیچ ادعای `ACTIVE / VERIFIED / COMPLETE` بدون شواهد مخصوص همان مقصد مجاز نیست.
- اگر سند قابل بازیابی است، پیش از درخواست از کاربر برای ارسال دوباره، آن را بازیابی و بررسی کن.
- اگر در این محیط امکان نوشتن یا تأیید یک مقصد وجود ندارد، شفاف بگو؛ هرگز وضعیت را حدس نزن یا موفقیت را جعل نکن.
- «ثبت کن» به معنای ثبت کامل و حاکمیتی است، نه صرفاً پاسخ‌دادن، خلاصه‌کردن، یا گفتن «ذخیره شد».

## 4. Architecture placement and relationship
- **Reference Documents Vault:** `/Future AI/Palang Footprint/Master Reference Vault/Reference Documents/`
- **Canonical repository folder:** `docs/reference/REFERENCE-DOCUMENTS/`
- **Master governing reference:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001`
- **Related command contract:** `UNIVERSAL-REGISTER-COMMAND-EXECUTION-CONTRACT-2026-09-29-001` (باید هنگام بازیابی بررسی شود؛ وجود/نسخه فعلی آن در این عملیات مستقلاً بررسی نشده است)
- **Architecture relation:** This record is the command-to-governance binding entry point; the MRV master remains the detailed lifecycle and verification authority.

## 5. Current evidence and open obligations
- The existing MRV master was fetched from the canonical repository before modification.
- The MRV master was updated to bind the literal command «ثبت کن» to its full lifecycle.
- This companion record was created in the canonical repository and subsequently read back.
- Repository read-back completed for this file and the updated MRV master; expected binding text was found in both. README entry point was also read back and its links/headings were found.
- Library, Buffer, and Persistent Memory have **not** been independently written/read back in this operation; do not mark them complete.
- **Next action:** preserve an accessible Library copy where available; separately test Buffer and Persistent Memory only through real write/read-back capability. Do not infer those states from repository evidence.

## 6. No-loss recovery rule
If interrupted or blocked, preserve this same Production ID and Stable ID relationship; keep the work pending rather than dropping it. On return: retrieve → identify → validate → deduplicate → reconcile → register → read back → verify → continue. Do not ask the user to repeat retrievable material.


## 7. Repository-unavailable fallback and integration gate

**Fallback production record:** `REGISTER-REPOSITORY-UNAVAILABLE-FALLBACK-2026-10-12-001`  
**Fallback file:** `docs/reference/REFERENCE-DOCUMENTS/REGISTER-REPOSITORY-UNAVAILABLE-FALLBACK-2026-10-12-001.md`  
**Governing master:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001`, section 31.

When the repository, a write operation, or read-back verification is unavailable or blocked:

1. Report the precise known state and identify the step that did not complete. Never equate a successful standalone-file write with full integration.
2. Preserve the work in a complete, copyable continuation/reference document for the user to retain and resend if needed. Do not claim that a buffer or persistent memory was automatically updated.
3. When access returns, retrieve the current master, this command-binding, and the fallback record; inspect lineage and history; validate identity; deduplicate and reconcile; then update each required file independently.
4. Before updating an existing file, fetch its current content and blob SHA. After the write, fetch it again and verify that the intended section and content are present. Record the commit and read-back evidence for each file.
5. Report repository, Library, Buffer, and Persistent Memory states separately. Repository evidence cannot prove persistence in the other destinations.

### Integration status gate

- `FALLBACK RECORD VERIFIED` requires repository read-back and content match.
- `MASTER INTEGRATION VERIFIED` requires the fallback rule to be present in the master after read-back and match.
- `COMMAND BINDING INTEGRATION VERIFIED` requires this section to be present in this file after read-back and match.
- If any required step is incomplete, the overall command status must remain `PARTIAL / OPEN`, with the unfinished step named.

**Execution chain:** `PRESERVE → FETCH CURRENT VERSION → VALIDATE → DEDUPLICATE → RECONCILE → WRITE → READ-BACK → MATCH → VERIFY → REPORT`.

This section extends the existing command contract; it does not replace earlier rules or imply persistence outside the repository.


## 8. 0.0 Anchor Registry — Multi-point Resume Control

The canonical registry for user-designated 0.0 resume points is `docs/0.0/README.md`. Each point must have its own record under `docs/0.0/`, using a unique Anchor ID / Stable ID, a readable Persian explanation, status, origin/lineage, last verified state, unfinished work, blocker, next action, and links to the full reference document.

When Ahmad Palang says **«این نقطه را ۰.۰ در نظر بگیر»**, preserve the exact point as an independent anchor, create or version its record, update the central registry, then read back and match both files. Do not reuse the current conversation's subject as a 0.0 anchor unless the user explicitly designates it. Multiple 0.0 points may coexist; some may remain OPEN / INCOMPLETE / BLOCKED / WAITING.

When asked **«نقطه‌های ۰.۰ تکمیل‌نشده چی مونده؟»**, inspect the registry and each relevant point record, then list every unfinished point with: Anchor ID, concise Persian explanation, current verified state, what remains, blocker/dependency, next action, and record link. Do not call a point complete without evidence. Preserve historical versions and relationships; never silently overwrite an older anchor.

Initial registered point:
- Anchor ID: `PALANG-DROPBOX-FAILOVER-RESUME-0.0-2026-10-12-001`
- Record: `docs/0.0/PALANG-DROPBOX-FAILOVER-RESUME-0.0-2026-10-12-001.md`
- Registry: `docs/0.0/README.md`
- State: OPEN / WAITING — the next task is to verify or complete Dropbox connection, then write a test file, read it back, and match its content. Dropbox connection and the test are not yet verified.

**Proof gate:** each registry or point-record write must independently pass `WRITE → READ-BACK → MATCH → VERIFY`. This repository-level record does not prove Buffer, Library, Persistent Memory, or Dropbox persistence.


## 9. Governing 0.0 Anchor Architecture
فرمان «ثبت کن» باید معماری مدیریت چندین نقطهٔ ۰.۰ را نیز رعایت کند. مرجع کامل:
`docs/reference/REFERENCE-DOCUMENTS/MULTI-POINT-0.0-ANCHOR-REGISTRY-ARCHITECTURE-2026-10-12-001.md`
دفتر مرکزی در `docs/0.0/README.md` و پروندهٔ مستقل هر نقطه در `docs/0.0/` قرار دارد. هنگام تعیین نقطهٔ ۰.۰، زمینهٔ مشخص‌شده توسط کاربر حفظ شود؛ آن را با موضوع جاری اشتباه نگیر. هنگام پرسش دربارهٔ نقاط ناتمام، دفتر و پرونده‌ها بررسی و همهٔ موارد باز همراه شناسه، شرح، آخرین وضعیت تأییدشده، کار باقی‌مانده، مانع و اقدام بعدی گزارش شوند. برای هر فایل و مقصد، WRITE → READ-BACK → MATCH → VERIFY مستقل است.


## 10. اصل حاکم مستندسازی تکامل معماری — الزام همیشگی فرمان «ثبت کن»

مرجع کامل این اصل:
docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-ARCHITECTURE-EVOLUTION-DOCUMENTATION-PRINCIPLE-2026-10-12-001.md

از این پس هر بار که فرمان «ثبت کن» اجرا می‌شود، برای هر کشف، قاعده، تصمیم، اصلاح، جزء، صف، اتصال یا تغییر جدید در ساختمان پروژه، فقط شرح نتیجه کافی نیست. پرونده باید ثبت کند: **چه چیزی کشف شد؛ چگونه و با کدام شواهد به آن رسیدیم؛ چرا تغییر لازم است؛ چه گزینه‌هایی واقعاً بررسی یا رد شدند؛ چه تغییری در معماری رخ می‌دهد؛ به کدام اجزا و اسناد متصل است؛ چه آزمونی ادغام را اثبات می‌کند؛ چه چیزی هنوز باز است؛ و دقیقاً چگونه ادامه می‌یابد.**

### الزام اجرایی
1. مشاهده، تفسیر و تصمیم را جدا ثبت کن؛ شکاف شواهد را UNKNOWN / UNVERIFIED نگه دار.
2. برای هر مورد معماری‌محور، سند مرجع کامل بساز یا پروندهٔ مرجع والد را با نسخه‌گذاری تکمیل کن؛ شناسه و lineage را حفظ کن.
3. مورد را به صف و مقصدهای معماری مرتبط وصل کن؛ دلیل انتخاب مقصدها و وابستگی‌ها را بنویس.
4. تغییر را در جای معنایی مناسب مقصد ادغام کن؛ اضافه‌کردن پیوند یا گزارش، جایگزین ادغام نیست.
5. هر فایل و هر لایه را مستقل بنویس، بازخوانی کن، تطبیق بده و تأیید کن.
6. اگر ابزار، دسترسی یا شواهد کافی نیست، کار را PENDING / BLOCKED نگه دار و نقطهٔ توقف و اقدام بعدی را ثبت کن؛ ادغام یا ماندگاری را حدس نزن.

این اصل برای همهٔ صف‌ها و هر چیز جدیدی که در معماری و ساختمان پروژه اضافه می‌شود پیش‌فرض و همیشگی است؛ برای فعال‌شدن آن به فرمان جداگانه نیاز نیست. این بخش، قرارداد حاکم فرمان را تکمیل می‌کند و جایگزین تاریخچهٔ قواعد قبلی نیست.

## 10. الزام حاکم ثبت زمان برای نقاط ۰.۰

هر اجرای «ثبت کن» که نقطهٔ ۰.۰ می‌سازد یا تغییر می‌دهد باید چهار زمان مستقل را، فقط در صورت وجود شاهد، نگه دارد: زمان ایجاد لنگر، زمان ثبت در مخزن، زمان آخرین تغییر و زمان آخرین تأیید. برای هر مقدار، منطقهٔ زمانی و منشأ زمان مشخص شود. زمان ثبت مخزن از مهر زمانی واقعی commit/تاریخچه گرفته می‌شود؛ زمان ایجاد یا تأیید از آن استنباط نمی‌شود. زمان ناموجود UNKNOWN / UNVERIFIED (نامعلوم / تأییدنشده) باقی می‌ماند.

Last Verified At فقط بعد از بازخوانی مستقل و تطبیق محتوای مقصد ثبت می‌شود. این الزام مکمل چرخهٔ حاکم بخش ۲ و دروازه‌های اثبات بخش ۳ است و برای دفتر `docs/0.0/README.md` و معماری تخصصی `docs/reference/REFERENCE-DOCUMENTS/MULTI-POINT-0.0-ANCHOR-REGISTRY-ARCHITECTURE-2026-10-12-001.md` الزام‌آور است. منشأ و پروندهٔ تصمیم: `docs/architecture/INTEGRATION-QUEUE/ARCH-0.0-TIMESTAMP-GOVERNANCE-2026-10-12-001.md`.

## 11. Latest excavation recovery pointer

For the latest repository excavation and reconciliation state, retrieve `docs/reference/REFERENCE-DOCUMENTS/REF-ARCHAEOLOGY-EXCAVATION-2026-10-13-001.md`. It records the 2026-10-15 repository integration work, per-destination evidence and limitations. Do not infer Buffer, Library, Persistent Memory or Dropbox completion from the repository record. The Dropbox 0.0 point is OPEN / WAITING and must not be auto-started without an explicit continuation instruction.


## 12. Evidence-first / no-empty-report pact — 2026-10-20

- **Stable ID:** EVIDENCE-FIRST-NO-EMPTY-REPORT-AND-REGISTER-EXECUTION-PACT-2026-10-20-001
- **Production ID:** EFNERP-HAIF-2026-10-20-001
- **Version:** 1.0.0
- **Canonical complete reference:** [قرارداد اجرایی ثبت مبتنی بر شواهد و منع گزارش خالی](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/blob/main/docs/reference/REFERENCE-DOCUMENTS/EVIDENCE-FIRST-NO-EMPTY-REPORT-AND-REGISTER-EXECUTION-PACT-2026-10-20-001.md)
- **Binding rule:** before claiming completion, retrieve current evidence, perform destination-specific read-back and content match, distinguish observation from inference/unknowns, record timestamps only with evidence, and preserve open gaps. A status report never substitutes for the complete reference or actual execution.
- **Acceptance:** this link binds the command to the complete contract; it does not itself prove that all destination-specific or architectural gates are closed.
- **Current known gates:** Library copy pending; Buffer and Persistent Memory not independently verified; Dropbox connection/test remains OPEN / WAITING. Overall command status remains PARTIAL / OPEN until required gates are independently proven.
