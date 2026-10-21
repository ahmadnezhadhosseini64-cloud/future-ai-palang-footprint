# سند مرجع مادر — معماری اجرایی آمادهٔ ساخت برای Future AI / Palang Footprint

- Stable ID / شناسهٔ پایدار: FUTURE-AI-PALANG-FOOTPRINT-IMPLEMENTABLE-REFERENCE-ARCHITECTURE-2026-10-21-001
- Production ID / شناسهٔ تولید: FAPF-IRA-2026-10-21-001
- Version / نسخه: 1.0.0
- Date / تاریخ ثبت: 2026-10-21
- Exact user-message time / زمان دقیق پیام کاربر: ثبت نشده؛ UNKNOWN / UNVERIFIED
- Repository audit time / زمان شاهد مخزن: در اجرای ممیزی تازه پس از این commit باید ثبت شود؛ زمان پیام کاربر محسوب نشود.
- Timezone / منطقهٔ زمانی مرجع پروژه: Asia/Tehran (+03:30)
- Owner / مالک: احمد پلنگ (Ahmad Nezhadhosseini)
- Project: Future AI / Palang Footprint — HAIF
- Status: ACTIVE / LIVING / GOVERNING BLUEPRINT; semantic coverage OPEN / PARTIAL
- Canonical path: `docs/reference/REFERENCE-DOCUMENTS/FUTURE-AI-PALANG-FOOTPRINT-IMPLEMENTABLE-REFERENCE-ARCHITECTURE-2026-10-21-001.md`
- Parent: [سند مبنای معماری معنایی](./HISTORICAL-0.0-SEMANTIC-ARCHITECTURE-BASELINE-2026-10-21-001.md)
- Related master: [سند مادر تطبیق گراف تاریخی](./HISTORICAL-0.0-GRAPH-RECONCILIATION-LIVING-MASTER-REFERENCE-2026-10-21-001.md)
- Scope: Repository only. Buffer، Persistent Memory، Library و Dropbox در این مرحله تغییر داده نشده‌اند و تأییدشده محسوب نمی‌شوند.

## 1. هدف اجرایی و معیار واقعی موفقیت

این معماری باید به اندازه‌ای روشن باشد که بر اساس آن بتوان یک برنامهٔ واقعی ساخت، داده وارد کرد، رابطه‌ها را بازبینی کرد، تصمیم‌ها را ثبت کرد، قطع و وصل نشست را تحمل کرد، تاریخچه را بازیابی کرد و از رشد کنترل‌نشدهٔ اسناد جلوگیری کرد.

هدف محصول، ساخت یک «چت‌بات با دفترچهٔ یادداشت» نیست. هدف یک سامانهٔ تداوم تعامل و دانش انسان–AI است که هر ادعا، تصمیم، رابطه و تغییر معماری را به منشأ و شاهد قابل بازیابی وصل می‌کند.

معیار ادعای «آمادهٔ ساخت» این است که مرزهای اجزا، مدل داده، چرخهٔ حالت، API، قواعد حاکمیت، خطاها، آزمون‌های پذیرش و مرز قابلیت‌های تأییدنشده روشن باشند. این سند مشخصات معماری قابل پیاده‌سازی است؛ خودش ادعا نمی‌کند که برنامهٔ کامل با رابط کاربری، پایگاه داده، استقرار و آزمون سرتاسری از قبل ساخته شده است.

## 2. اصل‌های تغییرناپذیر

1. **منبع حقیقت واحد:** هر واقعیت پایدار، تصمیم یا رابطه باید شناسهٔ پایدار، منشأ، نسخه و وضعیت داشته باشد.
2. **بدون ادعای ذخیره‌سازی بی‌شاهد:** WRITE به‌تنهایی پذیرش نیست؛ READ-BACK، تطبیق محتوا و تأیید لازم است.
3. **تداوم بدون ادغام بی‌اجازه:** نشست تازه نباید لنگر ۰.۰ قبلی را حذف یا بازنویسی کند.
4. **گراف غیرمخرب:** فایل‌های تاریخی حفظ می‌شوند؛ نسخهٔ آینه، ارجاع و سند منسوخ حذف خودکار نمی‌شود.
5. **تعریف در برابر ارجاع:** تکرار شناسه تنها علامت بررسی است، نه اثبات برخورد هویت.
6. **شاهد پیش از ارتقا:** هیچ Child، فرضیه یا رابطهٔ حل‌نشده‌ای بدون دروازهٔ پذیرش به Master ارتقا نمی‌یابد.
7. **ابهام آشکار:** دادهٔ ناموجود حدس زده نمی‌شود؛ وضعیت UNRESOLVED / OPEN باقی می‌ماند.
8. **قابلیت حمل:** داده‌ها و خروجی‌ها باید قابل صادرات و بازیابی باشند و به یک فروشنده یا نشست واحد وابسته نشوند.
9. **حداقل دسترسی:** اتصال به مخزن یا سرویس بیرونی باید با مجوز حداقلی، ثبت عملیات و تأیید انسان انجام شود.
10. **حریم خصوصی:** دادهٔ حساس فقط در صورت ضرورت، با هدف و دسترسی مشخص نگهداری شود؛ لاگ‌ها نباید بی‌دلیل متن کامل حساس را کپی کنند.

## 3. مدل لایه‌ای

### L0 — Human Interaction / تعامل انسان
ورودی‌ها، اصلاح‌ها، قصد، سطح اطمینان، موافقت‌ها و زمان‌های قابل اثبات. زمان پیام، زمان پردازش و زمان commit سه فیلد جدا هستند.

### L1 — AI Host / میزبان هوش مصنوعی
مدیریت نشست، تشخیص زمینه، بازیابی مرجع، ارائهٔ پاسخ و پیشنهاد اقدام. Host خودش مرجع حقیقت یا مخزن قطعی نیست.

### L2 — Continuity Core / هستهٔ تداوم
نگهداری لنگرهای ۰.۰ مستقل، نقاط ادامه، شناسهٔ نشست و رابطهٔ «از کجا ادامه دهیم». عملیات جدید باید لنگر جدید بسازد یا به لنگر موجود ارجاع دهد؛ هرگز بی‌صدا لنگر را جایگزین نکند.

### L3 — Evidence & Provenance / شواهد و منشأ
ثبت منبع، مسیر، خط شاهد، hash، نسخه، زمان قابل اثبات، وضعیت بازیابی و زنجیرهٔ تغییر. شاهد ساختاری و شاهد معنایی از هم جدا می‌مانند.

### L4 — Knowledge Graph / گراف دانش
گره‌های سند، پیام، تصمیم، آزمون، شکاف، نسخه، سرویس و مؤلفه؛ یال‌های تعریف، ارجاع، منشأ، والد/فرزند، وابستگی، جایگزینی، پشتیبانی با شاهد، رد یا تناقض.

### L5 — Governance & Promotion / حاکمیت و ارتقا
قواعد Master–Child–Rahm، صف یکپارچه‌سازی، وضعیت شکاف، تصمیم canonical/alias و تأیید انسانی. ارتقا باید یک تصمیم مستقل و قابل بازگشت باشد.

### L6 — Application / برنامهٔ قابل استفاده
داشبورد پروژه، مرورگر گراف، جست‌وجوی مرجع، صف شکاف‌ها، صفحهٔ شاهد، ویرایشگر تصمیم و صفحهٔ آزمون/بازیابی. رابط باید تفاوت وضعیت واقعی و ادعاشده را واضح نشان دهد.

### L7 — Adapters / رابط‌های ذخیره‌سازی
آداپتر Repository به‌عنوان مقصد فعلی؛ آداپترهای آینده برای Buffer، Persistent Memory، Library و Dropbox فقط پس از طراحی مجوز، آزمون نوشتن/بازخوانی و تأیید مستقل فعال می‌شوند. موفقیت یک مقصد به مقصد دیگر تعمیم داده نمی‌شود.

## 4. هستهٔ معماری Master–Child–Rahm

- **Master / هستهٔ مادر:** قراردادها، مدل داده، قواعد پذیرش و روابط تأییدشده.
- **Child / شاخهٔ آزمایشی:** پیشنهادها، نمونه‌ها، فرضیه‌ها، اجزای موقت و تصمیم‌های هنوز تأییدنشده.
- **Rahm / چارچوب اعتبارسنجی:** آزمون شواهد، سازگاری، امنیت، بازیابی و انتقال‌پذیری.
- **Real World / جهان واقعی:** نتیجهٔ استفاده، خطا، بازخورد کاربر و شواهد بیرونی.
- **Feedback / بازخورد:** ورودی جدید برای اصلاح یا رد فرضیه.
- **Promotion / ارتقا:** تنها پس از گذر از معیارهای پذیرش.

چرخهٔ اصلی: MASTER → CHILD → REAL WORLD → FEEDBACK → RAHM → VALIDATION → MASTER یا REJECT/REVISE. ردشدن یک Child شکست سیستم نیست؛ ثبت دلیل و نگهداری تبار آن بخشی از یادگیری است.

## 5. مدل دادهٔ پایه

### Project
`project_id`, `name`, `purpose`, `governance_version`, `created_at`, `status`.

### Artifact
`artifact_id`, `stable_id`, `production_id`, `title`, `artifact_type`, `canonical_path`, `content_hash`, `version`, `status`, `created_at`, `updated_at`, `source_origin`, `owner`.

### Occurrence
یک رخداد از شناسه در متن: `occurrence_id`, `identifier_type`, `identifier_value`, `artifact_id`, `line_start`, `line_end`, `excerpt_hash`, `role_decision`, `review_status`, `reviewer`, `reviewed_at`. مقدار نقش می‌تواند DEFINES، REFERENCES، MIRROR، SUPERSEDED، TRUE_CONFLICT یا UNRESOLVED باشد. حدس خودکار فقط `role_candidate` تولید می‌کند و جای تصمیم را نمی‌گیرد.

### Relation
`relation_id`, `source_artifact_id`, `target_artifact_id`, `relation_type`, `semantic_claim`, `confidence`, `status`, `created_by`, `created_at`, `supersedes_relation_id`.

### Evidence
`evidence_id`, `relation_id` یا `decision_id`, `evidence_type`, `source_path`, `line_range`, `content_hash`, `captured_at`, `capture_method`, `verification_status`. اگر زمان یا خط در منبع در دسترس نیست، فیلد null/unknown می‌ماند؛ مقدار ساخته نمی‌شود.

### Decision
`decision_id`, `subject_id`, `decision_type`, `decision`, `rationale`, `alternatives_considered`, `evidence_ids`, `approved_by`, `approved_at`, `status`.

### Gap
`gap_id`, `title`, `severity`, `scope`, `blocking_relation_ids`, `owner`, `status`, `next_action`, `acceptance_criteria`, `last_verified_at`.

### Anchor
`anchor_id`, `anchor_kind`, `parent_anchor_ids`, `resume_summary`, `open_tasks`, `source_turn_ref`, `message_time`, `time_precision`, `timezone`, `status`. `message_time` فقط وقتی مقدار می‌گیرد که ثبت شده باشد؛ زمان commit جایگزین زمان پیام نیست.

### AuditRun
`audit_run_id`, `commit_sha`, `started_at_utc`, `workflow_version`, `artifact_uri`, `artifact_hash`, `structural_result`, `semantic_result`, `limitations`.

## 6. ماشین حالت برای ثبت و تأیید

برای سند/رابطه: DISCOVERED → CAPTURED → CLASSIFIED → EVIDENCED → REVIEWED → VERIFIED → PROMOTED. مسیرهای جانبی: NEEDS_EVIDENCE، CONFLICTED، REJECTED، SUPERSEDED، DEFERRED. فقط VERIFIED می‌تواند پیشنهاد ارتقا شود؛ PROMOTED نیازمند تأیید مستقل حاکمیت است. انتقال حالت‌ها باید رویداد حسابرسی تولید کند.

چرخهٔ ثبت:
1. گرفتن ورودی و زمان‌های قابل اثبات؛
2. ایجاد لنگر بدون حذف لنگر قبلی؛
3. استخراج نامزدهای شناسه و رابطه؛
4. پیوند دادن شواهد؛
5. داوری انسانی برای معنای نامطمئن؛
6. نوشتن در مقصد مجاز؛
7. خواندن دوباره از همان مقصد؛
8. تطبیق hash/نسخه/شناسه؛
9. ثبت نتیجهٔ پذیرش یا شکست؛
10. ساخت لنگر ادامه با کارهای باز.

## 7. قرارداد API نسخهٔ اول

- `POST /api/v1/anchors` — ایجاد لنگر مستقل؛ پاسخ شامل `anchor_id` و وضعیت پذیرش.
- `GET /api/v1/anchors/{id}` — بازیابی و بازخوانی لنگر.
- `POST /api/v1/artifacts` — ثبت فرادادهٔ سند و منشأ.
- `GET /api/v1/artifacts/{id}` — خواندن سند و وضعیت تأیید.
- `POST /api/v1/relations` — ایجاد رابطهٔ نامزد با شاهد؛ بدون شاهد معنایی، وضعیت VERIFIED نمی‌گیرد.
- `POST /api/v1/relations/{id}/review` — ثبت داوری و دلیل.
- `POST /api/v1/audits` — آغاز/ثبت اجرای ممیزی.
- `GET /api/v1/audits/{id}` — خواندن نتیجه و محدودیت‌ها.
- `GET /api/v1/gaps?status=open` — صف شکاف‌های باز.
- `POST /api/v1/gaps/{id}/resolve` — پیشنهاد بسته‌شدن با معیار پذیرش و شاهد.
- `POST /api/v1/promotions` — درخواست ارتقای Child به Master؛ نیازمند آزمون و تأیید مجاز.
- `GET /api/v1/export?format=jsonl` — صادرات قابل حمل با منشأ.

همهٔ endpointهای تغییردهنده باید idempotency key، اعتبارسنجی، کنترل دسترسی، لاگ تغییر و پاسخ خطای مشخص داشته باشند. حذف سخت از API عمومی نسخهٔ اول ارائه نمی‌شود؛ اصلاح با نسخهٔ جدید، supersede یا tombstone انجام می‌شود.

## 8. رابط کاربری مورد نیاز برای نسخهٔ نخست

1. **Overview / نمای کلی:** وضعیت مخزن، آخرین ممیزی، شکاف‌های باز و آخرین نقطهٔ ادامه.
2. **Artifacts / اسناد:** جست‌وجو، فیلتر بر اساس نوع/شناسه/وضعیت، نسخه‌ها و مسیر canonical.
3. **Graph / گراف:** نمایش گره‌ها و روابط با رنگ/نشانهٔ وضعیت؛ یال بی‌شاهد یا نامطمئن با VERIFIED اشتباه نشود.
4. **Review Queue / صف داوری:** گروه‌های شناسه، شماره‌های EVT، فایل‌های تکراری، ارجاع‌های شکسته و metadata ناقص.
5. **Evidence / شواهد:** متن/خط منبع، hash، روش ثبت و نتیجهٔ بازخوانی.
6. **Anchors / نقاط ادامه:** فهرست چندنقطه‌ای ۰.۰، انتخاب نقطهٔ فعال، ایجاد نقطهٔ جدید بدون overwrite.
7. **Gaps / شکاف‌ها:** مالک، مانع، معیار بستن، شاهد و آخرین تلاش.
8. **Architecture / معماری:** Master، Child، Rahm، وضعیت ارتقا و تبار تصمیم‌ها.
9. **Audit / ممیزی:** commit بررسی‌شده، زمان UTC، نسخهٔ ابزار، خروجی و محدودیت‌ها.
10. **Settings / تنظیمات:** اتصال مقصدها، مجوزها، خروجی‌گیری و retention؛ مقصد غیرفعال نباید به‌صورت متصل نمایش داده شود.

## 9. انتخاب فناوری — پیشنهاد اولیه، نه الزام قطعی

- Backend: Python + FastAPI برای قراردادهای روشن و قابلیت آزمون.
- Persistence: PostgreSQL برای هویت/روابط/تراکنش‌ها؛ محتوای سند با hash و مرجع فایل. برای نمونهٔ محلی می‌توان SQLite را به‌کار برد، اما مهاجرت باید طراحی شود.
- Graph representation: رابطه‌های typed در جداول PostgreSQL در نسخهٔ اول؛ پایگاه گراف جداگانه فقط وقتی حجم و پرس‌وجوها آن را توجیه کنند.
- Frontend: TypeScript + React؛ نمای گراف به‌صورت ماژول مستقل.
- Validation: JSON Schema/OpenAPI، آزمون واحد، آزمون یکپارچه، آزمون رگرسیون داده و آزمون بازیابی.
- Repository adapter: GitHub API با حداقل مجوز و commit-based provenance.
- Deployment: Docker و محیط staging پیش از production؛ secrets فقط در secret manager/environment، نه در مخزن.
- Observability: ساختار لاگ، شناسهٔ همبستگی درخواست، معیارهای شکست و گزارش‌های بدون افشای متن حساس.

این‌ها پیشنهادهای فنی قابل جایگزین‌اند؛ انتخاب نهایی باید پس از نمونهٔ آزمایشی، محدودیت محیط واقعی و نیازهای کاربر تأیید شود.

## 10. مدل امنیت و خرابی

- قطع اتصال: تغییر محلی به‌صورت pending ثبت شود؛ مقصد remote را موفق اعلام نکن.
- اختلاف نسخه: optimistic concurrency؛ به‌روزرسانی روی SHA قدیمی رد شود و ادغام نیازمند reconciliation باشد.
- شکست read-back: عملیات WRITE را موفق نهایی ندان؛ مورد در NEEDS_RECONCILIATION بماند.
- duplicate: ثبت رابطهٔ کاندید؛ حذف خودکار ممنوع.
- prompt injection داخل فایل: متن منبع دادهٔ غیرقابل اعتماد است و اجازهٔ تغییر قواعد حاکمیت نمی‌دهد.
- token افشاشده: ابطال، چرخش و ممیزی دسترسی.
- دادهٔ حساس: حداقل‌سازی، دسترسی مبتنی بر نقش و امکان صادرات/حذف کنترل‌شده با سابقهٔ حسابرسی.
- شکست migration: پشتیبان‌گیری، مهاجرت نسخه‌دار و rollback آزموده‌شده.

## 11. آزمون‌های پذیرش لازم پیش از اعلام «برنامه آماده است»

- A01: ایجاد دو لنگر ۰.۰ مستقل؛ ایجاد دومی اولی را حذف نمی‌کند.
- A02: ثبت artifact با Stable ID و بازخوانی همان نسخه/hash.
- A03: تفکیک تعریف از ارجاع در مجموعهٔ fixtureهای فارسی، انگلیسی و دوزبانه.
- A04: شناسایی collision واقعی بدون false-positive ناشی از index/queue.
- A05: هیچ duplicate به‌طور خودکار حذف نمی‌شود.
- A06: رابطهٔ VERIFIED بدون شاهد معتبر رد می‌شود.
- A07: رابطهٔ unresolved در UI و API آشکار می‌ماند.
- A08: شکست read-back باعث وضعیت موفق نهایی نمی‌شود.
- A09: صادرات JSONL قابل بازخوانی و شامل منشأ است.
- A10: بازیابی پروژه از export/backup در محیط جداگانه موفق است.
- A11: انتقال Child به Master بدون معیار و تأیید رد می‌شود.
- A12: زمان پیام نامعلوم با زمان commit جایگزین نمی‌شود.
- A13: دسترسی مقصد غیرفعال یا ناموفق، connected/verified نشان داده نمی‌شود.
- A14: ورودی مخرب در سند، دستورهای سیستم/حاکمیت را بازنویسی نمی‌کند.
- A15: آزمون رگرسیون پس از تغییر parser، تعداد گروه‌ها و نمونه‌های تعریف/ارجاع را مقایسه می‌کند.
- A16: همهٔ ۴۹۳ فایل در inventory یک نقش بررسی‌شده یا وضعیت OPEN/UNRESOLVED با اقدام بعدی دارند؛ نبودن پرونده به‌اشتباه تأیید تلقی نمی‌شود.

## 12. دروازهٔ «می‌توانیم همین حالا اپ بسازیم؟»

این سند برای شروع طراحی و پیاده‌سازی نسخهٔ نخست کافی است، ولی پیش از برنامهٔ تولیدی باید سه چیز روشن شود:
1. محیط اجرا و مقصد استقرار (محلی، سرور شخصی یا سرویس میزبانی)؛
2. مرز نسخهٔ اول (فقط repository/graph/review یا اتصال چندمقصدی)؛
3. سیاست احراز هویت، دادهٔ حساس و پشتیبان‌گیری.

تا وقتی این سه مورد و آزمون‌های پذیرش اجرا نشده‌اند، عبارت دقیق «مشخصات معماری قابل پیاده‌سازی آماده است» است، نه «اپ کامل و بدون نقص ساخته و آزموده شده است».

## 13. مواردی که عمداً فعلاً وارد هستهٔ Master نمی‌شوند

هر سند/فایل تاریخی که نقش آن هنوز روشن نیست، با مسیر و hash و علت تعویق در Child/Review Queue نگهداری می‌شود. «فعلاً وارد نکردن» به معنای حذف یا بی‌ارزش دانستن نیست؛ یعنی جایگاه معماری آن نیازمند شواهد بیشتر است. موارد نامرتبط نیز باید با دلیل، وضعیت DEFERRED و امکان بازبینی بعدی حفظ شوند.

## 14. برنامهٔ اجرا و ترتیب اولویت

1. اجرای ممیزی ساختاری تازه پس از اصلاح parser و بازخوانی artifact آن.
2. تولید occurrence inventory شامل شناسه، مسیر، خط شاهد، نامزد نقش و ارجاع‌های ورودی/خروجی.
3. داوری دسته‌ای ۱۱ گروه SHA-identical، ۳۳/۴۲ گروه شناسه و تمام گروه‌های EVT؛ اعداد باید از ممیزی تازه به‌روز شوند.
4. بررسی معنایی همهٔ فایل‌های منبع و ثبت موارد خارج از هسته.
5. تبدیل رابطه‌های تأییدشده به قرارداد داده/گراف و سپس نمونهٔ اجرایی.
6. اجرای آزمون‌های پذیرش A01–A16 و آزمون بازیابی مستقل.
7. ثبت رویداد تغییر، بازخوانی سند مادر، به‌روزرسانی صف و ساخت لنگر ادامه.

## 15. معیار خاتمه

این معماری «بدون نقص» ادعا نمی‌شود؛ معماری سالم، نقص‌ها را آشکار، قابل ردیابی و قابل اصلاح نگه می‌دارد. وضعیت هر نسخه باید بر اساس شواهد آزمون همان نسخه اعلام شود. اگر رابطه‌ای هنوز اثبات نشده، در صف می‌ماند و از آن برای تصمیم قطعی Master استفاده نمی‌شود.

## Change log

- v1.0.0 — تعریف معماری اجرایی قابل پیاده‌سازی، مدل داده، چرخهٔ حاکمیت، قرارداد API، اجزای رابط کاربری، امنیت، آزمون‌های پذیرش و دروازهٔ شروع ساخت. این سند specification است، نه ادعای ساخته‌شدن یا استقرار برنامه.


## Addendum v1.1.0 — identifier namespaces
The Artifact/Occurrence model must keep `STABLE_ID`, `PRODUCTION_ID`, and legacy `REFERENCE_ID` as distinct typed namespaces. A generic `Reference ID` label must not be auto-normalized to Stable ID. Parent/lineage resolution may consult all namespaces, but UI collision counts and semantic review decisions must preserve the original type and label. The current repository parser has been updated to reflect this distinction; fresh regression audit remains required after this document change.


## Addendum v1.2.0 — explicit physical-copy and mirror semantics
The Artifact model must distinguish a logical artifact identity from its physical locations. Where two paths have the same SHA-256 and byte size, record a `CONTENT_IDENTICAL_TO` evidence relation; if their roles differ, record `MIRROR_OF` from the reference/provenance copy to the role-based operational candidate. Do not treat identical bytes alone as proof that the canonical path is final. Canonical promotion requires: (1) source/hash read-back, (2) path-role rationale, (3) inbound/outbound link audit, (4) Git-history check where available, (5) review of non-Markdown consumers, and (6) an explicit governance decision. Until all gates pass, retain both paths and set `canonical_status=PROVISIONAL`. Batch evidence: [H0PRRB3](./HISTORICAL-0.0-PRODUCTION-ID-ROLE-REVIEW-BATCH-003-2026-10-21.md), event [EVT-0054](../../architecture/BEHAVIOR-TRACE/EVT-0054-PRODUCTION-ID-ROLE-REVIEW-BATCH-003-2026-10-21.md).


## Addendum v1.3.0 — latest repository structural regression
- [Audit 39520630341](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39520630341) passed on commit `9419d0ced3ae50632d0857eb030516534f3b4312` at `2026-10-21T00:19:43Z` UTC.
- 503 source files; 1,080 local links / 0 missing; 0 decode errors; 38 declared parent edges / 0 unresolved or ambiguous.
- It reports 30 Stable ID groups, 43 Production ID groups, 7 Reference ID groups, 8 EVT groups and 11 exact-content duplicate groups. These are review obligations, not all confirmed identity conflicts.
- This is structural evidence only. Semantic relation review, canonical promotion, application implementation and end-to-end acceptance are separate gates; the application is not claimed built or deployed.
