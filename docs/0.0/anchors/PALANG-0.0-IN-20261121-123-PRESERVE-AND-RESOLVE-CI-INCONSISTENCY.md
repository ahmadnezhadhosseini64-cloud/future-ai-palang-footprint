# IN-123 — Preserve and resolve the first CI inconsistency

- Stable ID: HAIF-IN-123-CI-HISTORICAL-FAILURE-2026-11-21-001
- Status: ACTIVE / LIVING / HISTORICAL-FAILURE-PRESERVED
- Parent: CURRENT-132
- Root: POINT-0/077 (0++)
- Sole queue: NEXT-051
- Related event: EVT-0298 / AI Vacuum package integration

## Owner authorization
The owner explicitly authorized resolving the first-run inconsistency and required that the original inconsistency remain preserved, not deleted, while being connected to the corrected chain.

## Original inconsistency (preserved)
The portable starter README had advanced to CURRENT-132, but prototype/haif-gpt6-starter/test_engine.py still asserted the previous canonical chain ending at CURRENT-131 and the old expected chain string ending CURRENT-131 → NEXT-051. The first portable conformance run failed on this stale assertion. This record preserves the cause; it does not rewrite the earlier failed run as a success.

## Authorized resolution
The test's expected lineage was advanced to include IN-122, OUT-121, EVT-0298, TIME-BINDING-EVT-0298 and CURRENT-132, matching the README and current anchor. The prior CURRENT-131 history and the failed CI evidence remain intact.

## Evidence
- Failed portable conformance run: 44910997351 (earlier branch head; historical failure).
- Corrected test file commit: 4131c5fcd1c271aeb340717fd0baea86968be5e9.
- Passing verification head: 9190b0a9c2dcf1db0133bd937be0bb1a81d3624c.
- Passing portable conformance run: 44911581459.
- Passing architecture audit: 44911581473.
- Passing universal host contract tests: 44911581532.
- Passing universal AI host connectivity tests: 44911581743.

## Preservation rule
Keep this IN record and the failed run as historical evidence. Future fixes append resolution evidence; they must not delete or overwrite this failure record.
