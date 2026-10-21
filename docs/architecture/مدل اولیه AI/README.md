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
- برنامهٔ نرم‌افزاری: هنوز پیاده‌سازی/استقرار نشده.
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
