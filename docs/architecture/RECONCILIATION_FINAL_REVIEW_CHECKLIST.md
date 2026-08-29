# Final Review Checklist — Living Reconciliation

Before declaring the system final/proven, review:

- [ ] Production detection covers material productions.
- [ ] Detection safety net catches intentionally unregistered candidates.
- [ ] Stable production/trace identity exists.
- [ ] Durable Pending survives interruption.
- [ ] Every valid opportunity drains Pending automatically.
- [ ] Capability checks precede writes.
- [ ] Writes are idempotent.
- [ ] Read-back verification precedes completion.
- [ ] Conflicts and human approval are explicit.
- [ ] Watchdog reports stale/failed/degraded states.
- [ ] Cross-layer state is independently evidenced.
- [ ] Memory bridge exists and passes E2E, if Memory↔Repository automation is claimed.
- [ ] Acceptance suite has independently reviewable evidence.

**Rule:** unchecked boxes mean the corresponding capability is not PROVEN. Never infer completion from documentation alone.
