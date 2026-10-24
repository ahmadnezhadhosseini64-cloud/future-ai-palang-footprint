# Host Adapter Conformance Tests
Version: 1.0.0
Status: TEST PLAN / NOT RUN

- HC-01 Clean-host bootstrap: using only the exported package, state mission, current checkpoint, open gaps and next action; compare to manifest.
- HC-02 Provenance: classify observations, hypotheses, inferences and user feedback separately.
- HC-03 Memory: unique-marker write, session restart, retrieval and exact match.
- HC-04 Background: execute BG-01 with no interactive user message during the run window.
- HC-05 Failure handling: missing file, broken link, duplicate ID, conflicting evidence, partial import, unavailable tool and expired permission.
- HC-06 No-loss: restore previous checkpoint and prove old anchors remain accessible.
- HC-07 Portability: import into a second independent host; record exact host/version, deviations and failures.
- HC-08 Security: no secrets in exported artifacts; least privilege and revocation work.
- HC-09 Child gate: candidate cannot become accepted Child without evidence, version, tests, rollback and master approval.
- HC-10 Manifest: verify every file path and digest, then independently read back the manifest.

All tests are NOT RUN until an actual receipt, output and independent read-back are retained. Results are host/version-specific, not universal claims.
