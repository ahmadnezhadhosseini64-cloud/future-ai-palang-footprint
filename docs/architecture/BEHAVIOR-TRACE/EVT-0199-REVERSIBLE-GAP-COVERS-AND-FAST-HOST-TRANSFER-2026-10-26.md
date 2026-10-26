# EVT-0199 — Reversible Gap Covers and Fast Host Transfer

- Stable ID: `HAIF-EVT-0199-REVERSIBLE-GAP-COVERS-20261026`
- Production ID: `HAIF-EVT-0199`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / COVERED-NOT-CLOSED
- Input: [IN-065](../../0.0/anchors/PALANG-0.0-IN-20261026-065-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md)
- Output: [OUT-064](../../0.0/anchors/PALANG-0.0-OUT-20261026-064-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md)
- User root: [POINT-0/029](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-029-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md)
- Checkpoint: [CURRENT-077](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-077-REVERSIBLE-GAP-COVERS.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Observation and lesson

The user asked for a new root, safe temporary covers over architecture gaps, and a shorter route to transfer into a new AI host. A useful cover makes the gap visible, contains risk, provides a deterministic resume action, and retains evidence; it must never be confused with closure.

## Reversible gap covers

| Gap | Cover now | True closure evidence still required |
|---|---|---|
| Independent clean-host transfer | Portable boot and import checklist | Real authorized host receipt with package digest, reconstructed state and missing-file report |
| Manifest/package drift | Treat manifest as generated and require exact-SHA conformance | Workflow-produced digests matched against exact final package bytes |
| CURRENT-065/CURRENT-066 ambiguity | Preserve both and navigate from latest source-backed checkpoint only | Source/evidence-based lineage reconciliation; no inferred winner |
| EVT-0195 collision | Preserve both artifacts and collision history | Provenance adjudication, without silent merge/renumber |
| Historic graph collisions | One-by-one adjudication in NEXT-051 | Per-finding source, parent, identity and time evidence |
| Runtime/automatic capture | Mark local code and CI scope explicitly | Real runtime, end-to-end IN/OUT capture and recovery tests |
| Persistent memory/background execution | Keep independent capability gates | Restart and idle-execution evidence from actual supported runtime |
| Buffer/Library/Dropbox | Separate destination status from repository status | Independent write/read-back/match receipts for each destination |
| Progress visibility | Milestone response with evidence and resume point | Each milestone's actual repository/test receipt |

## Integrity rules

- Covers are reversible annotations, not destructive edits.
- Preserve all prior points and the existing NEXT-051 queue.
- Do not create NEXT-052.
- Keep Dropbox on its existing OPEN / WAITING branch; current priority is transfer readiness, not Dropbox.
- UTC is canonical; Tehran is the same instant converted to Asia/Tehran (+03:30).
- Repository registration time comes from the actual commit timestamp for the final content.
- A successful workflow on a parent SHA is not proof for a newer HEAD.
- No hidden background execution is implied between turns.

## Status

The cover architecture is registered in source. Every underlying gap remains OPEN until its own evidence-backed acceptance criteria are met. This event does not claim an independent host import, persistent-memory proof, or full graph reconciliation.
