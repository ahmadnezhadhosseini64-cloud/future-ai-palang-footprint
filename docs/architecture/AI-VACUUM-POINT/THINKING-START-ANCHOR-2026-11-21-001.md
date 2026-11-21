# THINKING START ANCHOR — لنگر آغاز پردازش

- Stable ID: HAIF-THINKING-START-ANCHOR-2026-11-21-001
- Parent: AI-VACUUM-TEMPORAL-BEHAVIORAL-ANCHOR-2026-11-21-001
- Status: ACTIVE / LIVING / DEFINITION REGISTERED
- Event: THINKING_START
- Observed timestamp for this model's private inference-start boundary: UNKNOWN / NOT_EXPOSED
- User-request receipt time: not independently supplied as a platform lifecycle event in this record
- Clock source: UNKNOWN
- Precision: UNKNOWN
- Evidence reference: no model-runtime lifecycle telemetry supplied
- Rule: do not relabel a message timestamp, repository timestamp, or assistant response timestamp as model inference start.

This anchor defines the second boundary. It means only the runtime's observable start of request processing; it does not expose or store hidden reasoning. If only REQUEST_RECEIVED is available, record that distinct event and keep THINKING_START unavailable.
