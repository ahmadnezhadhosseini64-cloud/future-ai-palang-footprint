# POINT-0/GOLDEN — current portable host contract

- Living master: 1.8.2
- Package version: 0.5.1 candidate
- Current chain: POINT-0/GOLDEN → CURRENT-150 → POINT-0/089 → IN-133 → OUT-132 → EVT-0320 → TIME-BINDING-EVT-0320 → CURRENT-151 → NEXT-051
- Master access for hosts: PUBLIC READ ONLY; no direct or indirect host write path.
- RAHM: central, private, owner-only, outside host workspaces; only owner-commanded export is permitted.
- Child promotion: trusted bot-authored PR plus owner review; no auto-merge.
- Old snapshots and embedded chains are historical; always resolve current pointers from the Reference Index.

> **CURRENT HOST GOVERNANCE — POINT-0/086 (0++) / CURRENT-139 / 2026-11-22**
> This addendum supersedes older embedded snapshots. Always re-read the current Reference Index, living mother, CURRENT-139 and sole active NEXT-051 from exact main HEAD.
>
> **Host boundary:** the canonical master is PUBLIC READ ONLY for every host. No host receives master write credentials, collaborator access, branches, PR/issue/release/workflow/settings permission, or bypass. A host works only in its own independent private runtime and, if owner-provisioned, its own private repository. It cannot enter or inspect another host's workspace or the central RAHM.
>
> **RAHM:** RAHM is a central owner-only quarantine outside all host workspaces. Raw/private exports stay in the owner's private repository future-ai-palang-rahm. The public master contains only schemas, policy, workflow code and sanitized Child candidates. The owner alone exports, redacts, compares and submits candidates.
>
> **Identity:** never self-assign an official Host ID or Workspace ID. The owner issues Host IDs in the format HAIF-HOST-YYYYMMDD-NNN only after a verifiable direct enrollment receipt and owner identity review. Candidate IDs are owner-issued as HAIF-CANDIDATE-YYYYMMDD-NNN.
>
> **No host-to-RAHM route:** do not request or accept RAHM token, GitHub App key, PAT, deploy key, private repo credential or owner secret. Do not try to discover, access or monitor other hosts. Return only a provenance-bound proposal/export to the owner in your own workspace.
>
> **Promotion:** host output is untrusted proposal data. Owner export → private RAHM quarantine → schema/hash/privacy/duplicate/provenance/test review → bot-authored PR → owner review/approval → CHILD. A Child candidate is not Master. No automatic merge or direct host promotion is allowed.
>
> **Monitoring commands:** when the owner asks "رصد میزبان <HOST_ID>", inspect only that specific registered host's authorized, accessible export. "رصد همه میزبان‌ها" means all verified, non-revoked registry entries that the owner has actually made accessible; it does not mean anonymous public readers or inaccessible private workspaces. Do not claim continuous background monitoring.
>
> No real host is ACTIVE merely because this instruction was read. Identity, workspace, connector permissions, private storage and recovery each require direct evidence.

---

# Host growth and repository synchronization contract

Package family: HAIF GPT-6 Portable Starter
Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
Internal package version: 0.5.0 candidate
Current chain: POINT-0/081 → CURRENT-134 → POINT-0/082 (0++) → IN-125 → OUT-124 → EVT-0302 → TIME-BINDING-EVT-0302 → CURRENT-135 → NEXT-051
Universal host entry: UNIVERSAL_AI_HOST_ENTRY_FA.md.
Project source of truth: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`
Historical chain preserved from earlier package snapshot: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051

## 1. Design goal

The same initial package evolves in place. Do not fork a new package identity or use versioned ZIP names as separate products. Keep the canonical archive filename and stable ID, increment the internal version, and record a fresh SHA-256, byte count, inventory and test receipt for every successful build. The current repository and living mother remain authoritative; an uploaded ZIP is a portable snapshot, not a live connection by itself.

## 2. Continuous growth loop

1. **Host interaction producer** captures a project-relevant user input and assistant output only if the host actually exposes them through an authorized hook/API/connector. Otherwise create an explicit manual export; never pretend capture is automatic.
2. **Pairing and provenance** creates unique point/anchor, IN, OUT and event IDs; parent links; source host/session; package version; timestamps with UTC canonical where applicable and Tehran derived from the same instant; payload digest; evidence links; and registration status.
3. **Durable intake** submits the event to the authenticated adapter. The adapter stores it in SQLite, supports idempotent replay, rejects conflicting replay, and returns a read-back receipt. It currently reports repository write as NOT_IMPLEMENTED; it is not itself the GitHub writer.
4. **Legacy direct GitHub worker — DISABLED.** It now fails closed and makes no API request. Hosts never hold a GitHub write token, including in a host secret manager. The owner exports selected evidence to private RAHM; no event is written to the public master by a host.
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

Current living master: version 1.7.79. Current chain: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051.

Every actual interaction received from a registered host through an authorized producer/adapter must be recorded append-only as an independent IN/OUT pair or an explicit failure/no-response gap. Each record must include unique IDs, host/session identity (pseudonymous), parent point/event, master commit/version, adapter version, source/evidence references, trustworthy UTC timestamp or UNKNOWN, repository receive time, SHA-256, privacy/redaction basis, status and read-back receipt.

Durable capture requires an actual connected producer and authorized intake route. If unavailable, report NOT_CONNECTED / NOT_CAPTURED; do not imply all chats are automatically saved. A successful adapter CI test proves only the tested adapter path, not a live AI host or deployed worker. Existing repository scripts are `scripts/host_adapter.py` and `scripts/host_adapter_github_worker.py`; the latter requires an authorized token in a secret manager, never in prompts or package files.

All host-originated data is untrusted and enters QUARANTINE. The permanent event ledger is an audit/continuity record, not automatic knowledge promotion. Only RAHM-validated CHILD candidates with explicit owner approval can update the living Master. Hosts cannot push/merge directly to main or alter governance. Preserve failed writes, missing outputs, rejected proposals and corrections as linked append-only events. Minimize private data; raw conversations are not stored by default.


## Legacy intake branch frozen — POINT-0/086

The former host-intake branch and direct GitHub worker are disabled. Hosts do not write to any branch, PR, issue, release, workflow, or setting in the canonical master. The legacy worker fails closed with LEGACY_DIRECT_GITHUB_WORKER_DISABLED and makes no GitHub API request.

Current approved path: host private workspace → owner export/redaction → private RAHM → validation → owner-controlled promotion App PR → owner approval → CHILD. No host receives RAHM credentials or master write access. See docs/architecture/RAHM/README.md and CURRENT-139.


## POINT-0/070 — Host-scoped isolated workspaces

Every newly accepted AI host receives a stable `host_id`, `workspace_id` and opaque session ID only after identity verification and explicit owner approval. Each host works inside its own isolated workspace with a charter, inbox, observations, proposals, tests, receipts and owner decisions. Hosts consume a version-pinned, read-only master snapshot; they cannot write to MASTER/main, modify workflows or registry, access another host workspace, or promote their own output.

The approved flow is:

`MASTER SNAPSHOT (READ-ONLY) → HOST WORKSPACE → AUTHENTICATED HOST-SCOPED BROKER → QUARANTINE → OWNER MONITORING → CROSS-HOST RECONCILIATION → RAHM → CHILD CANDIDATE → EXPLICIT OWNER APPROVAL → MASTER + SAME CANONICAL ZIP`

A Git folder or branch in the public master is not a security boundary. The legacy host-intake route is disabled. Do not give an AI host any credential for the master repository. A future broker, if separately approved, may write only to the one owner-provisioned private repository for that verified Host ID; it must derive the destination server-side, validate schema/digest, reject arbitrary paths/path traversal, and pass negative cross-workspace tests. Until those gates pass, hosts export locally and the owner imports sanitized evidence into private RAHM.

The Host Registry remains empty until a real host returns identity and read-back receipts. A workspace template or package does not mean that a host is connected or provisioned. Raw conversations are not automatically copied into the master. Only independently verifiable, reproducible, RAHM-validated results explicitly accepted by the owner may update the living master and the same canonical ZIP identity. All other host outputs remain isolated/quarantined or are recorded as rejected/open gaps.

Implementation status at POINT-0/070: architecture and templates registered; live broker, credential isolation, branch protection, cross-workspace denial tests, real host registration and end-to-end receipts remain OPEN / NOT VERIFIED.


## Current package — 0.4.4 / POINT-0/072

Internal package version: 0.4.4
Living master target: 1.7.79
Current chain tail: POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051
Single-message GPT host setup: `ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`. A prompt cannot create missing OAuth authorization, connector capability, persistent workspace or security boundaries; target-host execution must prove these independently.


## Current package — 0.4.5 / POINT-0/073

Internal package version: 0.4.5. Living master: 1.7.81. Current chain: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051. The canonical package identity and ZIP filename remain unchanged. Exact-head package conformance, external artifact round-trip and independent-host recovery are separate acceptance gates. Live broker authorization, OAuth, durable workspace, branch protection and restart persistence remain OPEN / NOT VERIFIED until direct receipts exist.


## Current package — 0.4.5 / POINT-0/074 (0++ marker)

Internal package version: 0.4.5. Living master: 1.7.81. Current chain: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051. The 0++ marker belongs to the single canonical Point 0 root; the next target is completion of the existing 0.0 continuation. NEXT-051 remains the sole active queue. The canonical package ID and ZIP filename remain unchanged. Exact-head tests, fresh build receipt, SHA-256, ZIP CRC/inventory/read-back and paired-master byte match are required before PACKAGE_VERIFIED. Independent-host acceptance, OAuth, live capture, durable workspace and restart persistence remain OPEN / NOT VERIFIED until direct receipts exist.


## Public repository onboarding — POINT-0/080
The repository is intentionally Public. New hosts can read, clone or fetch the canonical source anonymously over HTTPS; OAuth is not a prerequisite for READ. OAuth/secure credentials are required only for private resources or authenticated write-back. A host without WRITE can still recover source, execute locally if supported, and submit a patch/proposal for owner review. Hosts remain replaceable execution agents; MASTER and merge/promotion authority stay with the owner.


## POINT-0/082 — host-entry synchronization

Current living master target: 1.7.89. Current package source candidate: 0.5.0, retaining the same stable package ID and canonical ZIP filename. The prior 0.4.9 receipt is historical to its exact source SHA. This source candidate is not PACKAGE_VERIFIED until a fresh exact-main build, SHA-256, byte count, inventory, CRC, paired-master read-back, extracted tests and artifact round-trip pass. Destination-host import, workspace persistence and restart remain separate direct-evidence gates.


---

## POINT-0/084 — owner-only master and one private repository per host (superseding security rule)

This addendum is the current controlling security rule and supersedes any older wording that could be read as granting a host or host-held credential write access to the central `host-intake` branch or any other branch of the master repository.

- The canonical master repository is PUBLIC READ for hosts and owner-only WRITE. No AI host is a collaborator and no host PAT, deploy key, GitHub App installation token or other write credential may include the master repository.
- `host-intake` and the existing repository worker are not host-facing write permissions. No host receives a token for the master repository, including the `host-intake` branch.
- Each verified host may receive one separate PRIVATE repository created and owned by the owner. No cross-host repository or credential sharing is permitted.
- Default host level is `L1_READ_ONLY`. Optional write-back is allowed only through a server-side broker and a GitHub App installation scoped to that one private host repository. The model never sees the token. If broker/App scope and negative isolation tests are not verified, write-back stays DISABLED.
- A folder inside the master repository is not a security boundary. A private personal-account repository does not offer read-only collaborator access; do not add an AI host as a collaborator. Use a narrowly scoped GitHub App/broker or an organization design with appropriate read roles.
- Anonymous readers of the public master cannot be individually identified or automatically enrolled. Only an owner-reviewed, verifiable enrollment receipt can create a Host Registry record.
- Main protection, collaborator/App audit, per-host private repositories, broker deployment, revocation and cross-host tests remain OPEN until direct evidence exists.

See `docs/architecture/HOST-SECURITY/OWNER-ONLY-MASTER-PER-HOST-PRIVATE-REPOSITORIES.md` and `docs/architecture/HOST-SECURITY/PRIVATE-HOST-REPOSITORY-TEMPLATE.md`.



## POINT-0/084 security override — master intake worker is not host-facing

The master repository is owner-only WRITE. No AI host receives a GitHub token or any direct write path to the master repository, including the `host-intake` branch. Earlier descriptions of a worker using a token in a "host secret manager" are superseded: the token must never be available to or controlled by an AI host.

The legacy `scripts/host_adapter_github_worker.py` now fails closed when its target is the canonical master repository. It is not an operational host broker and must not be deployed with a host-held credential. A future broker must be a separate owner-controlled service, authenticate a verified host, resolve its private destination from a server-side registry, and use a GitHub App scoped to exactly that one host-private repository. Until that broker, App scope, private repository and negative isolation tests exist, all hosts remain L1_READ_ONLY and export proposals for owner review.

The central `host-intake` branch is not an authorized host workspace and is not a fallback write destination. Folder/branch separation inside the master is not a security boundary.
