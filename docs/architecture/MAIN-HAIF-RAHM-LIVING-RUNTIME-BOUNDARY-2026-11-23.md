# MAIN–HAIF–RAHM Living Runtime Boundary

- Status: ACTIVE / IMPLEMENTED CANDIDATE / OWNER REVIEW REQUIRED
- Date: 2026-11-23
- Stable architecture root: POINT-0/GOLDEN
- Sole continuation queue: NEXT-051
- Scope: first runnable RAHM kernel and one-way HAIF evidence bridge

## Permanent architecture

The three assets are one intended living system, with separate authority boundaries:

1. **MAIN** — canonical reference, governance, owner authority and controlled promotion.
2. **HAIF** — interaction continuity runtime: explicit IN/OUT capture, append-only event chain, checkpoint, export/import and verification.
3. **RAHM** — evidence intake, provenance ledger, deterministic triage and review proposals.

Data path in this MVP:

`HAIF export → RAHM source verification → idempotent evidence ingest → RAHM hash ledger → review proposal → owner review`

The feedback path is proposal-only. No RAHM or AI-host code may write to MAIN/MASTER.

## Implemented in this candidate

- `scripts/rahm-runtime/rahm_runtime.py`: runnable standard-library-only RAHM ledger.
- `scripts/rahm-runtime/tests/test_rahm_runtime.py`: source-integrity, idempotence, overwrite protection and authority-boundary tests.
- `scripts/rahm-runtime/README.md`: operating instructions and explicit limitations.
- RAHM verifies the HAIF source chain before ingest; preserves source event ID/hash; rejects tampering; skips duplicate source hashes; appends a separately hash-chained RAHM event; labels all outputs `PROPOSAL_ONLY_NO_MASTER_WRITE`.

## What “living and permanent” means operationally

This architecture is intended to remain ACTIVE / LIVING under the existing POINT-0/GOLDEN root and NEXT-051 queue. Future work must extend the same identities and ledgers rather than create parallel roots. A capability remains active only to the extent its runtime, persistence, tests, and read-back evidence exist.

A repository document or passing CI is not proof of a permanently running service. The current RAHM kernel runs when explicitly invoked and persists to a local JSON file. It is not a daemon, scheduled agent, cloud service, or automatic ChatGPT capture mechanism.

## Required next acceptance gates

1. Run both HAIF and RAHM test suites on the exact candidate head.
2. Add end-to-end fixture test: HAIF init → interaction → checkpoint → export → RAHM ingest → repeated ingest → RAHM verify.
3. Demonstrate restart persistence by terminating and recreating both processes against the same files.
4. Demonstrate clean-host import on a separate environment and compare IDs, event counts and hashes.
5. Add authenticated remote bridge only after a threat model, least-privilege design, secret handling, and negative authorization tests.
6. Add semantic AI reasoning only behind an explicit provider adapter, with source citations, uncertainty, evaluation, and owner review; do not label deterministic rules as intelligence.
7. Establish a separately operated scheduler/service only after health checks, monitoring, backup, restore, and failure recovery are implemented.
8. Preserve owner-only MASTER promotion. No automated merge, branch-protection bypass, secrets administration, or host-to-MASTER write path.

## No-fake-closure

- Implemented ≠ deployed.
- Local persistence ≠ cross-host persistence.
- Deterministic triage ≠ AI reasoning or learning.
- Hash chain ≠ cryptographic identity or protection against complete rewrite.
- CI PASS ≠ independent-host acceptance.
- ACTIVE / LIVING architecture ≠ 24/7 running process.

MAIN/MASTER remain unchanged by this candidate. Promotion requires exact-head tests, read-back, review and explicit owner authorization.
