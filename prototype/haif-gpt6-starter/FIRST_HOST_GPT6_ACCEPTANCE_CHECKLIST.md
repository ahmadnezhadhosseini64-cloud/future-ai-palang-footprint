# First interactive GPT-6 host — acceptance checklist

Package identity: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`
Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
Paired handoff: canonical ZIP + current living master reference.
Current source chain: POINT-0/050 (0+ marker on canonical root 0) → IN-088 → OUT-087 → EVT-0225 → CURRENT-100 → NEXT-051.

## A. Before import
- [ ] Record exact source commit, internal package version, ZIP byte count and SHA-256 from the fresh workflow receipt.
- [ ] Upload the ZIP and living master together into a clean interactive GPT-6 session.
- [ ] Confirm the host can access and read both files; record any tool/file limits instead of assuming access.
- [ ] Ask the host to recover canonical point 0, 0+ meaning, latest 0.0 checkpoint CURRENT-100, sole queue NEXT-051, stable package ID and all open gates without using prior chat history.

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

## E. Restart and final verdict
- [ ] Close/restart the session and recover from the same pair of files or proven durable state.
- [ ] Record separate PASS/FAIL/NOT RUN for import, digest, IN/OUT equivalence, negative controls, read-back, live producer, repository write-back and restart.
- [ ] Save the direct host receipt into the project chain only after read-back verification.

## Status boundary
A CI build, a local engine test, or two independent CI runners do not prove that an interactive GPT-6 host imported the package. Until this checklist has direct host evidence, real host acceptance is `NOT RUN / NOT VERIFIED`.
