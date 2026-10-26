# EVT-0195 — User Request: Anchor POINT-0/028 and Prepare Portable GPT-6 HAIF Execution

- Stable ID: `EVT-0195-USER-REQUEST-POINT-028-PORTABLE-GPT6-HAIF-EXECUTION-2026-10-26-001`
- Production ID: `G6IP-EVT-0195`
- Version: 1.0.0
- Status: REGISTERED / OPEN / LIVING
- User intent: create a new point, connect it to prior points, create next 0.0 steps, finish remaining required work, and prioritize an executable portable model for a new GPT-6 host.
- Parent observed: POINT-0/027 → CURRENT-074 → NEXT-051
- New point: [POINT-0/028](../../0.0/anchors/PALANG-0.0-POINT-0-028-GPT6-PORTABLE-HAIF-EXECUTION-2026-10-26.md)
- Portable package: [GPT-6 Portable HAIF Boot Package](../../portable/GPT6-HAIF-BOOT-PACKAGE/README.md)
- Canonical rule: repository source remains authoritative; no hidden background work is implied.

## Captured requirement
The user wants a portable package that can be transferred into a new GPT-6 environment and instruct that host to resume the project using its own visible capabilities, while preserving the graph, current queue, evidence discipline, historical points and open gates.

## Result and limits
The portable package files are being registered in the canonical repository. A package can carry instructions, a manifest and a recovery protocol; it cannot itself grant the new host access to GitHub, Library, Dropbox, memory or external execution. Each connector/permission must be present and each external destination independently verified.

## Failure-prevention lesson
Do not divert to the older Dropbox failover branch when the current user objective is continuing the HAIF model architecture and preparing clean-host portability. Dropbox remains a separate OPEN / NOT VERIFIED branch and must not displace NEXT-051.

## Acceptance gates
- Repository files independently read back and matched.
- Indexes and mother document linked.
- Strict portable conformance run and full audit tested on the exact final main SHA.
- Clean independent GPT-6 host import and state reconstruction evidenced; otherwise NOT RUN.
- NEXT-051, Issues #20/#21, CURRENT-065/CURRENT-066 and graph-census gaps remain open until proof closes them.
