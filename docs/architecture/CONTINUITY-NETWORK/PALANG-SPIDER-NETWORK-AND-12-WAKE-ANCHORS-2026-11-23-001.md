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
