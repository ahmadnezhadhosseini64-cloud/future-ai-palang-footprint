# قرارداد معماری اجرای خودکار، لنگرگذاری، ثبت زنده و راستی‌آزمایی
## LIVING INTERACTION AUTOMATION & RECONCILIATION CONTRACT

- Stable ID / شناسه پایدار: LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001
- Production ID / شناسه تولید: LIARC-2026-10-20-001
- Version / نسخه: 1.0.1
- Date / تاریخ: 2026-10-20
- Exact user-message/operation time / زمان دقیق پیام و عملیات: UNKNOWN / UNVERIFIED؛ زمان مستقل دقیق پیام کاربر در شواهد عملیات در دسترس نیست.
- Repository commit time / زمان commit: از تاریخچهٔ مخزن و اجرای خودکار استخراج شود و با زمان پیام یکی فرض نشود.
- Project timezone / منطقه زمانی پروژه: Asia/Tehran (UTC+03:30)
- Owner / مالک: احمد پلنگ (Ahmad Nezhadhosseini)
- Project / پروژه: Future AI / Palang Footprint — آینده AI / ردپای پلنگ
- Canonical path / مسیر مرجع: docs/reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md
- Status / وضعیت: REPOSITORY WRITE + READ-BACK VERIFIED; repository structural audit EXECUTED / VERIFIED in GitHub Actions run 39447083005 (run 23), with a successful artifact-backed audit. External integrations and automatic capture of all ChatGPT conversations remain OPEN / NOT PROVEN.
- Anchor / لنگر: PALANG-0.0-CURRENT-2026-10-20-001; this record does not replace prior independent 0.0 anchors.
- Lineage / زنجیره منشأ: user request to automate interaction anchoring, documentation, architecture integration, timestamping, gap checks, and destination-specific verification.

## 1. Purpose / هدف
این قرارداد از «توصیه و گزارش» به سازوکار اجرایی قابل‌آزمون در مخزن تبدیل می‌شود. هر ورودی کاربر یا خروجی دستیار که در اختیار چرخهٔ ثبت قرار گیرد، باید یک رکورد قابل‌بازیابی، شناسه، منشأ، وضعیت، پیوند معماری، شواهد و اقدام بعدی داشته باشد. اجرای خودکار فقط در محدوده‌ای ادعا می‌شود که workflow یا ابزار واقعی آن را انجام داده و شاهدش قابل‌بازیابی باشد.

## 2. Canonical event lifecycle / چرخهٔ رویداد
ANCHOR → CAPTURE → CLASSIFY → DEDUPLICATE → LINK → TRACE HUMAN → TRACE AI → PRESERVE → REGISTER → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS → RESUME

لنگرگذاری → ثبت رویداد → دسته‌بندی → رفع تکرار → پیوند معماری → ثبت مسیر انسان → ثبت مسیر AI → حفظ → ثبت → بازخوانی → تطبیق → تأیید → یکپارچه‌سازی → تعیین وضعیت → ادامه.

برای هر رویداد، تا حدی که شواهد موجود اجازه می‌دهد:
- Stable ID و Production ID یکتا؛ نسخه؛ تاریخ؛ منطقه زمانی؛ منشأ زمان؛ پروژه و نقطهٔ ۰.۰ مرتبط.
- متن/محتوای قابل حفظ یا ارجاع قابل بازیابی؛ دلیل اهمیت و طبقه‌بندی؛ lineage و وابستگی‌ها.
- مقصدهای موردنیاز با وضعیت مستقل: REGISTERED, VERIFIED, PENDING, BLOCKED, FAILED, UNAVAILABLE یا NOT APPLICABLE.
- شواهد واقعی عملیات، مسیر مقصد، commit/ref یا شناسه اجرای workflow، نتیجه بازخوانی و تطبیق.
- محدودیت‌ها، صف بازیابی، اقدام بعدی و لنگر ادامه.
- زمان پیام، زمان اقدام، زمان commit، زمان بازخوانی و زمان تأیید جدا ثبت می‌شوند. زمان نامعلوم هرگز از زمان دیگری حدس زده نمی‌شود.

## 3. Automatic repository-side enforcement / اجرای خودکار در مخزن
فایل workflow در `.github/workflows/living-architecture-audit.yml` باید در push به شاخهٔ اصلی، pull request، اجرای دستی و برنامهٔ زمان‌بندی‌شده اجرا شود. این workflow اسناد و پیوندهای کلیدی، شناسه‌های مرجع، پروندهٔ خاک‌برداری، صف معماری و قراردادهای لنگر را بررسی می‌کند و گزارش قابل‌دانلود به‌عنوان artifact نگه می‌دارد. شکست آزمون باید workflow را fail کند تا شکاف پنهان نماند.

این آزمون، سلامت ساختاری مخزن را می‌سنجد؛ به‌تنهایی اثبات نمی‌کند که Library، Buffer، Persistent Memory یا Dropbox نوشته و بازیابی شده‌اند. اجرای موفق هم به معنی ادغام تمام شکاف‌های باز نیست.

## 4. Automatic capture boundary / مرز ثبت خودکار تعامل
مخزن GitHub به‌تنهایی به متن تمام گفتگوهای ChatGPT دسترسی ندارد. بنابراین ثبت خودکار «هر پیام در هر گفتگوی ChatGPT» فقط وقتی ممکن است که یک اتصال واقعی مجاز (مثلاً API/webhook یا افزونه/عامل متصل) رویداد را به صف/مخزن بفرستد. این اتصال در این ثبت ساخته یا تأیید نشده است؛ تا زمان اتصال و آزمون end-to-end وضعیت آن NOT_PROVEN / OPEN می‌ماند. این قرارداد به هیچ وجه ادعای دسترسی پنهان یا ثبت همه گفتگوها نمی‌کند.

تا فراهم‌شدن اتصال، در همین گفت‌وگو اجرای ثبت توسط دستیار شامل ایجاد سند/رویداد، شناسه، ثبت زمانی با منشأ، به‌روزرسانی نمایه و صف، بازخوانی و تطبیق مخزن و ثبت موانع است. اگر ثبت واقعی ممکن نباشد، محتوای کامل باید در بستهٔ بازیابی قابل انتقال حفظ شود و مورد در صف باز بماند.

## 5. Destination verification / راستی‌آزمایی مستقل مقصدها
برای هر مقصد:
WRITE → READ-BACK → MATCH → VERIFY → RECORD EVIDENCE.
موفقیت مقصد A به مقصد B تعمیم داده نمی‌شود. برای Library، Buffer، Persistent Memory و Dropbox باید خود مقصد با ابزار مجاز نوشته و دوباره خوانده شود. اگر ابزار/مجوز در دسترس نیست، وضعیت UNAVAILABLE/UNVERIFIED و اقدام بعدی ثبت می‌شود؛ ادعای اتصال برقرار یا فعال ممنوع است.

## 6. Queue and idempotency / صف و جلوگیری از تکرار
- هر شکاف یک Stable ID ثابت دارد؛ تلاش‌های بعدی به همان پرونده و شناسه متصل می‌شوند.
- مورد باز با ثبت جدید بسته نمی‌شود؛ فقط شاهد اجرای واقعی و معیار پذیرش می‌تواند آن را ببندد.
- موارد نیازمند تأیید انسانی، مقصد خارجی یا مجوز، خودکار اجرا/تأیید نمی‌شوند.
- تکرار یک رویداد باید تشخیص داده شود؛ تاریخچه و منشأ حذف نمی‌شوند.
- پس از قطع عملیات، آخرین مرحلهٔ اثبات‌شده و اقدام بعدی ثبت می‌شود.

## 7. Acceptance gates / شروط پذیرش
1. Workflow definition committed and read back.
2. Real GitHub Actions run completed and independently inspectable.
3. Required reference files and links pass automated structural audit.
4. Audit result/artifact identifies run, commit and timestamp.
5. For every external destination, separate real write/read-back/match evidence exists.
6. For automatic ChatGPT capture, a real authorized event source, delivery, durable record, replay/idempotency and read-back test exists.
7. Any failed gate remains OPEN / PENDING with a recovery path.

## 8. Current open gaps / شکاف‌های باز در زمان ثبت
- G-AUTO-01: trigger-to-audit GitHub Actions workflow must run and yield inspectable evidence.
- G-AUTO-02: automatic event source from ChatGPT interaction to repository queue is not connected or proven.
- G-AUTO-03: independent Library write/read-back is unverified.
- G-AUTO-04: Buffer write/read-back is unverified.
- G-AUTO-05: provider-level Persistent Memory write/read-back is unverified.
- G-AUTO-06: Dropbox connection and failover test are open under PALANG-DROPBOX-FAILOVER-RESUME-0.0-2026-10-12-001.
- G-AUTO-07: complete reconciliation with MRV and all historical anchors requires destination-specific read-back.
- G-AUTO-08: full interruption/failure/recovery/idempotency acceptance remains subject to real execution evidence.

## 9. Timestamp and proof policy / سیاست زمان و اثبات
زمان درخواست، زمان نوشتن، زمان commit، زمان اجرای workflow، زمان بازخوانی و زمان تأیید، رویدادهای جدا هستند. برای زمان‌های مخزن از commit timestamp و برای اجرای خودکار از timestamp شناسه اجرای GitHub Actions استفاده شود. هر زمان محلی باید با منطقه زمانی و منشأ ثبت شود. «زمان دقیق نامعلوم» معتبرتر از زمان ساختگی است.

## 10. Recovery / بازیابی
در اجرای بعدی ابتدا این قرارداد، سند جامع خاک‌برداری `COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001`، نمایه مرجع، صف معماری، دفتر شکاف‌ها، دفتر ۰.۰ و آخرین نتیجهٔ workflow خوانده شود. سپس فقط شکاف‌هایی که هنوز شواهد پذیرش ندارند اجرا شوند. پس از هر تغییر: WRITE → READ-BACK → MATCH → VERIFY. اگر دسترسی/اتصال وجود ندارد، پرونده با همان شناسه باز بماند.

## 11. Governing invariants / اصول حاکم
- SPECIFIED ≠ IMPLEMENTED ≠ EXECUTED ≠ VERIFIED.
- Repository success ≠ external destination success.
- FOUND ≠ RETRIEVED ≠ VALIDATED ≠ REVIVED ≠ VERIFIED ≠ ACTIVE.
- INCOMPLETE ≠ LOST; PENDING ≠ BURIED; INTERRUPTED ≠ FAILED.
- No claim without retrievable evidence.
- The architecture is living; every change preserves prior anchors, provenance, time lineage, evidence and recovery pointers.


## 12. Verified repository automation execution / شاهد اجرای خودکار مخزن
- Workflow: `Living Architecture Audit`
- Workflow run: `39447083005` (run number 23)
- Run URL: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39447083005
- Trigger: push to `main`
- Tested commit: `746a04d04fab41b2ad62f1e3f3a1d9ef122539a6`
- Run start / آغاز اجرا: `2026-10-20T15:17:47Z`
- Run completion / پایان اجرا: `2026-10-20T15:18:00Z`
- Result: SUCCESS; `required_files_checked=9`; `result=PASS structural_repository_checks`.
- Evidence artifact: `living-architecture-audit-39447083005`, artifact ID `12275793048`, SHA-256 `c3d358d3326066ad5aa95b42ac5c3a251969082a20a75047ce2952b339b725d5`, retention until `2027-01-18T15:17:48Z`.
- Independent log confirms the workflow ran and uploaded its artifact. This proves only the defined repository structural audit. The log explicitly reports `external_persistence_tested=false` and `chatgpt_all_conversation_capture_tested=false`.
- Current status update: repository-side structural automation is EXECUTED / VERIFIED for this run. Automatic capture of all ChatGPT interactions, Library, Buffer, provider-level Persistent Memory, Dropbox, and full interruption/recovery acceptance remain OPEN / NOT PROVEN.


## 13. Follow-up architecture/build verification — 2026-10-20
- Stable ID: `ARCHITECTURE-BUILD-VERIFICATION-2026-10-20-001`; Production ID: `ABV-2026-10-20-001`.
- Event evidence: [EVT-0024](../../architecture/BEHAVIOR-TRACE/EVT-0024-ARCHITECTURE-BUILD-VERIFICATION-2026-10-20.md).
- A later GitHub Actions run, `39447416772`, was read back after completion; job `audit` has status `completed` and conclusion `success`. This run is distinct from the earlier run 39447083005 recorded above.
- The event and its references have now been integrated into the reference index, architecture integration queue, behavior-trace index and log, pending registration queue, open-gap recovery register, MRV, and 0.0 index. These updates themselves must still pass a subsequent audit run.
- Exact user-message time: UNKNOWN / UNVERIFIED; do not infer it from commits or workflow times.
- External destination write/read-back and automatic capture of every ChatGPT interaction remain OPEN / NOT PROVEN. Dropbox was deliberately not touched in this pass.
