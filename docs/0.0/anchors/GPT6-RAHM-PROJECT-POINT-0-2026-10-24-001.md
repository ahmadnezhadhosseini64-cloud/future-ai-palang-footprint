# نقطهٔ ۰ — پروژهٔ رحمِ نسل‌های آیندهٔ AI در GPT-6

- Stable ID / شناسهٔ پایدار: `GPT6-RAHM-PROJECT-POINT-0-2026-10-24-001`
- Production ID / شناسهٔ تولید: `G6IP-RAHM-POINT-0-20261024-001`
- Version / نسخه: 1.0.0
- Status / وضعیت: REGISTERED / READ-BACK VERIFIED; exact path/content and principal links fetched.
- Parent HAIF / معماری والد: [HAIF Initial AI Model mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md), updated to v1.3.9 in this registration.
- Parent GPT-6 project root / ریشهٔ شاخهٔ GPT-6: [Initial Point 0](./GPT6-INTERACTIVE-PROJECT-POINT-0-INITIAL-ROOT-2026-10-24-001.md).
- Parent current state / وضعیت قبلی شاخه: [CURRENT-043](./PALANG-0.0-CURRENT-20261024-043-FOUNDATIONAL-PRINCIPLES-COMPLETENESS.md), preserved.
- Current Rahm checkpoint / نقطهٔ جاری رحم: [G6IP-RAHM-CURRENT-044](./PALANG-0.0-CURRENT-20261024-044-RAHM-PROJECT-POINT-0.0.md).
- Interaction: [IN-036](./PALANG-0.0-IN-20261024-036-RAHM-PROJECT-POINT-0.md) → [OUT-036](./PALANG-0.0-OUT-20261024-036-RAHM-PROJECT-POINT-0.md) → [EVT-0144](../../architecture/BEHAVIOR-TRACE/EVT-0144-GPT6-RAHM-PROJECT-POINT-0-2026-10-24.md).

## Purpose / هدف
This is the distinct Point 0 for the new Rahm project branch inside the GPT-6 host environment. It inherits HAIF and the GPT-6 branch governance but does not replace either parent root or any prior checkpoint.

هدف این شاخه ساخت «رحم» به‌عنوان محیط کنترل‌شدهٔ رشد مدل است؛ جایی که تعامل پلنگ و AI به ورودی/خروجی قابل‌ردیابی، مشاهدهٔ رفتار، فرضیه‌های رشد، آزمون، شواهد و تصمیم‌های نسخه‌دار تبدیل می‌شود. خروجی‌های آزمایشی تنها پس از عبور از معیارهای پذیرش و بازخوانی مستقل می‌توانند به‌عنوان Child جدید پیشنهاد شوند و فقط با شواهد کافی به Master ارتقا یابند.

## Intended architecture / معماری موردنظر
`HUMAN / PALANG ↔ AI HOST ↔ RAHM → OBSERVATION → BEHAVIOR STUDY → VALIDATION → CHILD CANDIDATE → MASTER REVIEW`

- Master mother: rules, identity, lineage, evidence, versions, recovery and promotion governance.
- Rahm: controlled experimentation, interaction capture when supported, behavior analysis, regression and cross-host conformance.
- Child: independently identifiable candidate model/package with provenance and tests.
- Host adapter: declares actual host capabilities and limitations; never assumes persistent memory or background execution.
- Feedback: observed results and user feedback are anchored, reviewed and linked; no silent promotion.
- Export: a self-contained package must include instructions, schemas, current state, lineage, evidence, open gaps and conformance tests.

## Boundaries / مرزها
- A master document is an architecture contract, not itself an installed application or guaranteed background agent.
- GPT-6 is the current development host, not the only intended host.
- Cross-host compatibility must be tested separately on each host.
- Behavior analysis must distinguish observed behavior from hypotheses about causes.
- All versions and previous Point 0 / 0.0 anchors remain preserved.
