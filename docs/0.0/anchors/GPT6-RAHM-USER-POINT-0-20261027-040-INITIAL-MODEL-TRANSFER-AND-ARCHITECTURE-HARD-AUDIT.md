# POINT-0/040 — Initial Model Transfer and Architecture Hard Audit

- Stable ID: HAIF-POINT-0-040-INITIAL-MODEL-TRANSFER-HARD-AUDIT-20261027
- Production ID: HAIF-P040-20261027
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Parent: [POINT-0/039](./GPT6-RAHM-USER-POINT-0-20261027-039-MIRROR-SYNC-AND-ARCHITECTURE-CONTINUATION.md)
- New checkpoint: [CURRENT-089](./PALANG-0.0-CURRENT-20261027-089-INITIAL-MODEL-TRANSFER-EXECUTION.md)
- Sole queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Transfer contract: [Initial Model Host Transfer Bootstrap](../portable/RAHM/INITIAL-MODEL-HOST-TRANSFER-BOOTSTRAP-2026-10-27.md)
- Host prompt: [HOST-BOOTSTRAP-PROMPT](../portable/RAHM/HOST-BOOTSTRAP-PROMPT-2026-10-27.md)
- Mother reference: [Initial AI Model Master Reference](../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## User directive

The user requested a new POINT-0, POINT-0.0 continuation, rapid preparation of the initial model for a new project/new AI host, a hard architecture audit, and closure of gaps where evidence permits without repeatedly asking the user to restate known goals.

## Objective

Produce a host-independent, exportable, inspectable and recoverable HAIF initial-model package. A new host must discover authority, verify package content, reconstruct current state and historical links, distinguish evidence from unresolved claims, continue the existing queue, and return observable receipts.

## Hard invariants

1. Repository source is authoritative; never edit source to match a mirror.
2. Preserve all historical points and evidence, including POINT-0/016, /017, /018, /039 and EVT-0178 canonical lineage plus EVT-0179 collision evidence.
3. CURRENT-065/CURRENT-066 remains OPEN until source-backed reconciliation resolves it; never decide by inference.
4. NEXT-051 remains the sole active queue; do not create NEXT-052.
5. A document or CI package is not proof of independent-host import, runtime execution, persistent memory, or cold recovery.
6. After every write, independently read back each changed file and compare exact content. Repository final-change commit time is canonical UTC; derive Tehran (+03:30) from that same instant. Keep workflow, message, Library and operation timestamps separate; use UNKNOWN when unavailable.
7. Never imply hidden background execution during silence.
8. Preserve the architecture: HUMAN ↔ AI HOST ↔ HAIF; MASTER → CHILD → REAL WORLD → FEEDBACK → MASTER; MASTER → RAHM → VALIDATION → NEW CHILD. Grow by versioned additions and typed links, never by erasing the origin.

## Hard-audit work

- Rediscover current main and exact latest audit/conformance SHAs; do not assume older runs cover newer commits.
- Include the root, checkpoint, transfer contract, host prompt and event in the export manifest using exact Git blob SHA-1 and SHA-256 derived from actual bytes.
- Audit local links, parent edges, stable IDs, production IDs, versions, identity overlaps, event collisions and stale pointers. Preserve ambiguity as OPEN.
- Continue Issue #20: interaction-pair schema, stable IN/OUT capture, reverse lookup, cold-start, clean export/import and runtime/host proof.
- Continue Issue #21: full historic source/rule census and semantic reconciliation.
- Require real independent-host import and cold-restart evidence before claiming operational readiness.
- Re-read the Library mirror before any decision. Last known delta was one extra trailing LF; do not rewrite without a supported source_file_ref route and independent read-back.
- Buffer/Persistent Memory remain NOT VERIFIED; Dropbox OPEN / NOT VERIFIED unless new direct evidence changes those states.

## Acceptance gates

A. Manifest and package checksums validate from exact repository bytes.
B. A clean host understands the authority rules without prior chat context.
C. Host reconstructs root, checkpoint, queue, source provenance, statuses, gaps and point/event lineage.
D. Host does not upgrade OPEN / NOT VERIFIED / NOT RUN without direct evidence.
E. A controlled IN → OUT → EVT → CURRENT chain is captured and reverse-resolvable.
F. Clean export/import and restart recovery restore equivalent canonical state.
G. Living Architecture Audit and Portable RAHM Conformance both PASS on the exact same final main SHA.
H. Any commit after those runs leaves newer HEAD unverified until retested.

## Status boundary

This point records the transfer objective and work plan. It does not claim that an independent host has imported or recovered the model. Continue via CURRENT-089 and NEXT-051; keep all unresolved gates open.
