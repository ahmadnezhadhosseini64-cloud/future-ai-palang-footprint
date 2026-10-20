# رویداد EVT-0031 — زنجیرهٔ چهارتایی ۰.۰ و دروازهٔ کشف رفتاری

- Stable ID / شناسهٔ پایدار: EVT-0031-FOUR-LINKED-0.0-CHAIN-AND-BEHAVIORAL-DISCOVERY-2026-10-20
- Production ID / شناسهٔ تولید: EVT31-2026-10-20-001
- Version / نسخه: 1.0.0
- Date / تاریخ: 2026-10-20
- Exact user-message time / زمان دقیق پیام: UNKNOWN / UNVERIFIED؛ حدس زده نمی‌شود.
- Timezone / منطقهٔ زمانی: Asia/Tehran (UTC+03:30)
- Owner / مالک: احمد پلنگ
- Project / پروژه: Future AI / Palang Footprint / HAIF
- Status / وضعیت: REPOSITORY WRITE + READ-BACK PENDING FINAL CROSS-LINK CHECK.
- Origin / منشأ: کاربر دستور داد زنجیرهٔ نقاط ۰.۰ به‌صورت چهارتایی پیش برود و نقاط به هم وصل شوند، اما هر کشف یا الگوی رفتاری قبل از ورود به معماری مادر بررسی و اعتبارسنجی شود.
- Governing reference / سند حاکم: `docs/reference/REFERENCE-DOCUMENTS/FOUR-LINKED-0.0-CHAIN-AND-BEHAVIORAL-DISCOVERY-GATE-2026-10-20-001.md`
- Registry / دفتر ۰.۰: `docs/0.0/README.md`
- Behavior trace / دفتر رفتار: `docs/architecture/BEHAVIOR-TRACE/README.md`

## 1. ثبت خواسته و تصمیم
چهار گرهٔ مرجع پیمایش:
1. `PALANG-0.0-MAIN-LOCK-2026-10-20-002` — قفل اصلی ادامه.
2. `PALANG-0.0-CURRENT-2026-10-20-001` — لنگر قبلی مستقل.
3. `OUTPUT-ANCHOR-CHAIN-AND-SESSION-CLOSE-0.0-2026-10-19-002` — زنجیرهٔ خروجی و پایان موقت نشست.
4. `PALANG-DROPBOX-FAILOVER-RESUME-0.0-2026-10-12-001` — شاخهٔ مستقل Dropbox با وضعیت OPEN / WAITING.

این چهار مورد مسیر مرجع پیمایش‌اند، نه ادعای اینکه فقط چهار نقطهٔ ۰.۰ در کل پروژه وجود دارد. تمام نقاط تاریخی دیگر باید حفظ شوند و در گراف کامل به‌تدریج متصل شوند. هیچ لنگری حذف، overwrite، ادغام مخرب یا خودکار بسته نمی‌شود.

## 2. دروازهٔ کشف رفتاری
CAPTURE → CLASSIFY → COMPARE → EVIDENCE → HYPOTHESIS → TEST → RECONCILE → PROMOTE OR KEEP IN QUEUE.
معنی: ثبت → طبقه‌بندی → مقایسه با موارد قبلی → شواهد → فرضیه → آزمون → تطبیق → ارتقا یا نگهداری در صف.
الگوهای رفتاری تعامل انسان، پاسخ AI، اجرای ابزار و محدودیت میزبان باید حفظ شوند؛ ثبت‌شدن، به‌تنهایی، مجوز ورود به معماری مادر نیست. موارد بدون شواهد کافی در صف OPEN / PENDING می‌مانند.

## 3. زمان و منشأ
زمان دقیق پیام کاربر ثبت نشده و UNKNOWN / UNVERIFIED باقی می‌ماند. زمان commit، زمان پیام، زمان اقدام و زمان بازخوانی رویدادهای جدا هستند؛ زمان ناموجود حدس زده نمی‌شود.

## 4. مقصدها و اثبات
- Repository: ثبت این رویداد و سند مرجع باید پس از نوشتن بازخوانی و تطبیق شوند.
- 0.0 Registry, Reference Index, Integration Queue, Behavior Trace: پیوندها باید جداگانه بازخوانی شوند.
- Buffer, Library, Persistent Memory, Dropbox: وضعیت مستقل؛ ثبت مخزن موفقیت آن‌ها را ثابت نمی‌کند.
- اجرای خودکار سراسری لنگرگذاری و آزمون رفتاری سرتاسری همچنان OPEN / NOT PROVEN است.

## 5. اقدام بعدی
1. بازخوانی این رویداد و سند مرجع.
2. بازخوانی دفتر مرکزی ۰.۰ و تأیید چهار گرهٔ مرجع و حفظ نقاط دیگر.
3. بررسی پیوندها در نمایه، صف معماری و دفتر رفتار.
4. ادامهٔ تطبیق همهٔ نقاط تاریخی و ثبت روابط فقط با شواهد.
5. هر الگوی تازه را قبل از ارتقا به Master، در دروازهٔ کشف رفتاری بررسی و آزمون کن.
