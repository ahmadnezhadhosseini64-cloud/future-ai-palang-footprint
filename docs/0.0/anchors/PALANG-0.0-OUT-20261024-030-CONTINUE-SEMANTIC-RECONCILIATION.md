# OUT-030 — Source-backed semantic adjudication batch 1

- Anchor ID: OUT-20261024-030
- Stable ID: PALANG-0.0-OUT-20261024-030-CONTINUE-SEMANTIC-RECONCILIATION
- Production ID: OUT-030
- Interaction pair ID: INT-20261024-030
- Version: 1.0.0
- Status: REGISTERED / READ-BACK VERIFIED
- Input: [IN-030](./PALANG-0.0-IN-20261024-030-CONTINUE-SEMANTIC-RECONCILIATION.md)
- Previous checkpoint: [NEXT-029](./PALANG-0.0-NEXT-20261024-029-SEMANTIC-REVIEW-BATCH-2-AND-FRESH-SESSION.md)
- Current checkpoint: [NEXT-030](./PALANG-0.0-NEXT-20261024-030-SEMANTIC-REVIEW-BATCH-3-AND-COLD-START.md)\n- Event: [EVT-0128](../../architecture/BEHAVIOR-TRACE/EVT-0128-SEMANTIC-IDENTITY-ADJUDICATION-BATCH-1-2026-10-24.md)
- Decision register: [HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER-2026-10-21-001.md)

## Output
Three source-backed role decisions were added: one repeated Stable ID across EVT-0022 and its governing reference, plus two repeated Production IDs across operational/governance paths and their byte-identical Reference Vault mirror candidates. Git history, graph-manifest content hashes, explicit links, and inbound/outbound link counts were checked. The files are classified as event provenance and governing-reference candidate; neither is deleted or renamed.

## Evidence boundary
Read-back of the anchor text and its explicit pair/event/checkpoint links succeeded. CI evidence for the graph implementation is recorded in EVT-0128. Latest exact-head audit: run 40059261857, SHA d0bb633ade46b94bf20452c74efbc8137f4cbe99, artifact 12546287920 inspected, zero missing links, zero decode errors, three role decisions accepted. This anchor edit itself is documentation, not an additional code test.
