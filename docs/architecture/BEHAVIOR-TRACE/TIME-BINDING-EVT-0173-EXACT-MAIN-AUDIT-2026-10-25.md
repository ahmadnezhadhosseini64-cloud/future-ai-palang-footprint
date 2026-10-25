# TIME-BINDING-EVT-0173 — Exact-Main Audit Failure

- Event: [EVT-0173](./EVT-0173-CURRENT-065-EXACT-MAIN-AUDIT-FAILURE-AND-CORRECTION-2026-10-25.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0173-2026-10-25
- Canonical clock: actual last-change Git commit timestamp in UTC; Asia/Tehran is derived from the same instant.
- Event registration commit: `61c9c015ed5fb3e85c54590b858d50ea189cfcf1`; UTC `2026-10-25T06:38:57Z`; derived Tehran `2026-10-25T10:08:57+03:30`.
- Failed pre-correction audit run: `40169128251`, UTC `2026-10-25T06:27:09Z`–`2026-10-25T06:27:21Z`; derived Tehran `2026-10-25T09:57:09+03:30`–`2026-10-25T09:57:21+03:30`.
- Failed tested main SHA: `19044f6a238e3d00805813695f328f0540af5e8d`.
- Artifact ID `12589772215`; SHA-256 `4f5e864cbf439e0007974eb23d768827fefe381b1fdf4d81acb16973c6cf7029`.
- Corrective audit: [run 40169837600](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40169837600) PASSED all reported audit steps on repaired SHA `61c9c015ed5fb3e85c54590b858d50ea189cfcf1`; job `121098261378`; artifact `12590062963`, name `living-architecture-audit-40169837600`, size 1,656,191 bytes.
- Later commits advanced the live chain to CURRENT-066 / NEXT-051. [EVT-0175](./EVT-0175-CURRENT-066-RECOVERY-VERIFIER-STALE-CHECKPOINT-2026-10-25.md) records the subsequent stale CURRENT-065 verifier/manifest failure. Therefore the repair PASS applies only to SHA `61c9...`; the exact latest-main SHA is NOT VERIFIED until independently tested.
