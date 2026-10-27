# Time Binding — EVT-0214 Duplicate-ID Quarantine

- Stable ID: HAIF-TIME-BINDING-EVT-0214-POINT-040-20261027
- Status: REGISTERED / READ-BACK VERIFIED / ACTIVE / LIVING
- Canonical rule: actual final-change repository commit timestamp in UTC; Tehran time is derived from that same instant (+03:30).
- Event operation time: UNKNOWN / not exposed by repository metadata.
- Library metadata time: UNKNOWN / not queried as part of this event.
- Workflow execution time: separate from commit time; see the Actions run metadata.

## Source-backed repository commit times

| Artifact | Commit SHA | Canonical UTC commit time | Tehran equivalent |
|---|---|---|---|
| EVT-0214 collision event | 17f138368fcb99b5b347482a62477e23474dae15 | 2026-10-27T07:53:50Z | 2026-10-27T11:23:50+03:30 |
| Canonical POINT-0/040 last linked update | da340204158a2548571a5f318af0ef0148e6404a | 2026-10-27T07:55:02Z | 2026-10-27T11:25:02+03:30 |
| Canonical EVT-0213 last linked update | 94d74932477553fcdaacfc932dbb223bbd0c0717 | 2026-10-27T07:55:06Z | 2026-10-27T11:25:06+03:30 |
| Canonical CURRENT-089 last linked update | 825e1e9d5723e84d94358e0d46fe45d4f7c58c7b | 2026-10-27T07:55:11Z | 2026-10-27T11:25:11+03:30 |
| Supplemental transfer contract | 93ffab9a705df4c4b437f856a3340d2653cf5d5d | 2026-10-27T07:50:53Z | 2026-10-27T11:20:53+03:30 |
| Supplemental host prompt | 72553b0a0fd15b7a3f8ec62ca70dd2127bac2e45 | 2026-10-27T07:51:11Z | 2026-10-27T11:21:11+03:30 |

## Verification limits

These timestamps are the Git commit metadata returned for the exact commits above. They are not message times, workflow run times, or Library metadata times. A later change to any artifact requires a new final-change binding. The current main HEAD must be independently discovered; no claim that the current HEAD passed paired audit/conformance is made here.
