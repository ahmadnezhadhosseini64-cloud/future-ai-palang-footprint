# حاکمیت تداوم تصمیم و بازبینی وفادار
## DECISION CONTINUITY & REVIEW GOVERNANCE

- Stable ID: `DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE-2026-11-03-001`
- Production ID: `DCRG-HAIF-2026-11-03-001`
- Version: 1.0.0
- Status: ACTIVE / LIVING / REPOSITORY INTEGRATION IN PROGRESS
- Owner: احمد پلنگ (Ahmad Nezhadhosseini)
- Project: Future AI / Palang Footprint / HAIF
- Source chain: [POINT-0/061](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261030-061-ARCHITECTURE-GAP-RECONCILIATION.md) → [IN-100](../../0.0/anchors/PALANG-0.0-IN-20261103-100-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE.md) → [OUT-099](../../0.0/anchors/PALANG-0.0-OUT-20261103-099-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE.md) → [EVT-0246](../../architecture/BEHAVIOR-TRACE/EVT-0246-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE-2026-11-03.md) → [CURRENT-112](../../0.0/anchors/PALANG-0.0-CURRENT-20261103-112-DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE.md)
- Parent governance: [UIALAC](./UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md); [NPFAP](./NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Time policy: exact user-message time UNKNOWN / UNVERIFIED; actual repository commit time is recorded from Git metadata separately.

## 1. Purpose
Prevent human–AI collaboration from repeatedly reopening decisions that were already discussed, reasoned through and explicitly accepted. Preserve the user's prior intent and rationale across document reviews, task continuation and host handoffs, while keeping justified correction possible.

## 2. Core principle
**RETRIEVE → HONOUR → REVIEW ONLY ON TRIGGER.**
بازیابی تصمیم پیشین → وفاداری به نتیجهٔ توافق‌شده → بازبینی فقط با محرک معتبر.

A decision does not become undecided merely because a new turn, review, model, or session begins.

## 3. Decision record minimum
Every material settled decision should be represented, where applicable, by:
- decision ID and concise statement;
- owner/authority and decision scope;
- rationale and user intent;
- constraints, dependencies and affected artifacts;
- status: PROPOSED, UNDER DISCUSSION, SETTLED / ACTIVE, REOPENED, SUPERSEDED;
- source interaction/IN-OUT/event and canonical document;
- explicit reopening triggers;
- last verification and next action.

Do not invent a decision record for a casual remark or infer approval from silence. A user's explicit acceptance or a clearly recorded joint conclusion is required for SETTLED.

## 4. Mandatory review protocol
Before offering criticism, changing wording, proposing deletion, or revising an artifact:
1. Retrieve relevant prior decisions and their reasons.
2. Confirm whether the current artifact and context are still within the decision's scope.
3. Classify each proposed concern as:
   - objective defect supported by evidence;
   - new evidence or changed requirement;
   - material risk not previously considered;
   - optional alternative or stylistic preference.
4. If no valid reopening trigger exists, preserve the settled decision and do not repeat the earlier debate.
5. If a trigger exists, state what is new, show its evidence, explain its impact and ask for approval where the decision belongs to the user.
6. Preserve the previous decision, rationale and version lineage even if a new decision supersedes it.

## 5. Valid reopening triggers
A settled decision may be reopened only when at least one applies:
- reliable new evidence changes the factual basis;
- law, policy, technical requirement or external condition changes;
- a documented contradiction or inconsistency is found;
- an objective error is demonstrated;
- a material safety, legal, security or operational risk was not previously considered;
- the user explicitly asks to reconsider or revise it.

The assistant's preference, a generic checklist, a new session, forgetting the prior rationale, or the mere possibility of an alternative are not valid triggers.

## 6. Recovery after assistant drift
If the assistant reopens a settled decision without a valid trigger:
- acknowledge the specific continuity failure;
- retrieve and restate the prior decision and its rationale;
- restore the agreed direction without making the user repeat the earlier discussion;
- record the failure and correction if it is material or recurring;
- add a regression check so future reviews consult the decision ledger first.

## 7. Decision status and change control
- PROPOSED: not accepted.
- UNDER DISCUSSION: rationale or approval incomplete.
- SETTLED / ACTIVE: explicitly accepted and governs current work.
- REOPENED: a valid trigger exists; old decision remains preserved pending review.
- SUPERSEDED: a new decision was explicitly accepted; old decision remains in history.

Do not silently mutate a settled decision. A changed decision requires source, reason, approver, version and read-back.

## 8. Acceptance tests
- DCRG-AT-01: a later review retrieves the relevant settled decision and rationale.
- DCRG-AT-02: with no valid trigger, the system preserves it and does not present it as an error.
- DCRG-AT-03: alternatives are labelled as optional, not objective defects.
- DCRG-AT-04: with a valid trigger, the system identifies new evidence and impact, preserves the old decision and seeks approval when required.
- DCRG-AT-05: after a new session or host handoff, the decision can be recovered from the exported canonical records; actual host test receipt is required.
- DCRG-AT-06: assistant drift is acknowledged and corrected without requiring the user to repeat the original rationale.

All runtime tests remain NOT RUN until a real test and independent receipt exist.

## 9. Example and scope boundary
The source interaction involved an employment-certificate review where two previously discussed clauses were reopened without new evidence. The lesson is about continuity of decisions, not about making those certificate clauses universal policy. The certificate documents themselves are outside the scope of this architecture update and remain unchanged.

## 10. Integration map
This rule is incorporated by reference into:
- HAIF initial-model living mother;
- NPFAP cross-project foundational principles;
- UIALAC universal interaction/living architecture contract;
- 0.0 registry and CURRENT checkpoint;
- behavior-trace index and event record;
- Reference Index and sole active NEXT-051 queue;
- portable host instructions/recovery package, subject to independent conformance tests.

## 11. Status boundary
Repository write and exact read-back can prove that the rule is stored in this repository. They do not prove that ChatGPT Memory, Buffer, Library, Dropbox, another host, or background automation has synchronized or will enforce it. Those destinations remain separate and NOT VERIFIED until independently tested.
