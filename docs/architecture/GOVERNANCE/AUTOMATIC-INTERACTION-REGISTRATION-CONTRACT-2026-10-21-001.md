# قرارداد حاکم ثبت خودکار همهٔ ورودی‌ها و خروجی‌های تعامل

- Stable ID / شناسهٔ پایدار: `AUTOMATIC-INTERACTION-REGISTRATION-CONTRACT-2026-10-21-001`
- Production ID / شناسهٔ تولید: `AIRC-2026-10-21-001`
- Version / نسخه: 1.0.0
- Owner / مالک: احمد پلنگ (Ahmad Nezhadhosseini)
- Project / پروژه: Future AI / Palang Footprint / HAIF
- Status / وضعیت سیاست: ACTIVE / LIVING / GOVERNING
- Runtime enforcement status / وضعیت اجرای خودکار واقعی: OPEN / NOT YET PROVEN
- Canonical repository: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`
- Related standard: [Assistant Timestamp Anchor Standard](ASSISTANT-TIMESTAMP-ANCHOR-STANDARD-2026-10-21-001.md)
- Related event: [EVT-0073](../BEHAVIOR-TRACE/EVT-0073-AUTOMATIC-INTERACTION-REGISTRATION-CONTRACT-2026-10-21.md)
- Governing master: [Permanent Interaction Anchoring and Timestamp Governance](../../reference/REFERENCE-DOCUMENTS/PERMANENT-INTERACTION-ANCHORING-TIMESTAMP-GOVERNANCE-AND-CANONICAL-GRAPH-MASTER-REFERENCE-2026-10-21-001.md)

## 1. کاربر چه می‌خواهد و این قرارداد چه چیزی را الزام می‌کند
هر پیام ورودی کاربر و هر خروجی دستیار، از لحظهٔ شناسایی رویداد، باید بدون نیاز به فرمان «ثبت کن» وارد زنجیرهٔ ثبت شود. «ثبت کن» به معنی اجرای کامل‌تر و رسیدگی ویژه به یک مورد است، نه کلید روشن‌کردن اصل ثبت. سکوت کاربر دربارهٔ ثبت، معافیت ایجاد نمی‌کند.

## 2. زنجیرهٔ اجباری برای هر ورودی و خروجی
`CAPTURE → BIND → ANCHOR → CLASSIFY → PRESERVE → LINK → WRITE → READ-BACK → MATCH → VERIFY → STATUS`

معنی: دریافت → پابند/شناسه‌گذاری → لنگرگذاری → طبقه‌بندی → حفظ → پیونددهی → نوشتن → بازخوانی → تطبیق → تأیید → تعیین وضعیت.

هر رویداد باید:
1. شناسهٔ مستقل و غیرمبهم داشته باشد؛ شناسهٔ رویداد از شمارهٔ کوتاه EVT به‌تنهایی ساخته نشود.
2. به یک زمان UTC معتبر و منشأدار برای عملیات ثبت متصل شود. زمان پیام کاربر، زمان پردازش، زمان commit، زمان بازخوانی و زمان مقصدها فیلدهای مستقل‌اند.
3. زمان متناظر تهران را با `Asia/Tehran (+03:30)` تنها در صورت تبدیل معتبر ثبت کند؛ UTC مرجع اصلی است.
4. ورودی یا خروجی خام/مرجع، نقش پیام، خلاصهٔ وفادار، طبقه، منشأ، والد/فرزند، پیوندهای مرتبط، نسخه، وضعیت، شواهد، محدودیت‌ها، مقصدها و اقدام بعدی را ثبت کند.
5. اگر زمان پیام، محتوای خام، مقصد یا ابزار ثبت در دسترس نیست، کمبود را صریح با `UNKNOWN / UNAVAILABLE / NOT CAPTURED` ثبت کند؛ هرگز مقدار نسازد.
6. سند مرجع کامل تولید کند وقتی رویداد بر تصمیم، معماری، شکاف، آزمون، بازیابی یا تداوم اثر دارد. برای پیام‌های عادی کم‌اهمیت، رویداد می‌تواند در دفتر فشرده ثبت شود، اما شناسه، زمان، منشأ، متن/ارجاع قابل‌بازیابی و پیوند زنجیره حذف نشود. اصل پیش‌فرض حفظ همه است؛ فشرده‌سازی جای حذف را نمی‌گیرد.
7. پس از نوشتن، همان مقصد را بازخوانی و تطبیق کند. «قصد ثبت» یا موفقیت مقصد دیگر، شاهد ثبت این مقصد نیست.
8. وضعیت هر مقصد را جدا ثبت کند: Repository، Buffer، Library، Persistent Memory، Dropbox و runtime/session host.

## 3. قواعد پابند و چکش
- هر ورودی/خروجی باید قبل از تحلیل محتوایی به event envelope (پوشش رویداد) متصل شود؛ اگر پلتفرم اجازهٔ نوشتن پیش از پاسخ را نمی‌دهد، ثبت با وضعیت `CAPTURED-IN-SESSION / DURABLE-WRITE-PENDING` علامت‌گذاری شود.
- رویدادهای مهم به سند مرجع جامع و صف/معماری مرتبط متصل شوند؛ تغییر معماری باید به Master، index، event log و integration queue پیوند داده شود.
- اجرای چکش برای هر رویداد شامل: شناسهٔ یکتا، زمان و منبع، completeness، پیوند والد/فرزند، تکراری/برخورد، موفقیت نوشتن، read-back، مقصد مستقل و وضعیت واقعی.
- تکرار محتوا نباید رویداد مستقل را محو کند؛ رویدادها می‌توانند به یک محتوای canonical مشترک ارجاع دهند.
- اطلاعات حساس/غیرمجاز نباید بی‌قید در مخزن عمومی نوشته شود. سیاست ثبت باید حداقل‌سازی داده، مجوز، نگهداشت و حذف قانونی را رعایت کند؛ در چنین مواردی ثبت امنِ فراداده/ارجاع جایگزین انتشار متن حساس می‌شود.

## 4. مرز مهم میان سیاست و خودکارسازی واقعی
ثبت این قرارداد در مخزن، به‌خودی‌خود اتصال به جریان پیام‌های ChatGPT یا ثبت خودکار هر پیام را ایجاد نمی‌کند. GitHub Actions که با push، زمان‌بندی یا اجرای دستی شروع می‌شود فقط مخزن را می‌بیند؛ به ورودی/خروجی زندهٔ این گفتگو دسترسی ذاتی ندارد. برای خودکارسازی سرتاسری لازم است Host Adapter / integration واقعی پیام را به event-capture endpoint یا durable queue تحویل دهد، نتیجه را دریافت کند و retry/idempotency داشته باشد.

تا زمانی که آزمون runtime با پیام ورودی واقعی و خروجی واقعی، restart/recovery و read-back مستقل پاس نشده است، وضعیت اجرا `OPEN / NOT PROVEN` می‌ماند. دستیار نباید ادعا کند هر پیام در پس‌زمینه به GitHub/Buffer/Memory/Dropbox نوشته شده، مگر مدرک مقصدی وجود داشته باشد.

## 5. طراحی Host Adapter موردنیاز
ورودی حداقل:
- `event_id`, `event_type` (USER_INPUT / ASSISTANT_OUTPUT), `conversation_scope`, `content_or_secure_reference`
- `user_message_time` (اگر منبع معتبر دارد، وگرنه UNKNOWN)
- `assistant_processing_time_utc`, `timezone_source`, `event_time_precision`
- `parent_event_id`, `stable_id`, `production_id`, `version`
- `sensitivity_class`, `retention_policy`, `destination_policy`

مراحل Host Adapter:
1. گرفتن رویداد از میزبان مجاز؛
2. ایجاد شناسهٔ مستقل و idempotency key؛
3. ثبت در صف پایدار محلی/سروری؛
4. نوشتن در Repository یا مقصد مجاز؛
5. خواندن مجدد و تطبیق hash/فیلدهای کلیدی؛
6. ثبت زمان commit/read-back واقعی و نتیجه؛
7. retry امن پس از قطع؛
8. بازیابی پس از restart و جلوگیری از حذف/ثبت تکراری؛
9. گزارش جداگانهٔ موفقیت/شکست هر مقصد؛
10. انتقال خطا به integration queue با next action.

## 6. آزمون‌های پذیرش اجباری
- AIRC-T01: ورودی کاربر واقعی با شناسه و زمان ثبت شود.
- AIRC-T02: خروجی دستیار واقعی به رویداد ورودی پیوند بخورد.
- AIRC-T03: UTC و زمان تهران از یک instant واقعی منطبق باشند.
- AIRC-T04: قطع شبکه/میزبان، سپس restart و بازیابی بدون فقدان.
- AIRC-T05: idempotency؛ retry موجب حذف یا تکثیر معنایی نشود.
- AIRC-T06: read-back از همان مقصد و hash/content match.
- AIRC-T07: دسترسی و حداقل‌سازی داده آزموده شود.
- AIRC-T08: شش سند واقعی از چرخهٔ ورودی تا خروجی بازیابی شوند.
- AIRC-T09: Repository، Buffer، Library، Persistent Memory و Dropbox جداگانه PASS/BLOCKED/NOT TESTED شوند.
- AIRC-T10: اجرای بدون گفتن «ثبت کن» ثابت شود.
تا زمانی که هر آزمون اجرا و شاهدش ثبت نشده، وضعیتش `NOT RUN` یا `BLOCKED` است، نه PASS.

## 7. وضعیت فعلی و اقدام بعدی
- Policy / سیاست: ACTIVE / LIVING / GOVERNING.
- Repository contract/event integration: باید با read-back و اجرای ممیزی پس از ثبت تأیید شود.
- Live automatic capture of every user/assistant message: OPEN / NOT PROVEN.
- Buffer, Library, Persistent Memory, Dropbox: مستقل و UNVERIFIED مگر آزمون اختصاصی.
- Next action: پیوند این قرارداد به استاندارد زمان، سند مرجع مادر، نمایه و صف؛ سپس ساخت/اتصال Host Adapter و اجرای AIRC-T01 تا AIRC-T10.
