# First interactive GPT-6 host — acceptance checklist

> Compatibility checklist only. Current universal entry and chain are governed by UNIVERSAL_AI_HOST_ENTRY_FA.md and Reference Index: POINT-0/079 → CURRENT-132 → POINT-0/080 → IN-123 → OUT-122 → EVT-0300 → TIME-BINDING-EVT-0300 → CURRENT-133 → NEXT-051. Package target 0.4.9; living master 1.7.88.

Package identity: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
Paired handoff: canonical ZIP + current living master reference.
Current source chain: POINT-0/077 → CURRENT-130 → POINT-0/078 → IN-121 → OUT-120 → EVT-0298 → TIME-BINDING-EVT-0298 → CURRENT-131 → POINT-0/079 → IN-122 → OUT-121 → EVT-0299 → TIME-BINDING-EVT-0299 → CURRENT-132 → NEXT-051.

## A. Before import
- [ ] Record exact source commit, internal package version, ZIP byte count and SHA-256 from the fresh workflow receipt.
- [ ] Upload the ZIP and living master together into a clean interactive GPT-6 session.
- [ ] Confirm the host can access and read both files; record any tool/file limits instead of assuming access.
- [ ] Ask the host to recover canonical point 0, 0+ meaning, latest 0.0 checkpoint CURRENT-132, sole queue NEXT-051, stable package ID and all open gates without using prior chat history.

## B. Integrity and reconstruction
- [ ] Host repeats the ZIP filename/version/hash from the receipt; mismatch = FAIL.
- [ ] Recover state independently from the IN record and independently from the OUT record; normalized chains must match.
- [ ] Preserve old 0+ markers and historic digests; do not create a second root or NEXT-052.
- [ ] Negative control: alter one byte and verify rejection; remove a required file and verify rejection.
- [ ] Read back the host's reconstructed state and compare it with the expected chain.

## C. Live interaction and behavior data
- [ ] Establish how this host actually receives interaction pairs. A written instruction alone is not a live producer.
- [ ] Test one clearly synthetic event first; preserve input/output, IDs, provenance, classification, hash and UTC/Tehran receipt times.
- [ ] Verify idempotent retry and reject conflicting replay.
- [ ] If automatic capture is unavailable, mark it NOT SUPPORTED / NOT VERIFIED and use explicit/manual export rather than claiming always-on capture.

## D. Repository return
- [ ] Confirm an authorized connector or separately deployed host adapter/worker exists and is reachable.
- [ ] Never paste tokens/secrets into chat or commit them to the ZIP/repository.
- [ ] Send only a synthetic test event first; require repository write, fetch-back, byte/content comparison and evidence receipt.
- [ ] If no write permission exists, export a portable event file for an authorized manual import and leave automated write-back OPEN.

## E. Restart/persistence and final verdict
- [ ] Close/restart the session and recover from the same pair of files or proven durable state.
- [ ] Record separate PASS/FAIL/NOT RUN for import, digest, IN/OUT equivalence, negative controls, read-back, live producer, repository write-back and restart.
- [ ] Save the direct host receipt into the project chain only after read-back verification.

## Status boundary
A CI build, a local engine test, or two independent CI runners do not prove that an interactive GPT-6 host imported the package. Until this checklist has direct host evidence, real host acceptance is `NOT RUN / NOT VERIFIED`.


## F. Controlled learning and package growth
- [ ] Verify HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md is present in the received ZIP and exact inventory.
- [ ] Use a synthetic interaction only; verify input/output IDs, provenance, behavior evidence and digest.
- [ ] Test authenticated intake, idempotent retry, conflicting replay rejection, durable restart and exact repository read-back.
- [ ] Confirm candidate insights remain Child proposals until RAHM validation and explicit approval.
- [ ] After a new package build, refresh the same canonical ZIP plus living mother and verify the host's imported digest.


## G. Multi-host governance and owner authority — POINT-0/068

- [ ] Read the paired living master version 1.7.73 and its multi-host governance section.
- [ ] Confirm this host is a distinct Host Node and default access is L1 READ-ONLY.
- [ ] Confirm no direct write/merge to main, no self-promotion, no authority to change Master rules, and no admin/bypass permissions.
- [ ] Submit only a synthetic observation/proposal to an authorized quarantine/proposal route; if no such route is available, mark NOT IMPLEMENTED and do not invent a live connection.
- [ ] Include host identity, exact master commit/version, checkpoint, source references, UTC timestamp or UNKNOWN, SHA-256, privacy/redaction status and limitations.
- [ ] Verify cross-host reconciliation does not treat copied/shared-source outputs as independent evidence.
- [ ] Verify RAHM validation and CHILD candidacy are separate from owner approval.
- [ ] Confirm explicit owner approval is required before any Master promotion.
- [ ] Verify host credentials are least-privilege, stored outside prompts/files, and revocable by the owner.
- [ ] Return a raw receipt proving what was actually read, submitted, accepted or rejected. A ZIP import alone is not proof of repository connection.

 
## H. Permanent interaction ledger — POINT-0/069 / CURRENT-122
- [ ] Verify paired living master version 1.7.74 and exact current chain: `POINT-0/066 → CURRENT-119 → POINT-0/067 → IN-110 → OUT-109 → EVT-0285 → TIME-BINDING-EVT-0285 → CURRENT-120 → POINT-0/068 → IN-111 → OUT-110 → EVT-0286 → TIME-BINDING-EVT-0286 → CURRENT-121 → POINT-0/069 → IN-112 → OUT-111 → EVT-0287 → TIME-BINDING-EVT-0287 → CURRENT-122 → NEXT-051`.
- [ ] Verify every actual captured interaction creates independent IN and OUT IDs linked to parent point/event and master commit.
- [ ] Verify missing response, disconnected producer, failed write and failed read-back create explicit gap events, not silent omissions.
- [ ] Verify durable write followed by exact destination read-back and SHA-256 comparison.
- [ ] Verify idempotent same-payload retry and rejection of conflicting replay.
- [ ] Verify host/session provenance, adapter/model version, trustworthy UTC or UNKNOWN, receive time, privacy/redaction basis and receipt.
- [ ] Verify all host inputs stay quarantined until RAHM, CHILD and explicit owner approval.
- [ ] Verify no direct main write/merge, no self-promotion and revocable least-privilege credentials.
- [ ] If producer/worker is not actually connected/deployed, report NOT_CONNECTED / NOT_DEPLOYED; do not claim automatic all-chat capture.
- [ ] Return raw end-to-end host and repository read-back receipt. CI-only synthetic evidence is not live-host acceptance.
