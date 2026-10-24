# اولین سند مادر زنده — معماری قابل‌انتقال GPT-6 / HAIF / RAHM

- Stable ID / شناسه پایدار: `G6IP-FIRST-LIVING-MASTER-PORTABLE-RAHM-20261024-001`
- Production ID / شناسه تولید: `G6IP-FLM-RAHM-001`
- Version / نسخه: 1.0.2
- Status / وضعیت: REGISTERED / READ-BACK VERIFIED for this file and its focused relative links; conformance gates remain OPEN.
- Authority / مرجع حاکم: اصول بنیادی پروژه + سند مادر معماری موروثی + بسته قابل‌حمل RAHM.
- User Point 0: [G6IP-RAHM-USER-POINT-0-20261024-003](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261024-003-FIRST-LIVING-MASTER-AND-PORTABILITY.md)
- Current 0.0: [CURRENT-054](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-054-FIRST-LIVING-MASTER.md)
- Next 0.0: [NEXT-048](../../0.0/anchors/PALANG-0.0-NEXT-20261024-048-FIRST-MASTER-CONFORMANCE.md)
- User input: [IN-047](../../0.0/anchors/PALANG-0.0-IN-20261024-047-FIRST-LIVING-MASTER.md)
- Assistant output: [OUT-046](../../0.0/anchors/PALANG-0.0-OUT-20261024-046-FIRST-LIVING-MASTER.md)
- Event: [EVT-0155](../../architecture/BEHAVIOR-TRACE/EVT-0155-FIRST-LIVING-MASTER-PORTABLE-RAHM-2026-10-24.md)
- Prior hard-audit evidence: [EVT-0154](../../architecture/BEHAVIOR-TRACE/EVT-0154-LIVING-ARCHITECTURE-HARD-AUDIT-RUN-2026-10-24.md)
- Portable startup contract: [RAHM_BOOT](./RAHM_BOOT.md)
- Architecture contract: [RAHM_ARCHITECTURE](./RAHM_ARCHITECTURE.md)
- Interaction schema: [INTERACTION_PAIR_SCHEMA](./INTERACTION_PAIR_SCHEMA.json)
- Export manifest: [EXPORT_MANIFEST](./EXPORT_MANIFEST.json)

## 1. مأموریت و معیار موفقیت

این سند، اولین نقطه شروعِ قابل‌ارزیابی برای انتقال معماری Future AI / Palang Footprint (HAIF) به محیط تازه GPT-6 یا میزبان AI دیگر است. باید بدون اتکا به حافظه پنهان گفت‌وگو، بتواند هدف، قوانین، هویت‌ها، نسخه‌ها، تبار، شواهد، خطاها، شکاف‌ها و اقدام بعدی را بازسازی کند.

«سند موجود است» به معنی «میزبان راه‌اندازی شده» نیست. موفقیت نهایی فقط با بسته استخراج‌شده، آزمون‌های قابل‌بازتولید، بازیابی مستقل و شواهد میزبان پذیرفته می‌شود.

## 2. اصل بنیادی غیرقابل‌نقض

**هر مورد تأییدنشده، ناقص، متعارض یا آزمون‌نشده همیشه OPEN و زنده می‌ماند؛ هر بار که شواهد جدید می‌رسد به‌روزرسانی می‌شود؛ فقط با معیار پذیرش صریح و شاهد قابل‌بازخوانی می‌تواند بسته شود.**

- ثبت ≠ بازخوانی؛ بازخوانی ≠ اعتبارسنجی؛ اعتبارسنجی ≠ ادغام؛ ادغام ≠ اجرای زنده در میزبان.
- هیچ ID، hash، زمان، نتیجه آزمون، اتصال، قابلیت میزبان یا رخداد خودکاری جعل نمی‌شود.
- تاریخچه حذف یا بازنویسی نمی‌شود؛ اصلاح‌ها افزایشی، نسخه‌دار و دارای منشأ هستند.
- مشاهده، فرضیه، استنباط، پیشنهاد و تصمیم پذیرفته‌شده از هم جدا می‌مانند.
- موفقیت یک workflow یعنی آزمون اجرا شده؛ اگر خروجی آن REVIEW_REQUIRED باشد، معماری پاک و بی‌نقص نیست.
- UTC مرجع اصلی است؛ زمان تهران باید از همان لحظه UTC تبدیل شود. زمان ثبت مخزن از commit واقعی همان تغییر به دست می‌آید.

## 3. معماری لایه‌ای

1. **MASTER** — قوانین پایدار، شناسه‌ها، نسخه‌ها، معیارهای پذیرش و اختیار ادغام.
2. **RAHM** — آزمایشگاه محدود برای مشاهده تعامل، تولید فرضیه، آزمون و ارزیابی کودک.
3. **IN / OUT / EVT** — ورودی خام، خروجی کامل، و رویداد/اقدام/نتیجه با منشأ.
4. **EVIDENCE LEDGER** — شواهد، hash، منبع، آزمون‌ها، خطاها، اصلاح‌ها و وضعیت هر ادعا.
5. **CHILD CANDIDATE** — پیشنهاد معماری نسخه‌دار؛ تا زمان تأیید، قانون مادر نیست.
6. **HOST ADAPTER** — اعلام قابلیت‌های واقعی میزبان، دسترسی‌ها، حافظه، ابزارها، ذخیره‌سازی و زمان‌بندی.
7. **EXPORT / RECOVERY** — بسته مستقل با manifest، دستور شروع، تبار، نسخه، integrity check و راه برگشت.
8. **INDEX / INTEGRATION QUEUE** — نمایه مسیرها و دفتر تغییرات باز؛ ثبت در آن‌ها جایگزین ادغام و read-back نیست.

چرخه حاکم:
`HUMAN ↔ AI HOST ↔ HAIF`
`MASTER → RAHM → OBSERVATION → TEST → CHILD CANDIDATE → MASTER REVIEW`
`INPUT → OUTPUT → EVENT → EVIDENCE → VALIDATION → CHECKPOINT → NEXT`

## 4. ماشین وضعیت اجباری

| وضعیت | معنای دقیق | شاهد لازم |
|---|---|---|
| DRAFT | پیش‌نویس | متن موجود |
| REGISTERED | نوشته شده در مقصد | write/commit receipt |
| READ-BACK VERIFIED | بعد از نوشتن دوباره خوانده و تطبیق شده | fetch مستقل + تطبیق محتوا/شناسه |
| VALIDATED | معیارهای آزمون پاس شده | ورودی آزمون، نسخه ابزار، خروجی و معیار |
| INTEGRATED | در مقصد مادر/شاخص/صف ادغام و بازخوانی شده | تغییر مقصد + read-back |
| ACTIVE | برای استفاده جاری انتخاب شده | تصمیم/پیکربندی قابل‌اثبات |
| LIVING | تغییر افزایشی و پیگیری نسخه‌ها فعال است | نسخه، تاریخچه، گام بعدی و نگهداری موارد باز |
| OPEN / PENDING | کار ناتمام | مالک/مانع/اقدام بعدی |
| NOT RUN | هیچ اجرای آزمونی ثبت نشده | دلیل و پیش‌شرط اجرا |
| NOT VERIFIED | شواهد کافی نیست | شکاف و مسیر اثبات |
| BLOCKED / UNSUPPORTED | مانع واقعی یا قابلیت غایب | دلیل، نیازمندی و جایگزین |
| CLOSED | تنها پس از پذیرش صریح | همه معیارها + بازخوانی + تصمیم |

هیچ وضعیت بالاتری به صورت خودکار از وضعیت پایین‌تر استنتاج نمی‌شود. موارد OPEN/NOT RUN/NOT VERIFIED در هر checkpoint جدید منتقل می‌شوند تا شاهد کافی برای بستن آن‌ها وجود داشته باشد.

## 5. قالب استاندارد رکورد تعامل

برای هر تعامل معنادار یک جفت IN/OUT و رویداد متناظر بساز:

```yaml
record_id: "<unique stable id>"
production_id: "<unique production id>"
version: "1.0.0"
kind: "INPUT|OUTPUT|EVENT|TEST|ERROR|CORRECTION"
timestamp_utc: "<actual timestamp or UNKNOWN>"
timestamp_tehran: "<same instant converted, or UNKNOWN>"
repository_commit: "<actual commit SHA or PENDING>"
source_refs: []
parent_refs: []
content_ref: "<path or canonical source>"
observations:
  - statement: "<directly observed>"
    kind: "OBSERVED|HYPOTHESIS|INFERENCE|USER_FEEDBACK"
    evidence_refs: []
tests:
  - test_id: "<test id>"
    status: "PASS|FAIL|NOT RUN|NOT VERIFIED|BLOCKED"
    evidence_ref: "<raw result>"
failures:
  - description: "<failure or gap>"
    status: "OPEN|RESOLVED|UNTESTED"
    correction_ref: null
status: "REGISTERED"
next_action: "<deterministic next step>"
```

محتوای واقعی کاربر/مدل نباید با خلاصه حدسی جایگزین شود. اگر منبع خام در دسترس نیست، صریحاً MISSING ثبت شود.

## 6. قالب استاندارد آزمون

هر آزمون باید داشته باشد:
- شناسه آزمون و معیار پذیرش دقیق.
- ورودی و نسخه دقیق فایل/بسته.
- نام و نسخه ابزار/اعتبارسنج، میزبان و مدل در صورت معلوم بودن.
- زمان اجرای واقعی UTC و تبدیل تهران.
- نتیجه خام، نتیجه مورد انتظار و مقایسه.
- وضعیت PASS / FAIL / NOT RUN / BLOCKED.
- مسیر شواهد، digest واقعی و رسید بازخوانی مستقل.
- علت شکست، اصلاح پیشنهادی و شرط اجرای مجدد.

«توضیح آزمون نوشته شد» آزمون اجراشده محسوب نمی‌شود.

## 7. قابلیت میزبان و آزمون انتقال

قابلیت‌ها باید جداگانه ارزیابی شوند:
- دریافت/استخراج فایل‌ها.
- خواندن و نوشتن فایل/مخزن با مجوز.
- تولید hash دقیق بایت‌ها و تطبیق manifest.
- اعتبارسنجی JSON Schema با fixture معتبر و نامعتبر.
- بازیابی حالت از IN و جداگانه از OUT.
- بازیابی پس از پایان نشست/شروع مجدد.
- حافظه پایدار میزبان.
- زمان‌بندی و اجرای پس‌زمینه در حالت idle.
- اتصال ابزارها و ثبت رویدادهای شکست/تلاش مجدد.
- واردسازی در میزبان مستقل و سپس میزبان دوم.

نردبان اثبات:
`DECLARED → CONFIGURED → EXECUTION OBSERVED → RESTART/IDLE TEST PASSED → INDEPENDENT READ-BACK → ACCEPTED`

میزبان جدید باید فقط بر اساس فایل‌های ارائه‌شده وضعیت را بازسازی کند و فهرست فایل‌های غایب/شکسته، checkpoint جاری، مادر، تبار، شواهد، موارد باز و اقدام بعدی را گزارش دهد. اگر حافظه/زمان‌بندی/دسترسی وجود ندارد، UNSUPPORTED یا NOT VERIFIED ثبت شود.

## 8. قالب فهرست بازهای زنده

| Open ID | موضوع | وضعیت فعلی | مانع/شاهد لازم | اقدام بعدی | شرط بستن |
|---|---|---|---|---|---|
| OPEN-EXPORT-SHA256 | digest بسته | OPEN / NOT RUN | hash بایت‌های دقیق همه فایل‌های manifest | محاسبه و تطبیق | همه digestها و manifest دوباره خوانده و تطبیق شوند |
| OPEN-SCHEMA-FIXTURES | schema | OPEN / NOT RUN | اعتبارسنج و دو fixture | اجرای مثبت/منفی | معتبر پاس و نامعتبر رد شود |
| OPEN-IN-OUT-RECOVERY | بازیابی مستقل | OPEN / NOT RUN | دو ورودی مستقل | بازسازی و diff | حالت canonical و open gates برابر باشند |
| OPEN-REPO-LINK-ID-AUDIT | پیوند/شناسه | OPEN / REVIEW_REQUIRED | ۱۱ پیوند مفقود و برخوردهای شناسایی‌شده | triage موردبه‌مورد | هر مورد با تصمیم مستند حل یا به‌عنوان تعارض باز نگه داشته شود |
| OPEN-CLEAN-HOST | میزبان تمیز | OPEN / NOT RUN | محیط مجاز مستقل | import سرد | بازسازی بدون حافظه پنهان و ثبت شواهد |
| OPEN-SECOND-HOST | میزبان دوم | OPEN / BLOCKED UNTIL AVAILABLE | میزبان مستقل مجاز | آزمون conformance | رسید مستقل |
| OPEN-PERSISTENCE | حافظه پس از restart | OPEN / NOT VERIFIED | runtime مجاز و durable store | marker/restart/read-back | marker بازیابی و تطبیق شود |
| OPEN-IDLE-BACKGROUND | اجرای بی‌تعامل | OPEN / NOT VERIFIED | scheduler/agent واقعی | اجرای job زمان‌دار | خروجی و زمان واقعی پس از idle ثبت شود |
| OPEN-MOTHER-INDEX-QUEUE | ادغام مقصدها | OPEN / PARTIAL | فایل‌های اصلی و بازخوانی | ادغام افزایشی | هر مقصد مستقل بازخوانی و تطبیق شود |

فهرست بالا حداقل لازم است؛ کشف‌های تازه به آن افزوده می‌شوند. موارد باز نباید از checkpoint بعدی حذف شوند.

## 9. ممیزی سخت فعلی و تصمیم

آخرین ممیزی ساختاری موجود در EVT-0154 روی commit مشخص انجام شده و نتیجه آن REVIEW_REQUIRED است:
- ۱۱ پیوند محلی مفقود.
- ۶۱ گروه برخورد Stable ID، که ۶۰ گروه بررسی‌نشده‌اند.
- ۸۸ گروه برخورد Production ID.
- ۷ گروه برخورد Reference ID.
- ۳۶ گروه برخورد شماره رویداد.
- ۱۳ رابطه والد مبهم.
- یک زمان مبهم.
- آزمون‌های واقعی واردسازی کامل RAHM به میزبان AI مستقل، بازیابی IN/OUT، digest بسته و fixtureهای schema هنوز تأیید نشده‌اند.

این یافته‌ها باید با حفظ تاریخچه رسیدگی شوند؛ حذف خودکار، ادغام خودکار شناسه‌ها یا اعلام پاک‌بودن معماری ممنوع است.

## 10. قرارداد به‌روزرسانی سند مادر

هر تغییر باید:
1. ورودی/منشأ و دلیل تغییر را ثبت کند.
2. نسخه جدید بسازد و نسخه‌های قبلی را حفظ کند.
3. پیوندهای والد/فرزند، CURRENT و NEXT را به‌روزرسانی کند.
4. مقصدهای مادر، index، queue، manifest و evidence ledger را به‌صورت افزایشی اصلاح کند.
5. هر فایل را بعد از نوشتن دوباره بخواند و تطبیق دهد.
6. وضعیت را فقط بر اساس شواهد ارتقا دهد.
7. شکست/ابهام را در فهرست OPEN نگه دارد.
8. یک اقدام بعدی قابل اجرا و مشخص ثبت کند.

این سند یک قرارداد مرجع نسخه‌دار است، نه ادعای اجرای خودکار دائمی. زنده‌بودن واقعی در هر نشست به ابزار ذخیره‌سازی/زمان‌بندی و آزمون‌های میزبان وابسته است.

## 11. پذیرش نهایی این سند

- [ ] فایل سند مادر نوشته و دوباره خوانده شود.
- [ ] تمام پیوندهای همین سند در درخت مخزن بررسی شوند.
- [ ] manifest شامل این سند و digest دقیق شود.
- [ ] JSON Schema با fixture معتبر و نامعتبر اجرا شود.
- [ ] بسته از commit نام‌گذاری‌شده استخراج و در زمینه تمیز بازیابی شود.
- [ ] بازیابی از IN و OUT مستقل مقایسه شود.
- [ ] یک میزبان مستقل مجاز import را انجام دهد.
- [ ] حافظه پایدار/اجرای پس‌زمینه فقط در صورت وجود runtime واقعی آزموده شود.
- [ ] مادر، index و queue اصلی ادغام و بازخوانی شوند.

**وضعیت پذیرش:** OPEN / NOT RUN. ایجاد این سند به‌تنهایی هیچ‌یک از این معیارهای آزمون را PASS نمی‌کند.
