# CURRENT-131 — نسخهٔ اولیهٔ شدنی، عمومی و قابل‌بازیابی میزبان

- Status: ACTIVE / LIVING / REPOSITORY-INTEGRATED / MAIN-READBACK-VERIFIED
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
- Source documents: PR #68 and #69 merged; cross-layer recovery link audit PASS on the follow-up correction; main read-back verified.
- Canonical ZIP: PACKAGE_VERIFIED — internal version 0.4.6; exact build source 0d27972ac4d45349a85551f52e3b969ee581f843; current main 6ee4dff3adbdf65dadc4349106b1f120ca49c175 differs only by the Evidence Gate receipt commit.
- Package extraction, CRC, source-byte read-back, downloaded-artifact round-trip and extracted tests: PASS; 24/24 tests; 19 files; 255468 bytes; SHA-256 b9f56a360351d5ab16f07656018e576c2398a110db540138810e01358f8934fc.\n- Clean-host extraction and independent recovery: OPEN / NOT RUN.
- Destination OAuth and persistent workspace: OPEN / NOT RUN.
- HOST-RECOVERED: NOT CLAIMED.

NEXT-051 تنها صف اجرایی است. هیچ نقطه یا سابقهٔ قبلی حذف نمی‌شود.


## Canonical recovery link matrix — POINT-0/078

- Point: [POINT-0/078](GPT6-RAHM-USER-POINT-0-20261121-078-UNIVERSAL-HOST-0PLUSPLUS.md)
- Input: [IN-121](PALANG-0.0-IN-20261121-121-UNIVERSAL-HOST-INITIAL-RUNNABLE.md)
- Output: [OUT-120](PALANG-0.0-OUT-20261121-120-UNIVERSAL-HOST-INITIAL-RUNNABLE.md)
- Event: [EVT-0298](../../architecture/BEHAVIOR-TRACE/EVT-0298-UNIVERSAL-HOST-INITIAL-RUNNABLE-2026-11-21.md)
- Sole next: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Mirror event: [EVT-0241](../../architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md)
- Mirror time binding: [TIME-BINDING-EVT-0241](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-2026-10-31.md)


## Preserved open gates and unresolved historical pointer

- Full state recovery / reconstruct independently from IN and OUT: OPEN / NOT RUN.
- Clean host import / clean interactive AI-host session: OPEN / NOT RUN.
- Second-host import / second-host acceptance: OPEN / NOT RUN.
- Restart persistence / restart/new-session recovery: OPEN / NOT RUN.
- Automatic live message capture / idle/background capture: OPEN / NOT PROVEN.
- Graph/identity/parent/time triage: OPEN; duplicate IDs and ambiguous parents remain under source-backed review.
- CURRENT-065/CURRENT-066 pointer conflict: OPEN; no winner selected. Preserve both historical records until source adjudication is completed.

- Issue #20 and Issue #21: OPEN / NOT CLOSED; preserve their historical evidence and continue through the existing NEXT-051 triage gates.
