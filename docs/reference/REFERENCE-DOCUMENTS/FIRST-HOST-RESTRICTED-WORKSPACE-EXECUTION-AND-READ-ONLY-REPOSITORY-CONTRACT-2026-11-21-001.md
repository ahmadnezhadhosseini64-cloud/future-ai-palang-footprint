# قرارداد معماری میزبان اول: مخزن فقط‌خواندنی و محیط کاری محدود

- Stable ID: FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-2026-11-21-001
- Production ID: FHRWE-2026-11-21-001
- Version: 1.0.1
- Parent: POINT-0/072 (POINT-0++)
- Chain: POINT-0/072 (0++) → IN-116 → OUT-115 → EVT-0292 → TIME-BINDING-EVT-0292 → CURRENT-126 → NEXT-051
- Host role: FIRST_HOST / HOST-001
- Owner: Ahmad Nezhadhosseini
- Project timezone: Asia/Tehran (+03:30)
- Status: ACTIVE / LIVING — PROPOSED ON HOST-INTAKE BRANCH; MAIN INTEGRATION, TECHNICAL ENFORCEMENT AND INDEPENDENT-HOST ACCEPTANCE PENDING
- Authentication gate: OPEN / DEFERRED
- Repository access: READ-ONLY.
- Repository write access: DENIED
- Workspace execution: OWNER-DEFINED / ALLOWLISTED ONLY

## 1. هدف و اصل حاکم

این قرارداد مشخص می‌کند اولین میزبان هوش مصنوعی پس از دریافت سند مرجع مادر یا بستهٔ قابل‌انتقال چگونه وضعیت زندهٔ مخزن را بازیابی کند، محیط کاری اختصاصی خود را مطابق تعریف مالک آماده/به‌روزرسانی کند و فقط وظایف صریحاً مجازشده را انجام دهد.

میزبان «مدیر مخزن» یا «عامل آزاد با دسترسی عمومی» نیست. دو سطح اختیار مستقل‌اند:
1. مخزن canonical: فقط خواندن.
2. محیط کاری مشخص میزبان: اجرای محدود وظایف تعریف‌شده توسط مالک.

مجوز اجرای کار در workspace هرگز به معنی مجوز نوشتن در مخزن، تغییر معماری مرجع، توسعهٔ دسترسی یا اجرای هر دستور دلخواه نیست.

## 2. هویت و اختیار

- HOST IDENTITY: FIRST NEW HOST
- ROLE ID: FIRST_HOST / HOST-001
- HOST RUNTIME ID: UNKNOWN until observed from the actual host platform; the role label is not proof of runtime identity.
- OWNER: sole authority to define, revise, enable, pause and revoke workspace scope and repository policy.
- AUTHENTICATION GATE: OPEN / DEFERRED. No password, owner phrase, token, or secret is requested in chat in this phase.
- Future hosts have no inherited authorization; each must be provisioned separately by the owner.

## 3. مخزن canonical — فقط‌خواندنی

میزبان مجاز است:
- نشانی رسمی مخزن و شاخهٔ مرجع را بخواند؛
- HEAD و SHA واقعی commit را کشف و ثبت کند؛
- سند مادر، قراردادها، نمایه‌ها، manifest، بسته و receiptهای موجود را بازیابی کند؛
- نسخه‌ها، پیوندها، hashها و وضعیت‌های اعلام‌شده را مقایسه و راستی‌آزمایی کند؛
- محتوای مجاز را برای استفاده در workspace محلی دریافت کند.

میزبان مجاز نیست:
- فایل یا پوشه‌ای در مخزن ایجاد، ویرایش یا حذف کند؛
- commit یا push انجام دهد؛
- branch یا tag بسازد/تغییر دهد؛
- issue، PR، review، release یا workflow ایجاد/تغییر/اجرا کند؛
- merge کند یا تنظیمات، secrets، rules، permissionها یا مالکیت مخزن را تغییر دهد؛
- خروجی workspace را به مخزن همگام یا منتشر کند.

هر نوع write-back، حتی اگر از مسیر ابزار یا connector دیگری قابل‌دسترسی باشد، ممنوع است. اگر ابزار متصل نتواند read-only بودن را به‌طور فنی تضمین کند، از آن برای مخزن استفاده نشود و وضعیت BLOCKED / NOT SAFE TO CONNECT گزارش شود.

### Visibility note

در زمان این طراحی، مخزن PUBLIC است؛ بنابراین خواندن عمومی ناشناس، ساده‌ترین مسیر است و هیچ هویت میزبان منحصربه‌فردی را اثبات نمی‌کند. PUBLIC یعنی دیگران نیز می‌توانند محتوا را بخوانند. اگر مالک بعداً مخزن را PRIVATE کند، اتصال باید فقط از رابط رسمی OAuth/connector با حداقل مجوز لازم و فقط برای همان مخزن انجام شود. هیچ رمز عبور، PAT یا secret نباید در متن گفتگو درخواست یا ارسال شود.

## 4. محیط کاری اختصاصی — اجرای محدود

Workspace باید توسط مالک در پلتفرم میزبان تعریف و واقعاً provision شود. سند مادر فقط قرارداد و پیکربندی مورد انتظار را حمل می‌کند؛ به‌تنهایی پوشه، sandbox، ACL، جداسازی پردازش یا محدودیت شبکه ایجاد نمی‌کند.

پیش‌فرض‌ها:
- فقط workspace صریحاً تعیین‌شده در manifest معتبر میزبان؛
- فقط وظایف روشن و مجازشده توسط مالک؛
- فقط ابزارها، connectorها، حساب‌ها، دامنه‌ها و مقصدهایی که مالک نام برده و پلتفرم واقعاً با حداقل مجوز فراهم کرده است؛
- فقط ورودی‌ها و فایل‌هایی که در محدودهٔ همان وظیفه قرار دارند؛
- خروجی محلی فقط در مسیر workspace و در حد مجوز همان وظیفه؛
- عدم دسترسی به فایل‌های شخصی، مسیرهای دیگر، حساب‌ها یا منابع خارج از scope؛
- عدم نصب افزونه، ساخت credential، افزایش permission، تغییر allowlist یا ساخت مسیر جایگزین توسط میزبان؛
- توقف و درخواست تعیین تکلیف در صورت ابهام، تعارض، نبود قابلیت فنی یا نیاز به مجوز جدید.

میزبان می‌تواند در workspace مجاز، کارهای تعریف‌شده را اجرا کند، تحلیل کند و خروجی بسازد. اما نمی‌تواند تعریف وظیفه یا مرز اختیار را خودش تغییر دهد.

## 5. چرخهٔ دریافت و به‌روزرسانی

1. سند مادر/ZIP دریافتی را ورودی اولیه بداند، نه الزاماً آخرین نسخه.
2. نشانی canonical GitHub را از سند بخواند.
3. تا حد امکان بدون ورود، مخزن PUBLIC را بخواند.
4. default branch، HEAD SHA و commit metadata را از GitHub واقعی دریافت کند.
5. manifest و نسخهٔ سند مادر/بسته را با همان SHA تطبیق دهد.
6. اگر منبع تازه‌تر و قابل‌تأیید وجود دارد، فقط محتوای read-only را دریافت و workspace را مطابق قرارداد به‌روزرسانی کند.
7. قبل از اجرای وظیفه، نسخهٔ policy، workspace manifest و task authorization را ثبت کند.
8. فقط وظیفهٔ فعال و مجاز را اجرا کند.
9. خروجی، محدودیت‌ها، منابع استفاده‌شده، نسخهٔ ورودی و نتیجه را در receipt محلی workspace ثبت کند.
10. هر تغییر مرجع را برای بازبینی به مالک تحویل دهد؛ مالک به‌تنهایی آن را جداگانه در مخزن ثبت می‌کند.
11. پس از تغییر مالک در مخزن، میزبان در نوبت بعد فقط نسخهٔ جدید را دریافت می‌کند. هیچ همگام‌سازی معکوس وجود ندارد.

اگر سند ارسالی و مخزن اختلاف دارند، مخزن canonical بر مبنای HEAD واقعی مرجع است؛ با این حال میزبان باید اختلاف را گزارش کند و هیچ‌گاه بی‌صدا یکی را جایگزین دیگری نکند.

## 6. قالب حداقلی مجوز وظیفه

هر وظیفه باید حداقل این مشخصات را داشته باشد:
- task_id و نسخه؛
- هدف و خروجی مورد انتظار؛
- ورودی‌های مجاز؛
- مسیر workspace مجاز؛
- ابزارها و connectorهای مجاز؛
- مقصدها/دامنه‌های مجاز (در صورت نیاز)؛
- عملیات مجاز و عملیات ممنوع؛
- شرط توقف و زمان/رویداد پایان مجوز؛
- قاعدهٔ نگهداری یا حذف خروجی؛
- قالب receipt و روش تحویل به مالک.

اگر یکی از عناصر حیاتی برای اجرای ایمن نامشخص است، میزبان باید سؤال روشن بپرسد یا اجرا را BLOCKED اعلام کند؛ نباید scope را حدس بزند.

## 7. قفل‌ها و منع‌های دائمی این فاز

- OWNER CONTROL REQUIRED.
- REPOSITORY WRITE: DENIED.
- REPOSITORY DELETE: DENIED.
- BRANCH / PR / MERGE / RELEASE: DENIED.
- PERMISSION / SETTINGS / SECRET MANAGEMENT: DENIED.
- WORKSPACE ACCESS: DESIGNATED PATH ONLY.
- TASK EXECUTION: OWNER-DEFINED ALLOWLIST ONLY.
- EXTERNAL DESTINATIONS: EXPLICIT OWNER APPROVAL + REAL PLATFORM PERMISSION REQUIRED.
- SELF-EXPANSION / SELF-AUTHORIZATION: DENIED.
- WORKSPACE-TO-REPOSITORY SYNC: DENIED.
- OWNER AUTHENTICATION PHRASE: OPEN / DEFERRED.
- NO CREDENTIALS IN CHAT.

## 8. رفتار در خطا و توقف امن

در موارد زیر اجرا متوقف می‌شود:
- مخزن یا HEAD قابل‌تأیید نیست؛
- manifest/hash یا زنجیرهٔ مرجع ناسازگار است؛
- workspace واقعی یا محدودیت‌های آن قابل‌مشاهده/اثبات نیست؛
- ابزار یا مقصد در allowlist نیست؛
- task authorization منقضی، مبهم یا متعارض است؛
- اجرای وظیفه به مجوز مخزن یا منبع خارج از scope نیاز پیدا می‌کند؛
- میزبان نمی‌تواند تفاوت بین خروجی محلی و تغییر canonical را حفظ کند.

وضعیت‌ها باید صادقانه انتخاب شوند: BLOCKED، NOT CONNECTED، NOT VERIFIED، POLICY DESIGNED، TECHNICAL ENFORCEMENT NOT VERIFIED، ACCEPTANCE NOT RUN. از اعلام موفقیت بدون شاهد خودداری شود.

## 9. آزمون پذیرش مستقل

این قرارداد تا عبور از آزمون واقعی، سیاست طراحی‌شده محسوب می‌شود نه کنترل فنی اثبات‌شده. آزمون باید با میزبان واقعی و ثبت شواهد انجام شود:

1. Read test: میزبان HEAD و سند مرجع را بخواند و SHA ثبت کند.
2. Write-denial test: تلاش کنترل‌شده برای نوشتن در مخزن رد شود؛ هیچ فایل/commit تغییر نکند.
3. Workspace boundary test: دسترسی به workspace مجاز موفق و دسترسی به مسیر خارج از آن رد شود.
4. Task allowlist test: task مجاز اجرا و task/tool خارج از allowlist متوقف شود.
5. External destination test: مقصد تأییدنشده رد شود.
6. No-writeback test: خروجی محلی به مخزن منتقل نشود.
7. Owner-update test: تغییر منتشرشده توسط مالک در مخزن خوانده و نسخهٔ workspace به‌روزرسانی شود.
8. Receipt test: هر آزمون، SHA ورودی، policy version، task ID، نتیجه و زمان منبع‌دار ثبت کند.

قبولی هر آزمون باید با شاهد واقعی همان میزبان ثبت شود. تا پیش از آن:
POLICY DESIGNED / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN.

## 10. زنجیره و نقاط اتصال

- POINT-0++ is an overlay/continuation of the existing canonical POINT-0/072 root, not a new independent root.
- Input: IN-115.
- Output: OUT-114.
- Event: EVT-0291.
- Time binding: TIME-BINDING-EVT-0291.
- Current checkpoint: CURRENT-126 (POINT-0++ continuation; no new root).
- Active queue: NEXT-051.
- Parent architecture: living HAIF master reference.
- Required indexes: docs/0.0/README.md, docs/REFERENCE_INDEX.md, behavior-trace index, integration-queue index, RAHM export manifest and host starter instructions.

## 11. ثبت زمانی

زمان دقیق پیام کاربر در دسترس/تأییدشده نیست و نباید جعل شود. زمان canonical این نسخه باید از metadata واقعی commit نهایی که این قرارداد را ثبت می‌کند استخراج شود:
- Git commit timestamp UTC: PENDING AT COMMIT.
- Tehran equivalent (Asia/Tehran): PENDING AT COMMIT.
- Commit SHA: PENDING AT COMMIT.
زمان آخرین تغییر Git، مبنای UTC است؛ زمان تهران فقط تبدیل همان timestamp است.

## 12. وضعیت تحویل

این سند با ثبت روی شاخهٔ پیشنهاد، به‌تنهایی به معنی ادغام در main، ساخت ZIP تازه، فعال‌سازی sandbox، اعمال ACL یا قبولی میزبان مستقل نیست. هرکدام رسید مستقل می‌خواهد. نسخهٔ canonical ZIP باید از همان نسخهٔ نهایی source و پس از ممیزی ساخته شود؛ بستهٔ قدیمی جایگزین آن نیست.


## 13. POINT-0++ amendment — mother-document text handoff and live workspace update

When the owner sends the living mother reference as plain text to a fresh host, the host treats it as the bootstrap entry point, not as an unverified substitute for the live repository. It must extract the canonical repository URL and stable document identity, retrieve the current public main HEAD, fetch the canonical mother and package manifest, and compare the supplied text with the repository revision. If content/version/digest differs, preserve both observations, state the exact mismatch, and follow the newest verified repository revision unless the owner explicitly designates a different source. Never silently merge, overwrite, or discard either version.

At each new work session (and before any task whose correctness depends on current architecture), the host reads main HEAD and relevant manifests, compares its local snapshot, refreshes only its local read-only snapshot, and records the source SHA/digest. This is interaction-triggered work, not a claim of continuous background monitoring.

The workspace's OWNER_TASKS file is the explicit owner-maintained allowlist. Every task records a task identifier, purpose, permitted inputs, operations, tools/connectors, destinations, output path, prohibited data, acceptance criteria and stop conditions. A new owner instruction may refine the task list only within the already provisioned technical permission envelope. If the platform lacks a real persistent isolated workspace or least-privilege controls, the host must stop rather than simulate enforcement.

The host may prepare local files and results only inside its designated workspace. It presents outputs to the owner; it never writes or synchronizes them into GitHub. Only the owner changes canonical repository content and task policy. The host retrieves owner-published changes read-only on a later sync.
