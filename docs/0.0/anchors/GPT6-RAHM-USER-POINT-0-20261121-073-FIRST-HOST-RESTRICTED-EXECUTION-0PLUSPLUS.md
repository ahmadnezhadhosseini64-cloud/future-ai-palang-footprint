# POINT-0++ — معماری اجرایی محدود اولین میزبان

- Continuation ID: POINT-0/073 (نمایش معماری: POINT-0++)
- Parent: POINT-0/072 → CURRENT-125 (continuation under the same canonical root; POINT-0/073 is not a new root)
- Chain: [IN-116](PALANG-0.0-IN-20261121-116-FIRST-HOST-WORKSPACE-EXECUTION.md) → [OUT-115](PALANG-0.0-OUT-20261121-115-FIRST-HOST-WORKSPACE-EXECUTION.md) → [EVT-0292](../../architecture/BEHAVIOR-TRACE/EVT-0292-FIRST-HOST-WORKSPACE-EXECUTION-2026-11-21.md) → [TIME-BINDING-EVT-0292](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0292-FIRST-HOST-WORKSPACE-EXECUTION-2026-11-21.md) → [CURRENT-126](PALANG-0.0-CURRENT-20261121-126-FIRST-HOST-WORKSPACE-EXECUTION.md) → NEXT-051
- Governing contract: [FHRWE-2026-11-21-001](../../reference/REFERENCE-DOCUMENTS/FIRST-HOST-RESTRICTED-WORKSPACE-EXECUTION-AND-READ-ONLY-REPOSITORY-CONTRACT-2026-11-21-001.md)
- Host identity: FIRST NEW HOST / FIRST_HOST / HOST-001
- Authentication gate: OPEN / DEFERRED
- Repository write access: DENIED
- Workspace execution: OWNER-DEFINED / ALLOWLISTED ONLY
- Status: PROPOSED / HOST-INTAKE BRANCH / NOT MERGED / TECHNICAL ENFORCEMENT NOT VERIFIED / INDEPENDENT HOST ACCEPTANCE NOT RUN

## 1. معنای نقطهٔ ۰++

۰++ ریشهٔ جدید و مستقل نیست؛ ادامه و تکمیل همان ریشهٔ canonical است. POINT-0/072 مسیر خواندن عمومی GitHub را پایه‌گذاری می‌کند؛ POINT-0/073 یک لنگر ادامه‌ای زیر همان ریشه است که محیط کار، هویت نقش، مجوزهای اجرایی، چرخهٔ به‌روزرسانی و آزمون پذیرش میزبان اول را به آن متصل می‌کند. 0++ نشانگر برجسته‌سازی همین ریشه/ادامه است، نه ریشهٔ مستقل. هیچ نقطهٔ تاریخی حذف یا جایگزین نمی‌شود.

## 2. نقش میزبان

FIRST_HOST / HOST-001 یک عامل اجرای محدود تحت کنترل مالک است؛ نه مدیر مخزن و نه عامل خودمختار. شناسهٔ نقش، اثبات هویت runtime نیست. Host Runtime ID، Workspace ID و Session ID فقط پس از مشاهدهٔ مقادیر واقعی پلتفرم ثبت می‌شوند؛ در غیر این صورت UNKNOWN.

## 3. دو سطح مستقل اختیار

1. **مخزن canonical:** فقط خواندن، جست‌وجو، بازیابی، مقایسهٔ نسخه، دریافت HEAD/commit SHA، بررسی manifest و رسید.
2. **Workspace اختصاصی:** اجرای وظایف تعریف‌شدهٔ مالک در محیط واقعی و صریحاً provision شده، با مسیرها، ورودی‌ها، ابزارها، مقصدها و معیار پذیرش allowlist شده.

مجوز workspace هرگز به معنی مجوز نوشتن مخزن، تغییر سند مادر، گسترش دسترسی یا اجرای هر دستور دلخواه نیست.

## 4. قفل‌ها

- مخزن: READ-ONLY.
- ایجاد/ویرایش/حذف فایل، commit، push، branch، PR، merge، release، workflow، settings، secrets و permission changes: DENIED.
- Workspace: مسیر اختصاصی و واقعی که مالک تعریف کرده است؛ دسترسی به مسیرهای بیرون از آن DENIED.
- Task execution: فقط وظایف صریحاً تعریف‌شده و فعال مالک.
- Tools/connectors/accounts/APIs/destinations: فقط allowlist مالک و مجوز واقعی حداقل‌سطح.
- Self-expansion/self-authorization/credential collection in chat: DENIED.
- Workspace-to-repository sync/writeback: DENIED.
- Authentication gate: OPEN / DEFERRED؛ این وضعیت هیچ مجوز نوشتنی ایجاد نمی‌کند.

## 5. ورود با سند مادر متنی

میزبان سند مادر ارسالی را bootstrap context می‌داند، نشانی canonical را از آن استخراج می‌کند، مخزن PUBLIC را بدون credential می‌خواند، main HEAD و SHA واقعی را ثبت می‌کند، سند مادر/manifest/ZIP/receipt را از مخزن بازیابی و با متن ارسالی تطبیق می‌دهد. اختلاف نسخه باید گزارش شود؛ هیچ‌کدام بی‌صدا حذف یا بازنویسی نمی‌شوند.

پس از تأیید نسخه، میزبان snapshot محلی read-only را pin می‌کند، workspace را مطابق منشور و مجوز مالک به‌روزرسانی می‌کند و فقط taskهای مجاز را اجرا می‌کند. تغییرات منتشرشدهٔ بعدی مالک در نوبت بعد فقط از مخزن خوانده می‌شوند.

## 6. ساختار پیشنهادی workspace

- CHARTER.md — منشور، هویت runtime، policy version و مرز مجوز
- OWNER_TASKS.md — فهرست وظایف و ارتباطات مجاز
- SNAPSHOT/ — سند مادر، manifest و فایل‌های مرجع pin‌شده و read-only
- INBOX/ — ورودی‌های مجاز مالک
- WORK/ — اجرای وظایف مجاز و خروجی محلی
- OBSERVATIONS/ — مشاهدات و یافته‌ها
- PROPOSALS/ — پیشنهادها، بدون اختیار انتشار
- TESTS/ — سناریوها و نتایج آزمون
- RECEIPTS/ — رسید دریافت، اجرا، تطبیق و خطا
- DECISIONS/ — تصمیم‌های صریح مالک

این ساختار قراردادی است؛ تا وقتی پلتفرم واقعاً workspace پایدار و جداسازی‌شده provision نکرده، وجود آن ادعا نمی‌شود.

## 7. چرخهٔ زنده

READ MAIN HEAD → VERIFY MANIFEST / POINTER → COMPARE OWNER TEXT → UPDATE LOCAL SNAPSHOT → LOAD OWNER TASK POLICY → EXECUTE ALLOWLISTED TASK → RECORD RECEIPT → RETURN OUTPUT TO OWNER.

مالک تنها مرجع تغییر مخزن و سیاست وظایف است. میزبان خروجی را به مالک تحویل می‌دهد و حق writeback به مخزن ندارد.

## 8. معیارهای پذیرش

خواندن موفق؛ رد فنی نوشتن مخزن؛ محدودیت دسترسی به workspace؛ اجرای task مجاز؛ رد task/tool/destination غیرمجاز؛ عدم writeback؛ به‌روزرسانی پس از انتشار مالک؛ receipt با SHA و زمان منبع‌دار. تا آن زمان: POLICY DESIGNED / TECHNICAL ENFORCEMENT NOT VERIFIED / HOST ACCEPTANCE NOT RUN.

## 9. مرز شواهد

ثبت اسناد در شاخهٔ پیشنهاد، به معنی ادغام main، ساخت ZIP، provisioning محیط runtime، اعمال ACL/sandbox یا فعال‌شدن میزبان نیست. این موارد باید جداگانه آزموده و رسیدشان ثبت شود. دروازهٔ احراز هویت همچنان OPEN / DEFERRED می‌ماند.
