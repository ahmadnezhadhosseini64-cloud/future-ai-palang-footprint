# AI Vacuum Point — Temporal and Behavioral Anchor Contract

- Stable ID: AI-VACUUM-TEMPORAL-BEHAVIORAL-ANCHOR-2026-11-21-001
- Status: ACTIVE / LIVING / IMPLEMENTATION CANDIDATE
- Root: POINT-0/077 (0++)
- Parent: CURRENT-131
- Sole governing queue: NEXT-051
- Scope: provider-neutral behavior and timing observability for every compatible HAIF host

## Definition
The AI Vacuum Point (نقطهٔ خلأ هوش مصنوعی) is the measurable interval between the end of one assistant/host activity and the beginning of the next request-processing activity. "Vacuum" names an observability gap between two lifecycle boundaries; it does not assert that the model was idle, thinking continuously, or performing any particular hidden computation.

## Two mandatory temporal anchors

### STOP ANCHOR — لنگر توقف
Record the actual timestamp at which the prior assistant turn, host task, or execution segment ended. Required fields: event=STOP; timestamp (RFC 3339 with UTC offset, or null); clock_source; precision; evidence_reference; status=OBSERVED / UNAVAILABLE / NOT_RECORDED. Do not substitute message-send time, current time, or a Git commit time for an unavailable stop event.

### THINKING START ANCHOR — لنگر آغاز پردازش
Record the actual timestamp at which the destination host begins processing the next user request, only if the runtime exposes this boundary. Required fields mirror STOP, with event=THINKING_START. This means request-processing lifecycle start, not access to or disclosure of private chain-of-thought. If only request-received time is exposed, record REQUEST_RECEIVED and do not relabel it THINKING_START. If unavailable, preserve null.

## AI VACUUM INTERVAL
The interval is computable only when both anchors are OBSERVED, timestamps are valid, clocks are comparable, and THINKING_START is not earlier than STOP. Store duration_ms derived from timestamps; never estimate manually. Otherwise duration_ms=null and status=UNMEASURABLE with a reason. Negative duration is CLOCK_CONFLICT, never clamped to zero. Different clocks require documented synchronization before calculation.

## Permanent behavioral trace
Record only observable lifecycle events: REQUEST_RECEIVED; CONTEXT_RETRIEVAL_STARTED/COMPLETED; REPOSITORY_READ; TOOL_CALL_STARTED/COMPLETED/FAILED; FILE_READ/WRITE_REQUESTED/WRITE_COMPLETED; CODE_EXECUTION_STARTED/COMPLETED/FAILED; TEST_STARTED/PASSED/FAILED; VALIDATION_STARTED/COMPLETED; RESPONSE_COMPOSITION_STARTED; RESPONSE_SENT; HOST_YIELDED/STOPPED; EVENT_UNAVAILABLE.

Each event records timestamp, source, actor (host/model/tool/user), action category, outcome and evidence reference. Store sanitized tool metadata only where safe and necessary. Never store credentials, secrets, private user data or hidden reasoning.

## What the model may be doing — observable categories only
A host may report, only if supported and evidenced: receiving a request; assembling permitted context; retrieving approved memory/repository sources; high-level tool-use category; calling tools and handling results; executing code/tests in a real workspace; validating/reconciling results; composing/sending a response. These are possible categories, not claims that every model performs all of them in every gap. Mark each OBSERVED, NOT_OBSERVED or UNKNOWN.

## Privacy and reasoning boundary
Do not request, expose, reconstruct or persist private chain-of-thought, hidden deliberation, token-by-token reasoning, model scratchpads or confidential system instructions. Record external events, high-level action categories, timestamps, tool I/O references, status and verifiable outcomes—not private reasoning text.

## Cross-host and acceptance requirements
Every compatible host implements these anchors when runtime events are exposed. Otherwise report UNAVAILABLE / NOT_CHECKED. Missing telemetry is a recorded limitation, not evidence of inactivity. Validate schema; test measurable interval, missing anchor, negative interval, clock mismatch and private-reasoning rejection. This contract is additive under CURRENT-132 and NEXT-051; no new project or queue.
