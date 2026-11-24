# NEXT-051.05 — host enrollment, pair bridge and remaining execution

- Stable queue family: NEXT-051
- Revision: 051.05
- Status: ACTIVE / LIVING / GOLDEN-BRANCH-CANDIDATE / EXACT-SHA-CONFORMANCE-PASS / OWNER-REVIEW-PENDING
- Parent candidate: NEXT-051.04
- Current candidate: [CURRENT-150.05](PALANG-0.0-CURRENT-20261123-150-REVISION-05-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Input/Bridge/Output: [IN-138](PALANG-0.0-IN-20261123-138-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md) → [BRIDGE-0138](PALANG-0.0-BRIDGE-20261123-0138-IN-138-OUT-137.md) → [OUT-137](PALANG-0.0-OUT-20261123-137-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Event: [EVT-0325](../../architecture/BEHAVIOR-TRACE/EVT-0325-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE-2026-11-23.md) → [TIME-BINDING-EVT-0325](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0325-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE-2026-11-23.md)
- Root: [POINT-0/GOLDEN](GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md)
- No NEXT-052 or parallel queue.

- Historical mirror continuity: [EVT-0241](../../architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md) and [TIME-BINDING-EVT-0241](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-2026-10-31.md); preserved evidence only.

## Priority A — finish this interaction pair
- Read back all records and verify all edges.
- Exact PR-head conformance now PASS: Living Architecture Audit #45301053694, Portable RAHM Conformance #45301053616, interaction ledger/recovery #45301053649 and RAHM Runtime Tests #45301053707. Re-run after any further branch edit.
- Owner-controlled Golden review/merge remains pending; the last accepted Golden revision remains CURRENT-150.02 / NEXT-051.02.
- Keep PR #145 open for owner-controlled Golden review; main remains untouched.

## Priority B — simple new-host entry
1. Keep MASTER public for anonymous READ; no collaborator invite or OAuth for READ.
2. Use the one-message prompt to recover exact main HEAD, Reference Index, living mother, current checkpoint and sole queue.
3. Require a compact receipt with a one-time owner challenge, temporary host claim ID, observable model/runtime, exact source SHA/blob SHAs, capability matrix and isolated-workspace test.
4. Owner reviews receipt and issues the official Host ID; host never self-assigns it.
5. Initially allow no write-back. If persistent private work is needed, provision one isolated workspace/repository per host and only later add a narrow broker/App scoped to that host repository.
6. Never give any host MASTER/main write, RAHM access, owner secrets, or another host's data.

## Priority C — ten Partner issues (#114–#123)

| Issue | Assistant-side work still possible | Owner/platform gate |
|---|---|---|
| #114 private service repo/hosting | Prepare minimal Worker/service source and deployment files after target choice | Create/authorize private repo and hosting account |
| #115 GitHub App | Prepare manifest, permission matrix and callback design | Register/install App and authorize owner |
| #116 OAuth broker | Prepare code/tests for state, PKCE, CSRF, encrypted session lifecycle | Secure callback URL and secret storage |
| #117 remote MCP | Evaluate/implement narrow allowlisted tools; prefer maintained GitHub remote MCP for ordinary repo/PR work | Enable endpoint and owner OAuth |
| #118 OpenAI API | Prepare Responses API integration and request limits | Create API project/service account and store key only in provider secret manager |
| #119 deploy | Prepare health checks, logging and deployment workflow | Deploy to authorized HTTPS host |
| #120 promotion | Source workflow and tests exist; inspect/repair as needed | App identity, secrets/variables and owner-approved dispatch |
| #121 approval/principal audit | Read-only evidence and target configuration documented | Set one approval + Code Owner review and retrieve principal audit |
| #122 private RAHM | Prepare schema, export contract and negative tests | Create private owner-only repo and authorize access |
| #123 E2E/host acceptance | Prepare synthetic fixtures, acceptance script and test prompts | Real host, private environment and owner review |

All ten issues remain OPEN until their individual acceptance evidence exists. Avoid unnecessary infrastructure: no second private repo or external service solely for anonymous public READ.

## Priority D — Issue #20 runtime
- Preserve passing local runtime/schema/IN-OUT equivalence evidence at its exact SHA.
- Continue live-capture adapter design, idempotency/conflict tests, persistence and restart harness.
- Automatic capture of every ChatGPT message and clean independent-host recovery remain NOT PROVEN.

## Priority E — Issue #21 semantic source census
- Existing exact main tree inventory: 6,716 entries, not truncated.
- Targeted family counts: 579 0.0 anchors; 558 behavior-trace files; 20 architecture lessons; 9 observatory files; 13 behavior-hunter scripts; 3 HAIF runtime scripts; 5 RAHM tests; 23 starter files.
- Repeated-basename screen: 21 groups; 17 have different blob SHAs and 4 are byte-identical. Nine content-based triage groups have initial dispositions.
- Continue remaining divergent groups in small batches; preserve both sources until authority, lineage and semantic role are proven. Do not renumber, bulk-delete or infer a winner.

## Priority F — owner-only actions (request only at the exact boundary)
- Securely create/authorize private Partner repository and hosting.
- Register/install the GitHub App and complete owner OAuth.
- Create OpenAI API project/service account and place key only in provider secret manager.
- Configure Ruleset 27814009: required approval=1, Code Owner review ON, stale approval dismissal ON, conversation resolution required; then read back live values.
- Create private owner-only RAHM repository.
- Test one independent host with the one-message prompt and return its receipt.
No credentials, MFA codes, PATs or private keys are to be pasted into chat.

## Priority G — exclusions and non-blocking items
- Buffer/Persistent Memory and Dropbox are not core blockers for first public-read host enrollment. Keep their existing statuses; do not spend time on them unless a concrete dependency appears.
- Do not create a new root, queue, host ID, package identity, or external service merely to create the appearance of progress.


## Priority H — Bridge runtime upgrade (assistant-executed)

- Existing local runtime now emits a distinct BRIDGE ID for each IN/OUT pair.
- Bridge explicitly links input, output, event and prior event hash; verification rejects mismatches.
- Reverse lookup works from IN, OUT and BRIDGE.
- JSON Schema, portable RAHM schema, smoke fixture and valid fixture updated.
- Interaction ledger validation/recovery run 45128386247: SUCCESS (schema-validation + input/output recovery jobs all PASS).
- Remaining: fresh Portable RAHM Conformance on head 0f4754704f9837b631bc530e8924b8258f497cd7 after manifest digest reconciliation; then repeat exact-head audit.


## Priority I — reduce the ten Partner issues to what the first host actually needs

The first host is a PUBLIC-READ + local-workspace + owner-reviewed-receipt flow. It does not require a new private repository or deployed service before the first test.

| Issue | First-host dependency | Decision |
|---|---|---|
| #114 private service repo/hosting | NO | Defer; only needed if a custom owner broker is proven necessary. |
| #115 GitHub App | NO | Defer until authenticated owner operations or private per-host repo access is required. |
| #116 OAuth broker | NO | Defer; anonymous public READ does not need OAuth. |
| #117 remote MCP | OPTIONAL | Prefer GitHub's official remote MCP if the actual host/client supports it; custom MCP only for a proven gap. |
| #118 OpenAI API | NO | Needed only for a separately operated API-based host, not a new ChatGPT conversation reading public files. |
| #119 deploy | NO | Defer with the custom broker; do not deploy infrastructure for public READ. |
| #120 promotion automation | NO | Owner can review/export manually until automation is genuinely needed. |
| #121 owner approval gate | YES for any future automated promotion; NO for first read-only host | Existing main protection remains; the target one-approval/Code Owner enforcement is still an owner-side task. |
| #122 private RAHM | NO for first read-only host; YES before private quarantine/promotion | Create only when owner chooses to enable that lane. |
| #123 end-to-end acceptance | YES | Run only after the actual host returns a receipt and its runtime/workspace capabilities can be tested. |

This is a deliberate simplification, not deletion of the ten issues. Keep all ten OPEN with their existing history, but do not block first-host onboarding on optional infrastructure.

## Owner action minimization

Before any owner-side setup, the assistant must:
1. Send the current one-message prompt to a genuinely fresh host (owner action: paste once).
2. Read and validate the returned receipt, exact main SHA and claimed capabilities.
3. Determine whether the host has an isolated workspace, Python/code execution, persistence and restart recovery.
4. Ask for only the single missing owner action that is essential for the next chosen capability.

No new private repository is requested merely to let a host read the public master. No App, token, API key or secret is requested before the capability check. If the host can work locally but cannot persist or write back, it returns a proposal/export for owner review.


## Priority J — one canonical HAIF MVP runtime and package integration

- PR #147 proposes `scripts/haif-runtime/` as the single dependency-free HAIF MVP and archives the former FastAPI/SQLite prototype reversibly. Its checkpoint-prefix correction and runtime tests pass on its own PR head; it is still an unmerged candidate.
- PR #145 adds the IN/OUT/BRIDGE identity, pair verification and reverse lookup to the same runtime path. Both PRs modify `scripts/haif-runtime/haif_runtime.py` and its tests; do not merge them independently or lose either capability.
- Reconcile the checkpoint-prefix validation from #147 with the Bridge/pair implementation from #145 in one candidate branch, add a regression test for append-after-checkpoint, then run the full runtime suite and exact-head architecture/portable conformance.
- Keep one active runtime only. Preserve the former implementation as a recoverable archive; do not create a competing second core.

## Priority K — deliver the one-message + one-package handoff

- Canonical copyable host message: `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`; keep the universal-host entry aligned as a compatibility/reference surface, not a second competing workflow.
- Canonical ZIP identity and filename remain unchanged: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; internal package version is 0.5.2. Rebuild that same identity from the living mother and current references.
- Required before calling it transferable: exact-source build receipt, SHA-256, inventory, safe extraction/CRC, all extracted tests, mother/package byte or semantic read-back, exact-head audit and portable conformance.
- The first real-host test is one paste of the canonical message. The host must return the defined receipt; no official Host ID or ACTIVE status before owner review and independent evidence.
- Current candidate files remain on PR #145 until owner-controlled Golden acceptance. The published latest-verified release and clean-host recovery must not be claimed from a temporary workflow artifact.


## Open acceptance gates — preserved until direct evidence

- CURRENT-065/CURRENT-066 remain OPEN / AMBIGUOUS; no winner selected. Preserve both lineages until semantic source reconciliation proves a resolution.
- Full state recovery: OPEN / NOT RUN; reconstruct independently from IN and OUT.
- Clean host import: OPEN / NOT RUN; a clean interactive AI-host session must import and recover the package.
- Second-host import: OPEN / NOT RUN; second-host acceptance requires a separate receipt.
- Restart persistence: OPEN / NOT VERIFIED; restart/new-session recovery must be demonstrated.
- Idle/background capture: OPEN / NOT VERIFIED; automatic live message capture and idle/background capture require a real authorized producer.
- Graph/identity/parent/time triage: OPEN / REVIEW_REQUIRED; duplicate IDs and ambiguous parents remain subject to source-based adjudication.
