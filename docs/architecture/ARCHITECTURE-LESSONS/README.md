# دفتر زندهٔ درس‌های معماری — Living Architecture Lessons Registry

- Stable ID: PALANG-LIVING-ARCHITECTURE-LESSONS-REGISTRY-2026-10-23-001
- Production ID: LALR-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE
- Owner: Future AI / Palang Footprint
- Governing master: [CMIND — ادامه از مدل اولیه، نه Dropbox](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Governing architecture: [Living Evolutionary Architecture](../../../architecture/ARCH-2026-08-29-001-living-evolutionary-architecture.md)
- Intake: [Live Inbox](../LIVE-INBOX/README.md)
- Verification queue: [Architecture Integration Queue](../INTEGRATION-QUEUE/README.md)
- Current lesson: [LAL-20261023-001](./lessons/LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md)
- Related event: [EVT-0107](../BEHAVIOR-TRACE/EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23.md)

## 1. Purpose
این پوشه مرجع مستقل و قابل بازیابی برای هر درس معماری است. درس نباید در متن گفتگو یا گزارش رویداد گم شود. هر درس شناسهٔ پایدار، منشأ، نسخه، قاعدهٔ عملیاتی، معیار آزمون، نتیجهٔ آزمون، دامنهٔ اعتبار، پیوند به اجزای متأثر و وضعیت جاری دارد.

## 2. Core guarantee and boundary
این دفتر و قراردادش در مخزن ثبت می‌شوند؛ اما ثبت سند به‌تنهایی تضمین نمی‌کند که هر میزبان AI همهٔ تعامل‌ها را خودکار شکار کند یا تمام قواعد را در هر اجرا به‌طور خودکار enforce کند. این توانایی فقط پس از پیاده‌سازی producer/runtime و آزمون مستقل آن قابل ادعاست. تا آن زمان، گردش‌کار ثبت باید هر بار با بازیابی منبع و بررسی قواعد مربوط اجرا شود و شکاف خودکارسازی OPEN بماند.

## 3. Required lifecycle
DISCOVERED → CAPTURED → CLASSIFIED → REGISTERED → READ-BACK VERIFIED → OPERATIONALIZED → TESTED → VALIDATED → INTEGRATED → ACTIVE / LIVING

- DISCOVERED: نشانهٔ اولیه شناسایی شده؛ هنوز درس قطعی نیست.
- CAPTURED: عبارت/منشأ و شواهد حفظ شده‌اند.
- CLASSIFIED: مشاهده، استنباط، فرضیه یا ناشناخته بودن جدا شده است.
- REGISTERED: پروندهٔ نسخه‌دار در مخزن commit شده است.
- READ-BACK VERIFIED: فایل پس از نوشتن مجدداً خوانده و شناسه/پیوند/محتوا تطبیق داده شده است.
- OPERATIONALIZED: درس به قاعده، کنترل، تصمیم یا گام اجرایی قابل‌استفاده تبدیل شده است.
- TESTED: آزمون مشخص با نسخه، ورودی، انتظار، نتیجه و شاهد اجرا شده است.
- VALIDATED: شواهد معیارهای پذیرش را برآورده کرده‌اند.
- INTEGRATED: سند مادر، دفتر درس‌ها، نمایه‌ها، صف، جزء متأثر و تست‌های مربوط هم‌تراز شده‌اند.
- ACTIVE / LIVING: قاعده در مسیر ادامه اعمال می‌شود و با شواهد تازه دوباره ارزیابی می‌گردد.

هیچ مرحله‌ای از روی وجود فایل یا وعدهٔ اجراشده فرض نمی‌شود.

## 4. Append-only, immutable history, and version promotion
1. پروندهٔ ثبت‌شده و نسخهٔ قبلی پاک یا بی‌صدا بازنویسی نمی‌شود.
2. اصلاح با addendum یا نسخهٔ جانشین جدید انجام می‌شود؛ علت، شواهد، آزمون و رابطهٔ supersedes/derived-from ثبت می‌گردد.
3. نسخهٔ جدید تنها پس از عبور از معیارهای پذیرش و ثبت شواهد به CURRENT/ACTIVE ارتقا می‌یابد.
4. نسخهٔ پیشین به‌عنوان تاریخی و قابل‌بازیابی حفظ می‌شود؛ جایگزین‌شدن به معنی حذف یا کپی‌کردن روی آن نیست.
5. هر نسخهٔ جاری به آخرین نسخهٔ پذیرفته‌شده وابسته است، ولی زنجیرهٔ نسخه‌ها و شواهد مستقل می‌مانند.
6. در شکست یا تناقض، آخرین baseline سالمِ اثبات‌شده انتخاب می‌شود؛ تغییر ناموفق حفظ می‌شود و ادامه از نسخهٔ سالم با یک شاخه/نسخهٔ اصلاحی انجام می‌شود. بازگشت باید ثبت شود، نه اینکه تاریخچه پاک شود.

## 5. Verification cadence and no-redundant-retest rule
- در زمان کشف درس: آزمون مستقیم یا شاهد موجود بررسی می‌شود.
- پس از تغییر قاعده، کد، schema، workflow، dependency یا مقصد: آزمون‌های مرتبط دوباره اجرا می‌شوند.
- پس از خطا، regression، تناقض شواهد یا بازیابی: آزمون هدفمند دوباره اجرا می‌شود.
- در checkpointهای چرخه‌ای: ممیزی ساختاری/پیوند/وضعیت اجرا می‌شود؛ این ممیزی جایگزین آزمون رفتاری نیست.
- اگر آزمون در همان نسخه موفق و شاهد معتبر آن ثبت شده باشد، بدون تغییر/نیاز/خطا/تناقض همان آزمون تکراری انجام نمی‌شود. قاعدهٔ NO-REDUNDANT-RETEST حفظ می‌شود.
- آزمون باید نسخهٔ مورد آزمون، پیش‌شرط، روش، نتیجه، شاهد قابل‌بازخوانی و محدودهٔ ادعا را ثبت کند.

## 6. Universal rule for every material artifact
هر درس، سند، کد، schema، آزمون، لنگر، صف، شاخص، اتصال، checkpoint و جزء معماری باید:
- ID پایدار و مسیر canonical داشته باشد؛
- منشأ و زنجیرهٔ parent/related را نگه دارد؛
- version و وضعیت جداگانه داشته باشد؛
- شاهد ثبت، بازخوانی و آزمون را از هم تفکیک کند؛
- به مالک/جزء/صف اقدام بعدی متصل باشد؛
- تاریخچهٔ نسخه‌ها و مسیر بازیابی را حفظ کند؛
- در برابر تغییرات مرتبط و شواهد متناقض دوباره ارزیابی شود.

## 7. Current lesson inventory (initial, not exhaustive)
| Lesson ID | Lesson | Operational rule | Current state |
|---|---|---|---|
| LAL-20261023-001 | درس معماری نباید فقط نوشته شود؛ باید عملیاتی، آزموده و به چرخهٔ نسخه‌پذیر وصل شود | هر درس → کنترل/آزمون/شاهد/بازخوانی/ارتباط/بازیابی | REGISTERED / READ-BACK PENDING |
| EVT-0103 | کشف رفتاری و برخورد شناسه باید آشکارا ثبت و اصلاح شود | طبقه‌بندی شواهد؛ یکتایی ID پیش از write؛ regression test | Existing event; runtime remains OPEN |
| EVT-0093 | تعامل پروژه‌محور واحد رشد است | IN/OUT/EVT → inbox → master → action → evidence | Existing event |
| NO-REDUNDANT-RETEST-2026-09-03-001 | آزمون بسته‌شده و معتبر بی‌دلیل تکرار نشود | retest on change, deployment, need, error, regression, conflicting evidence | Existing registered rule |
| EVT-0106 | لنگر تاریخی مقصد نباید مسیر جاری را منحرف کند | بازیابی آخرین 0.0/master/queue پیش از انتخاب اقدام | Existing event |

این جدول فقط فهرست آغازین است؛ ادعای شمارش کامل همهٔ درس‌های تاریخی نیست. مرحلهٔ بعد باید همهٔ درس‌های پراکنده را از event، inbox، master، registry و queue استخراج و با حفظ منشأ به این دفتر وصل کند.

## 8. Audit checklist
- [ ] هر درس کشف‌شده شناسهٔ مستقل دارد.
- [ ] هر درس به ورودی/رویداد/سند مادر و جزء متأثر پیوند دارد.
- [ ] قواعد عملیاتی با متن درس سازگارند.
- [ ] آزمون و معیار پذیرش مشخص‌اند.
- [ ] نتیجهٔ آزمون شاهد واقعی دارد یا صریحاً NOT RUN است.
- [ ] نسخهٔ پیشین حفظ و رابطهٔ نسخه‌ها ثبت شده است.
- [ ] نمایه، صف، master و پیوندهای داخلی read-back شده‌اند.
- [ ] وضعیت runtime/host/external از وضعیت repository جداست.
- [ ] شکست‌ها و علت‌های محتمل از علت‌های اثبات‌شده تفکیک شده‌اند.
- [ ] rollback/recovery از baseline سالم دارای آزمون و شاهد است.

## 9. Known open gaps
- Automatic capture of every host interaction and automatic lesson candidate extraction: OPEN / NOT PROVEN.
- Enforcing every lesson in every future host/runtime without a retrieval/invocation mechanism: OPEN / NOT PROVEN.
- Full repository-wide migration/count of all historical architecture lessons into this directory: OPEN.
- Tested rollback/recovery across every component and external destination: OPEN / NOT PROVEN.
- External persistence beyond the canonical repository: NOT ATTEMPTED in this registration.

## 10. Change rule
این README خودش نسخه‌پذیر است؛ اما تغییرات باید append-only و شاهددار باشند. هر به‌روزرسانی، نسخهٔ قبلی را از تاریخچه حذف نمی‌کند. این دفتر تا رسیدن به شاهد تازه ACTIVE / LIVING می‌ماند؛ هر بار که درس جدید، شکست، تناقض یا تغییر معماری کشف شود، دفتر و آزمون مربوط باید به‌روزرسانی شوند.
