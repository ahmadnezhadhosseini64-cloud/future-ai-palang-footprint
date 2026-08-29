# Final Closure Recording Rule

**Project:** Future AI / Palang Footprint
**Status:** REGISTERED

## Rule
A checkpoint is not a final closure. When a task is actually complete, the assistant must create a distinct final-closure record rather than treating the latest checkpoint as completion.

## Mandatory Final-Closure Fields
- Unique closure ID
- Date and exact time with timezone
- Project and scope
- Final status
- Commit / execution identifier
- Evidence reference(s)
- Verification result
- Outstanding blockers, if any
- Explicit closure state: `PROVEN / CLOSED / PASS` only when evidence supports it

## Anti-False-Closure Guard
Never say or imply that work is finished merely because a checkpoint, architecture, specification, permission change, or simulated test exists.

A checkpoint means **resume from here**. A final-closure record means **the acceptance criteria have actually passed and the work is closed**.

If any required final evidence is missing, the status must remain `NOT_PROVEN` and the missing evidence must be named explicitly.

## Communication Rule
When the user authorizes work through completion, continue toward the actual completion gate. Do not stop at a checkpoint and label it as the endpoint.

## Priority
`EXECUTE → EVIDENCE → VERIFY → FINAL-CLOSURE RECORD → CLOSED`
