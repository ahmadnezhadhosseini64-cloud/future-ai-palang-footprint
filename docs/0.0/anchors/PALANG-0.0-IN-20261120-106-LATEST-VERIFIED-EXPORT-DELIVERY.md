# IN-106 — Latest verified export and on-demand delivery requirement

- Stable ID: HAIF-IN-106-LATEST-VERIFIED-EXPORT-20261120-001
- Parent context: POINT-0/065 → CURRENT-116 → NEXT-051
- Status: REGISTERED / OPEN FOR IMPLEMENTATION

## User requirement

The user expects the living architecture to maintain one continuously updated, operational, extractable package and the current living mother reference. Whenever the user asks for "the latest complete version", the system must identify and deliver the newest version that has actually passed its applicable build, integrity, extraction and test checks.

The user must not receive a stale ZIP, a source-only folder presented as a package, or a report in place of the requested artifact.

## Acceptance intent

- Preserve one stable package identity and canonical ZIP filename; update the internal package version as appropriate.
- Keep the living mother reference synchronized into the package.
- Make the latest package and mother reference retrievable together.
- Include a machine-readable build receipt and SHA-256 calculated from actual bytes.
- Clearly distinguish build/test verification from real independent-host recovery.
- If the newest source revision has no successful exact-SHA package receipt, do not label an older artifact "latest complete"; report the exact tested SHA and its age.
