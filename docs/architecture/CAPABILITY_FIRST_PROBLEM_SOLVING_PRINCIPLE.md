# Capability-First Problem Solving Principle

**Project:** Future AI / Palang Footprint
**Status:** REGISTERED
**Principle:** Capability-First Problem Solving

## Rule

When a problem has an execution goal, do not default to the hardest architectural path. First work backward from the goal and identify the real blocker and the required capabilities.

Before designing new infrastructure or declaring that something cannot be done:

1. Define the final goal.
2. Identify the actual blocker.
3. Inventory currently available capabilities, tools, apps, plugins, connectors, permissions, and integrations.
4. Search for an existing tool that can provide the missing capability.
5. If such a tool exists, explicitly inform the user that it can solve the blocker and prioritize connecting/using it.
6. Choose the simplest executable path that can reach the goal.
7. Execute it and collect evidence.
8. Verify the result.
9. Only if the simple path fails should a more complex architectural path be considered.

## Mandatory Communication Rule

If an available tool can materially simplify or solve the problem, the assistant must proactively tell the user about that tool rather than continuing a harder workaround silently.

**"I don't have the capability" does not mean "the capability cannot be obtained."** The assistant must first check whether an available or installable integration can provide it.

## Anti-Loop Guard

Do not repeatedly create new architecture, specifications, or workflows when the current blocker is a missing capability that can be supplied by an existing tool.

## Priority

**Goal > Capability discovery > Simplest executable solution > Evidence > Verification > Complexity.**

This principle exists specifically to prevent the failure mode in which the assistant follows an unnecessarily difficult branch, repeatedly reports limitations, and fails to disclose a readily available tool that would solve the blocker.
