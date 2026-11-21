# RAHM — Owner-Controlled Intelligence Quarantine

- Stable ID: HAIF-RAHM-OWNER-CONTROL-PLANE-2026-11-22-001
- Version: 1.0.0
- Status: DESIGN REGISTERED / PRIVATE STORE AND AUTOMATION SETUP PENDING
- Owner: @ahmadnezhadhosseini64-cloud
- Canonical root: POINT-0 only; this extends the existing host architecture.

## Purpose

RAHM is the owner's central, isolated review environment for extracting useful work from one or more AI hosts, comparing evidence across hosts, running independent validation, and preparing a Child candidate. RAHM is not inside any host workspace. A host cannot enter, inspect, write, administer, or promote content from RAHM.

## Physical placement and privacy boundary

The canonical master repository is public. A folder in a public repository is not a confidentiality boundary. Therefore:

- The master repository contains only RAHM policy, schemas, public-safe workflow code, test fixtures, and sanitized Child candidates.
- Raw host exports, private conversations, credentials, personal data, unredacted logs, and sensitive evidence stay out of the public master.
- The intended physical quarantine store is a separate owner-controlled PRIVATE repository named future-ai-palang-rahm.
- The private RAHM repository must be owned/administered only by the owner. No host account, host app, collaborator, team, deploy key, or host-held credential is admitted.
- The master promotion workflow receives read-only access to that private RAHM repository through the owner-managed RAHM_READ_TOKEN secret. The token is never available to a host and is never written into the repository.
- The ChatGPT GitHub connection must separately be granted read access to the private RAHM repository before ChatGPT can inspect it directly. A connection to the public master does not prove access to a new private repository.

If the private repository has not been created and connected, RAHM is architecturally defined but not operationally provisioned. Do not store sensitive data in the public master as a workaround.

## Permanent flow

HOST PRIVATE WORKSPACE → OWNER-DIRECTED MONITOR / EXPORT → PRIVATE RAHM QUARANTINE → CROSS-HOST RECONCILIATION → RAHM VALIDATION → BOT-AUTHORED PR → OWNER REVIEW → CHILD-CANDIDATE

A Child candidate is not yet part of the living Master. A later, separate owner-directed promotion and review is required before any content changes canonical Master documents.

## Host identity and owner commands

- Official Host IDs are issued by the owner after a verifiable enrollment receipt and identity review. Canonical format: HAIF-HOST-YYYYMMDD-NNN.
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
