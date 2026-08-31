# Candidate Path Vault Protocol

**Production ID:** CPVP-2026-08-31-001  
**Project:** Future AI / Palang Footprint  
**Status:** ACTIVE  
**Type:** Architecture / Preservation / Recovery Protocol

## Purpose

Preserve valuable but currently unvalidated, unfinished, unsuccessful, superseded, or otherwise non-active paths so they cannot be silently lost, while preventing them from contaminating the active architecture.

A path may have future value even when its current result has no active value.

## Core Rule

**Not Active ≠ Not Valuable ≠ Rejected.**

A path that has not produced a validated result must not automatically become an active rule, but it must not automatically be discarded.

## Lifecycle

`CAPTURED → PRESERVED → DORMANT → RE-EVALUATE → VALIDATED / REJECTED / ARCHIVED`

A path may return from `DORMANT` to `RE-EVALUATE` when new evidence, tools, architecture, context, or questions make it useful again.

## What belongs in the Vault

Candidate paths may include:

- unfinished architectural ideas;
- approaches that did not reach a result;
- failed experiments whose reasoning may remain useful;
- obsolete or currently impractical mechanisms;
- alternative designs;
- unresolved problems;
- discarded proposals that were not formally rejected;
- interaction paths containing useful reasoning or provenance;
- historical branches whose future reuse value is uncertain.

## Minimum Record

Where available, preserve:

- unique ID;
- source/origin interaction;
- date/time;
- author/owner;
- original problem or objective;
- proposed approach;
- actions/experiments performed;
- current result;
- evidence;
- reason it is not currently active;
- related architecture/rules/artifacts;
- repository path;
- current status;
- explicit continuation/re-evaluation path.

## Status Distinctions

- **DORMANT:** preserved for possible future use; not currently validated.
- **REJECTED:** evaluated and rejected for a stated reason.
- **ARCHIVED:** retained as historical material with no current active role.
- **VALIDATED:** evidence supports the candidate under the project's validation rules; promotion still requires the normal approval/registration gate.

`DORMANT` must never be interpreted as `REJECTED`.

## Promotion Gate

Nothing moves from the Vault into active architecture merely because it is stored there.

Required path:

`Vault → Re-evaluation → Test/Evidence → Evaluation → Approval → Record → Apply`

This preserves the project's **No Record → No Transition** and **Evidence before claims** rules.

## Retrieval Rule

When reviewing historical archives, do not only search for active rules. Also identify paths that:

1. were never finalized;
2. were marked red/unavailable;
3. stopped because of a temporary limitation;
4. contain potentially reusable reasoning;
5. are not represented elsewhere in the project.

If such a path has value, preserve it in the Vault rather than forcing it into the active architecture.

## Relationship to Existing Layers

- **Architecture:** contains validated/current structural rules.
- **Repository:** canonical durable record and retrieval source.
- **Field/Runtime:** execution and feedback environment.
- **Persistent Memory:** AI memory layer, subject to actual access and verification.
- **Candidate Path Vault:** preservation layer for potentially valuable non-active paths.
- **Recovery/Pending:** operational mechanism for unfinished required registrations.
- **Evidence/Verification:** gate for claims of validation or execution.

The Vault is therefore **not a replacement for Repository, Memory, or Recovery**. It is a preservation/state layer within the project's traceable lifecycle.

## Anti-Loss Rule

If an archive path is not currently useful enough to activate but has plausible future value, preserve it before discarding it.

If later review shows that its value was already fully absorbed elsewhere, do not create a duplicate; record the relationship if needed.

## Recovery Instruction

If this protocol is recovered from archive, first search the canonical Repository for existing Candidate Vault records and related artifacts. Then compare unresolved historical paths against the active architecture before creating anything new.
