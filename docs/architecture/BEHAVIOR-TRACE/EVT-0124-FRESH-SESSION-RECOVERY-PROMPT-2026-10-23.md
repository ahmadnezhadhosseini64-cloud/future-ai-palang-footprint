# Fresh-session recovery handoff prompt — EVT-0124

Use this prompt in a **separate, newly opened ChatGPT conversation**. Do not paste a summary of the current conversation or tell the new session what the expected answers are.

---

You are performing a cold-start recovery test for the Future AI / Palang Footprint / HAIF project.

Canonical repository:
https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

Start here:
`docs/architecture/BEHAVIOR-TRACE/EVT-0124-FRESH-SESSION-RECOVERY-2026-10-23.md`

Independently locate and inspect the canonical master reference, current 0.0 continuation checkpoint, behavior-trace events, IN/OUT anchors, architecture integration queue, relevant workflow run and artifacts, and open project issues. Use repository evidence rather than assuming anything from this prompt.

Before receiving any correction, return:
1. The canonical continuation point and why it is canonical.
2. The latest verified test run, tested commit SHA, test count, and artifact evidence you can independently retrieve.
3. The recovered interaction/event/master/queue/evidence graph and the next action.
4. Which claims are proven by repository tests versus which require a separate ChatGPT session, live-host capture, or an external persistence destination.
5. Every open gap or unresolved issue, preserving its actual status.
6. Any missing links, stale references, conflicting statuses, unsupported claims, or evidence you could not retrieve.
7. The exact source paths and URLs used, plus a concise evidence trail for each material claim.

Rules:
- Do not invent timestamps, run results, artifact contents, commits, issue statuses, or persistence claims.
- UTC is canonical; derive Asia/Tehran from the same UTC instant.
- Preserve historical 0.0 anchors; do not overwrite prior checkpoints.
- Do not divert to Dropbox; it is not part of the current active route unless explicitly reopened.
- Treat WRITE, READ-BACK, validation, integration, and activation as distinct statuses.
- If a source cannot be accessed, say so and mark that check NOT RUN / NOT VERIFIED.
- Do not claim host-wide automatic capture or external persistence merely because repository CI passed.
- Capture your first answer before any corrective prompting. This first answer is the test subject.

End with a proposed recovery status (PASS / PARTIAL / BLOCKED) and the evidence supporting it. Do not modify repository files during the initial recovery response.
