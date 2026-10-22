# TIME-BINDING-UIOAM-2026-10-22-001 — پابند زمانی ورودی/خروجی

- Stable ID: PALANG-TIME-BINDING-UIOAM-2026-10-22-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / EVIDENCE-BINDING
- Canonical rule: commit timestamp from actual GitHub commit metadata in UTC; Tehran = UTC+03:30 from same instant.

## زمان مشاهدهٔ ورودی
- User message observed: 2026-10-22 14:28 Asia/Tehran (+03:30), minute precision based on conversation metadata.
- This is not commit time and not an exact-second claim.

## ثبت این زنجیره
این پابند پس از ایجاد هر فایل باید با SHA و commit timestamp واقعی به‌روزرسانی شود. زمان commit فایل‌های اولیه و فایل‌های الحاقی متفاوت است؛ جدول نهایی باید برای هر فایل، آخرین commit واقعی را نشان دهد. timestampهای یک فایل قدیمی پس از تغییر آن دیگر canonical نیستند.

## آثار مرتبط
- [EVT-0089](./EVT-0089-UNIVERSAL-INPUT-OUTPUT-ANCHORING-GOVERNANCE-2026-10-22.md)
- [UIOAM master](../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-INPUT-OUTPUT-TEMPORAL-ANCHOR-MASTER-2026-10-22-001.md)
- [IN anchor](../../0.0/anchors/PALANG-0.0-IN-20261022-002-UNIVERSAL-IO-ANCHORING.md)
- [OUT anchor](../../0.0/anchors/PALANG-0.0-OUT-20261022-002-UNIVERSAL-IO-ANCHORING.md)
- [LBAF master](../../reference/REFERENCE-DOCUMENTS/LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)

## GAP
تا استخراج commit metadata و بازخوانی نهایی، این پابند در وضعیت PENDING / NOT FULLY VERIFIED است. زمان API، زمان پیام و زمان commit با هم خلط نمی‌شوند.


## جدول پابند commitهای این نوبت
تمام UTCهای زیر از GitHub commit metadata خوانده شده‌اند؛ زمان تهران برابر UTC+03:30 است.

| Artifact | Commit SHA | UTC | تهران |
|---|---|---|---|
| EVT-0089 | 8276d6e103266225b8533e0f38a703b3db5766e8 | 2026-10-22 10:59:24Z | 2026-10-22 14:29:24+03:30 |
| IN-20261022-002 | 9ef5a5bbff4b0e51769b3c0b18ba7c64c022371b | 2026-10-22 10:59:35Z | 2026-10-22 14:29:35+03:30 |
| OUT-20261022-002 | 6355822989ae52982c28ea98cd7be1a0ee713ce2 | 2026-10-22 11:00:28Z | 2026-10-22 14:30:28+03:30 |
| UIOAM master | b6cc4a4215c4a558f237b476da3b8edf20106a90 | 2026-10-22 11:00:39Z | 2026-10-22 14:30:39+03:30 |
| First version of this binding | 590d6710c6900d09cb9f4beab0babac1b5144802 | 2026-10-22 11:00:49Z | 2026-10-22 14:30:49+03:30 |
| LBAF master link update | 2cc31e8b50da7995babc81f25ab7b7c99c36a608 | 2026-10-22 11:01:19Z | 2026-10-22 14:31:19+03:30 |
| Initial architecture append | 117b86436a15ae92f0d5fd6da6b6f76d92b3b20f | 2026-10-22 11:01:30Z | 2026-10-22 14:31:30+03:30 |
| Canonical continuation master | 0a4937463b68d525284cea7501a1baff0afa8c8b | 2026-10-22 11:01:41Z | 2026-10-22 14:31:41+03:30 |
| Behavior trace index | c7c118d71ba51ce9c7b1b4f77454d5d2f95f8542 | 2026-10-22 11:01:52Z | 2026-10-22 14:31:52+03:30 |
| 0.0 index | 560b6863cd1e4bd16a0f4174079f01532c69b871 | 2026-10-22 11:02:05Z | 2026-10-22 14:32:05+03:30 |
| Reference index | 6811af73f293867cddb8b43114fb65fa91d0cd84 | 2026-10-22 11:02:16Z | 2026-10-22 14:32:16+03:30 |

If any listed artifact is amended again, its row becomes historical and must be replaced by the latest actual commit for that file in a new binding revision. The timestamp of this binding's current revision must be read from its own commit metadata after this update; it is intentionally not guessed here.
