# سند مرجع مادر زنده — حاکمیت دائمی لنگر تعامل، زمان‌گذاری، گراف مرجع و معماری قابل‌انتقال HAIF

## شناسنامه و وضعیت
- Stable ID / شناسه پایدار: PERMANENT-INTERACTION-ANCHORING-TIMESTAMP-GOVERNANCE-AND-CANONICAL-GRAPH-MASTER-REFERENCE-2026-10-21-001
- Production ID / شناسه تولید: PIATGCG-2026-10-21-001
- Version / نسخه: 1.0.7
- Owner / مالک: Ahmad Nezhadhosseini / احمد پلنگ
- Project / پروژه: Future AI / Palang Footprint — آیندهٔ AI / ردپای پلنگ
- Scope / دامنه: حاکمیت تعامل، لنگر ورودی/خروجی، زمان‌گذاری، گراف تاریخی ۰.۰، ثبت معماری، خاک‌برداری، بستهٔ انتقال میزبان
- Creation processing time UTC: 2026-10-20T20:56:16.235Z
- Creation processing time Asia/Tehran: 2026-10-21T00:26:16.235+03:30
- User message time: UNKNOWN / UNVERIFIED — منبع قابل‌اعتماد زمان پیام در زمینهٔ اجرایی موجود نبود.
- Canonical path: `docs/reference/REFERENCE-DOCUMENTS/PERMANENT-INTERACTION-ANCHORING-TIMESTAMP-GOVERNANCE-AND-CANONICAL-GRAPH-MASTER-REFERENCE-2026-10-21-001.md`
- Status: ACTIVE / LIVING / GOVERNING — قاعدهٔ معماری ثبت و نسخه‌گذاری شده؛ اجرای سراسری در تمام نشست‌ها/میزبان‌ها تا آزمون runtime اثبات‌نشده است.
- Input event: [EVT-0046](../../architecture/BEHAVIOR-TRACE/EVT-0046-USER-REQUEST-GOVERNING-ANCHORING-TIMESTAMP-AND-GRAPH-RECONCILIATION-2026-10-21.md)
- Output event: [EVT-0047](../../architecture/BEHAVIOR-TRACE/EVT-0047-ASSISTANT-GOVERNANCE-REFERENCE-AND-GRAPH-INVENTORY-2026-10-21.md)
- Parent references: [Universal Interaction Anchor Contract](./UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md); [Portable HAIF master](./UNIVERSAL-REGISTER-AND-PORTABLE-HAIF-ARCHITECTURE-MASTER-REFERENCE-2026-10-20-001.md); [Two-Time Anchoring](./TWO-TIME-ANCHORING-AND-LIVING-CONTINUITY-ARCHITECTURE-2026-10-20-001.md); [Four-linked 0.0 chain](./FOUR-LINKED-0.0-CHAIN-AND-BEHAVIORAL-DISCOVERY-GATE-2026-10-20-001.md); [Audit reference AAAPHR](./AUTOMATIC-ANCHORING-ARCHITECTURE-AUDIT-AND-PORTABLE-HAIF-REFERENCE-2026-10-21-001.md)

## 1. هدف نهایی پروژه — مرجع حاکم
هدف صرفاً ثبت گفتگو یا تولید گزارش نیست. هدف ساخت معماری قابل‌انتقال و قابل‌رشد HAIF (Human–AI Interaction Future — آیندهٔ تعامل انسان و هوش مصنوعی) است؛ معماری‌ای که تعامل‌های قابل‌دسترسی و مجاز، روش‌های مشاهده‌پذیر تعامل، قواعد، شواهد، آزمون‌ها، خطاها، ایده‌ها و شکاف‌ها را حفظ کند؛ از آن‌ها الگوهای مستند استخراج کند؛ فرضیه‌ها را در فضای آزمایش ایزوله بیازماید؛ و فقط تغییرهای تأییدشده را به هستهٔ اصلی ارتقا دهد. در زمان دلخواه کاربر باید بتوان یک بستهٔ کامل و قابل‌بازیابی از معماری تا یک نقطهٔ زمانی معین ساخت و آن را به میزبان AI دیگری منتقل کرد تا میزبان مقصد با اتکا به بسته، پروژه را بازسازی و ادامه دهد.

معماری مفهومی:
- HUMAN ↔ AI HOST ↔ HAIF
- MASTER → CHILD → REAL WORLD → FEEDBACK → MASTER
- MASTER → RAHM → VALIDATION → NEW CHILD
- CAPTURE → ANCHOR → LINK → PRESERVE → ANALYZE → HYPOTHESIZE → TEST → REVIEW → PROMOTE / KEEP OPEN

تعریف اجزا:
- Master / هستهٔ اصلی: قواعد و معماری تأییدشده.
- Child / شاخهٔ آزمایشی: ایده‌ها و تغییرهای در حال بررسی؛ اختیار تغییر مستقیم Master ندارد.
- Rahm / رحم اعتبارسنجی: فضای جدا برای آزمون و بررسی شواهد.
- Host Adapter / رابط میزبان: لایه‌ای برای سازگارکردن معماری با امکانات و محدودیت‌های میزبان جاری.
- Evidence Vault / صندوق شواهد: شواهد منشأدار، رویدادها، آزمون‌ها، خطاها، ایده‌ها و نتایج.
- Canonical Graph / گراف مرجع یکتا: شبکهٔ پیوند میان ورودی، خروجی، لنگرهای ۰.۰، اسناد مرجع، نسخه‌ها، تصمیم‌ها، آزمون‌ها، صف‌ها و بسته‌های انتقال.

## 2. قاعدهٔ دائمی ثبت هر ورودی و خروجی
این قاعده پیش‌فرض معماری است و به درخواست جداگانهٔ «ثبت کن» وابسته نیست. هر پیام کاربر و هر خروجی معنادار دستیار باید به‌عنوان رویداد مستقل با شناسهٔ پایدار ثبت شود؛ ورودی و خروجی به هم پیوند داشته باشند؛ لنگر زمانی و منشأ داشته باشند؛ و در صورت ایجاد قاعده، تصمیم، کشف، شکاف یا تغییر، به سند مرجع و ساختمان پروژه وصل شوند.

چرخهٔ استاندارد:
1. CAPTURE — ثبت محتوای واقعی ورودی/خروجی و زمینهٔ لازم.
2. IDENTIFY — تخصیص Stable ID، Production ID و Version.
3. ANCHOR — تخصیص شناسهٔ لنگر و پیوند به زنجیره/۰.۰ فعال، بدون حذف لنگرهای قبلی.
4. TIME-STAMP — ثبت زمان‌های مستقل طبق بخش ۳.
5. PROVENANCE — ثبت منبع، والد، رویداد مرتبط، commit و شواهد قابل‌مشاهده.
6. CLASSIFY — تعیین نوع: درخواست، تصمیم، قاعده، کشف، فرضیه، آزمون، نتیجه، شکاف یا اقدام.
7. PRESERVE — نوشتن در مقصدی که واقعاً در دسترس است؛ هر مقصد جداگانه وضعیت می‌گیرد.
8. READ-BACK — بازخوانی محتوا از همان مقصد.
9. MATCH — تطبیق شناسه، نسخه، محتوا و پیوندها.
10. RECONCILE — تطبیق با سند مرجع، گراف ۰.۰، صف‌ها و Master/Child/Rahm.
11. ARCHITECTURE UPDATE — افزودن تغییر به بخش مناسب معماری، نمایه و صف؛ ثبت علت و شواهد.
12. VERIFY — اجرای آزمون متناسب و ثبت نتیجهٔ PASS/FAIL/BLOCKED/NOT RUN.
13. STATUS — گزارش کوتاه وضعیت واقعی، محدودیت‌ها و اقدام بعدی؛ گزارش، جایگزین سند کامل نیست.

اگر یک خروجی صرفاً گفتگوی روزمره و بدون ارزش معماری باشد، رویداد آن همچنان در زنجیرهٔ تعامل باید قابل‌شناسایی باشد؛ اما ثبت آن نباید به‌دروغ ادعا کند که یک سند مرجع مستقل لازم است. در صورت نبود ابزار نوشتن، باید رکورد کامل قابل‌کپی و وضعیت NOT WRITTEN ارائه شود. این قرارداد به‌تنهایی اجرای خودکار در هر میزبان یا هر نشست را اثبات نمی‌کند؛ این بخش نیازمند آزمون اجرایی است.

## 3. حاکمیت زمان — پیشنهاد کاربر پذیرفته و به قاعده تبدیل شد
زمان پردازش داخلی دستیار برای زمان ثبت و اجرای عملیات، زمان پایهٔ عملیاتی است؛ زیرا زمان پیام کاربر همیشه در دسترس نیست. اما زمان پردازش نباید جای زمان پیام کاربر را جعل کند. هر کدام فیلد مستقل دارد.

فیلدهای لازم:
- `user_message_time`: زمان پیام کاربر از منبع معتبر؛ اگر موجود نیست `UNKNOWN / UNVERIFIED`.
- `assistant_processing_time_utc`: زمان داخلی واقعی در شروع/نقطهٔ ثبت عملیات، UTC.
- `assistant_processing_time_local`: نمایش همان لحظه در منطقهٔ زمانی مشخص‌شده، با offset.
- `repository_commit_time`: زمان commit طبق فرادادهٔ GitHub؛ پس از دریافت مدرک commit ثبت شود.
- `readback_time`: زمان بازخوانی واقعی از مقصد.
- `external_destination_time`: فقط وقتی مقصد خارجی نتیجه و زمان واقعی برگرداند.
- `event_time_precision`: ثانیه، میلی‌ثانیه، دقیقه یا نامشخص.
- `timezone_source`: منطقهٔ زمانی و منشأ آن.

قواعد:
1. از ساعت داخلی اجرای ابزار برای زمان پردازش استفاده کن و UTC را مرجع بی‌ابهام قرار بده.
2. زمان محلی را فقط با offset یا منطقهٔ زمانی مشخص‌شده نمایش بده؛ تبدیل محلی، زمان پیام کاربر نیست.
3. زمان پیام کاربر هرگز از زمان فعلی یا زمان پردازش حدس زده نشود.
4. زمان commit با زمان پردازش و زمان read-back یکی نیست.
5. اگر ساعت داخلی ابزار در دسترس نیست، زمان را UNKNOWN / UNVERIFIED بگذار؛ زمان خیالی نساز.
6. هر زمان دارای منبع، دقت و معنای مشخص باشد؛ timestamp بدون معنا کافی نیست.
7. ترتیب رخدادها با شناسه و پیوند رویدادها حفظ شود؛ اگر ساعت‌ها ناسازگارند، تضاد را ثبت کن، نه اینکه تاریخ را بی‌صدا بازنویسی کنی.

## 4. لنگرها و نقاط ۰.۰
۰.۰ یک نقطهٔ واحد و قابل‌جایگزینی نیست؛ چند لنگر مستقل می‌توانند موازی، والد/فرزند یا هم‌پوشان باشند. فهرست چهارلنگری، تنها میان‌بر پیمایش است، نه کل تاریخچه. هیچ لنگر تاریخی با ایجاد نقطهٔ تازه بسته یا بازنویسی نمی‌شود، مگر آنکه شواهد و دستور صریح برای بستن همان لنگر وجود داشته باشد.

چهار اشاره‌گر ناوبری شناخته‌شده از تاریخچهٔ اخیر:
- `PALANG-0.0-MAIN-LOCK-2026-10-20-002`
- `PALANG-0.0-CURRENT-2026-10-20-001`
- `OUTPUT-ANCHOR-CHAIN-AND-SESSION-CLOSE-0.0-2026-10-19-002`
- `PALANG-DROPBOX-FAILOVER-RESUME-0.0-2026-10-12-001` — OPEN / WAITING.

این چهار شناسه، نمایهٔ تاریخی کامل نیستند. برای گراف کامل باید همهٔ مسیرهای ۰.۰، checkpointها، اسناد مرجع، رویدادها، نسخه‌های بایگانی و اشاره‌گرهای داخل فایل‌ها بررسی شوند.

## 5. روش تطبیق گراف مرجع
برای هر فایل/گره این فیلدها استخراج شوند:
- path، filename، title، Stable ID، Production ID، Version، status
- نوع گره: ورودی، خروجی، ۰.۰، سند مرجع، قرارداد، آزمون، تصمیم، صف، آرشیو یا مقصد ذخیره‌سازی
- parent IDs، child IDs، related IDs، canonical reference، supersedes/superseded-by
- زمان‌ها و منشأ زمان، commit SHA، content SHA، آخرین read-back
- وضعیت پیوندها، شواهد و اقدام بعدی

مراحل:
A. فهرست درختی مخزن از Git tree recursive؛ ثبت تعداد کل فایل‌ها، تعداد نتایج و اینکه tree کامل یا truncated بوده.
B. استخراج همهٔ فایل‌های مرتبط با ۰.۰، checkpoint، anchor، register، timestamp، behavior trace، reference و queue.
C. بازخوانی محتوای فایل‌ها و استخراج شناسه‌ها از متن، نه فقط نام فایل.
D. ساخت شاخص شناسه‌ها: هر شناسه ← همهٔ مسیرهایی که آن را تعریف/ذکر می‌کنند.
E. تشخیص:
- تکرار نام فایل؛
- تکرار Stable ID با محتوا یا نسخه‌های متفاوت؛
- تکرار Production ID؛
- نسخه‌های مشابه با lineage نامعلوم؛
- ارجاع شکسته؛
- گره بدون والد/مرجع؛
- گره یتیم بدون فرزند/پیوند؛
- چرخهٔ ناخواسته؛
- ادعای وضعیت متناقض.
F. مقایسهٔ شناسه‌های تعریف‌شده با ارجاع‌شده؛ ایجاد جدول روابط پیشنهادی.
G. هر اتصال خودکار فقط برای پیوند قطعی و بدون ابهام مجاز است؛ موارد مبهم به صف بررسی می‌روند.
H. هیچ حذف/ادغام مخرب انجام نشود؛ نسخهٔ تاریخی حفظ و فقط canonical pointer افزوده شود.
I. گراف بعد از تغییرها دوباره از مخزن خوانده و صحت پیوندها سنجیده شود.
J. وضعیت G-01 فقط پس از پوشش کامل دامنه، رسیدگی به همهٔ اختلاف‌ها یا ثبت استثناهای توضیح‌دار، read-back و آزمون بازیابی قابل‌بستن است.

## 6. تکراری‌ها و نسخه‌گذاری
نام مشابه به معنی محتوای یکسان نیست؛ محتوای مشابه به معنی lineage یکسان نیست. قبل از merge:
- Stable ID و Production ID مقایسه شوند؛
- version و زمان/commit بررسی شود؛
- تفاوت محتوا محاسبه/بررسی شود؛
- parent/child و وضعیت تاریخی حفظ شود؛
- اگر یکی نسخهٔ تازهٔ دیگری است، رابطهٔ `supersedes` ثبت شود، نه حذف فایل قدیمی؛
- اگر شناسهٔ یکسان برای دو مفهوم متفاوت به‌کار رفته، هر دو مورد ثبت و اصلاح شناسه با lineage شفاف انجام شود.

## 7. معماری کشف و رشد
ردپای تعامل صرفاً لاگ نیست. داده‌های ثبت‌شده می‌توانند برای تحلیل بازهٔ زمانی و کشف الگو استفاده شوند، اما باید چهار سطح از هم جدا بمانند:
1. Observation / مشاهدهٔ مستقیم: چیزی که در متن یا رفتار قابل‌مشاهده وجود دارد.
2. Pattern / الگوی تکرارشونده: مشاهده‌هایی که معیار تکرار مشخص دارند.
3. Hypothesis / فرضیه: تفسیر قابل‌آزمون، نه واقعیت اثبات‌شده.
4. Verified Discovery / کشف تأییدشده: نتیجه‌ای که آزمون و شواهد کافی دارد.

فرایند رشد:
CAPTURE → ANCHOR → LINK → ANALYZE → HYPOTHESIZE → TEST IN RAHM → REVIEW → PROMOTE TO MASTER OR KEEP IN CHILD/QUEUE.
هیچ استنباطی دربارهٔ حالت ذهنی پنهان کاربر نباید به‌عنوان واقعیت قطعی ثبت شود؛ فقط الگوهای مبتنی بر شواهد قابل‌مشاهده.

## 8. بستهٔ قابل‌انتقال به میزبان جدید
درخواست «تا اینجا بسته/آپ معماری بساز» باید نسخهٔ نقطه‌زمانی و بازتولیدپذیر تولید کند که شامل موارد زیر باشد:
- manifest و شناسه/نسخهٔ بسته؛
- سند مرجع مادر و قراردادهای حاکم؛
- نقشهٔ معماری و واژه‌نامه؛
- فهرست اسناد مرجع و پیوندهای canonical؛
- گراف لنگرها/۰.۰ و دفتر رویدادهای ورودی/خروجی؛
- وضعیت گره‌ها، پیوندهای شکسته، موارد تکراری و موارد نامطمئن؛
- صف معماری، شکاف‌ها، آزمون‌ها و شواهد؛
- قواعد زمان‌گذاری و منشأ؛
- Host Adapter و فهرست قابلیت‌های مجاز/غیرمجاز میزبان؛
- دستور import، راستی‌آزمایی checksum/شناسه‌ها، بازیابی و ادامه؛
- گزارش تفاوت نسبت به بستهٔ قبلی؛
- وضعیت جداگانهٔ مخزن، بافر، کتابخانه، حافظهٔ پایدار و Dropbox.
بسته باید مرزهای دسترسی/حریم خصوصی را رعایت کند و فقط داده‌هایی را شامل شود که مجاز و در دسترس‌اند. سند متنی به‌تنهایی اثبات نمی‌کند که یک برنامهٔ اجرایی قابل‌نصب ساخته شده است.

## 9. مقصدها و اثبات
وضعیت هر مقصد مستقل است: Repository، Buffer، Library، Persistent Memory، Dropbox و بستهٔ میزبان.
- WRITE ≠ READ-BACK
- READ-BACK ≠ VALIDATED
- REGISTERED ≠ ARCHITECTURE INTEGRATED
- ARCHITECTURE INTEGRATED ≠ RUNTIME AUTOMATED
- TEST DEFINED ≠ TEST PASSED
- FOUND ≠ RETRIEVED ≠ VALIDATED ≠ REVIVED ≠ VERIFIED ≠ ACTIVE

هیچ مقصدی صرفاً بر اساس موفقیت مقصد دیگر تأیید نمی‌شود. Dropbox در حال حاضر OPEN / WAITING است مگر آزمون اتصال/نوشتن/بازخوانی/بازیابی مدرک جدیدی ارائه کند.

## 10. شکاف‌های پذیرش و آزمون‌ها
- G-01: گراف تاریخی کامل و canonical ۰.۰؛ باز تا تطبیق کل مخزن.
- G-02: Dropbox failover؛ باز تا اتصال و آزمون write/read/recover.
- G-03: اثبات مستقل Buffer/Library/Persistent Memory؛ باز تا مدرک هر مقصد.
- G-04: اجرای خودکار هر ورودی/خروجی در نشست واقعی؛ قرارداد ثبت‌شده اما runtime proof لازم.
- G-05: انتقال واقعی به میزبان دوم؛ باز تا export/import/rebuild test.
- G-06: schema ماشینی رویدادها و گراف؛ باز تا تعریف و اعتبارسنجی خودکار.
- G-07: امنیت، مجوز، حداقل‌سازی داده و سیاست نگهداشت؛ باز تا آزمون اجرایی.
- G-08: جلوگیری از تکرار، نسخه‌گذاری و بازیابی idempotent؛ باز تا آزمون.
- G-09: تحلیل بازهٔ زمانی با منشأ/دادهٔ مفقود؛ باز تا اجرای نمونهٔ واقعی.
- G-10: تولید بستهٔ معماری از یک نقطهٔ زمانی؛ باز تا تولید و import واقعی.

آزمون پذیرش پایه:
T1 ورودی و خروجی قابل‌بازیابی؛ T2 زمان‌های مستقل و منشأدار؛ T3 پیوندهای والد/فرزند؛ T4 بازیابی بازهٔ زمانی؛ T5 گراف تاریخی ۰.۰؛ T6 کشف تکراری/یتیم/ارجاع شکسته؛ T7 ایزوله‌بودن Master؛ T8 انتقال به میزبان دوم؛ T9 اثبات مقصدهای مستقل؛ T10 idempotency و recovery after interruption؛ T11 امنیت و مجوز داده؛ T12 export/import و تطبیق نسخه. هر آزمون باید وضعیت NOT RUN/PASS/FAIL/BLOCKED، شاهد، زمان و اقدام بعدی داشته باشد.

## 11. قواعد وضعیت و توقف
- INCOMPLETE ≠ LOST؛ PENDING ≠ BURIED؛ INTERRUPTED ≠ FAILED.
- هیچ شکافی با صرف ساخت سند بسته نمی‌شود.
- اگر دسترسی به مخزن یا مقصد وجود نداشت، ثبت را انجام‌شده ادعا نکن؛ رکورد قابل‌کپی بساز و مسیر بازیابی ارائه بده.
- اگر زمان پیام کاربر در دسترس نبود، UNKNOWN / UNVERIFIED ثبت شود.
- اگر گراف/محتوا ناقص بود، دامنهٔ واقعی بررسی و محدودیت دقیق گزارش شود.
- کارهای باز به صف معماری با شناسه، منشأ، مقصد، مانع و next action منتقل شوند.

## 12. گردش کار خاک‌برداری
1. بازیابی همهٔ موارد باز و صف‌های پیشین.
2. خواندن گراف Git در شاخهٔ هدف و شمارش فایل‌ها.
3. تطبیق فهرست فایل‌ها با فهرست اسناد و شناسه‌های داخل محتوا.
4. بازخوانی سندهای مادر و نقاط ۰.۰.
5. استخراج گره‌ها/روابط و کشف شکاف‌ها.
6. اتصال موارد قطعی؛ ثبت ابهام‌ها در صف.
7. به‌روزرسانی سند مادر، نمایه، دفتر رفتار، دفتر ۰.۰ و صف.
8. read-back و تطبیق پس از تغییر.
9. اجرای آزمون‌های متناسب.
10. ثبت نتیجهٔ ممیزی و ادامه از اولین شکاف باز؛ هرگز صرفاً گزارش بدون تغییر نده.

## 13. مسیر و وضعیت این اجرای جاری
این سند و رویداد EVT-0046 بخشی از ثبت جاری‌اند. مخزن دارای تعداد زیادی پروندهٔ تاریخی ۰.۰ و رویدادهای مشابه‌نام است؛ شمارش صرف مسیرهای مستقیم کافی نیست. ممیزی جاری باید کل درخت را بررسی کند، سپس فایل‌های مرتبط را بخواند و شاخص شناسه/روابط را تولید کند. تا آن زمان، گراف canonical کامل اعلام نمی‌شود.

## 14. اجرای ممیزی گراف در EVT-0047
- رویداد ورودی: [EVT-0046](../../architecture/BEHAVIOR-TRACE/EVT-0046-USER-REQUEST-GOVERNING-ANCHORING-TIMESTAMP-AND-GRAPH-RECONCILIATION-2026-10-21.md).
- رویداد خروجی: [EVT-0047](../../architecture/BEHAVIOR-TRACE/EVT-0047-ASSISTANT-GOVERNANCE-REFERENCE-AND-GRAPH-INVENTORY-2026-10-21.md).
- موجودی گراف: [C0GIR](./CANONICAL-0.0-GRAPH-INVENTORY-AND-RECONCILIATION-2026-10-21-001.md).
- در بازخوانی محتوایی رویدادها، برخورد شمارهٔ EVT و برخورد Stable ID میان EVT-0003/EVT-0004 مشاهده شد؛ موارد در C0GIR ثبت شده‌اند. تا زمانی که lineage و مالکیت شناسه با شواهد تطبیق نشود، تغییر یا حذف شناسهٔ تاریخی مجاز نیست.
- نسخهٔ 1.0.0 این سند، قرارداد حاکم را تعریف می‌کند؛ اجرای کامل تمام گیت‌ها همچنان وابسته به آزمون و شواهد مقصدی است.

## 15. رویداد خروجی و وضعیت زنده
- رویداد خروجی این نسخه: [EVT-0047](../../architecture/BEHAVIOR-TRACE/EVT-0047-ASSISTANT-GOVERNANCE-REFERENCE-AND-GRAPH-INVENTORY-2026-10-21.md).
- موجودی گراف تازه‌تر: [C0GIR](./CANONICAL-0.0-GRAPH-INVENTORY-AND-RECONCILIATION-2026-10-21-001.md), tree SHA `19058e7d68a540862c618176c4c5e64109c62c0c`.
- وضعیت: ACTIVE / LIVING / GOVERNING؛ در مخزن ثبت و در نمایه/صف/دفتر ۰.۰ پیوند داده شده است. اجرای خودکار در همهٔ نشست‌ها/میزبان‌ها همچنان نیازمند آزمون اجرایی است.

## 16. الحاقیهٔ ممیزی شناسه‌ها و گراف — نسخهٔ 1.0.1
- موجودی جاری C0GIR در tree SHA `19058e7d68a540862c618176c4c5e64109c62c0c) به 653 فایل، 93 مسیر دارای 0.0، 38 مسیر checkpoint، 51 رویداد EVT و 48 سند مرجع مرتبط رسیده است.
- سرآیند و فرادادهٔ 51 رویداد EVT و فراداده/پیوندهای اصلی 48 سند مرجع مرتبط خوانده شده‌اند. استخراج کامل همهٔ رابطه‌های داخلی از تمام پرونده‌های ۰.۰ هنوز باز است.
- G-11: فرادادهٔ ناقص پرونده‌های قدیمی؛ G-12: برخورد شناسه‌ها/شماره‌های EVT؛ G-13: اعتبارسنجی ماشینی پیوندها به‌عنوان شکاف‌های جدید ثبت شدند.
- جزئیات، مسیرها، SHAهای کاندیدای تکرار و یافته‌ها در [C0GIR](./CANONICAL-0.0-GRAPH-INVENTORY-AND-RECONCILIATION-2026-10-21-001.md) ثبت شده‌اند.
- Version history: 1.0.0 تعریف قرارداد حاکم؛ 1.0.1 پیوند EVT-0047، snapshot جدید گراف و شکاف‌های G-11 تا G-13.

## 17. شکاف‌های معماری افزوده‌شده پس از چکش گراف
- **G-11 — فرادادهٔ ناقص legacy:** رکوردهای قدیمی که Stable ID یا Version ندارند باید بدون جعل هویت اصلی، با برچسب ناقص‌بودن فراداده و سیاست مهاجرت نسخه‌دار وارد گراف شوند.
- **G-12 — برخورد شناسه/شمارهٔ رویداد:** برخورد Stable ID و Production ID میان EVT-0003/EVT-0004 و شماره‌های EVT تکرارشده باید با کلید مرکب و lineage شفاف حل شود؛ هیچ فایل تاریخی حذف نشود.
- **G-13 — اعتبارسنجی ماشینی گراف:** ساخت validator برای مسیرهای canonical، لینک‌های شکسته، شناسه‌های والد/فرزند، تکرارهای محتوا و گره‌های یتیم؛ تا زمان اجرای آزمون، این شکاف باز است.
جزئیات و شواهد اولیه در C0GIR v1.0.1 آمده است. این سه شکاف به G-01 تا G-10 اضافه می‌شوند و جایگزین آن‌ها نیستند.

## Version history update
- 1.0.2 — G-11 through G-13 were integrated into this governing reference and the architecture integration queue; the stale EVT-0047 placeholder was replaced with the canonical event link.

## 18. شاهد اجرایی محدود از GitHub Actions — 2026-10-21
- Workflow: Evidence Gate - Independent Execution Test.
- Run ID: `39497698663`; conclusion: `success`; head commit: `1dad17490b47364228d2ad45ee39703dfd573790`.
- Run time from GitHub metadata: started `2026-10-20T21:06:50Z`, completed `2026-10-20T21:07:01Z`.
- Job steps reported success for Stable Retrieval Core consistency test, Independent execution test, creation/commit of durable evidence record and artifact upload.
- Evidence artifact: `evidence/evidence-gate-39497698663.txt`.
- Interpretation boundary: this is real automated evidence for the repository's configured Evidence Gate and its tested stable-retrieval/independent-execution scope. It does **not** prove every user input/output is automatically captured, full 0.0 graph reconciliation, Dropbox, independent Buffer/Library/Persistent Memory, or second-host transfer.
- The workflow creates a new evidence artifact on a successful push. Therefore tree counts are time-bounded snapshots and may change after any repository write.
- Version history: 1.0.3 records this narrow execution proof and the distinction between tested workflow automation and universal interaction capture.

## 19. G-14 — پایداری snapshot در برابر شواهد تولیدشده توسط CI
- **مشاهده:** Evidence Gate در هر push موفق، فایل `evidence/evidence-gate-<run-id>.txt` می‌سازد. در snapshot مشاهده‌شده، 192 فایل evidence gate وجود داشت؛ 15 فایل جدید بین snapshot 653 و 668 اضافه شده بود، و دو فایل دیگر تا snapshot 670 اضافه شدند.
- **اثر:** شمارش کل فایل‌ها با هر commit تغییر می‌کند و اگر فایل‌های تولیدشدهٔ CI با منابع معماری یکی شمرده شوند، مقایسهٔ گراف بین نسخه‌ها ناپایدار می‌شود.
- **قاعدهٔ اصلاحی:** manifest باید دو طبقهٔ جدا داشته باشد: (A) منابع معماری/مرجع/رویداد/۰.۰ و (B) شواهد اجرای تولیدشده. شواهد B حفظ و پیوند داده شوند اما در شمارش گره‌های منبع معماری با A مخلوط نشوند. هر snapshot باید tree SHA، زمان، scope و exclusions را ثبت کند.
- **Status:** OPEN / PARTIAL؛ قاعده تعریف شد، اما فیلتر/اعتبارسنجی ماشینی manifest هنوز اجرا نشده است.
- Version history: 1.0.4 adds G-14 for reproducible graph snapshots and CI-generated evidence separation.



## 35. گسترش حاکمیت گراف تاریخی و زمان‌گذاری UTC — 2026-10-21
- Addendum reference: [H0G-RDR — تطبیق گراف تاریخی ۰.۰ و دفتر تکرارها](./HISTORICAL-0.0-GRAPH-RECONCILIATION-AND-DEDUPLICATION-REGISTER-2026-10-21-001.md).
- Input event: [EVT-0048](../../architecture/BEHAVIOR-TRACE/EVT-0048-USER-REQUEST-FULL-HISTORICAL-0.0-GRAPH-RECONCILIATION-2026-10-21.md).
- Audit script: [audit_historical_0_0_graph.py](../../../scripts/audit_historical_0_0_graph.py).
- Workflow: [Living Architecture Audit](../../../.github/workflows/living-architecture-audit.yml); run [39501699736](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39501699736) succeeded and uploaded artifact `living-architecture-audit-39501699736`.
- Latest observed tree snapshot UTC 2026-10-20T21:38:13.394Z: 682 files; 95 paths containing 0.0; 38 checkpoint paths; 52 EVT files; 85 paths under Reference Documents; 201 generated Evidence Gate files; `truncated=false`. This is a time-bounded snapshot; generated evidence and new registrations change counts.
- The workflow's earlier audit snapshot was 678 files / 93 0.0 paths / 51 EVT / 84 reference-document paths / 199 Evidence Gate files. Both snapshots are retained as dated observations; neither overwrites the other.
- New active gaps: G-15 canonical alias/lineage manifest; G-16 semantic review of event/reference contents; G-17 Dropbox write/read/recovery; G-18 independent Buffer/Library/Persistent Memory proof; G-19 second-host transfer; G-20 runtime-wide interaction capture proof. See H0G-RDR and the Integration Queue.
- Deduplication rule: canonicalize logically by alias/lineage; preserve historical files. The audit script reports exact-content groups and ID collisions; a successful workflow means the scan ran, not that every collision is resolved.
- Time rule: all new processing/registration/read-back timestamps use UTC as the primary source. Tehran time is optional derived display only. User-message time stays UNKNOWN / UNVERIFIED when no trusted source exists.
- Status: ACTIVE / LIVING; repository registration is being integrated. Full semantic graph reconciliation remains OPEN / PARTIAL.


## 36. خروجی و شواهد ممیزی گراف — EVT-0049
- Output event: [EVT-0049](../../architecture/BEHAVIOR-TRACE/EVT-0049-ASSISTANT-EXECUTION-AND-RECONCILIATION-2026-10-21.md); input [EVT-0048](../../architecture/BEHAVIOR-TRACE/EVT-0048-USER-REQUEST-FULL-HISTORICAL-0.0-GRAPH-RECONCILIATION-2026-10-21.md).
- Canonical reconciliation: [H0G-RDR](./HISTORICAL-0.0-GRAPH-RECONCILIATION-AND-DEDUPLICATION-REGISTER-2026-10-21-001.md).
- Workflow run [39502190776](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39502190776) SUCCESS; artifact `living-architecture-audit-39502190776`, digest `sha256:0bff6ba4b290be28a172dce5682ac7396d52013a62d6b61d2ccd93a52df45dd9`.
- Last observed pre-EVT-0049 snapshot UTC 2026-10-20T21:40:47.065Z: 689 files, 95 0.0 paths, 38 checkpoint paths, 52 EVT paths, 85 reference-document paths, 208 generated Evidence Gate artifacts; tree complete.
- Eight core repository files were fetched after integration writes and passed targeted checks for expected IDs, versions, links and G-15/G-20 entries.
- Exact duplicate/collision/broken-link counts are not claimed because the artifact's full report has not been directly inspected here. Full semantic review remains OPEN / PARTIAL.
- UTC is primary for new registration, execution and read-back; local time is derived display only; user-message time remains UNKNOWN / UNVERIFIED when unsourced.


## 37. سند مرجع مادر تجمیعی و نقطهٔ ادامهٔ canonical
- **Current continuation master:** [CCCMR-2026-10-21-001](./CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md), Version 1.0.0, Status ACTIVE / LIVING / CANONICAL CONTINUATION BASE.
- **Input event:** [EVT-0050](../../architecture/BEHAVIOR-TRACE/EVT-0050-USER-REQUEST-CONSOLIDATED-LIVING-MASTER-CONTINUATION-2026-10-21.md).
- **Rule:** For the next continuation, read CCCMR first, then the latest EVT-0051, latest graph audit artifact, and only then continue G-01/G-12/G-13/G-15/G-16. Do not restart completed checks without reason or claim unresolved work closed.
- UTC is the primary timestamp; Asia/Tehran is derived display only; user-message time is UNKNOWN / UNVERIFIED when unsourced.


## 38. خروجی سند مادر تجمیعی — EVT-0051
- Current canonical continuation: [CCCMR-2026-10-21-001](./CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md), Version 1.0.1.
- Input: [EVT-0050](../../architecture/BEHAVIOR-TRACE/EVT-0050-USER-REQUEST-CONSOLIDATED-LIVING-MASTER-CONTINUATION-2026-10-21.md).
- Output and verification record: [EVT-0051](../../architecture/BEHAVIOR-TRACE/EVT-0051-ASSISTANT-CONSOLIDATED-MASTER-CREATION-AND-READBACK-2026-10-21.md).
- The consolidated master is the current continuation entry point; the historic graph remains OPEN / PARTIAL.
