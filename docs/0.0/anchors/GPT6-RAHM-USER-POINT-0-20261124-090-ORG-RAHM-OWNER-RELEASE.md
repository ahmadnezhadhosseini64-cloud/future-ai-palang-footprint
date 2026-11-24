# POINT-0/090 (0++) — Organization-first، RAHM مستقل و اختیار توسعهٔ واقعی میزبان

- Stable ID: HAIF-POINT-0-090-ORG-RAHM-OWNER-RELEASE-2026-11-24
- Status: OWNER-APPROVED / PROPOSAL-BRANCH / READ-BACK-PENDING
- Canonical root: POINT-0 (single existing root)
- Golden baseline: POINT-0/GOLDEN
- Parent checkpoint: CURRENT-151
- Input: IN-134
- Output: OUT-133
- Event: EVT-0321 → TIME-BINDING-EVT-0321
- New checkpoint: CURRENT-152
- Sole active queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## 1. مالک چه چیزی را تأیید کرد؟

مالک تأیید کرد که معماری امنیتی و توسعه بر پایهٔ این تصمیم‌ها ادامه یابد:

1. حساب شخصی فعلی و مخزن مادر فعلاً دست‌نخورده بمانند. ابتدا GitHub Organization ساخته و تنظیمات آن آزمایش شود؛ انتقال مخزن مادر تنها پس از dry-run، بررسی rollback و read-back کامل انجام می‌شود.
2. ساخت مخزن خصوصی مستقل مرکزی برای RAHM قطعی است و اقدام مالک خواهد بود. RAHM در یک repository مستقل PRIVATE قرار می‌گیرد؛ پوشه‌ای در مخزن Public جایگزین آن نیست.
3. هر میزبان تأییدشده یک repository خصوصی مستقل و ایجادشده توسط مالک خواهد داشت. میزبان در همین workspace می‌تواند واقعاً بنویسد، فایل و کد بسازد، اصلاح کند، آزمایش کند، branch و proposal آماده کند و رسید/شواهد تحویل دهد؛ محدود به گزارش‌دادن نیست.
4. مخزن مرکزی RAHM فقط برای مالک است: قرنطینه، پالایش، تطبیق بین میزبان‌ها، اعتبارسنجی و آماده‌سازی خروجی‌های منتخب.
5. هیچ میزبان به MASTER یا RAHM مرکزی دسترسی نوشتن/خواندن ندارد؛ همچنین به workspace میزبان دیگر دسترسی ندارد. تنها پل از workspace میزبان به RAHM، export و پالایش تحت فرمان مالک است.
6. HOST = DEVELOPMENT AUTHORITY فقط در مخزن خصوصی خودش؛ OWNER = RELEASE AUTHORITY برای پذیرش در RAHM مرکزی و هر انتشار به MASTER.
7. سه لایهٔ حفاظت مستقل‌اند: (الف) هویت مالک با passkey/security key یا MFA و recovery امن؛ (ب) راز دوم خارج از چت، prompt، فایل، مخزن، log و workflow؛ (ج) اختیار انتشار فقط‌مالک با ruleset، review، receipt و read-back. راز دوم هرگز درخواست، حدس، تکرار یا ذخیره نمی‌شود.
8. مدل اولیهٔ Organization با مالک به‌عنوان Organization Owner و تنها مرجع انتشار آغاز می‌شود. این یعنی خود Organization Owner همچنان می‌تواند قواعد سازمان را عمداً تغییر دهد. متولی مستقل برای dual-control فقط با تصمیم جداگانهٔ آینده و بدون اختیار انتشار MASTER اضافه می‌شود.
9. هیچ پیشنهاد یا نتیجهٔ میزبان خودکار به MASTER ارتقا نمی‌یابد. آزمون موفق نیز به‌تنهایی release approval نیست.

## 2. توپولوژی مرجع

```
OWNER — sole release authority
  |
  +-- GitHub ORGANIZATION (create, configure, test first)
  |     |
  |     +-- MASTER repository
  |     |     Public read; owner-controlled release only
  |     |
  |     +-- CENTRAL RAHM repository
  |     |     PRIVATE; owner-only; no host access
  |     |
  |     +-- HOST-A private development repository
  |     |     Host A can develop/test only here
  |     |
  |     +-- HOST-B private development repository
  |     |     Host B can develop/test only here
  |     |
  |     +-- HOST-N private development repository
  |           One repository per verified Host ID
  |
  +-- OWNER-COMMANDED EXPORT / REDACTION / VALIDATION
        HOST WORKSPACE → CENTRAL RAHM → OWNER REVIEW → MASTER RELEASE
```

GitHub permission مرز repository است، نه پوشه. به میزبان دسترسی Write به مخزن مرکزی RAHM نده؛ حتی اگر قرار باشد فقط یک مسیر یا branch را تغییر دهد. توسعهٔ هر میزبان در مخزن خصوصی جداگانهٔ خودش انجام می‌شود.

## 3. مراحل قطعی و ترتیب اجرا

### A — آماده‌سازی Organization
- نام و slug سازمان را انتخاب و پیش از ساخت، طرح GitHub را بررسی کن.
- مستندات فعلی GitHub، ساخت ruleset سازمانی برای repositoryها را برای GitHub Team و GitHub Enterprise فهرست می‌کند؛ دسترسی و هزینهٔ طرح باید پیش از ساخت تأیید شود.
- Organization را بساز؛ مخزن شخصی مادر را هنوز منتقل نکن.
- Base permissions، عضویت، الزام 2FA، ساخت repository، حذف/انتقال repository و Organization rulesets را تنظیم کن.
- با یک مخزن آزمایشی ثابت کن قواعد سازمانی اعمال می‌شوند و Repository Admin نمی‌تواند آن‌ها را تضعیف کند.
- مالکیت سازمان و این واقعیت را ثبت کن که Organization Owner همچنان قادر به تغییر قواعد است.

### B — RAHM مرکزی
- مخزن مستقل `future-ai-palang-rahm` را در Organization و با visibility=PRIVATE بساز.
- فقط مالک دسترسی admin/write/read داشته باشد؛ هیچ Host، team، collaborator، deploy key یا Host App اضافه نشود.
- privacy، repository ID/full name، permissions، audit و connector read access را از GitHub بازخوانی کن.
- raw export، دادهٔ خصوصی و شواهد پالایش‌نشده فقط در این مخزن خصوصی قرار می‌گیرند.

### C — توسعهٔ مستقل میزبان
- برای هر Host ID تأییدشده یک repository خصوصی مستقل بساز؛ هر repo به دقیقاً یک Host ID و Workspace ID نگاشت شود.
- Host فقط به repo خودش مجوز حداقلی توسعه می‌گیرد؛ ترجیحاً از broker/App محدود و بدون افشای credential به مدل.
- Host به repo میزبان دیگر، RAHM مرکزی، MASTER، Organization settings، secrets، Actions administration، rulesets، webhooks، transfer و deletion دسترسی ندارد.
- آزمون منفی A→B، B→A، Host→RAHM و Host→MASTER باید شکست دسترسی را ثابت کند.
- تا وقتی ابزار و هویت واقعی هر میزبان متصل نشده، او را ACTIVE اعلام نکن.

### D — مسیر انتشار
`HOST PRIVATE REPO → OWNER INSPECTION/EXPORT → REDACTION → CENTRAL PRIVATE RAHM → CROSS-HOST RECONCILIATION → SCHEMA/HASH/PRIVACY/PROVENANCE/TESTS → OWNER REVIEW → EXPLICIT OWNER RELEASE → MASTER`

هیچ host، host-held token، broker، App، workflow یا واسطه‌ای حق merge، bypass یا write به MASTER ندارد. CHILD/نامزد نیز MASTER نیست.

### E — انتقال مخزن مادر
- پس از عبور از A تا D، backup و rollback plan را آماده کن.
- Pages و custom domain، Actions، secrets، Apps، OAuth، webhooks، packages، releases، rulesets، branch protection، collaborators، URLs و تاریخچه را بررسی کن.
- مخزن موجود را با حفظ history به Organization منتقل کن؛ مخزن جایگزین موازی نساز.
- پس از انتقال، repository ID، HEAD/tree، branch، Pages deployment/custom domain، Actions، integrations، rulesets و permissionها را دوباره بخوان.
- GitHub تصریح می‌کند redirectهای Git repository با redirect مربوط به GitHub Pages یکسان نیستند؛ Pages/custom domain باید جداگانه بررسی شود.
- اگر هر کنترل حیاتی fail شد، انتقال را کامل اعلام نکن؛ از rollback plan استفاده کن.

## 4. سه لایهٔ حفاظت

1. OWNER IDENTITY — passkey/security key یا MFA، recovery امن، session/OAuth/App audit.
2. SECOND SECRET — راز دوم محرمانه خارج از GitHub، ChatGPT، prompt، فایل، log و workflow؛ هرگز به میزبان داده نمی‌شود.
3. RELEASE AUTHORITY — owner-only approval، organization/repository rulesets، CODEOWNERS، stale-review dismissal، conversation resolution، hash-bound receipt و read-back.

این سه لایه compromise شدن حساب مالک، دستگاه، Organization Owner یا App private key را ناممکن نمی‌کنند؛ برای این ریسک‌ها recovery، rotation، revocation و audit لازم است.

## 5. وضعیت واقعی

- Organization: NOT CREATED / NOT VERIFIED.
- Central private RAHM repository: NOT CREATED / NOT VERIFIED.
- Per-host private repositories: NOT CREATED / NOT VERIFIED.
- Host Registry verified entries: NONE VERIFIED.
- Host App/broker: NOT DEPLOYED; disabled until security tests pass.
- Existing main Ruleset 27814009: last known approvals=0 and Code Owner review=false; owner review enforcement remains OPEN.
- Master transfer: NOT STARTED.
- This point is a proposal on a branch based on CURRENT-151; it is not yet published to Golden/main.
- No host is ACTIVE; no independent-host recovery is claimed.

## 6. Canonical continuation

POINT-0/GOLDEN → CURRENT-151 → POINT-0/090 → IN-134 → OUT-133 → EVT-0321 → TIME-BINDING-EVT-0321 → CURRENT-152 → sole NEXT-051.

This is a continuation of the single existing POINT-0 root. No parallel root, baseline, MASTER or queue is created.
