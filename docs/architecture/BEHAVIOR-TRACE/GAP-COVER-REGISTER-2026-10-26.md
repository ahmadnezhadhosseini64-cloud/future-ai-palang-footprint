# GAP-COVER-REGISTER — Reversible graph, provenance and parent gaps

- Stable ID: `HAIF-GAP-COVER-REGISTER-20261026-001`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / REVERSIBLE
- Root: [POINT-0/031](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-031-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md)
- Checkpoint: [CURRENT-078](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-078-REVERSIBLE-GRAPH-GAP-COVERS.md)
- Event: [EVT-0200](./EVT-0200-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER-2026-10-26.md)
- Queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Semantics

`COVERED / DEFERRED` is a reversible priority decision. The underlying issue remains `OPEN / ACTIVE / LIVING`, indexed, exportable, discoverable and eligible for Behavior Hunter review. A cover is not a fix, verification, acceptance, deletion or permanent closure.

## Current cover ledger

| Gap key | Underlying status | Cover status | Preserved evidence / conflict | Reopen trigger |
|---|---|---|---|---|
| `GAP-CURRENT-065-066` | OPEN / CONFLICTED | COVERED / DEFERRED / REVERSIBLE | Two current-pointer candidates; no winner inferred. | Source-backed comparison or NEXT-051 pointer-reconciliation step. |
| `GAP-EVT-0195-COLLISION` | OPEN / CONFLICTED | COVERED / DEFERRED / REVERSIBLE | Two files claim EVT-0195; preserve both and their history. | Original-source/provenance and index/commit-history adjudication. |
| `GAP-HISTORIC-GRAPH-CENSUS` | OPEN / NOT COMPLETE | COVERED / DEFERRED / REVERSIBLE | Historic file/source census and semantic reconciliation remain incomplete. | Resume source census in evidence-backed batches under NEXT-051. |
| `GAP-SOURCE-PROVENANCE` | OPEN / PARTIAL OR MISSING PER ITEM | COVERED / DEFERRED / REVERSIBLE | Missing/conflicting source, time or production provenance remains distinguishable per item. | Primary source, Git metadata or explicit user confirmation. |
| `GAP-PARENT-EDGE-AMBIGUITY` | OPEN / PARTIAL OR CONFLICTED PER ITEM | COVERED / DEFERRED / REVERSIBLE | Never infer parent links from names, order or similarity alone. | Validate candidate through source content, chronology, cross-links and history. |
| `GAP-ORPHAN-AND-BROKEN-LINKS` | OPEN / NOT FULLY AUDITED | COVERED / DEFERRED / REVERSIBLE | Prior missing-link and orphan findings remain until rechecked. | Exact-tree link scan and source-backed reconciliation. |
| `GAP-HOST-IMPORT-COLD-START` | OPEN / NOT RUN | COVERED / DEFERRED / REVERSIBLE | CI success is not independent host-import evidence. | Actual destination host returns structured receipt and recovered-state comparison. |
| `GAP-PERSISTENCE-BACKGROUND` | OPEN / NOT VERIFIED | COVERED / DEFERRED / REVERSIBLE | Buffer, Persistent Memory, Library, Dropbox and always-on monitoring are not proven by repository records alone. | Each destination/runtime returns direct write/read-back or execution evidence. |

## Behavior Hunter scan contract

On each available repository scan or CI run, detect new/changed/deleted graph records; broken links/orphan anchors; duplicate IDs; pointer conflicts; ambiguous parent edges; missing provenance; conflicting timestamps; disappearance of covered gaps from index/boot/manifest; tests bound to a SHA other than current main; and host-import claims without direct destination receipts.

For each finding retain gap key, source path, observed evidence, competing interpretations, uncertainty, failed checks, cover reason, next trigger and exact commit/run receipt. This is scan-driven monitoring; do not claim a continuously running watcher without direct scheduler/runtime evidence.

## Update protocol

When the user says “فعلاً ببند / صرف‌نظر کن”, mark the cover `COVERED / DEFERRED` and keep the issue `OPEN`. Only evidence-backed acceptance can move underlying status to VERIFIED/ACCEPTED/CLOSED, with prior state and acceptance receipt preserved.

## Limitation

This is a living architecture record, not proof that the entire historic graph has already been audited. Source-backed inventory and exact-head tests remain in NEXT-051 / CURRENT-078.