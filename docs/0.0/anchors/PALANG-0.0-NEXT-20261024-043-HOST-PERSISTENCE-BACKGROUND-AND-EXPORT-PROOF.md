# NEXT-043 — اثبات بسته، حافظهٔ پایدار و اجرای پس‌زمینه
- Stable ID: G6IP-RAHM-NEXT-043-20261024
- Production ID: G6IP-NEXT-043
- Version: 1.0.0
- Status: OPEN / NOT RUN
- Parent: CURRENT-045

## Required sequence
1. Fetch all eight package files after writes; record path, blob SHA and content.
2. Compute SHA-256 from exact UTF-8 bytes; update EXPORT_MANIFEST, fetch it again, and independently recompute/compare. Record the manifest's own digest in the checkpoint/ledger to avoid self-reference.
3. Parse HOST_CAPABILITY_MANIFEST.json and INTERACTION_PAIR_SCHEMA.json; validate syntax and one valid plus one invalid sample.
4. Run CT-001–CT-006 in a clean context and preserve evidence.
5. Test persistent memory with a unique marker across a new session/restart if supported; otherwise UNSUPPORTED/NOT VERIFIED.
6. Test idle background only if an authorized scheduler/agent exists: run while user interaction is inactive, retain timestamped log and durable output, independently read back, and prove stop/revoke. Otherwise UNSUPPORTED/NOT VERIFIED.
7. Run the same package on an independently available second AI host; preserve failures. No universal compatibility claim.
8. Update living masters, index and queue with exact evidence and statuses.

## Acceptance
Package integrity PASS only when digests match. Persistent memory PASS only after restart retrieval. Background execution PASS only after idle execution evidence. Cross-host PASS only for the tested host/version and exact package. Otherwise keep gates open.
