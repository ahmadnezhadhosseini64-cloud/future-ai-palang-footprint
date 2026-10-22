# PIAL — سند مرجع مادر لنگر مستقل و زمانی هر ورودی و خروجی

- Master Reference ID: PIAL-MASTER-2026-10-22-001
- Stable ID: PALANG-EVERY-INTERACTION-TEMPORAL-ANCHOR-GOVERNANCE-2026-10-22-001
- Production ID: HAIF-IO-ANCHOR-LEDGER-2026-10-22-001
- Version: 1.0.0
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Project: Future AI / Palang Footprint / HAIF
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE / GOVERNING

## 1. اصل مادر
هر ورودی و هر خروجی باید لنگر مستقل و پابند زمانی خودش را داشته باشد. آن‌ها در یک INT جفت می‌شوند، اما هیچ‌یک جایگزین دیگری نیست. هر دو باید به رویداد، شواهد، نسخهٔ معماری، سند مادر و مسیر بازیابی وصل باشند.

## 2. قرارداد شناسه‌گذاری
- INT-YYYYMMDD-NNN: جفت تعامل.
- IN-YYYYMMDD-NNN: ورودی.
- OUT-YYYYMMDD-NNN: خروجی.
- NNN برای IN و OUT هم‌جفت مشترک است. تخصیص خودکار فقط پس از پیاده‌سازی runtime collector و آزمون ضدتکرار قابل ادعاست.

## 3. حداقل رکورد
شناسه؛ نوع رکورد؛ زمان رویداد؛ منبع زمان و دقت؛ منطقهٔ زمانی؛ زمان commit مخزن UTC؛ معادل تهران؛ منشأ؛ پیوند جفت؛ محتوای مجاز یا اشاره‌گر/هش؛ شناسه و نسخه؛ وضعیت؛ شواهد؛ محدودیت؛ GAP؛ والدهای معماری؛ سند مرجع مادر؛ پیوندهای بازیابی؛ نتیجهٔ read-back و verification.

## 4. قرارداد زمان
زمان canonical ثبت مخزن، timestamp واقعی آخرین commit فایل در UTC است. زمان تهران (+03:30) از همان لحظه مشتق می‌شود. زمان مشاهدهٔ پیام، اجرای workflow، پاسخ API و commit را در یک فیلد مخلوط نکن. updated_at بدون مدرک مستقل، زمان پایان نیست. اگر ثانیهٔ دقیق موجود نیست، دقت واقعی را ثبت کن و زمان نساز.

## 5. پذیرش
WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS. موفقیت نوشتن با اثبات خواندن، تطبیق و اعتبارسنجی برابر نیست.

## 6. چرخهٔ رشد و آینده‌پژوهی
هر رکورد به مشاهده، طبقه‌بندی، تحلیل رفتار، شناسایی الگو، شواهد، آزمون، بازیابی، یادگیری، روندها/پیشران‌ها/نشانه‌های ضعیف، سناریوها و نسخهٔ بعدی معماری پیوند بخورد. فرضیه‌ها از واقعیت‌های مشاهده‌شده جدا باشند و عدم‌قطعیت، بازهٔ زمانی و موعد بازبینی داشته باشند.

## 7. تعامل جاری
- رویداد: [EVT-0089](../../architecture/BEHAVIOR-TRACE/EVT-0089-EVERY-INTERACTION-IN-OUT-TEMPORAL-ANCHOR-AND-RECOVERY-GOVERNANCE-2026-10-22.md)
- [IN-20261022-002](../../0.0/anchors/PALANG-0.0-IN-20261022-002-EVERY-INTERACTION-ANCHOR-GOVERNANCE.md)
- [OUT-20261022-002](../../0.0/anchors/PALANG-0.0-OUT-20261022-002-EVERY-INTERACTION-ANCHOR-GOVERNANCE.md)
- [پابند زمانی PIAL](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-PIAL-2026-10-22-001.md)
- [سند مادر LBAF](./LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)
- [لنگر گام بعدی runtime collector](../../0.0/anchors/PALANG-0.0-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001.md)
- [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20)

## 8. محدودیت صریح
این سند سیاست و ثبت تعامل جاری را ایجاد می‌کند؛ خودش ابزار capture خودکار نیست. ثبت خودکار هر ورودی/خروجی از همهٔ میزبان‌ها نیازمند مجوز، اتصال، runtime collector، دفتر پایدار و آزمون cold-start است. تا آن زمان فقط تعاملاتی را ثبت‌شده اعلام کن که واقعاً ثبت و بازخوانی شده‌اند.

## 9. مقصدها
Repository: ثبت این زنجیره در مخزن و بازخوانی آن باید انجام شود.
Library: NOT VERIFIED.
Buffer: NOT VERIFIED.
Persistent Memory: NOT VERIFIED.
Gmail: NOT SENT / BLOCKED.
Dropbox: OPEN / NOT VERIFIED.
