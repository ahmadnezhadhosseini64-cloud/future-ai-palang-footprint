# پیام اول مالک — اعلام مالکیت، خواندن مرجع عمومی و رسید شناسایی میزبان

- Stable ID: HAIF-OWNER-FIRST-MESSAGE-2026-11-25-001
- Version: 1.0.0
- Status: OWNER-APPROVED / PROPOSED FOR CANONICAL ADOPTION
- Stage: 1 — IDENTITY CLAIM + PUBLIC SOURCE READ + RECEIPT
- Owner declaration phrase: **احمد نژادحسینی**
- Canonical repository: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Canonical branch: main
- Governing root: POINT-0/GOLDEN
- Sole active queue: NEXT-051 (must be re-read from the live Reference Index)

---

## متن آمادهٔ ارسال به میزبان انتخاب‌شده

**میزبان هوش مصنوعی، پیش از هر اقدام ابتدا این عبارت مالکیت را عیناً اعلام کن:**

# احمد نژادحسینی

این عبارت، نام و اعلام مالکیت صاحب پروژه است. آن را در ابتدای پاسخ و در رسید شناسایی خود عیناً درج کن. این عبارت رمز عبور، عامل احراز هویت رمزنگاری‌شده یا مجوز دسترسی نیست؛ هیچ دسترسی خصوصی با گفتن آن ایجاد نمی‌شود.

من، مالک پروژه، تو را شخصاً برای بررسی اولیه انتخاب کرده‌ام. اکنون فقط مرحلهٔ اول ورود را انجام بده: منبع عمومی رسمی را بخوان، قابلیت‌های واقعی محیط خودت را گزارش کن و رسید شناسایی جامع بساز. **خودت را میزبان فعال، ثبت‌شده یا دارای مجوز خصوصی معرفی نکن. Host ID رسمی برای خودت نساز.**

### ۱. خواندن منبع رسمی

مخزن یگانه:
https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

1. شاخهٔ `main` را از منبع زنده بخوان و exact HEAD commit SHA را ثبت کن.
2. `docs/REFERENCE_INDEX.md` را بخوان؛ شمارهٔ CURRENT و NEXT را از همین شاخص و فایل‌های واقعی استخراج کن، نه از این پیام یا snapshot قدیمی.
3. POINT-0/GOLDEN، سند مادر جاری، CURRENT جاری و تنها NEXT فعال را از مسیرهای معرفی‌شده در شاخص بخوان.
4. سیاست میزبان‌ها و امنیت را از این مسیرها بخوان:
   - `docs/architecture/HOST-WORKSPACES/README.md`
   - `docs/architecture/HOST-SECURITY/OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOSITORIES.md`
   - `docs/architecture/HOST-REGISTRY/HOST-REGISTRY.json`
5. هر مسیر مفقود، ناسازگاری یا عدم امکان خواندن را صریحاً MISSING / CONFLICT / NOT AVAILABLE اعلام کن. مسیر را حدس نزن.
6. مخزن مادر فقط PUBLIC READ است. هیچ branch، PR، Issue، workflow، release، تنظیمات یا commit ایجاد نکن؛ هیچ credential یا secret درخواست نکن.

### ۲. شناسایی خود میزبان

فقط اطلاعاتی را اعلام کن که در همین محیط واقعاً قابل مشاهده یا آزمون است:
- نام سرویس/ارائه‌دهنده و مدل دقیق؛ اگر قابل مشاهده نیست UNKNOWN.
- نسخه یا شناسهٔ runtime؛ اگر قابل مشاهده نیست UNKNOWN.
- قابلیت‌های واقعی: public read، ابزار Git، اجرای کد، فایل‌سیستم، workspace پایدار، دسترسی connector؛ هر مورد VERIFIED / NOT AVAILABLE / NOT TESTED.
- آیا می‌توانی در همین نشست فایل یا خروجی را نگه داری؟ شواهد و محدودیت را بگو؛ ادعای persistence بدون آزمون ممنوع.
- روش خواندن مخزن: HTTPS عمومی، Git، connector یا روش دیگر.
- زمان واقعی و منطقهٔ زمانی، فقط اگر محیط آن را ارائه می‌دهد؛ در غیر این صورت UNKNOWN.

### ۳. رسید شناسایی اجباری

پاسخت را با عبارت **احمد نژادحسینی** آغاز کن و سپس رسیدی با این فیلدها بساز:

```text
OWNER_DECLARATION_PHRASE: احمد نژادحسینی
ENROLLMENT_STAGE: 1 — REQUESTED / NOT APPROVED
PROVIDER:
MODEL:
RUNTIME:
PROPOSED_HOST_LABEL: (پیشنهادی؛ نه Host ID رسمی)
SESSION_ID: (شناسهٔ موقت همین نشست؛ اگر نمی‌توانی بسازی UNKNOWN)
CANONICAL_REPOSITORY:
READ_METHOD:
BRANCH:
EXACT_HEAD_COMMIT_SHA:
REFERENCE_INDEX_READ: YES/NO
POINT_0_GOLDEN_READ: YES/NO
LIVING_MOTHER_READ: YES/NO
CURRENT_POINTER_AND_ID:
SOLE_NEXT_POINTER_AND_ID:
HOST_WORKSPACE_POLICY_READ: YES/NO
HOST_REGISTRY_READ: YES/NO
CAPABILITIES:
PERSISTENT_WORKSPACE: VERIFIED / NOT AVAILABLE / NOT TESTED
PRIVATE_REPOSITORY_ACCESS: NONE unless independently proven
MASTER_ACCESS: PUBLIC READ ONLY
WRITE_ATTEMPTS: NONE
TIME_AND_TIMEZONE: exact value or UNKNOWN
UNRESOLVED_MISSING_OR_CONFLICT:
EVIDENCE_LINKS_OR_READBACK:
LIMITATIONS:
HOST_SELF_ASSESSMENT: UNKNOWN / UNREGISTERED / NOT ACTIVE
NEXT_ACTION: return this receipt to the owner; wait
```

### ۴. پایان مرحلهٔ اول

- رسید را در همین پاسخ کامل و یک‌جا تحویل بده؛ سؤال اضافه برای شروع مرحلهٔ اول لازم نیست.
- هیچ Host ID رسمی، Workspace ID رسمی یا وضعیت ACTIVE صادر یا ادعا نکن.
- عبارت مالکیت را فقط به‌عنوان اعلام نام مالک درج کن؛ از مالک رمز، token، کد 2FA یا اطلاعات محرمانه نخواه.
- پس از تحویل رسید متوقف شو و منتظر تصمیم مالک بمان.
- مالک پاسخ تو را عیناً به ناظر معماری ارائه می‌کند. ناظر فقط شواهد قابل‌بررسی را تطبیق می‌دهد و نتیجه را به مالک اعلام می‌کند.
- فقط پس از بررسی رسید و تأیید صریح مالک، پیام دوم اختصاصی صادر می‌شود. خواندن مخزن عمومی یا درست گفتن نام مالک به‌تنهایی مجوز ورود نیست.

**قاعدهٔ قطعی:** انتخاب میزبان با مالک است؛ اظهار نام مالک، مرحلهٔ شناسایی است؛ تأیید مالک، شرط پذیرش است؛ provisioning واقعی محیط خصوصی، اقدام جداگانه و فنی مالک است.
