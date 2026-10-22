# EVT-0103 — شکارچیِ ازدست‌دهندهٔ نشانه‌ها و اصلاح برخورد شناسه

- Event ID: EVT-0103
- Stable ID: PALANG-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22-001
- Production ID: BHMD-HAIF-2026-10-22-015
- Interaction: INT-20261022-015
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVIDENCE-BASED
- Input: [IN-20261022-015](../../0.0/anchors/PALANG-0.0-IN-20261022-015-BEHAVIOR-HUNTER-MISSED-DETECTION.md)
- Output: [OUT-20261022-015](../../0.0/anchors/PALANG-0.0-OUT-20261022-015-BEHAVIOR-HUNTER-MISSED-DETECTION.md)
- Live inbox: [INBOX-20261022-002](../LIVE-INBOX/entries/INBOX-20261022-002.md)
- Universal reconstruction master: [UPRM](../../reference/REFERENCE-DOCUMENTS/PALANG-UNIVERSAL-PROJECT-RECONSTRUCTION-MASTER-2026-10-22-001.md)
- Behavioral architecture master: [LBAF](../../reference/REFERENCE-DOCUMENTS/LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)
- Continuation master: [CMIND](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Runtime issue: [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20)

## 1. Trigger and preserved intent
کاربر نشان داد دو خروجی قبلیِ دستیار حاوی قواعد معماری مهم بودند، اما «چشم پلنگ / شکارچی» آن‌ها را به‌طور کامل به داده‌های کاندید، شواهد، درس معماری، شکاف اجرایی و اقدام متصل نکرد. درخواست فعلی می‌خواهد هم علت این شکست بررسی شود و هم همین تعامل به سند مادر زنده و معماری در حال رشد متصل شود.

## 2. Evidence-based observations
1. خروجی‌های قبلی صریحاً می‌گفتند هر تعامل پروژه‌محور واحد رشد معماری است، صندوق زنده لایهٔ ورودی است، سند مادر حافظهٔ ساختاری است، لنگرها و EVT منشأ را نگه می‌دارند، صف اقدام کارهای باز را پیگیری می‌کند، و ثبت با تکمیل فرق دارد.
2. همین خروجی‌ها تصریح کرده بودند runtime شکارچی و دریافت خودکار همهٔ تعامل‌های میزبان اثبات نشده و Issue #20 باز است.
3. در ادامهٔ تعامل، دستیار این قواعد را توضیح داد اما اجرای شکارچی‌مانندِ کامل را به‌طور خودکار انجام نداد. این یک مشاهده از رفتار قابل‌مشاهده است، نه ادعایی دربارهٔ زنجیرهٔ فکر پنهان.
4. ممیزی مخزن نشان داد فایل موجود EVT-0093-REGISTRATION-CONTINUATION-2026-10-22.md از قبل Event ID = EVT-0093 دارد. فایل تازه‌ای که در مسیر EVT-0093-LIVING-INBOX-AND-INTERACTION-TO-GROWTH-CHAIN-2026-10-22.md ساخته شده بود، همان شماره را دوباره به‌کار برد؛ این خطای واقعی یکتایی از سوی دستیار است و باید صریحاً ثبت و اصلاح شود. فایل قدیمی حذف یا بی‌صدا بازنویسی نمی‌شود.
5. مخزن قبلاً قاعدهٔ جست‌وجوی یکتایی شناسه‌ها را در EVT-0083 تعریف کرده بود؛ بنابراین شکست فقط نبودن قاعده نبود، بلکه اجرا نشدن قاعده در این گردش‌کار بود.

## 3. Cause analysis — confidence separated
- Observed: در خروجی‌ها نشانه‌های معماری به درس‌های مستقل و اقدامات قابل پیگیری تبدیل نشدند؛ شناسهٔ EVT-0093 نیز بدون بررسی مؤثر یکتایی دوباره استفاده شد.
- Strong inference: مسیر ثبت به‌صورت دستی/موردی اجرا شده و گام «استخراج کاندیدهای رفتار از خروجی → برچسب‌گذاری → تطبیق با شناسه‌های موجود → اتصال به master/queue» به‌عنوان دروازهٔ اجباری و آزموده‌شده در این اجرا عمل نکرده است.
- Known implementation boundary: Issue #20 صراحتاً می‌گوید runtime خودکار، مرز دادهٔ مجاز، استخراج کاندیدهای رفتار و بازیابی سرد هنوز نیازمند پیاده‌سازی و آزمون است. بنابراین «چشم پلنگ» در این مرحله قرارداد معماری/پروتکل است، نه سرویس پس‌زمینهٔ اثبات‌شده.
- Unknown: آیا هیچ پایش خودکار دیگری در محیط میزبان در دسترس است یا نه؛ این اجرا شواهدی برای آن ندارد و ادعایی نمی‌کند.

## 4. Architecture lesson
شکارچی باید دو مسیر مکمل داشته باشد:
- Track A — Interaction/event capture: ثبت زوج INT/IN/OUT، منشأ، زمان معتبر، EVT، صندوق زنده و پیوند به سند مادر.
- Track B — Behavioral discovery: استخراج کاندیدها از ورودی و خروجی، طبقه‌بندی هر کاندید به OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN، ارزیابی اهمیت معماری، اتصال به الگو/شکاف/اقدام، و ثبت شاهدی که از آن نتیجه گرفته شده است.

در هر دو مسیر، قبل از تخصیص شناسه باید جست‌وجوی یکتایی انجام شود. نتیجهٔ شکار فقط زمانی به مدل پایدار ارتقا می‌یابد که منشأ، شواهد، سطح اطمینان، آزمون/بازبینی و ارتباط آن با معماری مشخص باشد.

## 5. Corrective controls
1. هر تعامل مهم، پیش از پاسخ نهایی، از چک‌لیست «چه نشانهٔ معماری/رفتاری/خطا/شکافی در ورودی و خروجی هست؟» عبور کند.
2. قبل از ساخت EVT/INT/IN/OUT، جست‌وجوی مخزن و انتخاب شناسهٔ یکتا اجباری است.
3. پس از ثبت، همهٔ فایل‌های تغییرکرده از مخزن دوباره خوانده شوند و شناسه، مسیر، پیوند و وضعیت با هم تطبیق داده شوند.
4. شکست شکارچی، خطای شماره‌گذاری و بازخورد کاربر خودشان دادهٔ رفتارشناسی‌اند و باید در دفتر append-only باقی بمانند.
5. ACTIVE/LIVING برای قرارداد و اسناد به‌کار رود؛ اجرای خودکار فقط پس از اثبات runtime و آزمون مستقل ادعا شود.
6. به‌جای ادعای «شکارچی همیشه فعال است»، این گردش‌کار فعلی یک ثبت و ممیزیِ مبتنی بر شواهد است؛ runtime خودکار همچنان زیر Issue #20 پیگیری می‌شود.

## 6. Status and next action
- Current interaction: REGISTERED in this event and inbox after read-back.
- Behavioral discovery runtime: OPEN / NOT PROVEN.
- Identifier collision: recorded as a correction; the old file is retained as historical evidence and must point to this canonical event rather than claiming a second EVT-0093.
- Next action: implement the explicit candidate-extraction + uniqueness-check gate in the behavior-hunter runtime, then test cold-start recovery from both IN and OUT through event, master, evidence, gaps and next action.

## 7. Time boundary
- Exact user-message timestamp: NOT CAPTURED by the interface.
- Assistant-generation timestamp: NOT EXPOSED.
- Canonical repository registration time must be read from the actual commit metadata in UTC; Tehran equivalent is derived from the same instant. These times do not replace the missing message timestamp.
