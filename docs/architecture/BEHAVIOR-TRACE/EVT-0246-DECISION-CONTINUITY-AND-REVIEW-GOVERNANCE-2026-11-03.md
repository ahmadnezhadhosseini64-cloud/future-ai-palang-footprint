# EVT-0246 — درس رفتاری تداوم تصمیم و بازبینی وفادار

- Stable ID: `HAIF-EVT-0246-DECISION-CONTINUITY-20261103`
- Production ID: `HAIF-EVT-0246`
- Version: 1.0.0
- Parent root: [POINT-0/061](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261030-061-ARCHITECTURE-GAP-RECONCILIATION.md)
- Input: [IN-100](../../0.0/anchors/PALANG-0.0-IN-20261103-100-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE.md)
- Output: [OUT-099](../../0.0/anchors/PALANG-0.0-OUT-20261103-099-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE.md)
- Current: [CURRENT-112](../../0.0/anchors/PALANG-0.0-CURRENT-20261103-112-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE.md)
- Sole active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Canonical rule: [Decision Continuity & Review Governance](../../reference/REFERENCE-DOCUMENTS/DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE-2026-11-03-001.md)
- Status: OBSERVED / REGISTERED; repository integration and exact read-back are pending at creation. Runtime enforcement NOT VERIFIED.

## 1. Observed interaction
During collaborative editing of an employment certificate, the user and assistant had previously discussed and settled the purpose of two clauses. In a later quality review, the assistant reopened those same choices as possible issues without presenting new evidence or a changed requirement. The user identified the inconsistency. The assistant acknowledged that it had failed to carry forward the prior rationale and restored the agreed decisions.

The two certificate-specific choices are evidence of the interaction pattern only; this event does not revise the certificate or turn its wording into a universal template.

## 2. Behavioral finding
A review that ignores a relevant, previously accepted decision creates avoidable rework, weakens trust, and makes the user repeat context. The failure is not that the assistant reviewed the document; it is that the review did not first retrieve and respect the already settled decision and its rationale.

## 3. Architectural rule proposed
- Maintain a retrievable decision ledger: decision, rationale, owner/authority, scope, status, source anchor, constraints, and valid reopening triggers.
- Load relevant decisions before critique, rewriting, recommendations, or handoff to another host.
- Preserve SETTLED / ACTIVE decisions unless new evidence, changed conditions, documented contradiction, demonstrable error, material unconsidered risk, or explicit user request triggers review.
- Label alternatives as alternatives, not defects.
- On justified reopening, show the new evidence and impact; preserve the prior decision and lineage.
- Never claim cross-session memory or host enforcement solely because a rule was committed to the repository.

## 4. Evidence boundary
This event is based on the current conversation and the user's explicit correction. Exact user-message timestamps are not independently available and remain UNKNOWN. The repository commit timestamp will be recorded separately from the message time. No external-host behavior test is claimed.

## 5. Required integration
The rule is proposed for the canonical interaction contract, foundational architecture principles, HAIF living mother, behavior-trace index, 0.0 registry, reference index and the sole active queue NEXT-051. Integration requires write → read-back → match → link reconciliation. Do not create NEXT-052.
