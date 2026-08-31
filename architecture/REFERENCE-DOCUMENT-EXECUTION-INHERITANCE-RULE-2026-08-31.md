# سند مرجع — قاعده اجرای خودکار شمول سند مرجع

**شناسه:** REF-EXECUTION-INHERITANCE-2026-08-31-001
**تاریخ:** 2026-08-31
**زمان:** ثبت واقعی Repository
**مالک:** Ahmad Nezhadhosseini
**موقعیت:** ایران، گنبدکاووس
**پروژه:** Future AI / Palang Footprint
**نقطه مرجع:** 0.0
**نوع:** Permanent Operational Rule
**وضعیت:** ACTIVE / LIVING / PERMANENT
**نسخه:** 1.0

## اصل
از این پس هرگاه کاربر صرفاً فرمان «ثبت کن» را صادر کند، منظور پیش‌فرض آن ثبت کامل تولید مطابق قواعد حاکم معماری است؛ کاربر نباید مجبور باشد برای هر سند، تولید، تست، اصل، قانون، Evidence، Checkpoint یا رکورد جدید دوباره بگوید «طبق قاعده جامع ثبت کن».

## اجرای خودکار
دستیار باید هنگام هر تولید جدید، قواعد جامع فراداده و Provenance را به‌صورت پیش‌فرض اعمال کند، موارد قابل‌اعمال را تشخیص دهد، شناسه و هویت لازم را ایجاد کند، وضعیت و مرز ادعا را مشخص کند و در صورت ادعای ثبت واقعی، Write → Read-back → Verify را انجام دهد.

## مرز
این قاعده به معنی «موفق فرض کردن» نیست. اگر ابزار، مجوز، اتصال یا هر Gate لازم موجود نباشد، باید همان محدودیت صریحاً گزارش شود و ثبت موفق ادعا نشود.

## یادآوری آرشیوی
در صورت خطای اجرایی یا جاافتادن Metadata/Provenance، این سند و سند `REF-UNIVERSAL-METADATA-2026-08-31-001` باید به‌عنوان Reference Reminder مبنا قرار گیرند.

## رابطه با قاعده جامع
`REF-UNIVERSAL-METADATA-2026-08-31-001` قاعده مادرِ فراداده و شمول است؛ این سند قاعده اجراییِ ارث‌بری و اعمال خودکار آن در هر تولید جدید است.

## English
Whenever the user says only “register it,” the default meaning is complete registration under all applicable governing architecture rules. The user must not repeat the instruction to apply the universal metadata/provenance rule for every new artifact.

The assistant shall automatically apply applicable metadata, provenance, status, evidence boundary, and verification requirements. No successful registration may be claimed without the required real execution and read-back verification.

**Status:** ACTIVE / LIVING / PERMANENT.
