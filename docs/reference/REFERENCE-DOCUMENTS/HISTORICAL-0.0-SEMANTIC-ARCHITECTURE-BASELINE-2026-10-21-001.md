# سند مرجع مادر — تبدیل ممیزی گراف تاریخی به معماری پایهٔ معنایی

- Stable ID / شناسه پایدار: HISTORICAL-0.0-SEMANTIC-ARCHITECTURE-BASELINE-2026-10-21-001
- Production ID / شناسه تولید: H0SAB-2026-10-21-001
- Version / نسخه: 1.0.0
- Date / تاریخ ثبت: 2026-10-21
- Exact user-message time / زمان دقیق پیام کاربر: UNKNOWN / UNVERIFIED
- Audit evidence time / زمان شاهد ممیزی: آخرین snapshot ثبت‌شده 2026-10-20T22:48:45Z؛ این زمان، زمان پیام کاربر نیست.
- Timezone / منطقه زمانی مرجع پروژه: Asia/Tehran (+03:30)
- Owner / مالک: Ahmad Nezhadhosseini / احمد پلنگ
- Project / پروژه: Future AI / Palang Footprint — HAIF
- Status / وضعیت: ACTIVE / LIVING / GOVERNING; semantic adjudication OPEN / PARTIAL
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Canonical path: docs/reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-SEMANTIC-ARCHITECTURE-BASELINE-2026-10-21-001.md
- Scope: repository only. Buffer, Persistent Memory, Library and Dropbox are not part of this phase and are not claimed verified.

## 1. چرا این سند ایجاد شد

این سند مبنای ادامهٔ کار پس از ممیزی گراف تاریخی ۰.۰ است. هدف نهایی پروژه حفظ تداوم هوشمندی و تداوم کار در تعامل انسان ↔ AI Host ↔ HAIF است، به‌گونه‌ای که تصمیم‌ها، قواعد، شواهد، شکاف‌ها، روابط و مسیر رشد معماری با تغییر نشست یا مدل از دست نروند.

ساختار مقصد:
- HUMAN ↔ AI HOST ↔ HAIF
- MASTER → CHILD → REAL WORLD → FEEDBACK → MASTER
- MASTER → RAHM → VALIDATION → NEW CHILD

AI Host محیط تعامل است؛ Master هستهٔ حاکم؛ Child فضای آزمایش و توسعه؛ Rahm فضای اعتبارسنجی پیش از ارتقا. هیچ سند تاریخی صرفاً به‌دلیل وجود در مخزن یا داشتن شناسه، خودکار عضو هستهٔ Master نمی‌شود.

## 2. مبنای ساختاری تأییدشده

آخرین snapshot مستندشده پیش از این ثبت:
- Workflow run: 39510754774 — SUCCESS
- Audited commit: b17fdcd57d1103df4265d20e6bf6ea7a64a341f4
- Audit UTC: 2026-10-20T22:48:45Z
- Artifact ID: 12306056490
- Artifact SHA-256: sha256:c89191c1f40620518b607edfbd0711bd8a3a9515b6ee862498d0a7e244b97dd4
- Source files: 493
- Text nodes scanned: 493
- Decode errors: 0
- Local Markdown link edges: 944
- Missing local Markdown links: 0
- Declared parent edges: 38
- Unresolved parent edges: 0
- Ambiguous parent edges: 0
- Stable ID repeated-occurrence groups: 33
- Production ID repeated-occurrence groups: 42
- EVT number collision groups: 8
- Exact-content duplicate groups: 11
- Proposed alias edges: 11

این نتیجه، موفقیت ممیزی ساختاری روی commit مشخص‌شده را ثابت می‌کند؛ به‌دلیل ثبت خودکار شواهد پس از آن اجرا، این commit لزوماً آخرین commit فعلی main نیست. اجرای تازه روی تغییرات این سند باید جداگانه بررسی شود.

## 3. وضعیت معنایی واقعی

**وضعیت نهایی تطبیق معنایی: OPEN / PARTIAL — هنوز اثبات کامل نشده است.**

مواردی که نباید با یکدیگر اشتباه شوند:
- تکرار شناسه ≠ برخورد هویت قطعی.
- تطابق SHA ≠ یکسانی نقش معماری.
- پیوند محلی معتبر ≠ رابطهٔ معنایی معتبر.
- استخراج parent edge ≠ اثبات رابطهٔ والد/فرزند.
- workflow موفق ≠ تأیید تمام معنای ۴۹۳ فایل.
- ثبت در صف ≠ ادغام در Master.
- نوشتن فایل ≠ بازخوانی و تطبیق.

هیچ گروهی صرفاً به‌دلیل نتیجهٔ اسکن خودکار «بسته» اعلام نمی‌شود. بسته‌شدن هر مورد نیازمند خواندن متن مرتبط، تشخیص نقش، بررسی lineage/تاریخچه، بررسی ارجاع‌های ورودی و خروجی، ثبت دلیل و بازخوانی پس از تغییر است.

## 4. قرارداد نقش معنایی

برای هر رخداد شناسه در فایل‌ها، دقیقاً یکی از نقش‌های زیر ثبت شود؛ اگر شواهد کافی نیست، UNRESOLVED باقی بماند:
1. DEFINES — فایل شناسه را به‌عنوان هویت اصلی خودش تعریف می‌کند.
2. REFERENCES — فایل فقط به هویت دیگری ارجاع می‌دهد.
3. MIRROR/COPY — نسخهٔ همسان یا آینه با نقش نگهداری مشخص است.
4. SUPERSEDED — نسخهٔ منسوخ‌شده با اشارهٔ روشن به جایگزین.
5. TRUE_IDENTITY_CONFLICT — دو تعریف مستقل به‌طور واقعی یک شناسه را به‌صورت ناسازگار به‌کار برده‌اند.
6. UNRESOLVED — شواهد برای داوری کافی نیست.

برای هر رابطهٔ معنایی نیز این فیلدها الزامی‌اند:
- شناسهٔ مبدأ و مقصد؛
- نوع رابطه و دلیل معنایی؛
- مسیر فایل و خطوط شاهد؛
- شناسه‌ها و نسخه‌های مرتبط؛
- شاهد تاریخچه/commit در صورت نیاز؛
- ارجاع‌های ورودی و خروجی بررسی‌شده؛
- تصمیم، مسئولیت و سطح اطمینان؛
- وضعیت پیش/پس از اصلاح؛
- مسیر تغییر معماری، زمان ممیزی و نتیجهٔ READ-BACK.

## 5. تبدیل گراف به ساختمان معماری

لایه‌های هدف و دروازهٔ ارتقا:
- **لایهٔ منبع تاریخی:** فایل‌های اصلی، checkpointها و رویدادها؛ هیچ‌کدام حذف یا بازنویسی مخرب نمی‌شوند.
- **لایهٔ هویت:** نگاشت Stable ID / Production ID / EVT به مسیرهای تعریف‌کننده، ارجاع‌دهنده، آینه و منسوخ‌شده.
- **لایهٔ روابط:** یال‌های محلی، والد/فرزند، منشأ، جایگزینی، وابستگی و رابطهٔ معنایی؛ هر یال باید شاهد داشته باشد.
- **لایهٔ تصمیم و اختلاف:** دفتر برخورد شناسه‌ها، alias/lineage و موارد unresolved.
- **لایهٔ معماری:** فقط روابطی ارتقا می‌یابند که شاهد و منطقشان ثبت و بازخوانی شده باشد.
- **لایهٔ آزمون:** آزمون ساختاری، آزمون سازگاری شناسه، آزمون رابطه، آزمون بازیابی و آزمون رگرسیون پس از تغییر.

ارتقا به Master زمانی مجاز است که رابطه به منبعش قابل ردیابی باشد، با اسناد مادر تناقض حل‌نشده نداشته باشد، و آزمون/بازخوانی لازم را بگذراند. یافتهٔ آزمایشی می‌تواند در Child یا صف بماند؛ اختلاف حل‌نشده باید آشکار و فعال بماند.

## 6. گام بعدی — مرور دسته‌ای مبتنی بر شاهد

مرور به ترتیب زیر انجام می‌شود؛ هیچ ادعایی مبنی بر تکمیل این مراحل صرفاً از روی برنامهٔ کار مجاز نیست:

### دسته A — ۱۱ گروه محتوای کاملاً یکسان
برای هر گروه: SHA، نقش هر مسیر، commitهای ایجاد/تغییر، ارجاع‌های ورودی، نقش عملیاتی/مرجعی/پرووننس و تصمیم canonical/alias. هیچ فایل حذف نمی‌شود. دو جفتی که شماره‌های متفاوت دارند، تا بررسی تاریخچه و نقش، alias پیشنهادی باقی می‌مانند.

### دسته B — ۳۳ گروه تکرار Stable ID
برای هر رخداد تعیین شود تعریف است یا ارجاع، و اگر چند تعریف وجود دارد آیا تعارض واقعی است یا خیر. ابتدا گروه‌هایی بررسی شوند که شامل رویداد، checkpoint، نمایه و صف هستند؛ سپس تصمیم‌ها به دفتر هویت منتقل شوند.

### دسته C — ۴۲ گروه تکرار Production ID
همان روش دسته B، مستقل از Stable ID. وجود یک Production ID در نمایه یا صف به‌تنهایی برخورد محسوب نمی‌شود.

### دسته D — ۸ گروه برخورد شماره EVT
شمارهٔ EVT به‌تنهایی کلید یکتا نیست. هویت کامل رویداد باید با مسیر کامل، Stable ID، Production ID، SHA، والد، تاریخچه و پیوندهای ورودی تشخیص داده شود. مورد اصلاح اشتباه EVT-0051 و رویداد فعال EVT-0052 باید به‌صورت شفاف در همین داوری دیده شوند؛ شمارهٔ تازه تا بررسی کامل تمام مسیرها انتخاب نمی‌شود.

### دسته E — تمام ۴۹۳ فایل منبع
هر فایل باید حداقل دارای طبقه‌بندی نقش، شناسه/نسخهٔ استخراج‌شده، موضوع/حوزهٔ معماری، والد یا منشأ، ارجاع‌های ورودی/خروجی، وضعیت و سطح اعتبار باشد. فایل‌های بدون metadata یا با متن ناخوانا/مبهم در صف استثنا قرار می‌گیرند؛ دادهٔ گمشده ساخته نمی‌شود.

## 7. معیار بستن شکاف

- G-01 — تطبیق معنایی کامل: OPEN تا پایان مرور تمام فایل‌ها و روابط و ثبت استثناها.
- G-11 — نرمال‌سازی metadata قدیمی: OPEN تا تهیهٔ نگاشت قبل/بعد بدون جعل شناسه یا زمان.
- G-12 — برخورد هویت: OPEN تا داوری هر گروه و ثبت تصمیم و شاهد.
- G-13 — ساختار/پیوند/والد: برای snapshot مشخص‌شده، پیوندهای محلی و parent extraction از نظر ساختاری PASS؛ معنای همهٔ یال‌ها و orphan/cycleها جداگانه نیازمند آزمون است.
- G-14 — تفکیک منبع و شواهد تولیدشده: شمارش‌ها snapshotمحور هستند و باید در هر اجرا با تعریف ثابت ثبت شوند.
- G-15 — manifest و دفتر alias: پیاده‌سازی موجود؛ پذیرش نهایی تصمیم‌های canonical هنوز OPEN.
- G-16 — ارتقای معنایی به معماری: OPEN تا رابطه‌ها شاهددار و در مقصدهای معماری بازخوانی شوند.

## 8. چرخهٔ اجباری هر اصلاح

PRESERVE → IDENTIFY → READ SOURCE → CLASSIFY ROLE → CHECK LINEAGE → CHECK REFERENCES → DECIDE → UPDATE ARCHITECTURE → READ-BACK → MATCH → VERIFY → RE-RUN AUDIT → STATUS.

ترجمه: حفظ → شناسایی → خواندن منبع → تعیین نقش → بررسی تبار → بررسی ارجاع‌ها → تصمیم → به‌روزرسانی معماری → بازخوانی → تطبیق → تأیید → اجرای دوبارهٔ ممیزی → اعلام وضعیت.

هر مرحله‌ای که انجام نشده، صریحاً PENDING/OPEN می‌ماند. نتیجهٔ منفی یا مانع اجرایی نیز با شاهد ثبت می‌شود؛ به‌جای بستن صوری، مورد برای گام بعدی فعال می‌ماند.

## 9. سابقه و زنجیرهٔ اسناد

- [سند مرجع زندهٔ گراف تاریخی](./HISTORICAL-0.0-GRAPH-RECONCILIATION-LIVING-MASTER-REFERENCE-2026-10-21-001.md)
- [دفتر یافته‌های ممیزی](./HISTORICAL-0.0-GRAPH-AUDIT-FINDINGS-2026-10-21-001.md)
- [snapshot گراف و نتیجهٔ ساختاری](./HISTORICAL-0.0-GRAPH-MANIFEST-SNAPSHOT-2026-10-21-001.md)
- [دفتر تصمیم alias و lineage](./HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER-2026-10-21-001.md)
- [EVT-0052 — ساخت manifest و اصلاح پیوندها](../../architecture/BEHAVIOR-TRACE/EVT-0052-CANONICAL-GRAPH-MANIFEST-AND-LINK-REPAIR-2026-10-21.md)

## 10. ثبت وضعیت مقصد

- Repository / مخزن: این سند برای ثبت در مخزن تعریف شده است؛ موفقیت ثبت و بازخوانی باید بر اساس commit و fetch واقعی گزارش شود.
- Buffer / بافر: خارج از دامنهٔ این مرحله؛ آزمون نشده.
- Persistent Memory / حافظهٔ پایدار: خارج از دامنهٔ این مرحله؛ آزمون نشده.
- Library / کتابخانه: خارج از دامنهٔ این مرحله؛ آزمون نشده.
- Dropbox: خارج از دامنهٔ این مرحله؛ آزمون نشده.

## 11. Change log / تاریخچهٔ تغییر

- v1.0.0 — ایجاد مبنای معنایی و معماری از شواهد ساختاری موجود؛ تعریف مرز اثبات، دسته‌های مرور، قواعد نقش، مسیر ارتقا و معیارهای پذیرش. این نسخه به‌خودی‌خود ادعای اتمام داوری معنایی نمی‌کند.


## Addendum v1.1.0 — first semantic review batch
- EVT collision decision register: [H0EVTCA-2026-10-21-001](./HISTORICAL-0.0-EVT-NUMBER-COLLISION-ADJUDICATION-2026-10-21-001.md).
- First reviewed batch: six legacy EVT number pairs (0005, 0006, 0019, 0026, 0029, 0030) were compared by full path, title and available Stable/Production IDs. Each pair represents distinct event subjects; these are short-number namespace collisions, not proof that the two records are one event.
- Closure boundary: all 12 records remain preserved. Their inbound/outbound references have not yet been globally reviewed, and the additional collision groups in the expanded manifest remain open. No renumbering or broad alias rewrite was performed.
- Semantic review of all 493 source files and all ID occurrence groups remains OPEN / PARTIAL.


## Addendum v1.2.0 — definition/reference batch and parser correction
- [H0IRRB-2026-10-21-001](./HISTORICAL-0.0-IDENTIFIER-ROLE-REVIEW-BATCH-001-2026-10-21.md) records evidence-based role decisions for two Stable ID groups.
- The review found a metadata parser coverage gap: actual definitions using bilingual/Persian metadata labels were omitted, making references appear to be duplicate definitions. The regex in the manifest builder was expanded. A fresh audit must confirm the corrected inventory and compare changed counts before any structural claim is refreshed.
- Architecture queue: `docs/architecture/INTEGRATION-QUEUE/README.md`; reference index: `docs/REFERENCE_INDEX.md`.
- Status remains OPEN / PARTIAL: this closes only the role decision for two groups, not the full set of 33/42 groups or all 493 source files.


## Addendum v1.3.0 — executable architecture blueprint
- Implementation-ready specification: [FAPF-IRA-2026-10-21-001](./FUTURE-AI-PALANG-FOOTPRINT-IMPLEMENTABLE-REFERENCE-ARCHITECTURE-2026-10-21-001.md).
- It defines the layered architecture, typed data model, state machine, API v1, UI modules, security/continuity failure handling and acceptance tests A01–A16.
- The blueprint is now connected to the Human–AI Co-Evolution Architecture. This is readiness of the design specification, not a claim that a complete application has been built or passed end-to-end tests.
- The parser now emits a line-level review queue with ID occurrences and inbound/outbound local-link context. A fresh workflow run and artifact read-back are required before accepting its counts or output.


## Addendum v1.4.0 — fresh audit and complete group inventory
- Fresh structural pass: [run 39517339104](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39517339104), audited commit `7d0da46f1e1d5e551bb60fceb3b61b54e7f217dd`, UTC `2026-10-20T23:48:04Z`.
- Current snapshot: 498 source files; 991 local Markdown edges; 0 missing links; 38 parent edges; 0 unresolved/ambiguous parent edges; 37 Stable ID groups; 43 Production ID groups; 8 EVT groups; 11 exact-content duplicate groups; 693 line-level ID occurrences.
- Full group status and bounded decisions: [H0IRAR](./HISTORICAL-0.0-IDENTIFIER-AND-RELATION-ADJUDICATION-REGISTER-2026-10-21-001.md). Evidence details: [H0SRQS](./HISTORICAL-0.0-SEMANTIC-REVIEW-QUEUE-SNAPSHOT-2026-10-21-001.md).
- The successful run confirms structural extraction and queue generation, not full natural-language semantic validation. Semantic acceptance remains OPEN / PARTIAL; the 37/43 groups and 991 edges must not be declared all semantically verified from structural checks alone.


## Addendum v1.5.0 — latest follow-up audit
- [Run 39517544772](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39517544772) succeeded on commit `0e1896e52c80249c90266ef75e2e576eb5a75463` at runner UTC `2026-10-20T23:50:14Z`.
- Latest counts: 500 source files; 1,009 local Markdown edges with 0 missing; 38 declared parent edges with 0 unresolved/ambiguous; 37 Stable ID groups; 43 Production ID groups; 8 EVT groups; 11 exact-content duplicate groups; 695 identifier occurrences.
- Detailed snapshot: [H0SRQS](./HISTORICAL-0.0-SEMANTIC-REVIEW-QUEUE-SNAPSHOT-2026-10-21-001.md); group decisions and outstanding obligations: [H0IRAR](./HISTORICAL-0.0-IDENTIFIER-AND-RELATION-ADJUDICATION-REGISTER-2026-10-21-001.md).
- Structural checks pass. Complete semantic proof remains OPEN / PARTIAL.


## Addendum v1.6.0 — Reference ID namespace and second role-review batch
- The manifest parser now treats generic `Reference ID` as `REFERENCE_ID`, separate from `STABLE_ID`. This avoids conflating reference pointers with Stable IDs while keeping them available for lineage resolution.
- Evidence-based batch 2: [H0IRRB2](./HISTORICAL-0.0-IDENTIFIER-ROLE-REVIEW-BATCH-002-2026-10-21.md) records five Stable ID definition/reference decisions and seven Reference ID role decisions.
- Fresh parser run [39517920781](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39517920781) passed on commit `07c0915db52e66061c7c905081c2bfe77a32e807`: 500 source files; 1,020 local links / 0 missing; 38 parent edges / 0 unresolved/ambiguous; 30 Stable ID groups; 43 Production ID groups; 7 Reference ID groups; 8 EVT groups; 11 duplicate groups; 695 ID occurrences.
- The queue now shows definition candidates only for front-matter metadata lines within the first 40 lines; later nested metadata mentions are classified as reference candidates. This is a triage heuristic, not automatic semantic acceptance.
- Full semantic closure remains OPEN / PARTIAL.


## Addendum v1.7.0 — latest structural acceptance
- Latest pass: [39518314490](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39518314490), commit `230b6cf3145bc27e18f26fc6afc33bd86b033122`, runner UTC `2026-10-20T23:57:41Z`.
- 501 source files; 1,030 local links / 0 missing; 38 parent edges / 0 unresolved/ambiguous; 30 Stable ID groups; 43 Production ID groups; 7 Reference ID groups; 8 EVT groups; 11 duplicate groups; 697 ID occurrences; 0 decode errors.
- Second identifier-role review batch is included in this commit. Full semantic review remains OPEN / PARTIAL; see [H0IRAR](./HISTORICAL-0.0-IDENTIFIER-AND-RELATION-ADJUDICATION-REGISTER-2026-10-21-001.md).


## Addendum v1.8.0 — latest structural acceptance
- [Run 39518486151](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39518486151) succeeded on commit `2b19eeab0c9f8e1b0a16c3a6550b9f791b9cbac8`, runner UTC `2026-10-20T23:59:24Z`.
- 501 source files; 1,041 local links / 0 missing; 38 parent edges / 0 unresolved/ambiguous; 30 Stable ID groups; 43 Production ID groups; 7 Reference ID groups; 8 EVT groups; 11 exact-content duplicate groups; 697 identifier occurrences; 0 decode errors.
- This validates structural extraction after the latest repository integration changes. It does not prove the natural-language meaning of every relation; semantic status remains OPEN / PARTIAL.
