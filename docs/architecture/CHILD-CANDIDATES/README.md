# CHILD — Owner-Reviewed Candidate Area

- Status: EMPTY UNTIL A VALIDATED BOT PR IS APPROVED AND MERGED
- Owner / sole Code Owner: @ahmadnezhadhosseini64-cloud
- Parent flow: private host workspace → owner export → private RAHM → RAHM validation → bot-authored PR → owner approval → CHILD.

This directory contains sanitized, provenance-linked candidate knowledge extracted from host work. A merged Child candidate is NOT automatically part of the living Master and does not authorize any host to write to the master repository.

## Admission rules

1. A candidate must originate from a registered Host ID and a pinned source workspace/repository commit.
2. The owner must export and redact the candidate before it enters the public Child area.
3. The private RAHM manifest must attest to owner redaction and owner authorization for Child review.
4. The promotion workflow verifies candidate identity, required files, SHA-256 digests, byte limits, file types, and secret/path-traversal/symlink checks.
5. The workflow opens a PR as the owner-controlled promotion GitHub App. It never merges or edits the living Master.
6. The owner reviews and approves the PR. Required Ruleset approval must be from @ahmadnezhadhosseini64-cloud.
7. Rejected, superseded, or conflicting candidates remain traceable in RAHM; do not silently overwrite them.

## Status lifecycle

EXPORTED → QUARANTINED → RAHM_VALIDATED → BOT_PR_OPEN → OWNER_APPROVED → CHILD_ACCEPTED

Any failed gate remains REJECTED, CONFLICT, or OPEN / NOT VERIFIED. No automatic transition to MASTER exists.
