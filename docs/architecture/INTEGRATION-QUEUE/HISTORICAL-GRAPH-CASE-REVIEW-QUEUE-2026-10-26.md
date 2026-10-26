# Historical Graph Case Review Queue — 2026-10-26

- Stable ID: HAIF-HISTORICAL-GRAPH-CASE-REVIEW-QUEUE-20261026-001
- Production ID: HAIF-HGCRQ-20261026-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVIDENCE-REQUIRED
- Root: [POINT-0/027](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-027-PATH-B-GAP-RECONCILIATION.md)
- Current checkpoint: [CURRENT-074](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-074-PATH-B-GAP-RECONCILIATION.md)
- Active parent queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Audit baseline: [Living Architecture Audit 40275138033](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40275138033), tested SHA e7e423a5070ca46abfd1365cf444298d2f8ba5a3, artifact ID 12629668562, artifact digest SHA-256 657c850dbd34d598179d88e6cdacfe47d032f0e22ded7a76aaef7de53d9c1297.

## 1. Baseline inventory (historical snapshot, not current truth after edits)

| Finding class | Count at baseline | Status |
|---|---:|---|
| Stable-ID collision groups | 63 total / 62 unreviewed | OPEN |
| Production-ID collision groups | 89 | OPEN; case-level status must be recomputed |
| Reference-ID collision groups | 7 | OPEN; case-level status must be recomputed |
| Event-number collision groups | 38 | OPEN; short numbers are not unique identity |
| Exact-content duplicate groups | 11 | Role proposals recorded; no deletion/merge authorized |
| Ambiguous parent edges | 13 | OPEN |
| Missing local Markdown links | 0 | Structural subgate passed on baseline only |
| Timestamp strings / parse ambiguity | 2,749 / 1 | One item needs raw value/path/line before adjudication |

The audit artifact contains machine-readable group and occurrence details. The current chat connector exposed the artifact metadata and digest but did not return its raw JSON payload; therefore this ledger does not fabricate the names or paths of all 62/89/7/38 groups or the 13 parent edges. Re-run/download the artifact or add a workflow step that publishes the case queue in an inspectable form before claiming individual closure.

## 2. Known source-backed ID role decisions

Source ledger: [semantic-role-decisions.jsonl](../../../data/interaction-pairs/semantic-role-decisions.jsonl).

- H0-ID-REVIEW-001 — shared governing concept: EVT-0022 is EVENT_PROVENANCE / ORIGIN_TRACE; the reference-vault document is CANONICAL_GOVERNING_REFERENCE_CANDIDATE. Keep both files.
- H0-ID-REVIEW-002 — Production ID 0.0V-2026-09-13-001: operational governance path and reference-vault mirror candidate have identical SHA-256. Keep both; no exclusive canonical promotion without link/lineage evidence.
- H0-ID-REVIEW-003 — Production ID 0.0V-ARCH-2026-09-13-001: operational architecture placement and reference-vault mirror candidate have identical SHA-256. Keep both; no exclusive canonical promotion without link/lineage evidence.

The new decision engine records partial source-backed coverage without treating a partially reviewed group as closed. Fresh audit output must confirm which of these decisions apply to the current path groups.

## 3. Exact-content duplicate queue

The existing [canonical alias and lineage decision register](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER-2026-10-21-001.md) records 11 groups: nine proposed role-based mirrors and two proposed earliest-commit aliases. These are proposals to preserve role/lineage, not file deletion instructions. Acceptance requires:
1. Current content SHA-256 and path read-back.
2. Git commit history for each path.
3. Inbound/outbound local-link inventory.
4. Role decision and evidence reference.
5. Post-decision graph rebuild; raw duplicate count remains visible.
6. No deletion, rename, or silent overwrite.

Known alias candidates:
- REG-2026-09-03-GAP-CLOSURE-OUTCOME-003 / -005 (identical-content alias candidate).
- REG-2026-09-03-GAP-CLOSURE-OUTCOME-001 / -002 (identical-content alias candidate).

Known mirror groups and their content hashes are enumerated in the linked decision register; keep the registry as the source of truth rather than duplicating a potentially stale copy here.

## 4. Event-number collisions

The [EVT collision adjudication register](../../reference/REFERENCE-DOCUMENTS/HISTORICAL-0.0-EVT-NUMBER-COLLISION-ADJUDICATION-2026-10-21-001.md) records six pairs as distinct event identities sharing short numbers: EVT-0005, EVT-0006, EVT-0019, EVT-0026, EVT-0029 and EVT-0030. Its addendum also classifies the two EVT-0050 files as distinct identities, and EVT-0051's mistaken graph-manifest path as a retained correction notice pointing to canonical EVT-0052. These classifications preserve files but do not prove every inbound reference has been disambiguated. New references must use full path and stable/production identity, not the short number alone.

## 5. Parent-edge review protocol — 13 baseline edges

Each edge needs a durable record with:
- source path and source SHA-256;
- raw declared parent token and line number;
- all candidate target paths and their SHA-256;
- inbound/outbound links and commit chronology;
- evidence-backed decision: UNIQUE / CANONICAL-PREFERRED / DISTINCT-LINEAGE / UNRESOLVED / AMBIGUOUS;
- reviewer rationale and evidence references.

Do not resolve by highest numeric suffix, newest file, filename similarity or identifier prefix alone. If two candidates remain plausible, preserve AMBIGUOUS and keep the child’s parent gate open.

## 6. Timestamp exception protocol — one baseline item

The raw offending value and path/line must be extracted from the fresh timestamp audit artifact. Record the raw string, parser failure, timezone context, source commit time and whether the value is a user/event timestamp or repository registration time. UTC repository commit time remains canonical; Asia/Tehran is derived from that same instant. Do not infer a missing user-message time from commit time.

## 7. Required next execution

1. Confirm partial-role tests pass on the exact current HEAD.
2. Run Living Architecture Audit and Portable RAHM Conformance on that same SHA.
3. Inspect the fresh artifact and persist a case-level JSON/Markdown queue with exact paths, lines, hashes and candidate links.
4. Resolve only cases meeting the evidence rule; leave the rest OPEN with reason and next action.
5. Read back the queue and all master/index/queue links.
6. Update counts only from the new audit receipt and keep old snapshots as historical evidence.

## Closure rule

This queue is not complete because it exists. Each case closes independently after source-backed decision, read-back and a fresh audit. Structural PASS does not imply semantic closure. Path A independent-host import remains a separate gate.
