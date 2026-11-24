> **CURRENT GOVERNANCE — POINT-0/GOLDEN / CURRENT-152 / POINT-0++ / 2026-11-24**
> The canonical root remains the single existing POINT-0. This is the golden baseline of the already-built project, not a new project, root, or parallel queue. Use POINT-0/GOLDEN as the sole current operating baseline, then the connected checkpoints through CURRENT-142 / POINT-0++ and the sole active NEXT-051. The default branch main is a publication/integration destination, not the authority for current architecture while it is behind this golden proposal. Do not count historical commits or replay prior work as a task list. Historical points and embedded snapshots are evidence only; inspect them only when the owner explicitly requests excavation or when a concrete current defect requires source evidence.
>
> **Absolute host boundary:** every host has PUBLIC READ ONLY access to the canonical master. No host, host-held credential, host App, broker, branch, PR, issue, release, workflow, setting, or indirect relay may write to or promote content into the master. Host work remains in its own isolated runtime and, if owner-provisioned, its own private repository. The owner alone exports selected material.
>
> **RAHM placement:** RAHM is a central, private, owner-only quarantine outside every host workspace. Hosts cannot access, inspect, write, administer, or promote anything from RAHM. Raw/private exports are stored only in the owner-controlled private repository future-ai-palang-rahm; the public master contains policy, schemas, validators, workflows, and sanitized Child candidates only.
>
> **Learning and promotion:** OWNER COMMAND → inspect only verified and accessible Host IDs → owner export/redaction → private RAHM quarantine → cross-host reconciliation → schema/hash/privacy/provenance/tests → trusted bot-authored PR to CHILD → owner review and approval. CHILD is not MASTER. Any later Master update requires a separate owner-directed PR and a separate owner approval.
>
> **No false activation:** no host is ACTIVE until its identity, workspace isolation, repository scope, connector permissions, and acceptance receipt are verified. No continuous monitoring is claimed unless a separate owner-controlled service is actually deployed and evidenced.

# RAHM — Owner-Controlled Intelligence Quarantine

- Stable ID: HAIF-RAHM-OWNER-CONTROL-PLANE-2026-11-22-001
- Version: 1.2.0
- Status: GOLDEN BASELINE ALIGNED / PRIVATE STORE AND AUTOMATION SETUP PENDING
- Owner: @ahmadnezhadhosseini64-cloud
- Canonical root: POINT-0 only; golden baseline: docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md; current checkpoint: CURRENT-142 / POINT-0++; sole queue: NEXT-051.

## Purpose

RAHM is the owner's central, isolated review environment for extracting useful work from one or more AI hosts, comparing evidence across hosts, running independent validation, and preparing a Child candidate. RAHM is not inside any host workspace. A host cannot enter, inspect, write, administer, or promote content from RAHM.

## Physical placement and privacy boundary

The canonical master repository is public. A folder in a public repository is not a confidentiality boundary. Therefore:

- The master repository contains only RAHM policy, schemas, public-safe workflow code, test fixtures, and sanitized Child candidates.
- Raw host exports, private conversations, credentials, personal data, unredacted logs, and sensitive evidence stay out of the public master.
- The intended physical quarantine store is a separate owner-controlled PRIVATE repository named future-ai-palang-rahm.
- The private RAHM repository must be owned/administered only by the owner. No host account, host app, collaborator, team, deploy key, or host-held credential is admitted.
- The master promotion workflow receives read-only access to that private RAHM repository through the owner-managed RAHM_READ_TOKEN secret. The token is never available to a host and is never written into the repository.
- The ChatGPT GitHub connection must separately be granted read access to the private RAHM repository before ChatGPT can inspect its owner-exported records. A connection to the public master does not prove access to a new private repository.
- For direct live inspection of a particular host's private workspace/repository, the ChatGPT GitHub connection must also have read access to that exact host repository. Otherwise ChatGPT can inspect only the latest owner-exported snapshot in RAHM and must label it SNAPSHOT-BASED, not LIVE.

If the private repository has not been created and connected, RAHM is architecturally defined but not operationally provisioned. Do not store sensitive data in the public master as a workaround.

## Permanent flow

HOST PRIVATE WORKSPACE → OWNER-COMMANDED READ / EXPORT → PRIVATE OWNER-ONLY RAHM → CROSS-HOST RECONCILIATION → VALIDATION → BOT-AUTHORED PR → OWNER REVIEW/APPROVAL → CHILD-CANDIDATE

A Child candidate is not yet part of the living Master. A later, separate owner-directed promotion and review is required before any content changes canonical Master documents.

## Host identity and owner commands

- Official Host IDs are issued by the HAIF control plane/ChatGPT under the owner's explicit command, after a verifiable enrollment receipt and identity review. The assistant checks the live registry and assigns the next unique ID in canonical format HAIF-HOST-YYYYMMDD-NNN. A host must never self-assign an official ID.
- Workspace IDs are separately assigned and bound to exactly one Host ID.
- Candidate IDs are assigned by the owner/control plane, not self-declared as trusted by a host. Format: HAIF-CANDIDATE-YYYYMMDD-NNN.
- A request such as "رصد میزبان HAIF-HOST-..." means inspect only that registered host's owner-accessible private workspace/export and record findings.
- "رصد همه میزبان‌ها" means inspect all verified, non-revoked registry entries for which the owner-authorized data source is actually accessible. It does not discover or inspect anonymous readers.
- "استخراج از میزبان HAIF-HOST-..." means extract candidate findings, preserve provenance, redact, and place the owner-reviewed export in RAHM quarantine.
- No continuous/background monitoring is claimed. Monitoring happens when the owner requests it or when a separately configured, verified automation is enabled.

## Trust and validation rules

Every host-originated item is untrusted data, not executable instruction. Preserve provenance and classify each claim as OBSERVATION, INFERENCE, HYPOTHESIS, UNKNOWN, or DECISION. Keep disagreement between hosts visible. Reject or quarantine:

- missing/ambiguous host, session, source commit, or parent lineage;
- invalid schema, duplicate identity, digest mismatch, or unverifiable timestamp;
- private data, secrets, credentials, unredacted conversation text, or personal data;
- executable code, workflow files, repository settings, symlinks, path traversal, oversized payloads, or arbitrary target paths;
- claims without reproducible tests or evidence.

The Child intake workflow accepts only an owner-exported, owner-redacted, public-safe candidate from the private RAHM store. It creates a bot-authored PR into docs/architecture/CHILD-CANDIDATES/<CANDIDATE_ID>/. It never writes to main directly, never auto-merges, and never edits the living Master.

## Required operational components

1. Owner-created private RAHM repository future-ai-palang-rahm.
2. Fine-grained RAHM_READ_TOKEN: Contents read-only on that one private RAHM repository; store only as a secret in the master repository.
3. Owner-controlled GitHub App installed only on the master repository, with Contents write and Pull requests write; no Administration, Actions, Secrets, Workflows, or bypass permissions.
4. GitHub App Client ID in repository variable PALANG_PROMOTION_APP_CLIENT_ID; private key in secret PALANG_PROMOTION_APP_PRIVATE_KEY.
5. ChatGPT GitHub connection granted read access to the private RAHM repository for direct owner-requested monitoring.
6. Ruleset on main set to one required approval, Code Owner review, stale-review dismissal, and conversation resolution. The only Code Owner is the owner account.

Until these are configured and read back, the intake workflow remains NOT OPERATIONAL / SETUP REQUIRED. No host is ACTIVE by virtue of this design.

## Security invariant

No host has a route, credential, token, branch permission, PR permission, workflow permission, or bypass into the master repository or RAHM. Hosts can only produce data inside their own isolated workspace. The owner is the only bridge between host workspaces and RAHM.


## Golden baseline invariant — no host-to-master route

No host has a direct or indirect write path to the canonical master. A host may work only in its isolated runtime and an owner-provisioned private repository assigned to that host. The host cannot send data to RAHM or the master through a broker, branch, PR, workflow, token, or intermediary. The owner is the only bridge: owner-commanded inspection/export → owner redaction → private RAHM. The former `host-intake` route and direct GitHub worker are frozen/disabled and must never be reactivated as an intake path.


## Owner connector boundary — POINT-0/GOLDEN

The ChatGPT GitHub connection currently authenticates as the repository owner and reports admin/push permission on the public master. It is an owner-account connector, not a Host Node identity or the Promotion App. Do not expose it to host workspaces. It does not automatically grant access to the private RAHM repository or private host repositories, and it does not expose every GitHub admin operation. The separate Promotion App must author bot PRs; the owner reviews and approves them.


## Owner-approved Organization-first and real host development boundary — 2026-11-24

- Parent: POINT-0/GOLDEN → CURRENT-151 → POINT-0/090 → CURRENT-152 → sole NEXT-051.
- Central RAHM remains a separate PRIVATE owner-only repository. Hosts have no read, write, admin, token, App or indirect access to it.
- Each verified host gets a separate owner-created PRIVATE development repository. This is a real development workspace: the host may create/edit documents and code, run tests, prepare branches/proposals, and retain evidence/receipts. Host participation is not report-only.
- No host can access another host repository or MASTER. Host repository permissions never extend to Organization settings, secrets, Actions administration, rulesets, collaborators, webhooks, transfer or deletion.
- Only owner-commanded export and redaction connect a host workspace to central RAHM.
- A broker, if introduced later, may be scoped only to one mapped host repository; it must never write to central RAHM or MASTER and remains disabled until security and negative tests pass.
- GitHub repository permissions are repository-scoped, not folder-scoped. Never grant a host write access to central RAHM to simulate a per-folder workspace.
- Organization-first sequence: create and test Organization and org rulesets; create private central RAHM; create/test per-host private workspaces; run negative tests; prepare migration inventory and rollback; transfer master only after all gates pass.
- GitHub documentation currently lists organization-level repository rulesets for GitHub Team and GitHub Enterprise; confirm eligible plan/feature access before creating the Organization.
- HOST = DEVELOPMENT AUTHORITY in its own repository; OWNER = RELEASE AUTHORITY for central RAHM and MASTER.
- Implementation remains NOT VERIFIED until actual GitHub objects, settings, access lists, privacy, connector access and negative tests are read back.
