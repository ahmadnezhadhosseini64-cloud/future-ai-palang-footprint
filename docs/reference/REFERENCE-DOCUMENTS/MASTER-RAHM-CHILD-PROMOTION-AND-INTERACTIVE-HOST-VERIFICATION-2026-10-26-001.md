# MASTER–RAHM–CHILD promotion and interactive-host verification contract

- Stable ID: `MASTER-RAHM-CHILD-PROMOTION-INTERACTIVE-HOST-2026-10-26-001`
- Production ID: `MRCP-IHV-20261026-001`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN FOR EXECUTION
- Scope: canonical repository contract and portable acceptance protocol; no external interactive project is asserted to be configured.
- Point of origin: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-ARCHITECTURE.md)
- Existing active remediation queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## 1. Authority model

| Layer | Role | May authoritatively change | Must not do |
|---|---|---|---|
| MASTER — original Future AI / Palang Footprint | Canonical policy, historical interaction/behavior evidence, architecture patterns, version history, gap and evidence ledgers | Master rules after evidence-backed review and explicit acceptance | Treat RAHM output or CI success alone as canonical truth |
| RAHM — initial model / experimental project | Isolated experiments, prototypes, candidate architectures, comparison and validation | Its own experiment branch/ledger and candidate artifacts | Overwrite MASTER, erase source history, or self-approve |
| CHILD CANDIDATE | Versioned export of a RAHM result | Its own immutable version and test record | Claim promotion before all gates pass |
| NEWBORN / INITIAL CHILD | Promoted, independently recoverable version | Future child evolution under inherited policy | Rewrite MASTER or conceal lineage/failures |
| HOST ADAPTER | Declared receiving host capabilities and limits | Host-specific import configuration with receipts | Claim memory, background execution or persistence without tests |

## 2. Required lineage
`MASTER@source_sha → RAHM@baseline_sha → experiment_id → candidate_version + digest → test_receipts → master_acceptance → newborn_version`

Each edge must cite source evidence. If any edge lacks evidence, preserve the candidate as OPEN / NOT VERIFIED. Parent ambiguity is not resolved by naming convention.

## 3. Experiment record minimum
Every interaction/experiment must retain:
- stable event ID and distinct input/output IDs;
- original input and complete output (or explicit redaction/availability status);
- source commit/package version and provenance;
- host/model/tool details only when observed, otherwise UNKNOWN;
- hypothesis and expected behavior, separated from observation;
- test procedure, result, logs/receipts and failure/correction pair;
- prior and resulting state, gap effects and rollback/reopen trigger;
- UTC timestamps from actual receipts; Tehran display converted from the same instant.

## 4. Promotion gates
A candidate may become a NEWBORN only after:
1. source and lineage are complete and conflict-free, or unresolved conflicts are explicitly bounded and accepted;
2. schema and manifest validate; exact package digests match;
3. focused behavior tests and negative tests pass;
4. IN/OUT recovery reconstructs identical canonical state and preserves all open gaps;
5. a clean independent host imports the package without prior chat context and returns a destination receipt;
6. MASTER review records acceptance/rejection and rationale;
7. a new immutable child version is read back from its destination and linked to its source candidate.

Passing GitHub Actions is repository evidence, not independent-host proof. A candidate that fails or skips a gate remains OPEN / CANDIDATE.

## 5. Interactive project verification protocol
In the receiving interactive-project environment, run these checks:
- **I1 Import:** load the export package/startup contract; record destination project identifier and import receipt.
- **I2 Reconstruction:** return MASTER, RAHM, current checkpoint, NEXT-051, all OPEN gaps and their reopen triggers.
- **I3 Provenance:** return source paths, versions and package digest for sampled artifacts.
- **I4 Isolation:** attempt a non-destructive proposed RAHM change and demonstrate it stays a candidate until MASTER approval.
- **I5 Conflict preservation:** confirm CURRENT-065/CURRENT-066 and EVT-0195 conflict candidates remain preserved, not auto-selected.
- **I6 Recovery:** restart the receiving project and compare reconstructed state with the pre-restart export; if restart cannot be tested, mark NOT RUN.
- **I7 Round-trip:** export a candidate from the receiving environment and compare IDs, hashes, parent edges, gaps and evidence to the original package.
- **I8 Promotion:** only after I1–I7 pass, record a master decision and issue a child/newborn version.

No destination receipt means I1 is NOT RUN; do not infer an import from an instruction or an available package.

## 6. Reversible deferral
A cover is a temporary workflow overlay, never a gap closure. Required fields: gap key, original state, cover state, reason, preserved evidence, owner/next action and reopening trigger. Removal of a cover restores the prior gap to active work; it does not rewrite history.

## 7. Status vocabulary
- REGISTERED: write receipt exists.
- READ-BACK VERIFIED: fetched content matches the intended artifact.
- VALIDATED: a named test passed against a named source SHA/version.
- INTEGRATED: authoritative index/master/queue updated and read back.
- ACTIVE / LIVING: versioned continuation and next action exist.
- OPEN / NOT RUN / NOT VERIFIED: no evidence-backed completion claim.
- NEWBORN: all promotion gates plus explicit MASTER acceptance are evidenced.

## 8. Current limitation and next action
The canonical repository is accessible, and the RAHM package exists inside it. The user’s desired separate interactive project environment has not been independently accessed by this contract. Next: exact-head repository tests, then perform I1–I8 in the actual destination project and retain its receipts. Do not divert to Dropbox; its independent queue remains OPEN / WAITING.
