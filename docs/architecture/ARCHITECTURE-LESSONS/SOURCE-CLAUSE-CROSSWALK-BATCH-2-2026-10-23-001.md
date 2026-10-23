# Source Clause → Rule → Component → Test Crosswalk — Batch 2

- Stable ID: PALANG-SOURCE-CLAUSE-RULE-TEST-CROSSWALK-2026-10-23-001
- Production ID: SCRTC-B2-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / PROVISIONAL / OPEN
- Governing master: [ULCG](../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md)
- Source map: [SRCMAP-2026-10-23-001](./SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md)
- Historic ledger: [HALML](./HISTORIC-LESSON-MIGRATION-LEDGER-2026-10-23-001.md)
- Current point 0: [CURRENT-023](../../0.0/anchors/PALANG-0.0-CURRENT-20261023-023-USER-CHECKPOINT-AND-CONTINUATION.md)
- Interaction: [IN-024](../../0.0/anchors/PALANG-0.0-IN-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md) / [OUT-024](../../0.0/anchors/PALANG-0.0-OUT-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md)
- Event/lesson: [EVT-0113](../BEHAVIOR-TRACE/EVT-0113-VISIBLE-CONTINUATION-AND-SOURCE-CLAUSE-EXCAVATION-2026-10-23.md) / [LAL-20261023-011](./lessons/LAL-20261023-011-VISIBLE-CONTINUATION-AND-RESUMABLE-WORK.md)
- Next checkpoint: [NEXT-025](../../0.0/anchors/PALANG-0.0-NEXT-20261023-025-SOURCE-RULE-TEST-CROSSWALK-AND-COLD-START.md)
- Retrieval method: full canonical file fetch, then section-heading and numbered-clause extraction. The blob SHA identifies the exact retrieved source version.

## Source retrieval evidence

| Alias | Canonical source | Blob SHA | Retrieved characters | Source version | Extraction status |
|---|---|---|---:|---|---|
| PIATGCG | [Permanent Interaction Anchoring, Timestamp Governance and Canonical Graph](../../reference/REFERENCE-DOCUMENTS/PERMANENT-INTERACTION-ANCHORING-TIMESTAMP-GOVERNANCE-AND-CANONICAL-GRAPH-MASTER-REFERENCE-2026-10-21-001.md) | `2212b390634a8a9530a3dce15fabd53762e478cd` | 32,006 | 1.1.0 | Full source fetched; clauses mapped provisionally |
| UIALAC | [Universal Interaction Anchor and Living Architecture Contract](../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md) | `12a37ffb1ba86080abfb39462468ac7c99f8125d` | 25,308 | 1.2.0 | Full source fetched; clauses mapped provisionally |
| ICMCRR | [Interaction Continuity Master–Child–Rahm Registration](../../reference/REFERENCE-DOCUMENTS/INTERACTION-CONTINUITY-MASTER-CHILD-RAHM-REGISTRATION-2026-10-20-001.md) | `438c7c75577800da0b7eb33ca88dc9a743f1e7fd` | 13,449 | 1.0.0 | Full source fetched; G-01…G-09 mapped provisionally |
| H0GLMR | [Historical 0.0 Graph Reconciliation Living Master](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-GRAPH-RECONCILIATION-LIVING-MASTER-REFERENCE-2026-10-21-001.md) | `6c746acb5d2ab9edff4b22fe42f8489335c123a3` | 62,106 | 1.0.0 | Full source fetched; historical snapshot rules mapped provisionally |
| STAR-HCR | [Semantic Timestamp Audit and Host Capture Recovery Master](../../reference/REFERENCE-DOCUMENTS/SEMANTIC-TIMESTAMP-AUDIT-AND-HOST-CAPTURE-RECOVERY-MASTER-REFERENCE-2026-10-21-001.md) | `cef495e5dc9c27ddfc10dbcb43396a907cdf3c92` | 10,809 | 1.0.0 | Full source fetched; runtime boundaries mapped provisionally |

## Provisional clause crosswalk

| Source clause / section | Extracted obligation (not a final merged law) | Component | Existing executable check or evidence | Status / unresolved question |
|---|---|---|---|---|
| PIATGCG §2, §4 — each material input/output and 0.0 anchor | Give each material IN and OUT an independent identity and explicit parent/next links; preserve older anchors. | IN/OUT ledger, 0.0 registry, canonical graph | CI continuity gate checks CURRENT-023, NEXT-024, IN-023/OUT-023, EVT-0112 and links; pair schema defines paired IDs. | Static graph enforcement exists; host-wide automatic capture NOT PROVEN. |
| PIATGCG §3 — time governance | Separate message time, processing time, repository commit time and read-back time; never infer one from another; UTC canonical commit time with Tehran equivalent. | Time-binding ledger, timestamp inventory and semantic audit | Living Architecture Audit includes repository timestamp inventory and semantic UTC/Tehran pair audit; each new time binding needs actual commit metadata. | Exact user-message time for IN-024 remains UNKNOWN; commit time is separate. |
| PIATGCG §5–6 — graph reconciliation and duplicates | Compare stable/production IDs, version, content and parent lineage; preserve collisions and supersession history rather than overwrite. | Historical graph manifest, edge validator, source map and conflict ledger | Graph manifest/edge validation and structural audit run in CI; prior failed audit evidence is retained. | Rule-level collision adjudication across all history remains OPEN (Issue #21). |
| PIATGCG §9–12 — destination proof and excavation | Each destination has independent status; excavation must end in registered or traceable pending/recovery state; record gaps and deterministic next action. | Registration queue, recovery register, source ledger and destination matrix | Repository read-back can be verified; destination-wide proof requires each destination's own test. | Buffer/library/persistent/external destination proof is not inferred from repository success. |
| UIALAC §4–6 — schema and registration lifecycle | Capture, anchor, classify, preserve, integrate, store, read back, match, verify, reconcile and report; every material item retains provenance and recovery pointers. | Pair ledger, registration orchestrator, indexes, queue | `interaction-pair-ledger.schema.json`, fixture validation and interaction-ledger workflow provide schema/fixture checks; structural audit checks architecture links. | Schema/workflow coverage is not proof every live conversation is captured. |
| UIALAC §7–8 — independent destinations and status vocabulary | Repository, buffer and persistent memory have independent states; REGISTERED, READ-BACK VERIFIED, VALIDATED and ACTIVE are not synonyms. | Destination state matrix and status vocabulary | Prototype reports WRITE_READBACK_VERIFIED for its SQLite path; CI tests must be cited for their exact scope. | Cross-destination integration remains OPEN unless each destination returns independent evidence. |
| UIALAC §9–13 — 0.0, recovery, automation limits and acceptance | Resume from the last valid checkpoint; preserve previous anchors; distinguish defined tests from passed tests; do not claim host-wide capture without runtime proof. | CURRENT/NEXT anchors, recovery bootstrap, Issue #20 | Existing interaction recovery implementation documents fresh-checkout recovery by input ID; prototype tests fresh app recovery against persisted SQLite. | Need confirm current workflow and test scope against current exact main SHA; host-wide capture still NOT PROVEN. |
| ICMCRR §1–4 — Master/Child/Rahm and portable recovery | Master governs accepted architecture, Child explores, Rahm validates; export must preserve source, lineage, rules, gaps and enough data to resume. | Initial-model master, portable HAIF package, validation workflow | Initial-model master and recovery bootstrap are repository artifacts; test claims must reference actual workflow result. | Validate all G-01…G-09 against current canonical records; no blanket closure by document presence. |
| ICMCRR §5 — G-01…G-09 acceptance gaps | Treat each gap as a separately identified acceptance obligation; close only with matching evidence. | Issue #20/#21, integration queue, open-gap register | Existing issue and queue links provide tracking; per-gap tests/evidence must be reconciled individually. | Current gap-to-test mapping is partial; unresolved gaps remain OPEN. |
| H0GLMR sections on historical graph, duplicates, aliases and snapshots | Historical counts and graph snapshots are time-bounded evidence; repeated IDs, mirrors and aliases require provenance and semantic adjudication. | Historical graph manifest, timestamp inventory, source census and collision ledger | Historical 0.0 graph audit and graph manifest/edge validation are executable CI steps. | Dated snapshots must not be presented as current counts; full tree/history census remains OPEN. |
| H0GLMR sections on reconciliation and audit scope | Structural existence/link validity does not prove semantic equivalence or canonical authority; keep uncertain collisions separate. | SRCMAP, HALML, reference index and reconciliation queue | Structural audit catches required IDs/links; semantic decisions require source comparison and recorded authority. | Human/source-authority adjudication is still needed for candidate collisions. |
| STAR-HCR — semantic UTC/time audit | Validate that paired UTC and Tehran times refer to the same instant; retain precision, source and event meaning. | Time-binding records and timestamp audit | Workflow includes semantic UTC/Tehran pair audit and timestamp inventory. | Exact final-main run evidence must be bound to the exact SHA; message timestamps stay unknown if not exposed. |
| STAR-HCR — host capture/runtime boundary | A schema, repository document or adapter is not proof of capture by every host; runtime hooks and observed retrieval tests are required. | Host adapter, interaction API, Issue #20 | Prototype exposes POST/GET paired interaction API, ID reverse lookup, idempotency/conflict checks and fresh-app recovery tests; separate workflow evidence is required for current code. | Prototype-scope evidence is not global ChatGPT capture proof. |
| STAR-HCR — destination-specific persistence and cold-start | Recover from persisted state, and prove each destination separately; cold-start means reloading durable state in a fresh process/context, not rereading the same in-memory object. | Interaction recovery tests, portable package, Issue #20 | Existing prototype test suite documents fresh app instance recovery against the same SQLite DB; workflow evidence must be inspected before promoting status. | Current exact-main runtime test and all external destinations remain OPEN / NOT PROVEN. |

## Cross-source interpretation

1. These sources converge on provenance, independent anchors, explicit time semantics, append-only lineage, per-destination proof, and recoverable continuation.
2. They serve different scopes. PIATGCG governs anchors/time/graph; UIALAC governs the registration lifecycle and status distinctions; ICMCRR governs Master–Child–Rahm and acceptance gaps; H0GLMR governs historical graph/snapshot reconciliation; STAR-HCR governs semantic timestamp and runtime/recovery proof.
3. Similarity is not equivalence. No source is marked superseded and no duplicate rule is merged by this crosswalk.
4. The named source fetch total is 19, not a complete repository tree/history census.
5. Tests are cited at the scope they actually exercise. Static CI link checks do not prove runtime-wide capture; prototype cold-start does not prove external persistence.

## Next actions

- Confirm actual workflow run IDs and tested SHAs for schema/fixture validation, reverse lookup and fresh-app recovery.
- Compare the 5-source clauses against the first 14 named-source batch; record conflicts, duplicates and authority decisions separately.
- Add source-clause matrix checks to the Living Architecture Audit.
- Keep Issue #21 open until full repository-tree/history census and semantic reconciliation pass; keep Issue #20 open until runtime and cold-start acceptance criteria pass.
