# POINT-0/048 (0+) — Same initial ZIP, byte-level read-back and continuous update

- Stable ID: HAIF-POINT-0-048-SAME-ZIP-READBACK-20261027
- Production ID: HAIF-P048-SAME-ZIP-READBACK-20261027
- Type: 0+ production marker on the existing canonical root 0; NOT a second root
- Parent/context: POINT-0/047 → CURRENT-097
- Continuation: IN-086 → OUT-085 → EVT-0223 → CURRENT-098 → NEXT-051
- Status: REGISTERED / LIVING / IMPLEMENTATION IN PROGRESS
- Objective: continue improving the existing initial HAIF starter ZIP with one stable package identity and one canonical archive filename, not create separate version-named ZIPs.

## Verified prior receipt
Run [40516397323](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40516397323), commit `aab1654758d29a05edd240c754d780f3f35a3641`, built the canonical filename `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` from internal package version 0.3.3. Receipt: 19,268 bytes; SHA-256 `fa226aab5a35a76c3f289b511566257a443821195ebdfdfb21f1cc093026e091`; ZIP integrity PASS; 16 source-package tests PASS. This is a historical, run-specific receipt, not a claim about future bytes.

## Corrective implementation
The portable conformance workflow now extracts the exact newly built ZIP to a clean temporary directory, byte-compares all eight required files against the checked-out source, and runs `test_engine.py` from the extracted package before uploading the artifact. This closes the previous gap where source tests and ZIP CRC/inventory checks were not the same as executing tests from the extracted archive.

- Fix commit: `08155ef02f30533558b2396848e9772621b865ba`
- Exact-head workflow run: [40517444577](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40517444577) — QUEUED at registration time; no result inferred.
- Real independent-host import and restart/persistence remain OPEN / NOT RUN.

NEXT-051 remains the only active queue. Do not create NEXT-052.


## Verified canonical ZIP build and artifact round-trip — run 40518077494

- Tested source commit: `b5e29697ec2733c9e9f3ff914525304b2fcb6914`.
- Run: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40518077494
- Uploaded artifact: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40518077494/artifacts/12740188113
- Artifact name: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean`; artifact wrapper: 19,903 bytes; artifact digest SHA-256 `8966f5c58517d1d2c032ae2fcdffb0dd12a1ad8a22f47981ed6b756c1b699d83`.
- ZIP inside artifact: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; internal version 0.3.3; 19,268 bytes; SHA-256 `fa226aab5a35a76c3f289b511566257a443821195ebdfdfb21f1cc093026e091`.
- Exact ZIP extracted and source bytes matched: PASS. Tests run from extracted ZIP: 16/16 PASS. Uploaded artifact was downloaded back by the workflow; the contained ZIP's byte count and SHA-256 matched the receipt, ZIP CRC/inventory passed, and tests ran again from the downloaded artifact: PASS.
- This proves the repository CI artifact round-trip for this run. It does NOT prove import into a real independent AI host; that gate remains NOT RUN.
