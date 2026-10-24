# TIME-BINDING-INT-20261024-026 — Current point 0 registration

- Stable ID: PALANG-TIME-BINDING-INT-20261024-026
- Production ID: TIME-BINDING-INT-20261024-026
- Version: 1.0.0
- Interaction: IN-026 / OUT-026 / EVT-0134
- Current point: CURRENT-036
- Next 0.0: NEXT-036
- Canonical rule: actual last-change Git commit timestamp in UTC; Tehran equivalent is derived from the same instant (UTC+03:30).
- Contextual user-message time supplied by session metadata: UTC 2026-10-24T05:57:00Z = Tehran 2026-10-24T09:27:00+03:30. This is not the repository registration time.

## Canonical repository registration time

Exact per-file last-change commit times are to be filled from GitHub commit metadata after the files are committed. Do not substitute a guessed time or reuse the contextual message time as the canonical repository time.

## Required evidence

- Record the actual commit SHA, UTC commit timestamp, and derived Tehran timestamp for each artifact whose canonical registration time is asserted.
- Preserve separate operation, message, test, and automation timestamps where available.
- A successful write is not a read-back; a read-back is not a semantic match; a structural audit is not runtime/cold-start proof.
- Time-binding ledger's own latest change must be handled by a successor binding/checkpoint rather than guessed in advance.
