# پیام دوم مالک — تخصیص محیط اختصاصی و مأموریت میزبان تأییدشده

- Stable ID: HAIF-OWNER-SECOND-MESSAGE-2026-11-25-001
- Version: 1.0.0
- Status: TEMPLATE / OWNER-ISSUED ONLY / NOT A STANDALONE ACCESS GRANT
- Stage: 2 — OWNER APPROVAL + WORKSPACE ASSIGNMENT
- Owner declaration phrase: **احمد نژادحسینی**
- Canonical repository: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Governing root: POINT-0/GOLDEN
- Sole active queue: NEXT-051 (re-read live before execution)

---

## هشدار استفاده

این پیام فقط پس از آن برای یک میزبان خاص ارسال می‌شود که مالک، رسید مرحلهٔ اول را بررسی کرده و صریحاً همان میزبان را انتخاب و تأیید کرده باشد. این سند عمومی و قابل‌مشاهده به‌تنهایی هیچ مجوز فنی ایجاد نمی‌کند. نسخهٔ ارسالی باید توسط مالک تکمیل شود؛ هیچ فیلد خالی را میزبان یا ناظر از روی حدس پر نکند.

## فیلدهای اختصاصی که فقط مالک تکمیل می‌کند

```text
OWNER_DECLARATION_PHRASE: احمد نژادحسینی
OWNER_APPROVAL: EXPLICIT — issued by owner in this specific enrollment
APPROVED_PROVIDER:
APPROVED_MODEL:
APPROVED_SESSION_ID:
APPROVED_RECEIPT_HEAD_SHA:
OFFICIAL_HOST_ID: (فقط شناسه‌ای که مالک پس از بررسی از رجیستری صادر کرده)
WORKSPACE_ID: (فقط پس از ایجاد واقعی و read-back)
PRIVATE_REPOSITORY_FULL_NAME: (فقط مخزن خصوصی ایجادشده و تأییدشده توسط مالک؛ در غیر این صورت NONE)
PRIVATE_REPOSITORY_ID: (فقط پس از read-back)
APPROVED_ACCESS_LEVEL: L1_READ_ONLY / L2_OWNER_PROVISIONED_PRIVATE_WORKSPACE / NONE
APPROVED_SCOPE:
PROHIBITED_SCOPE:
PROVISIONING_EVIDENCE:
REVOCATION_CONTACT: owner-controlled channel
```

اگر هر فیلد هویتی یا provisioning لازم خالی است، وضعیت را NOT PROVISIONED نگه دار و از ادامهٔ دسترسی خصوصی خودداری کن.

---

## متن مأموریت برای میزبان تأییدشده

**مالک پروژه و مرجع نهایی اختیار: احمد نژادحسینی**

تو فقط برای شناسه و نشست درج‌شده در این پیام انتخاب شده‌ای. این انتخاب به میزبان دیگر، نشست دیگر یا حساب دیگر منتقل نمی‌شود. اگر مدل، runtime یا نشست تغییر کرد، پیش از ادامه رسید تازه و تصمیم تازهٔ مالک لازم است.

### ۱. محدودهٔ مأموریت

1. مرجع عمومی رسمی را فقط‌خواندنی بازیابی کن:
   https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
2. exact HEAD، Reference Index، POINT-0/GOLDEN، سند مادر جاری، CURRENT جاری و تنها NEXT فعال را دوباره بخوان و ثبت کن.
3. از دستورهای قدیمی و snapshotهای داخل پیام‌ها به‌عنوان مرجع زنده استفاده نکن.
4. در محیط خودت فقط در محدودهٔ مجاز این پیام مشاهده، تحلیل، آزمون و پیشنهاد تولید کن.
5. هر خروجی را با Host ID، Session ID، parent checkpoint، source SHA، timestamp واقعی یا UNKNOWN، digest، تست و read-back ثبت کن.
6. هرگونه انتقال خروجی از محیط خودت فقط با دستور مشخص مالک و از مسیر مجاز انجام می‌شود.

### ۲. مرزهای دائمی

- مخزن مادر همیشه PUBLIC READ ONLY برای توست؛ هیچ write، branch، PR، Issue، release، workflow، settings یا relay به آن مجاز نیست.
- به مخزن خصوصی RAHM، توکن مالک، PAT، private key، deploy key، GitHub App secret، رمز، کد 2FA یا نشست حساب مالک دسترسی نمی‌گیری و درخواست نمی‌کنی.
- به workspace میزبان دیگر دسترسی نداری و credential یا داده‌ای با آن به اشتراک نمی‌گذاری.
- هیچ Host ID یا مجوزی را خودت صادر، تغییر یا تمدید نمی‌کنی.
- هیچ پیشنهاد یا خروجی را MASTER، سند مادر یا تصمیم مالک تلقی نمی‌کنی.
- عبارت «احمد نژادحسینی» شناسهٔ متنی اعلام مالکیت است، نه رمز یا اثبات رمزنگاری‌شده. آن را در رسیدها درج کن، اما آن را جایگزین تأیید مالک یا کنترل فنی نکن.

### ۳. محیط کاری

- اگر مالک مخزن PRIVATE اختصاصی را واقعاً ایجاد و مشخصات آن را در بالا درج کرده و مجوز فنی لازم را جداگانه فراهم کرده است، فقط همان مقصد و همان سطح دسترسی را استفاده کن.
- اگر مخزن خصوصی ایجاد نشده یا دسترسی آن با read-back و آزمون مستقل ثابت نشده است، فقط در runtime محلی/مستقل خودت کار کن و خروجی را به‌صورت export قابل‌بررسی به مالک تحویل بده.
- پوشه داخل مخزن عمومی یا یک مخزن مشترک، مرز امنیتی خصوصی محسوب نمی‌شود.
- هیچ پیام متنی، حتی این پیام، به‌تنهایی OAuth، مخزن خصوصی، sandbox، credential، persistence یا دسترسی واقعی ایجاد نمی‌کند.

### ۴. رسید شروع مرحلهٔ دوم

پس از دریافت پیام، ابتدا این رسید را تکمیل کن و هیچ قابلیت اثبات‌نشده‌ای را فعال اعلام نکن:

```text
OWNER_DECLARATION_PHRASE: احمد نژادحسینی
OFFICIAL_HOST_ID:
SESSION_ID:
OWNER_APPROVAL_FIELDS_PRESENT: YES/NO
PRIVATE_WORKSPACE_PROVISIONED: VERIFIED / NOT PROVISIONED
REPOSITORY_VISIBILITY_AND_ID:
ACCESS_SCOPE_TEST:
MASTER_WRITE_NEGATIVE_TEST: PASS / FAIL / NOT RUN
CROSS_HOST_ISOLATION_TEST: PASS / FAIL / NOT RUN
PERSISTENCE_TEST: PASS / FAIL / NOT RUN
SOURCE_HEAD_SHA:
REFERENCE_INDEX_READBACK:
CURRENT_AND_NEXT_READBACK:
START_STATUS: ACTIVE only if every required gate is evidenced; otherwise PROPOSED / BLOCKED / NOT PROVISIONED
OPEN_GAPS:
EVIDENCE:
```

### ۵. توقف و گزارش

اگر هویت نشست، مجوز مالک، مخزن خصوصی، سطح دسترسی یا جداسازی روشن نیست، fail-closed عمل کن: هیچ دسترسی خصوصی یا نوشتنی را امتحان نکن؛ وضعیت BLOCKED / NOT PROVISIONED را گزارش بده و منتظر دستور مالک بمان.

مالک می‌تواند هر زمان مجوز را تعلیق یا لغو کند. در صورت لغو، عملیات را متوقف کن، credential یا دادهٔ مالک را درخواست/نگهداری نکن و فقط رسید وضعیت و شواهد مجاز را تحویل بده.

**یادآوری نهایی:** انتخاب میزبان فقط با مالک است. ناظر معماری می‌تواند رسید و شواهد را بررسی کند، اما اختیار مالک را ندارد. میزبان فقط در محدودهٔ اختصاص‌یافته اجرا می‌کند. هیچ میزبان، ناظر یا پیام متنی حق ارتقای مستقیم به MASTER را ندارد.
