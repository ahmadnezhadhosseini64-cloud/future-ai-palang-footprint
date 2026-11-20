# POINT-0/068 — اتصال چندمیزبانی و تکامل تحت حاکمیت مالک

- Stable ID: GPT6-RAHM-USER-POINT-0-20261120-068-OWNER-GOVERNED-MULTI-HOST-EVOLUTION-0PLUS
- Status: ACTIVE / LIVING / 0+ / APPEND-ONLY
- Parent: POINT-0/067 → CURRENT-120
- Current architecture: [معماری اتصال چندمیزبانی و تکامل تحت حاکمیت مالک](../../architecture/مدل%20اولیه%20AI/معماری%20اتصال%20چندمیزبانی%20و%20تکامل%20تحت%20حاکمیت%20مالک.md)
- New input/output: IN-111 → OUT-110
- Event: EVT-0286
- Current checkpoint: CURRENT-121
- Sole execution queue: NEXT-051

## اصل نقطه
میزبان‌های متصل، گره‌های مستقل تعامل و تولید مشاهده/شاهد/پیشنهاد هستند. آن‌ها از طریق مخزن می‌توانند به تکامل تحت نظارت کمک کنند، اما اختیار مستقیم تغییر سند مادر یا شاخه اصلی ندارند. مسیر اجباری:
HOST → QUARANTINE → VALIDATION → RAHM → CHILD CANDIDATE → OWNER APPROVAL → MASTER.

## قواعد
- دسترسی پیش‌فرض میزبان جدید READ-ONLY است.
- پیشنهادها و شواهد باید منشأ، میزبان، نسخه مرجع، hash و زمان قابل اثبات داشته باشند.
- ورودی میزبان نامطمئن است و پیش از پذیرش باید قرنطینه، پالایش و راستی‌آزمایی شود.
- چند میزبان یا توافق اکثریت جایگزین شاهد مستقل و تأیید مالک نیست.
- نوشتن مستقیم میزبان روی main، merge خودکار، ارتقای خودکار و انتقال خام مکالمه ممنوع/غیرفعال است.
- هر میزبان قابل ممیزی، محدودسازی و قطع اتصال است.
- ثبت معماری، به‌تنهایی پیاده‌سازی آداپتر یا اتصال واقعی را ثابت نمی‌کند.

## زنجیره
POINT-0/066 → CURRENT-119 → POINT-0/067 → IN-110 → OUT-109 → EVT-0285 → TIME-BINDING-EVT-0285 → CURRENT-120 → POINT-0/068 → IN-111 → OUT-110 → EVT-0286 → TIME-BINDING-EVT-0286 → CURRENT-121 → NEXT-051.

این نقطه ادامهٔ ریشهٔ دائمی موجود است، نه ریشه یا صف موازی.

## Successor link — POINT-0/069
POINT-0/068 continues to [POINT-0/069 (0+)](GPT6-RAHM-USER-POINT-0-20261120-069-PERMANENT-INTERACTION-LEDGER-0PLUS.md) → [IN-112](PALANG-0.0-IN-20261120-112-PERMANENT-INTERACTION-LEDGER.md) → [OUT-111](PALANG-0.0-OUT-20261120-111-PERMANENT-INTERACTION-LEDGER.md) → [EVT-0287](../../architecture/BEHAVIOR-TRACE/EVT-0287-PERMANENT-INTERACTION-LEDGER-2026-11-20.md) → [TIME-BINDING-EVT-0287](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0287-PERMANENT-INTERACTION-LEDGER-2026-11-20.md) → [CURRENT-122](PALANG-0.0-CURRENT-20261120-122-PERMANENT-INTERACTION-LEDGER.md) → NEXT-051. The permanent event ledger preserves actual interactions; it does not bypass quarantine or owner approval.
