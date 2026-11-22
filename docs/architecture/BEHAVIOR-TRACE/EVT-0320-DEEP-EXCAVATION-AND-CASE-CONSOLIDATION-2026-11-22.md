# EVT-0320 — Deep excavation and case consolidation

- Stable ID: HAIF-EVT-0320-DEEP-EXCAVATION-CASE-CONSOLIDATION-2026-11-22
- Point: POINT-0/089
- Input: IN-133
- Output: OUT-132
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Current checkpoint: CURRENT-151 (after time binding)
- Sole active queue: NEXT-051

## Event

The owner requested a deep excavation and practical simplification of the Future AI / Palang Footprint architecture. The repository was inspected at the existing Golden baseline before any new source files were created. The inspection identified legacy CURRENT-065/CURRENT-066 pointer ambiguity, a quarantined duplicate EVT-0178 draft, deferred-value storage destinations, stale portable package pins, two independent open tracks (#20/#21), and ten Partner implementation cases.

## Disposition

The two legacy checkpoints are retained as immutable historical evidence. Neither is selected as winner. CURRENT-151 becomes the sole live continuation pointer, while the useful work is consolidated into the runtime, historic-census and NEXT-051 tracks. Buffer and Dropbox are explicitly deferred and removed from core acceptance. The ten Partner Issues are maintained as separate cases under NEXT-051.

## Evidence and limitations

The Golden branch was compared with main: 219 ahead / 26 behind; main SHA observed 30d1d3b2de09078131fa3c8a0ff7c492a7ab0d7e. The last exact-main architecture/Evidence Gate receipts passed on that SHA; Portable RAHM Conformance failed on stale package version pins. PR candidate SHA bf7e7ab3fc79e598bf5456605dae2bfa75ef929c passed Portable RAHM Conformance run 45020163367 and Living Architecture Audit run 45020163375. The 24 Starter tests, 31 architecture/governance tests, package digest/inventory, paired-master byte read-back, ZIP extraction and artifact round-trip passed. PR #137 merged to Golden as 41487c7ddab3a7847e569e2fe3ac5d2d69fcca87; a fresh run on the exact post-merge Golden HEAD is pending. Release publication was skipped because the run was a PR. Independent real-host recovery and automatic live ChatGPT capture remain NOT RUN / NOT PROVEN.

This event records repository inspection and scope decisions only. External service provisioning, OAuth, MCP, OpenAI API, private RAHM, independent-host recovery and package verification remain open.

## PR candidate conformance evidence — PR #137

- Tested source SHA: bf7e7ab3fc79e598bf5456605dae2bfa75ef929c (PR candidate before squash merge).
- Portable RAHM Conformance: run 45020163367 / job 137201049892 — SUCCESS.
- Living Architecture Audit: run 45020163375 / job 137201050285 — SUCCESS.
- Starter source and extracted ZIP: 24 tests PASS; architecture/governance audit: 31 tests PASS.
- Synthetic host adapter tests: synthetic ingest, authentication, durable read-back, idempotent retry, conflicting retry rejection and restart recovery all PASS.
- RAHM export package: 1,433,152 bytes; SHA-256 357f770a66e561b851578c2b4db23b2e6b20207ded1a11df6718699a7d95101c.
- Canonical starter ZIP: 281,026 bytes; SHA-256 2046e3ee8aa9f567a42e4f5c85c4d2cba98223671536fd65723df82d2185cbfd.
- Uploaded starter artifact: ID 14753028941; artifact-wrapper SHA-256 49b25df527418e5c50e8aeafad4ea7e3cca7ef230572da8bb4afb75789fb0f64.
- Downloaded artifact receipt, paired-master byte comparison, ZIP inventory/CRC and extracted 24-test round-trip: PASS.
- Release publication was SKIPPED because the run was a PR event. Independent real-host import/restart and automatic live ChatGPT capture were NOT RUN / NOT PROVEN.
- The PR was merged to Golden as commit 41487c7ddab3a7847e569e2fe3ac5d2d69fcca87. A fresh exact-post-merge Golden run is required; PR candidate receipts do not certify the merge commit.

