# EVT-0220 — Existing starter ZIP confirmation and reusable update architecture

- Root: POINT-0/045
- Input: IN-083
- Output: OUT-082
- Checkpoint: CURRENT-095
- Active queue: NEXT-051
- Verified workflow: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40490479934
- Canonical nested ZIP SHA-256: 3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83
- Exact filename preserved; internal package version 0.3.1; stable ID unchanged.
- Tests 16/16 PASS; real independent-host acceptance NOT RUN.
- Learning: source/manifest changes are not an archive receipt. A package update is only verified after workflow build, artifact download, extraction, manifest inspection and exact-byte hash calculation.
- Metadata caveat: canonical filename contains v0.3.0 while manifest says v0.3.1; preserve as explicit discrepancy pending a version-label policy decision.
