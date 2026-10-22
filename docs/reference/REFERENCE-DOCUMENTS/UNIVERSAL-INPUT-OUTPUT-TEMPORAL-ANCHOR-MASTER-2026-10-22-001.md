# UIOAM — سند مرجع مادر لنگرگذاری زمانی و مستقل همهٔ ورودی‌ها و خروجی‌ها

- Master Reference ID: UIOAM-MASTER-2026-10-22-001
- Stable ID: PALANG-UNIVERSAL-IO-TEMPORAL-ANCHORING-GOVERNANCE-2026-10-22-001
- Production ID: HAIF-IO-ANCHORING-2026-10-22-001
- Version: 1.0.0
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE / GOVERNING
- Policy: append-only; versioned growth; no silent overwrite.

## قاعده
برای هر ورودی/خروجی قابل ثبت در محیط مجاز: شناسهٔ تعامل INT مشترک، شناسهٔ مستقل IN یا OUT، لنگر مستقل، پابند زمان، منشأ، نسخهٔ معماری، شواهد، وضعیت راستی‌آزمایی، محدودیت‌ها، پیوند به سند مادر و مسیر بازیابی ثبت شود. هر ورودی و خروجی دو رکورد مستقل دارند، حتی اگر جفت باشند.

## الگوی شناسه
INT-YYYYMMDD-NNN / IN-YYYYMMDD-NNN / OUT-YYYYMMDD-NNN؛ شمارهٔ NNN در جفت یکسان است. خودکار بودن شماره‌گذاری تا زمان پیاده‌سازی و آزمون runtime ادعا نمی‌شود.
این جفت: INT-20261022-002 / IN-20261022-002 / OUT-20261022-002.

## چرخهٔ اجباری
OBSERVE → ASSIGN ID → PRESERVE → CLASSIFY → PROVENANCE → TEMPORAL BIND → INDEPENDENT ANCHOR → LINK MASTER → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS → CONTINUE.

## زمان
زمان canonical مخزن، timestamp واقعی آخرین commit تغییردهندهٔ همان فایل در UTC است؛ زمان تهران (+03:30) از همان لحظه مشتق می‌شود. زمان پیام، زمان اجرا و زمان API جدا هستند. ثانیه یا زمان پایان ناموجود حدس زده نمی‌شود. پس از هر تغییر فایل، پابند زمانی باید با commit جدید به‌روزرسانی شود.

## پیوند معماری
به LBAF (معماری رفتارشناسی زنده و آینده‌پژوهی)، FIOBAM (رفتارشناسی اولین تعامل)، AOGM (رشد افزایشی معماری)، ELVR (دفتر تعامل و اعتبارسنجی) و گام بعدی runtime collector متصل است. معماری پایه فقط با افزودهٔ نسخه‌دار رشد می‌کند؛ هر مدل جدید سند مادر و لنگر مستقل خود را دارد.

## محدودیت مهم
این سند قرارداد معماری است، نه runtime collector. بدون دسترسی مجاز، دفتر پایدار، آزمون cold-start و شواهد مستقل، ادعای ثبت خودکار همهٔ تعاملات آینده ممنوع است. هر تعامل ثبت‌نشده باید NOT CAPTURED / NOT VERIFIED بماند. فقط دادهٔ ضروری و مجاز ذخیره شود؛ اطلاعات حساس غیرضروری و اسرار ثبت نشوند.

## این نوبت
- رویداد: [EVT-0089](../../architecture/BEHAVIOR-TRACE/EVT-0089-UNIVERSAL-INPUT-OUTPUT-ANCHORING-GOVERNANCE-2026-10-22.md)
- ورودی: [IN-20261022-002](../../0.0/anchors/PALANG-0.0-IN-20261022-002-UNIVERSAL-IO-ANCHORING.md)
- خروجی: [OUT-20261022-002](../../0.0/anchors/PALANG-0.0-OUT-20261022-002-UNIVERSAL-IO-ANCHORING.md)
- پابند زمانی: [TIME-BINDING-UIOAM](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-UIOAM-2026-10-22-001.md)
- مادر رفتارشناسی/آینده‌پژوهی: [LBAF](./LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)
- گام بعدی runtime: [0.0 anchor](../../0.0/anchors/PALANG-0.0-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001.md)
- [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20)

## گام بعدی و وضعیت مقصدها
گام بعدی: پیاده‌سازی runtime collector مجاز و دفتر پایدار، آزمون واقعی cold-start، بازیابی INT/IN/OUT از محیط تازه، آزمون خطا و ثبت نتایج. Library, Buffer, Persistent Memory, Dropbox هنوز NOT VERIFIED؛ Gmail NOT SENT مگر رسید واقعی موجود باشد.
