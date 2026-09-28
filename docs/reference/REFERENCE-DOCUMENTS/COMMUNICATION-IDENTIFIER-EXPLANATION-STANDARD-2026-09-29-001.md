# Communication & Identifier Explanation Standard

- Stable ID: COMMUNICATION-IDENTIFIER-EXPLANATION-STANDARD-2026-09-29-001
- Production ID: COMMUNICATION-IDENTIFIER-EXPLANATION-STANDARD-2026-09-29-001
- Version: 1.0
- Date: 2026-09-29
- Time: 02:17:16
- Timezone: Asia/Tehran (+03:30)
- Owner: Ahmad Nezhadhosseini / احمد پلنگ
- Project: Future AI / Palang Footprint
- Role: Permanent Communication Governance Reference
- Status: ACTIVE / LIVING / EXECUTABLE

## Purpose
این سند یک قاعده دائمی برای نحوه ارائه اطلاعات پروژه به کاربر است تا هیچ شناسه یا اصطلاح انگلیسی بدون توضیح فارسی ارائه نشود.

## Mandatory Communication Rule
1. هر اصطلاح English (انگلیسی) که برای معماری، پروتکل، وضعیت، ابزار یا مفهوم فنی استفاده می‌شود باید همراه معادل فارسی آن ارائه شود.
2. برای زنجیره‌های پروتکلی، ابتدا English و بلافاصله زیر آن فارسی ارائه شود:
   READ-BACK → MATCH → VERIFY
   بازخوانی → تطبیق → تأیید
3. هر Stable ID / Production ID / Reference ID (شناسه مرجع) یا هر شناسه مهم سند/رکورد، علاوه بر خود شناسه باید یک توضیح کوتاه و قابل فهم داخل پرانتز داشته باشد که بگوید آن مورد چیست.
4. برای Reference Document (سند مرجع)، قالب معرفی باید حداقل شامل «شناسه + توضیح کوتاه در پرانتز» باشد.
5. این توضیح جایگزین شناسه نیست؛ شناسه دقیق و بدون تغییر حفظ می‌شود و توضیح فقط برای فهم سریع کاربر است.
6. این قاعده برای فهرست‌ها، گزارش‌های Excavation (خاک‌برداری)، Revival (زنده‌سازی)، Repository (مخزن) و Reference Documents (اسناد مرجع) نیز الزامی است.

## Example
- HAIF-CORE-MASTER-CHILD-RAHM-2026-09-15-001 (معماری تعامل انسان و AI با ساختار Master/Child/Rahm)
- MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001 (قرارداد معماری مخزن اسناد مرجع و چرخه زنده‌بودن آن)
- REFERENCE-WORKBENCH-ARCHITECTURE-2026-09-29-001 (معماری کارگاه اسناد مرجعی که هنوز در انتظار تکمیل شواهد یا رفع مغایرت هستند)

## Governance
این اصل باید در تمام خروجی‌های بعدی رعایت شود و یک قاعده ارتباطی دائمی پروژه محسوب می‌شود.
عدم رعایت آن به‌معنای نقص در Presentation Layer (لایه ارائه) است، نه تغییر در شناسه یا اصل سند.

## Reference Document Gate
WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS
ثبت/نوشتن → بازخوانی → تطبیق → تأیید → همسان‌سازی/رفع مغایرت → تعیین وضعیت

## Evidence / Limitation
این ثبت در Repository (مخزن) انجام می‌شود. Persistent Memory (حافظه پایدار) فقط زمانی می‌تواند ACTIVE / LIVING اعلام شود که چرخه واقعی
WRITE → READ-BACK → MATCH → VERIFY
ثبت/نوشتن → بازخوانی → تطبیق → تأیید
برای آن اثبات شده باشد.

## Next Action
اجرای این استاندارد در تمام پاسخ‌ها و معرفی‌های آینده، بدون حذف شناسه و بدون حذف توضیح فارسی.
