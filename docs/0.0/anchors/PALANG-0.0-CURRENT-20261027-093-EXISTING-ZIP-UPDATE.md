# CURRENT-093 — ادامهٔ 0.0: اصلاح بستهٔ اولیهٔ موجود

- Stable ID: HAIF-CURRENT-093-EXISTING-ZIP-UPDATE-20261027
- Production ID: G6IP-CURRENT-093
- Version: 1.0.0
- Status: ACTIVE / LIVING / IN PROGRESS / NOT COMPLETE
- Chain: POINT-0/043 (0+) → IN-081 → OUT-080 → EVT-0218 → CURRENT-093 → NEXT-051
- Existing package line: [HAIF GPT-6 Portable Starter](../../../../prototype/haif-gpt6-starter/README.md)
- Recovery protocol in ZIP: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Work status
- [x] Confirmed prior turn changed documents/manifest but did not update the starter ZIP.
- [x] Preserved existing stable package ID and historic v0.3.0 digest.
- [x] Updated the same starter package source line to v0.3.1; added the independent-host recovery protocol.
- [x] Updated package tests and build workflow to create a clean, versioned ZIP from the existing package source.
- [ ] Verify fresh workflow run exact commit, test count, artifact presence, ZIP byte count and SHA-256.
- [ ] Download/extract artifact and independently rerun package tests.
- [ ] Real independent-host import, negative controls and independent read-back.
- [ ] Second-host/restart persistence.

No new project or replacement queue was created. NEXT-051 remains the sole active queue. This checkpoint is not complete until build and artifact evidence are read back.
