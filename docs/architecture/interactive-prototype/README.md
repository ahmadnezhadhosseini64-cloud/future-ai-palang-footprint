# HAIF Interactive Prototype v0

- Stable ID: HAIF-INTERACTIVE-PROTOTYPE-V0-2026-10-25-001
- Production ID: HAIF-PROTOTYPE-V0
- Version: 0.1.0
- Status: SOURCE BUILT / REPOSITORY READ-BACK REQUIRED / BROWSER EXECUTION NOT RUN BY REPOSITORY WRITE ALONE
- Parent: [NEXT-039](../../0.0/anchors/PALANG-0.0-NEXT-20261024-039-BUILD-INTERACTIVE-PROTOTYPE.md)
- Architecture mother: [Initial-model master](../مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Artifact: [index.html](./index.html)

## Purpose
A small, inspectable browser prototype demonstrating user input, visible output, IN/OUT event capture, checkpoint creation, structural validation, JSON export/import and same-browser persistence where localStorage is available.

## Run
Open `index.html` in a modern browser. No build system or network dependency is required.

## Acceptance test
1. Open the page and confirm it explicitly identifies itself as a prototype.
2. Submit a non-empty input; verify one IN/OUT event and an updated count.
3. Submit an empty input; verify an error and no new event.
4. Create a checkpoint; verify a checkpoint ID and that open external-host/persistence/background gates remain visible in exported JSON.
5. Export JSON; copy the JSON to a separate file.
6. Reload the page; if localStorage is available, verify same-browser events persist. If not, record UNSUPPORTED rather than PASS.
7. Paste exported JSON into a clean browser/profile or another device and import it; verify the events and checkpoint are reconstructed. This demonstrates manual JSON import, not automatic independent-host adoption.
8. Replace JSON with invalid text and verify rejection.
9. Change a valid field or remove a required field and verify structural validation rejects the altered state where the required condition is violated.
10. Record actual browser/version, UTC test time, pass/fail, screenshots or logs, and independent read-back in the execution receipt.

## Explicit non-claims
- No remote database, authentication, encryption, synchronization or cloud backup.
- No automatic connection to an AI host, no automatic capture of every chat, no background/idle agent.
- Browser localStorage is same-origin local persistence, not durable cross-host memory.
- Source presence and repository read-back do not equal browser execution. Until a real test receipt exists, browser exercise and clean-profile adoption remain NOT RUN / NOT VERIFIED.
