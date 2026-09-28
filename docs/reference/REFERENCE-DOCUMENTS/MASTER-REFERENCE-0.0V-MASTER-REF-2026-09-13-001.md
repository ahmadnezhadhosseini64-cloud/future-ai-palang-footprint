# سند مرجع معماری نقاط ۰.۰
## 0.0 Vault / Point-Lineage-Continuation Architecture

**Project:** Future AI / Palang Footprint  
**Owner:** احمد پلنگ  
**Reference:** Master / 0.0  
**Date:** 2026-09-13  
**Timezone:** Asia/Tehran (+03:30)

## 1. ایده اصلی

«نقطه ۰.۰» یک یادداشت موقت یا آخرین پیام نیست؛ یک **Continuation Anchor** است: نقطه‌ای قابل‌بازیابی که مسیر متوقف، نیمه‌تمام، منشعب یا ادغام‌شده بتواند از آن دوباره ادامه پیدا کند.

**۰.۰ = نقطه قابل‌بازیابی برای ادامه، نه نقطه قابل‌حذف یا جایگزینی.**

## 2. نتیجه دو مرحله چکش

دو مرحله «چکش» روی ایده معماری ۰.۰ انجام شد.

**Hammer 1 — بررسی معماری ایده:** مشخص شد زنجیره خطی به‌تنهایی کافی نیست، زیرا نزدیکی زمانی دو ۰.۰ الزاماً به معنی تبار یا ادامه‌بودن آن‌ها نیست.

**Hammer 2 — سخت‌سازی معماری:** مشخص شد معماری باید همزمان Permanent Registry، Lineage / Relationship Graph، Continuation Index و Recovery / Retrieval Layer داشته باشد.

نتیجه نهایی:

**0.0 Vault = Permanent Registry + Lineage Graph + Continuation/Recovery Index**

## 3. اصل هویت مستقل

هر ۰.۰ هویت مستقل خود را حفظ می‌کند. هیچ ۰.۰ حذف، جایگزین، buried یا invalidated نمی‌شود. Original Snapshot حفظ می‌شود و اطلاعات بعدی باید به‌صورت append / reconcile به آن اضافه شود؛ نه با بازنویسی خاموش تاریخچه.

## 4. ساختار اطلاعات هر ۰.۰

هر نقطه تا حد امکان دارای Stable ID، Production ID، Date، Exact Time، Timezone، Owner، Location/Context، Origin/Source، Creation Context، What Was Reached، Unresolved Remainder، Unresolved Reason، Status، Last Known State، Last Continuation Point، Parent/Related 0.0 References، Path/Track Identifier، Lineage State، Relationship State، Evidence/References، Possible Next Continuation و Last Update/Continuation Time است.

## 5. تفکیک وضعیت‌ها

`OPEN ≠ ERROR`  
`UNRESOLVED ≠ LOST`  
`PAUSED ≠ ABANDONED`  
`CONTINUATION NOT COMPLETED ≠ FINISHED`  
`RESOLVED ≠ DELETED`  
`UNKNOWN RELATIONSHIP ≠ CONFIRMED RELATIONSHIP`

همچنین:

`FOUND ≠ RETRIEVED ≠ REVIVED ≠ REGISTERED ≠ VERIFIED ≠ ACTIVE`

## 6. رابطه میان نقاط

رابطه میان دو ۰.۰ باید یکی از این وضعیت‌ها باشد:

- `CONFIRMED CONNECTION`
- `POSSIBLE CONNECTION`
- `INDEPENDENT`
- `UNKNOWN`

صرف شباهت موضوع، نزدیکی زمانی یا شباهت محتوا مجوز اتصال نیست.

## 7. Split / Branch و Merge

یک ۰.۰ می‌تواند به چند مسیر منشعب شود و چند مسیر نیز می‌توانند بعداً ادغام شوند. در هر دو حالت هویت نقاط اولیه حفظ می‌شود و نقطه جدید نیز هویت مستقل دارد. Merge و Split نباید باعث حذف تاریخچه شوند.

## 8. Master 0.0 در برابر 0.0 Vault

**Master 0.0** نقطه مرجع/Anchor اصلی است.  
**0.0 Vault** مخزن کامل نقاط، روابط، وضعیت‌ها، تبار، ادامه و بازیابی است.

Vault جای Master 0.0 را نمی‌گیرد؛ بلکه آن را به ساختار کامل نقاط و مسیرهای قابل‌بازیابی متصل می‌کند.

## 9. هدف اصلی Vault

دو خطر باید همزمان مهار شوند:

1. **Prevent Loss of Unfinished Paths** — هیچ مسیر نیمه‌تمامی به دلیل توقف یا گذشت زمان گم نشود.
2. **Prevent False Linkage** — مسیرهای مستقل به اشتباه یک زنجیره واحد فرض نشوند.

## 10. Last Known State و Last Continuation Point

`Last Message ≠ Last Continuation Point`

برای هر مسیر باید آخرین وضعیت شناخته‌شده و دقیقاً نقطه‌ای که ادامه باید از آن انجام شود حفظ شود.

`Stopped ≠ Finished`  
`Paused ≠ Abandoned`

مسیر حل‌شده نیز حذف نمی‌شود؛ `RESOLVED ≠ DELETED`.

## 11. Retrieval / Recovery

Vault باید بتواند نقاط OPEN، UNRESOLVED، PAUSED، CONTINUATION NOT COMPLETED، UNKNOWN-RELATIONSHIP، BRANCHED، MERGED و نقاطی را که مدت طولانی ادامه نیافته‌اند بازیابی کند و برای هرکدام Last Known State و Last Continuation Point را نشان دهد.

## 12. نقاط ۰.۰ شناخته‌شده فعلی

در معماری فعلی، Master 0.0 تاریخی، نقطه مربوط به مسیر ادغام‌شده Track A + Track B، و نقطه جدید 2026-09-13 حفظ شده‌اند. ترتیب زمانی به‌تنهایی رابطه تبار ایجاد نمی‌کند؛ هر رابطه باید متناسب با Evidence تعیین شود.

نقطه جدید 2026-09-13 با زمان `22:28` در `Asia/Tehran (+03:30)` به‌عنوان Anchor جدید حفظ شده و جایگزین نقاط قبلی نیست.

## 13. جایگاه معماری

`MASTER / 0.0`  
`↓`  
`0.0 VAULT`  
`├── Permanent Registry`  
`├── Lineage Graph`  
`├── Relationship Map`  
`├── Continuation Index`  
`├── Recovery / Retrieval`  
`└── Historical Preservation`

Vault با Production Registry، Recovery Architecture، Evidence / Validation، Persistent Memory Adapter و Continuation / Lineage مرتبط است.

## 14. Evidence Rules

`Evidence ≠ Interpretation`  
`Unknown ≠ False`  
`Unknown ≠ Extraordinary`  
`Compatible ≠ Proven`  
`Unresolved ≠ Supernatural`  
`No Evidence → No Strong Claim`

## 15. وضعیت ثبت این سند

**Production ID:** `0.0V-MASTER-REF-2026-09-13-001`  
**Type:** Canonical Reference Document  
**Status:** `ACTIVE / LIVING / PERMANENT`

این سند به‌عنوان سند مرجع معماری ۰.۰ در Repository پروژه ثبت می‌شود و برای بازیابی/انتقال معماری استفاده خواهد شد.

## 16. مرز Persistent Memory

ثبت در Repository و ثبت/تأیید مستقل در Persistent Memory دو ادعای متفاوت‌اند. این سند نباید بدون Evidence ادعا کند که Provider-level Persistent Memory نوشته یا Verified شده است.

وضعیت Persistent Memory در این مرحله:

`UNVERIFIED / PENDING`

## 17. اصل نهایی

**۰.۰ یک نقطه پایان نیست؛ یک لنگر قابل‌بازیابی برای ادامه مسیر است.**

**0.0 Vault یک آرشیو ساده نیست؛ مخزن دائمی نقاط + گراف تبار و رابطه + شاخص ادامه و بازیابی مسیرهاست.**

**هر ۰.۰ هویت مستقل خود را حفظ می‌کند؛ ارتباط‌ها باید با Evidence تعیین شوند؛ توقف هرگز به معنی پایان نیست.**
