# EVT-0278 — New certificate branch Point 0 and next 0.0

- Trace ID: `EVT-0278`
- Stable ID: `PALANG-CERTIFICATE-NEW-POINT-0-AND-NEXT-0.0-2026-11-20`
- Project event: `CERT-EVT-20261120-003`
- Input: [CERT-IN-20261120-003](../../../گواهی/شروع-جدید-۳۰-آبان-۱۴۰۵/رویدادها/CERT-IN-20261120-003.md)
- Output: [CERT-OUT-20261120-003](../../../گواهی/شروع-جدید-۳۰-آبان-۱۴۰۵/رویدادها/CERT-OUT-20261120-003.md)
- New child root: [CERT-POINT-0-20261120-003](../../../گواهی/شروع-جدید-۳۰-آبان-۱۴۰۵/نقطه-۰-جدید-لنگر-ادامه-۲۰۲۶-۱۱-۲۰.md)
- Next checkpoint: [CERT-POINT-0.0-20261120-003](../../../گواهی/شروع-جدید-۳۰-آبان-۱۴۰۵/نقطه-۰-۰-بعدی-اقدامات-و-اتصال-نقاط-۲۰۲۶-۱۱-۲۰.md)
- Previous introduction anchor: `CERT-POINT-0PLUS-20261120-002`
- Previous CV checkpoint: `CERT-POINT-0.0-20261120-002`
- Global parent: POINT-0/064 → CURRENT-115 → NEXT-051 (unchanged).
- Status: ACTIVE / LIVING / OPEN; child-branch event, not a replacement for the global root.

## User instruction
The user explicitly requested: “اینجا رو نقطه ۰ کن و اقدامات رو نقطه ۰.۰ بعدی و اتصال بده ب باقی نقاط”.

## Observed behavior
The user is explicitly setting the current conversational position as a new local root and assigning the execution/action record to its successor 0.0 checkpoint. The user expects additive continuity to prior points, not replacement or deletion of them.

## Architectural handling
1. Keep global Palang root POINT-0/064 and its CURRENT-115 / NEXT-051 lineage unchanged.
2. Create a local certificate child-branch Point 0 for this new stage.
3. Record the execution actions in the next local 0.0 checkpoint.
4. Preserve all prior certificate anchors, including CERT-POINT-0.0-20261120-002 and CERT-POINT-0PLUS-20261120-002.
5. Preserve the immutable introduction baseline CERT-INTRO-BASELINE-20261120-001; no content edit is authorized.
6. Distinguish repository registration, CI validation, and independent-host recovery; never overstate one as another.

## Trace chain
`CERT-IN-20261120-003` → `CERT-OUT-20261120-003` → `CERT-EVT-20261120-003` → `CERT-POINT-0-20261120-003` → `CERT-POINT-0.0-20261120-003` → this EVT-0278 → Behavior Trace index / Reference Index / certificate living master.

## Timestamp integrity
- Processing-time reference at start: `2026-11-20T11:29:57+03:30` Asia/Tehran.
- UTC equivalent: `2026-11-20T07:59:57Z`.
- This is not asserted to be the exact user-message receipt time.
- Per-file Git timestamps must be obtained from actual commit metadata after each write.
- Time-binding and final receipt are separate evidence artifacts.
