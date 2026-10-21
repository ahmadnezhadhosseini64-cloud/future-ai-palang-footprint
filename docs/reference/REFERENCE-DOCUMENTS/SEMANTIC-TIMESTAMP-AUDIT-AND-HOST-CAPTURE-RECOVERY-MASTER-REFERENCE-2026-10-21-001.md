# سند مرجع مادر: ممیزی معنایی UTC، اتصال میزبان و بازیابی ثبت خودکار

## شناسنامه
- Stable ID: SEMANTIC-TIMESTAMP-AUDIT-AND-HOST-CAPTURE-RECOVERY-MASTER-REFERENCE-2026-10-21-001
- Production ID: STAR-HCR-2026-10-21-001
- Version: 1.0.0
- Owner: احمد پلنگ
- Project: Future AI / Palang Footprint / HAIF
- Canonical timezone: UTC
- Derived local timezone: Asia/Tehran
- Status: ACTIVE / LIVING REFERENCE; LIVE PRODUCER CONNECTION OPEN / NOT PROVEN
- Related event: EVT-0075-ASSISTANT-OUTPUT-TIMESTAMP-SEMANTIC-AUDIT-AND-HOST-ADAPTER-2026-10-21
- Governing registration contract: AUTOMATIC-INTERACTION-REGISTRATION-CONTRACT-2026-10-21-001
- Timestamp standard: ASSISTANT-TIMESTAMP-ANCHOR-STANDARD-2026-10-21-001

## 1. هدف و تصمیم
این سند مبنای ادامهٔ کار برای ثبت خودکار، لنگرگذاری مستقل، ممیزی زمان، اتصال میزبان، بازیابی و مقصدهای مستقل است. فرمان «ثبت کن» محرک اصل ثبت نیست؛ ثبت باید پیش‌فرض معماری باشد. با این حال، هیچ سند یا گردش‌کاری نباید به‌جای مدرک اتصال واقعی میزبان جا زده شود.

## 2. چرا اسکن قبلی کافی نبود
اسکن رشته‌های زمانی فقط می‌گوید در فایل‌ها چه رشته‌هایی شبیه تاریخ/زمان وجود دارد. به‌تنهایی ثابت نمی‌کند که دو رشته متعلق به یک رویدادند، یکی UTC و دیگری زمان محلی متناظر است، منطقهٔ زمانی درست به‌کار رفته، یا زمان پیام با زمان commit اشتباه نشده است. بنابراین موجودی رشته‌ها و تطبیق معنایی/ریاضی دو خروجی جدا هستند.

## 3. قاعدهٔ ممیزی زمان
1. هر timestamp به شناسهٔ رویداد، نقش زمان (پیام، شروع پردازش، نوشتن/commit، read-back، audit)، منبع، دقت و منطقهٔ زمانی وصل شود.
2. UTC مرجع canonical است.
3. جفت UTC/محلی فقط با شواهد رابطهٔ معنایی، مانند شناسهٔ رویداد و برچسب‌های روشن، جفت محسوب می‌شود.
4. هر دو مقدار باید parse شوند و offset/zone معلوم داشته باشند.
5. هر دو به UTC تبدیل و instantها با دقت ثبت‌شده از نظر ریاضی مقایسه شوند؛ اختلاف باید صفر باشد تا جفت PASS شود.
6. مقدار محلی مستقل از مقدار ثبت‌شده با پایگاه IANA یعنی Asia/Tehran برای همان تاریخ محاسبه و مقایسه شود؛ offset ثابت برای همهٔ تاریخ‌های تاریخی فرض نشود.
7. زمان بدون منطقه، ناسازگار، مبهم یا بدون منشأ در دستهٔ REVIEW/UNKNOWN بماند. زمان commit هرگز زمان پیام نیست.
8. گزارش باید تعداد فایل‌های بررسی‌شده، رشته‌های زمانی، جفت‌های صریح، PASS، mismatch، parse error، مبهم و timestampهای بدون جفت را جدا کند. نبودن جفت صریح اثبات نبودن جفت نیست.

## 4. اتصال میزبان و مرز دسترسی
GitHub connector امکان انجام عملیات مخزن را هنگام فراخوانی ابزار می‌دهد. GitHub Actions نیز فقط eventهایی را می‌بیند که GitHub یا یک producer مجاز به آن تحویل دهد. هیچ‌کدام به‌طور خودکار یک subscription برای همهٔ پیام‌های زندهٔ ChatGPT ایجاد نمی‌کنند. اتصال واقعی نیازمند producer/host hook مجاز است که هر پیام را به adapter ارسال کند.

Receiver/adapter مخزنی در scripts/host_adapter.py پیاده‌سازی اولیه شده است و باید حداقل این قابلیت‌ها را داشته باشد: احراز هویت امضاشده، اندازهٔ ورودی محدود، شناسهٔ مستقل، idempotency key، زمان دریافت UTC و تهران، صف پایدار، hash، read-back، رد تعارض، retry/replay و گزارش وضعیت. دریافت موفق در صف به‌معنی نوشتن در GitHub نیست؛ انتقال به مخزن مرحلهٔ جداگانه است.

## 5. آزمون‌های میزبان
- دریافت ورودی ساختگی: ثبت در صف و بازخوانی hash.
- احراز هویت: امضای معتبر پذیرفته و نامعتبر رد شود.
- retry یکسان: همان رویداد برگردد و تکثیر نشود.
- retry با محتوای متفاوت و همان کلید: تعارض صریح 409، بدون overwrite.
- restart: رویداد قبلی پس از راه‌اندازی مجدد قابل بازیابی باشد.
- اتصال producer واقعی: هنوز NOT TESTED تا زمانی که یک میزبان مجاز پیام واقعی را بفرستد.
- ارسال به GitHub: هنوز NOT IMPLEMENTED در receiver اولیه؛ نیازمند توکن محدود، سیاست امنیتی و آزمون مقصد جداست.

## 6. مقصدها و بازیابی
- Repository: اسناد مرجع، رویدادها، کد و شواهد ممیزی.
- Durable inbox / Buffer: رویداد خام مجاز، retry و وضعیت pending/dead-letter؛ ماندگاری پس از restart.
- Library: آینهٔ اسناد موردنیاز برای بازیابی؛ write/read-back جداگانه.
- Persistent Memory: خلاصهٔ بازیابی‌پذیر و قواعد پایدار، نه جایگزین متن مرجع.
- Dropbox: مقصد failover مستقل که اتصالش باید واقعاً برقرار و بازیابی‌اش آزموده شود.
هر مقصد فقط پس از نوشتن و بازخوانی همان مقصد PASS می‌شود. اگر مقصدی در دسترس نیست، رویداد در صف باقی می‌ماند و وضعیت BLOCKED/PENDING می‌گیرد؛ موفقیت مقصد دیگر نباید آن را سبز کند.

## 7. چرخهٔ اجرایی و چکش
CAPTURE → BIND → ANCHOR → CLASSIFY → PRESERVE → QUEUE → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS.
معنی: دریافت → پابند → لنگرگذاری → طبقه‌بندی → حفظ → صف پایدار → نوشتن → بازخوانی → تطبیق → تأیید → آشتی‌دادن نسخه‌ها/مقصدها → وضعیت.
چکش هر بار شناسهٔ یکتا، منبع زمان، تطبیق UTC/محلی، lineage، hash، مقصد، read-back، idempotency و محدودیت‌های اجرایی را می‌سنجد.

## 8. وضعیت شواهد به‌روزشده
- ثبت رویداد EVT-0075 و سند مادر در مخزن باید با commit metadata و read-back مستقل تأیید شود.
- اسکریپت ممیزی معنایی زمان scripts/audit_timestamp_pairs_semantic.py به مخزن افزوده شده و به workflow متصل شده است؛ نتیجهٔ واقعی workflow/artifact هنوز باید جداگانه بازخوانی شود.
- receiver صف پایدار scripts/host_adapter.py و worker انتقال به GitHub scripts/host_adapter_github_worker.py به مخزن افزوده شده‌اند. worker نیازمند GITHUB_TOKEN محدود در secret manager و استقرار روی میزبان است.
- آزمون مصنوعی محلی با نتیجهٔ PASS اجرا شد؛ شاهد: evidence/host-adapter-synthetic-test-2026-10-21-001.md. این آزمون اتصال producer زنده یا نوشتن واقعی به GitHub را آزمایش نکرد.
- receiver میزبان و آزمون‌های مصنوعی به‌عنوان زیرساخت اولیه افزوده شده‌اند؛ موفقیت workflow و آزمون باید جداگانه بررسی شود.
- اتصال producer زندهٔ ChatGPT: OPEN / NOT PROVEN.
- نوشتن به GitHub: worker پیاده‌سازی شده، اما اجرای واقعی با توکن مجاز و read-back مخزن NOT TESTED.
- Buffer، Library، Persistent Memory و Dropbox: هرکدام NOT VERIFIED تا زمانی که شاهد مستقل مقصد ثبت شود.

## 9. ادامهٔ کار
1. اجرای ممیزی معنایی و بررسی گزارش جفت‌های mismatch/parse error/unpaired.
2. اجرای آزمون adapter و بازخوانی نتیجهٔ workflow.
3. اتصال producer مجاز به receiver؛ اگر محیط میزبان هیچ hook یا connector مجاز عرضه نکند، ثبت خودکار سرتاسری از این گفتگو قابل ادعا نیست و باید این شکاف باز بماند.
4. پیاده‌سازی worker انتقال صف به GitHub با توکن محدود و read-back، سپس آزمون قطعی/بازیابی.
5. آزمون مقصدهای مستقل و بازیابی شش سند واقعی پس از restart.
6. ثبت هر نتیجه با زمان commit واقعی، زمان workflow و زمان read-back جدا از زمان پیام.

## 10. اصل صداقت اجرایی
POLICY ACTIVE ≠ LIVE CAPTURE PROVEN. Repository access ≠ host message subscription. Queue accepted ≠ repository written. Workflow success ≠ every message captured. FOUND ≠ RETRIEVED ≠ VALIDATED ≠ REVIVED ≠ VERIFIED ≠ ACTIVE.

## 11. اصلاحیهٔ تصمیم‌ساز — یک جفت زمان برای هر ثبت مخزن
این قاعدهٔ جدید برای ثبت فایل‌ها و رویدادهای مخزن بر الزام قبلیِ چندزمانی اولویت دارد:
1. هر فایل/رویداد ثبت‌شده باید یک جفت زمان ثبت داشته باشد: `repository_registration_utc` و `repository_registration_tehran`.
2. منبع معتبر جفت، زمان واقعی commit تغییر‌دهندهٔ همان فایل است. UTC مرجع است؛ تهران از همان instant ساخته می‌شود.
3. برای زمان‌های داخل محتوا، هر زمان صریح فقط یک بار نرمال‌سازی می‌شود: تهران‌تنها ← UTC معادل؛ UTC‌تنها ← تهران معادل. زمان بدون منطقه فقط با برچسب روشن UTC یا تهران قابل تفسیر است.
4. اگر محتوا زمان ندارد، زمان ثبت فایل از تاریخچهٔ Git به دست می‌آید. اگر تاریخچه در دسترس نباشد، UNKNOWN می‌ماند؛ زمان commit به زمان پیام تبدیل معنایی داده نمی‌شود.
5. اگر جفت UTC/تهران موجود و هر دو ادعا شده‌اند، هر دو به UTC تبدیل می‌شوند و اختلاف ریاضی باید صفر باشد. offset تهران با `Asia/Tehran` برای همان تاریخ نیز تطبیق داده می‌شود.
6. زمان پیام، اگر در دسترس باشد، اختیاری و جداگانه است و شرط ثبت فایل نیست. زمان آغاز پردازش و read-back نیز برای هر ثبت اجباری نیستند.
7. ممیزی باید برای هر فایل آخرین commit تغییر‌دهنده، UTC، تهران، منبع زمان و هش فایل را گزارش کند؛ و برای هر زمان توکار، مقدار اصلی، نقش، UTC معادل، تهران معادل، و هر ابهام/ناسازگاری را ثبت کند.
8. گردش‌کار از checkout با تاریخچهٔ کامل استفاده می‌کند؛ اگر تاریخچه ناقص باشد، نتیجهٔ ممیزی باید محدود/نامطمئن اعلام شود.


## 12. رویداد اصلاح مبنای زمان
- [EVT-0076 — زمان ثبت مخزن معیار واحد](../../architecture/BEHAVIOR-TRACE/EVT-0076-REPOSITORY-REGISTRATION-TIME-IS-CANONICAL-2026-10-21.md).
- اصلاحیهٔ استاندارد حاکم: 1.2.0.
- قاعدهٔ اجرایی: زمان آخرین commit تغییر‌دهندهٔ هر فایل، زمان ثبت آن فایل در مخزن است؛ UTC مرجع و تهران از همان instant محاسبه می‌شود.
- ممیزی تازهٔ اجراشده روی 1,256 فایل، 669 رشتهٔ زمان را یافت؛ 1,256 فایل زمان commit قابل‌استخراج داشتند. اجرای نخست با دسته‌بندی نادرست بعضی خطوطی که هم‌زمان واژه‌های UTC و تهران داشتند، 127 مورد محلی و 81 مورد UTC را برای بازبینی نشان داد. این شمارش به‌عنوان نتیجهٔ نهایی پذیرفته نمی‌شود؛ طبقه‌بندی اصلاح شده و باید نتیجهٔ اجرای جدید بازخوانی شود.


## 13. شاهد ممیزی سرتاسری مخزن — PASS
- Workflow: [Living Architecture Audit #39635817039](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39635817039)
- Workflow head commit: `1c8040316b0f85fbede61b5ccb17d2fb55ae0dda`
- Run start UTC: `2026-10-21T16:33:22Z`; Tehran: `2026-10-21T19:03:22+03:30`.
- Semantic audit execution UTC: `2026-10-21T16:33:30Z`; Tehran: `2026-10-21T20:03:30+03:30`.
- Files scanned (tracked files in scope): 1,232.
- Embedded timestamp strings: 632.
- Every embedded timestamp received a UTC and Tehran normalized pair: 632.
- Ambiguous/parse errors: 0.
- Tehran offset/value mismatches: 0.
- UTC label failures: 0.
- Files with repository registration commit time: 1,232.
- Files without repository registration commit time: 0.
- Result: `REPOSITORY_TIME_NORMALIZATION_PASS`.
- Audit code and all workflow steps completed successfully, including compile checks and synthetic host adapter test.
- Scope boundary: the above validates repository file registration anchors and normalized timestamps in the audited tracked-file scope. It does not prove live ChatGPT producer capture or independent Buffer/Library/Persistent Memory/Dropbox persistence.
