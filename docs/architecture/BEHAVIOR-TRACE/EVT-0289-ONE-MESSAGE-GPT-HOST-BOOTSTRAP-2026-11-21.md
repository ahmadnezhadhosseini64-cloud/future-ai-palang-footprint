# EVT-0289 — راه‌اندازی یک‌پیامی میزبان GPT و نقطه 0++

- Parent: OUT-113
- Status: REGISTERED / PACKAGE CI PENDING
- Point: POINT-0/071 (0++ marker on canonical point 0)
- Input: IN-114
- Output: OUT-113
- Previous checkpoint: CURRENT-123
- Next checkpoint: CURRENT-124
- Queue: NEXT-051

رویداد معماری: تبدیل قرارداد انتقال به یک پیام واحد قابل ارسال برای میزبان GPT جدید، شامل اتصال محدود به مخزن رسمی، خواندن pointer/receipt، بازیابی سند مادر و ZIP، آزمون مستقل بسته و ایجاد workspace خصوصی و شناسه‌دار برای همان میزبان. امنیت workspace واقعی باید از سطح sandbox/ACL بیاید؛ پوشه‌بندی در مخزن مشترک کافی نیست.

هیچ میزبان مقصد در این رویداد متصل یا فعال نشده است. این رویداد ثبت طراحی و source implementation است، نه رسید اتصال end-to-end.
