# OUT-085 — اصلاح گردش‌کار ZIP موجود

- Stable ID: HAIF-OUT-085-SAME-ZIP-READBACK-20261027
- Production ID: G6IP-OUT-085
- Version: 1.0.0
- Status: ZIP BUILD + ARTIFACT ROUND-TRIP VERIFIED / REAL HOST OPEN
- Parent: [IN-086](./PALANG-0.0-IN-20261027-086-SAME-ZIP-READBACK-AND-CONTINUOUS-UPDATE.md)
- Root marker: [POINT-0/048 (0+)](./GPT6-RAHM-USER-POINT-0-20261027-048-SAME-ZIP-READBACK-AND-CONTINUOUS-UPDATE.md)
- Next checkpoint: [CURRENT-098](./PALANG-0.0-CURRENT-20261027-098-SAME-ZIP-READBACK-AND-CONTINUOUS-UPDATE.md)

## Implementation
1. Preserved stable package identity `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
2. Preserved canonical archive filename `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
3. Kept package internal version 0.3.3; workflow hardening does not change package source bytes or falsely claim a new product version.
4. Added clean extraction, byte-for-byte source comparison and execution of package tests from extracted ZIP.
5. The run on fix commit `08155ef02f30533558b2396848e9772621b865ba` is queued; final pass/fail, new digest and artifact read-back must be inspected before closure.

Real independent-host import, negative controls at that host, independent reconstruction from IN/OUT and restart persistence remain OPEN / NOT VERIFIED.


## Verified canonical ZIP build and artifact round-trip — run 40518077494

- Tested source commit: `b5e29697ec2733c9e9f3ff914525304b2fcb6914`.
- Run: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40518077494
- Uploaded artifact: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40518077494/artifacts/12740188113
- Artifact name: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean`; artifact wrapper: 19,903 bytes; artifact digest SHA-256 `8966f5c58517d1d2c032ae2fcdffb0dd12a1ad8a22f47981ed6b756c1b699d83`.
- ZIP inside artifact: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; internal version 0.3.3; 19,268 bytes; SHA-256 `fa226aab5a35a76c3f289b511566257a443821195ebdfdfb21f1cc093026e091`.
- Exact ZIP extracted and source bytes matched: PASS. Tests run from extracted ZIP: 16/16 PASS. Uploaded artifact was downloaded back by the workflow; the contained ZIP's byte count and SHA-256 matched the receipt, ZIP CRC/inventory passed, and tests ran again from the downloaded artifact: PASS.
- This proves the repository CI artifact round-trip for this run. It does NOT prove import into a real independent AI host; that gate remains NOT RUN.
