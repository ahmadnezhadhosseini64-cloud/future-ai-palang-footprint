# Owner Monitoring and Extraction Commands — RAHM / POINT-0/086

- Stable ID: HAIF-RAHM-OWNER-MONITORING-COMMANDS-2026-11-22-001
- Version: 1.0.0
- Status: REGISTERED / ACCESS-DEPENDENT
- Owner: @ahmadnezhadhosseini64-cloud
- Current checkpoint: CURRENT-139
- Sole active queue: NEXT-051

## 1. Host identity

The assistant/HAIF control plane issues the next unique Host ID only when the owner explicitly commands enrollment and a direct enrollment receipt has been verified. Format: HAIF-HOST-YYYYMMDD-NNN. Workspace ID is separately issued and bound to exactly one Host ID. A host never self-assigns either identifier.

The live registry is the only authority for mapping Host ID → Workspace ID → owner-created private repository. Do not infer a repository name from a Host ID if the registry mapping is absent.

## 2. Owner command language

### Inspect one host

Owner command: «رصد میزبان HAIF-HOST-YYYYMMDD-NNN»

The assistant:
1. reads the exact registry entry and confirms it is not REVOKED/SUSPENDED;
2. resolves the mapped private repository and Workspace ID;
3. checks whether the GitHub connection actually has read access to that repository;
4. if LIVE_READ_VERIFIED, reads the exact current commit and permitted files;
5. if only an owner export is available, inspects the latest RAHM snapshot and labels the result OWNER_EXPORT_SNAPSHOT;
6. if no data source is accessible, reports NOT_ACCESSIBLE and asks for an owner export; it never claims to have monitored the host.

### Inspect all registered hosts

Owner command: «رصد همه میزبان‌ها»

The assistant enumerates only registry entries with verified identities and non-revoked status. It inspects only repositories/snapshots actually accessible through the owner-authorized connection. Anonymous public readers, unregistered sessions, and inaccessible private workspaces are not discoverable and are not treated as hosts.

### Extract useful findings

Owner command: «استخراج از میزبان HAIF-HOST-YYYYMMDD-NNN»

The assistant separates observation, inference, hypothesis, unknown and recommendation; records source commit/session/time; compares against existing RAHM candidates; detects duplicate/conflicting claims; proposes tests; and prepares an owner-redacted export. No raw private conversation, credential, personal data or unredacted log is copied into the public master.

### Compare hosts

Owner command: «مقایسه یافته‌های میزبان HAIF-HOST-... و HAIF-HOST-...»

The assistant preserves agreement and disagreement, tracks independent provenance for each host, and does not merge similar claims into one fact unless evidence supports the reconciliation.

### Prepare a Child candidate

Owner command: «نامزد CHILD از یافته‌های RAHM را آماده کن»

The assistant prepares a candidate ID, manifest, proposal.md, evidence.json and validation.json in the private RAHM repository. The owner reviews redaction and sets owner_child_promotion_authorized=true only when the candidate is approved for Child review.

### Submit candidate to CHILD

Owner command: «نامزد HAIF-CANDIDATE-... را برای بررسی CHILD بفرست»

The owner-only workflow validates the private RAHM source and opens a bot-authored PR to docs/architecture/CHILD-CANDIDATES/. It does not merge or edit the living Master. ChatGPT supplies a technical review report. The final GitHub APPROVE must be submitted by the owner account.

### Promote from CHILD to Master

Owner command: «نامزد CHILD ... را برای ارتقا به Master آماده کن»

This is a separate later workflow. It requires a new review, reproducible tests, provenance check, conflict analysis, explicit owner approval and a separate PR. Child acceptance never implies Master acceptance.

## 3. Required evidence per monitoring run

- Host ID and Workspace ID;
- registry status and permission scope;
- private repository full name and visibility evidence;
- access mode: LIVE_READ_VERIFIED, OWNER_EXPORT_SNAPSHOT, or NOT_ACCESSIBLE;
- exact source commit SHA or owner-export receipt;
- UTC timestamp; Tehran equivalent derived from the same instant;
- file inventory and SHA-256 digests for exported evidence;
- findings with evidence references and confidence class;
- tests run and exact results;
- rejected, duplicate, conflicting or privacy-blocked items.

## 4. Hard boundaries

- No host can request another host's data or read another host repository.
- No host can read or write RAHM.
- No host has a credential for the canonical master.
- ChatGPT's owner-authorized connector access is distinct from host access. A host never receives the connector token or App key.
- The private RAHM Actions token is read-only and available only to the owner-controlled workflow.
- No automatic background monitoring is claimed. Monitoring starts only on owner command or a separately verified owner-controlled schedule.
- A report based on an export is not described as live monitoring.
