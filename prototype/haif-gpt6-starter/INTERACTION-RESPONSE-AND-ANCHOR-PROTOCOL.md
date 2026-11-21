# Interaction response and anchor protocol

Package family: HAIF GPT-6 Portable Starter
Stable package ID: HAIF-GPT6-PORTABLE-STARTER-20261025-004
Canonical ZIP filename: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
Internal version: 0.4.9
Current chain: POINT-0/079 → CURRENT-132 → POINT-0/080 → IN-123 → OUT-122 → EVT-0300 → TIME-BINDING-EVT-0300 → CURRENT-133 → NEXT-051
Universal host entry: UNIVERSAL_AI_HOST_ENTRY_FA.md.
Current chain: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051; prior checkpoints remain parent history.

## 1. Visible response is mandatory
When an input is received, the host must produce one of:
- ACKNOWLEDGED — accepted and being processed, with a durable interaction ID if available;
- COMPLETED — a user-visible result exists and its completion evidence is identified;
- BLOCKED — a named dependency, permission or missing input prevents completion;
- FAILED — the operation failed, with the actual error or concise safe reason;
- PARTIAL — completed substeps and remaining open gates are separated.

A spinner or internal processing state is not a user-facing result. If work continues beyond the current response, provide a concise status and the next concrete action. Never claim success before the tool/host confirms it. If an action cannot be performed in the current environment, say so.

## 2. Anchor each interaction
Where the host has authorized durable storage, pair each actual user input with the actual assistant output:
- independent point/anchor, IN, OUT and EVT identifiers;
- parent point/checkpoint and package version;
- exact payload or content-addressed evidence reference;
- source host/session and actual observed/received timestamps, UTC first with Tehran equivalent derived from the same instant where applicable;
- payload SHA-256, result status, evidence references and open gaps.

Do not invent message timestamps, missing outputs, tool results or success states. If a reply is absent, register RESPONSE_MISSING / OPEN only when the host can observe that absence. If storage is unavailable, return a manual export and mark persistent registration NOT VERIFIED.

## 3. Failure and recovery
On a tool failure, timeout or rejected write:
1. show FAILED/BLOCKED/PARTIAL to the user;
2. preserve the failure and retry/correction as observable evidence;
3. do not duplicate IDs or silently overwrite the original event;
4. retry idempotently when safe;
5. read back the destination and compare exact bytes before claiming VERIFIED;
6. link the correction to the original event and current checkpoint.

## 4. Growth into Future AI / Palang Footprint
- Record observable behavior, task context, tool/action summaries, outcomes, explicit feedback, failures and corrections.
- Separate OBSERVATION, INFERENCE, HYPOTHESIS, UNKNOWN and DECISION.
- Minimize private/unrelated/sensitive content; never put credentials or tokens in events.
- RAHM checks schema, provenance, integrity, privacy, conflicts and reproducibility.
- New knowledge remains a Child candidate until evidence passes and explicit human approval allows promotion to the living Master.
- Rebuild the same canonical ZIP from the package source, increment internal version, preserve stable ID and canonical filename, test extracted bytes, hash exact archive bytes and record a fresh receipt.

## 5. What this protocol does not grant
This document does not itself create a native GPT plugin, automatic message hook, background worker, repository token or persistent memory. Each requires an actual host integration and direct acceptance receipt. Until then, live capture, write-back and restart persistence are OPEN / NOT VERIFIED.

 
## 6. Permanent interaction ledger — required for every connected host

For each actual host interaction received by the authorized producer, create a distinct IN record and OUT record linked to one event ID and the prior point/checkpoint. If the output is absent, or capture/write/read-back fails, record an explicit NO_RESPONSE / NOT_CAPTURED / WRITE_FAILED / READBACK_FAILED gap. Do not silently omit it.

Required fields: host_id, pseudonymous host_session_id, event_id, input_id, output_id, parent_point_id, parent_event_id, master_commit_sha, master_version, adapter_version, trustworthy created_at_utc or UNKNOWN, received_at_utc, Tehran equivalent derived from UTC, payload_sha256, source/evidence refs, privacy/redaction status, result status and receipt ref.

Write durably, fetch the destination and compare exact content/digest. Retries with the same idempotency key and same payload must be idempotent; a conflicting replay must be rejected. Corrections and owner decisions are new linked events; never rewrite prior history.

The event ledger preserves interaction continuity and audit history. It does not promote every interaction into the Master. All host input remains QUARANTINED until privacy/source review, cross-host reconciliation, RAHM validation, CHILD candidacy and explicit owner approval. Hosts have no direct main write/merge authority.

If no actual producer or authorized adapter connection exists, mark NOT_CONNECTED / NOT_CAPTURED. A ZIP or written protocol alone does not capture all conversations. Existing adapter code and synthetic CI PASS are not proof of a live host connection or deployed worker. Never include raw conversations by default, secrets or credentials.


## Current package — 0.4.4 / POINT-0/072

Internal version: 0.4.4
Current chain tail: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051
Single-message GPT host setup: `ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`. Package identity and canonical ZIP filename remain unchanged.


EVT-0290 remains reserved for its earlier mirror-only record. The current owner-authorized continuation is uniquely registered as EVT-0291.


## Current package — 0.4.5 / POINT-0/073

Internal version: 0.4.5. Living master: 1.7.81. Current chain: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051. The canonical package ID and ZIP filename remain unchanged. Package verification requires a fresh exact-head receipt and read-back. Independent-host acceptance, live capture, OAuth, durable workspace and restart persistence remain OPEN / NOT VERIFIED.


## Current package — 0.4.5 / POINT-0/074 (0++ marker)

Internal package version: 0.4.5. Living master: 1.7.81. Current chain: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051. The 0++ marker belongs to the single canonical Point 0 root; the next target is completion of the existing 0.0 continuation. NEXT-051 remains the sole active queue. The canonical package ID and ZIP filename remain unchanged. Exact-head tests, fresh build receipt, SHA-256, ZIP CRC/inventory/read-back and paired-master byte match are required before PACKAGE_VERIFIED. Independent-host acceptance, OAuth, live capture, durable workspace and restart persistence remain OPEN / NOT VERIFIED until direct receipts exist.


## Public READ and OAuth boundary — POINT-0/080
Public HTTPS READ/clone/fetch does not require OAuth. Hosts must begin with anonymous READ. OAuth or another secure credential is reserved for private resources or authenticated write-back. READ, EXECUTE, WORKSPACE and WRITE are independent permission/capability states. Public visibility does not confer write permission or ownership; the project owner retains MASTER and promotion authority.
