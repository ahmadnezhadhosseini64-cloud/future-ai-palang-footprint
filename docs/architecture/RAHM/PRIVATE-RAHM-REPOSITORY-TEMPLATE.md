# Private RAHM Repository — Owner Provisioning Template

- Required repository name: future-ai-palang-rahm
- Required full name: ORG_SLUG/future-ai-palang-rahm (set ORG_SLUG only after the owner creates and verifies the Organization)
- Intended location: the owner-approved GitHub Organization
- Visibility: PRIVATE
- Access: owner-only; no host, team, collaborator, host App, deploy key or shared credential
- Status until created and read back: NOT CREATED / NOT VERIFIED

## Required repository settings

- Create as a separate private repository in the owner-approved Organization after Organization policy verification.
- Do not add AI hosts, host accounts, host applications, collaborators, teams, deploy keys, or shared credentials.
- Keep the project owner as the only Organization Owner/administrator with access to central RAHM.
- Do not enable public visibility, Pages, public releases, or public artifacts.
- Keep Actions disabled unless a separately reviewed need exists; no RAHM workflow should execute untrusted host content.
- Store only owner-reviewed exports and evidence; raw secrets and credentials are never accepted.
- Enable MFA/passkey on the owner account and retain recovery controls.

## Directory layout

    candidates/
      HAIF-CANDIDATE-YYYYMMDD-NNN/
        manifest.json
        proposal.md
        evidence.json
        validation.json
      README.md
    receipts/
      exports/
      redaction/
      decisions/
    README.md

## Candidate handling

- The owner copies an export from one or more isolated host workspaces into a new candidate folder.
- The owner assigns the Host ID and Candidate ID and records source repo, session, source commit, master snapshot SHA, and export receipt.
- The owner removes personal/private data and secrets before setting privacy_class=PUBLIC_REDACTED and redaction_status=OWNER_VERIFIED.
- The owner records owner_redaction_attestation=OWNER_REVIEWED_AND_REDACTED and owner_child_promotion_authorized=true only after deciding that the sanitized candidate may be submitted for Child review.
- Every file listed in the manifest must have an exact SHA-256 digest and byte count.
- Required files: proposal.md, evidence.json, validation.json.
- The promotion workflow checks that this repository is actually private, validates the manifest and hashes, rejects path traversal/symlinks/secrets/unsupported files, and opens a bot-authored PR to the Child area.
- The workflow never merges the PR or updates the living Master.

## GitHub connection

The ChatGPT GitHub connection must be explicitly granted read access to this private repository if the owner expects ChatGPT to inspect owner-exported RAHM records on command. For direct live inspection of a host workspace, the connection must separately have read access to that exact host-private repository. Without that, only the latest owner-exported snapshot can be inspected and must be labelled SNAPSHOT-BASED, not LIVE. The Actions secret RAHM_READ_TOKEN is separate from ChatGPT's connector authorization and does not grant ChatGPT UI access by itself.

## Read-only workflow credential

Create a fine-grained token limited to this one repository with Contents: Read only (plus GitHub's required Metadata read). Store it in the master repository as secret RAHM_READ_TOKEN. Do not paste it into ChatGPT, host prompts, files, commits, issues, or logs. Rotate/revoke it if exposure is suspected.


## Organization-first provisioning — 2026-11-24

The owner approved creating and testing the GitHub Organization before transferring the master. Verify the eligible plan for organization-level repository rulesets (GitHub Team or GitHub Enterprise according to current GitHub documentation) before provisioning. Central RAHM is never a host workspace. Each verified host's development authority belongs in its own separate PRIVATE repository.

The connected GitHub tool surface does not expose repository creation. The owner must create this repository through authenticated GitHub UI or another owner-authorized administrative route. After creation, independently read back repository ID/full name, PRIVATE visibility, collaborators, teams, installed Apps, deploy keys, Actions policy and connector read access. Until verified, the repository remains NOT CREATED / NOT VERIFIED.
