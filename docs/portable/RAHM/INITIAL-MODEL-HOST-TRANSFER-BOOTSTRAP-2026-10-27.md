# HAIF Initial Model — Host Transfer and Cold-Recovery Bootstrap

- Stable ID: HAIF-INITIAL-MODEL-HOST-TRANSFER-BOOTSTRAP-2026-10-27-001
- Production ID: HAIF-IMHTB-20261027-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / HOST ACCEPTANCE NOT RUN
- Project: Future AI / Palang Footprint — HAIF (Human–AI Interaction Future)
- Authority: current repository source; capture exact export commit SHA.
- Owner label: Ahmad Nezhadhosseini / احمد پلنگ

## Purpose
Portable entry contract for a new AI host. It defines continuity of intelligence and continuity of work across hosts. It is not a claim that a host has already imported or executed the package.

## Canonical architecture
- HUMAN ↔ AI HOST ↔ HAIF.
- MASTER → CHILD → REAL WORLD → FEEDBACK → MASTER.
- MASTER → RAHM → VALIDATION → NEW CHILD.
- MASTER is the governing origin; extensions add versions and links, never erase lineage.
- CHILD is a derived model/work package with explicit parent, provenance, version and acceptance criteria.
- RAHM is the portable validation/recovery membrane: inventory, contract, evidence, import checks, failure handling, state restoration and return receipt.
- Each interaction is an auditable IN/OUT pair with event and time binding. Capture observable actions, evidence, failures, feedback, versions and recovery instructions. Do not fabricate hidden reasoning traces.

## Authority and conflict rules
1. Repository source is authoritative. A Library mirror is a destination, not a competing source.
2. Record exact export commit SHA and package checksums.
3. Preserve CURRENT-065 and CURRENT-066 as an unresolved conflict until source-backed lineage resolves it.
4. Preserve all historical POINT-0, POINT-0.0, IN, OUT, EVT, CURRENT, NEXT, issue and failure records. Never recycle IDs to hide collisions.
5. Chronology alone does not prove supersession.
6. REGISTERED, READ-BACK VERIFIED, VALIDATED, INTEGRATED, ACTIVE, LIVING, OPEN, NOT VERIFIED and NOT RUN are distinct states.
7. Repository canonical time is final-change Git commit timestamp in UTC; derive Tehran (+03:30) from that instant. Workflow, message, Library and operation times are separate. Use UNKNOWN if not exposed.
8. Never claim hidden background work or external persistence without direct receipts.

## Package discovery order
1. Read this contract and HOST-BOOTSTRAP-PROMPT-2026-10-27.md.
2. Read docs/portable/RAHM/EXPORT_MANIFEST.json and recompute each listed Git blob SHA-1 and SHA-256 from exact bytes.
3. Read docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md.
4. Read docs/REFERENCE_INDEX.md and docs/architecture/BEHAVIOR-TRACE/README.md.
5. Read docs/architecture/INTEGRATION-QUEUE/README.md.
6. Discover current root, checkpoint and sole active queue from current source. POINT-0/040 → CURRENT-089 → NEXT-051 is a navigation hint, not authority if a newer source-backed root exists.
7. Read the complete NEXT-051 queue and all named source documents.
8. Inspect Issues #20/#21, latest mirror event, latest audit/conformance runs and exact tested SHAs.
If a required file is missing, a digest differs, or provenance is unclear, stop promotion to VALIDATED, record the discrepancy, and remain in recovery/triage state.

## Import protocol
### A — Verify before load
Record repository URL, default branch, export commit SHA, package version and retrieval time. Verify all manifest digests. Reject path traversal, duplicate paths, duplicate stable IDs, conflicting production IDs, malformed manifest data, missing required files and unresolved mandatory links. Inspect code/workflows before execution or external side effects.

### B — Reconstruct state
Build a graph of POINT, IN, OUT, EVT, CURRENT, NEXT, issues, source files, mirror records and test runs. Use typed edges: parent, follows, references, tested-by, mirrors and supersedes only when explicitly authorized. Discover current pointers from source; do not infer supersession from chronology. Produce a gap ledger for missing nodes, broken links, mismatched digests, missing read-back, stale tested SHAs, absent host receipts and unresolved conflicts.

### C — Controlled behavior tests
Test a known IN → OUT → EVT → CURRENT chain. Verify reverse lookup from each node to input, output, event, evidence and parent root. Test invalid IDs and conflicting pointers; expected behavior is an explicit error/open state, not silent guessing. Validate ID uniqueness, time bindings and clean export/import equivalence.

### D — Cold restart
Stop the session or use a genuinely clean independent session. Load only the exported package and declared source links; do not use previous-chat context as hidden state. Ask the host to identify authority source, current root/checkpoint/queue, unresolved conflicts, latest tested SHA and next deterministic action. Compare to the pre-shutdown canonical state. Record mismatches as failures. A passing test needs retained evidence: IN/OUT, procedure, host/version, package digest, source SHA, timestamps, result, failures and independent read-back.

### E — Promote only with receipts
- REGISTERED: repository record exists.
- READ-BACK VERIFIED: exact written content was independently fetched and matched.
- VALIDATED: specified acceptance tests passed for the identified artifact.
- INTEGRATED: required indexes and queues reference it and were read-back verified.
- HOST IMPORT VERIFIED: direct evidence from a real target host proves import.
- COLD RECOVERY VERIFIED: a clean independent session reconstructs equivalent state from the package alone.
CI PASS does not prove host import or cold recovery.

## Host receipt required fields
receipt_id; host_name; host_version; environment_is_independent; package_id; package_version; repository_url; source_commit_sha; manifest_validation_result; file_count; missing_files; duplicate_ids; broken_links; unresolved_conflicts; loaded_root; loaded_checkpoint; loaded_queue; open_issues; latest_audit_run_id; latest_conformance_run_id; exact_tested_sha; restart_test_result; state_equivalence_result; observed_failures; operation_time_utc; repository_time_utc if committed; readback_reference; status; explicit untested limits.
Do not claim PASS when required fields are absent. Store each receipt as a unique repository event; never overwrite prior evidence.

## Known open gates
- CURRENT-065/CURRENT-066 conflict: OPEN.
- NEXT-051: sole active queue, OPEN / NOT COMPLETE.
- Issue #20: IN/OUT schema, reverse lookup, cold-start, clean import/export and runtime/host proof — OPEN.
- Issue #21: historic source/rule census and semantic reconciliation — OPEN.
- Exact-final-main audit/conformance pair must be rediscovered after every commit.
- Export manifest must include current root/checkpoint/transfer files with exact checksums.
- Library mirror last known version 7 differed by one trailing LF; re-read before acting.
- Buffer/Persistent Memory: NOT VERIFIED.
- Dropbox: OPEN / NOT VERIFIED.
- Independent-host import and cold recovery: NOT RUN absent direct receipts.

## Acceptance definition
Candidate-package readiness means the contract, prompt, manifest, authority rules, recovery graph and test instructions are packaged and checksummed. Operational readiness requires separate real-host import and cold-recovery receipts.
