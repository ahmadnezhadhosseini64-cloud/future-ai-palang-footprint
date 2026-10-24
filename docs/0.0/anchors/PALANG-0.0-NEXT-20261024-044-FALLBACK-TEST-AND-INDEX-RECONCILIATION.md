# NEXT-044 — آزمون جایگزین میزبان، تطبیق فهرست و چکش معماری
- Stable ID: G6IP-RAHM-NEXT-044-20261024
- Production ID: G6IP-NEXT-044
- Version: 1.0.0
- Status: OPEN / NOT RUN
- Parent: CURRENT-046
## Work order
1. Fetch every new fallback-architecture file and CURRENT-046 after write; compare IDs, links and exact content.
2. Update docs/REFERENCE_INDEX.md with IN-038, OUT-038, EVT-0146, CURRENT-046, NEXT-044 and fallback folder. Fetch index again using both fetch_file and direct GitHub Contents API if necessary; compare expected unique marker and links. If mismatch, leave OPEN and retain failure evidence.
3. Update both living GPT-6 masters and the HAIF mother, then fetch each and match version, branch pointer and open gates.
4. Validate all JSON files and JSON Schema; run valid/invalid fixtures. Record exact validator/version and output.
5. Calculate SHA-256 from exact bytes for each package file, update EXPORT_MANIFEST, fetch and recompute. Never label Git blob SHA-1 as SHA-256.
6. Audit all architecture links, IDs, duplicated content, status contradictions and dangling links; record findings, don't silently merge branches.
7. If an authorized runtime exists, run persistence PT-01–PT-07 and background BG-01; otherwise explicitly record UNSUPPORTED/NOT VERIFIED.
8. Run HC-01–HC-10 in a clean host and independent second host only when available; keep all unrun gates open.
## Acceptance
A file is READ-BACK VERIFIED only when fetched after write and content matches. A capability is VALIDATED only with reproducible evidence. A test not run remains NOT RUN. No background execution is promised by this document.
