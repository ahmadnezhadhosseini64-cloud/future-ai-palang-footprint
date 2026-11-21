# POINT-0/072 — تأیید مالک و اتصال امن GitHub (0++)

- Parent: canonical POINT-0/071; 0+ و 0++ فقط نشانگر روی همان ریشهٔ canonical هستند، نه ریشهٔ جدید.
- Input: IN-115
- Output: OUT-114
- Event: EVT-0291
- Time binding: TIME-BINDING-EVT-0291
- Current: CURRENT-125
- Sole active queue: NEXT-051
- Status: PROPOSED / HOST-INTAKE BRANCH / NOT MERGED / PACKAGE BUILD PENDING / HOST ACCEPTANCE NOT RUN

## هدف
هر میزبان جدیدی که سند مادر یا ZIP را دریافت می‌کند، پیش از هر عملیات GitHub عبارت تأیید مالک «احمد نژادحسینی» را درخواست کند؛ سپس احراز هویت واقعی GitHub را فقط از طریق OAuth/connector رسمی همان میزبان انجام دهد.

## تصمیم امنیتی
عبارت مذکور در سند و ZIP قابل مشاهده است؛ بنابراین رمز یا اثبات هویت نیست و هیچ مجوز مخزنی ایجاد نمی‌کند. این عبارت فقط گیت مکالمه‌ای برای تأیید قصد کاربر است. حساب GitHub متصل‌شده باید با مالک مورد انتظار `ahmadnezhadhosseini64-cloud` تطبیق داده شود. دسترسی اولیه READ-ONLY است. هرگونه نوشتن نیازمند broker/worker کم‌مجوز، host-intake، quarantine، PR بازبینی‌شده توسط مالک و read-back است. هرگز رمز/PAT/Secret را در چت نخواه.

## تحویل
قرارداد کامل در `prototype/haif-gpt6-starter/OWNER-CONFIRMATION-AND-GITHUB-AUTHORIZATION-CONTRACT.md` و متن bootstrap و دستورالعمل میزبان به‌روزرسانی شده‌اند. سند مادر به v1.7.79 ارتقا یافته است. بستهٔ ZIP هنوز بازسازی و تأیید نشده؛ میزبان مستقل نیز هنوز آزموده نشده است.

## لنگر زمانی
- مشاهدهٔ ساعت محیط: 2026-11-21 09:32 Asia/Tehran / 06:02 UTC.
- زمان دقیق ارسال پیام کاربر: UNKNOWN / UNVERIFIED.
- زمان commit نهایی این شاخه: باید از GitHub پس از ثبت و read-back استخراج شود؛ زمان مشاهده جایگزین آن نیست.
