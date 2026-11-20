# Durable Host Event Ledger

This directory is the repository-side destination for events transferred by the authorized host adapter worker.

- Target branch: `host-intake` only.
- Every event is a separate JSON record with stable event_id, event_type (USER_INPUT / ASSISTANT_OUTPUT), parent_event_id, received UTC and Tehran timestamps, exact payload SHA-256 and provenance.
- Worker refuses any target branch other than `host-intake`.
- All received host events remain QUARANTINED and require owner review through a pull request before merge to main or promotion into the living Master.
- Do not commit secrets, raw private conversation by default, or data without an authorized privacy basis.
- A repository event file proves only that the event reached the repository intake branch; it does not prove that the host itself has durable memory or that all conversations are captured.
- Empty directory README is a structural marker, not a claim that live events have been received.

Related: POINT-0/069, IN-112, OUT-111, EVT-0287, CURRENT-122.
