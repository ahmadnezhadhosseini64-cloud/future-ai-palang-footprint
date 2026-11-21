# POINT-0/080 — دسترسی عمومی میزبان بدون OAuth برای خواندن مخزن

- Stable ID: HAIF-POINT-0-080-PUBLIC-READ-NO-OAUTH-2026-11-21
- Status: ACTIVE / LIVING / OWNER-DIRECTED
- Parent: POINT-0/079 → CURRENT-132 → NEXT-051
- Owner: احمد پلنگ
- Project timezone: Asia/Tehran (+03:30)
- Exact owner-message timestamp: UNKNOWN / UNVERIFIED

## قصد مالک
مالک تأکید کرد مخزن شخصی GitHub او عمداً Public است تا میزبان تازهٔ هوش مصنوعی بتواند با کمترین مانع وارد منبع شود. میزبان باید به‌عنوان عامل اجرایی قابل‌تعویض در محیط کاری خودش فعالیت کند؛ مالکیت ساختمان و معماری MASTER نزد مالک باقی می‌ماند.

## تصمیم
- READ/clone/fetch عمومی مخزن Public با HTTPS بدون OAuth ممکن است؛ میزبان باید این مسیر را اول امتحان کند.
- OAuth برای مشاهده و دریافت عمومی پیش‌شرط نیست.
- OAuth یا credential امن معادل فقط برای write-back احراز‌شده یا منابع خصوصی لازم است.
- EXECUTE و WORKSPACE قابلیت‌های مستقل sandbox میزبان‌اند؛ عمومی بودن repo یا تأیید مالک آن‌ها را ایجاد نمی‌کند.
- WRITE اختیاری است؛ patch محلی و تحویل به مالک می‌تواند بدون OAuth انجام شود. نوشتن مستقیم به GitHub نیازمند مجوز واقعی و branch اختصاصی است.
- هیچ میزبان حق push مستقیم به main، تغییر MASTER یا ارتقای خودکار دانش را ندارد.
- Public یعنی محتوای مخزن برای عموم قابل مشاهده است؛ هیچ secret یا دادهٔ حساس نباید در آن قرار گیرد.

## زنجیره
POINT-0/079 → CURRENT-132 → POINT-0/080 → IN-123 → OUT-122 → EVT-0300 → TIME-BINDING-EVT-0300 → CURRENT-133 → NEXT-051

## منابع
- [معماری دسترسی عمومی مخزن و ورود کم‌اصطکاک میزبان](../../architecture/مدل%20اولیه%20AI/معماری%20دسترسی%20عمومی%20مخزن%20و%20ورود%20کم‌اصطکاک%20میزبان.md)
- [دستور واحد ورود میزبان](../../../prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md)
- [سند مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## وضعیت پذیرش
معماری ثبت‌شده است. آزمون میزبان تمیز، clone عمومی از نشست مقصد، اجرای بسته، persistence و restart هنوز OPEN / NOT RUN هستند.
