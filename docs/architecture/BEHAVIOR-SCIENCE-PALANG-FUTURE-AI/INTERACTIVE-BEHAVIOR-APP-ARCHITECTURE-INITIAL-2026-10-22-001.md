# معماری اولیه اپ — رفتارشناسی تعاملی پلنگ و آینده AI

## شناسنامه
- Stable ID / شناسه پایدار: PALANG-INTERACTIVE-BEHAVIOR-SCIENCE-APP-ARCHITECTURE-2026-10-22-001
- Production ID / شناسه تولید: IBSA-HAIF-2026-10-22-001
- Version / نسخه: 0.1.0 — طرح اولیه قابل تکامل
- Status / وضعیت: ACTIVE / LIVING / INITIAL DESIGN — فعال، زنده، طرح اولیه
- Project / پروژه: Future AI / Palang Footprint — آینده AI / ردپای پلنگ
- Parent event / رویداد مادر: [EVT-0051](../BEHAVIOR-TRACE/EVT-0051-GMAIL-ACCESS-CLAIM-AND-LIVING-0.0-ANCHOR-2026-10-22.md)
- Master reference / سند مرجع مادر: [GACIB](../../reference/REFERENCE-DOCUMENTS/GMAIL-ACCESS-CLAIM-AND-INTERACTION-BEHAVIOR-LIVING-MASTER-REFERENCE-2026-10-22-001.md)
- 0.0 anchor / لنگر صفر: [GACIB 0.0](../../0.0/anchors/PALANG-0.0-GMAIL-ACCESS-CLAIM-INTERACTION-BEHAVIOR-2026-10-22-001.md)

## 1. هدف محصول
ساخت یک اپ/سامانه ثبت و تداوم تعامل انسان–AI که ورودی‌ها، خروجی‌ها، تصمیم‌ها، ادعاها، شواهد، محدودیت ابزار، زمان‌ها، لنگرهای مستقل و تغییرات معماری را با شناسه‌های قابل بازیابی نگه دارد. هدف صرفاً نگهداری متن گفتگو نیست؛ هدف، تداوم کار و قابلیت بازسازی وضعیت با منشأ و شواهد است.

## 2. اصول طراحی
1. Evidence before status / شاهد پیش از وضعیت.
2. Preserve claim and provenance / حفظ ادعا و منشأ.
3. Separate event clock from repository clock / جداسازی زمان رویداد از زمان مخزن.
4. No fabricated timestamps or identity fields / عدم ساخت زمان یا اطلاعات هویتی.
5. Destination-specific verification / راستی‌آزمایی مستقل هر مقصد.
6. Append-only anchors / لنگرهای افزایشی؛ نقاط ۰.۰ قبلی حذف نشوند.
7. Read-back is mandatory / بازخوانی پس از نوشتن الزامی.
8. Open gaps remain visible / شکاف‌های باز پنهان نشوند.
9. Human-confirmed sensitive actions / اقدامات حساس بیرونی مانند ارسال ایمیل فقط با گیرنده/محتوای روشن و دسترسی مجاز.
10. Model behavior only from observable evidence / مدل رفتار فقط از شواهد قابل مشاهده، نه ادعای دسترسی به تفکر پنهان.

## 3. اجزای اصلی
- Interaction Capture / دریافت تعامل: ثبت ورودی کاربر و خروجی قابل مشاهده دستیار.
- Event Ledger / دفتر رویداد: شناسه یکتا، نوع رویداد، منشأ، نسخه و ارتباطات.
- Temporal Anchor Service / سرویس لنگر زمانی: UTC مرجع مخزن از commit واقعی؛ زمان تهران مشتق‌شده؛ زمان پیام/ابزار جداگانه با منبع.
- Claim & Evidence Registry / ثبت ادعا و شاهد: هر گزاره با برچسب user-claim، tool-evidence، verified, unknown یا disputed.
- Capability Registry / ثبت توانایی مقصد: وضعیت واقعی اتصال Gmail/Dropbox/Library و غیره، همراه شاهد و زمان بررسی.
- Reference Vault / خزانه اسناد مرجع: اسناد مادر، نسخه‌ها، شناسه‌ها و پیوندهای بازیابی.
- Recovery Orchestrator / هماهنگ‌کننده بازیابی: بازخوانی، تطبیق، رفع تعارض، ادامه کارهای باز.
- Destination Adapters / رابط‌های مقصد: GitHub، Gmail، Dropbox، Library، Buffer، Persistent Memory؛ هرکدام وضعیت و اثبات جداگانه.
- Architecture Evolution Queue / صف تکامل معماری: ایده‌های تازه، شکاف‌ها، آزمون‌ها، تصمیم‌ها و وضعیت جذب.
- Audit & Read-back / ممیزی و بازخوانی: ثبت نتیجه واقعی هر مرحله.
- User Interface / رابط کاربر: نمایش ورودی، خروجی، زمان‌ها، شناسه‌ها، شاهدها و وضعیت هر مقصد.

## 4. مدل داده پیشنهادی
هر رویداد حداقل این فیلدها را دارد:
`event_id, stable_id, production_id, version, event_type, user_input, assistant_output, claims[], evidence[], timestamps{user_message_utc, tool_check_utc, repository_commit_utc, tehran_derived}, timezone, location_provenance, destination_statuses[], parent_ids[], open_gaps[], next_action, readback_result, integrity_result`.

فیلدهای هویتی حساس مثل شماره تلفن فقط با منبع روشن و ضرورت واقعی ذخیره می‌شوند؛ فیلد نامعلوم با UNKNOWN ثبت می‌شود، نه با مقدار ساختگی.

## 5. چرخه اجرایی
CAPTURE → CLASSIFY → ASSIGN IDS → ATTACH PROVENANCE → CHECK CAPABILITY → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → UPDATE INDEX → REPORT → RESUME.
ترجمه: دریافت → دسته‌بندی → شناسه‌گذاری → اتصال منشأ → بررسی دسترسی → نوشتن → بازخوانی → تطبیق → تأیید → رفع تعارض → به‌روزرسانی نمایه → اعلام وضعیت → ادامه.

## 6. صفحات اصلی اپ
1. Live Interaction / تعامل زنده: آخرین ورودی و خروجی با وضعیت زمان و منشأ.
2. Event Timeline / خط زمانی رویدادها: رویدادهای مرتب‌شده با UTC و زمان محلی مشتق‌شده.
3. 0.0 Anchors / لنگرهای صفر: چندین نقطه شروع مستقل، باز و نسخه‌دار.
4. Reference Vault / خزانه مرجع: سند مادر، اسناد فرزند و گراف ارتباطات.
5. Capability & Destinations / توانایی و مقصدها: Gmail، مخزن، Dropbox و سایر مقصدها با وضعیت جدا.
6. Evidence Audit / ممیزی شواهد: ادعا در برابر شواهد قابل مشاهده.
7. Open Gaps / شکاف‌های باز: موانع، مالک اقدام و وضعیت.
8. Architecture Lab / آزمایشگاه معماری: ایده‌های جدید، فرضیه، آزمون و تصمیم ادغام.
9. Recovery Console / کنسول بازیابی: بازخوانی شناسه و ازسرگیری بدون حذف لنگرهای قبلی.
10. Export & Portability / خروجی و قابلیت انتقال: بسته قابل استخراج با فایل‌های Markdown/JSON و manifest، بدون ادعای ذخیره در مقصدی که تأیید نشده است.

## 7. معماری سطح بالا
Human / انسان
→ Interaction Capture / دریافت تعامل
→ Event & Evidence Ledger / دفتر رویداد و شواهد
→ Temporal Anchor / لنگر زمانی
→ Reference Graph / گراف اسناد مرجع
→ Destination Adapters / رابط‌های مقصد
→ Read-back & Audit / بازخوانی و ممیزی
→ Recovery & Evolution Queue / صف بازیابی و تکامل
→ UI + Export / رابط و خروجی قابل انتقال
Feedback / بازخورد انسان و آزمون‌ها به چرخه برمی‌گردد.

## 8. حالت‌های وضعیت
- CLAIMED / ادعاشده: از سوی کاربر یا دستیار گفته شده اما مستقل تأیید نشده.
- OBSERVED / مشاهده‌شده: ابزار یا منبع آن را برگردانده.
- WRITTEN / نوشته‌شده: عملیات نوشتن موفق اعلام شده.
- READ_BACK / بازخوانی‌شده: همان مقصد دوباره خوانده شده.
- MATCHED / تطبیق‌شده: شناسه و محتوای مورد انتظار دیده شده.
- VERIFIED / تأییدشده: شواهد کافی برای ادعای مشخص وجود دارد.
- BLOCKED / مسدود: دسترسی یا مجوز مانع است.
- UNKNOWN / نامعلوم: شاهد کافی وجود ندارد.
این وضعیت‌ها مترادف نیستند.

## 9. آزمون‌های پذیرش نسخه اولیه
- A1: هر رویداد شناسه یکتا دارد.
- A2: UTC مخزن از commit واقعی خوانده می‌شود؛ زمان تهران از همان لحظه مشتق می‌شود.
- A3: زمان پیام و مدت تفکر هرگز از زمان commit استنتاج نمی‌شوند.
- A4: پس از هر نوشتن، خواندن مجدد همان فایل/پیام انجام می‌شود.
- A5: هر مقصد وضعیت مستقل دارد.
- A6: ادعای کاربر بدون شاهد مستقل حذف یا به‌عنوان واقعیت قطعی بازنویسی نمی‌شود.
- A7: لنگر جدید، لنگر قبلی را نمی‌پوشاند.
- A8: خروجی قابل استخراج شامل سند مرجع، دفتر رویداد، نمایه، وضعیت مقصدها و کارهای باز است.
- A9: اطلاعات شخصی غایب حدس زده نمی‌شود.
- A10: هر خطای نوشتن/بازخوانی به‌صورت gap باز ثبت می‌شود.

## 10. مرز نسخه اولیه
این سند طرح معماری است، نه اپ اجرایی deployشده. هیچ رابط کاربری، پایگاه داده زنده، ارسال خودکار ایمیل یا اجرای پس‌زمینه با این فایل به‌تنهایی ایجاد نشده است. گام بعدی پس از تثبیت اسناد: تعریف JSON schema، نمونه داده واقعی با فیلدهای نامعلوم صریح، wireframe قابل آزمون، سپس پیاده‌سازی یک مسیر انتهابه‌انتها.

## 11. گام بعدی
- تثبیت اسناد در مخزن و بازخوانی مستقل.
- افزودن پیوند این پوشه به نمایه رفتارشناسی و سند مادر ادامه.
- باقی‌گذاشتن Gmail در وضعیت مسدود تا وقتی ابزار واقعی قابل استفاده شود؛ عدم جایگزینی خاموش Gmail با سرویس دیگری.
- بعد از دسترسی، آزمون انتهابه‌انتها: ثبت رویداد → ارسال مجاز → یافتن پیام ارسالی → تطبیق → ثبت شواهد.
