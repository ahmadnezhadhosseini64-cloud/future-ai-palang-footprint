# AI VACUUM — Permanent Behavioral Trace Standard

- Stable ID: HAIF-AI-VACUUM-BEHAVIORAL-TRACE-2026-11-21-001
- Status: ACTIVE / LIVING / IMPLEMENTATION CANDIDATE
- Parent: AI-VACUUM-TEMPORAL-BEHAVIORAL-ANCHOR-2026-11-21-001
- Scope: every future HAIF host and every interaction where lifecycle telemetry is available

## Observable trace sequence
Record applicable events in actual order: STOP of previous turn; THINKING_START of new request (or REQUEST_RECEIVED only if that is all the host exposes); context retrieval; actual tool calls; actual file operations; code execution and tests; validation; response composition; response sent or host stopped.

## Required event fields
event_id, event_type, timestamp, clock_source, actor, outcome, evidence_reference. Optional sanitized metadata may include tool identifier, repository/commit, file path, test count and exit status. Never include tokens, credentials, raw private reasoning, hidden prompts or unnecessary personal data.

## Status vocabulary
OBSERVED means direct runtime/tool evidence exists. NOT_OBSERVED means checked for and did not occur. UNKNOWN means the host cannot determine it. UNAVAILABLE means the host does not expose that telemetry. Do not conflate these states.

## The gap
AI_VACUUM_INTERVAL is derived from STOP and THINKING_START only when both are observed on comparable clocks. Do not infer what happened during the gap from duration alone. Behavioral events explain only evidenced operations.

## Cross-host continuity
Each host appends its event receipt to the existing HAIF evidence/event lineage, references the current checkpoint and sole queue, and preserves original timestamps. No host may overwrite unknown timestamps with guesses. This standard is part of the portable host package so future hosts inherit the same observability contract.
