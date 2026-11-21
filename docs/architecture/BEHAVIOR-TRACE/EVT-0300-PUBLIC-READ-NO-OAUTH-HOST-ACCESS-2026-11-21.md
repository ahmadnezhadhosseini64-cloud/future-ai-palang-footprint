# EVT-0300 — ثبت معماری دسترسی عمومی میزبان بدون OAuth

- Event ID: EVT-0300
- Project date: 2026-11-21
- Parent: POINT-0/080 → IN-123 → OUT-122
- Status: REGISTERED / ACTIVE
- Canonical architecture: [HAIF public repository access architecture](../مدل%20اولیه%20AI/معماری%20دسترسی%20عمومی%20مخزن%20و%20ورود%20کم‌اصطکاک%20میزبان.md)

## ثبت
تصمیم مالک برای استفاده از Public بودن مخزن به‌عنوان مسیر کم‌اصطکاک ورود میزبان ثبت شد. READ عمومی با HTTPS و clone/fetch ناشناس از OAuth مستقل است. OAuth فقط برای دسترسی خصوصی یا عملیات احراز‌شدهٔ نوشتن لازم می‌شود. محیط اجرای مستقل و workspace پایدار نیز قابلیت‌های جداگانهٔ میزبان هستند.

## زنجیرهٔ رویداد
POINT-0/079 → CURRENT-132 → POINT-0/080 → IN-123 → OUT-122 → EVT-0300 → TIME-BINDING-EVT-0300 → CURRENT-133 → NEXT-051

## محدودیت اثبات
ثبت این رویداد، پذیرش میزبان واقعی، ایجاد workspace، اجرای کد یا write-back را ثابت نمی‌کند. این گیت‌ها تا دریافت receipt مستقیم OPEN / NOT RUN می‌مانند.
