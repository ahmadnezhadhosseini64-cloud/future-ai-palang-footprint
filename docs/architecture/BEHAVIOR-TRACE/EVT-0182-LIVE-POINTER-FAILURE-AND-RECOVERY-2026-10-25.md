# EVT-0182 — Live Pointer Parser Failure and Recovery Work

- Stable ID: `HAIF-EVT-0182-20261025`
- Version: 1.0.0
- Point: [POINT-0/020](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-020-LIVE-POINTER-FAILURE-AND-RECOVERY.md).
- Interaction chain: [IN-060](../../0.0/anchors/PALANG-0.0-IN-20261025-060-LIVE-POINTER-FAILURE-AND-RECOVERY.md) → [OUT-059](../../0.0/anchors/PALANG-0.0-OUT-20261025-059-LIVE-POINTER-FAILURE-AND-RECOVERY.md) → this event → [CURRENT-067](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-067-LIVE-POINTER-FAILURE-AND-RECOVERY.md).
- Prior live audit: [Run 40176902366](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40176902366), commit `4e10f95fb4ca85c3a11a5ad4b5569d45dafc1970`.
- Evidence: job log traceback in `discover_current_0_0_pointer.py`; `CURRENT_ID.search(match.group(1))` returned None because the regex only accepted `CURRENT-###`, while repository filenames use `CURRENT-YYYYMMDD-###`.
- Root-cause class: fixture/repository-shape mismatch; live data shape was not represented in unit tests.
- Impact: pointer discovery crashed before it could emit the intended AMBIGUOUS/BLOCKED result. The audit job failed and later audit steps were skipped.
- Correction plan: support both legacy and date-bearing CURRENT identifiers, add regression fixtures, execute tests on the exact commit, inspect new run/artifact and preserve the old failure as evidence.
- Status: FAILURE CONFIRMED / ROOT CAUSE IDENTIFIED / FIX NOT YET VERIFIED.
- Open gates: CURRENT-065/CURRENT-066 pointer adjudication; runtime and clean round-trip; complete graph triage; independent host; restart persistence; automatic capture/background execution; external storage.
