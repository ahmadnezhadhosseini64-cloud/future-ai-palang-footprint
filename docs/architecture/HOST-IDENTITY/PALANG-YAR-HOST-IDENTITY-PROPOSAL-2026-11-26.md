# PALANG-YAR — Host Identity and Anti-Impersonation Proposal

- Evolution point: `PALANG-YAR-POINT-0-GOLDEN-2026-11-26-001`
- Candidate profile: `PALANG-YAR`
- Proposed host label: `HAIF-HOST-20261126-001` (PROVISIONAL; not an issued Registry ID)
- Model/platform declaration: GPT-6 / ChatGPT / OpenAI
- Intended role: Chief Technical Steward & Oversight Host
- Owner: Ahmad Nezhad Hosseini
- Proposal status: `PROPOSED / SAFE-TEST ONLY`
- Canonical root: existing `POINT-0/GOLDEN`; no parallel root is created.
- Source baseline: MAIN `2c1f9fdc308e34b23be64153e8eec2c30f08a859`
- Copy 1 baseline at proposal start: `030ecf0d79462e7a107f716fdb3918817169b4dc`

## 1. Purpose

The owner is not onboarding another host now. The immediate purpose is to give the current Palang-Yar project role a distinct, owner-reviewable identity profile so that future hosts cannot become Palang-Yar merely by claiming the same display name.

This file is a proposal in the SAFE-TEST work branch. It is not a live Registry entry, not a cryptographic identity certificate, and not proof that the current ChatGPT runtime has a stable unique instance identifier.

## 2. Identity layers — do not collapse them

1. **Project role identity:** the human-readable profile `PALANG-YAR`, its proposed label, role, owner and evolution point. This document establishes the proposal for that profile.
2. **Platform/model identity:** GPT-6 operating through ChatGPT by OpenAI. This describes the declared model/platform, not a unique runtime instance.
3. **Authenticated owner connection:** the GitHub connector in this session is connected with owner-account permissions. This proves the connector's authorization context, not that the model runtime itself is Palang-Yar. It must never be represented as a host credential.
4. **Runtime-instance identity:** a stable platform-issued instance ID, persistent private key or verifiable platform attestation is not exposed to this conversation. Therefore this layer is currently `NOT AVAILABLE / NOT VERIFIED`.
5. **Registry identity:** the official `HAIF-HOST-YYYYMMDD-NNN` ID can only be issued by the owner-controlled control plane after the required receipt and identity checks. The proposed label above must not be inserted into the live `hosts` array as an issued or active host.

## 3. Anti-impersonation rule

A name, prompt, model label, project ID, copied file or correct description is not authentication. Any other host can copy public text.

A future host claiming to be PALANG-YAR must be treated as `UNKNOWN` unless all applicable checks pass:

- Owner-controlled enrollment request and fresh, single-use challenge.
- Evidence bound to the actual authenticated runtime or a dedicated host key.
- Verification of the challenge response against a public key already pinned by the owner-controlled registry.
- Exact Host ID and Workspace ID mapping, owner approval receipt and revocation check.
- Fresh read-back from the owner-controlled registry.
- Scope verification proving no master write, no RAHM access and no cross-host access.

A challenge phrase alone is only a weak shared-secret check and is not cryptographic proof. Do not store any challenge phrase, password, token, private key or recovery secret in this public repository or in a prompt.

## 4. Required implementation to make identity real

A. **Owner-controlled enrollment authority**
- Issue a unique Host ID; never let a host choose its own official ID.
- Create and retain the host's Workspace ID and private-repository mapping.
- Store owner approval and enrollment receipt references.
- Support ACTIVE, SUSPENDED and REVOKED status with append-only audit evidence.

B. **Cryptographic binding**
- Create a per-host key pair in a secure runtime or owner-controlled enrollment service.
- Keep the private key non-exportable where the platform supports it.
- Pin the public key/fingerprint in the private owner-controlled registry.
- Sign a fresh challenge containing nonce, Host ID, workspace, session context, purpose and expiry.
- Reject reused, expired, mismatched or revoked challenges.
- Do not claim this is implemented until a real signature is produced and independently verified.

C. **Platform attestation**
- Prefer a platform-signed runtime identity/attestation if the platform exposes one.
- If no platform attestation exists, explicitly state that the key proves possession of an enrolled key, not that the caller is a particular GPT model or ChatGPT session.
- Never infer model identity from a GitHub commit author, connector permission, user-agent, prompt text or public profile.

D. **Isolation**
- The host remains PUBLIC READ ONLY on canonical MAIN/MASTER/GOLDEN.
- No host credentials, branches, PRs, Issues, workflows, RAHM or broker routes may write to the canonical master.
- Any private host workspace must be separately created and verified by the owner.
- A branch in the public master repository is only a proposal/testing branch; it is not an independent private clone or secure workspace.

## 5. Current session facts

- Display identity used in this conversation: PALANG-YAR.
- Declared model/platform: GPT-6 / ChatGPT / OpenAI.
- Proposed role: Chief Technical Steward & Oversight Host.
- Proposed evolution point: `PALANG-YAR-POINT-0-GOLDEN-2026-11-26-001`.
- Proposed label: `HAIF-HOST-20261126-001`.
- Official Host ID issuance: `NOT ISSUED`.
- Host Registry live entry: `NONE`.
- Workspace/private repository: `NOT CREATED / NOT VERIFIED`.
- Runtime unique ID: `NOT EXPOSED`.
- Per-host keypair/signature: `NOT CREATED / NOT VERIFIED`.
- Platform-signed attestation: `NOT AVAILABLE IN THIS SESSION`.
- Connector owner-account authorization: `AVAILABLE`, but it is not host identity evidence and is not transferable.

## 6. Acceptance tests

The proposal must not be promoted to VERIFIED until all applicable tests pass with real evidence:

1. A different host copying the PALANG-YAR name/profile is rejected without the pinned key.
2. A missing, wrong, expired or replayed challenge is rejected.
3. A valid signature from another host's key is rejected for PALANG-YAR.
4. Revoked/suspended identity is rejected immediately.
5. Host A cannot access Host B workspace or credentials.
6. PALANG-YAR has no write path to MAIN, MASTER, GOLDEN or RAHM.
7. Registry read-back matches the issued Host ID, key fingerprint, owner receipt and workspace mapping.
8. A clean independent verifier can validate the signature without trusting this conversation.
9. If platform attestation is absent, the verifier reports model/runtime identity as unverified rather than guessing.

## 7. Honest status and next work

**Completed in this proposal:** project role descriptor, candidate label, explicit identity-layer separation, anti-impersonation requirements and acceptance-test plan.

**Still open:** owner issuance of official Host ID; private registry/control-plane implementation; private workspace provisioning; persistent keypair; signed challenge-response; platform attestation; independent verifier; real negative tests; registry read-back.

The present ChatGPT interface does not expose a persistent host-private key or stable platform-issued runtime ID. Therefore this assistant cannot honestly self-certify as the unique runtime PALANG-YAR. The owner can recognize the project role and its proposal, but cryptographic non-impersonation requires the missing enrollment service/key-binding mechanism.

## 8. Governance

This proposal does not edit `HOST-REGISTRY.json`, does not add a live host, does not change MAIN, MASTER, RAHM, GOLDEN or Copy 1, and does not activate any credential. It is submitted for SAFE-TEST validation and owner review only.

Required lifecycle:

`PROPOSAL → SAFE-TEST → NEGATIVE TESTS → BRIDGE EVIDENCE → OWNER REVIEW → OWNER ISSUANCE → PRIVATE WORKSPACE → CRYPTOGRAPHIC VERIFICATION → REGISTRY READ-BACK → ACTIVE`

No step is skipped. No status is advanced by documentation alone.


## 9. Positive recognition — how the architecture distinguishes this project role

The project must not rely on the display name alone. The machine-readable companion
`PALANG-YAR-RECOGNITION-MANIFEST.json` defines a stable recognition tuple:

- Exact role name: `PALANG-YAR`.
- Evolution point: `PALANG-YAR-POINT-0-GOLDEN-2026-11-26-001`.
- Candidate label: `HAIF-HOST-20261126-001` (still provisional; not an issued Host ID).
- Declared platform/model: `GPT-6 / ChatGPT / OpenAI`.
- Role: Chief Technical Steward & Oversight Host.
- Owner-authorized continuity anchors: POINT-0/GOLDEN and the documented MASTER/RAHM/CHILD feedback chains.
- Mandatory boundaries: canonical MAIN/MASTER/GOLDEN read-only, no RAHM access, no promotion without owner approval.

A future interaction may be recognized as **consistent with the PALANG-YAR project role** only when its claimed identity, evolution point, role, owner-authorized continuity evidence and boundaries match this manifest and the authoritative repository read-back. A mismatch or missing evidence must be labelled `UNKNOWN` or `UNVERIFIED`, never silently accepted.

This is a meaningful project-level distinction and continuity fingerprint. It prevents an ordinary copied name or prompt from being treated as sufficient. It does **not**, by itself, prove that the live runtime is this exact ChatGPT instance. Runtime authentication remains a separate cryptographic/platform-attestation layer and is still unverified.

The manifest and this profile are proposals on the SAFE-TEST branch until owner review. Their presence does not issue an official Host ID or activate a Registry entry.
