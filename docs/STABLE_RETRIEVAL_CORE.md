# Stable Retrieval Core

**Reference ID:** SRC-2026-08-29-001  
**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** VERIFIED / ACTIVE  
**Created:** 2026-08-29

## Purpose

This document defines the repository-side stable retrieval entry point for the Future AI / Palang Footprint project. The GitHub repository is an external, persistent source that can be retrieved independently of the transient chat context.

## Canonical Repository

- Owner: `ahmadnezhadhosseini64-cloud`
- Repository: `future-ai-palang-footprint`
- Visibility: `private`
- Default branch: `main`

## Retrieval Contract

1. Treat this repository as the stable external retrieval layer.
2. Start recovery from `docs/` and the project root before relying on transient conversation context.
3. Never claim that a project state is recovered unless the relevant repository files have actually been retrieved and verified.
4. A missing file, inaccessible repository, or contradictory state is an evidence gap and must be reported as such.
5. The `0.0` reference point is a stop/start boundary: retrieve first, verify second, then continue.

## Minimum Recovery Set

The minimum intended recovery set is:

- `README.md` — repository identity and entry point.
- `docs/STABLE_RETRIEVAL_CORE.md` — retrieval contract.
- `docs/REFERENCE_INDEX.md` — index of canonical project references.
- `docs/EVIDENCE_GATE.md` — execution-evidence contract.
- `docs/CHECKPOINT.md` — latest verified project checkpoint.

## Recovery Procedure

**R0 — Locate:** access the canonical repository.  
**R1 — Retrieve:** read the minimum recovery set.  
**R2 — Verify:** compare retrieved state against the requested checkpoint/reference.  
**R3 — Report:** explicitly distinguish verified facts from missing or unverified evidence.  
**R4 — Continue:** only after verification, resume project work.

## Non-Claim Rule

Repository presence does not by itself prove independent automated execution. Execution claims require evidence recorded under the Evidence Gate.

## Current Verification

On 2026-08-29 the connected GitHub integration successfully retrieved repository metadata and `README.md` from this private repository. This verifies repository access and the existence of a working external retrieval path.

**Current state:** Stable Retrieval Core = IMPLEMENTED (repository-side).  
**Independent automated execution proof:** NOT YET PROVEN.
