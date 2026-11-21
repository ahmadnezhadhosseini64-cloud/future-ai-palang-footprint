# OUT-122 — خروجی معماری: تفکیک READ عمومی از OAuth و WRITE

- Parent point: POINT-0/080
- Status: ARCHITECTURE-DECISION-RECORDED
- Source: IN-123
- Canonical architecture: [Public repository and low-friction host access](../../architecture/مدل%20اولیه%20AI/معماری%20دسترسی%20عمومی%20مخزن%20و%20ورود%20کم‌اصطکاک%20میزبان.md)

## نتیجه
1. مخزن Public است؛ بنابراین میزبان می‌تواند بدون OAuth با HTTPS عمومی آن را بخواند و clone/fetch کند.
2. OAuth برای READ عمومی لازم نیست.
3. OAuth یا credential امن فقط برای WRITE احراز‌شده یا دسترسی به دادهٔ خصوصی لازم است.
4. EXECUTE، workspace خصوصی/پایدار و restart به امکانات واقعی محیط مقصد وابسته‌اند.
5. تأیید مالک برای آغاز مراحل مجاز معتبر است؛ اما credential و امکانات میزبان را ایجاد نمی‌کند.
6. میزبان نقش عامل اجرایی موقت دارد؛ MASTER و حاکمیت پروژه در اختیار مالک باقی می‌ماند.
7. تغییرات پیشنهادی ابتدا در workspace/branch جدا و سپس از مسیر PR و تصمیم مالک بررسی می‌شوند.

## تفکیک نتیجه‌ها
- PUBLIC_SOURCE_RECOVERED: فایل‌های عمومی و exact HEAD خوانده شده‌اند.
- LOCAL_EXECUTION_VERIFIED: آزمون‌ها در محیط واقعی اجرا شده‌اند.
- WORKSPACE_READY: جداسازی و پایداری اثبات شده‌اند.
- HOST_RECOVERED: بازیابی مستقل و restart با رسید مستقیم میزبان ثابت شده است.
این وضعیت‌ها مترادف نیستند و نباید با یکدیگر ادغام شوند.

## موارد باز
آزمون clean-host، اجرای مقصد، workspace پایدار، restart و write-back احراز‌شده همچنان OPEN / NOT RUN هستند.
