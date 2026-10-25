# EVT-0171 — CURRENT-065 Chain Recovery Failure

- Stable ID: HAIF-EVT-0171-CURRENT-065-CHAIN-RECOVERY-FAILURE-2026-10-25
- Production ID: EVT-0171
- Version: 1.0.0
- Lifecycle: ACTIVE / LIVING / FAILURE-PRESERVED / CORRECTION-REQUIRED
- Related prior failures: [EVT-0168](./EVT-0168-LIVING-ARCHITECTURE-AUDIT-FAILURE-AND-ROOT-CAUSE-2026-10-25.md), [EVT-0169](./EVT-0169-PORTABLE-CONFORMANCE-FAILURES-AND-ROOT-CAUSE-2026-10-25.md).
- Current checkpoint: [CURRENT-065](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-065-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md).
- Active next: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Time binding: [TIME-BINDING-EVT-0171](./TIME-BINDING-EVT-0171-CURRENT-065-CHAIN-RECOVERY-2026-10-25.md).

## 1. Failed audit receipt
- Workflow: [Living Architecture Audit run 40168913972](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40168913972).
- Tested commit: `62ac061c3a8e0866a47e782d75c46c4b4863b400`.
- Job: `121095580129`.
- Gate test ID: `RAHM-CURRENT-065-IN-OUT-STATE-RECOVERY-2026-10-25-001`.
- Result: FAIL; `canonical_state_equivalent=true`, but `from_IN=BLOCKED` and `from_OUT=BLOCKED`. Equivalent blocked states are not a PASS.
- All six open gates were preserved as OPEN in both paths; no clean-host, restart, background or external-persistence claim was promoted.

## 2. Exact failure findings
1. OUT-057 had no `Stable ID` field; expected `G6IP-OUT-057-20261025`, actual null.
2. POINT-0/014 did not contain explicit markdown links to IN-058, OUT-057, EVT-0167 and CURRENT-065; a plain-text chain description was insufficient for the verifier.
3. OUT-057 did not directly link back to IN-058 or forward to EVT-0167 and CURRENT-065, so the OUT-origin recovery path was BLOCKED.
4. The failure is in current-chain registration/link integrity. It is separate from the mirror comparison and separate from the portable package build.

## 3. Independent successful result on the same tested SHA
- Portable conformance run [40168913968](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40168913968) passed on the same SHA `62ac061c3a8e0866a47e782d75c46c4b4863b400`.
- Runtime unit tests, valid/invalid pair-schema fixtures, historical CURRENT-062 link recovery, exact-byte SHA-256 evidence, package build and artifact upload all passed.
- Package artifact ID: `12589126698` (`haif-rahm-portable-package`).
- Conformance/digest evidence artifact ID: `12589006804` (`rahm-portable-conformance-evidence`).
- This successful package proof does not override the failed CURRENT-065 interaction-chain gate.

## 4. Corrective work
- Add a complete Stable ID / Production ID / Version / Status / parent-link header to OUT-057.
- Add explicit links in POINT-0/014 to IN-058, OUT-057, EVT-0167, CURRENT-065 and NEXT-051.
- Add explicit links in OUT-057 to IN-058, EVT-0167, CURRENT-065 and NEXT-051.
- Bind OUT-057's actual last-change commit to a separate UTC/Tehran time record.
- Rerun the Living Architecture Audit on the corrected commit and inspect the new output. Keep this failure as historical evidence.
