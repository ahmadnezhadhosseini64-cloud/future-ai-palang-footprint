# Repository Time Binding — POINT-0/036 Chain

- Stable ID: HAIF-TIME-BINDING-POINT-0-036-CHAIN-20261026
- Production ID: HAIF-TB-P036-20261026
- Version: 1.0.0
- Status: READ-BACK VERIFIED / ACTIVE / LIVING
- Rule: canonical repository time is the actual last-change Git commit timestamp in UTC; Asia/Tehran is calculated from the same instant (+03:30 on the listed dates). User-message time is contextual and was not captured as an exact timestamp.

| Record | Commit SHA | Canonical UTC | Asia/Tehran (+03:30) | Blob SHA |
|---|---|---|---|---|
| POINT-0/036 | `bc7eaacacaaf88273c20dfaeca5753a974ed6fe8` | 2026-10-26T15:10:07Z | 2026-10-26 18:40:07 +03:30 | `a2633039460ed6a689ff0f2cd35b5dfa052f35cd` |
| IN-072 | `99713815c57d6e1fb7d94138189f4399c2f06436` | 2026-10-26T15:10:44Z | 2026-10-26 18:40:44 +03:30 | `dd79bc2912260ee8363fd60464a5d4fa38321e23` |
| OUT-071 | `0bf3cea679426946d9ae94c1a678d0960709fd7d` | 2026-10-26T15:10:55Z | 2026-10-26 18:40:55 +03:30 | `0a877aa5d834e9bc21ae4e4575d3aea5674d43da` |
| EVT-0206 | `69ac1705e4437c082de0b3625989e27a0f749674` | 2026-10-26T15:11:07Z | 2026-10-26 18:41:07 +03:30 | Not separately fetched in this read-back |
| CURRENT-084 | `65a7416de38dfb3473c8e797b69e7d8dba2a848c` | 2026-10-26T15:11:20Z | 2026-10-26 18:41:20 +03:30 | `d49c8b463c9f1fb3e34fce52db2063dd204922b6` |

## Read-back method
The repository path history was queried for each of the five records, and each returned last-change commit was inspected. The root commit is `bc7eaacacaaf88273c20dfaeca5753a974ed6fe8`; the value `a2633039460ed6a689ff0f2cd35b5dfa052f35cd` is the root file's blob SHA, not a commit SHA. This distinction is retained to prevent commit/blob identifier confusion.

## Current verification boundary
This time-binding document does not assert graph closure or independent-host acceptance. Those remain governed by CURRENT-084 and NEXT-051.