# TIME-BINDING-EVT-0251 — Live mirror synchronization

- Stable ID: `PALANG-TIME-BINDING-EVT-0251-LIVE-MIRROR-SYNC-2026-11-06`
- Version: 1.0.0
- Event: [EVT-0251](./EVT-0251-LIVE-MIRROR-SYNC-RECHECK-2026-11-06.md)
- Time rule: actual Git commit UTC is canonical; Tehran is derived from the same instant (+03:30). Workflow run time, Library metadata time and operation/read-back time are distinct.

## Event registration and exact Git binding

- Event registration commit: `88d1d368e854da5e9f6f1963419778b7eccb289f`
- Event commit UTC: `2026-11-06T06:11:02Z`
- Derived Tehran: `2026-11-06T09:41:02+03:30`
- Parent main at event registration: `ca86557ac9d12582f3962fdece9863c09697378e`; commit UTC `2026-11-05T07:07:38Z`; derived Tehran `2026-11-05T10:37:38+03:30`.
- Event file blob SHA after independent read-back: `df17e7dcd6052c7d028f3972b3f229c611e5df1e`; 5,878 characters; exact read-back PASS.
- Event registration operation time and read-back operation time: UNKNOWN (not exposed by GitHub connector).

## Mirror comparison

- Canonical source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`; 10,479 characters.
- Library stable ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`; file ID `file_00000000942881f8a4a3833110229fb7`; exact version 7; 10,480 characters; metadata modified UTC `2026-10-24T04:45:28.479773Z`.
- Normalized content equality PASS; exact content equality FALSE; edit distance 1; only one additional terminal LF in Library. Test ID, Stable ID, Production ID, Version 1.0.0, destination statuses and BOART-FOLLOWUP-01 → 02 → 03 match.
- No Library write. No supported `source_file_ref` upload action was available; the available Library upload path accepts `container_path`, which was not used. No canonical source modification.

## Actions run-time evidence

| Workflow | Run ID | UTC created → updated | Exact tested SHA | Result |
|---|---:|---|---|---|
| Living Architecture Audit (scheduled, run-start head) | 42015763286 | 2026-11-05T11:03:17Z → 11:03:37Z | `ca86557ac9d12582f3962fdece9863c09697378e` | SUCCESS |
| Living Architecture Audit (event push) | 42172829315 | 2026-11-06T06:11:05Z → 06:11:25Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| Portable RAHM Conformance (event push) | 42172828710 | 2026-11-06T06:11:05Z → 06:11:22Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| Evidence Gate (event push) | 42172828774 | 2026-11-06T06:11:05Z → 06:11:17Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| CPREL Independent Runtime Transfer Harness | 42172828635 | 2026-11-06T06:11:05Z → 06:11:21Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| CPREL Independent Transfer Evidence | 42172828737 | 2026-11-06T06:11:05Z → 06:11:23Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| Reconciliation Acceptance Test | 42172828727 | 2026-11-06T06:11:05Z → 06:11:12Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| Production Detection Safety Net | 42172828730 | 2026-11-06T06:11:05Z → 06:11:14Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| Pending Registration Drain | 42172828694 | 2026-11-06T06:11:05Z → 06:11:14Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |
| Reconciliation Watchdog | 42172828648 | 2026-11-06T06:11:05Z → 06:11:15Z | `88d1d368e854da5e9f6f1963419778b7eccb289f` | SUCCESS |

- Audit run 42172829315 job checkout and `GITHUB_SHA` independently identify the exact event SHA.
- Conformance run 42172828710 job checkout and `repository_commit_sha` independently identify the exact event SHA.
- Evidence Gate run 42172828774 checked out the event SHA and created follow-up main `1234599754401221891592d232436c8810018ef0`.
- Evidence Gate follow-up commit: `1234599754401221891592d232436c8810018ef0`; parent `88d1d368e854da5e9f6f1963419778b7eccb289f`; UTC `2026-11-06T06:11:11Z`; derived Tehran `2026-11-06T09:41:11+03:30`. Its only changed path is `evidence/evidence-gate-42172828774.txt`.
- No full Living Architecture Audit or Portable RAHM Conformance run was found on `1234599754401221891592d232436c8810018ef0`; combined-status endpoint returned no individual records. This current head remains NOT VERIFIED.
- Prior Portable RAHM Conformance 41985021983 and Evidence Gate 41985022074 were both on `dfa5c8390350031770af969ac94add523199de51`; they do not verify ca865 or later heads.

## Current anchors and open gates

- Root/checkpoint/queue: POINT-0/061 → CURRENT-112 (Version 1.0.5) → NEXT-051 (Version 1.0.30). Living master Version 1.7.52; Behavior Trace Index 1.0.22; Integration Queue 1.10.26; Behavior Observatory 1.0.13.
- Issues #20 and #21: OPEN.
- CURRENT-065/CURRENT-066 and overlay-manifest lineage: OPEN / AMBIGUOUS; `winner_selected=false`.
- NEXT-051 forensic archive: OPEN / NOT RECOVERED.
- BOART-FOLLOWUP-01: ACTIVE.
- Buffer and Persistent Memory: NOT VERIFIED.
- Dropbox: OPEN / NOT VERIFIED.
- External end-to-end / independent-host recovery: NOT RUN.
- Tool operation/read-back times and exact Library read operation time: UNKNOWN unless separately exposed. Git commit UTC remains the canonical registration time.
- The time-binding file's own final-change commit time is its Git commit metadata; it is not guessed before registration.
