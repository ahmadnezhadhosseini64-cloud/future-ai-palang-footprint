# EVT-0123 — Deep excavation and architecture update

- Event ID: EVT-0123
- Stable ID: PALANG-DEEP-EXCAVATION-ARCHITECTURE-UPDATE-2026-10-23-001
- Production ID: DEA-AU-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / REPOSITORY-RECOVERY-PASS / FRESH-SESSION-GATE-ACTIVATED
- Parent: EVT-0122
- Input/output pair: [IN-027](../../0.0/anchors/PALANG-0.0-IN-20261023-027-DEEP-EXCAVATION-ARCHITECTURE-UPDATE.md) / [OUT-027](../../0.0/anchors/PALANG-0.0-OUT-20261023-027-DEEP-EXCAVATION-ARCHITECTURE-UPDATE.md)
- Canonical master: [CCCMR](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)
- Previous gate: [EVT-0122](./EVT-0122-BIDIRECTIONAL-IN-OUT-RECOVERY-2026-10-23.md)
- Next gate: [EVT-0124](./EVT-0124-FRESH-SESSION-RECOVERY-2026-10-23.md)

## Request preserved
«خوب خاک‌برداری عمیق کن؛ ثبت و فعال و زنده کن؛ در معماری و بروزرسانی کن»

## Findings from the excavation
1. Prior repository cold-start checks verified a continuation chain on their tested revisions, but they did not independently prove recovery when starting from either side of the current IN/OUT pair.
2. EVT-0122's bidirectional repository recovery implementation was added: `scripts/behavior-hunter/recover_interaction_graph.py`.
3. Regression tests cover IN→OUT, OUT→IN, missing pair file, missing reverse link, mismatched pair identity, stale master reference, missing queue reference, and explicit reporting of open gaps and unproven capabilities.
4. The IN and OUT anchors now share the explicit pair ID `INT-20261023-026`; EVT-0122 binds directly to the canonical master, queue and evidence-integrity target.
5. CI run [40005934719](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40005934719) passed 47 tests on tested HEAD `30f0eca4877039409ca3b0eda8643b6f8e0f4634`. Artifact `12523149825`, SHA-256 `fbda979225dc567c54a8bcf984363f6a4e242fe7f602859e95033e69733201d2`, was downloaded and inspected. Both direction manifests returned `RECOVERED`, zero failures.
6. Failed run [40005682381](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40005682381) is retained as a real design lesson: pair identity and direct graph bindings must be explicit, not inferred from adjacent prose.
7. The implementation remains repository-state-only. Fresh-session recovery, host-wide automatic capture and external destinations remain unproven.

## Active open gaps
- Issue #20: runtime capture and end-to-end recovery — OPEN.
- Issue #21: historic source census and semantic reconciliation — OPEN.
- Fresh ChatGPT session recovery — NOT RUN.
- Buffer, Library, Persistent Memory and Dropbox persistence — NOT independently verified; Dropbox remains outside this active route.

## Decision
Keep EVT-0122 as a successful repository-recovery gate for its tested SHA. Activate EVT-0124 as the next separate fresh-session recovery gate. Preserve earlier 0.0 checkpoints, failure lineage and all open gaps; no historic item is deleted or silently closed.
