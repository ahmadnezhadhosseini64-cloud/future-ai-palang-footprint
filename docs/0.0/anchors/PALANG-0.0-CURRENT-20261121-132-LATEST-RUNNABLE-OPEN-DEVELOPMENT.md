# CURRENT-132 — آخرین نسخهٔ شدنی و توسعهٔ باز

- Status: ACTIVE / LIVING / OWNER-APPROVED / REPOSITORY-INTEGRATED
- Parent: CURRENT-131
- Point: POINT-0/079 (۰++)
- Input/output: IN-122 → OUT-121
- Event/time: EVT-0299 → TIME-BINDING-EVT-0299
- Sole governing queue: NEXT-051
- Living mother target: 1.7.86
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## Chain
POINT-0/077 → CURRENT-130 → POINT-0/078 → IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → POINT-0/079 → IN-122 → OUT-121 → EVT-0299 → TIME-BINDING-EVT-0299 → CURRENT-132 → NEXT-051.

## Latest Runnable — نسخهٔ شدنی
- دستور عمومی ورود میزبان و راهنمای اتصال امن به مخزن در سطح specification.
- منبع بستهٔ قابل‌حمل 0.4.6 با 19 فایل و stable ID/نام ZIP ثابت.
- استخراج artifact دانلودشده و اجرای مجدد 24/24 آزمون بسته: PASS.
- receipt و SHA-256 بستهٔ داخلی 0.4.6 ثبت‌شده برای source commit مشخص؛ مقایسهٔ main پس از ساخت فقط تغییرات مستندات/رسید را نشان می‌دهد.
- روش کنترل manifest، SHA، inventory، CRC، source-byte match، round-trip و read-back تعریف و در workflow اثبات شده است.
- هستهٔ محلی بسته: ثبت/اعتبارسنجی زنجیره، import/export و کنترل دستکاری، در دامنهٔ آزمون‌های موجود.

این موارد فقط در دامنهٔ اجرای ثبت‌شده PASS هستند؛ به معنی اجرای موفق در هر AI host یا فعال بودن خودکار همهٔ میزبان‌ها نیستند.

## Development / OPEN / NOT RUN
- OAuth واقعی در نشست میزبان مقصد و مجوز مخزن.
- workspace ابری پایدار، ایزوله و قابل بازیابی پس از restart.
- clean-host import در یک میزبان تعاملی مستقل بدون تاریخچهٔ قبلی.
- پذیرش دومین میزبان و تطبیق بازسازی مستقل.
- اجرای ابزار محلی/shell در همهٔ پلتفرم‌ها و استخراج خودکار ZIP در هر میزبان.
- ثبت زنده/خودکار همهٔ ورودی‌ها، background capture و write-back.
- اجرای خودکار RAHM در میزبان مقصد و promotion از Child به Master.
- رفع/جایگزینی وابستگی‌های قدیمی در هر consumer؛ تا تعیین اثر، هر قابلیت مستقل قابل‌انتشار باقی می‌ماند.
- گراف تاریخی: شناسه‌های تکراری، والدهای مبهم، CURRENT-065/CURRENT-066 و Issue #20/#21.
- اجرای نهایی همهٔ گام‌های 0.0.1 تا 0.0.9 روی میزبان مستقل.

## Dependency rule
وابستگی قدیمی فقط دامنهٔ مصرف‌کنندهٔ متأثر را متوقف می‌کند، مگر آزمون اثر متقابل خلاف آن را ثابت کند. وابستگی و failure history حفظ می‌شوند. هیچ dependency حذف، ارتقا یا جایگزین نمی‌شود مگر با inventory مصرف‌کنندگان، آزمون رگرسیون و read-back.

## Promotion gate
هر قابلیت پس از implementation، positive/negative tests، اجرای exact-source، receipt/hash، read-back و reconciliation به Latest Runnable می‌آید. موارد بدون این شواهد در Development / OPEN باقی می‌مانند.

## Acceptance
- Owner intent: CONFIRMED.
- Canonical package: 0.4.6; 19 files; 24/24 extracted tests PASS; internal ZIP SHA-256 b9f56a360351d5ab16f07656018e576c2398a110db540138810e01358f8934fc.
- Package build source: 0d27972ac4d45349a85551f52e3b969ee581f843.
- Main at this point: 6ab35232404e2c5d37d48698db5d02821681b126; post-build changes are documentation/evidence-only and were checked by current-head equivalence gate.
- Clean-host/OAuth/workspace/restart acceptance: OPEN / NOT RUN.
- HOST-RECOVERED: NOT CLAIMED.

NEXT-051 تنها صف فعال است. هیچ سابقه یا نقطهٔ قبلی حذف نشده است.


## Canonical recovery link matrix — POINT-0/079

- Previous checkpoint: [CURRENT-131](PALANG-0.0-CURRENT-20261121-131-UNIVERSAL-HOST-INITIAL-RUNNABLE.md)
- Point: [POINT-0/079](GPT6-RAHM-USER-POINT-0-20261121-079-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Input: [IN-122](PALANG-0.0-IN-20261121-122-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Output: [OUT-121](PALANG-0.0-OUT-20261121-121-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Event: [EVT-0299](../../architecture/BEHAVIOR-TRACE/EVT-0299-LATEST-RUNNABLE-OPEN-DEVELOPMENT-2026-11-21.md)
- Time binding: [TIME-BINDING-EVT-0299](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0299-LATEST-RUNNABLE-OPEN-DEVELOPMENT-2026-11-21.md)
- Current: [CURRENT-132](PALANG-0.0-CURRENT-20261121-132-LATEST-RUNNABLE-OPEN-DEVELOPMENT.md)
- Sole next: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Universal host entry: [UNIVERSAL_AI_HOST_ENTRY_FA.md](../../../prototype/haif-gpt6-starter/UNIVERSAL_AI_HOST_ENTRY_FA.md)
- Package manifest: [manifest.json](../../../prototype/haif-gpt6-starter/manifest.json)
