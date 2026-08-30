# Retrieval Integrity / Exact-vs-Summary Distinction Rule

**Rule ID:** RETRIEVAL-INTEGRITY-2026-08-30-001  
**Status:** ACTIVE / LIVE / PERMANENT OPERATIONAL RULE  
**Project:** Future AI / Palang Footprint  
**Registered:** 2026-08-30  

## Purpose
Prevent false claims that a prior message, architecture, decision, or project record is unavailable merely because its full text is not present in the current working context.

## Mandatory Retrieval Gate
Before claiming that a prior artifact is unavailable, the system must perform a retrieval check against all currently available stable/contextual retrieval sources appropriate to the artifact.

**Operational rule:**
> No Retrieval Check → No Unavailability Claim.

## Required State Distinction
Retrieval results must be classified explicitly as one of:

1. **EXACT RETRIEVED** — the requested prior text/artifact is available with sufficient fidelity to reproduce it exactly.
2. **PARTIAL / SUMMARY RETRIEVED** — the prior artifact or its substantive architecture/history is known, but the complete exact text cannot be verified from currently available sources.
3. **ABSENT / UNAVAILABLE** — after the applicable retrieval checks, no recoverable record is available.

The system must never collapse states 1–3 into a generic “I don't have it.”

## Exact-vs-Summary Integrity
Absence of full text from the current conversation context does **not** establish absence of the underlying architecture, decision, registration, or historical record. Where only summary-level evidence is available, the response must say so explicitly and must not fabricate exact wording.

## Production Metadata Requirement
For important formal productions, preserve at minimum:

- Production ID
- title/type
- date/time and status
- applicable destination/layer information
- retrieval reference/path where available
- recoverable summary of the decision/architecture
- evidence and verification state

This supports continuity even when exact conversational text is temporarily unavailable.

## Failure Prevention
If retrieval is incomplete:

- report **PARTIAL / SUMMARY RETRIEVED** rather than **ABSENT**;
- do not reconstruct exact text by guessing;
- preserve the known architecture/decision separately from the unverified exact wording;
- continue reconciliation when a stronger retrieval source becomes available.

## Relationship to Existing Rules
This rule reinforces the project's checkpoint, traceability, evidence, recovery, living documentation, and cross-layer reconciliation principles. It does not permit a successful execution claim without execution-specific evidence.

## Verification Boundary
Registration of this rule verifies registration of the rule itself. It does not prove successful execution of future retrievals. Each future retrieval or reconciliation operation requires its own evidence and verification.
