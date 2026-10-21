# دفتر داوری معنایی دستهٔ شناسه‌ها — تعریف در برابر ارجاع

- Stable ID: HISTORICAL-0.0-IDENTIFIER-ROLE-REVIEW-BATCH-001-2026-10-21
- Production ID: H0IRRB-2026-10-21-001
- Version: 1.0.0
- Project: Future AI / Palang Footprint — HAIF
- Owner: احمد پلنگ
- Date: 2026-10-21
- User-message time: UNKNOWN / UNVERIFIED
- Status: ACTIVE / LIVING / PARTIAL
- Parent baseline: [H0SAB](./HISTORICAL-0.0-SEMANTIC-ARCHITECTURE-BASELINE-2026-10-21-001.md)
- Structural findings: [H0GAF](./HISTORICAL-0.0-GRAPH-AUDIT-FINDINGS-2026-10-21-001.md)
- Related correction: `scripts/build_historical_graph_manifest.py`

## Method

For each repeated ID, inspect the exact source lines, determine whether each line defines its own document or refers to another document, search for the actual canonical definition, and record the role decision. Scanner groups are triage signals only. A missing definition in the group is a parser coverage warning, not proof that no definition exists.

## Batch 1 — Stable ID: CERTIFICATE-INBOX-0.0-FOURTH-LETTER-02-2026-10-19-001

### Evidence retrieved

1. `docs/reference/REFERENCE-DOCUMENTS/گواهی/گواهی های ارسالی اولیه/لنگر ادامه و قرارداد دائمی ثبت کن - صندوق گواهی.md`
   - Its own top-level Stable ID is `CERTIFICATE-INBOX-CONTINUITY-REGISTER-COMMAND-2026-10-19-001`.
   - The repeated target ID appears later inside the document as a reference to the independent fourth 0.0 checkpoint.
2. `docs/reference/REFERENCE-DOCUMENTS/گواهی/گواهی های ارسالی اولیه/لنگر پایان نوبت و ادامه پروژه - ۲۰۲۶-۱۰-۱۹.md`
   - Its own top-level Stable ID is `CERTIFICATE-INBOX-SESSION-HANDOFF-2026-10-19-001`.
   - The repeated target ID appears under a subsection naming “نقطهٔ ۰.۰ چهارم — نامهٔ شمارهٔ ۲”; this is a reference, not this document's own ID.
3. Search and source retrieval located the actual definition:
   `docs/reference/REFERENCE-DOCUMENTS/گواهی/گواهی های ارسالی اولیه/نقطه ۰.۰ چهارم - گواهی درخواست اولیه شماره ۲.md`
   - Its metadata states “شناسهٔ پایدار این نقطه: CERTIFICATE-INBOX-0.0-FOURTH-LETTER-02-2026-10-19-001”.
   - Therefore this file is the definition candidate; the two paths listed by the old collision table are references.

### Decision

- First path: REFERENCES.
- Second path: REFERENCES.
- Actual fourth-point file: DEFINES.
- Identity-conflict result: NOT A TRUE IDENTITY CONFLICT based on this evidence.
- Parser finding: the previous metadata regex did not recognize the bilingual/Persian definition label, so the actual definition was omitted from the scanner's collision group. The regex in `scripts/build_historical_graph_manifest.py` was expanded to recognize bilingual/Persian Stable ID and Production ID metadata labels. The next workflow run must prove the fix and regenerate counts.
- Closure boundary: the role of these three occurrences is adjudicated; all links around the certificate inbox should still be included in the full reference-graph audit.

## Batch 2 — Stable ID: INITIAL-NAVIGATION-SOLUTION-HUMAN-AI-2026-10-19-001

### Evidence retrieved

1. Canonical source:
   `architecture/INITIAL-NAVIGATION-SOLUTION-HUMAN-AI-2026-10-19-001.md`
   - Top-level metadata defines this Stable ID and Production ID `INS-HUMAN-AI-20261019-112500-TEHRAN`.
2. `architecture/HUMAN-AI-COEVOLUTION-ARCHITECTURE.md`
   - The ID appears in an architecture integration section pointing to the canonical artifact path; this is a reference.
3. `docs/governance/0.0-VAULT/MASTER-REFERENCE-2026-09-13.md`
   - The ID appears beside the related document path in a section describing the later navigation solution; this is a reference.

### Decision

- `architecture/INITIAL-NAVIGATION-SOLUTION-HUMAN-AI-2026-10-19-001.md`: DEFINES.
- `architecture/HUMAN-AI-COEVOLUTION-ARCHITECTURE.md`: REFERENCES.
- `docs/governance/0.0-VAULT/MASTER-REFERENCE-2026-09-13.md`: REFERENCES.
- Identity-conflict result: NOT A TRUE IDENTITY CONFLICT based on source roles reviewed.
- Architectural relation: the canonical navigation solution is a later interaction/continuity artifact referenced from the co-evolution architecture and the older 0.0 master reference. Preserve the older reference as lineage; do not treat it as a second definition.

## Parser correction and required regression

The prior extractor accepted only a narrow English metadata form such as `Stable ID:` and `Production ID:`. This omitted real definitions expressed as `Stable ID / شناسهٔ پایدار:` or `شناسهٔ پایدار این نقطه:`, leaving references to look like duplicate definitions. The regex was broadened in the existing manifest builder. The next audit must:
1. run on the commit containing the regex correction;
2. retrieve the resulting manifest artifact;
3. confirm both definition paths appear as nodes with the expected IDs;
4. compare the old and new occurrence-group counts and inspect any newly surfaced groups;
5. retain all old snapshots as history; do not overwrite historical metrics;
6. rerun local-link and parent-edge validation.

## Results

- Two identifier occurrence groups reviewed.
- One group exposed a metadata-parser omission and was reclassified as two references plus one definition.
- One group was reclassified as one definition plus two references.
- No files were deleted, renamed or silently rewritten.
- These are bounded batch decisions; they do not close all 33/42 repeated-occurrence groups or prove the semantics of all 493 files.

## Next batch

Review the remaining Stable ID groups in the findings register, prioritizing:
1. groups with more than two paths;
2. groups containing two or more event/checkpoint paths;
3. bilingual/Persian metadata labels;
4. any ID for which the supposed definition is absent from the group;
5. Production ID groups that overlap exact-content duplicate groups.


## Batch 2 continuation — ARCHITECTURE-INTEGRATION-QUEUE-2026-10-12-001

### Source evidence read-back
1. `docs/architecture/INTEGRATION-QUEUE/README.md` has this ID in its own top-level identity block: `Stable ID: ARCHITECTURE-INTEGRATION-QUEUE-2026-10-12-001`, with Production ID `AIQ-2026-10-12-001`. Role: DEFINES.
2. `docs/reference/REFERENCE-DOCUMENTS/CANONICAL-COMPLETE-PATH-ARCHIVE-2026-10-19/MASTER-CANONICAL-COMPLETE-INTERACTION-AND-REGISTRATION-PATH-2026-10-19-001.md` contains the same ID inside its P1 section describing the architecture integration queue and its work items; the document's own top-level Stable ID is `MASTER-CANONICAL-COMPLETE-INTERACTION-REGISTRATION-PATH-2026-10-19-001`. Role: REFERENCES.

### Decision
- Queue README: DEFINES.
- Canonical complete-path archive: REFERENCES.
- Identity conflict: NOT A TRUE IDENTITY CONFLICT for these two observed occurrences; the repeated identifier is a source definition plus a reference.
- Limitation: this bounded decision classifies these two paths only. It does not prove all inbound/outbound links have been reviewed or close G-01/G-12.
- Preservation: no source file deleted, renamed, or rewritten.

### Verification state
The two source files were fetched from the current repository and their identifier contexts were read back. This is a content-role decision based on visible source text, not a claim that the entire repository's incoming-reference graph is complete. The newly observed 13 missing local links and differing collision-group counts remain separate open audit findings.

### Next batch
Continue with the next unreviewed Stable ID group from H0GAF, prioritizing bilingual metadata, event/checkpoint intersections, and groups whose scanner output differs from the manifest summary. Preserve the full audit snapshot and inspect exact path/line evidence before making further decisions.


## PEH finding — parser scope mismatch and corrective commit (2026-10-21)

### Verified cause
A source-code comparison of `scripts/audit_historical_0_0_graph.py` and `scripts/build_historical_graph_manifest.py` showed that the content scanner used narrower Stable ID / Production ID metadata patterns and did not separately count Reference ID. The manifest supports additional bilingual/Persian metadata labels and filters placeholder/non-token values. This explains why the pre-fix run reported 16/25 Stable/Production collision groups while the manifest reported 38/49; these were not comparable parser scopes and must not be treated as a single count.

### Actual change
- Commit: `8ed24fc75e7a8634c33e87eaf0744bcb8f091008`.
- The content scanner was updated to share the manifest's identifier token normalization and broader metadata patterns, add Reference ID collision groups, and print every missing local link's source and target into the workflow log.
- The post-fix run on commit `f9da1be59e5e14d721d308b2ec36be06b6276477` now reports matching counts: Stable ID 39 / 39, Production ID 50 / 50, Reference ID 7 / 7. The matching scopes are now aligned; the remaining 13 missing local links were emitted with exact source/target paths.

### Missing-link triage
The 13 links resolve to four canonical checkpoint records under root `checkpoints/0.0/`, but historical links expected the same names under `docs/checkpoints/0.0/`. Four compatibility bridges were added under `docs/checkpoints/0.0/` to preserve existing link targets and point to the canonical records. This preserves historical links without duplicating or renaming canonical checkpoint files. A fresh audit is required to prove the missing-link count is zero.

### Acceptance gate
Run the audit after the compatibility bridges and prior link corrections; read the workflow log; confirm zero missing local links and matching identifier counts; then continue the next semantic role-review batch. No historical files are deleted or renamed.
