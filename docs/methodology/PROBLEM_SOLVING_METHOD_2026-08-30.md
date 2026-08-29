# Problem-Solving Method — Reverse Engineering to the Goal

**Project:** Future AI / Palang Footprint  
**Date:** 2026-08-30  
**Status:** APPROVED METHOD

## Failure identified
The prior approach over-optimized for architectural completeness before exhausting available execution capabilities. This created unnecessary branches and delayed the real objective.

## Correct method
Start from the required end state and work backward:

1. Define the exact final outcome.
2. Identify the actual blocking capability, not a hypothetical architectural gap.
3. Inventory all currently available tools, permissions, connectors, and execution paths.
4. Try the simplest viable path first.
5. If it fails, inspect the concrete failure and try the next viable path.
6. Only create new architecture when an actual capability gap—not an untested path—requires it.
7. Every execution claim requires operation-specific evidence.
8. Close only after acceptance criteria pass; otherwise retain the explicit unresolved state.

## Anti-loop rule
Do not generate a new architecture branch merely because an execution path has not yet been attempted. Do not repeatedly return to design while a viable capability path remains untested.

## Goal-oriented priority
**Goal → Blocker → Capability inventory → Simplest executable path → Execute → Evidence → Verify → Repair → Re-test → Close.**

## Learning requirement
This method is a reusable project operating rule. Future execution tasks should first apply this reverse-engineering/capability-first method and explicitly check for an easier available route before declaring a limitation.
