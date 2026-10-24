# Host Capability Fallback Architecture
Version: 1.0.0
Status: REGISTERED / IMPLEMENTATION AND RUNTIME TESTS OPEN
Parent: HAIF-CORE-MASTER-CHILD-RAHM-2026-09-15-001
Current branch: G6IP-RAHM-CURRENT-046-20261024

## Purpose
Provide an explicit, replaceable architecture for hosts that lack one or more required capabilities. This architecture does not secretly enable unavailable features inside a provider. It selects a declared adapter or external authorized runtime and keeps unsupported capabilities OPEN.

## Capability substitution matrix
| Required capability | Native host path | Fallback path | Proof gate |
|---|---|---|---|
| Durable records | Native durable store | Versioned Git repository / approved object store | Write → fetch → byte/content match |
| Cross-session recall | Native persistent memory | Explicitly load the current master + checkpoint + evidence ledger at session start | Clean-session marker recovery |
| Scheduled work | Native scheduler | Authorized external scheduler/agent invoking a controlled worker | Scheduled idle run + timestamped log + output read-back |
| Continuous observation | Provider-supported events/hooks | Explicit polling/event adapter with permissions and rate limits | Event receipt, duplicate handling, stop control |
| Behavior study | Native logs/hooks | Explicit IN/OUT pair recorder | Pair completeness + provenance + privacy checks |
| Recovery | Native snapshots | Git history + manifest + recovery procedure | Restore into clean workspace and compare |

## Mandatory safety and governance
- Never claim an adapter is installed or running until installation and runtime evidence exist.
- Every external adapter must declare owner, permissions, secret handling, scope, retention, rate limits, stop/revoke method and failure behavior.
- Never bypass provider access controls, user consent, security restrictions or rate limits.
- If no authorized runtime exists, mark background execution UNSUPPORTED / NOT VERIFIED and preserve a manual continuation queue.
- Repository state is the durable source of truth for project artifacts; host memory is a convenience, not the sole archive.
- No Child promotion without evidence, acceptance tests, version/provenance, rollback and master review.

## Activation lifecycle
SPECIFIED → ADAPTER SELECTED → PERMISSIONS REVIEWED → CONFIGURED → TEST EXECUTED → LOGS READ BACK → ACCEPTED FOR A SPECIFIC HOST/VERSION.
Any missing stage leaves the capability OPEN or BLOCKED.

## Linked specifications
- LOCAL_AGENT_RUNTIME_CONTRACT.md
- PERSISTENCE_ADAPTER_SPEC.md
- SCHEDULER_ADAPTER_SPEC.md
- HOST_ADAPTER_CONFORMANCE.md
- Parent portable package: ../../portable/RAHM/
