# CURRENT-131 — نسخهٔ اولیهٔ شدنی، عمومی و قابل‌بازیابی میزبان

- Status: ACTIVE / LIVING / REPOSITORY-INTEGRATION-PENDING
- Parent: CURRENT-130
- Point: POINT-0/078 (۰++)
- Input/output: IN-121 → OUT-120
- Event/time: EVT-0298 → TIME-BINDING-EVT-0298
- Sole governing queue: NEXT-051
- Living mother target: 1.7.85
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## Chain
POINT-0/077 → CURRENT-130 → POINT-0/078 → IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → NEXT-051.

## Latest Runnable
نسخهٔ اولیه، دستور عمومی آغاز میزبان و قرارداد بازیابی/تداوم است. قابلیت‌های قابل پیاده‌سازی شامل خواندن مخزن یا بستهٔ دریافت‌شده، تعیین exact HEAD/commit، بررسی manifest و SHA-256 در صورت وجود ابزار، استخراج امن در پوشهٔ جدا، تطبیق inventory و فایل‌ها، بازسازی زنجیره از Reference Index، اجرای آزمون‌های موجود در runtime مناسب، ثبت خروجی و رسید، و پیشنهاد تغییرات در branch جدا است. این موارد در هر میزبان فقط وقتی VERIFIED محسوب می‌شوند که همان میزبان شاهد اجرای مستقیم ارائه کند.

## Development / OPEN
- OAuth و اتصال واقعی در هر میزبان مقصد.
- workspace ابری پایدار، ایزوله و قابل بازیابی پس از restart.
- اجرای shell/Python و ابزارهای محلی در همهٔ پلتفرم‌ها.
- دریافت و استخراج خودکار ZIP در هر میزبان.
- پذیرش مستقل میزبان بدون تاریخچهٔ قبلی و بازسازی کامل گراف.
- اتصال زندهٔ ورودی/خروجی، ثبت خودکار و write-back به مخزن.
- اجرای خودکار RAHM و بازگشت کنترل‌شدهٔ Child به Master.
- بسته‌بندی تازه و receipt exact-main برای این نقطه تا پایان workflow.

## Promotion gate
هر قابلیت تنها با پیاده‌سازی واقعی، آزمون مثبت و منفی، اجرای روی منبع مشخص، رسید دارای SHA و زمان، read-back و تطبیق نسخه به Latest Runnable ارتقا می‌یابد. قابلیت‌هایی که فقط در یک میزبان کار می‌کنند با همان دامنه ثبت می‌شوند و عمومی فرض نمی‌شوند.

## Acceptance
- Owner intent: CONFIRMED.
- Source documents: prepared on a dedicated branch; main integration pending.
- Canonical ZIP exact-current-main rebuild: OPEN / NOT RUN.
- Clean-host extraction and independent recovery: OPEN / NOT RUN.
- Destination OAuth and persistent workspace: OPEN / NOT RUN.
- HOST-RECOVERED: NOT CLAIMED.

NEXT-051 تنها صف اجرایی است. هیچ نقطه یا سابقهٔ قبلی حذف نمی‌شود.
