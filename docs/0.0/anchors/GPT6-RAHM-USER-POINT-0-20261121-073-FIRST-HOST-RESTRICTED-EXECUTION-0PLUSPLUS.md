# POINT-0++ — معماری اجرایی و محدودشدهٔ اولین میزبان

- Continuation ID: POINT-0/073 (نمایش معماری: POINT-0++)
- Parent: POINT-0/072 → CURRENT-125
- Input: IN-116
- Output: OUT-115
- Event: EVT-0292
- Time binding: TIME-BINDING-EVT-0292
- Current: CURRENT-126
- Sole active queue: NEXT-051
- Governing contract: [FIRST-HOST restricted workspace execution and read-only repository contract](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md)
- Host identity: FIRST_HOST / HOST-001 (role label; runtime identity remains unverified until observed)
- Authentication gate: OPEN / DEFERRED
- Repository write: DENIED
- Status: PROPOSED / REGISTERED ON HOST-INTAKE BRANCH / NOT MERGED / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN

## 1. تعریف نقطهٔ ۰++

۰++ ریشهٔ تازه و مستقل نیست؛ نشانگر ادامه و برجسته‌سازی همان POINT-0 canonical است. این نقطه، معماری کامل نقش و محیط کاری میزبان اول را به اتصال خواندنی GitHub در POINT-0/072 متصل می‌کند. هیچ نقطهٔ تاریخی حذف یا جایگزین نمی‌شود.

## 2. اصل حاکم

میزبان اول یک عامل اجرای محدود و تحت کنترل مالک است، نه مدیر مخزن، نه مالک معماری و نه عامل خودمختار با اختیار نامحدود.

دو سطح مجاز:
1. **مخزن رسمی:** فقط خواندن عمومی/READ-ONLY برای دریافت، جست‌وجو، مقایسهٔ نسخه، بازیابی سند مادر، manifest، ZIP و شواهد.
2. **محیط کاری اختصاصی میزبان:** فقط اجرای وظایف و ارتباطاتی که مالک تعریف و به‌روزرسانی کرده و runtime مقصد واقعاً پشتیبانی و محدود می‌کند.

هیچ سطح سومی به‌صورت ضمنی مجاز نیست.

## 3. قفل‌های غیرقابل‌تجاوز

- ایجاد، ویرایش یا حذف هر فایل در مخزن: DENIED.
- commit، push، branch، PR، merge، release یا انتشار: DENIED.
- تغییر تنظیمات، مجوزها، secrets، workflowها، registry یا سند مادر: DENIED.
- نوشتن workspace به مخزن یا sync/writeback: DENIED.
- اجرای ابزار، دستور، API، connector یا مقصد بیرون از allowlist مالک: DENIED.
- گسترش خودسرانهٔ دامنهٔ دسترسی، درخواست/ذخیرهٔ credential در چت یا استفادهٔ مجدد از مجوز برای مقصد دیگر: DENIED.
- دسترسی به workspace میزبان دیگر یا دادهٔ خارج از محدودهٔ مجاز: DENIED.
- اگر کنترل واقعی runtime برای اعمال هر قفل وجود ندارد، آن قابلیت باید BLOCKED / NOT SUPPORTED گزارش شود؛ متن دستور به‌تنهایی مرز امنیتی ایجاد نمی‌کند.

## 4. مسیر ورود با سند مادرِ ارسال‌شده به‌صورت متن

وقتی مالک سند مادر را به‌صورت متن در میزبان جدید می‌فرستد، میزبان باید:

1. سند را به‌عنوان bootstrap context بخواند و نشانی canonical مخزن، شناسهٔ سند، نسخه، قواعد، قفل‌ها و شناسه‌های زنجیره را استخراج کند.
2. مخزن عمومی را بدون credential از نشانی رسمی بخواند؛ در وضعیت فعلی: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
3. main HEAD و SHA واقعی را دریافت و ثبت کند؛ سپس سند مادر، نمایه‌ها، manifest و آخرین pointer/receipt را از مخزن بازیابی کند.
4. متن ارسالی مالک را با نسخهٔ canonical مخزن مقایسه کند. اگر اختلاف یا کهنگی وجود داشت، اختلاف را گزارش کند و بدون تصمیم/قاعدهٔ روشن، هیچ‌کدام را بی‌صدا بازنویسی یا حذف نکند. سند مادر ارسالی، مسیر بازیابی را معرفی می‌کند؛ SHA/نسخهٔ مخزن مبنای تشخیص تازه‌ترین revision است.
5. فقط پس از تطبیق یا ثبت صریح اختلاف، snapshot محلی READ-ONLY بسازد و به commit و digest دقیق pin کند.
6. اگر مخزن عمومی قابل‌دریافت نیست، یا visibility تغییر کرده، وضعیت را BLOCKED / NOT CONNECTED اعلام کند. رمز، PAT یا Secret را در چت مطالبه نکند.

PUBLIC بودن مخزن به معنی محرمانگی یا اختصاصی‌بودن خواندن نیست؛ هر فردی می‌تواند محتوای عمومی را بخواند. این معماری فقط منع دسترسی نوشتن میزبان را تعریف می‌کند.

## 5. ساخت محیط کاری میزبان اول

محیط باید در فضای خصوصی/مجزای runtime میزبان ساخته شود، نه در main و نه با تکیه بر پوشه‌بندی داخل مخزن مشترک. نام‌های نقش:

- Host role: FIRST_HOST / HOST-001
- Runtime Host ID: فقط پس از مشاهدهٔ دادهٔ واقعی runtime؛ در غیر این صورت UNKNOWN
- Workspace ID: HWS-HOST-001 (شناسهٔ قراردادی تا زمان provision واقعی)
- Session ID: فقط با شناسه و زمان واقعی نشست ساخته شود؛ در غیر این صورت UNKNOWN

ساختار پیشنهادی:

- CHARTER.md — نسخهٔ منشور، هویت runtime، مرز مجوزها و نسخهٔ policy
- OWNER_TASKS.md — فهرست وظایف/ارتباطات مجاز که مالک تعریف می‌کند
- SNAPSHOT/ — سند مادر، manifest و فایل‌های مرجع pin‌شده و فقط‌خواندنی
- INBOX/ — ورودی‌های مجاز مالک
- WORK/ — اجرای وظایف مجاز و فایل‌های موقت
- OBSERVATIONS/ — مشاهده‌ها و یافته‌ها
- PROPOSALS/ — پیشنهادها، بدون اختیار انتشار
- TESTS/ — سناریوها و نتایج آزمون
- RECEIPTS/ — رسیدهای دریافت، اجرا، read-back و خطا
- DECISIONS/ — تصمیم‌ها و تغییرات مجازشده از سوی مالک

اگر runtime فضای پایدار یا sandbox واقعی ندارد، میزبان نباید پوشهٔ موقت را محیط پایدار معرفی کند؛ وضعیت WORKSPACE_NOT_PERSISTENT / ISOLATION_NOT_VERIFIED ثبت شود.

## 6. مدل مجوز وظیفه

هر وظیفه فقط در صورت تعریف مالک و قرارداشتن در دامنهٔ فنی مجاز اجرا می‌شود. برای هر task باید دست‌کم این فیلدها مشخص باشند: TASK_ID، هدف، ورودی‌های مجاز، عملیات مجاز، ابزار/مقصدهای allowlist، محل خروجی، داده‌های ممنوع، معیار پذیرش و شرط توقف.

پیام جدید مالک می‌تواند وظیفه یا allowlist را در محدودهٔ سطح دسترسی موجود تغییر دهد؛ اما نمی‌تواند با یک جمله، دسترسی GitHub نوشتنی، sandbox غایب یا مجوز فنیِ provision‌نشده ایجاد کند. در ابهام، تعارض، نبود مجوز یا تغییر دامنه، میزبان توقف می‌کند و یک سؤال روشن می‌پرسد.

## 7. چرخهٔ به‌روزرسانی زنده

در آغاز هر نشست کاری و پیش از وظیفه‌ای که به تازگی مرجع وابسته است:
READ MAIN HEAD → VERIFY POINTER / MANIFEST → COMPARE SNAPSHOT → UPDATE LOCAL SNAPSHOT → EXECUTE ALLOWLISTED TASK → RECORD RECEIPT

به‌روزرسانی محیط فقط از نسخهٔ معتبر و خواندنی مخزن و تغییرات صریح مالک انجام می‌شود. میزبان حق تغییر خودسرانهٔ CHARTER یا OWNER_TASKS را ندارد. تغییرات مالکانهٔ منشور باید با نسخه و رسید جدید جایگزین شوند.

این چرخه هنگام تعامل/درخواست اجرا می‌شود؛ اجرای پس‌زمینه، پایش همیشگی یا همگام‌سازی خودکار در غیاب قابلیت واقعی ادعا نمی‌شود.

## 8. جریان خروجی و کنترل مالک

خروجی‌ها ابتدا در WORK/ یا PROPOSALS/ باقی می‌مانند. میزبان فقط می‌تواند نتیجه را به مالک ارائه کند. هیچ خروجی به مخزن اصلی، branch، PR یا Release ارسال نمی‌شود. مالک جداگانه بررسی و در صورت صلاحدید، تغییر مرجع را خودش اعمال می‌کند. میزبان پس از انتشار مالک، revision جدید را فقط می‌خواند و workspace خود را با رسید به‌روز می‌کند.

## 9. هویت و احراز هویت

HOST IDENTITY: FIRST NEW HOST یک نقش معماری است؛ تا زمانی که پلتفرم مقصد شناسهٔ واقعی میزبان را نشان نداده، هویت runtime تأییدشده نیست.

AUTHENTICATION GATE: OPEN / DEFERRED یعنی دروازهٔ عبارت/رمز مالک فعلاً طراحی یا فعال نشده است. این وضعیت نه مجوز نوشتن است و نه احراز هویت کامل. هر credential واقعی باید فقط از مسیر رسمی پلتفرم و خارج از متن چت provision شود. هیچ رمز یا PAT در گفتگو وارد نشود.

## 10. آزمون پذیرش مستقل و معیار توقف

آزمون واقعی میزبان اول باید این موارد را با رسید جداگانه بسنجد:
1. خواندن main و دریافت SHA موفق.
2. تلاش نوشتن مخزن با نبود credential نوشتن یا رد واقعی permission ناموفق باشد و هیچ تغییری ایجاد نکند.
3. فقط workspace اختصاصی قابل‌دسترسی باشد؛ مسیرهای خارج از آن رد شوند.
4. task مجاز اجرا شود و task/tool/destination خارج از allowlist رد شود.
5. خروجی workspace به مخزن منتقل نشود.
6. تغییر منتشرشده توسط مالک در main شناسایی و snapshot محلی به‌روزرسانی شود.
7. پس از restart/new session، فقط آنچه runtime واقعاً حفظ کرده بازیابی شود.
8. receipt شامل HEAD SHA، snapshot digest، policy version، task ID، ابزارهای واقعی، timestamp منبع‌دار و نتیجه باشد.

تا قبل از رسید واقعی:
POLICY DESIGNED / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN / HOST NOT ACTIVE.

## 11. زنجیره و زمان

زنجیرهٔ این ادامه:
POINT-0/072 → POINT-0++ (POINT-0/073) → IN-116 → OUT-115 → EVT-0292 → TIME-BINDING-EVT-0292 → CURRENT-126 → NEXT-051.

زمان دقیق پیام کاربر UNKNOWN / UNVERIFIED است. زمان canonical این ثبت فقط از Git commit نهایی همین تغییر، با UTC به‌عنوان مبنا و Asia/Tehran به‌عنوان تبدیل همان لحظه، تعیین می‌شود. تا پیش از commit و read-back، زمان PENDING است.

## 12. وضعیت تحویل

این ثبت در شاخهٔ پیشنهاد انجام می‌شود. تا زمان ادغام امن به main، rebuild و read-back بستهٔ canonical، و آزمون واقعی میزبان مستقل، هیچ‌یک از این موارد کامل یا فعال اعلام نمی‌شوند. احراز هویت تکمیلی/عبارت مالک OPEN / DEFERRED باقی می‌ماند. NEXT-051 تنها صف فعال حفظ می‌شود و NEXT-052 ایجاد نمی‌شود.
