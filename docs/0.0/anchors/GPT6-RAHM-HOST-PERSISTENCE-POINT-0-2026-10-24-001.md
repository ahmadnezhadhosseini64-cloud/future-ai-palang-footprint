# Point 0 — شاخهٔ اثبات حافظهٔ پایدار و اجرای پس‌زمینهٔ میزبان
- Stable ID: G6IP-RAHM-HOST-PERSISTENCE-POINT-0-20261024-001
- Production ID: G6IP-HOST-PERSISTENCE-POINT-0-001
- Version: 1.0.0
- Parent architecture: HAIF-CORE-MASTER-CHILD-RAHM-2026-09-15-001
- Parent Rahm branch checkpoint: G6IP-RAHM-CURRENT-044-20261024
- Interaction: IN-037 → OUT-037 → EVT-0145 → CURRENT-045
- Status: REGISTERED; package files fetched after write; full integrity and runtime validation remain open.

## Purpose
Establish a distinct, recoverable branch focused on whether an AI host can actually provide durable memory and automatic background execution, and how the transferable HAIF/Rahm package can prove those capabilities instead of assuming them.

## Governing distinction
1. Repository/durable artifact storage is not conversational memory.
2. Conversational memory is not a complete versioned archive.
3. Responding to a prompt is not an always-on background process.
4. A declared capability is not an observed capability.
5. A write receipt is not read-back verification.
6. Read-back is not acceptance testing.

## Proof contract
- Persistent memory: unique marker write, session boundary/restart, retrieval by key, exact match, retained evidence.
- Background execution: authorized scheduler/agent, job scheduled while user is inactive, timestamped execution log, durable output, independent read-back, stop/revoke verification.
- If host support or permissions are absent, status is UNSUPPORTED/NOT VERIFIED; architecture cannot force a provider to supply a feature.
- The portable package lives in `docs/portable/RAHM/`; package manifest, test outcomes and host-specific capability declaration govern each export.

## No-drop rule
This point does not replace the general Rahm Point 0, CURRENT-044, the main HAIF CURRENT-052 line, or any prior anchor. It creates a new focused branch and keeps unresolved tests open.
