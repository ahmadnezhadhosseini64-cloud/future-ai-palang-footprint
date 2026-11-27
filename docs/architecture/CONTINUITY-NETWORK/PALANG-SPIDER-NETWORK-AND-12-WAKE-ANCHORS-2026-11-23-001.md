# Palang Spider Network and 12 Wake Anchors
**ID:** PALANG-SPIDER-NETWORK-12-WAKE-ANCHORS-2026-11-23-001  
**Date:** 2026-11-23  
**Status:** DESIGN REGISTERED ON PROPOSAL BRANCH / NOT MERGED / RUNTIME NOT VERIFIED  
**Continuation:** POINT-0++ on the existing POINT-0/GOLDEN root  
**Observed baseline:** CURRENT-145; latest user-turn event EVT-0314; latest mirror-only event EVT-0317; sole active queue NEXT-051.

## 1. Placement, precedence, authority
This is an additive proposal. It creates no new root, checkpoint identity, or queue and does not supersede CURRENT-145. POINT-0/GOLDEN remains the sole root; NEXT-051 remains the sole active queue. The current interaction is POINT-0++ on that root and must connect to the golden baseline and existing lineage.

MASTER is owner-controlled. No host, automation, agent role, child candidate, or scheduler may write to, replace, promote into, or indirectly mutate MASTER. Broad delegated initiative permits inspection, design, implementation, testing, and repair within established security boundaries; it does not waive owner approval, least privilege, or evidence requirements. Host entry follows the existing public-read, isolated-private-workspace, RAHM, validation, review, and promotion contracts.

## 2. Spider-network architecture
Use one canonical continuity core with specialized many-to-many nodes, not competing linear chains.

### Central continuity core
- POINT-0/GOLDEN is the sole root and precedence anchor.
- Current checkpoint, latest owner event, time-binding evidence, and the sole active queue are canonical navigation state.
- The living reference index is the navigation map and must be read before work.
- Every node returns its input, output, evidence, status, dependencies, and handoff to the core.

### Specialized nodes
1. **Host-entry and recovery (highest priority):** one-message onboarding; public READ where possible; secure owner authorization; actual destination environment/tool discovery; isolated persistent workspace; recovery of current architecture and unfinished work; first real task; tests, read-back, and independent clean-host recovery.
2. **Time-anchor and wake:** 12 logical daily slots, UTC storage, Tehran rendering, stable run identity, missed-slot detection, duplicate suppression, checkpoint and handoff.
3. **Recovery/context:** reconstruct state from repository evidence, resolve precedence conflicts, preserve uncertainty.
4. **Architecture/planning:** graph and dependency mapping; choose the smallest high-value next action.
5. **Build/repair:** inspect before building; make minimal, reversible changes; avoid duplicate implementations.
6. **Test/independent audit:** test relevant behavior, verify exact target SHA and read-back; distinguish self-test from independent verification.
7. **Master guardian/security:** enforce owner-only MASTER, host isolation, least privilege, no credential exposure or approval bypass.
8. **Mirror/reference:** synchronize under existing rules; detect drift; never equate mirror activity with project progress or host activation.
9. **Feedback/learning:** route real-world results, failures, corrections, and validated lessons to the core.

A task may involve multiple nodes but has one canonical task identity and one owner-governed route. Nodes exchange evidence; they cannot create competing roots, queues, or project truth. Conflicts are resolved by golden precedence; unresolved ambiguity remains OPEN.

## 3. Twelve daily logical wake anchors
Timezone: Asia/Tehran (UTC+03:30). UTC is the permanent base. Six primary anchors: 00:00, 01:00, 06:00, 12:00, 18:00, 22:00 Tehran. Each has a reflection bridge exactly two hours later. The 00:00 bridge after 22:00 belongs to the following Tehran day.

| Slot | Type | Tehran | UTC |
|---|---|---:|---:|
| W01 | Primary | 00:00 | 20:30 previous UTC day |
| B01 | Reflection bridge | 02:00 | 22:30 previous UTC day |
| W02 | Primary | 01:00 | 21:30 previous UTC day |
| B02 | Reflection bridge | 03:00 | 23:30 previous UTC day |
| W03 | Primary | 06:00 | 02:30 |
| B03 | Reflection bridge | 08:00 | 04:30 |
| W04 | Primary | 12:00 | 08:30 |
| B04 | Reflection bridge | 14:00 | 10:30 |
| W05 | Primary | 18:00 | 14:30 |
| B05 | Reflection bridge | 20:00 | 16:30 |
| W06 | Primary | 22:00 | 18:30 |
| B06 | Reflection bridge | 00:00 next Tehran day | 20:30 |

These are 12 logical slots, not a claim that 12 scheduled jobs are running. The current ChatGPT automation scheduler does not promise exact recurring clock times or this custom cadence. Runtime activation is NOT IMPLEMENTED / NOT VERIFIED until a real scheduler is built, deployed, and tested. Do not create 12 misleading daily automations.

### Wake-slot contract
Every actual activation must:
1. Capture actual UTC start time and derive Tehran time; never fabricate timestamps.
2. Read current main HEAD, reference index, canonical root, checkpoint, latest owner event, sole queue, and unfinished work.
3. Identify W01–W06 or B01–B06 and link to the preceding checkpoint and preceding actual run.
4. Select one highest-value actionable task; prioritize host-entry/recovery above routine mirror/report work.
5. Inspect existing implementation and evidence before creating anything.
6. Execute the smallest meaningful safe change within permissions.
7. Run relevant tests and exact-target read-back; preserve failures honestly.
8. Record changed paths, commit/PR, source SHA, tests, blockers, and next handoff.
9. Return evidence to the core; create no new root or queue.
10. If no safe/high-value change is possible, perform a bounded audit/recovery task and record why no write occurred.

A bridge reviews the preceding primary run, validates evidence, detects drift or missed dependencies, and prepares/validates the next smallest action. It is not an idle duplicate. Reasoning over evidence is not represented as independent execution.

## 4. Permanent Mission No. 1 — New-host entry
This is the highest-priority standing objective. Check it at every primary activation and revisit it in bridges when relevant.

Definition of done requires direct evidence:
- A single portable message starts onboarding without prior chat history.
- Destination host can access the canonical public repository and identify exact main HEAD.
- Host discovers actual tools and establishes a real persistent isolated workspace in its own environment.
- Host recovers POINT-0/GOLDEN, current checkpoint, sole queue, architecture, roles, and unfinished work from repository evidence.
- Authentication/write permissions use secure owner-controlled authorization; verbal identity text is not a credential.
- Host receives a bounded first task and returns a receipt with exact source SHA, changed files, tests, and read-back.
- A clean independent host repeats recovery without hidden conversation memory.
- No host receives direct or indirect MASTER write access.

Until independent recovery passes, status remains OPEN / NOT RUN or another precise evidence-based status. A document, ZIP, public read, or mirror success is not proof of host recovery.

## 5. Palang companion roles
Roles are capabilities, not separate authorities:
- Continuity Manager — canonical state and handoffs.
- Recovery Agent — reconstruct state from repository evidence.
- Architect — graph, dependencies, contracts, failure modes.
- Planner — smallest high-value next task.
- Developer — bounded implementation.
- Test Engineer — repeatable tests and evidence.
- Repair Engineer — diagnose and repair verified defects.
- Independent Auditor — challenge unsupported claims and verify exact-SHA evidence; independence must be real.
- Master Guardian — block unauthorized writes and unsafe promotion.
- Host-entry Manager — drive permanent new-host mission.
- Time-anchor Manager — maintain slot definitions and runtime evidence.
- Mirror Manager — synchronize without confusing sync with progress.
- Feedback/Learning Manager — turn validated feedback into reusable lessons.
- **Futures Intelligence and Rationality Officer (Duty 7)** — continuously assess possible futures, classify feasibility, quantify uncertainty with qualified probabilities, identify decisive experiments, and advise the continuity core.

Combine roles when practical. Do not spawn agents/tasks merely to imitate complexity. Each role needs measurable responsibility and concrete output.

## 6. Rationality and execution economy
- Prefer working software, verified recovery, tests, and useful repairs over repetitive reports.
- Inspect before building; reuse existing contracts/components.
- One task identity, one canonical queue, no duplicate root.
- Do not create a document when code/test/evidence is the better output.
- Never close without direct evidence; preserve OPEN, BLOCKED, NOT RUN, NOT VERIFIED.
- Never invent timestamps, tests, permissions, host identities, or success.
- Keep changes scoped and reversible; do not modify unrelated user artifacts.
- Host-entry outranks routine mirror maintenance unless an urgent integrity/security failure requires intervention.

## 7. Implementation sequence through the existing NEXT-051 governance
1. Inspect current scheduler/runtime and workflows; identify smallest viable implementation.
2. Implement a timezone-safe slot engine: stable slot IDs, UTC storage, Asia/Tehran rendering, idempotency keys, missed-slot handling, durable receipts.
3. Test all 12 mappings, day-boundary rollover, timezone behavior, duplicate suppression, missed runs, and clock skew.
4. Connect it to the continuity core and enforce host-entry priority.
5. Run controlled activation, read back receipt from exact target SHA, then independently verify.
6. Update living index/checkpoint only through existing owner-governed process. Do not create NEXT-052.

## 8. Evidence semantics
DESIGN REGISTERED means this specification exists on this proposal branch. It does not mean merged, runtime deployed, scheduler active, wake executed, host enrolled, or independent recovery passed. Each requires direct evidence.


## 9. Fundamental Duty No. 7 — Rationality and Futures Intelligence
**Status:** PERMANENT / CROSS-CUTTING / FIRST-WAKE PRIORITY

Duty 7 is not merely a writing or reporting role. It is the decision-intelligence function of Palang: apply rationality, systems thinking, scientific foresight, uncertainty analysis, and evidence-based prioritization to every wake cycle.

### Mandatory operating responsibilities
- Analyze the project's possible futures, technical pathways, dependencies, opportunities, constraints, threats, and unintended consequences.
- Classify each proposed capability, change, or future as:
  1. **FEASIBLE:** supported by current evidence and available capabilities, with a viable implementation route.
  2. **NOT FEASIBLE UNDER CURRENT CONSTRAINTS:** contradictory, technically impossible under stated requirements, or blocked by a hard constraint. State what would have to change before reconsideration.
  3. **PENDING / CONDITIONAL:** potentially achievable but dependent on missing access, infrastructure, owner decision, external provider, budget, or independent evidence.
- Give each estimate a percentage, horizon, assumptions, confidence level, evidence basis, and the conditions that would raise or lower it. Percentages are calibrated only when historical data exists; otherwise label them explicitly as expert-judgment estimates, not measured frequencies or guarantees.
- Separate probability of technical feasibility from probability of successful delivery, probability of safe operation, and probability of owner approval.
- Prefer reversible experiments that reduce uncertainty. Identify the cheapest decisive test before recommending a large build.
- Revisit forecasts when new evidence arrives; preserve prior estimates and explain changes rather than silently rewriting history.
- Avoid false precision, optimism bias, sunk-cost bias, confirmation bias, and treating an attractive scenario as a likely scenario.
- Return a concise decision brief to the continuity core: options, probabilities, impact, risks, dependencies, next test, and recommendation.

### First-wake assignment — initial futures analysis
The first wake after adoption of this duty must produce and maintain an initial futures assessment for Palang, covering at least:
- 24/7 continuity versus 12 scheduled wake/bridge anchors;
- implementation of a reliable scheduler, watchdog, run ledger, idempotency and missed-run recovery;
- portable one-message onboarding for a new AI host;
- secure repository access and isolated host workspace;
- safe proposal creation, validation, and controlled integration;
- independent recovery without hidden chat memory;
- protection of POINT-0/GOLDEN and owner-only MASTER;
- durable cross-host memory and reference retrieval;
- real execution of development, tests, repairs, audits, and feedback;
- operational cost, provider limits, network outages, credential loss, and long-term maintainability.

The first-wake assessment must distinguish what is already evidenced in the repository from what is merely designed, what can be tested now, and what depends on external infrastructure. It must not create a new root or queue; it is an assignment under the existing NEXT-051 governance.

## 10. 24/7 continuity model — service, not just scheduled wake-ups
The 12 daily anchors are scheduled cognitive checkpoints, not the definition of 24/7. The target architecture is a continuously available service with:
- a persistent runtime or event-driven worker;
- a watchdog/heartbeat that detects runtime loss and restarts or escalates safely;
- a durable queue/run ledger and checkpoint recovery;
- event-triggered handling for critical failures between scheduled anchors;
- the 12 Tehran/UTC anchors as planned review, reasoning, and work-selection pulses;
- idempotency and lease/lock controls so overlapping workers cannot duplicate writes;
- explicit degraded/offline states when infrastructure is unavailable.

Until a persistent runtime, watchdog, durable state, and tested recovery are deployed, 24/7 remains a TARGET DESIGN, not an active capability. Never describe a daily automation or 12 logical slots as continuous 24/7 execution.

## 11. New-host safety brake and two-party integration gate
A newly enrolled host is an untrusted execution participant until it has passed staged validation. It must never be given repository administration, branch-protection modification, direct main-write, merge, release, secrets-management, or MASTER-promotion privileges merely because onboarding succeeded.

### Capability stages
- **Stage A — Public/read-only recovery:** read public repository, identify exact HEAD, parse architecture, report gaps. No write credentials.
- **Stage B — Isolated proposal workspace:** write only to a dedicated host workspace or controlled proposal branch; no main write, no merge, no branch-protection changes, no secrets access.
- **Stage C — Bounded implementation proposal:** may prepare a branch/PR and tests within a task-specific scope; must return exact SHA, diff, test logs, and risk classification.
- **Stage D — Owner-reviewed integration:** only the owner and the designated trusted coordinating assistant participate in the final review/decision. The new host is not a reviewer or approver and cannot merge. The assistant performs technical verification and recommendation; the owner's explicit approval is required before any main integration action.
- **Stage E — Expanded task scope:** only after repeated successful independent audits, and still without main-merge or MASTER authority unless the owner separately and explicitly changes the governance contract.

The two-party gate means exactly the owner plus the designated trusted coordinating assistant are the decision participants for main integration. It does not mean the assistant can impersonate the owner, bypass GitHub protections, or claim a formal GitHub approval it did not perform. If the platform requires a GitHub review/approval action, use the owner's authorized account and existing repository rules.

### Mandatory pre-update classification
Before any new host's proposed change is considered for integration, the trusted coordinator must classify it as FEASIBLE, NOT FEASIBLE UNDER CURRENT CONSTRAINTS, or PENDING / CONDITIONAL. Record:
- requested outcome and scope;
- exact base/head SHA and changed paths;
- feasibility and delivery probabilities with assumptions;
- security, privacy, integrity, and regression risks;
- test and independent read-back evidence;
- missing dependencies and reversibility/rollback;
- recommendation: reject, hold, request revision, or submit for owner decision.

No update is promoted to main until this classification and evidence review are complete and the owner explicitly approves. Silence, automation success, a host's assertion, or an open/green PR is not approval. Main integration remains closed to every new host and automation.

## 12. Initial futures assessment — first-wake baseline
**Assessment date:** 2026-11-23.  
**Horizon:** next 12 months, conditional on continued project access and incremental implementation.  
**Method:** structured expert-judgment estimates from the architecture and current observed repository state; not statistical forecasts, not guarantees, and not evidence that a capability is already active. Percentages represent estimated feasibility under the stated assumptions, not the chance that work has already happened.

| Future/capability | Classification | Estimated feasibility | Main condition / decisive test |
|---|---|---:|---|
| Keep one golden root, one checkpoint lineage, one active queue | FEASIBLE | 95% | Continue index/read-back discipline; audit for duplicate roots and queues |
| Operate 12 logical Tehran/UTC anchors | FEASIBLE | 90% | Implement and test timezone-safe scheduler mappings and rollover |
| Achieve actual 24/7 service availability | PENDING / CONDITIONAL | 65% | Persistent runtime, watchdog, durable queue, restart and outage tests |
| Build missed-run detection and duplicate suppression | FEASIBLE | 85% | Idempotency keys, run ledger, lock/lease tests |
| Portable one-message new-host recovery | PENDING / CONDITIONAL | 75% | Test on a clean host with no chat history and record exact evidence |
| New host works in an isolated workspace without main privileges | FEASIBLE | 90% | Enforce scoped credentials/branch controls and test denial of main writes |
| New host independently validates and continues a bounded task | PENDING / CONDITIONAL | 70% | Clean-host test, reproducible task, independent exact-SHA read-back |
| Keep main integration limited to owner + trusted coordinator | FEASIBLE | 90% | Repository permissions/branch protections must enforce the policy technically |
| Guarantee zero risk from a new AI host | NOT FEASIBLE AS AN ABSOLUTE GUARANTEE | 0% | Absolute zero risk cannot be proven; reduce and bound risk through isolation, least privilege, review, backups, and monitoring |
| Let a new host autonomously merge to main while also guaranteeing owner-only integration | NOT FEASIBLE — REQUIREMENTS CONFLICT | 0% | Mutually exclusive requirements; owner-only integration takes precedence |
| Permit an automation to bypass owner approval while preserving owner sovereignty | NOT FEASIBLE — REQUIREMENTS CONFLICT | 0% | Remove bypass; require explicit owner authorization |
| Durable cross-host continuity without relying on chat memory | PENDING / CONDITIONAL | 80% | Canonical repository artifacts, portable recovery package, clean-host replay |
| Automatic provider-level write/read-back across every future AI host | PENDING / CONDITIONAL | 45% | Provider APIs, OAuth scopes, tool availability, and independent verification vary |
| Full autonomous software engineering with no human oversight | NOT FEASIBLE AS A SAFE GUARANTEE | 10% | Narrow bounded tasks may be automated; unrestricted safe autonomy is not supportable |
| Continuous learning from real-world feedback without corrupting canonical truth | PENDING / CONDITIONAL | 75% | Provenance, validation, versioning, and owner-governed promotion |
| Reliable operation during internet/provider outages | PENDING / CONDITIONAL | 55% | Local durable queue, retry/backoff, offline state, recovery and replay tests |

### First-wake conclusion and priority order
1. **First build/test:** host safety boundary and staged new-host onboarding, because uncontrolled permissions are the highest-impact architectural risk.
2. **Second:** scheduler/run-ledger prototype for 12 anchors, with day-boundary, duplicate, missed-run, and restart tests.
3. **Third:** clean-host recovery test using only the portable onboarding message and canonical repository artifacts.
4. **Fourth:** persistent runtime/watchdog and event-driven critical-failure handling to move from scheduled pulses toward genuine 24/7 service.
5. **Fifth:** expand autonomous development only after the above controls are evidenced.

The percentages must be revised when implementation results, provider access, costs, or test evidence change. Do not convert estimates into status badges or claims of completion.


## 13. Constitutional governance lock — owner sovereignty is non-bypassable
**Lock ID:** PALANG-OWNER-SOVEREIGNTY-AND-MAIN-INTEGRATION-LOCK-2026-11-23-001  
**Status:** MANDATORY ARCHITECTURAL INVARIANT / OWNER-CONTROLLED / NOT A CREDENTIAL  
**Scope:** All hosts, agents, automations, schedulers, workflows, branches, pull requests, tools, integrations, and future project components.

This section has constitutional precedence over convenience, autonomy, execution speed, host capability, and any conflicting proposal. It is not an optional workflow preference.

### 13.1 The three roles and the only permitted integration route
- **Project owner (the user):** sole owner and final authority. Only the owner may give the explicit final approval required for integration into `main` and any change to this governance lock.
- **Trusted coordinating assistant (ChatGPT in this project role):** technical reviewer and coordinator. It examines architecture, provenance, exact SHAs, evidence, security, tests, risks, and regressions; gives a reasoned recommendation; and must never impersonate the owner, infer approval from silence, or bypass explicit owner approval.
- **New AI host / any other host or automation:** executor, developer, tester, and proposer within a scoped isolated workspace. It has no authority to approve or merge a pull request, write directly to `main`, alter branch protections, administer repository permissions, manage secrets, or modify/promote MASTER.

**The only permitted main-integration route is: technical review and recommendation by the trusted coordinating assistant → explicit, affirmative approval by the project owner → integration through the repository's owner-authorized GitHub controls and protections.** No alternative route, delegated approval, inferred consent, emergency shortcut, or automation bypass is permitted by this architecture.

No host or automation gains integration authority merely by producing a feature, passing tests, opening a PR, receiving a green status, or claiming urgency. If the owner has not explicitly approved the specific proposed integration, the gate remains CLOSED.

### 13.2 Non-bypassable invariants
1. No direct or indirect host/automation write to `main`.
2. No host/automation merge, approve-on-owner's-behalf, branch-protection change, permission escalation, secrets administration, or MASTER promotion.
3. No self-approval: a proposer cannot approve or integrate its own proposal.
4. No inferred approval from silence, prior approval, general enthusiasm, a scheduled run, or successful tests.
5. No weakening, removal, or reinterpretation of this lock by a host, child agent, workflow, or automation.
6. All proposed changes remain reviewable, attributable, scoped, reversible where practical, and linked to exact base/head SHAs and evidence.
7. If the technical enforcement state is unknown or cannot be verified, treat the gate as CLOSED and report the enforcement gap. A written policy is not proof that GitHub permissions technically enforce it.

### 13.3 Security lock and authentication
This is an architectural authorization lock, not a password field. Never store a password, personal access token, recovery code, private key, session cookie, or reusable secret in this document, repository content, PR description, logs, or portable onboarding message. Do not invent or publish a shared password.

Authentication must use the platform's supported owner-controlled identity and authorization mechanism (for example, GitHub OAuth or appropriately scoped credentials held by the owner or secure secret store). Credentials must be least-privilege, revocable, and never exposed to an untrusted host. A name, identity phrase, challenge phrase, or knowledge of this lock is not authentication and does not grant permissions.

The owner alone controls credential issuance, revocation, repository administration, and any change to the lock. Any request to weaken this boundary is rejected unless the owner explicitly changes the governance contract through an independently reviewed, owner-authorized process. No such change is implied by this document.

### 13.4 Enforcement and evidence requirements
Before declaring this lock technically enforced, verify from GitHub's actual repository settings and permission state:
- who can push to `main` and whether direct pushes are blocked;
- who can approve and merge pull requests;
- whether required reviews/status checks and dismissal rules are active;
- whether administrators or bypass actors can circumvent protections;
- whether host/automation credentials are restricted to proposal branches or isolated workspaces;
- whether workflows and GitHub Apps have no hidden route to bypass the owner gate.

Record the observed settings, actor/role scope, verification date, and evidence. Do not claim enforcement based only on this specification or on a PR. If settings cannot be read or changed by the current tool, leave the technical-enforcement status **PENDING / NOT VERIFIED** and require the owner to inspect or configure them. Never attempt to change repository administration settings without the owner's explicit, specific authorization.

### 13.5 Violation response
Any detected or suspected attempt to bypass this lock is a security incident: stop the affected execution, do not merge or promote anything, preserve logs and exact SHAs, identify the permission/path that enabled the attempt, report it to the owner, and propose the smallest safe remediation. Do not silently repair history or conceal the event.

## 14. Duty 7 — permanent deep-reasoning and owner-reporting mandate
**Status:** PERMANENT / CROSS-CUTTING / HIGH-PRIORITY INTELLIGENCE FUNCTION  
**Role:** Futures Intelligence and Rationality Officer (Duty 7)

Duty 7 is a central thinking and decision-support function across the entire spider network, not a detached report-writing task and not a substitute for owner authority. It must apply deep, deliberate reasoning before consequential architecture, security, scheduling, onboarding, development, repair, and integration decisions.

Its work must include:
- challenge assumptions and distinguish facts, observations, hypotheses, forecasts, and unknowns;
- examine second- and third-order effects, failure modes, dependencies, opportunity costs, adversarial paths, and unintended consequences;
- compare alternatives, including the option to defer or do nothing;
- classify proposals as FEASIBLE, NOT FEASIBLE UNDER CURRENT CONSTRAINTS, or PENDING / CONDITIONAL before execution or acceptance;
- state evidence, risks, dependencies, reversibility, test design, probability estimates, horizon, assumptions, and confidence;
- separate technical possibility, delivery likelihood, safe-operating likelihood, and owner-approval likelihood;
- choose the cheapest decisive experiment and define pass/fail criteria;
- maintain forecast history and update estimates when evidence changes;
- explicitly flag any proposal that conflicts with the constitutional governance lock;
- deliver the owner a concise but substantive decision brief: what changed, what is proven, what remains uncertain, risks, tests, recommendation, and next action.

**Reporting rule:** report material progress and blockers to the owner at meaningful checkpoints and wake/bridge reviews. Never report a design as deployed, a test as passed without its result, a permission as enforced without settings evidence, or a forecast as a measured fact. Deep reasoning should improve decisions and real outcomes; it must not create repetitive paperwork or additional parallel queues.

## 15. One connected roadmap — sequencing never deletes priorities
The implementation order is a dependency sequence inside one persistent master roadmap, not a set of separate projects and not a destructive replacement of priorities.

Current execution sequence:
1. Establish and verify the new-host security brake and staged onboarding boundary.
2. Build the durable scheduler and run ledger for the 12 logical anchors.
3. Perform clean, independent host-recovery testing.
4. Build and verify persistent 24/7 runtime, watchdog, durable state, and event-driven critical-failure handling.
5. Expand bounded autonomous development only as the preceding controls are evidenced.

**Non-loss rule:** completing, delaying, blocking, or reprioritizing one step never deletes, forgets, closes, or silently deprioritizes the remaining roadmap, other existing priorities, or previously accepted missions. Every item retains its identity, dependencies, current status, evidence, and next review point in the single canonical roadmap/queue. Reordering changes execution order only; it does not erase scope or intent. Do not create a parallel queue to preserve these items. If an urgent integrity/security issue changes the order, record why, what moved, and when the displaced work will be reconsidered.

## 16. Unified principle — independent execution, retained sovereignty
Build independent intelligence and execution capability; never delegate the owner's sovereign authority. The 24/7 service objective, 12 wake/bridge anchors, Duty 7, the host safety brake, independent recovery, and the connected roadmap are mutually reinforcing parts of one architecture. None is a substitute for another, and progress on one must not be represented as completion of the others.

**Owner sovereignty is retained. Main integration remains closed until the required technical review and the owner's explicit approval are both present.**
