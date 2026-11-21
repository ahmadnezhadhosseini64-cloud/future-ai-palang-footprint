# Private RAHM Repository — Owner Provisioning Template

- Required repository name: future-ai-palang-rahm
- Required full name: ahmadnezhadhosseini64-cloud/future-ai-palang-rahm
- Visibility: PRIVATE
- Owner: ahmadnezhadhosseini64-cloud
- Status until created and read back: NOT CREATED / NOT VERIFIED

## Required repository settings

- Create as a separate private repository under the owner account.
- Do not add AI hosts, host accounts, host applications, collaborators, teams, deploy keys, or shared credentials.
- Keep owner as the only administrator and writer.
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

The ChatGPT GitHub connection must be explicitly granted access to this private repository if the owner expects ChatGPT to inspect it on command. The Actions secret RAHM_READ_TOKEN is separate from ChatGPT's connector authorization and does not grant ChatGPT UI access by itself.

## Read-only workflow credential

Create a fine-grained token limited to this one repository with Contents: Read only (plus GitHub's required Metadata read). Store it in the master repository as secret RAHM_READ_TOKEN. Do not paste it into ChatGPT, host prompts, files, commits, issues, or logs. Rotate/revoke it if exposure is suspected.
