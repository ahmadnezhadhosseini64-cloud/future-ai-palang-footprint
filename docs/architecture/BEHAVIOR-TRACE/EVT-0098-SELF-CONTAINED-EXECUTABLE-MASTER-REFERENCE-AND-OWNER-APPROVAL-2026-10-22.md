# EVT-0098 — سند مادر خودبسنده و دروازهٔ تأیید مالک

- Event ID / شناسهٔ رویداد: `EVT-0098`
- Stable ID / شناسهٔ پایدار: `EVT-0098-SELF-CONTAINED-EXECUTABLE-MASTER-REFERENCE-AND-OWNER-APPROVAL-2026-10-22`
- Interaction ID / شناسهٔ تعامل: `INT-20261022-011`
- Input / ورودی: [IN-20261022-011](../../0.0/anchors/PALANG-0.0-IN-20261022-011-SELF-CONTAINED-EXECUTABLE-MASTER-REFERENCE.md)
- Output / خروجی: [OUT-20261022-011](../../0.0/anchors/PALANG-0.0-OUT-20261022-011-SELF-CONTAINED-EXECUTABLE-MASTER-REFERENCE.md)
- Master standard / سند مادر: [SCEMRS v1.0.0](../../reference/REFERENCE-DOCUMENTS/PALANG-SELF-CONTAINED-EXECUTABLE-MASTER-REFERENCE-STANDARD-2026-10-22-001.md)
- Architecture / معماری: [HAIF master](../مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Registration governance / حاکمیت ثبت: [PIRHA](../../reference/REFERENCE-DOCUMENTS/PALANG-INTERACTION-REGISTRATION-AND-HISTORICAL-AUDIT-MASTER-REFERENCE-2026-10-22-001.md)
- Owner / مالک و تنها مرجع تصویب تغییرات حاکم: احمد پلنگ
- Exact user-message timestamp / زمان دقیق پیام کاربر: NOT CAPTURED; never replace with commit time.
- Status / وضعیت: WRITTEN; repository read-back and architecture integration must be independently checked.

## What changed
The owner requested that every master reference be self-contained and executable as the sole available document when transferred into another AI environment or app model. The receiving agent must know the project's goal, architecture, registration sequence, evidence rules, status distinctions, recovery procedure, and owner-approval gate without hidden memory.

## Behavioral observations
- User behavior observed: requires evidence that a master document actually exists; requires portability, completeness, and explicit human approval before architecture changes; separates creating a document from integrating it.
- Assistant/system behavior risk addressed: a document may be written but not self-contained, indexed, or integrated; a proposal may be mistaken for a completed change; an environment may claim external persistence without evidence.
- Architectural response: mandatory self-contained master-reference schema; explicit PROPOSE vs APPLY distinction; owner approval gate; acceptance checks; per-destination status and read-back.

## Factual boundaries
This event records the contract and repository operations. It does not claim the master document is already verified until read-back, matching and link/architecture checks are complete. It does not claim that a second AI environment, app model, Buffer, Persistent Memory, Dropbox, or a background service has been activated or tested.

## Acceptance tests
1. Fetch the master file back and verify Stable ID, version, owner approval rule, standalone runbook, transfer protocol and recovery rules.
2. Fetch input and output anchors back; verify their IDs and cross-links.
3. Verify PIRHA and HAIF masters link this standard and preserve the same owner-approval rule.
4. Verify reference index and 0.0 ledger list the standard/event.
5. Run repository link/audit workflow on the resulting snapshot; report structural and semantic results separately.
