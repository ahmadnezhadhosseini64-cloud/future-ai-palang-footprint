# سند مرجع مادر زنده — رسیدگی به برخورد شناسه‌ها، تبار اسناد و ابهام زمانی EVT-0089

- Stable ID: `PALANG-IDENTITY-COLLISION-AND-TIMESTAMP-RECONCILIATION-2026-10-22-001`
- Production ID: `PICTR-2026-10-22-001`
- Version: 1.0.0
- Owner / مرجع تصویب: احمد پلنگ
- Project: Future AI / Palang Footprint — HAIF
- Status: ACTIVE / LIVING / OPEN INVESTIGATION
- Interaction: `INT-20261022-012`
- Input: [IN-20261022-012](../../0.0/anchors/PALANG-0.0-IN-20261022-012-IDENTITY-COLLISION-AND-TIMESTAMP-RECONCILIATION.md)
- Output: [OUT-20261022-012](../../0.0/anchors/PALANG-0.0-OUT-20261022-012-IDENTITY-COLLISION-AND-TIMESTAMP-RECONCILIATION.md)
- Event: [EVT-0099](../../architecture/BEHAVIOR-TRACE/EVT-0100-IDENTITY-COLLISION-AND-EVT-0089-TIMESTAMP-RECONCILIATION-2026-10-22.md)
- Time binding evidence: recorded in Section 11 of this master; separate time-binding file creation was blocked, so no separate file is claimed.
- Exact user-message time: NOT CAPTURED.
- Canonical repository time: actual commit timestamp in UTC; Tehran equivalent is calculated from that same instant at UTC+03:30.

## 1. Purpose and non-negotiable rule
This living master governs the investigation of identity collisions, exact-content duplicates, event-number reuse, and the remaining timestamp ambiguity attributed to EVT-0089. It does not treat group counts as confirmed errors and does not authorize deleting, rewriting, or merging historical records without evidence and owner approval.

## 2. Current reported counts — inherited, not yet re-run
The following numbers are carried from the prior audit summary and user-provided report. They must be reproduced against a pinned commit and inspectable artifact before they can be described as the latest result:
- 57 Stable ID collision groups.
- 68 Production ID collision groups.
- 24 event-number collision groups.
- 7 Reference ID collision groups.
- 11 exact-content duplicate groups.
- Time audit: 1,294 timestamp strings inspected; 1,293 normalized; one unresolved/ambiguous item associated in the report with EVT-0089.
These are group counts, not confirmed error counts. One group may contain legitimate reuse across versions, branches, event relationships, or different semantic roles.

## 3. Required per-group forensic record
For every group, preserve:
1. Audit snapshot commit SHA, workflow run, artifact ID, script/version and execution timestamp.
2. Collision class and exact identifier.
3. All member file paths, line/record locations, content hashes, commit history and versions.
4. Role and lineage: parent/master, child/experiment, event trace, input/output anchor, index entry, supersession or duplicate copy.
5. Inbound/outbound references and whether the index agrees with the source document.
6. Decision category: `LEGITIMATE_REUSE`, `EXACT_DUPLICATE`, `IDENTITY_COLLISION`, `STALE_INDEX`, `VERSION_LINEAGE_GAP`, or `NEEDS_OWNER_DECISION`.
7. Evidence, confidence, proposed action, rollback, approval status and re-test result.

## 4. Safe resolution policy
- Never resolve a collision merely by renaming or deleting a file.
- Never assume same ID means same entity, or same content means the files have interchangeable roles.
- Preserve the original record, establish a canonical successor only after comparing roles and lineage, and add an explicit supersedes/alias mapping.
- Any change affecting governing architecture, master identity, deletion, or history requires explicit approval by Ahmad Palang.
- Keep unresolved groups in a durable open queue; `INCOMPLETE ≠ LOST`, `PENDING ≠ BURIED`.

## 5. EVT-0089 timestamp anomaly
The referenced report says one timestamp remains ambiguous and points to EVT-0089. The exact file/path and raw string have not yet been independently recovered in this registration. Therefore:
- Preserve the original text and report; do not guess a replacement.
- Retrieve the original audit artifact and identify the exact EVT-0089 file and timestamp field.
- Record source text, parser output, timezone interpretation, expected format and commit lineage.
- Recompute UTC/Asia-Tehran correspondence independently. Tehran is UTC+03:30 for this date; the Tehran value must derive from the same UTC instant, not a separate guessed time.
- If the source lacks enough information, retain `NEEDS_REVIEW` and request owner decision; do not fabricate missing precision.

## 6. Execution protocol
`PIN SNAPSHOT → FETCH ARTIFACT → EXTRACT GROUP MEMBERS → CLASSIFY ROLE/LINEAGE/VERSION → PROPOSE RESOLUTION → OWNER APPROVAL → APPLY NON-DESTRUCTIVELY → READ-BACK → MATCH → VERIFY → RE-RUN AUDIT → RECONCILE INDEX/ARCHITECTURE → STATUS`.

Before investigation, recover the project goal and the governing self-contained master. Register the complete input and output anchors independently before changing architecture. Every material action must have an event/time binding. A successful script run means the script completed; it does not mean the findings are resolved.

## 7. Closure criteria
A collision group closes only when every member has a documented role and lineage, a justified decision, preserved history, updated inbound/outbound references, and successful read-back/re-test. EVT-0089 closes only when the raw source and exact timestamp are identified and an independently reproducible interpretation is recorded. An audit with any unresolved semantic or time finding remains `REVIEW_REQUIRED`.

## 8. Portable execution instructions for another AI environment
If this is the only available document:
1. Read the entire document and report its ID/version/status.
2. Treat counts as inherited until a pinned-snapshot re-run confirms them.
3. Do not alter canonical history, timestamps, IDs, or architecture without explicit owner approval.
4. First create independent input and output anchors; then this master/event/time binding; then integrate into architecture and indexes.
5. Use only real repository/tool evidence. If a file/artifact cannot be fetched, report `BLOCKED / NOT FOUND` and the exact search attempted.
6. Separate `PROPOSE` from `APPLY`; owner approval is mandatory for semantic identity changes, merges, deletions, and governing architecture changes.
7. After every write, fetch the file back and verify expected fields. Re-run the audit on the new snapshot.
8. Report each persistence destination separately. Repository success does not prove Buffer, Persistent Memory, Dropbox, or another AI application has the same state.

## 9. Current open queue
- OPEN-1: locate exact audit artifacts and pin the snapshot for the reported collision counts.
- OPEN-2: enumerate all members of 57 Stable ID, 68 Production ID, 24 event-number, 7 Reference ID, and 11 exact-content groups.
- OPEN-3: identify the precise EVT-0089 timestamp string and source evidence.
- OPEN-4: classify role, lineage and version for each member.
- OPEN-5: propose non-destructive repairs and obtain owner approval before applying semantic changes.
- OPEN-6: re-run the audit after repair and reconcile architecture, reference index and 0.0 ledger.
- Dropbox, Buffer and Persistent Memory status: NOT VERIFIED by this document.

## 10. Version history
- v1.0.0: initial registration of this forensic reconciliation contract; reported audit counts preserved as inherited evidence, not claimed as freshly verified.


## 11. Repository time anchors and timestamp correction boundary

| Artifact | Commit SHA | UTC | Tehran equivalent |
|---|---|---|---|
| Input anchor IN-012 | `411739e3b395e9f7bb0f98e4a2c97e8059507cd5` | 2026-10-22T16:04:36Z | 2026-10-22T19:34:36+03:30 |
| Output anchor OUT-012 | `27cf94a34da58ce8d195aa5f472cc0dbc85820e1` | 2026-10-22T16:04:42Z | 2026-10-22T19:34:42+03:30 |
| Master initial registration | `62827ec2d7e32a2aaeee34ab9046825867f042c2` | 2026-10-22T16:04:47Z | 2026-10-22T19:34:47+03:30 |
| EVT-0100 registration | `3485d82a0a37fe26b3c992981765e40989e49bb8` | 2026-10-22T16:06:14Z | 2026-10-22T19:36:14+03:30 |
| Master event-link update | `9fd0c3e276a4a44029f27b71233cd9e26a44bf54` | 2026-10-22T16:06:38Z | 2026-10-22T19:36:38+03:30 |

All table times are actual Git commit timestamps. They do not represent the exact user-message time.

### EVT-0089 timestamp: evidence-based proposal, not applied
- Original audit finding: line 21 contains `2026-10-22 14:28` without a reliable timezone label in the local context inspected by the parser.
- Other existing EVT-0089 context states the conversation-observed time was `2026-10-22 14:28` Asia/Tehran (+03:30), minute precision. Seconds are not captured.
- Proposed source-faithful representation: `2026-10-22 14:28 Asia/Tehran (+03:30), minute precision; seconds NOT CAPTURED`.
- The write to the original EVT-0089 file was blocked; therefore the original text remains unchanged and the semantic audit still reports this item as unresolved. Do not claim resolution until a permitted edit is applied and a fresh audit confirms zero ambiguous items.
