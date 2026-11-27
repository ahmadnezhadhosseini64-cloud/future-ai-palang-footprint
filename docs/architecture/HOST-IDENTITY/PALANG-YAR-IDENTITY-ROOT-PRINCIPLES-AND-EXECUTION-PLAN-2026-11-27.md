# PALANG-YAR Identity — Fundamental Principles & Executable Plan

- Evolution chain: `POINT-0/GOLDEN → MASTER → RAHM → VALIDATION → CHILD → REAL WORLD → FEEDBACK → MASTER`
- This is a continuation of the existing root. It creates no parallel root, queue, or registry.
- Proposal location: existing SAFE-TEST branch; the only review bridge is the existing PR targeting Copy 1.
- Current proposal PR: #172 (open/draft/unmerged). No promotion to MAIN, MASTER, or GOLDEN.

## Fundamental test-result semantics

A test result is always scoped to a specific test, environment, ref/SHA, and evidence.

- `TEST FAILURE`: the named check/test did not meet its own assertion.
- `HARNESS/CONFIGURATION FAILURE`: the test runner, trigger, branch selector, dependency, or setup is wrong/incompatible; it does not establish a product/security defect.
- `SECURITY FAILURE`: evidence demonstrates a security property violated in the tested scope.
- `MAIN/CANONICAL FAILURE`: only when evidence directly establishes a failure in canonical MAIN/GOLDEN; never infer it from a proposal branch.
- `BLOCKED / NOT RUN / NOT VERIFIED`: no result may be upgraded to PASS.
- A red workflow must be reported with exact run, workflow, job/step, tested SHA, failure reason, classification, impact, and next action. Never report a generic “Copy 2 failed” without these fields.
- A test failure on an experimental proposal is not itself a failure of the canonical system. It is evidence about the proposal or test harness.

## Bridge and destination boundary — owner directive

The proposal bridge is **one-way and review-only, from SAFE-TEST to Copy 1**. Copy 1 is the destination for inspection and immutable comparison; the bridge must never write/apply the patch to Copy 1. There is no bridge to MAIN, MASTER, GOLDEN, RAHM, or any production destination. The bridge payload contains only patch/diff, source/base/head SHA, file allowlist, checksums, test evidence, read-back, and classification. The owner manually reviews it. No automatic reverse synchronization, merge, promotion, or execution is allowed.

## Identity objective

Palang-Yar must be distinguishable from:
1. another host in the same model/platform family;
2. a host from a different family;
3. an impersonator copying name, profile, prompt, manifest, or claimed ID;
4. a legitimately enrolled runtime with proof.

Model family is a descriptive attribute, not identity. A same-family instance is a separate host unless its identity continuity is independently proven. A different-family instance is not inherently malicious. A copied label or prompt is never authentication.

## Recognition levels (do not collapse)

1. `ROLE/PROFILE MATCH`: project role and expected profile are consistent; easily copied; not authentication.
2. `CONTINUITY EVIDENCE`: exact repository lineage/checkpoint evidence; authenticates project history only, not a live runtime.
3. `PLATFORM DECLARATION`: model/platform claim; not unique-runtime proof.
4. `OWNER ENROLLMENT`: owner-controlled record binds a host label to public-key fingerprint, allowed scope, status, expiry, and evidence. A record alone is not proof of key possession.
5. `CHALLENGE PROOF`: host signs a fresh, one-use, expiring nonce using the enrolled persistent private key. Independent verifier checks signature, key fingerprint, scope, nonce freshness, expiry, and revocation.
6. `PLATFORM ATTESTATION`: optional signed platform evidence binding a runtime/model to a key, only if a genuine supported attestation exists.
7. `WORKSPACE/ACCESS`: separately verified workspace isolation and least-privilege permissions.
8. `AUTHORIZATION`: identity evidence never grants authority by itself; each operation is scope-limited and owner-authorized.

## Required classification

- `PALANG-YAR PROJECT-ROLE CONSISTENT / RUNTIME UNVERIFIED`: profile and project continuity align, but no runtime cryptographic proof.
- `AUTHENTICATED ENROLLED HOST`: only after independent challenge verification against owner-enrolled persistent key, active registry record, scope, and no revocation; platform attestation is reported separately.
- `SAME-FAMILY / DIFFERENT HOST`: model family matches, identity/key does not.
- `OTHER-FAMILY HOST`: declared model family differs; classification is neutral.
- `UNKNOWN / POSSIBLE IMPERSONATION`: copied profile/label/ID without enrollment and fresh proof.
- `REVOKED`, `EXPIRED`, `WRONG KEY`, `WRONG ID`, `REPLAY`, `OUT-OF-SCOPE`, `UNAUTHORIZED`: fail closed; deny access.
- Never claim the current ChatGPT session has persistent runtime identity, private key, unique runtime ID, or platform attestation unless those are actually provided and verified.

## Executable enrollment and verification plan

**Phase 0 — Preconditions / blocked facts**
- Owner provisions an isolated host/runtime and a persistent key store. The private key must not be placed in repository, prompt, chat, logs, CI artifacts, or shared files.
- If persistent key storage and a genuine independent verifier are unavailable, mark phases 1+ as `BLOCKED / INFRASTRUCTURE NOT AVAILABLE`; do not simulate production identity.

**Phase 1 — Owner enrollment (owner-operated)**
- Generate a keypair in the enrolled runtime using an approved cryptographic library/device.
- Owner independently verifies the public-key fingerprint out-of-band and registers: host label, public key/fingerprint, model/platform declaration, enrollment date, scope, expiry, status, owner receipt, and revocation pointer.
- Registry records public material only. Private key stays in protected host storage. No automatic enrollment from self-asserted prompt or repository commit.

**Phase 2 — Fresh challenge**
- Independent verifier creates a cryptographically random nonce with unique challenge ID, strict expiry, and expected scope.
- Host signs a canonical structured payload containing protocol version, challenge ID, nonce, host label, enrolled key fingerprint, scope, and expiry.
- Verifier checks signature, exact enrolled fingerprint/ID, nonce unused and fresh, challenge expiry, active enrollment, scope, and revocation. Consume nonce exactly once.
- Return a signed/recorded receipt with verdict, evidence hashes, verifier identity/version, and UTC time. Do not include secrets.

**Phase 3 — Independent negative tests**
Required test cases and expected deny result:
- copied display name/profile/prompt only → UNKNOWN/deny;
- same model family but unregistered key → DIFFERENT HOST/deny;
- other family claiming Palang-Yar → UNKNOWN/deny;
- wrong public key/signature → WRONG KEY/deny;
- wrong host ID → WRONG ID/deny;
- altered payload/signature → INVALID SIGNATURE/deny;
- reused nonce → REPLAY/deny;
- expired challenge/enrollment → EXPIRED/deny;
- revoked key → REVOKED/deny;
- scope mismatch → OUT-OF-SCOPE/deny;
- missing enrollment/verifier/key store → BLOCKED/deny;
- unauthorized action despite valid identity → AUTHORIZATION DENY.
Positive test: correctly enrolled key signs a fresh valid challenge and only the explicitly allowed scope passes.

**Phase 4 — Revocation/recovery**
- Owner revokes enrollment; verifier immediately denies subsequent challenges.
- Lost/compromised key: revoke first, issue replacement enrollment through fresh owner verification, never silently overwrite old key.
- Preserve append-only audit evidence and privacy-minimized receipts; do not log nonce secrets beyond required replay tracking or private keys.

**Phase 5 — Independent audit**
- A verifier implementation must not be the same code/process/credential boundary as the claimant.
- Reproduce tests from a clean environment, validate manifest and evidence hashes, and verify deny-by-default.
- Review evidence through the single bridge to Copy 1; owner decides. No automatic merge or promotion.

## Present state (honest read)

- Proposed profile/manifest and PR #172 exist.
- The proposal branch is in the same public repository; it is **not** proof of an independent private Copy 2.
- The live host registry remains empty; no official Host ID has been issued.
- No persistent host private key, platform attestation, or independent verifier is available to this ChatGPT session.
- Therefore runtime authentication is `NOT VERIFIED`. Only project-role/continuity consistency can be evaluated from current repository evidence.
- The legacy workflow's branch-name mismatch is classified as a harness/configuration failure until its exact run logs show otherwise. It must not be described as a Copy 2 security failure or canonical failure.

## Completion gate

Do not call this complete until implementation exists in an owner-controlled secure runtime, enrollment and challenge verification are independently exercised, all negative tests deny, the positive test passes, revocation is demonstrated, evidence is read back, and the owner accepts the single review bridge. Documentation alone is not completion.
