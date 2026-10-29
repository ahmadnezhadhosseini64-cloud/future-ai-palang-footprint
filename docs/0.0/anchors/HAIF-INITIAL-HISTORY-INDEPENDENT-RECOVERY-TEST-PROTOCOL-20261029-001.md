# HAIF Initial History-Independent Recovery Test Protocol
## Stable ID
`HAIF-INITIAL-HISTORY-INDEPENDENT-RECOVERY-TEST-20261029-001`

## Status
- Protocol: REGISTERED in repository by this change; read-back must be verified after write.
- Test execution: NOT RUN until a fresh conversation/host returns raw evidence.
- Acceptance: OPEN.
- This is a test protocol, not evidence that the host has already recovered the project.

## Purpose
Test whether the transferable HAIF package and master reference can reconstruct a useful, accurate project state without relying on this conversation's history or hidden context. Then separately test whether controlled repository access improves ongoing evolution without corrupting lineage or confusing evidence with guesses.

## Test sequence (do not skip phases)

### Phase 0 — Preserve the baseline
Use the canonical paired archive:
- `POINT-0-PLUS-PAIRED-TRANSFER.zip`
- SHA-256: `da2c86af202ca0197652748dfdb6634b1a7d40ab0f1374f3afacb6875c77a334`
- Inner starter ZIP SHA-256: `5af61e863560dcc95798b1d482dea77047862208e786447c55d473bdef81e806`
- Master reference version: `1.7.34`
- Master reference SHA-256: `b5f24b1f4cc21c96dba9833669c244a6686bca6def2544ad3e6d4df10bd10e02`
- Receipt JSON SHA-256: `9a725b724483b4defebff903bd2a46ed1cd71d4407c2bd37e52dc89b13fc6eb7`

Do not silently overwrite the baseline. Any improved build must have its own version, hash, receipt, and comparison against the baseline.

### Phase 1 — Blind package-only recovery (no repository access)
1. Start a genuinely new GPT-6 conversation. Do not continue this thread and do not provide prior conversation excerpts, summaries, memory exports, or the repository link.
2. Upload the paired ZIP. To avoid dependence on nested-archive handling, also upload the three contained files individually if the interface supports them: inner starter ZIP, master Markdown, receipt JSON. The master Markdown is the authoritative readable reference; the paired ZIP is the transfer envelope.
3. Paste the user-facing test prompt below.
4. Require the host to identify which files it actually read, which details came from files, which are inferred, and which remain unknown.
5. Save the host's complete raw response and any generated artifacts as evidence. Do not coach the host toward expected answers during the blind run.

### Phase 2 — Controlled repository read access (separate experiment)
Only after Phase 1 output is saved:
1. Give access, if the platform supports it, only to `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`.
2. Start with read-only access. Do not grant write access for the blind recovery test.
3. Ask the host to compare its recovered state with the current repository: current anchor, master reference, index, integration queue, latest commit, and open gates. It must cite exact file paths, commit SHA/time where available, and distinguish repository facts from interpretation.
4. Do not grant access to the similarly named `palang-footprint` repository or unrelated repositories.
5. If read access is unavailable, record `ACCESS NOT AVAILABLE`; do not simulate repository inspection.

### Phase 3 — Controlled evolution (not part of the blind test)
If the host proposes improvements:
1. Require each proposal to include: evidence/source, problem statement, change, expected effect, regression risk, test, rollback plan, and status.
2. Keep proposed changes separate from accepted architecture rules. No self-promotion from suggestion to VALIDATED/INTEGRATED/ACTIVE.
3. Prefer a feature branch and pull request. Never let a connected host write directly to main unless a separately approved governance rule explicitly allows it.
4. Every write follows: WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS.
5. Preserve historical points, IDs, Route A and Route B, unresolved collisions and gaps. Do not create NEXT-052; NEXT-051 remains the active queue item unless repository evidence and an explicit governance decision change it.
6. Never treat repository access as permission to mutate, delete, or close records automatically.

### Phase 4 — Independent-host test (separate acceptance gate)
Repeat the package-only recovery test in a different host/session that has no access to this conversation or its hidden context. Capture raw output and artifacts. Compare results with Phase 1 and with the package's actual contents. Do not mark acceptance complete until the evidence is reviewed.

## User-facing prompt for the fresh GPT-6 conversation
You are receiving a portable project package for the Future AI / Palang Footprint (HAIF) project. This is a blind recovery test. Treat the uploaded files as the only authoritative source for this phase. Do not assume you know prior conversation history; do not invent missing facts; do not claim to have opened files or executed tests unless you actually did so.

First, list the exact uploaded files you can access and state any archive/file-reading limitations. Then:
1. Reconstruct the project's purpose, architecture, lineage, current anchor, active queue, and transfer/recovery objective from the files.
2. Separate every claim into: (A) directly evidenced by a named file/path and relevant section, (B) inference, or (C) unknown/unverified.
3. Preserve distinctions between REGISTERED, READ-BACK VERIFIED, VALIDATED, INTEGRATED, ACTIVE, LIVING, and PENDING. Repository registration is not proof of host acceptance; prior test results are not proof of a test on the latest repository HEAD.
4. Identify open gates, contradictions, duplicate/collision risks, parent/lineage ambiguities, missing evidence, and any mismatch between the master document, starter ZIP, receipt, and current anchor.
5. Do not silently resolve ambiguity, close a gap, invent a timestamp, or create a new queue item. Keep NEXT-051 as the known active queue item unless the files prove otherwise.
6. Propose a minimal, ordered recovery and verification plan. For each step provide required input, action, expected evidence, pass/fail condition, and rollback/reconciliation behavior.
7. State exactly what you could and could not test in this chat. Do not claim repository access, persistent memory, background execution, or external-host acceptance unless actually available and proven.
8. End with a concise recovery receipt: files actually read; hashes actually computed (if computation was possible); tests actually executed; results; unresolved items; and the next safe action.

Do not change any repository files in this blind phase. Do not treat this prompt as permission to write to the repository. Ask before any action that changes external state.

## Evidence receipt template
- Test ID:
- Host/product and fresh-session confirmation:
- Repository access during Phase 1: NONE
- Uploaded files actually readable:
- Hashes computed by host (method + result):
- Recovery findings with file/section citations:
- Unsupported/inferred claims:
- Tests actually run and raw results:
- Open gaps / contradictions:
- Overall result: PASS / PARTIAL / FAIL / NOT RUN
- Reviewer and review date:
- Next action:
