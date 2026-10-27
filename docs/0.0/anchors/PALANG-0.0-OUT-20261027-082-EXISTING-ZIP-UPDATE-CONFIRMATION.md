# OUT-082 — Verified answer: same existing ZIP rebuilt, architecture is in-place update

- Stable ID: HAIF-OUT-082-20261027-EXISTING-ZIP-UPDATE-CONFIRMATION
- Production ID: G6IP-OUT-082
- Version: 1.0.0
- Parent: [IN-083](./PALANG-0.0-IN-20261027-083-EXISTING-ZIP-UPDATE-CONFIRMATION.md)
- Root: [POINT-0/045](./GPT6-RAHM-USER-POINT-0-20261027-045-EXISTING-ZIP-UPDATE-CONFIRMATION.md)
- Status: ZIP BUILD + DOWNLOAD + NESTED ARCHIVE READ-BACK VERIFIED; REAL HOST ACCEPTANCE NOT RUN.

Confirmed from the actual downloaded GitHub Actions artifact, not inferred from source files alone:
- Workflow run 40490479934 passed all steps, including rebuilding and uploading the existing starter ZIP.
- Existing canonical filename retained: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Internal manifest version 0.3.1; stable ID `HAIF-GPT6-PORTABLE-STARTER-20261025-004` and production ID `HAIF-G6PS-20261025-004` unchanged.
- Nested ZIP: 19,042 bytes, SHA-256 `3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83`, 8 members, includes independent-host recovery protocol, ZIP integrity PASS.
- Starter tests: 16/16 PASS in the successful workflow. Real independent AI-host import, negative controls and restart persistence remain NOT RUN.
- Outer artifact wrapper is a separate file/hash: 19,635 bytes, SHA-256 `88414a6eae631189dfa364aa382afeba24639571a589d2e44fa8f4f409b62c93`.

Architecture decision: same stable package identity + same canonical ZIP filename + updated source/internal version + rebuilt bytes/hash receipt. Previous hashes are retained as historical versions, not overwritten as if they described the new ZIP. Filename-version mismatch is a known metadata caveat to reconcile explicitly.
