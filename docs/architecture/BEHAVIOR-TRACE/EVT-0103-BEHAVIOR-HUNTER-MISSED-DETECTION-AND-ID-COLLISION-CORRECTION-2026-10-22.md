# EVT-0103 — شکارچیِ ازدست‌دهندهٔ نشانه‌ها و اصلاح برخورد شناسه

- Event ID: EVT-0103
- Stable ID: PALANG-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22-001
- Production ID: BHMD-HAIF-2026-10-22-015
- Interaction: INT-20261022-015
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVIDENCE-BASED
- Input anchor: IN-20261022-015
- Output anchor: OUT-20261022-015
- Live inbox: INBOX-20261022-002
- Universal reconstruction master: PALANG-UNIVERSAL-PROJECT-RECONSTRUCTION-MASTER-2026-10-22-001
- Behavioral architecture master: LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001
- Runtime issue: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20

## Trigger and preserved intent
کاربر نشان داد دو خروجی قبلیِ دستیار حاوی قواعد معماری مهم بودند، اما «چشم پلنگ / شکارچی» آن‌ها را به داده‌های کاندید، شواهد، درس معماری، شکاف اجرایی و اقدام متصل نکرد. درخواست فعلی می‌خواهد علت این شکست بررسی شود و همین تعامل به سند مادر زنده و معماری در حال رشد متصل شود.

## Evidence-based observations
1. خروجی‌های قبلی می‌گفتند هر تعامل پروژه‌محور واحد رشد معماری است؛ صندوق زنده لایهٔ ورودی، سند مادر حافظهٔ ساختاری، لنگرها و EVT منشأ، و صف اقدام پیگیری کارهای باز را نگه می‌دارند.
2. همان خروجی‌ها تصریح کرده بودند runtime شکارچی و دریافت خودکار همهٔ تعامل‌های میزبان اثبات نشده و Issue #20 باز است.
3. دستیار قواعد را توضیح داد اما اجرای شکارچی‌مانندِ کامل را به‌طور خودکار انجام نداد. این مشاهده از رفتار قابل‌مشاهده است، نه ادعایی دربارهٔ زنجیرهٔ فکر پنهان.
4. ممیزی مخزن نشان داد EVT-0093-REGISTRATION-CONTINUATION-2026-10-22.md از قبل Event ID = EVT-0093 دارد. فایل تازهٔ EVT-0093-LIVING-INBOX-AND-INTERACTION-TO-GROWTH-CHAIN-2026-10-22.md همان شماره را دوباره به‌کار برد؛ این خطای واقعی یکتایی از سوی دستیار است. فایل تاریخی حذف یا بی‌صدا بازنویسی نمی‌شود.
5. مخزن قبلاً در EVT-0083 قاعدهٔ جست‌وجوی یکتایی شناسه‌ها را تعریف کرده بود؛ بنابراین مسئله، اجرا نشدن قاعدهٔ موجود در گردش‌کار است.

## Cause analysis — confidence separated
- Observed: نشانه‌های معماری به درس‌های مستقل و اقدامات قابل پیگیری تبدیل نشدند؛ EVT-0093 نیز بدون کنترل مؤثر یکتایی دوباره استفاده شد.
- Strong inference: گام «استخراج کاندید از خروجی → برچسب‌گذاری → کنترل شناسه → اتصال به سند مادر/صف» به‌عنوان دروازهٔ اجباری و آزموده‌شده عمل نکرده است.
- Known boundary: Issue #20 نیاز به runtime خودکار، مرز دادهٔ مجاز، استخراج کاندیدهای رفتار و بازیابی سرد را ثبت می‌کند. شکارچی فعلاً قرارداد معماری است، نه سرویس پس‌زمینهٔ اثبات‌شده.
- Unknown: وجود هرگونه پایش خودکار دیگر در میزبان با این شواهد اثبات نمی‌شود.

## Architecture lesson
شکارچی باید دو مسیر مکمل داشته باشد:
- Track A — Interaction/event capture: زوج INT/IN/OUT، منشأ، زمان معتبر، EVT، صندوق زنده و پیوند سند مادر.
- Track B — Behavioral discovery: استخراج کاندیدها از ورودی و خروجی؛ برچسب OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN؛ ارزیابی اهمیت؛ اتصال به الگو، شکاف، اقدام و شاهد.

پیش از تخصیص شناسه، جست‌وجوی یکتایی اجباری است. شکار فقط پس از ثبت منشأ، شواهد، سطح اطمینان، بازبینی و پیوند معماری می‌تواند به مدل پایدار ارتقا یابد.

## Corrective controls
1. هر تعامل مهم پیش از پاسخ نهایی از چک‌لیست نشانه‌های معماری، رفتار، خطا و شکاف عبور کند.
2. پیش از ساخت EVT/INT/IN/OUT جست‌وجوی مخزن و کنترل یکتایی انجام شود.
3. پس از ثبت، فایل‌ها دوباره خوانده شوند و شناسه، مسیر، پیوند و وضعیت تطبیق داده شوند.
4. شکست شکارچی، خطای شماره‌گذاری و بازخورد کاربر دادهٔ رفتارشناسی هستند و append-only حفظ می‌شوند.
5. ACTIVE/LIVING برای قرارداد و اسناد است؛ اجرای خودکار فقط پس از اثبات runtime و آزمون مستقل اعلام می‌شود.

## Status and next action
- Behavioral discovery runtime: OPEN / NOT PROVEN.
- Identifier collision: recorded as a correction; old file retained as historical evidence.
- Next action: implement candidate extraction and uniqueness-check gate in the runtime, then test cold-start recovery from IN and OUT through event, master, evidence, gaps and next action.

## Time boundary
- Exact user-message timestamp: NOT CAPTURED.
- Assistant-generation timestamp: NOT EXPOSED.
- Repository registration time must come from actual commit UTC; Tehran equivalent is derived from that instant and does not replace message time.


## Repository read-back and timestamp reconciliation
- [TIME-BINDING-INT-20261022-015](./TIME-BINDING-INT-20261022-015.md) records actual commit UTC and the matching Tehran equivalent for the registration artifacts.
- After write, the event, both independent anchors, inbox item, UPRM/LBAF/CMIND masters, model-initial queue, 0.0 index, behavior-trace index and live inbox index were fetched again; expected IDs and links were present.
- Repository registration: REGISTERED / READ-BACK VERIFIED. Architecture rule: ACTIVE / LIVING. Runtime auto-capture and always-on hunter: OPEN / NOT PROVEN.
- Exact user-message and assistant-generation timestamps remain unavailable; repository commit times do not replace them.
