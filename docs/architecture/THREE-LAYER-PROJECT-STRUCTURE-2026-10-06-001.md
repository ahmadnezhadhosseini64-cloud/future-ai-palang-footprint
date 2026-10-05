# Three-Layer Project Structure — Future AI / Palang Footprint

**Stable ID:** THREE-LAYER-PROJECT-STRUCTURE-2026-10-06-001
**Production ID:** 3LR-STRUCT-2026-10-06-001
**Status:** ACTIVE / LIVING / REGISTERED
**Parent:** THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001

## Canonical structure

/Future AI/Palang Footprint/
- docs/reference/REFERENCE-DOCUMENTS/ — سندهای مرجع کامل و Canonical
- docs/architecture/ — کنترل‌ها و معماری‌های پروژه
- docs/reports/THREE-LAYER/ — گزارش‌های سه‌سطحی
- registry/ — Registry تولیدها و 0.0
- Registration Buffer/
  - سند مرجع/ — نسخه کامل قابل‌بازیابی اسناد مرجع
  - reports/THREE-LAYER/ — کپی پایدار گزارش‌های سه‌سطحی

## Three-surface rule

هر Production یک Stable ID و Production ID دارد و همزمان برای سه سطح ثبت/تلاش می‌شود:

Repository + Persistent Memory + Buffer

هر سطح وضعیت مستقل دارد و هیچ سطحی وضعیت دیگری را به ارث نمی‌برد.

## Reference Document rule

سند مرجع کامل باید در Reference Documents ثبت شود. Buffer نیز نسخه کامل هم‌هویت را نگه می‌دارد تا در محدودیت مقصد، بازیابی کامل ممکن باشد.

## Operational rule

ثبت جدید:
CAPTURE → ONE ID → COMPLETE PAYLOAD → THREE-SURFACE REGISTRATION → STATE CAPTURE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS

در صورت محدودیت:
PRESERVE SAME ID → RECORD BLOCKER → KEEP COMPLETE BUFFER PAYLOAD → EXCAVATE/RETRY → VERIFY → RECONCILE → CLOSE

## Memory boundary

Persistent Memory یک سطح مستقل معماری است؛ اما تا وقتی ابزار Provider-level Write + independent Read-back در Runtime در دسترس نباشد، وضعیت آن NOT-VERIFIED / CAPABILITY-GAP است و Repository/Buffer جای آن را نمی‌گیرند.
