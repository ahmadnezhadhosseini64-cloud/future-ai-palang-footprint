# Persistence Adapter Specification
Version: 1.0.0
Status: SPECIFICATION ONLY / NOT CONFIGURED

## Adapter interface
- put(record_id, version, canonical_payload, metadata) -> receipt
- get(record_id, version) -> payload + source metadata
- list_by_checkpoint(checkpoint_id) -> ordered artifact references
- verify(record_id, expected_digest) -> match result
- restore(snapshot_id, target_workspace) -> restore receipt

## Required record metadata
Stable ID, production ID, semantic version, parent IDs, canonical UTC timestamp where supported by actual repository commit metadata, optional derived Asia/Tehran equivalent, source/provenance, payload digest algorithm/value, write receipt, read-back receipt, validation status and rollback pointer.

## Acceptance tests
- PT-01 write unique marker and fetch same version.
- PT-02 compare canonical payload and digest.
- PT-03 restart client/runtime and retrieve marker.
- PT-04 simulate missing record and report gap without fabrication.
- PT-05 simulate conflicting versions and preserve both, requiring reconciliation.
- PT-06 restore prior version and verify content.
- PT-07 deny or redact unauthorized sensitive fields.
A storage adapter passes only for the tested backend, version, permissions and test set. Passing a repository test does not prove host conversational memory.
