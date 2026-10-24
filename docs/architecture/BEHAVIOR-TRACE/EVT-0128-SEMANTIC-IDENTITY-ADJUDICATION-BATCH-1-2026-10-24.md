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
