# IN-116 — ورودی معماری POINT-0++

- Parent: POINT-0/072 → CURRENT-125.
- Continuation: POINT-0/073 / POINT-0++.
- Owner intent: میزبان اول با دریافت متن سند مادر بتواند مخزن را فقط بخواند، محیط کاری محدود خود را از نسخهٔ معتبر به‌روز کند و فقط وظایف تعریف‌شدهٔ مالک را اجرا کند.
- Host role: FIRST NEW HOST / FIRST_HOST / HOST-001.
- Authentication gate: OPEN / DEFERRED.
- Repository write: DENIED.
- Workspace execution: OWNER-DEFINED / ALLOWLISTED ONLY.
- Exact user-message time: UNKNOWN / UNVERIFIED.

## ورودی
اتصال GitHub به‌تنهایی هدف نیست. میزبان باید سند مادر ارسالی را بخواند، به مخزن canonical وصل شود، HEAD و manifest را بررسی کند، snapshot محلی را تطبیق دهد، workspace واقعی و محدود را طبق سیاست مالک به‌روز کند و فقط taskهای مجاز را انجام دهد.

## محدودیت
میزبان حق تغییر مخزن، انتشار، مدیریت دسترسی، تغییر قواعد مرجع، گسترش ابزارها یا انتقال خروجی workspace به مخزن را ندارد. متن سند به‌تنهایی sandbox، ACL یا workspace پایدار ایجاد نمی‌کند؛ اگر پلتفرم کنترل فنی ندارد، اجرا BLOCKED / NOT SUPPORTED است.

## قرارداد
[FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md).
