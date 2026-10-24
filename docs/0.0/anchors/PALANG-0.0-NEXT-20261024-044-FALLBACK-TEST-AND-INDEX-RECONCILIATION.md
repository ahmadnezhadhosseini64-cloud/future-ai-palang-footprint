# NEXT-044 — آزمون جایگزین میزبان، تطبیق فهرست و چکش معماری
- Stable ID: G6IP-RAHM-NEXT-044-20261024
- Production ID: G6IP-NEXT-044
- Version: 1.0.1
- Status: OPEN / NOT RUN
- Parent: CURRENT-046
## Work order
1. Fetch every new fallback-architecture file and CURRENT-046 after write; compare IDs, links and exact content.
2. DONE FOR THIS CYCLE: docs/REFERENCE_INDEX.md was updated with IN-038/OUT-038/EVT-0146/CURRENT-046/NEXT-044/fallback folder and fetched after write; markers and links matched. Read-back blob SHA: `7c6c88d62681bf0d09c333004a87560c10ac9e87`. If the 404 recurs, retain failure evidence and use an alternate authorized GitHub Contents fetch before calling it recovered.
3. Update both living GPT-6 masters and the HAIF mother, then fetch each and match version, branch pointer and open gates.
4. Validate all JSON files and JSON Schema; run valid/invalid fixtures. Record exact validator/version and output.
5. Calculate SHA-256 from exact bytes for each package file, update EXPORT_MANIFEST, fetch and recompute. Never label Git blob SHA-1 as SHA-256.
6. Audit all architecture links, IDs, duplicated content, status contradictions and dangling links; record findings, don't silently merge branches.
7. If an authorized runtime exists, run persistence PT-01–PT-07 and background BG-01; otherwise explicitly record UNSUPPORTED/NOT VERIFIED.
8. Run HC-01–HC-10 in a clean host and independent second host only when available; keep all unrun gates open.
## Acceptance
A file is READ-BACK VERIFIED only when fetched after write and content matches. A capability is VALIDATED only with reproducible evidence. A test not run remains NOT RUN. No background execution is promised by this document.


## Execution checkpoint — partial completion
- Completed: index recovery/update/read-back; creation and read-back of five fallback architecture files; read-back of CURRENT-046, IN-038/OUT-038, EVT-0146, three living mothers and integration queue; syntax parse of three package JSON files.
- Still OPEN / NOT RUN: exact-byte SHA-256 verification; JSON Schema valid/invalid fixtures; full link graph audit; external runtime deployment; persistent-memory restart test; idle background execution test; clean-host and second-host conformance.
- Continue from CURRENT-046. Do not close this action until remaining tests either pass with retained evidence or are explicitly marked unsupported/not verified with reasons.
