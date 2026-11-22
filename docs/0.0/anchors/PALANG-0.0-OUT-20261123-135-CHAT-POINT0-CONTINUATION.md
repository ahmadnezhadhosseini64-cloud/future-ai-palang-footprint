# OUT-135 — تصمیم و برنامهٔ اجرایی یار پلنگ

- Stable family: POINT-0/GOLDEN → CURRENT-150 → NEXT-051
- Parent accepted revision: CURRENT-150.02 / NEXT-051.02
- Input: [IN-136](PALANG-0.0-IN-20261123-136-CHAT-POINT0-CONTINUATION.md)
- Owner: @ahmadnezhadhosseini64-cloud
- Status: ACTIVE / LIVING / EXECUTION-IN-PROGRESS

## تصمیم معماری

این تعامل به‌عنوان یک نشانگر ادامهٔ نقطهٔ صفر روی همان ریشهٔ canonical ثبت می‌شود. هیچ POINT-0 root، Golden baseline، CURRENT family یا NEXT queue جدیدی ساخته نمی‌شود. تمام نقاط قبلی از طریق اسناد مرجع و زنجیرهٔ جاری حفظ می‌شوند.

## تصمیم نسخه و بسته

سند مادر Golden نسخهٔ 1.8.4 مرجع جاریِ خوانده‌شده است. بستهٔ قابل‌حمل، manifest، mirror، آزمون و receipt باید به همین منبع و زنجیرهٔ جاری متصل شوند. هیچ downgrade یا بازنویسی تاریخچه‌ای مجاز نیست. پذیرش بسته تنها با آزمون exact-SHA، digest، inventory، استخراج، آزمون‌های استخراج‌شده، artifact round-trip و read-back مستقل قابل اعلام است.

## مسیر اجرا

1. ثبت ورودی، تصمیم و رویداد در زنجیرهٔ جاری.
2. ثبت timestamp رویداد از Git commit metadata واقعی.
3. ایجاد revision افزایشی CURRENT-150.03 و NEXT-051.03 بدون تغییر هویت‌های ثابت.
4. اتصال نشانگر جدید به POINT-0/GOLDEN، CURRENT-150.02 و تمام تاریخچهٔ قبلی از طریق شاخص‌ها و سند مادر.
5. ممیزی و پیشبرد تمام کارهای قابل‌انجام در صف موجود، به‌ویژه ده پروندهٔ Partner #114–#123 و Issues #20/#21.
6. حفظ main/MASTER بدون نوشتن مستقیم؛ هر انتشار یا promotion فقط از مسیر کنترل‌شده و با گیت‌های واقعی.
7. بازخوانی فایل‌های تغییرکرده و ثبت دقیق نتیجهٔ آزمون‌ها و موانع واقعی.

## مرز ادعا

این تصمیم به‌تنهایی به معنی انجام آزمون، انتشار Release، provision سرویس خصوصی، ثبت GitHub App/OAuth/MCP، فعال‌شدن Host، یا بازیابی مستقل نیست. هرکدام فقط با شاهد مقصدی و read-back همان گیت قابل پذیرش‌اند.

## اتصال زنجیرهٔ جاری و read-back

- ریشهٔ یگانه: [POINT-0/GOLDEN](GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md)
- ورودی: [IN-136](PALANG-0.0-IN-20261123-136-CHAT-POINT0-CONTINUATION.md)
- خروجی: [OUT-135](PALANG-0.0-OUT-20261123-135-CHAT-POINT0-CONTINUATION.md)
- رویداد: [EVT-0323](../../architecture/BEHAVIOR-TRACE/EVT-0323-CHAT-POINT0-CONTINUATION-2026-11-23.md)
- زمان رویداد: [TIME-BINDING-EVT-0323](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0323-CHAT-POINT0-CONTINUATION-2026-11-23.md)
- بازبینی جاری: [CURRENT-150.03](PALANG-0.0-CURRENT-20261123-150-REVISION-03-CHAT-POINT0-CONTINUATION.md)
- صف یگانه: [NEXT-051.03](PALANG-0.0-NEXT-20261123-051-REVISION-03-EXECUTION-CONTINUATION.md)
- سند مادر: [سند مرجع مادر مدل اولیه هوش مصنوعی](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- قرارداد بازیابی مستقل: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../portable/RAHM/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- قرارداد بستهٔ میزبان: [INDEPENDENT_HOST_RECOVERY_PROTOCOL](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Manifest: [EXPORT_MANIFEST](../../portable/RAHM/EXPORT_MANIFEST.json)
- نشانگر این گفتگو: [POINT-0-GOLDEN-CHAT-CONTINUATION-2026-11-23-001](POINT-0-GOLDEN-CHAT-CONTINUATION-2026-11-23-001.md)
- Mirror event: [EVT-0241](../../architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md)
- Mirror time binding: [TIME-BINDING-EVT-0241](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md)

