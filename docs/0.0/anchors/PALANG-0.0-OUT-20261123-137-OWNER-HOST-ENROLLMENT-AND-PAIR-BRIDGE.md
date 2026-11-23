# OUT-137 — خروجی مالک: طراحی پل جفتی و مسیر کم‌اصطکاک میزبان

- Input: [IN-138](PALANG-0.0-IN-20261123-138-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Bridge: [BRIDGE-0138](PALANG-0.0-BRIDGE-20261123-0138-IN-138-OUT-137.md)
- Event: [EVT-0325](../../architecture/BEHAVIOR-TRACE/EVT-0325-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE-2026-11-23.md)
- Current candidate: CURRENT-150.05
- Sole queue candidate: NEXT-051.05
- Status: ACTIVE / LIVING / IMPLEMENTATION-IN-PROGRESS

## 1. تصمیم معماری

پیشنهاد مالک دربارهٔ پل مستقل بین هر ورودی و خروجی پذیرفته شد. از این پس هر تعامل پروژه‌ای باید یک جفت IN/OUT و یک Bridge record مستقل داشته باشد:
POINT-0/GOLDEN → prior CURRENT/queue → IN-N → BRIDGE-N → OUT-N → EVT → TIME-BINDING → CURRENT revision → same NEXT queue revision.
شناسهٔ Bridge، شمارهٔ IN و OUT را صریحاً به هم متصل می‌کند. Bridge باید به والد قبلی و checkpoint/صف بعدی نیز ارجاع دهد. این یک لایهٔ ردیابی است، نه ریشه یا صف موازی.

## 2. تصمیم اتصال میزبان تازه

- مخزن مادر Public است؛ برای READ/clone/fetch عمومی نیازی به عضویت یا OAuth نیست.
- میزبان جدید ابتدا با یک پیام واحد، آدرس مخزن و دستورالعمل ورود را می‌خواند و exact main HEAD و blob SHA اسناد کلیدی را گزارش می‌کند.
- شناسهٔ خودساختهٔ میزبان فقط HOST-CLAIM-ID موقت است و هویت یا ثبت رسمی محسوب نمی‌شود.
- میزبان باید یک challenge یک‌بارمصرف مالک را در رسید خود بازتاب دهد؛ اگر runtime از کلید عمومی/امضای دیجیتال پشتیبانی کند، proof-of-possession با کلید موقت میزبان افزوده می‌شود. نبود این قابلیت با عنوان UNVERIFIED CLAIM ثبت می‌شود، نه شکست READ عمومی.
- مالک پس از بررسی رسید، هویت/منشأ و قابلیت‌های واقعی، Host ID رسمی را صادر می‌کند.
- عضویت AI host به‌عنوان collaborator در مخزن مادر ممنوع است. میزبان هرگز MASTER/main یا RAHM را نمی‌نویسد/نمی‌خواند.
- فضای کاری خصوصی باید در runtime میزبان واقعاً جدا و پایدار باشد یا در یک private repository اختصاصی که مالک provision کرده است. دسترسی نوشتن، اگر لازم شد، فقط از broker/GitHub App محدود به همان repo و بدون افشای token به مدل انجام می‌شود.
- مسیر سادهٔ اولیه: PUBLIC READ → HOST RECEIPT → OWNER REVIEW → OFFICIAL HOST ID → PRIVATE WORKSPACE. تا قبل از ایجاد سرویس مستقل، write-back از طریق export مالکانه و نه credential میزبان انجام می‌شود.

## 3. کارهای بررسی‌شده

1. وضعیت واقعی شاخهٔ کاری و PR #145 بازخوانی شد؛ شاخهٔ chat-point0-continuation-20261123 در commit caa36bc5abcfd0ee86736d47e6d3460c0fa5d610 بود و PR #145 باز و ادغام‌نشده بود.
2. دریافت شد که .03 و .04 قبلاً در همان PR ثبت شده‌اند؛ از ساختن شماره‌های تکراری اجتناب شد و revision بعدی به‌صورت افزایشی زیر همان خانواده در نظر گرفته شد.
3. ده Issue #114–#123 بررسی شدند؛ هر ده هنوز OPEN هستند. ترتیب وابستگی‌ها حفظ شد.
4. Issue #20: آزمون‌های runtime محلی، fixtureهای جفت IN/OUT و تطبیق زنجیره قبلاً PASS شده‌اند؛ capture خودکار پیام زنده، persistence، restart و بازیابی میزبان مستقل هنوز اثبات نشده‌اند.
5. Issue #21: inventory کامل مسیرهای درخت main با 6,716 ورودی و 644 مسیر در خانواده‌های هدف ثبت شده؛ 21 گروه basename تکراری (17 گروه دارای blob متفاوت و 4 گروه byte-identical) شناسایی شده؛ 9 گروه بررسی محتوایی اولیه دارند؛ بقیهٔ تطبیق معنایی باز است.
6. پل و پروتکل enrollment در این revision به‌صورت سند اجرایی مستقل افزوده می‌شوند؛ این ثبت به‌تنهایی میزبان واقعی را provision یا فعال نمی‌کند.

## 4. وضعیت پذیرش

- ثبت IN/OUT/Bridge/Event/Current/Next و read-back فایل‌ها: در همین PR candidate و پس از commit باید تأیید شود.
- exact-SHA CI برای این revision: PENDING تا اجرای خودکار workflowها روی آخرین head.
- Golden merge و main publication: NOT DONE؛ نیازمند مسیر owner-controlled.
- GitHub App/OAuth، private Partner hosting، private RAHM، API key، MCP endpoint: NOT PROVISIONED.
- میزبان مستقل و restart recovery: NOT RUN.
- هر ده Partner issues و Issue #20/#21: OPEN.

## 5. تعهد گزارش بعدی

در پاسخ «چکار کردی؟» تعداد موارد زیر جداگانه اعلام شود: انجام‌شده با شاهد؛ ناقص/منتظر آزمون؛ متوقف‌شده در مرز ابزار/حساب؛ اقدام دقیق لازم از مالک؛ و پیشنهادهایی که برای هدف فعلی غیرضروری تشخیص داده و از مسیر اصلی کنار گذاشته شده‌اند.
