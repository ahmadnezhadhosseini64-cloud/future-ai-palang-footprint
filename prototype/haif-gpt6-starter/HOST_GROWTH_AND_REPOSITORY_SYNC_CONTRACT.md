# Host growth and repository synchronization contract

Package family: HAIF GPT-6 Portable Starter
Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
Internal package version: 0.4.4
Project source of truth: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`
Current chain: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051

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


## Visible response and interaction anchoring

See `INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md`. Each actual host interaction must receive a visible truthful status. Where authorized storage exists, pair actual input/output with independent anchors, provenance, payload digest, and read-back receipt. Missing response, unavailable persistence or failed writes must remain explicit gaps rather than silently implying completion. This rule is architectural; live automatic capture remains unproven until the host producer and connector pass direct acceptance tests.


## Multi-host intake and owner-controlled promotion

Each connected host is a separate producer. The default connection is read-only. Proposal/test permissions must be separately scoped, revocable and least-privilege. A host may submit only to an isolated intake/quarantine route or a dedicated proposal branch; it must never push to the protected main branch or merge its own changes.

Treat all host content as untrusted input. Validate host identity, source/version lineage, timestamps, hashes, privacy basis, redaction, duplicate/dependent sources and reproducibility. Cross-host comparison may increase confidence only when evidence sources are genuinely independent. Repeated output from the same source/model family is not independent corroboration.

Accepted evidence may create a RAHM validation task and a CHILD candidate. The living Master is changed only after successful validation and an explicit, attributable owner decision. Preserve rejected proposals and conflicts as history. Never place tokens, private keys or secrets in prompts, package files or event records. The owner retains the right to revoke any host credential or connection.

This contract defines the governance path; it does not itself implement a live Host Registry, ingress API, branch protection, deployed connector or multiple live host connections. All remain OPEN until direct end-to-end receipts exist.


## Permanent interaction ledger — POINT-0/069 / CURRENT-122

Current living master: version 1.7.74. Current chain: POINT-0/066 → CURRENT-119 → POINT-0/067 → IN-110 → OUT-109 → EVT-0285 → TIME-BINDING-EVT-0285 → CURRENT-120 → POINT-0/068 → IN-111 → OUT-110 → EVT-0286 → TIME-BINDING-EVT-0286 → CURRENT-121 → POINT-0/069 → IN-112 → OUT-111 → EVT-0287 → TIME-BINDING-EVT-0287 → CURRENT-122 → POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051 → NEXT-051.

Every actual interaction received from a registered host through an authorized producer/adapter must be recorded append-only as an independent IN/OUT pair or an explicit failure/no-response gap. Each record must include unique IDs, host/session identity (pseudonymous), parent point/event, master commit/version, adapter version, source/evidence references, trustworthy UTC timestamp or UNKNOWN, repository receive time, SHA-256, privacy/redaction basis, status and read-back receipt.

Durable capture requires an actual connected producer and authorized intake route. If unavailable, report NOT_CONNECTED / NOT_CAPTURED; do not imply all chats are automatically saved. A successful adapter CI test proves only the tested adapter path, not a live AI host or deployed worker. Existing repository scripts are `scripts/host_adapter.py` and `scripts/host_adapter_github_worker.py`; the latter requires an authorized token in a secret manager, never in prompts or package files.

All host-originated data is untrusted and enters QUARANTINE. The permanent event ledger is an audit/continuity record, not automatic knowledge promotion. Only RAHM-validated CHILD candidates with explicit owner approval can update the living Master. Hosts cannot push/merge directly to main or alter governance. Preserve failed writes, missing outputs, rejected proposals and corrections as linked append-only events. Minimize private data; raw conversations are not stored by default.


## Intake branch enforcement — POINT-0/069

The repository worker default target is now the dedicated `host-intake` branch. The worker explicitly refuses `PALANG_GITHUB_BRANCH=main`. Events written there remain QUARANTINED and require owner review through a separate pull request before any merge to main or promotion into the living Master. The `host-intake` branch was created from main at `e94520a42a0910b3a4d2c2d41263e6428b0b499e`.

Verified repository state at registration: GitHub reports the `main` branch as `protected=false`; this connection lacks a supported mutation action for branch protection/rulesets. Therefore branch protection is NOT CONFIGURED / OPEN. The worker-level main-write block is implemented, but is not a substitute for GitHub branch protection or least-privilege token configuration. Do not claim main is protected.

 
### اجرای امن ورودی مخزن — وضعیت واقعی POINT-0/069
- worker مخزن اکنون فقط شاخهٔ `host-intake` را می‌پذیرد و در صورت تنظیم هر شاخهٔ دیگری متوقف می‌شود؛ به‌ویژه هیچ نوشتن مستقیمی روی `main` انجام نمی‌دهد.
- شاخهٔ `host-intake` از main در commit `e94520a42a0910b3a4d2c2d41263e6428b0b499e` ساخته شد. رویدادهای آن شاخه QUARANTINED هستند و برای ورود به main نیازمند PR و بررسی/تصمیم مالک‌اند.
- GitHub در زمان بررسی `main.protected=false` گزارش کرد. ابزار در دسترس، تغییر branch protection/rulesets را پشتیبانی نمی‌کند؛ بنابراین محافظت واقعی شاخه هنوز NOT CONFIGURED / OPEN است. محدودیت کد worker جایگزین branch protection یا credential کم‌اختیار نیست.
- قرارداد JSON Schema دفتر تعامل به‌روزرسانی شد تا input_id، output_id، host_id، host_session_id، master_commit_sha، master_version، checkpoint_id، adapter_version، payload_sha256، privacy_class، redaction_status، capture_status و receipt_ref الزامی باشند.
- این به‌روزرسانی ساختار و گیت‌ها را محکم‌تر می‌کند؛ اتصال زندهٔ میزبان، استقرار worker و بازیابی مستقل همچنان نیازمند رسید end-to-end واقعی‌اند.


---

## POINT-0/070 — Host-scoped isolated workspaces

Every newly accepted AI host receives a stable `host_id`, `workspace_id` and opaque session ID only after identity verification and explicit owner approval. Each host works inside its own isolated workspace with a charter, inbox, observations, proposals, tests, receipts and owner decisions. Hosts consume a version-pinned, read-only master snapshot; they cannot write to MASTER/main, modify workflows or registry, access another host workspace, or promote their own output.

The approved flow is:

`MASTER SNAPSHOT (READ-ONLY) → HOST WORKSPACE → AUTHENTICATED HOST-SCOPED BROKER → QUARANTINE → OWNER MONITORING → CROSS-HOST RECONCILIATION → RAHM → CHILD CANDIDATE → EXPLICIT OWNER APPROVAL → MASTER + SAME CANONICAL ZIP`

A Git folder is not a security boundary. Do not give an AI host a direct repository write token. A broker must authenticate host identity, derive the allowed destination from that identity, validate the schema and digest, reject arbitrary paths/path traversal, and write only to the host's quarantine area on `host-intake`. Least-privilege credentials, real branch protection and negative cross-workspace tests must be proven before any live write-enabled host is accepted. If GitHub's repository-level permissions cannot enforce the needed separation, use a dedicated private intake repository or isolated sandbox and pass only sanitized evidence through the broker.

The Host Registry remains empty until a real host returns identity and read-back receipts. A workspace template or package does not mean that a host is connected or provisioned. Raw conversations are not automatically copied into the master. Only independently verifiable, reproducible, RAHM-validated results explicitly accepted by the owner may update the living master and the same canonical ZIP identity. All other host outputs remain isolated/quarantined or are recorded as rejected/open gaps.

Implementation status at POINT-0/070: architecture and templates registered; live broker, credential isolation, branch protection, cross-workspace denial tests, real host registration and end-to-end receipts remain OPEN / NOT VERIFIED.


## Current package — 0.4.4 / POINT-0/072

Internal package version: 0.4.4
Living master target: 1.7.79
Current chain tail: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051
Single-message GPT host setup: `ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`. A prompt cannot create missing OAuth authorization, connector capability, persistent workspace or security boundaries; target-host execution must prove these independently.
