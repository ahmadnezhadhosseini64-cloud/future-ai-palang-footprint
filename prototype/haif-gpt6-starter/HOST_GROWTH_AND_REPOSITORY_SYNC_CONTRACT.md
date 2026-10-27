# Host growth and repository synchronization contract

Package family: HAIF GPT-6 Portable Starter
Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
Internal package version: 0.3.6
Project source of truth: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`
Current chain: POINT-0/051 (0+ marker on canonical root 0) → IN-089 → OUT-088 → EVT-0226 → CURRENT-101 → NEXT-051

## 1. Design goal

The same initial package evolves in place. Do not fork a new package identity or use versioned ZIP names as separate products. Keep the canonical archive filename and stable ID, increment the internal version, and record a fresh SHA-256, byte count, inventory and test receipt for every successful build. The current repository and living mother remain authoritative; an uploaded ZIP is a portable snapshot, not a live connection by itself.

## 2. Continuous growth loop

1. **Host interaction producer** captures a project-relevant user input and assistant output only if the host actually exposes them through an authorized hook/API/connector. Otherwise create an explicit manual export; never pretend capture is automatic.
2. **Pairing and provenance** creates unique point/anchor, IN, OUT and event IDs; parent links; source host/session; package version; timestamps with UTC canonical where applicable and Tehran derived from the same instant; payload digest; evidence links; and registration status.
3. **Durable intake** submits the event to the authenticated adapter. The adapter stores it in SQLite, supports idempotent replay, rejects conflicting replay, and returns a read-back receipt. It currently reports repository write as NOT_IMPLEMENTED; it is not itself the GitHub writer.
4. **Authorized repository worker** reads queued events and writes one provenance-bearing JSON event to `docs/architecture/BEHAVIOR-TRACE/INGESTED-EVENTS/`. It requires a GitHub token with contents:write held in a host secret manager, not in chat or the ZIP. After write it fetches the destination and compares exact bytes. No token or permission means no repository write.
5. **Behavior evidence** records observable actions and outcomes: task/context category, action/tool used, evidence references, success/failure, validation result, user feedback if explicitly present, retries, correction, and what changed. Do not store hidden chain-of-thought; store concise decision summaries and observable evidence.
6. **Classification** labels each item as OBSERVATION, INFERENCE, HYPOTHESIS, UNKNOWN or DECISION. Record confidence and falsification/validation criteria. Keep conflicts and failed checks as OPEN gaps.
7. **RAHM gate** checks provenance, schema, integrity, duplicate identity, relation validity, privacy/sensitivity, reproducibility and independent read-back. Invalid or ambiguous items remain quarantined/OPEN.
8. **Master/Child promotion** places a candidate in Child first. Only validated evidence plus an explicit approval can change the living Master. Rejected and superseded candidates remain traceable; history is never silently overwritten.
9. **Package release** updates source files in this same package family, runs tests on source and extracted ZIP, rebuilds the same canonical filename, hashes exact bytes, uploads the artifact, downloads it again and verifies receipt, inventory, CRC, byte-for-byte source match and extracted tests.
10. **Host refresh** sends the newly built ZIP and current living master together to a clean host. The host records its actual import result and package digest. This is a separate step; CI does not automatically refresh an external host unless an authorized deployment connector explicitly does so.

## 3. Minimum event record

Each accepted interaction record should include, when available:

- `event_id`, `anchor_id`, `input_id`, `output_id`, `parent_event_id`
- exact input/output or a secure reference to them; do not invent missing content
- `source`, `source_host`, `session_id`, `package_version`, `repository_commit`
- `observed_at_utc`, `observed_at_tehran`, `received_at_utc`, `received_at_tehran`
- `payload_sha256`, schema version, registration status and read-back receipt
- `classification`, `confidence`, `behavior_tags`, `action_summary`, `outcome`, `feedback`, `failure_or_correction`
- `evidence_refs`, `open_gaps`, `validation_status`, `promotion_decision`

Unknown values remain UNKNOWN/null; no fabricated timestamps, outcomes or feedback.

## 4. Security and data boundaries

- Start with synthetic events for connector tests.
- Never put credentials, access tokens, private keys or secret environment values in package files, repository records or conversation text.
- Exclude unrelated personal data and sensitive material unless necessary, authorized and appropriately minimized.
- Keep raw evidence separate from inferred interpretations; do not treat all observed behavior as permanent personality or model truth.
- Require idempotency and conflict detection; never overwrite conflicting event content silently.
- Every repository write must be followed by exact read-back. A successful API response without read-back is not VERIFIED.
- Keep a human approval gate for changes to the living Master and any irreversible external action.

## 5. Acceptance gates

| Gate | PASS evidence | Default until evidence |
|---|---|---|
| Package integrity | exact ZIP bytes, SHA-256, inventory, CRC, source comparison, extracted tests | OPEN |
| Host import | direct receipt from a clean interactive host | NOT RUN |
| Live producer | direct synthetic input/output capture receipt from that host | NOT RUN |
| Durable intake | authenticated adapter receipt + DB read-back + restart test | NOT RUN outside CI |
| Repository write-back | authorized worker receipt, commit SHA, fetched exact bytes | NOT VERIFIED |
| Behavior trace | event has provenance, outcome, evidence, classification and status | OPEN |
| RAHM validation | schema, identity, relation, privacy and evidence checks pass | OPEN |
| Master promotion | validated Child + explicit approval + read-back | NOT APPROVED |
| Host refresh | target host reports imported exact ZIP hash and master revision | NOT RUN |
| Cross-session persistence | restart/new-session recovery receipt | NOT RUN |

## 6. Current known implementation boundary

The repository contains `scripts/host_adapter.py` and `scripts/host_adapter_github_worker.py`. The adapter has authenticated durable intake and reports `repository_write=NOT_IMPLEMENTED`; the separate worker can write queued events when explicitly deployed with an authorized secret. The repository does not currently prove that a ChatGPT host is connected to the producer or that this worker is deployed and running. Keep those gates open until direct receipts exist.

## 7. Release rule

The only canonical package identity is the existing stable ID and filename. Each source revision may produce a fresh artifact with the same filename and a different digest. A previous digest is historical evidence only. Never mark an external host refreshed simply because CI generated an artifact.
