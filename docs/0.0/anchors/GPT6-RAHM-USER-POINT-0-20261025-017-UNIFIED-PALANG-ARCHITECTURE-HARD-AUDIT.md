# POINT-0/017 — Unified Palang Architecture Hard Audit

- Stable ID: HAIF-POINT-0-017-UNIFIED-PALANG-HARD-AUDIT-20261025
- Production ID: HAIF-P0-017-20261025
- Version: 1.0.0
- Status: REGISTERED; repository read-back verification required and performed after write.
- User intent: audit overlapping points and architecture across the entire Future AI / Palang Footprint project; integrate all findings from newer work into the original project; do not create or operate a detached parallel project.
- Prior user-turn point: [POINT-0/016](./GPT6-RAHM-USER-POINT-0-20261025-016-MIRROR-DELTA-AND-ARCHITECTURE-RECOVERY.md).
- Execution checkpoint under audit: [CURRENT-066](./PALANG-0.0-CURRENT-20261025-066-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md) and [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md); preserve both and all historical anchors.
- Event: [EVT-0178](../../architecture/BEHAVIOR-TRACE/EVT-0178-UNIFIED-PALANG-ARCHITECTURE-HARD-AUDIT-2026-10-25.md).
- Living master: [HAIF Initial Model Master Reference](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).

## Core architecture invariant: one project, not two

Future AI / Palang Footprint is the canonical parent project and repository. Any newer model, runtime, recovery package, behavior hunter, mirror workflow or research result must be classified and linked into the original project through source provenance, stable identity, version, component, parent/child relation, test, evidence, open gap and integration status. A new folder, document or package is not automatically a new independent project. Do not fork the architecture conceptually, duplicate automation, overwrite earlier points or merge records by title similarity alone.

Canonical graph:
Human interaction IN/OUT → independent anchor → event/time binding → current 0.0 checkpoint → living master → reference index/trace index/integration queue → source/rule/component/test/evidence/gap graph → runtime/package/host recovery evidence → feedback into master. Each edge must be resolvable and backed by source evidence.

## Hard-audit findings from current readable repository records

1. **Current-pointer conflict:** the 0.0 registry / latest mirror event contains declarations of CURRENT-065 as execution current, while CURRENT-066 describes itself as the newer registered checkpoint and NEXT-051 as active. These are not to be resolved by guessing. Treat CURRENT-065 as preserved history; adjudicate all canonical pointer surfaces and make one explicit current pointer, with commit-bound evidence.
2. **Verifier / manifest lineage mismatch:** `scripts/behavior-hunter/verify_current_0_0_chain.py` expects the CURRENT-066 chain while loading `docs/portable/RAHM/CURRENT-065-OVERLAY-MANIFEST.json`. That manifest's package ID says CURRENT-066, yet its filename and file list retain a mix of CURRENT-065 / prior IN/OUT / older event records. This may be a historical overlay or stale manifest; inspect its contract and exact-byte digest before changing it. Do not relabel or rewrite the manifest by guess.
3. **Verifier is hard-coded:** it pins a specific point0/IN/OUT/event/current/NEXT and old direct-link expectations. Separate the intended test scope (reconstruct historical CURRENT-066 from its own input/output anchors) from the latest live pointer. A historical recovery test should remain reproducible; a live-pointer test should discover the canonical current pointer independently.
4. **Graph overlap is not yet adjudicated:** Issue #21 lists Stable-ID, Production-ID, reference-ID and event-ID collision/overlap groups. Existing historical graph snapshots show structural counts but do not prove every semantic edge. Do not bulk rename, delete or merge. Record each source's provenance, role, version, alias/lineage, dependent tests and evidence.
5. **Multiple registry surfaces can drift:** 0.0 registry, living master, reference index, behavior-trace index, integration queue, portable master, overlay manifest, workflow and Issues #20/#21 need a controlled single-current-pointer contract plus append-only history. A text mention is not a machine-verified graph edge.
6. **Execution proof boundary:** a GitHub CI run or repository read-back does not prove live AI-host message capture, independent-host import, restart persistence, idle/background execution, Buffer/Persistent Memory or Dropbox.
7. **Mirror newline delta:** canonical source 10,479 chars vs Library 10,480; one extra trailing newline, edit distance 1. Removing it from the Library copy is semantically safe for Markdown, but do not normalize until a supported Library write route and independent read-back are available. Never modify canonical source to match mirror.
8. **Timestamp integrity:** repository registration time must be the actual final-change commit timestamp in UTC, Tehran derived from that same instant. Do not infer the exact user-message or operation time from commit time.

## Open work; do not claim completion

- NEXT-051 remains OPEN until its existing acceptance criteria pass.
- Issue #20: runtime interaction pair schema, reverse lookup, cold-start, IN/OUT reconstruction and clean-host recovery.
- Issue #21: full source/rule census, provenance, duplicate/alias adjudication, source→rule→component→test→evidence→gap graph and exact-final-HEAD audit.
- BOART-FOLLOWUP-01: source-backed master-reference and historic graph reconciliation.
- Repair/clarify the split between historical CURRENT-066 reconstruction and live-current discovery without erasing historical reproducibility.
- Inspect actual latest Actions runs and exact tested SHAs; a PASS on a prior SHA is not a pass for current main.
- Library newline normalization remains OPEN until supported write + independent read-back.
- Buffer/Persistent Memory NOT VERIFIED; Dropbox OPEN/NOT VERIFIED; external end-to-end recovery NOT RUN.
- Preserve all earlier 0.0 points, events, failures, corrections, and unresolved edges.

## Acceptance gates for this audit

A. Re-read every changed file after write.
B. Every point/event/master/index/queue link resolves.
C. Exactly one explicitly designated live execution pointer is discoverable; historical checkpoints remain immutable and addressable.
D. The verifier clearly distinguishes historical reconstruction tests from live-current discovery.
E. Manifest/package IDs, included file list and digests reconcile from exact bytes, or discrepancies remain OPEN with evidence.
F. Every collision/overlap decision is source-backed; unresolved groups remain queued.
G. A fresh audit passes on the exact final main SHA, and the tested SHA is recorded.
H. No external capability is called verified without independent external evidence.

## Canonical continuation

Continue from the existing NEXT-051 queue. This point is a user-interaction root and audit overlay, not a replacement execution checkpoint and not permission to mint NEXT-052. Merge all findings into the original Future AI / Palang Footprint architecture and its living mother reference.


## Registration collision follow-up — EVT-0179
- [EVT-0179](../../architecture/BEHAVIOR-TRACE/EVT-0179-UNIQUE-ID-COLLISION-AND-POINTER-RECONCILIATION-2026-10-25.md) records and quarantines an accidental duplicate EVT-0178-numbered pointer draft. Canonical EVT-0178 remains this point's unified hard-audit event. CURRENT-065/CURRENT-066 pointer conflict remains OPEN; no promotion is inferred.
