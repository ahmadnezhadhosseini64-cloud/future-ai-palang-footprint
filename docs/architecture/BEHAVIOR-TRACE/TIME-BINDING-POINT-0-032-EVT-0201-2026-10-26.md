# Canonical time binding — POINT-0/032 / EVT-0201

- Stable ID: HAIF-TIME-BINDING-POINT-0-032-EVT-0201-20261026
- Version: 1.0.0
- Status: REGISTERED / READ-BACK PENDING
- Rule: actual repository commit time in UTC is canonical; Asia/Tehran is the same instant converted by +03:30. User-message time is not inferred from commit time.

| Artifact | Commit SHA | Canonical repository time (UTC) | Derived Tehran time |
|---|---|---|---|
| POINT-0/032 | b6ab52f279ec4a68d494a1520c3fafd34d06e813 | 2026-10-26T08:57:51Z | 2026-10-26T12:27:51+03:30 |
| IN-067 | e3b6b5c4f41fa25be0eb1bf26027a1fad334251e | 2026-10-26T08:51:12Z | 2026-10-26T12:21:12+03:30 |
| OUT-066 | 4b3b70faf31a85b93676ae2bdb28355fa199d123 | 2026-10-26T08:51:16Z | 2026-10-26T12:21:16+03:30 |
| EVT-0201 | 2862ed661c1013bff4a17c604edcb6309ef04a26 | 2026-10-26T09:02:40Z | 2026-10-26T12:32:40+03:30 |
| Cross-validation contract | 43fb22c35161a87feae778a8af128621cd425f55 | 2026-10-26T09:01:41Z | 2026-10-26T12:31:41+03:30 |
| CURRENT-079 | 2de366040c7b0e04a344bffac22cb6f7911a8085 | 2026-10-26T09:05:24Z | 2026-10-26T12:35:24+03:30 |

## Evidence boundary
These timestamps are actual commit metadata fetched from the repository. They do not prove external project execution, independent-host import, persistence or background operation. The time-binding document's own timestamp is intentionally not self-referenced; it can be added by a later ledger update.


## Added repository artifacts (latest actual content-change commits)

| Artifact | Commit SHA | Canonical repository time (UTC) | Derived Tehran time |
|---|---|---|---|
| Interactive project validation runbook | c615b9278dbe344f5fb6fa9c4a680a13da33e63f | 2026-10-26T08:57:14Z | 2026-10-26T12:27:14+03:30 |
| Reversible gap-cover register update | 4dbc99185daa656a30140074405e68e171f3b4e2 | 2026-10-26T08:58:32Z | 2026-10-26T12:28:32+03:30 |
| RAHM_BOOT update | c35b2f031326b63d3776f58983d222804d1005db | 2026-10-26T08:57:50Z | 2026-10-26T12:27:50+03:30 |

The duplicate same-number artifacts are intentionally not treated as canonical rows in this table; they are preserved as conflicted evidence in GAP-POINT032-DUPLICATE-CHAIN. The time-binding document's own current edit time is not self-referenced. The export manifest's version and digest are recorded by the manifest and workflow receipts; the manifest is not given a row here because it includes this mutable time-binding document and a self-referential registration timestamp would not be stable.

- Current-checkpoint conformance receipt added by commit `2de366040c7b0e04a344bffac22cb6f7911a8085`; its actual commit time is the canonical repository registration time for CURRENT-079.
