# Project Zero — مبدأ معماری پروژهٔ تعاملی GPT-6

- Stable ID: `GPT6-INTERACTIVE-PROJECT-ZERO-BASELINE-2026-10-24-001`
- Production ID: `G6IP-P0-20261024-001`
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / EVOLVABLE / RECOVERABLE
- Parent: Future AI / Palang Footprint — HAIF
- Parent current anchor preserved: CURRENT-037
- New interaction: INT-20261024-028
- Pair: IN-028 ↔ OUT-028
- Event: EVT-0136
- New current continuation: CURRENT-038
- Next action anchor: NEXT-037
- Governing master: GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001

## Purpose / هدف
این سند نقطهٔ صفرِ معماری اولیهٔ پروژهٔ جدید کارهای تعاملی و تصویری در ChatGPT/GPT-6 است. این نقطه معماری را تثبیت می‌کند اما رشد را متوقف نمی‌کند. شاخهٔ جدید زیر حاکمیت HAIF و Future AI / Palang Footprint باقی می‌ماند و معماری موازیِ بی‌ارتباط ایجاد نمی‌کند.

## Rules inherited and activated / قواعد به‌ارث‌رسیده و فعال
1. Preserve before change: تاریخچه، شناسه‌ها، نقاط صفر و نسخه‌های قبلی حذف، بازنویسی یا ادغام بدون داوری شواهد نمی‌شوند.
2. UTC is canonical: زمان commit واقعی مخزن مرجع ثبت مخزنی است؛ زمان تهران با UTC+03:30 از همان لحظه مشتق می‌شود. زمان پیام، اجرا، آزمون و بازخوانی فیلدهای جدا هستند.
3. Evidence over assertion: هیچ وضعیت، زمان، آزمون یا مقصدی بدون شاهد مستقل تأییدشده اعلام نمی‌شود.
4. Write → Read-back → Match → Verify → Reconcile → Status: ثبت نوشتاری به‌تنهایی تأیید نهایی نیست.
5. IN/OUT/event/anchor: هر تعامل مهم دارای ورودی، خروجی، رویداد، لنگر مستقل، شناسهٔ پایدار و پیوند به سند مادر است.
6. Behavior trace: هدف درخواست، اقدام قابل‌مشاهده، نتیجه، خطا، اصلاح، بازخورد کاربر در صورت مشاهده، فرضیه‌ها و شواهد ثبت می‌شوند. علت پنهان مدل از روی خروجی حدس زده و واقعیت تلقی نمی‌شود.
7. Child → Rahm → Master: ایده ابتدا Child/فرضیه است؛ Rahm آن را با معیار و شواهد بررسی می‌کند؛ فقط پس از آزمون و پذیرش مستند به Master ارتقا می‌یابد.
8. Recoverability: از IN یا OUT باید بتوان به CURRENT، EVT، سند مادر، شواهد و NEXT برگشت؛ آزمون بازیابی تا زمان اجرا NOT RUN باقی می‌ماند.
9. Host honesty: قابلیت‌های این میزبان از قرارداد پروژه جدا ثبت می‌شوند. ACTIVE/LIVING بودن سند به معنی سرویس پس‌زمینه یا ثبت خودکار تمام گفتگوها نیست.
10. Destination-specific status: GitHub، Library، Buffer، حافظهٔ پایدار و Dropbox وضعیت مستقل دارند؛ موفقیت یک مقصد برای مقصد دیگر شاهد نیست.
11. Error learning: انحراف مسیر یا شکست، با علت قابل‌اثبات/فرضیهٔ جدا، اقدام اصلاحی و آزمون پیشگیری ثبت می‌شود؛ خطا پنهان یا به موفقیت تبدیل نمی‌شود.
12. No redundant retest: آزمون صحیح و مستند بی‌دلیل تکرار نمی‌شود؛ فقط تغییر واقعی، نیاز جدید، خطا، رگرسیون یا شاهد متناقض، آزمون مجدد را توجیه می‌کند.
13. Human decision boundary: ارتقای قواعد حاکم و ادعاهای مهم با شواهد و تصمیم روشن انجام می‌شود؛ بازخورد کاربر از واقعیت فنی تفکیک می‌شود.
14. Privacy minimization: شناسه‌های حساس و اطلاعات غیرضروری در اسناد عمومی مخزن تکثیر نمی‌شوند.
15. Living versioning: هر تغییر مهم نسخه، تاریخچه، دلیل، آزمون و وضعیت خودش را دارد؛ هیچ نسخهٔ قبلی بی‌ردپا جایگزین نمی‌شود.

## Product architecture / معماری محصول
- Interaction layer: کنترل‌ها، انتخاب‌گرها، لغزنده‌ها، چک‌لیست‌ها و سناریوهای مرحله‌ای.
- Visual layer: نمودارها، نقشه‌های مفهومی، تصویرهای درخواستی و پیش‌نمایش‌های روشن.
- Experiment layer: هدف، فرضیه، پارامترها، ورودی، خروجی، معیار پذیرش و نتیجه.
- Behavior layer: زوج‌های IN/OUT، ردیابی رفتار، خطاها، اصلاح‌ها و بازخورد.
- Evidence layer: منابع، commitها، آزمون‌ها، پیوندها و وضعیت هر ادعا.
- Recovery layer: CURRENT/NEXT، master reference، crosswalk و آزمون cold-start.
- Governance layer: Master/Child/Rahm و ارتقای نسخه‌دار بر پایهٔ شواهد.

## Acceptance gates / دروازه‌های پذیرش
A. مقصد و مسیر فایل معلوم باشد.
B. شناسهٔ پایدار، نسخه، منشأ و وضعیت موجود باشد.
C. معیار پذیرش قبل از ادعای موفقیت تعریف شود.
D. نتیجه و شواهد آزمون ثبت شود.
E. بازخوانی مستقل و تطبیق انجام شود.
F. پیوندهای مرجع و مسیر بازیابی بررسی شوند.
G. مقصدهای تأییدنشده صریحاً NOT VERIFIED بمانند.

## Baseline and open work
- This project-zero baseline does not close historic census Issue #21, runtime/cold-start Issue #20, NEXT-036, NEXT-035, or other prior open tasks.
- First product build remains pending: choose one small interactive experience, define I/O and acceptance criteria, implement/assemble, test, record evidence and read back.
- Fresh-session/cold-start recovery for this new branch remains NOT RUN until actually performed.
- GitHub repository registration is the only destination covered by this operation; Buffer/Persistent Memory/Library are NOT VERIFIED and Dropbox remains OPEN / NOT VERIFIED.

## Return path
Start from CURRENT-038 → NEXT-037 → first interactive prototype → test evidence → read-back/reconcile → Rahm review → versioned master update.


## Final read-back receipt — Project Zero
- Status: READ-BACK VERIFIED / CONTENT PRESENT / IDENTIFIERS MATCHED.
- Verification: this exact path was fetched again after write; expected project-zero identifiers and relevant cross-links were present in the repository.
- Scope: repository file presence and text/link checks only. Prototype build and cold-start recovery remain OPEN / NOT RUN; other destinations remain independently unverified.
- Canonical timestamp: use the actual last-change Git commit timestamp in UTC; Tehran equivalent is UTC+03:30 from that same instant. User-message timestamp remains UNKNOWN / UNVERIFIED.
