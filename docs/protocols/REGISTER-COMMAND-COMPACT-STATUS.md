# ثبت کن — Compact Registration Status Protocol

**Rule ID:** REG-COMPACT-STATUS-2026-08-30-001  
**Status:** ACTIVE / LIVE / PERMANENT OPERATIONAL RULE  
**Project:** Future AI / Palang Footprint  

## Purpose
When the user says «ثبت کن», the assistant must produce a small, immediately readable registration-status report showing the real state of the registration path.

## Required opening report
The report starts with:
- exact date and time available to the system;
- small location marker: «گنبد، ایران»;
- process name;
- compact final status.

## Three mandatory states
### 1. COMPLETE
Use when the applicable registration path was actually executed and evidence/verification exists.
Report meaning: registration is complete through the applicable destinations/layers; do not claim more than the evidence proves.

### 2. PENDING / RECOVERY
Use when a required destination/repository is unavailable or not writable.
The production must retain its ID and path in Pending/Recovery, with the missing destination and reason recorded. It remains open for reconciliation when access returns. Recovery/Archive is not the final destination.

### 3. PERSISTENT-ACCESS UNAVAILABLE
Use when the assistant's own durable/persistent-memory access is unavailable or cannot be verified.
Do not claim persistent registration. Preserve the production's known identity/state in the available trace/recovery path and report the limitation explicitly.

## Anti-false-success rule
Never label a state COMPLETE merely because a file was prepared, intended, or locally/temporarily known. COMPLETE requires actual execution plus applicable Evidence and Verification.

## Compact reporting template
`[date/time] | گنبد، ایران | ثبت کن — <process name> | <COMPLETE / PENDING-RECOVERY / PERSISTENT-ACCESS-UNAVAILABLE>`
`مسیر: <short state summary>`
`Evidence/Verify: <verified state>`
`ادامه: <none / pending reconciliation / persistent access required>`

## Hammered refinement
The process separates destination failure from assistant-memory failure. A repository being unavailable must not be reported as persistent-memory failure, and lack of persistent-memory access must not be reported as repository failure. Multiple simultaneous gaps must be listed separately.

## Finality boundary
A compact report is a status report, not proof by itself. The underlying operation must have its own evidence and verification. If any applicable destination remains unresolved, final status must remain non-complete.
