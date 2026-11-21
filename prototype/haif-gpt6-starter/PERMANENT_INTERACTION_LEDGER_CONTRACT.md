# Permanent Interaction Ledger — HAIF / RAHM

- Package version: 0.4.8
- Living master: 1.7.87
- Current chain: POINT-0/077 → CURRENT-130 → POINT-0/078 → IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → POINT-0/079 → IN-122 → OUT-121 → EVT-0299 → TIME-BINDING-EVT-0299 → CURRENT-132 → NEXT-051

## 1. What is permanent
Every actual interaction received from a registered host through the authorized producer/adapter must be represented by a durable IN/OUT pair or an explicit gap/failure record. Each pair is append-only and linked to its parent point/event and the exact master revision used by that host.

Required fields include:
- input_id and output_id;
- host_id and pseudonymous host_session_id;
- event_id, parent_point_id, parent_event_id and checkpoint_id;
- master_commit_sha, master_version and adapter_version;
- created_at_utc only when trustworthy; received_at_utc from the repository; UNKNOWN when unprovable;
- payload_sha256, source/evidence refs, privacy class, redaction status and consent basis;
- capture/result status and destination read-back receipt.

## 2. Failure is also recorded
A missing response, disconnected producer, denied permission, failed write, failed read-back, conflict or rejected replay must remain an explicit linked event. Never silently drop it, fabricate a timestamp or overwrite a previous event. Corrective actions create new linked events.

## 3. Ledger is not Master
All host-originated data is untrusted and first enters QUARANTINE. The ledger preserves continuity and audit history; it does not automatically promote every interaction into the living Master. Promotion requires source/privacy review, cross-host reconciliation, RAHM validation, CHILD candidacy and explicit owner approval.

## 4. Least privilege and repository intake
Default host access is L1 READ-ONLY. Proposal events may enter only an authorized intake path. The repository worker writes exclusively to the dedicated `host-intake` branch and refuses any other branch. Events remain QUARANTINED and require an owner-reviewed pull request before merge to main. The GitHub `main` branch was observed unprotected at the time of this package revision; branch protection remains an OPEN deployment/configuration requirement.

## 5. No false automation claims
The adapter and worker code exist and synthetic CI tests cover authenticated intake, durable local storage, idempotent retry, conflicting replay rejection and read-back. This does not prove a live AI host producer, worker deployment, actual credential setup, automatic capture of every chat, or clean-host AI recovery. If the producer is not connected, report NOT_CONNECTED / NOT_CAPTURED.

## 6. Privacy
Do not store raw conversation by default. Capture only the minimum authorized information required for continuity and audit. Never put credentials, tokens, private keys or unrelated sensitive data in prompts, payloads, logs, ZIP files or repository records.
