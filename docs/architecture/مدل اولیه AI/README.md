# مدل اولیهٔ هوش مصنوعی — HAIF

این پوشه، نقطهٔ شروع رسمی توسعهٔ محصول Future AI / Palang Footprint است. از اینجا به بعد، تغییرات مدل اولیه باید بر مبنای سند مرجع مادر و صف گام‌های بعدی انجام شوند.

## فایل‌های این پوشه

1. [سند مرجع مادر مدل اولیهٔ هوش مصنوعی](./سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md) — تعریف هدف، معماری، اجزا، مدل داده، قواعد حاکم، مراحل ساخت، شواهد و محدودیت‌ها.
2. [صف گام‌های بعدی و موارد باز](./صف%20گام‌های%20بعدی%20و%20موارد%20باز.md) — کارهای مرحله‌بندی‌شده، معیار پذیرش و مواردی که هنوز نباید بسته‌شده اعلام شوند.
3. [رویداد ثبت ساخت بسته](../BEHAVIOR-TRACE/EVT-0058-INITIAL-AI-MODEL-PACKAGE-CREATION-2026-10-21.md) — منشأ درخواست، اقدامات واقعی، commitها، بازخوانی و نتیجهٔ ممیزی پس از ایجاد.

## منابع مرجع متصل

- [مدل اولیهٔ محصول HAIF](../../reference/REFERENCE-DOCUMENTS/HAIF-INITIAL-PRODUCT-ARCHITECTURE-2026-10-21-001.md)
- [معماری اجرایی قابل پیاده‌سازی](../../reference/REFERENCE-DOCUMENTS/FUTURE-AI-PALANG-FOOTPRINT-IMPLEMENTABLE-REFERENCE-ARCHITECTURE-2026-10-21-001.md)
- [مبنای معماری معنایی گراف تاریخی](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-SEMANTIC-ARCHITECTURE-BASELINE-2026-10-21-001.md)
- [سند مادر تطبیق گراف تاریخی](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-GRAPH-RECONCILIATION-LIVING-MASTER-REFERENCE-2026-10-21-001.md)
- [دفتر داوری شناسه‌ها و روابط](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-IDENTIFIER-AND-RELATION-ADJUDICATION-REGISTER-2026-10-21-001.md)
- [نمایهٔ مرجع پروژه](../../REFERENCE_INDEX.md)

## وضعیت فعلی

- مدل اولیهٔ مستندشده: ثبت شده؛ read-back و ممیزی تازهٔ همین commit باید در رویداد ثبت شود.
- برنامهٔ نرم‌افزاری: هستهٔ محلی `scripts/haif-runtime/haif_runtime.py` و آزمون‌هایش از قبل در مخزن هستند؛ در POINT-0/019 ابزار کشف اشاره‌گر جاری و آزمون‌های fixture نیز اضافه و به ممیزی CI وصل شدند. نتیجهٔ اجرای دقیق commit هنوز نیازمند خواندن رسید واقعی است؛ استقرار تولیدی، واردسازی میزبان مستقل، ضبط خودکار و اجرای پس‌زمینه اثبات نشده‌اند.
- بررسی معنایی گراف و گروه‌های شناسه/EVT: باز و مرحله‌ای.
- محدودهٔ این مرحله: فقط مخزن GitHub. Buffer، Persistent Memory، Library و Dropbox تغییر داده نشده‌اند و تأییدشده نیستند.

## قاعدهٔ ادامه

پیش از هر تغییر، سند مرجع مادر و صف گام‌های بعدی را بخوان. پس از هر تغییر، فایل‌ها را بازخوانی کن، پیوندها را بررسی کن، ممیزی تازه اجرا کن و وضعیت واقعی را در رویداد و صف ثبت کن. هیچ مورد نامطمئن یا تاریخی را صرفاً برای کم‌کردن تعداد موارد باز حذف یا بسته‌شده اعلام نکن.


## نمونهٔ اجرایی شروع‌شده
- [HAIF v0 — نمونهٔ اجرایی اولیه](../../../prototype/haif-v0/README.md): API پایهٔ لنگر و رویداد، SQLite محلی، hash و بازخوانی پس از نوشتن.
- [EVT-0059 — رویداد پیاده‌سازی نمونه](../BEHAVIOR-TRACE/EVT-0059-HAIF-V0-PROTOTYPE-IMPLEMENTATION-2026-10-21.md).
- آزمون خودکار: [HAIF Prototype Tests 39536269368](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39536269368) — 5 passed, 1 warning, 0 failed.
- مرز وضعیت: نمونهٔ v0 پیاده‌سازی و آزموده شده؛ برنامهٔ تولیدی، استقرار امن، گراف معنایی و مقصدهای بیرونی هنوز کامل/تأییدشده نیستند.


## سند مرجع زندهٔ نام‌گذاری‌شده — مبنای بازگشت ۰.۰
- [مدل اولیه — لنگر ۰.۰ و سند مرجع زنده](./مدل%20اولیه%20—%20لنگر%20۰.۰%20و%20سند%20مرجع%20زنده.md) — Stable ID: `PALANG-INITIAL-AI-MODEL-0.0-RETURN-MASTER-REFERENCE-2026-10-21-001`, Production ID: `PIM0RM-2026-10-21-001`, Version 1.0.0.
- این سند، مرجع جامع نام‌گذاری‌شده برای هدف محصول، معماری، قواعد ثبت، وضعیت شواهد و صف ادامه است. وضعیت: ACTIVE / LIVING / GOVERNING BASELINE در مخزن؛ مقصدهای بیرونی تأیید نشده‌اند.

## سند مرجع مادر — الگوریتم استخراج و محصول رایگان HAIF
[سند مرجع مادر — الگوریتم استخراج مدل و محصول رایگان HAIF](./سند%20مرجع%20مادر%20—%20الگوریتم%20استخراج%20مدل%20و%20محصول%20رایگان%20HAIF.md)
- Stable ID: `HAIF-EXTRACTABLE-INTERACTION-MODEL-FREE-APP-MASTER-REFERENCE-2026-10-21-001`
- Production ID: `HEIMFA-MR-2026-10-21-001`; Version: `1.0.0`.
- Status: ACTIVE / LIVING / GOVERNING / OPEN FOR GROWTH. سند شامل معماری Master–Child–Rahm، الگوریتم استخراج از مخزن، طرح نسخهٔ رایگان، معیارهای پذیرش و صف بازگشت است.
- Registration timestamp: `2026-10-21T11:09:51+03:30` (Asia/Tehran).


## لنگر زندهٔ ثبت خودکار و ادامه پس از بازگشت — 2026-10-21

- [لنگر ۰.۰ — ثبت خودکار ورودی، لنگر زمانی، چکش و ادامهٔ پس از بازگشت](../../../checkpoints/0.0/PALANG-0.0-AUTOMATIC-INPUT-ANCHOR-AND-RETURN-RESUME-GOVERNANCE-2026-10-21-001.md).
- Stable ID: `PALANG-0.0-AUTOMATIC-INPUT-ANCHOR-AND-RETURN-RESUME-GOVERNANCE-2026-10-21-001`; Production ID: `P0AIRRG-2026-10-21-001`; Version 1.0.0.
- زمان ثبت سند: `2026-10-21T11:32:53+03:30` (Asia/Tehran).
- رویداد: [EVT-0059](../BEHAVIOR-TRACE/EVT-0059-AUTOMATIC-ANCHOR-REGISTRATION-AND-RETURN-RESUME-GOVERNANCE-2026-10-21.md).
- قاعده: برای هر ورودی/خروجی مرتبط با پروژه، چرخهٔ لنگرگذاری، ثبت، مستندسازی، پیوند معماری و چکش پیش‌فرض است؛ لازم نیست کاربر دوباره «ثبت کن» بگوید. این پیوند، لنگرهای تاریخی را ادغام یا جایگزین نمی‌کند.


## سند مرجع مادر — ثبت جامع و بازگشت اجرایی زنده
- [سند مرجع مادر — ثبت جامع و بازگشت اجرایی زنده](./سند%20مرجع%20مادر%20—%20ثبت%20جامع%20و%20بازگشت%20اجرایی%20زنده.md)
- Stable ID: `PALANG-MASTER-REFERENCE-AUTOMATIC-REGISTRATION-AND-RETURN-EXECUTION-2026-10-21-001`; Production ID: `PMR-ARRE-2026-10-21-001`; Version 1.0.0.
- زمان ثبت: `2026-10-21T11:37:45+03:30` (Asia/Tehran).
- لنگر مستقل: [PALANG-0.0-MASTER-REFERENCE-RETURN-EXECUTION-2026-10-21-001](../../../checkpoints/0.0/PALANG-0.0-MASTER-REFERENCE-RETURN-EXECUTION-2026-10-21-001.md).
- رویداد: [EVT-0060](../BEHAVIOR-TRACE/EVT-0060-MASTER-REFERENCE-RETURN-EXECUTION-2026-10-21.md).
- وضعیت: ACTIVE / LIVING / GOVERNING / OPEN FOR GROWTH؛ صف اجرایی پس از بازگشت در سند مادر آمده است.


## قابلیت اجرایی تازه — ورود و بازیابی سند با منشأ
- [EVT-0064 — ورود سند و بازیابی همراه با منشأ](../BEHAVIOR-TRACE/EVT-0064-HAIF-DOCUMENT-RETRIEVAL-PROVENANCE-2026-10-21.md).
- `prototype/haif-v0`: `POST /api/v1/documents` و `GET /api/v1/search?q=...`؛ مسیر منبع، نسخه، منشأ و SHA-256 حفظ می‌شود.
- آزمون CI: [39580170352](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39580170352) — 7 passed, 1 warning, 0 failed.
- مرز: بازیابی واژه‌محور است؛ جست‌وجوی معنایی/برداری و آزمون restart در صف باز می‌مانند.


## نسخهٔ معماری 1.1.0 — DTRC

- [سند مرجع مادر زندهٔ DTRC](../../reference/REFERENCE-DOCUMENTS/PALANG-DUAL-TRACK-BEHAVIORAL-ARCHITECTURE-MASTER-REFERENCE-2026-10-22-001.md) — استدلال دو‌مسیره و پیوستگی.
- [زوج ورودی/خروجی INT-20261022-008](../../0.0/anchors/PALANG-0.0-IN-20261022-008-BEHAVIORAL-ARCHITECTURE-UPDATE.md) / [خروجی](../../0.0/anchors/PALANG-0.0-OUT-20261022-008-BEHAVIORAL-ARCHITECTURE-UPDATE.md).
- [EVT-0094](../BEHAVIOR-TRACE/EVT-0094-DUAL-TRACK-BEHAVIORAL-ARCHITECTURE-2026-10-22.md).
- نسخهٔ سند مادر مدل به 1.1.0 افزایش یافت؛ تغییر به‌صورت الحاقیه انجام شده و تاریخچه حفظ شده است.
- وضعیت: ثبت و جای‌گذاری مخزنی انجام شده؛ آزمون runtime برای DTRC هنوز انجام نشده.

- پابند زمان UTC/تهران برای زنجیرهٔ DTRC: [TIME-BINDING-DTBA-2026-10-22-001](../BEHAVIOR-TRACE/TIME-BINDING-DTBA-2026-10-22-001.md).


## نسخهٔ معماری 1.2.0 — PIRHA

- [سند مرجع مادر PIRHA](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md) — حاکمیت ثبت تعاملی و ممیزی تاریخی.
- [زوج ورودی/خروجی INT-20261022-009](../../0.0/anchors/PALANG-0.0-IN-20261022-009-INTERACTION-GOVERNANCE-AND-AUDIT.md) / [خروجی](../../0.0/anchors/PALANG-0.0-OUT-20261022-009-INTERACTION-GOVERNANCE-AND-AUDIT.md).
- [EVT-0095](../BEHAVIOR-TRACE/EVT-0095-INTERACTION-GOVERNANCE-AND-HISTORICAL-AUDIT-2026-10-22.md).
- رویداد مستقل تاریخی [EVT-0093](../BEHAVIOR-TRACE/EVT-0093-REGISTRATION-CONTINUATION-2026-10-22.md) اکنون فایل مستقل دارد؛ بازخوانی آن شرط پذیرش باقی است.
- وضعیت: جای‌گذاری مستند انجام شد؛ ممیزی ساختاری تازه و تطبیق معنایی کامل هنوز باید با شواهد اجرا تأیید شوند.

- پابند زمانی PIRHA: [TIME-BINDING-PIRHA-2026-10-22-001](../BEHAVIOR-TRACE/TIME-BINDING-PIRHA-2026-10-22-001.md).
- لنگر ادامه: [PALANG-0.0-PIRHA-HISTORICAL-AUDIT-CONTINUATION-2026-10-22-001](../../0.0/anchors/PALANG-0.0-PIRHA-HISTORICAL-AUDIT-CONTINUATION-2026-10-22-001.md).


## نسخهٔ 1.3.0 — مبنای دائمی هر تعامل

- معماری مادر HAIF به نسخهٔ 1.3.0 ارتقا یافت؛ [سند مادر](سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- [PIRHA](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md) حاکم ترتیب ثبت، بازخوانی و ممیزی تاریخی است.
- زوج تعامل: [IN-010](../../0.0/anchors/PALANG-0.0-IN-20261022-010-BASELINE-REGISTRATION-AND-ARCHITECTURE-EVOLUTION.md) / [OUT-010](../../0.0/anchors/PALANG-0.0-OUT-20261022-010-BASELINE-REGISTRATION-AND-ARCHITECTURE-EVOLUTION.md); [EVT-0096](../BEHAVIOR-TRACE/EVT-0096-BASELINE-REGISTRATION-AND-ARCHITECTURE-EVOLUTION-2026-10-22.md).
- پذیرش کامل تاریخی هنوز باز است؛ نسخه‌گذاری به‌تنهایی نتیجهٔ ممیزی نیست.

- پابند زمانی: [TIME-BINDING-INT-20261022-010](../BEHAVIOR-TRACE/TIME-BINDING-INT-20261022-010.md).


## نسخهٔ 1.3.1 — دروازهٔ پذیرش

- معماری مادر HAIF: [نسخهٔ 1.3.1](سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- سند حاکم ثبت: [PIRHA نسخهٔ 1.2.0](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md).
- شکاف جاری: `GAP-PIRHA-ACCEPTANCE-GATE-001` — دروازهٔ پذیرش واحد برای هر تعامل.


## نسخهٔ 1.3.2 — ممیزی تاریخی و حلقهٔ اصلاح

- [معماری مادر HAIF v1.3.2](سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- [PIRHA v1.3.0](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md).
- [گزارش ممیزی تاریخی](../../reference/REFERENCE-DOCUMENTS/PALANG-REPOSITORY-HISTORICAL-AUDIT-RESULTS-2026-10-22-001.md) و [EVT-0097](../BEHAVIOR-TRACE/EVT-0097-REPOSITORY-HISTORICAL-AUDIT-RESULTS-2026-10-22.md).


## نسخهٔ 1.3.2 — ممیزی تاریخی و حلقهٔ اصلاح

- [معماری مادر HAIF v1.3.2](سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- [PIRHA v1.3.0](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md).
- [گزارش ممیزی تاریخی](../../reference/REFERENCE-DOCUMENTS/PALANG-REPOSITORY-HISTORICAL-AUDIT-RESULTS-2026-10-22-001.md) و [EVT-0097](../BEHAVIOR-TRACE/EVT-0097-REPOSITORY-HISTORICAL-AUDIT-RESULTS-2026-10-22.md).


## نسخهٔ 1.3.3 — پذیرش ساختاری پس از اصلاح
- [مدل مادر HAIF v1.3.3](سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- [PIRHA v1.4.0](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md).
- [گزارش PRHAR v1.1.0](../../reference/REFERENCE-DOCUMENTS/PALANG-REPOSITORY-HISTORICAL-AUDIT-RESULTS-2026-10-22-001.md)؛ [EVT-0097](../BEHAVIOR-TRACE/EVT-0097-REPOSITORY-HISTORICAL-AUDIT-RESULTS-2026-10-22.md).
- نتیجهٔ ممیزی ساختاری snapshot 0f29c9a: صفر پیوند محلی شکسته؛ تطبیق معنایی تاریخچه همچنان باز است.


## سند مادر خودبسنده و قابل‌انتقال — نسخهٔ HAIF 1.3.5
- قرارداد حاکم برای هر سند مادر: [SCEMRS v1.0.0](../../reference/REFERENCE-DOCUMENTS/PALANG-SELF-CONTAINED-EXECUTABLE-MASTER-REFERENCE-STANDARD-2026-10-22-001.md).
- رویداد: [EVT-0098](../BEHAVIOR-TRACE/EVT-0098-SELF-CONTAINED-EXECUTABLE-MASTER-REFERENCE-AND-OWNER-APPROVAL-2026-10-22.md).
- قاعدهٔ اختیار: تنها احمد پلنگ تغییر معماری حاکم را تأیید می‌کند؛ عامل فقط می‌تواند پیشنهاد را آماده کند تا زمانی که تأیید صریح ثبت شود.


- Active investigation: [PICTR-2026-10-22-001](../../reference/REFERENCE-DOCUMENTS/PALANG-IDENTITY-COLLISION-AND-TIMESTAMP-RECONCILIATION-MASTER-REFERENCE-2026-10-22-001.md) — identity collisions and EVT-0089 timestamp; open until semantic audit closes.


## شاخهٔ تعاملی GPT-6 — CURRENT-037
- [سند مرجع مادر زندهٔ پروژهٔ تعاملی GPT-6](../../reference/REFERENCE-DOCUMENTS/GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001.md) — Stable ID: `GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001`, Production ID: `G6IP-LMR-20261024-001`, Version 1.0.0.
- [CURRENT-037](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-037-GPT6-INTERACTIVE-PROJECT-START.md) is the new continuation anchor; [IN-027](../../0.0/anchors/PALANG-0.0-IN-20261024-027-GPT6-INTERACTIVE-PROJECT-START.md), [OUT-027](../../0.0/anchors/PALANG-0.0-OUT-20261024-027-GPT6-INTERACTIVE-PROJECT-START.md), and [EVT-0135](../BEHAVIOR-TRACE/EVT-0135-GPT6-INTERACTIVE-PROJECT-START-2026-10-24.md) preserve the interaction lineage.
- This is an additive product branch under the existing HAIF master architecture. Prior anchors and NEXT-036 remain intact; external storage and always-on global capture are not implied.
## شاخهٔ تعاملی GPT-6 — CURRENT-037

- پابند زمان: [TIME-BINDING-GPT6-INTERACTIVE-2026-10-24-001](../BEHAVIOR-TRACE/TIME-BINDING-GPT6-INTERACTIVE-2026-10-24-001.md)؛ UTC مرجع اصلی و زمان تهران معادل از همان commit.
- بازخوانی پنج فایل اصلی و پیوندهای نمایه تأیید شد؛ مقصدهای بیرونی هنوز اثبات نشده‌اند.


## Latest continuation — POINT-0/019
- [POINT-0/019 — Build model capabilities](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-019-MODEL-CAPABILITY-BUILD.md)
- [EVT-0181 — capability build event](../BEHAVIOR-TRACE/EVT-0181-POINT-0-019-MODEL-CAPABILITY-BUILD-2026-10-25.md)
- [Updated living master](./سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- [Updated capability and open-gap queue](./صف%20گام‌های%20بعدی%20و%20موارد%20باز.md)
- First executable addition: [live CURRENT pointer discovery checker](../../../scripts/behavior-hunter/discover_current_0_0_pointer.py) and [fixture tests](../../../scripts/behavior-hunter/tests/test_discover_current_0_0_pointer.py). CI result remains pending until the exact current main run and artifact are inspected.


## Executable portable starter — POINT-0/022

- [HAIF GPT-6 Portable Starter v0.1](../../../prototype/haif-gpt6-starter/README.md): executable Python engine, evidence-gated gap/Child state, hash-linked IN/OUT and portable bundle.
- [GPT-6 host instructions](../../../prototype/haif-gpt6-starter/GPT6_HOST_INSTRUCTIONS.md): startup, recovery, architecture governance and capability boundaries.
- [CURRENT-069](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-069-PORTABLE-STARTER-ENGINE-AND-GATE-CLOSURE.md): next acceptance gate.
- This is part of the existing Future AI / Palang Footprint repository, not a separate project.
- Status: seven starter tests and clean-process round-trip passed on tested SHA f482083cc2aeab82964c271c5d97ba4bb8657ce1; ZIP artifact 12600674334 was read back from Actions metadata. Independent download/import into a real GPT host is still unverified. Native GPT plugin, automatic capture, background execution, external writes and independent-host durable memory are not claimed.


## اتصال معماری Master–Rahm–Child — 2026-10-26
- نقطهٔ جاری: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md) و [CURRENT-079](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION.md).
- قرارداد آزمون و ارتقا: [Master–Rahm–Child](../MASTER-RAHM-CHILD/MASTER-RAHM-CHILD-CROSS-VALIDATION-CONTRACT-2026-10-26.md).
- این پوشه نقش RAHM را دارد و زیرمجموعهٔ Master اصلی است؛ مستقل یا مرجع موازی نیست. خروجی آزمون فقط CHILD CANDIDATE است تا Master صریحاً آن را بپذیرد.
- آزمون واقعی در محیط تعاملی، ورود میزبان مستقل و ماندگاری بیرونی هنوز رسید اجرایی ندارند و NOT RUN / OPEN باقی می‌مانند.


## اتصال معماری MASTER / RAHM / CHILD — POINT-0/032

- نقطهٔ ریشه: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- ورودی/خروجی: [IN-067](../../0.0/anchors/PALANG-0.0-IN-20261026-067-MASTER-RAHM-CHILD-BRIDGE.md) → [OUT-066](../../0.0/anchors/PALANG-0.0-OUT-20261026-066-MASTER-RAHM-CHILD-BRIDGE.md)
- رویداد: [EVT-0201](../BEHAVIOR-TRACE/EVT-0201-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION-2026-10-26.md)
- وضعیت جاری: [CURRENT-079](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION.md)
- نقش‌ها: پروژهٔ اصلی = MASTER؛ این بستهٔ مدل اولیه/محیط رشد = RAHM؛ نسخهٔ آزموده و دارای شواهد = CHILD candidate تا تصمیم مستر.
- معیار آزمون مستقل و محدودیت محیط تعاملی در سند POINT-0/032 آمده است. CI یا ثبت مخزن، واردسازی واقعی در پروژهٔ تعاملی را ثابت نمی‌کند.
- صف فعال همچنان NEXT-051 است؛ NEXT-052 ساخته نشود. شکاف‌های تاریخی و میزبان مستقل OPEN می‌مانند.

> Reconciliation: the canonical POINT-0/032 chain is the Master–Rahm–Child bridge chain. Do not use alternate same-number artifacts as active pointers; the duplicate records are retained for audit and require explicit source-lineage reconciliation.


- **Run the RAHM project validation:** [Interactive Project Validation Runbook](../MASTER-RAHM-CHILD/INTERACTIVE-PROJECT-VALIDATION-RUNBOOK.md). Paste its prompt into the actual interactive project after attaching the exact export bundle. The runbook is ready; actual test results remain NOT RUN until the project returns receipts.