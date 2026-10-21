# EVT-0070 — ثبت مستقل خروجی جاری و الزام سراسری لنگرگذاری

- Event ID / شناسهٔ رویداد: `EVT-0070`
- Stable ID / شناسهٔ پایدار: `PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21-002`
- Production ID / شناسهٔ تولید: `POA-HI-2026-10-21-002`
- Version / نسخه: 1.0.0
- Project / پروژه: Future AI / Palang Footprint
- Owner / مالک: احمد پلنگ
- Parent anchor / لنگر والد: `PALANG-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21-001`
- Child anchor / لنگر فرزند: [لنگر مستقل خروجی](../../0.0/PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21-002.md)
- Related event / رویداد مرتبط: [EVT-0069 — واردکنندهٔ کنترل‌شده](./EVT-0069-HAIF-CONTROLLED-REPOSITORY-DOCUMENT-INGESTION-2026-10-21.md)
- UTC reference / زمان مرجع UTC: UNAVAILABLE / NOT CAPTURED — زمان دقیق ایجاد رویداد از فرادادهٔ قابل‌دسترسی قابل‌استخراج نیست.
- Tehran equivalent / معادل تهران: UNAVAILABLE / NOT DERIVED — تا وقتی لحظهٔ دقیق UTC معلوم نیست، معادل تهران ساخته نمی‌شود.
- User message time / زمان دقیق پیام کاربر: UNAVAILABLE / در فرادادهٔ قابل‌دسترسی ثبت نشده است.
- Status / وضعیت: ACTIVE / LIVING / REPOSITORY REGISTRATION PENDING READ-BACK
- Scope / دامنه: ایجاد لنگر مستقل برای خروجی جاری، حفظ دستور کاربر و قاعدهٔ ثبت خودکار هر ورودی/خروجی مرتبط

## ورودی محرک

کاربر تأکید کرد که با آغاز کار، همین خروجی باید لنگر زمانی و مستقل داشته باشد و رویداد آن ساخته و کامل ثبت شود؛ این دستور یک قاعدهٔ کلی و دائمی است و نباید کاربر مجبور به تکرار توضیح آن باشد.

## اقدام ثبت‌شده

1. لنگر مادر و رویداد EVT-0069 و صف موارد باز بازخوانی شدند.
2. واردکنندهٔ کنترل‌شدهٔ شش سند در `prototype/haif-v0/ingest_repository_docs.py` وجود دارد.
3. آزمون واحد قبلی موفق است: 10 passed, 1 warning, 0 failed، run 39611314780.
4. آزمون یکپارچهٔ واردسازی واقعی، جست‌وجوی منشأ و بازیابی پس از restart اضافه شده؛ run 39611543861 در آخرین مشاهده در صف بوده و هنوز موفقیت آن اثبات نشده.
5. این رویداد و لنگر مستقل برای جلوگیری از گم‌شدن خروجی جاری ایجاد شدند.
6. سند مادر و صف باید به این رویداد/لنگر پیوند داده شوند؛ پس از نوشتن باید بازخوانی و تطبیق انجام شود.

## شواهد

- [لنگر مستقل](../../0.0/PALANG-OUTPUT-ANCHOR-HAIF-INGESTION-2026-10-21-002.md)
- [کد واردکننده](../../prototype/haif-v0/ingest_repository_docs.py)
- [آزمون یکپارچه](../../prototype/haif-v0/test_app.py)
- [EVT-0069](./EVT-0069-HAIF-CONTROLLED-REPOSITORY-DOCUMENT-INGESTION-2026-10-21.md)
- [اجرای آزمون یکپارچه در انتظار](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39611543861)

## معیار پذیرش

- لنگر و رویداد هر دو در مخزن موجود باشند.
- هر دو پس از نوشتن دوباره خوانده شوند و شناسه‌ها، پیوندها و وضعیت‌ها تطبیق داده شوند.
- لنگر مادر و صف جاری این زنجیره را ارجاع دهند.
- نتیجهٔ آزمون در انتظار فقط با شاهد تازه بسته شود.
- وضعیت مقصدهای دیگر جداگانه و بدون ادعای ساختگی گزارش شود.

## محدودیت‌ها و اقدام بعدی

این رویداد، اثبات ذخیره‌سازی در Buffer، Persistent Memory، Library یا Dropbox نیست. آزمون یکپارچه نیز تا مشاهدهٔ نتیجهٔ CI باز می‌ماند. اقدام بعدی: بررسی run 39611543861، اصلاح هر خطای واقعی، به‌روزرسانی شواهد و بازخوانی مجدد لنگر/رویداد/سند مادر/صف.

## قاعدهٔ سراسری

هر ورودی/خروجی اجرایی مرتبط با پروژه: ثبت زمان UTC، معادل تهران، منشأ، لنگر مستقل، شناسهٔ رویداد، رابطهٔ والد/فرزند، اقدام واقعی، شواهد هر مرحله، محدودیت، مقصدهای ذخیره‌سازی به تفکیک، بازخوانی، تطبیق و گام بعدی. این قاعده نباید به کاربر واگذار شود تا هر بار یادآوری کند.


## 9. ممیزی پیگیری آزمون و اصلاح خطا — 2026-10-21

- **Read-back / بازخوانی:** لنگر، EVT-0070، سند مادر، EVT-0069 و صف از مخزن دوباره خوانده شدند؛ شناسهٔ لنگر و EVT-0070 در اسناد مرتبط پیدا شد. این، تأیید مخزن برای همان snapshot است.
- **Failure evidence / شاهد شکست:** [HAIF Prototype Tests run 39611543861](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39611543861) شکست خورد: 1 failed, 10 passed, 1 warning. علت: آزمون یکپارچه عبارت جست‌وجوی EVT-0069 را درخواست می‌کرد، درحالی‌که EVT-0069 در allowlist واردکننده نبود؛ جست‌وجو صفر نتیجه برگرداند. این خطای آزمون بود، نه اثبات شکست ذخیره‌سازی API.
- **Correction / اصلاح:** در commit `23ccedc9b2a5e6a9f0c9ccc4f6f62e65041a1fc6` جست‌وجوی آزمون به شناسهٔ سند مرجع مادر که واقعاً در allowlist است تغییر کرد و مسیر مورد انتظار نیز به همان فایل تغییر یافت.
- **Current CI / وضعیت آزمون اصلاح‌شده:** run `39612322105` در آخرین مشاهده IN_PROGRESS بود؛ نتیجه هنوز نامعلوم است.
- **Timestamp integrity / صحت زمان:** زمان دقیق ایجاد لنگر/رویداد و زمان دقیق بازخوانی در فرادادهٔ قابل‌دسترسی موجود نیست؛ UTC و معادل تهران برای این لحظات `UNAVAILABLE / NOT CAPTURED` باقی می‌مانند. زمان runهای CI فقط زمان CI است.
- **Storage destinations / مقصدها:** Repository read-back verified; Buffer, Persistent Memory, Library and Dropbox remain NOT VERIFIED.


### Second integration-test result and correction
- Run [39612322105](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39612322105) failed: 1 failed, 10 passed, 1 warning. The second query was not unique because the master anchor ID appeared in two allowlisted documents; expected count 1, actual count 2.
- Corrected the test query to the master anchor's production ID `PREMA-2026-10-21-001`, commit `987bb7f72488d3c3f9b245445703dac7a7ce5734`. This is a test determinism fix; the next run [39612477894](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39612477894) was queued at the last observation.
- Integration acceptance remains OPEN until the rerun passes. The two failures are retained as evidence, not erased.


### Third integration-test result and correction
- Run [39612477894](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39612477894) failed: 1 failed, 10 passed, 1 warning. The chosen production ID was also present in two ingested documents; count was 2 instead of 1.
- The search endpoint searches title/content (not source_path), confirmed by rereading `prototype/haif-v0/app.py`. The test query now uses the distinctive phrase `Storage proof / اثبات ذخیره‌سازی:` found in the allowlisted master reference, commit `6ff6f8377706dc5d8f0093cab577b9ace5266dbc`.
- The corrected test run must still be observed; integration acceptance remains OPEN until its result is successful.
