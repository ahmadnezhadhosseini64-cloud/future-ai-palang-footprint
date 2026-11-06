# Stable Retrieval Core

**Reference ID:** SRC-2026-08-29-001  
**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** VERIFIED / ACTIVE  
**Created:** 2026-08-29  
**Last Verified:** 2026-08-29

## Purpose

This document defines the repository-side stable retrieval entry point for the Future AI / Palang Footprint project. The GitHub repository is an external, persistent source that can be retrieved independently of transient chat context.

## Canonical Repository

- Owner: `ahmadnezhadhosseini64-cloud`
- Repository: `future-ai-palang-footprint`
- Default branch: `main`
- Repository-side retrieval path: **VERIFIED / ACTIVE**

## Retrieval Contract

1. Treat this repository as the stable external retrieval layer.
2. Start recovery from `docs/` and the project root before relying on transient conversation context.
3. Never claim that a project state is recovered unless the relevant repository files have actually been retrieved and verified.
4. A missing file, inaccessible repository, or contradictory state is an evidence gap and must be reported as such.
5. The `0.0` reference point is a stop/start boundary: retrieve first, verify second, reconcile contradictions, then continue.
6. Repository-side state is authoritative for project recovery when it is successfully retrieved and internally consistent.

## Minimum Recovery Set

The minimum intended recovery set is:

- `README.md` — repository identity and entry point.
- `docs/STABLE_RETRIEVAL_CORE.md` — retrieval contract.
- `docs/REFERENCE_INDEX.md` — index of canonical project references.
- `docs/EVIDENCE_GATE.md` — execution-evidence contract.
- `docs/CHECKPOINT.md` — latest verified project checkpoint.
- `docs/RETRIEVAL_RUNTIME.md` — operational retrieval sequence.

## Recovery Procedure

**R0 — Locate:** access the canonical repository.  
**R1 — Retrieve:** read the minimum recovery set.  
**R2 — Verify:** compare retrieved state against the requested checkpoint/reference.  
**R3 — Reconcile:** resolve stale or contradictory documentation against the latest verified evidence without silently overwriting history.  
**R4 — Report:** explicitly distinguish verified facts from missing or unverified evidence.  
**R5 — Continue:** only after verification and reconciliation, resume project work.

## Operational Runtime

The repository-side runtime contract is recorded in `docs/RETRIEVAL_RUNTIME.md` as:

**LOCATE → RETRIEVE → VERIFY → RECONCILE → REPORT → CONTINUE**

The runtime is now paired with an automated GitHub Actions consistency check so that key recovery-state contradictions can fail an independent execution rather than remaining only as written guidance.

## Evidence Gate Relationship

Repository retrieval proves the stable retrieval path; it does not by itself prove independent automated execution. The independent execution requirement is governed by `docs/EVIDENCE_GATE.md`.

As of 2026-08-29, the Evidence Gate is **PROVEN / ACTIVE / CLOSED / PASS**, supported by successful GitHub Actions execution with an inspectable trace. The latest verified execution is Run #7 on commit `c557be1cbfb518eb7066d0b15b4bf52fed2de5e9`.

## Current Verification

On 2026-08-29 the connected GitHub integration successfully retrieved repository metadata and canonical repository files, and the Evidence Gate independently executed successfully. The Stable Retrieval Core is therefore **VERIFIED / ACTIVE** as a repository-side recovery component.

**Current state:** Stable Retrieval Core = VERIFIED / ACTIVE.  
**Independent automated execution:** PROVEN / ACTIVE / CLOSED / PASS.

## Non-Claim Rule

Never infer permanent availability from a single successful retrieval. Future recovery must re-retrieve and verify the canonical sources. A later contradiction or inaccessible repository is a new evidence gap and must be reported rather than hidden.


## Permanent source-routing and verified-retrieval rule — LAL-20261106-001

**DESTINATION-FIRST ROUTING:** Select the retrieval destination from the user's explicit request before searching. If the user says GitHub/repository, search that repository first; if the user says ChatGPT Library, use Library first. If the destination is unclear, clarify or inspect stores separately without conflating their results.

**STORE SEPARATION:** GitHub repository, ChatGPT Library, local files, package archives and independent hosts are distinct stores. A miss, stale result, inaccessible index or absent file in one store is not evidence that the artifact is absent from another.

**CANONICAL ALIAS RESOLUTION:** Read the selected destination's official README, index or recovery manifest; map the user's short name/alias to the exact canonical path and version/ref. Do not select a merely similar filename when an authoritative alias map exists.

**FULL FETCH AND IDENTITY READ-BACK:** Retrieve the complete artifact from the exact destination and known ref/branch. Verify and report the repository/store, path, ref/version, blob SHA or equivalent identity, and requested key content. Search snippets and file listings are discovery aids, not full-retrieval proof.

**SAME-DESTINATION RECOVERY:** If the first search fails, do not prematurely report absence. Recheck spelling, aliases, branch/ref, folder README/index and search terms within the same requested destination; change the search strategy while preserving the destination constraint.

**EVIDENCE BOUNDARY:** Distinguish NOT FOUND IN THIS STORE, INACCESSIBLE, SEARCH INCOMPLETE, FOUND, FULLY RETRIEVED, READ-BACK VERIFIED and INDEPENDENT-HOST RECOVERED. Never promote one state into another without evidence.

Source lesson: `LAL-20261106-001`; source event: `EVT-0252`. This rule is part of the stable retrieval contract and must be exercised by the repository regression check and applicable host adapters.
