# Registration Workflow Guarantee

**ID:** REG-WF-2026-08-30-001
**Date:** 2026-08-30
**Project:** Future AI / Palang Footprint
**Status:** ACTIVE / FUNDAMENTAL OPERATIONAL RULE
**Type:** Registration / Routing / Recovery / Verification Rule

## Core rule

Every explicit “ثبت کن / Register it” command MUST enter a traceable registration workflow. Registration intent, actual registration, evidence, and verification MUST NOT be conflated.

## Mandatory workflow

`COMMAND → UNIQUE ID + FULL METADATA → CLASSIFY → ROUTE → ACTUAL OPERATION → EVIDENCE → VERIFY → RECONCILE → FINAL STATE`

## Applicable destinations

For every official production, determine and record the applicable destinations according to its nature, including when applicable: Architecture; Reference Document; Canonical Repository; Persistent Memory; Runtime/Playground; Checkpoint/Anchor; Recovery/Pending Store; Evidence/Verification.

No applicable destination may be silently skipped. Each destination MUST have an explicit state such as REGISTERED, VERIFIED, PENDING, UNAVAILABLE, FAILED, or NOT APPLICABLE.

## Failure and recovery

If a required destination cannot be reached or written, the production MUST NOT be lost and MUST NOT be reported as successfully registered there. A durable Pending/Recovery record MUST preserve the unique ID, content or recoverable reference, intended destination, status, reason, timestamp/provenance, retry/reconciliation state, and next action/continuation path.

When the destination becomes available, reconcile:

`PENDING → ACTUAL REGISTRATION → EVIDENCE → VERIFICATION`

No Silent Loss.

## Claim integrity

- No actual write = no registration-success claim.
- No evidence = no verification-success claim.
- Access, intent, instructions, or tool availability alone are NOT evidence.
- Failed attempts MUST remain recorded as failures and MUST NOT become success claims.

## Reference metadata

Official registration records MUST preserve applicable metadata including: ID, Date, Exact Local Time, Timezone, City/Country when actually known, Project, Title, Status, Version, Type, Trigger/Request, Origin, Method, Architecture Placement, Applicable Destinations, Per-Destination State, Evidence, Verification, Result, Checkpoint/Recovery, Continuation Path, and Next Action.

Unknown information MUST NOT be invented; use an explicit UNKNOWN/UNAVAILABLE/NOT APPLICABLE state when appropriate.

## Relationship to existing rules

This rule operationalizes and does not replace: No Record → No Transition; Execution Claim Integrity; Closed-Loop Command Integrity; Dual Durable Registration & Deferred Reconciliation; Continuation Path Preservation & Recovery; 0.0 Checkpoint Rule; Reference Metadata & Registration Gate; Evidence Gate.

## Acceptance criterion

A registration is complete only when every applicable required destination has an independently stated state and the overall record preserves evidence, verification status, and recovery/reconciliation information for every incomplete destination.
