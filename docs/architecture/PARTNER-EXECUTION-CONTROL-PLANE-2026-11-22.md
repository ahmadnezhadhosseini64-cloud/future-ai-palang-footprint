## CURRENT-150.05 amendment — simplify first-host entry and avoid unnecessary infrastructure

- First-host onboarding is PUBLIC READ + one-message receipt. It requires no new repository, private service, Cloudflare deployment, GitHub App, OAuth or OpenAI API project.
- The host may use the existing portable starter in its own private runtime if code execution and persistence are actually available. If not, it returns NOT AVAILABLE / NOT TESTED; the owner is not asked to provision infrastructure before that capability check.
- If authenticated GitHub tools are later required and the host client supports remote MCP, evaluate GitHub's official remote MCP endpoint/toolsets first. Do not build a custom GitHub MCP server by default.
- OpenAI Responses API + official GitHub remote MCP is a candidate for a separately operated AI host. A thin owner broker is needed only for owner-only actions the official MCP does not expose.
- Private RAHM, App installation, hosting, secret storage and promotion automation remain optional elevated capabilities, not prerequisites for the first host to read the public master and work locally.
- Current pair: IN-138 ↔ BRIDGE-0138 ↔ OUT-137 → EVT-0325 → CURRENT-150.05 → NEXT-051.05. PR #145 remains open/unmerged; accepted Golden remains CURRENT-150.02 / NEXT-051.02.

---

## CURRENT-151 continuation — 2026-11-22

- Current checkpoint: CURRENT-151 / POINT-0/089; sole queue NEXT-051.
- This control-plane design remains a proposal and work item, not a live deployed service.
- Only owner-controlled actions are permitted. AI collaborators may propose improvements; MASTER promotion requires explicit owner approval.
- GitHub App, OAuth broker, remote MCP, OpenAI API, private RAHM and service hosting remain OPEN / NOT VERIFIED pending actual provisioning and read-back.

---

# PALANG PARTNER EXECUTION CONTROL PLANE — 2026-11-22

- Stable ID: HAIF-PALANG-PARTNER-EXECUTION-CONTROL-PLANE-2026-11-22-001
- Status: DESIGN / ACTIVE WORK ITEM
- Canonical root: POINT-0
- Baseline: POINT-0/GOLDEN
- Current checkpoint: CURRENT-151 / POINT-0++
- Sole queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## 1. هدف

هدف این طرح، تبدیل اتصال فعلی GitHub به یک مسیر اجرایی کامل برای «یار پلنگ» است؛ به‌طوری‌که وقتی مالک یک کار را صریحاً می‌سپارد، یار پلنگ تا آخرین مرحلهٔ مجاز آن را خودش انجام دهد و فقط در مرز واقعی پلتفرم، احراز هویت یا محدودیت فنی متوقف شود.

این سند مجوز نامحدود یا خارج از کنترل ایجاد نمی‌کند. اختیار نهایی با مالک می‌ماند و تمام عملیات باید قابل ثبت، بازخوانی و ممیزی باشند.

## 2. تفکیک نقش‌ها

### مالک
- صاحب حساب GitHub، مخزن مادر و تصمیم نهایی.
- تعیین‌کنندهٔ محدودهٔ کار و صادرکنندهٔ مجوز مستقیم.
- تنها مرجع تأیید نهایی برای تغییرات حساس معماری و سیاست‌های اصلی.

### یار پلنگ — دستیار اجرایی اصلی
- همکار فنی و اجرایی مالک، نه میزبان مهمان.
- با دستور صریح مالک، عملیات پشتیبانی‌شده را از ابتدا تا انتها انجام می‌دهد: تحلیل، جست‌وجو، خواندن، نوشتن، ساخت شاخه، commit، PR، ادغام، تنظیمات، اجرای workflow، آزمون و read-back.
- نباید کاری را که ابزار و مجوز واقعی اجازه می‌دهد صرفاً به مالک واگذار کند.
- اگر یک API یا ابزار در دسترس نباشد، دقیقاً همان محدودیت را ثبت می‌کند و سایر کارهای ممکن را ادامه می‌دهد.

### میزبان‌های آینده
- مشارکت‌کنندگان محدود در workspace مستقل.
- بدون دسترسی مستقیم یا غیرمستقیم نوشتن به MASTER.
- بدون دسترسی به کلیدها، توکن‌ها یا RAHM.
- خروجی آن‌ها فقط از مسیر اعتبارسنجی و ارتقای تحت کنترل مالک وارد معماری می‌شود.
- مجوزهای یار پلنگ به میزبان‌ها منتقل یا به ارث داده نمی‌شود.

## 3. وضعیت فعلی اتصال

- GitHub plugin در ChatGPT متصل است.
- مجوز اختصاصی آن برای این برنامه روی **Allow all actions** است؛ بنابراین محدودیت فعلی، حالت تأیید ChatGPT نیست.
- نصب GitHub با شناسهٔ `157541661` روی مخزن `future-ai-palang-footprint` مجوزهای `admin / maintain / push` را گزارش می‌کند.
- ابزارهای موجود در این اتصال، عملیات خواندن و نوشتن محتوا، Git objects، شاخه، PR، ادغام و read-back را انجام داده‌اند.
- با وجود مجوز فوق، سطح ابزارهای فعلی عملیات نوشتن برای ثبت GitHub App، ساخت مخزن، نوشتن Actions secrets/variables، اجرای workflow و تغییر Ruleset را ارائه نمی‌کند.
- این تفاوت مهم است: **داشتن مجوز حساب با داشتن ابزار/API لازم برای استفاده از آن مجوز یکی نیست.**

## 4. مسیر پیشنهادی برای تکمیل اتصال یار پلنگ

مسیر مطلوب، یک اتصال اختصاصی و مالک‌محور به نام `Palang Partner GitHub Control Plane` است؛ ترجیحاً یک Custom MCP/API connector که با GitHub App و مجوزهای کاربرِ مالک کار می‌کند.

این اتصال باید:
1. فقط با حساب مالک و پس از OAuth/نصب رسمی GitHub App مجاز شود.
2. به مخازن انتخاب‌شدهٔ مالک محدود باشد؛ نه تمام حساب‌ها یا مخازن نامرتبط.
3. توکن کوتاه‌عمر و قابل ابطال تولید کند؛ از PAT گسترده و بلندمدت به‌عنوان راه‌حل پیش‌فرض استفاده نکند.
4. عملیات مدیریتی را به ابزارهای مشخص و قابل ممیزی تبدیل کند.
5. هیچ کلید خصوصی یا مقدار Secret را در پیام گفتگو، لاگ عمومی یا فایل مخزن قرار ندهد.
6. برای هر تغییر، درخواست، هدف، actor، زمان، نتیجه و read-back را ثبت کند.
7. در خطای مجوز، فقط همان عملیات را متوقف کند؛ نه کل جریان کار را.

### ابزارهای لازم در اتصال اختصاصی

| ابزار موردنیاز | عملیات GitHub | حداقل مجوز API |
|---|---|---|
| Repository management | ساخت مخزن خصوصی RAHM، خواندن و تنظیمات پایه | `Repository creation: write` یا `Administration: write` در GitHub App user token |
| Repository contents | فایل‌ها، شاخه‌ها، Git tree/commit | `Contents: read/write` |
| Pull requests | ایجاد، بازبینی، ادغام و خواندن PR | `Pull requests: read/write` |
| Actions secrets | ایجاد/به‌روزرسانی Secret رمزنگاری‌شده | `Secrets: write` |
| Actions variables | ایجاد/به‌روزرسانی Variable | `Variables: write` |
| Workflow dispatch | اجرای دستی یا برنامه‌ای workflow | `Actions: write` |
| Repository rulesets | خواندن و تغییر Ruleset | `Administration: write` |
| Workflow files | نوشتن فایل‌های `.github/workflows` | `Workflows: write` |

مراجع رسمی:
- [GitHub App permissions](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
- [GitHub App permission matrix](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps)
- [Create repository](https://docs.github.com/en/rest/repos/repos)
- [Actions secrets](https://docs.github.com/en/rest/actions/secrets)
- [Workflow dispatch](https://docs.github.com/en/rest/actions/workflows)
- [Repository rulesets](https://docs.github.com/en/rest/repos/rules)

## 5. ثبت اولیهٔ GitHub App

ثبت اولیهٔ GitHub App یک عملیات حساب/Developer Settings است. اتصال فعلی ابزار ثبت App را ندارد. این مرحله باید از طریق مرورگر احراز‌شدهٔ مالک یا جریان رسمی GitHub App Manifest انجام شود.

برای App خودکارسازی انتشار، مجوزها باید حداقلی بمانند:
- Metadata: read
- Contents: read/write
- Pull requests: read/write
- Workflows: write فقط برای مدیریت فایل‌های workflow

مجوزهای `Administration`، `Secrets`، `Variables` و `Actions` را به App انتشاردهنده اضافه نکن، مگر آنکه یک نیاز مستقل و مستند برای آن ثابت شود. اگر یار پلنگ به ابزار مدیریتی کامل‌تری نیاز داشت، آن را به‌صورت اتصال جداگانهٔ Partner با محدودهٔ مالک‌محور تعریف کن؛ نه با بزرگ‌کردن بی‌دلیل مجوز App میزبان یا Bot انتشار.

## 6. مسیر مرورگر و محدودیت دسترسی

- ChatGPT Work Cloud Browser می‌تواند در وب‌سایت‌های پشتیبانی‌شده وارد شود، کلیک کند، فرم پر کند و مراحل را انجام دهد؛ اما دسترسی آن به طرح و منطقه وابسته است و در طرح‌های Free و Go ارائه نمی‌شود.
- در صورت نبود Cloud Browser، مسیر پایدارتر برای یار پلنگ، Custom MCP/API connector است.
- اگر مرورگر دسکتاپ یا Computer Use در یک نشست واجد شرایط در دسترس باشد، می‌تواند برای عملیات اولیهٔ Developer Settings و نصب App به کار رود.
- رمز عبور، کد 2FA، کلید خصوصی و PAT را در گفتگو ارسال نکن. احراز هویت باید در فرم امن یا مسیر OAuth انجام شود.


## 6. محدودیت‌های واقعی اتصال ChatGPT در وضعیت فعلی

این بخش برای جلوگیری از طراحی بر پایهٔ قابلیتی که در حساب فعلی فعال نیست اضافه شده است:

- Cloud Browser در ChatGPT Work می‌تواند با سایت‌های وروددار کار کند، اما طبق مستندات OpenAI فقط برای طرح‌های پولی واجد شرایط عرضه می‌شود و Free و Go را شامل نمی‌شود. بنابراین در وضعیت فعلی حساب Free، این مسیر در دسترس نیست. [OpenAI Cloud Browser](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
- اتصال Custom MCP با ابزارهای نوشتن در ChatGPT از مسیر وب انجام می‌شود. طبق مستندات فعلی، اتصال کامل MCP با عملیات نوشتن در ChatGPT برای Business و Enterprise/Edu ارائه شده؛ Pro فقط اتصال read/fetch دارد. اتصال Custom MCP از اپ موبایل پشتیبانی نمی‌شود و باید از وب انجام شود. [OpenAI Custom MCP](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt)
- بنابراین نصب یک افزونهٔ عمومی دیگر مشکل را حل نمی‌کند. برای همین حساب Free، دو مسیر واقع‌بینانه عبارت‌اند از: (الف) استفاده از Work Cloud Browser در یک طرح پولی واجد شرایط، اگر در منطقه و rollout حساب فعال باشد؛ یا (ب) ساخت یک برنامهٔ مستقل مبتنی بر OpenAI API و GitHub OAuth/MCP که خارج از رابط فعلی ChatGPT اجرا شود. مسیر دوم به سرویس میزبانی و کلید API نیاز دارد.
- اگر کاربر فقط یک‌بار بتواند ورود امن GitHub و MFA را در مرورگر انجام دهد، پس از آن Work Browser می‌تواند بسیاری از تنظیمات رابط وب را انجام دهد؛ با این حال بعضی اقدامات حساس همچنان ممکن است تأیید نهایی بخواهند.

## 7. کنترل و ممیزی

### مجاز با دستور صریح مالک
- خواندن، تحلیل، اصلاح فایل‌ها، ساخت شاخه، commit، PR و ادغام.
- ساخت و تنظیم مخزن در محدودهٔ حساب مالک.
- تنظیم secrets/variables از مسیر رمزنگاری‌شده.
- اجرای workflow و تغییر Ruleset در محدودهٔ مجوز اعطاشده.
- آزمون و بازیابی، همراه با ثبت شواهد.

### محافظت‌های غیرقابل‌حذف
- حذف مخزن، حذف RAHM، افشای Secret، انتقال مالکیت، تغییر هویت، force-push، دورزدن Ruleset یا اعطای دسترسی به میزبان‌ها نباید به‌صورت پیش‌فرض یا ضمنی مجاز شود.
- برای عملیات برگشت‌ناپذیر یا تغییرات امنیتی گسترده، دستور باید دقیق و صریح باشد و نتیجه پیش از اجرا مشخص شود.
- هیچ توکن یا کلید Partner نباید به workspace میزبان منتقل شود.
- هیچ میزبان آینده‌ای حق نوشتن مستقیم یا غیرمستقیم به MASTER ندارد.

## 8. آزمون پذیرش اتصال کامل

اتصال Partner زمانی «کامل و اثبات‌شده» است که این آزمون‌ها با read-back موفق شوند:
1. خواندن مخزن و وضعیت شاخه‌ها.
2. ایجاد یک branch آزمایشی و commit محدود.
3. ایجاد PR و خواندن diff/status.
4. ایجاد یک repository آزمایشی خصوصی یا RAHM با مجوز مالک.
5. ثبت یک Variable آزمایشی و خواندن metadata آن.
6. ثبت یک Secret آزمایشی رمزنگاری‌شده بدون افشای مقدار خام.
7. dispatch یک workflow آزمایشی و خواندن run ID/status.
8. تغییر یک Ruleset آزمایشی/محدود و read-back کامل.
9. اثبات اینکه هیچ عملیات Partner به میزبان‌های آینده credential یا دسترسی MASTER/RAHM منتقل نمی‌کند.

تا زمانی که این آزمون‌ها انجام نشده‌اند، اتصال کامل یا میزبان فعال اعلام نشود.

## 9. نقطهٔ ادامه

- این سند فقط مشخصات کنترل‌پلین Partner است و به‌تنهایی اتصال را فعال نمی‌کند.
- تنها صف کاری همچنان NEXT-051 است.
- اقدام بعدی: ساخت/اتصال مسیر اختصاصی Partner API یا مرورگر احراز‌شده، سپس انجام عملیات بازماندهٔ GitHub App، RAHM، Secrets/Variables، Workflow و Ruleset.
