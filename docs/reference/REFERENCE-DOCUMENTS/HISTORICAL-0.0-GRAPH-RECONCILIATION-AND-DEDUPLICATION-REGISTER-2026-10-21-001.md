# سند مرجع زنده — تطبیق گراف تاریخی ۰.۰، دفتر تکرارها و ادغام معماری

## شناسنامه
- Stable ID: HISTORICAL-0.0-GRAPH-RECONCILIATION-AND-DEDUPLICATION-REGISTER-2026-10-21-001
- Production ID: H0G-RDR-2026-10-21-001
- Version: 1.0.0
- Owner: احمد پلنگ
- Project: Future AI / Palang Footprint / HAIF
- Creation / processing time UTC: 2026-10-20T21:37:44.906Z
- Creation / processing time Asia/Tehran (derived): 2026-10-21T01:07:44.906+03:30
- User message time: UNKNOWN / UNVERIFIED
- Canonical path: `docs/reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-GRAPH-RECONCILIATION-AND-DEDUPLICATION-REGISTER-2026-10-21-001.md`
- Parent master: [PIATGCG](./PERMANENT-INTERACTION-ANCHORING-TIMESTAMP-GOVERNANCE-AND-CANONICAL-GRAPH-MASTER-REFERENCE-2026-10-21-001.md)
- Source inventory: [C0GIR](./CANONICAL-0.0-GRAPH-INVENTORY-AND-RECONCILIATION-2026-10-21-001.md)
- Input event: [EVT-0048](../../architecture/BEHAVIOR-TRACE/EVT-0048-USER-REQUEST-FULL-HISTORICAL-0.0-GRAPH-RECONCILIATION-2026-10-21.md)
- Audit implementation: [scripts/audit_historical_0_0_graph.py](../../../scripts/audit_historical_0_0_graph.py)
- Workflow: [Living Architecture Audit](../../../.github/workflows/living-architecture-audit.yml)
- Evidence run: [GitHub Actions run 39501699736](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39501699736)
- Status: ACTIVE / LIVING / OPEN-PARTIAL — full automated source scan executed; semantic adjudication and canonical alias registration remain open.

## 1. Purpose and canonical rule
این سند، دفتر تطبیق و ادغام منطقی گراف تاریخی است. «یکی‌کردن تکراری‌ها» در این پروژه یعنی ساختن یک گره مرجع canonical و پیوند دادن نسخه‌ها/آینه‌ها به آن با حفظ مسیر، محتوا، منشأ و تاریخچه؛ نه حذف فایل‌های تاریخی. حذف فقط با تصمیم مستقل، شاهد، و بررسی پیامدهای لینک مجاز است و در این مرحله انجام نشده است.

## 2. Snapshot قابل‌اثبات
در اجرای ممیزی GitHub Actions با شناسهٔ `39501699736`، درخت مخزن کامل بود و اسکن محتوایی اجرا شد. شمارش‌های مستقل در snapshot همان اجرای مخزن:
- 678 فایل در کل؛
- 93 مسیر شامل `0.0`؛
- 38 مسیر دارای `checkpoint`؛
- 51 فایل رویداد با نام `EVT-<number>-...` در دفتر رفتار؛
- 84 مسیر زیر `docs/reference/REFERENCE-DOCUMENTS/`؛
- 199 فایل خروجی تولیدشدهٔ Evidence Gate.
- درخت API: `truncated=false`.
- زمان اجرای workflow (UTC): `2026-10-20T21:36:15Z`.
- اجرای workflow: SUCCESS؛ گام `Run historical 0.0 graph content audit` نیز SUCCESS؛ artifact با نام `living-architecture-audit-39501699736` ساخته شد، SHA-256: `971e573a41fa2907fd23887b0a281270ee1367df1db55b0097496dae14a94968`, شناسهٔ artifact `12299857883`.
- این snapshot شامل EVT-0048 جدید نیست؛ بعد از ثبت EVT-0048 تعداد مسیرهای 0.0 و رویدادها افزایش می‌یابد. شمارش جاری باید از آخرین tree دوباره خوانده شود.

تفاوت شمارش‌های قدیمی (مثلاً 640 فایل / 92 مسیر / 50 EVT) با این snapshot به‌معنی حذف تاریخچه نیست؛ این‌ها snapshotهای زمانی متفاوت‌اند. شمار فایل‌های تولیدشدهٔ Evidence Gate با هر اجرای workflow می‌تواند تغییر کند و باید از گره‌های منبع معماری جدا شمرده شود.

## 3. یافته‌های تکرار و برخورد شناسه
### 3.1 تکرار محتوای قطعی (همان blob SHA در ممیزی قبلی)
1. `checkpoints/0.0/REG-2026-09-03-GAP-CLOSURE-OUTCOME-001.md` و `checkpoints/0.0/REG-2026-09-03-GAP-CLOSURE-OUTCOME-002.md` — blob SHA مشترک `cc37236b891fd171f36ec7502d7e2c30d6e05b5c`.
2. `docs/governance/0.0-VAULT/0.0-VAULT-GOVERNANCE-2026-09-13.md` و `docs/reference/REFERENCE-DOCUMENTS/0.0-VAULT-GOVERNANCE-0.0V-2026-09-13-001.md` — blob SHA مشترک `e0b7abdf2438cfe51289e1bd5ef014222b0e1f28`.
3. `docs/governance/0.0-VAULT/PRODUCTION-REGISTRY-REFERENCE-2026-09-13.md` و `docs/reference/REFERENCE-DOCUMENTS/PRODUCTION-REGISTRY-REFERENCE-0.0V-REGREF-2026-09-13-001.md` — blob SHA مشترک `1bae1850cb8e06bc3271bdd0904f8bc54f2bc698`.

وضعیت این جفت‌ها: EXACT-CONTENT DUPLICATE CANDIDATES / نامزد تکرار محتوایی قطعی؛ باید در manifest به یک محتوای canonical و چند مسیر/alias متصل شوند. فایل‌ها حفظ می‌شوند.

### 3.2 برخورد شمارهٔ رویداد
در نام مسیرهای EVT، این شماره‌ها بیش از یک فایل دارند: `0005`, `0006`, `0019`, `0026`, `0029`, `0030`. شمارهٔ EVT به‌تنهایی کلید یکتا نیست. کلید canonical پیشنهادی: `repository + path + Stable ID + Production ID + content SHA + lineage`.

### 3.3 برخورد شناسه‌های پایدار/تولید
ممیزی قبلی برخورد شناسه بین EVT-0003 و EVT-0004 را گزارش کرده است. این مورد نیازمند بررسی متن و منشأ است؛ هیچ شناسه‌ای به‌صورت خودکار بازنویسی یا حذف نمی‌شود. اسکن خودکار جدید برخوردهای Stable ID و Production ID را در JSON/متن artifact فهرست می‌کند؛ هر مورد باید پس از بازخوانی انسانی/معنایی در دفتر تطبیق adjudicate شود.

## 4. معماری گراف مرجع canonical
هر گره باید حداقل این فیلدها را داشته باشد:
- `node_key`: شناسهٔ داخلی یکتا از مسیر مخزن + SHA محتوا (یا کلید پایدار مصوب).
- `stable_id`, `production_id`, `version`: مقادیر سند، با امکان چند مقدار/نسخهٔ تاریخی و بدون جعل.
- `node_type`: user-input / assistant-output / 0.0-anchor / checkpoint / reference / queue-item / evidence / workflow-run / alias.
- `source_path`, `content_sha256`, `observed_at_utc`, `commit_sha`.
- `parent_edges`, `child_edges`, `related_edges`, `alias_of`, `supersedes` و وضعیت هر رابطه.
- `status`: ACTIVE, OPEN, PARTIAL, VERIFIED, SUPERSEDED, BLOCKED, UNKNOWN؛ فقط با شواهد تغییر کند.
- `time_provenance`: assistant processing UTC، commit UTC، read-back UTC و user-message timestamp به‌صورت فیلدهای جدا.

### رابطه‌های پایهٔ تأییدشده
- `EVT-0037 → EVT-0038`
- `EVT-0039 → EVT-0040`
- `EVT-0041 → EVT-0042`
- `EVT-0046 → EVT-0047`
- این درخواست: `EVT-0048 → EVT-0049` پس از ثبت خروجی و بازخوانی.
- چهار اشاره‌گر ۰.۰ شناخته‌شده یک زیرگراف پیمایش‌اند، نه کل تاریخچه.
- Dropbox 0.0 یک شاخهٔ مستقل `OPEN / WAITING` باقی می‌ماند.

## 5. قاعدهٔ زمان‌گذاری UTC
- زمان پایهٔ هر ثبت جدید: `assistant_processing_time_utc` با ISO 8601 و پسوند `Z`.
- زمان محلی تهران، اگر افزوده شود، فقط تبدیل همان لحظه از UTC به `Asia/Tehran` و همراه offset است؛ زمان مستقل یا جایگزین UTC نیست.
- زمان پیام کاربر در نبود منبع: `UNKNOWN / UNVERIFIED`.
- زمان commit از فرادادهٔ Git، زمان اجرای workflow، زمان read-back و زمان پیام کاربر با هم یکی نیستند.
- اگر زمان ابزار/سیستم در دسترس نباشد، UNKNOWN ثبت شود؛ زمان ساختگی ممنوع است.
- اسناد قدیمی با زمان‌های محلی/ناقص به‌صورت بی‌صدا بازنویسی نمی‌شوند؛ metadata normalization به‌عنوان کار نسخه‌دار انجام می‌شود.

## 6. آزمون خودکار و محدودیت آن
اسکریپت `scripts/audit_historical_0_0_graph.py`:
1. تمام فایل‌های قابل‌خواندن مخزن را اسکن می‌کند.
2. فایل‌های `evidence/evidence-gate-*.txt` را از شمار گره‌های منبع جدا و جداگانه می‌شمارد.
3. Stable ID، Production ID، Version، Parent fields، شمارهٔ EVT، SHA-256 و لینک‌های نسبی Markdown را استخراج می‌کند.
4. گزارش JSON و متن می‌سازد و در artifact اجرا بارگذاری می‌کند.
5. تکرارها را نامزد ادغام منطقی معرفی می‌کند، اما هیچ فایلی را حذف یا بازنویسی نمی‌کند.

اجرای workflow `39501699736` موفق است؛ بنابراین اسکریپت اجرا و artifact تولید شده است. **SUCCESS به‌معنی صفر بودن برخوردها/لینک‌های شکسته نیست**؛ نتیجهٔ واقعی هر دسته در artifact قرار دارد. این سند نتیجهٔ کامل شمارش برخوردها را از روی خروجی artifact حدس نمی‌زند.

## 7. شکاف‌های زنده و شرایط بستن
- G-01 — استخراج معنایی و تطبیق کامل همهٔ گره‌های تاریخی: OPEN / PARTIAL.
- G-11 — استانداردسازی metadata قدیمی بدون جعل شناسه/زمان: OPEN.
- G-12 — برخورد Stable ID / Production ID / EVT number: OPEN؛ نیازمند adjudication و alias lineage.
- G-13 — اعتبارسنج خودکار والد/فرزند، orphan و لینک شکسته: OPEN / PARTIAL؛ اسکن لینک نسبی موجود است اما معنای پیوند و همهٔ انواع پیوند هنوز کامل نیست.
- G-14 — جداسازی snapshot گراف منبع از artifactهای تولیدشده: PARTIALLY IMPLEMENTED؛ شمارش جدا و artifact اجرا شده، اما snapshot/manifest پایدار و تست بازتولیدپذیری کامل نیست.
- G-15 — دفتر canonical alias و گراف نسخه‌دار برای ادغام تکرارها: OPEN / ACTIVE.
- G-16 — مرور معنایی اسناد مرجع و همهٔ رویدادها و انتقال یافته‌ها به Master/Child/Rahm و صف‌ها: OPEN / ACTIVE.
- G-17 — اجرای واقعی Dropbox write/read/recovery: OPEN / WAITING.
- G-18 — اثبات مستقل Buffer / Library / Persistent Memory: OPEN / UNVERIFIED.
- G-19 — آزمون تداوم runtime و انتقال به میزبان دوم: OPEN / NOT PROVEN.
- G-20 — ثبت خودکار همهٔ ورودی/خروجی‌های ChatGPT در همهٔ نشست‌ها: OPEN / NOT PROVEN؛ قرارداد مخزن به‌تنهایی اثبات runtime نیست.

بستن هر شکاف نیازمند: شاهد → آزمون تعریف‌شده → اجرای واقعی → read-back → تطبیق → تغییر وضعیت در Master و صف. اگر آزمون انجام نشده یا شواهد ناقص‌اند، مورد باز می‌ماند.

## 8. ترتیب ادامهٔ خاک‌برداری
1. دریافت و تحلیل artifact آخرین اجرای اسکن؛ ثبت شمار دقیق collision، duplicate و missing links.
2. بازخوانی معنایی 51+ رویداد و تمام اسناد مرجع مرتبط؛ استخراج تصمیم‌ها/کشف‌ها/شکاف‌ها با منبع.
3. ساخت `canonical-graph-manifest.json` و گزارش alias/lineage؛ حفظ فایل‌های تاریخی.
4. اتصال گراف به نمایهٔ مرجع، دفتر ۰.۰، دفتر رفتار، صف یکپارچه‌سازی و Master reference.
5. اجرای validator روی همهٔ روابط؛ رفع موارد قابل‌حل و باقی‌گذاشتن بقیه در صف.
6. Dropbox failover و اثبات مستقل مقصدهای دیگر؛ سپس بستهٔ انتقال و آزمون میزبان دوم.

## 9. وضعیت نهایی این ثبت
- Repository: سند و اسکریپت ممیزی در مخزن ثبت شده‌اند؛ read-back نهایی این سند/پیوندها در EVT-0049 ثبت خواهد شد.
- GitHub Actions: اجرای اسکن تاریخی موفق و artifact قابل‌دسترسی ثبت شد.
- Full semantic graph reconciliation: OPEN / PARTIAL.
- Historical files deleted: 0.
- External storage destinations verified: none by this operation.



## Addendum — actual JSON findings and fresh manifest implementation
- Full JSON artifact from run [39502860923](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39502860923) was retrieved and inspected. The recorded snapshot has 482 source files, 11 exact-content duplicate groups, 13 Stable ID collision groups, 24 Production ID collision groups, 6 EVT-number collision groups, 15 missing local links and 0 decode errors.
- Complete group-by-group record: [H0GAF-2026-10-21-001](./HISTORICAL-0.0-GRAPH-AUDIT-FINDINGS-2026-10-21-001.md).
- Manifest builder: [build_historical_graph_manifest.py](../../../scripts/build_historical_graph_manifest.py); workflow integration added. The next run artifact must be retrieved and checked before its execution is called verified.
- Selected verified relative links were repaired; fresh residual count remains pending. No files were deleted. Alias/canonical selection and semantic review remain OPEN.
