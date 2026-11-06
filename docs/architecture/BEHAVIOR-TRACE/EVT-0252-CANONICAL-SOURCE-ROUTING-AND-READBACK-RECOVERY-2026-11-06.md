# EVT-0252 — درس بازیابی منبع مرجع و بازخوانی سند از مخزن

- Event ID: EVT-0252
- Stable ID: CANONICAL-SOURCE-ROUTING-AND-READBACK-RECOVERY-2026-11-06-001
- Date: 2026-11-06
- Project: Future AI / Palang Footprint
- Status: REGISTERED / REPOSITORY READ-BACK VERIFIED / POLICY OPERATIONALIZED; repository CI regression PASS on exact source commit `471941d0cbc5f28a0c4364e85c1b99c833f0529d` (run `42284923957`); live AI-host enforcement and independent-host test OPEN
- Root preserved: POINT-0/061
- Checkpoint preserved: CURRENT-112
- Sole active queue preserved: NEXT-051
- Derived lesson: [LAL-20261106-001](../ARCHITECTURE-LESSONS/lessons/LAL-20261106-001-CANONICAL-SOURCE-ROUTING-AND-READBACK-RECOVERY.md)

## User intent

کاربر خواست نتیجهٔ بازیابی سند، خطاهای رخ‌داده، علت تأخیر در پیدا کردن سند و روش موفق کشف و استخراج آن به پروژهٔ «آینده AI / ردپای پلنگ» منتقل شود تا به درس، قاعده و جزء قابل استفاده در معماری تبدیل شود؛ نه اینکه صرفاً گزارش این گفت‌وگو باقی بماند.

## Observed sequence

1. درخواست اولیه دربارهٔ بازیابی «چکیده آخر» و سپس «۲ زبانه آخر» از پوشهٔ گواهی بود.
2. تلاش‌های ابتدایی در Library فایل‌های ChatGPT انجام شد. آن مقصد، نسخه‌های چکیده و یک فایل دوزبانهٔ قدیمی را نشان می‌داد؛ فایل نهایی موردنظر از آن مسیر به دست نیامد.
3. خطای روش: منبع جست‌وجو با مقصدی که کاربر صریحاً به آن اشاره می‌کرد (مخزن پروژه) هم‌راستا نبود.
4. مسیر دقیق فایل در GitHub branch `main` مستقیماً fetch شد: `گواهی/گواهی-سابقه-کار-دوزبانه-آخر.md`.
5. blob SHA بازخوانی‌شده: `acdbb688d19ba3e86658826857ed5885bfd8da9c`.
6. جست‌وجوی درون همان repository دو راهنمای رسمی را یافت: `گواهی/README.md` و `گواهی/فهرست-بازیابی-سه-سند-نهایی.md`. هر دو نام «۲ زبانه آخر» را به مسیر قطعی فوق متصل می‌کنند.
7. هیچ فایل یا محتوای گواهی در جریان این بازیابی تغییر نکرد.

## Root-cause classification

- Confirmed: source-routing error — ابتدا Library بررسی شد، در حالی که سند canonical در GitHub repository بود.
- Confirmed: دو مقصد مستقل با هم خلط شدند؛ نبود نتیجه در Library نباید به نبود فایل در GitHub تعبیر شود.
- Not established: اینکه فایل در مخزن وجود نداشت، حذف شده بود یا کاربر مسیر را اشتباه گفته بود؛ شواهد خلاف این برداشت را نشان می‌دهد.
- Not yet proven: اجرای خودکار این قاعده در همهٔ میزبان‌ها یا بازیابی مستقل بدون سابقهٔ گفتگو.

## Operational correction

از این پس برای درخواست صریح «از مخزن»:
1. مخزن GitHub پروژه منبع اصلی است.
2. README/index و فهرست بازیابی رسمی پیش از جست‌وجوی آزاد بررسی می‌شوند.
3. نام کوتاه به مسیر canonical نگاشت می‌شود.
4. فایل کامل از branch/ref مشخص fetch می‌شود.
5. مسیر، SHA، متن کامل و داده‌های کلیدی read-back می‌شوند.
6. شکست جست‌وجوی اولیه باعث تغییر راهبرد در همان مقصد می‌شود، نه اعلام زودهنگام فقدان سند.
7. Library، GitHub، بستهٔ محلی و میزبان مستقل مقصدهای جدا با شواهد جدا هستند.

## Evidence boundary

این مورد بازیابی موفق فایل از GitHub و خواندن راهنماهای رسمی را اثبات می‌کند. این مورد به‌تنهایی آزمون میزبان مستقل، اجرای runtime خودکار یا همگام‌سازی Library را اثبات نمی‌کند. وضعیت این قابلیت‌ها OPEN / NOT RUN / NOT PROVEN باقی می‌ماند.

## Architecture disposition

- Lesson: [LAL-20261106-001](../ARCHITECTURE-LESSONS/lessons/LAL-20261106-001-CANONICAL-SOURCE-ROUTING-AND-READBACK-RECOVERY.md)
- Root/checkpoint/queue unchanged: POINT-0/061 → CURRENT-112 → NEXT-051.
- No NEXT-052 created.
- Completed: lesson connected to the living lesson registry, Reference Index, integration queue and HAIF mother; destination-first controls added to Stable Retrieval Core and Retrieval Runtime; repository CI regression check wired. Pending: inspect CI on the final integration SHA, then run fresh-context/independent-host retrieval as a separate acceptance gate.


### Repository regression execution receipt — 2026-11-06
- Workflow: Evidence Gate - Independent Execution Test
- Run ID: 42284923957
- Tested source commit: `471941d0cbc5f28a0c4364e85c1b99c833f0529d`
- Result: SUCCESS; job `evidence-gate` completed successfully.
- Log confirms the destination-first regression assertions executed and printed `Canonical source-routing regression contract: VERIFIED`.
- Scope: repository policy-presence/linkage regression only. It does not prove live AI tool-selection behavior or independent-host recovery.
