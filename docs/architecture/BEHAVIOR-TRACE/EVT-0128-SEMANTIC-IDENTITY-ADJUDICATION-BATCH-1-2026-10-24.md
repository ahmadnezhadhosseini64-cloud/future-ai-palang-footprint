# EVT-0128 — Semantic identity adjudication, batch 1

- Event ID: EVT-0128
- Stable ID: PALANG-SEMANTIC-IDENTITY-ADJUDICATION-BATCH-1-2026-10-24-001
- Production ID: SIAB1-HAIF-2026-10-24-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / ONE-GROUP-ROLE-ADJUDICATED / SEMANTIC-RECONCILIATION-OPEN
- Parent: [EVT-0127](./EVT-0127-DEEP-REPOSITORY-AUDIT-AND-GAP-REGISTER-2026-10-23.md)
- Active checkpoint: [NEXT-028](../../0.0/anchors/PALANG-0.0-NEXT-20261023-028-POST-REPAIR-AUDIT-AND-SEMANTIC-RECONCILIATION.md)
- Decision register: [HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER-2026-10-21-001.md)
- Canonical master: [CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)

## Source-backed finding
Reviewed repeated Stable ID `ACTIVE-LIVING-EVERY-INPUT-OUTPUT-ANCHOR-TEST-AND-PERMANENT-OPERATING-RULE-2026-10-20-001` and Production ID `ALEIOAT-PALANG-2026-10-20-001` across the EVT-0022 event trace and its fuller governing reference.

Evidence at audit SHA `ffc4fb8136cdd4168910f8c0ba58d6619fddfa13`:
- Event content SHA-256: `966409f3f21f8814dee60310b81993271490b6b6cb19f1c5937f199f281d38af`.
- Reference content SHA-256: `52822f45817dd18d48392f13e0da526cda0261d1ee7691e757d6517e66c96688`.
- Reference commit `2e9fb693b48cc34c89349bca3cb3044f90e1dd23`, UTC `2026-10-20T10:06:24Z`; event commit `3394f983124cb80850a8fd9fa5c10a87897b1794`, UTC `2026-10-20T10:07:02Z`.
- The event explicitly links to the governing reference. The audited graph recorded 1 inbound / 5 outbound links for the event and 6 inbound / 7 outbound links for the reference.

## Decision
- Event path role: `EVENT_PROVENANCE / ORIGIN_TRACE`.
- Reference path role: `CANONICAL_GOVERNING_REFERENCE_CANDIDATE`.
- Status: `SOURCE-REVIEWED / ROLE-ADJUDICATED / HISTORICAL-PATHS-PRESERVED`.
- The shared identifiers express one governing concept represented by two different document roles; the files are not interchangeable.
- No IDs were rewritten; no file was deleted; no historic anchor was overwritten.

## Remaining gaps and next actions
- Structural collision counters remain unchanged until the audit pipeline consumes the role-decision register.
- This is one reviewed group only; all other collision groups remain open until individually adjudicated.
- 13 ambiguous parent edges, 11 proposed aliases and the unresolved timezone at EVT-0089 line 21 remain open.
- Fresh-session recovery remains a separate test; Issues #20 and #21 remain open.
- Continue source/history/link-based review one group at a time; add regression tests so role decisions remain visible to audits. Run Living Architecture Audit, Behavior Hunter and Cross-Layer Integrity Gate on identifiable SHAs and inspect artifacts.


## Independent CI and artifact proof — source SHA `c54ea409d43d0650066433b63bf364c9ae9e2279`
- Living Architecture Audit [run 40058599484](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058599484): SUCCESS on the exact source SHA above; artifact `12546426252` downloaded and inspected; ZIP SHA-256 `881f6edd39e2f2e836e21e84ddee3f0f9b90a58c53a18a99950293308ce66b4e`.
- Audit snapshot: 2,708 total files, 865 source files, 3,687 local-link edges, 0 missing local links, 0 decode errors. Raw counts remain 60 Stable-ID, 71 Production-ID, 7 Reference-ID and 30 event-number collision groups; 11 exact duplicate groups; 13 ambiguous parent edges; 11 proposed aliases.
- The generated manifest independently applied two source-hash-verified role decisions: one Stable-ID group and one Production-ID group; remaining unreviewed groups are 59 Stable-ID and 70 Production-ID. Raw collision counts remain unchanged by design.
- Behavior Hunter [run 40058599527](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058599527): SUCCESS; 67 tests passed on the same SHA; artifact `12546421339` inspected; ZIP SHA-256 `b3d9e3c05044a57fd4485112b4a446427e1b7ad76bb4ec9184574ae4d4c1b8cf`. Append-only architecture ledger PASS (2 records, hash chain verified); proposal gate READY_FOR_OWNER_REVIEW, evidence VERIFIED, promotion false.
- Cross-Layer Integrity Gate [run 40058599467](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058599467): SUCCESS on the same SHA.
- Main later advanced to evidence-only commit `0d13be4be55aa6c29efb95ce00aa39f29314a19a` at `2026-10-24T03:30:48Z`; this exact later HEAD was not rerun. The successful proofs are for source SHA `c54ea...`.
- Audit also caught a generated `__pycache__/*.pyc` file as a non-text source node in an earlier run. The graph builder now excludes Python bytecode; the final artifact above shows zero decode errors. The failed/interim audit artifact remains part of the history.


## Latest source-hash-aware graph audit — run 40058848054
- [Living Architecture Audit run 40058848054](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058848054): SUCCESS on SHA `871e02fb87e2ff04db380dcad64fc1bd0939e8a6`; artifact `12546671470` inspected; ZIP SHA-256 `6c15a33dc10a9e6f83bde49f7f6c3ae4d01501e00e92f5ed43d086659a131199`.
- Manifest: 2,712 total files, 865 source files, 3,689 local-link edges, zero missing local links, zero decode errors. Raw collisions remain visible; the manifest marks one Stable-ID and one Production-ID group ROLE-ADJUDICATED, with 6 line-level occurrences reviewed and 1,417 still unreviewed.
- Six dedicated semantic-role unit tests passed in the audit workflow. Cross-Layer Integrity Gate [40058848116](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058848116) and Reconciliation Acceptance Test [40058848140](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058848140) also passed on the same SHA.
- Failure lesson preserved: an interim run [40058772530](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40058772530) failed because a literal escaped newline was inserted into the Python count dictionary. The run log identified the exact SyntaxError; the line was repaired and the later audit passed. The preceding run also exposed generated Python bytecode entering the graph; the builder now excludes `__pycache__` and `.pyc` files, and the final artifact reports zero decode errors.
- Current main HEAD at verification was exactly `871e02fb87e2ff04db380dcad64fc1bd0939e8a6`; the audit artifact's commit equals the current HEAD observed at that check.


## Interaction pair and continuation
- Current pair: [IN-030](../../0.0/anchors/PALANG-0.0-IN-20261024-030-CONTINUE-SEMANTIC-RECONCILIATION.md) / [OUT-030](../../0.0/anchors/PALANG-0.0-OUT-20261024-030-CONTINUE-SEMANTIC-RECONCILIATION.md), interaction ID `INT-20261024-030`.
- Active successor: [NEXT-029](../../0.0/anchors/PALANG-0.0-NEXT-20261024-029-SEMANTIC-REVIEW-BATCH-2-AND-FRESH-SESSION.md).
- Decision ledger: `data/interaction-pairs/semantic-role-decisions.jsonl` contains H0-ID-REVIEW-001 and H0-ID-REVIEW-002; both are source-hash-verified by the graph builder on the audited source SHA.


## Additional adjudication — H0-ID-REVIEW-003
- Third source-backed Production-ID role decision: `0.0V-ARCH-2026-09-13-001`, shared by `architecture/0.0-VAULT-ARCHITECTURAL-PLACEMENT-2026-09-13.md` and `docs/reference/REFERENCE-DOCUMENTS/0.0-VAULT-ARCHITECTURAL-PLACEMENT-0.0V-ARCH-2026-09-13-001.md`.
- Both paths have identical content SHA-256 `d3921368cf3ad35d6b428860c67ad47f4e395c731f9249dc7b84006614558dad` at audited SHA `871e02fb87e2ff04db380dcad64fc1bd0939e8a6`.
- Git history: operational path `dfbed7d0c4e55a4d0caf443a0fd2b310dccd369e` at `2026-09-13T19:14:10Z`; reference copy `af9cdb562ec54fc7df0ac07b99a60d69a0ef372a` at `2026-09-28T22:31:02Z`. Both had zero inbound/outbound local links in the audited manifest.
- Roles: `OPERATIONAL_ARCHITECTURE_PLACEMENT_CANDIDATE` and `REFERENCE_VAULT_MIRROR_CANDIDATE`. The role distinction is recorded; exclusive canonical promotion remains provisional. No rename/delete/merge.
- Machine-readable decision `H0-ID-REVIEW-003` was appended to `data/interaction-pairs/semantic-role-decisions.jsonl`; the next audit must prove it is accepted against the exact current source hashes.
