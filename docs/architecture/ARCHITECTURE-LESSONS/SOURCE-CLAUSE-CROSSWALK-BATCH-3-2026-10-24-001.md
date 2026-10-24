# Source-Clause Crosswalk Batch 3 — 2026-10-24

- Stable ID: PALANG-SOURCE-CLAUSE-CROSSWALK-BATCH-3-2026-10-24-001
- Production ID: SCRTC-B3-2026-10-24-001
- Version: 1.0.0
- State: SOURCE-FETCHED / RULE-EXTRACTED / PROVISIONAL / OPEN
- Governing master: ULCG v1.2.4
- Current point 0: CURRENT-036
- Next 0.0: NEXT-036
- Scope: five source artifacts fully fetched from canonical main and mapped clause-by-clause at the rule-family level. This is not the complete repository/history census.
- Time: source blob SHAs and character counts below are evidence; source registration time remains each source's actual last-change commit timestamp in UTC with Tehran derived from the same instant.

## Source inventory and provenance

| Source ID | Canonical path | Blob SHA | Characters | Provenance / version |
|---|---|---|---:|---|
| EXREG-GATE | `docs/protocols/EXCAVATION-TO-REGISTRATION-GATE-2026-09-02.md` | `9bdbf9c63673396d5e50cff8cabb1e972394cc8f` | 2,826 | Production ID EXC-REG-GATE-2026-09-02-001; FINAL / ACTIVE / LIVING |
| AUTO-FINAL-REG | `docs/architecture/AUTOMATIC_FINAL_REGISTRATION_ORCHESTRATOR.md` | `2b36f1c24eeff4eadd1f9f444f45173a8368ead0` | 3,490 | Rule ID AUTO-FINAL-REG-ORCH-2026-08-30-001; operational design; execution evidence required |
| 3LR-GOVREG | `docs/reference/REFERENCE-DOCUMENTS/THREE-LEVEL-GOVERNED-REGISTRATION-COMMAND-2026-10-06-001.md` | `78db3590df3317ba739c7684b727e17da3f4ee73` | 29,130 | Stable ID THREE-LEVEL-GOVERNED-REGISTRATION-COMMAND-2026-10-06-001; Version 1.1.4 |
| EIO-ANCHOR | `docs/reference/REFERENCE-DOCUMENTS/EVERY-INPUT-OUTPUT-ANCHOR-AND-COMPLETE-REGISTRATION-GOVERNANCE-2026-10-20-001.md` | `32c7194fc76c2393b1f64fe390422cf01b86cc14` | 9,553 | Stable ID EVERY-INPUT-OUTPUT-ANCHOR-AND-COMPLETE-REGISTRATION-GOVERNANCE-2026-10-20-001; Version 1.0.0 |
| EI-ANCHOR | `docs/reference/REFERENCE-DOCUMENTS/EVERY-INTERACTION-ANCHOR-AND-COMPLETE-REGISTRATION-GOVERNANCE-2026-10-20-001.md` | `a12b00090ffd3b19f7282df94f4befb6f57eaad1` | 16,145 | Stable ID EVERY-INTERACTION-ANCHOR-AND-COMPLETE-REGISTRATION-GOVERNANCE-2026-10-20-001; Version 1.0.0 |

## Rule-to-component-to-test matrix

| Source clause / rule family | Normalized rule (not a replacement for source text) | Connected component | Existing test / evidence | Status / unresolved gap |
|---|---|---|---|---|
| EXREG-GATE — Canonical Rule / Mandatory Transition | An excavation finding cannot end as finding-only. Every item must become REGISTERED or PENDING/RECOVERY under the same Production ID and provenance, with exact blocker and deterministic next transition. | Historic source ledger, recovery queue, registration gate, NEXT-036 | Structural source-graph gate and issue-linked recovery queue; individual recovered items still need status/evidence checks. | RULE EXTRACTED; per-item closure test and full census OPEN. |
| EXREG-GATE — mandatory lifecycle | RETRIEVE → IDENTIFY/CLASSIFY → VALIDATE → DEDUPLICATE → RECONCILE → COMPLETE → REVIVE/ABSORB → REGISTER → APPLY/TEST → EVIDENCE → READ-BACK → VERIFY → ACTIVE/LIVING. | Historic source census, reference master, evidence ledger, read-back verifier | Repository read-back and structural audit prove only the tested repository graph. | Lifecycle is normative; cross-destination proof not inferred. |
| AUTO-FINAL-REG — automatic lifecycle / pending queue / idempotent resume | Incomplete work stays owned and resumable; resume from the first unresolved gate without duplicate Production IDs or false completion. | Interaction registration orchestrator, pending/recovery queue, automation watchdog | Push/scheduled repository workflows and durable host-adapter tests exist; they do not prove every live conversation is captured. | DESIGN ACTIVE; runtime universal capture NOT PROVEN. |
| AUTO-FINAL-REG — triggers / finalization gates / failure handling | Triggers include new registration, main push, scheduled check, manual dispatch, and capability recovery. COMPLETE requires write, evidence, read-back, identity/content and destination-matrix reconciliation, provenance and audit. Failures remain pending/blocked/conflict with explicit blocker. | CI workflow, event trace, issue #20/#21, status matrix | Living Architecture Audit run 40069144491 passed the candidate graph; latest-main audit is separately gated. | Repository policy checks PASS on candidate; production orchestrator execution OPEN. |
| 3LR-GOVREG — three required levels | “ثبت کن” expands into full registration: repository, buffer, persistent memory, reference document, IDs, lineage, read-back and verification. Each destination has independent evidence/status. | Master reference, destination matrix, registration command, durable buffer and memory adapters | Repository registration/read-back is evidenced; Buffer/Persistent Memory destination proof is not inherited from repository success. | GOVERNING SPEC ACTIVE; cross-destination completion PARTIAL / OPEN. |
| 3LR-GOVREG — blocker and recovery chain | A technical blocker does not cancel the request: preserve available levels, keep the same Stable ID/lineage, record blocker, mark pending/blocked, recover and verify remaining levels. | Pending/recovery store, same-ID lineage, resumable queue | Issue #20 and #21 track unresolved runtime and historic work; bounded Git rollback evidence remains scope-limited. | Rule active; cold-start and external recovery OPEN. |
| EIO-ANCHOR — per-input/output anchor and time governance | Each material IN/OUT has independent identity, provenance, links, and explicit state. Message time is only recorded from a trustworthy source; commit time is a separate clock. | IN/OUT pair ledger, time-binding ledger, 0.0 registry, event trace | Timestamp inventory and semantic UTC/Tehran pair audit; CURRENT-036/IN-026/OUT-026 are linked. | Repository anchoring verified for this record; host-wide capture NOT PROVEN. |
| EI-ANCHOR — complete interaction lifecycle | Preserve the full user input and visible assistant output; link each to the event, master, 0.0 chain, affected components, evidence, blockers, and deterministic next action. Distinguish intent from executed action and unknown from false. | Interaction graph, behavior trace, master reference, verification checkpoint, NEXT-036 | Structural audit enforces current/next and paired anchors; no claim of unattended background execution. | Static graph PASS on candidate; universal live capture and cold-start OPEN. |

## Cross-source reconciliation

1. All five sources converge on identity/provenance preservation, explicit unresolved states, independent read-back, and no false completion.
2. The orchestration source describes triggers and resumability, but its own implementation boundary explicitly prevents treating a workflow definition as proof that every interaction is captured.
3. The three-level command source governs destination scope; repository/Library success does not establish Buffer/Persistent Memory/Dropbox completion.
4. The interaction-anchor sources govern per-interaction identity and time semantics; a repository commit timestamp must not be substituted for the original message time.
5. The excavation gate governs closure of discovered items: REGISTERED or same-ID PENDING/RECOVERY with a blocker and next transition. “Found” alone is not a terminal state.
6. These sources are linked but not collapsed into one authority. Conflicts or ambiguities must remain explicit until adjudicated with source/version evidence.

## Acceptance and next action

- Static graph: batch ID, source IDs, paths, blob SHAs, rule families and linked components are checkable by CI.
- Semantic mapping: PROVISIONAL until the complete repository/history census and conflict adjudication under Issue #21 finish.
- Runtime acceptance: OPEN under Issue #20; validate IN/OUT schema, reverse lookup from either side, cold-start recovery, and destination-specific read-back.
- Exact-final-main audit: OPEN / NOT CONFIRMED until a full audit run is tied to the exact main SHA.
- Next: continue source families beyond this five-source batch; preserve NEXT-022 through NEXT-036 and do not close Issue #20/#21 based on this partial crosswalk.


## Audit correction record
- Candidate Living Architecture Audit [run 40069565070](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40069565070) failed at the structural gate because the Integration Queue and 0.0 registry used the shorthand `SCRTC-B3` instead of the full required ID `SCRTC-B3-2026-10-24-001`.
- Cause: human-readable short label was present but the stable full identity was not present on those two surfaces; the CI check correctly rejected this incomplete link.
- Correction: add the full ID explicitly to both surfaces, retain the failed run as evidence, and rerun the audit. No previous evidence is deleted.
