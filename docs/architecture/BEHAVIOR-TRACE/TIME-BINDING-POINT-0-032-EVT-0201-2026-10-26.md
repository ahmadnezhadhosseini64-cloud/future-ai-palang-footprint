# Canonical time binding — POINT-0/032 / EVT-0201

- Stable ID: HAIF-TIME-BINDING-POINT-0-032-EVT-0201-20261026
- Version: 1.0.0
- Status: REGISTERED / READ-BACK PENDING
- Rule: actual repository commit time in UTC is canonical; Asia/Tehran is the same instant converted by +03:30. User-message time is not inferred from commit time.

| Artifact | Commit SHA | Canonical repository time (UTC) | Derived Tehran time |
|---|---|---|---|
| POINT-0/032 | eae81b2812dfb3fb49f9f180327af3be7cb56f84 | 2026-10-26T08:57:38Z | 2026-10-26T12:27:38+03:30 |
| IN-067 | e3b6b5c4f41fa25be0eb1bf26027a1fad334251e | 2026-10-26T08:51:12Z | 2026-10-26T12:21:12+03:30 |
| OUT-066 | 4b3b70faf31a85b93676ae2bdb28355fa199d123 | 2026-10-26T08:51:16Z | 2026-10-26T12:21:16+03:30 |
| EVT-0201 | b5af6112a503593a8874bfaa9de304b27ae41ebb | 2026-10-26T08:58:06Z | 2026-10-26T12:28:06+03:30 |
| Cross-validation contract | d4f33fb192641aa35b5e33bde8985e4c846a50b6 | 2026-10-26T08:57:32Z | 2026-10-26T12:27:32+03:30 |
| CURRENT-079 | 5ed2805d0bb0befb39570d60ffd04fd200a2d602 | 2026-10-26T08:57:44Z | 2026-10-26T12:27:44+03:30 |

## Evidence boundary
These timestamps are actual commit metadata fetched from the repository. They do not prove external project execution, independent-host import, persistence or background operation. The time-binding document's own timestamp is intentionally not self-referenced; it can be added by a later ledger update.


## Added repository artifacts (latest actual content-change commits)

| Artifact | Commit SHA | Canonical repository time (UTC) | Derived Tehran time |
|---|---|---|---|
| Interactive project validation runbook | c615b9278dbe344f5fb6fa9c4a680a13da33e63f | 2026-10-26T08:57:14Z | 2026-10-26T12:27:14+03:30 |
| Reversible gap-cover register update | 4dbc99185daa656a30140074405e68e171f3b4e2 | 2026-10-26T08:58:32Z | 2026-10-26T12:28:32+03:30 |
| RAHM_BOOT update | c35b2f031326b63d3776f58983d222804d1005db | 2026-10-26T08:57:50Z | 2026-10-26T12:27:50+03:30 |
| Export manifest 1.8.10 | 1f53122f2f0ccc0889e9219f36ff10d936d807b6 | 2026-10-26T09:01:03Z | 2026-10-26T12:31:03+03:30 |

The duplicate same-number artifacts are intentionally not treated as canonical rows in this table; they are preserved as conflicted evidence in GAP-POINT032-DUPLICATE-CHAIN. The time-binding document's own current edit time is not self-referenced; a later ledger update may add it.
