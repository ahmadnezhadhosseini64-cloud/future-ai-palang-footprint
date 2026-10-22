# سند مرجع مادر — اعتبارسنجی اجرایی، لنگر زمانی و بازیابی دفتر تعامل

- Stable ID: PALANG-EXECUTABLE-INTERACTION-LEDGER-MASTER-REFERENCE-2026-10-22-001
- Production ID: ELVR-HAIF-2026-10-22-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / GOVERNING
- Owner: احمد پلنگ
- Project: Future AI / Palang Footprint / HAIF
- Governing event: EVT-0086
- Parent chain: EVT-0083 → EVT-0084 → EVT-0085 → EVT-0086

## 1. حکم رشد معماری
معماری اولیه خط مبنای محفوظ است. هیچ بخش تاریخی نباید بی‌صدا بازنویسی یا حذف شود. این سند قابلیت‌های اجرایی را به‌صورت افزودهٔ نسخه‌دار ثبت می‌کند: اعتبارسنجی طرح‌واره، fixture آزمایشی، آزمون جست‌وجوی معکوس، CI و سپس آزمون بازیابی سرد. تغییرات آینده باید رویداد و شواهد مستقل داشته باشند.

## 2. زنجیرهٔ منابع
- EVT-0086: رویداد آزمون اجرایی.
- EVT-0085: دفتر زوج‌های تعامل، JSON Schema و طرح آزمون بازیابی.
- JSON Schema: docs/architecture/BEHAVIOR-TRACE/interaction-pair-ledger.schema.json
- Fixture ساختگی: docs/architecture/BEHAVIOR-TRACE/fixtures/interaction-pair-ledger-smoke-test.json
- Workflow: .github/workflows/interaction-ledger-validation.yml
- راهنمای دفتر: docs/architecture/BEHAVIOR-TRACE/INTERACTION-PAIR-LEDGER-README-2026-10-22-001.md
- آزمون بازیابی سرد: docs/architecture/BEHAVIOR-TRACE/INTERACTION-RECOVERY-TEST-PLAN-2026-10-22-001.md
- معماری اولیهٔ افزایشی: docs/architecture/BEHAVIOR-SCIENCE-PALANG-FUTURE-AI/INTERACTIVE-BEHAVIOR-APP-ARCHITECTURE-INITIAL-2026-10-22-001.md

## 3. قرارداد زوج
- INT-YYYYMMDD-NNN = شناسهٔ زوج.
- IN-YYYYMMDD-NNN = ورودی.
- OUT-YYYYMMDD-NNN = خروجی.
- پسوند تاریخ/شماره در هر سه شناسه باید برابر باشد.
- شماره‌گذاری پایدار در محیط واقعی، تا پیش از پیاده‌سازی و آزمون شمارنده، فعال تلقی نمی‌شود.
- Fixture موجود ساختگی است و محتوای واقعی کاربر/دستیار نیست.

## 4. اعتبارسنجی و بازیابی
CI تعریف شده است تا طرح‌واره را با Draft 2020-12 بررسی کند، fixture را اعتبارسنجی کند و جست‌وجوی معکوس IN و OUT را آزمایش کند. این آزمون، smoke test ساختگی است؛ اثبات بازیابی یک سرویس واقعی پس از cold start نیست. نتیجهٔ موفق تنها وقتی ادعا می‌شود که اجرای واقعی workflow از GitHub خوانده و نتیجه‌اش ثبت شود.

## 5. لنگر زمانی
- زمان مرجع ثبت مخزن: timestamp واقعی commit نهاییِ تغییر‌دهنده، در UTC.
- زمان تهران: همان لحظهٔ UTC به‌علاوهٔ اختلاف رسمی همان تاریخ؛ برای 2026-10-22 برابر UTC+03:30.
- زمان پیام، زمان رویداد، زمان عملیات، زمان اجرای CI و زمان آزمون فیلدهای جدا هستند.
- زمان گمشده هرگز از زمان محلی فعلی یا حدس ساخته نمی‌شود.
- هر رویداد باید پس از commit، timestamp واقعی را از فرادادهٔ همان commit بخواند و زمان تهران را از آن محاسبه کند.

## 6. وضعیت مقاصد
- Repository: فایل‌های این زنجیره پس از read-back قابل تأییدند.
- GitHub Actions: workflow ثبت شده؛ اجرای موفق تا زمان بازخوانی نتیجه NOT VERIFIED است.
- Gmail / Library / Buffer / Persistent Memory / Dropbox: NOT VERIFIED؛ هر مقصد نیازمند آزمون جداگانه است.

## 7. شکارچی رفتارشناسی
شکارچی، نام نقش معماری برای استخراج الگو از شواهد مجاز است. هر مورد باید OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN طبقه‌بندی شود. ثبت خودکار همهٔ گفتگوها، جمع‌آوری بین نشست‌ها و فعال‌بودن دائمی تا زمان پیاده‌سازی، مجوزهای روشن و آزمون مستقل، ادعا نمی‌شود.

## 8. معیار زنده‌بودن
ACTIVE / LIVING یعنی سند قابل‌توسعه، نسخه‌دار، دارای رویداد و مسیر بازیابی است؛ نه اینکه تمام مقصدها یا جمع‌آوری خودکار حتماً فعال باشند. شکست‌ها و GAPها باید آشکار بمانند.

## 9. گام بعدی
1. خواندن نتیجهٔ اجرای واقعی GitHub Actions.
2. اگر CI سبز بود، ثبت commit و timestamp واقعی UTC/تهران.
3. پیاده‌سازی دفتر پایدار و index جست‌وجوی معکوس.
4. آزمون cold-start واقعی از IN و OUT در محیطی مستقل.
5. ثبت نتیجه در EVT تازه، با شواهد و وضعیت مقصدها.
