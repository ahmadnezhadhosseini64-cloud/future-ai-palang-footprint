# IN-104 — دستور ادامه و تحویل امن POINT-0/064

- Stable ID: HAIF-IN-104-DEPARTURE-CONTINUITY-2026-11-07-001
- Parent root: POINT-0/064 (0+)
- Prior checkpoint: CURRENT-115
- Sole queue: NEXT-051
- Status: REGISTERED / READ-BACK VERIFIED / APPEND-ONLY
- User-message timestamp: UNKNOWN / UNVERIFIED
- Source: direct user instruction in the current conversation.

## Preserved user instruction

The user is leaving and explicitly asks that the current point, all historical point connections, remaining work, anchoring, documentation and living reference state be preserved. All subsequent project steps are to continue under 0.0, with the tests and reference documents kept active and living.

## Required interpretation

1. Keep POINT-0/064 as the current root; this instruction does not create a competing root or a new NEXT queue.
2. Preserve the chain POINT-0/064 → IN-103 + OUT-102 → EVT-0256 → TIME-BINDING-EVT-0256 → CURRENT-115 → NEXT-051, and attach this handoff as an additive child event.
3. Preserve POINT-0/063, POINT-0/062, POINT-0/061 and all older roots, events, checkpoints, lessons, contracts and unresolved branches.
4. Continue every remaining step in 0.0 through the sole existing NEXT-051 queue. Do not create NEXT-052.
5. Keep the living mother, 0.0 registry, Reference Index, Behavior Trace index, Integration Queue and recovery/package manifests synchronized and read-back verified.
6. Keep applicable structural, regression, behavioral, scheduled-run, restart, clean-host and independent-host tests active as recurring acceptance gates. Re-run relevant tests on the exact final commit SHA after changes; preserve individual receipts.
7. A test may be marked PASS only with an inspectable run receipt, exact tested SHA and scope. Tests not run remain OPEN / NOT RUN; failed or incomplete tests remain visible.
8. Maintain UTC as permanent time base; derive Asia/Tehran only from exact source timestamps. User-message time remains UNKNOWN / UNVERIFIED unless directly supplied.
9. Do not claim persistent memory, background execution, live host capture, external destination sync or scheduled delivery without direct evidence.
10. Continue WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS and keep the original portable ZIP identity stable; update its contents in place rather than creating competing package identities.
