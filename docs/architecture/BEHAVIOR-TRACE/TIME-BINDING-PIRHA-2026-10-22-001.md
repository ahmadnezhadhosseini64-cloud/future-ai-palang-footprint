# پابند زمانی — PIRHA / حاکمیت ثبت تعاملی و ممیزی تاریخی

- Stable ID / شناسهٔ پایدار: `TIME-BINDING-PIRHA-2026-10-22-001`
- Production ID / شناسهٔ تولید: `TB-PIRHA-2026-10-22-001`
- Master / سند مادر: [PIRHA](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md)
- Pair / زوج تعامل: `INT-20261022-009`
- Event / رویداد: [EVT-0095](EVT-0095-INTERACTION-GOVERNANCE-AND-HISTORICAL-AUDIT-2026-10-22.md)
- Historical event / رویداد تاریخی تکمیل‌شده: [EVT-0093](EVT-0093-REGISTRATION-CONTINUATION-2026-10-22.md)
- Rule / قاعده: آخرین تغییر ثبت مخزن بر اساس metadata واقعی commit به UTC گرفته می‌شود؛ زمان تهران از همان لحظه با اختلاف +03:30 محاسبه می‌شود. زمان دقیق پیام کاربر جداست و در این تعامل در دسترس نیست.

## زمان‌های ثبت اولیه

| مورد | Commit SHA | UTC مرجع | تهران |
|---|---|---|---|
| EVT-0093 — فایل مستقل رویداد تاریخی | `714d3a58f276eb5557ed71d7332da483ac07dd61` | 2026-10-22T14:37:37Z | 2026-10-22T18:07:37+03:30 |
| IN-20261022-009 | `5c56e2fa6ad98062e338bd067ca3a65a88cf3569` | 2026-10-22T14:37:41Z | 2026-10-22T18:07:41+03:30 |
| OUT-20261022-009 | `916c74732390ea0518fb55c88adef61d0276c546` | 2026-10-22T14:37:46Z | 2026-10-22T18:07:46+03:30 |
| PIRHA master v1.0.0 | `0056c53f73b3b31fd321206e7a05e644916dc3e9` | 2026-10-22T14:38:53Z | 2026-10-22T18:08:53+03:30 |
| EVT-0095 | `4c8496429e76045a6559dd3181b593e14e5b2684` | 2026-10-22T14:39:14Z | 2026-10-22T18:09:14+03:30 |
| HAIF mother model v1.2.0 | `5018c1e5f59518615fd532e628c3328e4c6b749f` | 2026-10-22T14:40:19Z | 2026-10-22T18:10:19+03:30 |
| Reference index update | `c6621c102dd47fdc00f195abfa57de490fb10b7d` | 2026-10-22T14:41:09Z | 2026-10-22T18:11:09+03:30 |
| Integration queue update | `522f460848907cab42269c7e43370a73585fe47c` | 2026-10-22T14:41:44Z | 2026-10-22T18:11:44+03:30 |
| Zero checkpoint update | `3088cbd3ef303123332b5a592b0ddd27df708fae` | 2026-10-22T14:42:01Z | 2026-10-22T18:12:01+03:30 |
| 0.0 checkpoint update | `f81a112b108f42aae9c892f68bd984d01a37bc7d` | 2026-10-22T14:43:00Z | 2026-10-22T18:13:00+03:30 |

## Historical correction
The older `TIME-BINDING-PRC-2026-10-22-001.md` explicitly said standalone EVT-0093 creation was unconfirmed. This file was created in the current interaction; after read-back, that old statement must be updated to point to this file and mark the existence of EVT-0093 as confirmed at repository level.

## Last-change metadata and limitations
The timestamps above are initial creation/update commits for those items. Later revisions must be appended with their actual commit SHAs and timestamps. The latest-change timestamp of this time-binding file itself is determined from its own commit metadata after creation and cannot be embedded in the same commit without another revision.

## Verification boundary
This file is a time-binding record, not evidence of a completed full historical semantic audit. Buffer, Persistent Memory and Dropbox remain independently unverified.
