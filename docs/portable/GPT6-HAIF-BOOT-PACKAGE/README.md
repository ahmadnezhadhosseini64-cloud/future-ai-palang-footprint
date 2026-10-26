# GPT-6 Portable HAIF Boot Package

- Stable ID: `GPT6-HAIF-BOOT-PACKAGE-2026-10-26-001`
- Production ID: `G6IP-PORTABLE-HAIF-001`
- Version: 1.0.0
- Status: REPOSITORY REGISTERED / OPEN / READY FOR EXPORT TEST
- Canonical repository: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Point: [POINT-0/028](../../0.0/anchors/PALANG-0.0-POINT-0-028-GPT6-PORTABLE-HAIF-EXECUTION-2026-10-26.md)
- Event: [EVT-0195](../../architecture/BEHAVIOR-TRACE/EVT-0195-USER-REQUEST-POINT-028-PORTABLE-GPT6-HAIF-EXECUTION-2026-10-26.md)
- Boot instructions: [BOOTSTRAP.md](./BOOTSTRAP.md)

## What this package is
A portable instruction-and-recovery layer for a new GPT-6 host. It tells the host how to rediscover the live canonical repository state, preserve the existing architecture and resume the active work queue without relying on this conversation's hidden history.

## Required boot sequence
1. Read BOOTSTRAP.md completely.
2. Confirm the actual host/model and list available tools/connectors. Do not claim unavailable capabilities.
3. Fetch current `main`, current point register, latest root, current checkpoint, NEXT-051, living master, behavior-trace index, reference index, integration queue, Issues #20/#21, latest mirror event, latest relevant Actions runs and exact tested SHAs.
4. Treat all identifiers mentioned in bootstrap as historical hints only. Rediscover current values independently; never assume this README's observed checkpoint is still current.
5. Build a recovery snapshot with UTC canonical commit times and derived Asia/Tehran times. Keep workflow time, commit time, Library metadata time and operation time distinct; use UNKNOWN if not exposed.
6. Preserve historical points, collision lineage, failed attempts, quarantined records and open gates. Never choose CURRENT-065 vs CURRENT-066 by inference.
7. Continue NEXT-051. Do not create NEXT-052.
8. Read/write/verify repository files only through actually available authorized routes. After every write, independently read back and compare.
9. Run strict portable conformance and the full Living Architecture Audit on the exact final `main` SHA. If any later commit moves `main`, that newer SHA is NOT VERIFIED until separately audited.
10. Attempt clean-host import only when a real independent GPT-6 host is available and authorized. Record exact package digest, host/model, capability manifest, reconstructed state, read-back and differences.
11. Keep Buffer/Persistent Memory as NOT VERIFIED, Dropbox as OPEN/NOT VERIFIED, and external recovery as NOT RUN unless direct evidence changes them.

## Portable contents
- BOOTSTRAP.md — host startup instructions and operating contract.
- manifest.json — package identity, authoritative source, required documents, state rediscovery requirements and explicit unverified gates.

## Important limitation
This directory is not yet proof of a downloaded archive, clean-host import, autonomous background execution or external persistence. Export the package from repository files and calculate the actual archive SHA-256 before claiming a distributable binary artifact.
