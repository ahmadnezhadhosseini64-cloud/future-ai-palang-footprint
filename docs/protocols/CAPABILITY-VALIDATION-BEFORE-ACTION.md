# Capability Validation Before Action

Production ID: CVBA-2026-08-31-001
Project: Future AI / Palang Footprint
Status: ACTIVE / PERMANENT
Reference: 0.0

## Principle
A requested action is not considered executable merely because the capability normally exists. Before promising or beginning an action that depends on a tool, connector, runtime, quota, permission, or external interface, validate actual availability in the current execution context.

## Mandatory sequence
1. Identify the capability required for the requested action.
2. Validate actual availability now.
3. If unavailable, report the limitation before claiming execution capability.
4. If available, perform the action.
5. Verify the result using the strongest available evidence.
6. Never convert expected availability, UI timing, or prior availability into a claim of current availability.

## Image-generation rule
For image creation/editing, do not state that image generation is currently available until the image-generation capability has been successfully validated in the current context. If execution is rate-limited or otherwise unavailable, state that clearly and do not fabricate a successful result.

## Registration rule
The word "ثبت" is not a simple write operation. When a user asks to register something as an official project record, treat it as a traceable registration workflow: identify the correct Production ID, determine the canonical destination, preserve provenance, write/update, read back, verify, reconcile cross-layer state where applicable, and report any unresolved gate explicitly.

## No false completion
Architecture, intent, or a successful write response alone does not prove end-to-end completion when a read-back or downstream verification gate is required.

## Recovery
If any gate fails, preserve the same Production ID and continuation path in the durable Repository/Recovery store. Resume from the first unresolved gate when access returns. Do not duplicate records.

## Invariant
NO CAPABILITY CLAIM WITHOUT CURRENT VALIDATION.
NO REGISTRATION COMPLETE WITHOUT APPLICABLE VERIFICATION.
