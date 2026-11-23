# HAIF host enrollment challenge, workspace boundary and paired-interaction bridge

- Stable ID: HAIF-HOST-ENROLLMENT-CHALLENGE-AND-PAIR-BRIDGE-2026-11-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / CANDIDATE-ON-OWNER-REVIEW-BRANCH
- Root: POINT-0/GOLDEN
- Parent: CURRENT-150.04 / NEXT-051.04
- Owner: @ahmadnezhadhosseini64-cloud

## 1. Goal

Make a new AI host's first entry low-friction: one message should be enough to begin public repository recovery and return a structured enrollment receipt. It must not grant the host master write access, private RAHM access, or another host's workspace.

## 2. No membership required for public READ

The canonical repository is Public. Anonymous HTTPS read/clone/fetch is the default first step. A host does not need to become a GitHub collaborator, receive a PAT, or complete OAuth merely to read the public repository. OAuth is reserved for an explicitly required authenticated operation or a private resource.

## 3. Three distinct identity levels

1. HOST-CLAIM-ID: a host-generated ephemeral label for this one enrollment attempt. It helps correlate the receipt but is not a trusted identity and cannot be used to issue a permanent Host ID.
2. OWNER-CHALLENGE: a one-time, owner-generated random nonce with an expiry and intended host/session scope. The host returns it unchanged in the receipt. This is a replay-detection/correlation aid, not proof of provider identity by itself.
3. HAIF-HOST-YYYYMMDD-NNN: official owner-issued Host ID, created only after owner review of the returned receipt and direct evidence. Never self-assign or infer the next number.

If the host runtime supports local key generation and signing, it may additionally return an ephemeral public key and a signature over the owner challenge. The owner verifies the signature independently. Private keys never leave the host. If signing is unavailable, the host remains CLAIMED / IDENTITY-UNVERIFIED until a stronger provider-authenticated signal is available.

## 4. Required first-entry receipt

The host returns a compact JSON or Markdown receipt containing:
- owner challenge (exactly as supplied);
- host claim ID (self-generated, clearly marked untrusted);
- model/provider/runtime name and version only if actually observable;
- repository URL, branch, exact main HEAD SHA and retrieval method;
- blob SHA of Reference Index, living mother, universal entry and current NEXT/CURRENT references;
- capability matrix: public READ, Git/clone, code execution, isolated workspace, durable storage, restart recovery, GitHub connector, remote MCP support;
- evidence for each claimed capability, or NOT AVAILABLE / NOT TESTED;
- workspace test: create/read/delete a temporary file only inside the host's own workspace; no repository write;
- explicit declaration: no access to MASTER write, RAHM, owner secrets or other hosts;
- next action requested from owner, if any.

A returned string, model name, or self-declared identifier is not proof of a unique model instance. The owner verifies source SHA and receipt independently before registration.

## 5. Workspace and permissions

- Public MASTER: anonymous or authenticated READ only for all hosts.
- Owner control plane: owner-only; credentials never enter model context.
- RAHM: private, owner-only, outside every host workspace.
- Host workspace: isolated to one host; no cross-host visibility.
- Private host repository, if required: created by the owner and scoped to exactly one host. Never add an AI host as a collaborator on the public MASTER.
- Optional write-back: only through a server-side broker/GitHub App restricted to that host's private repository, with narrow tools, per-operation approval, audit and read-back. The model never receives raw tokens.
- No broker or private repository is required for initial public READ and receipt generation.

## 6. Minimal one-message flow

PUBLIC READ → EXACT-SHA RECOVERY → OWNER CHALLENGE RECEIPT → OWNER REVIEW → OFFICIAL HOST ID → ISOLATED WORKSPACE

The first message should not ask the owner to create a repository before public READ succeeds. It must first determine which capabilities the host already has. Only then may it request one precise owner-side action if a missing capability is essential.

## 7. Paired input/output bridge

Every project interaction uses a single pair:
IN-N → BRIDGE-N → OUT-N → EVT-N → TIME-BINDING-N → CURRENT-family.revision → NEXT-family.revision.

The Bridge links IN and OUT in both directions and references the single POINT-0/GOLDEN root, the prior checkpoint, and the next checkpoint/queue. It records exact commit evidence and read-back. It is a version-controlled record, not an extra runtime service. No parallel root or queue is allowed.

## 8. Acceptance

- Anonymous public read and exact main SHA independently verified.
- Receipt fields present and no secret material.
- Host claim clearly distinguished from owner-issued official ID.
- Workspace isolation proven by host-side tests; otherwise not verified.
- No host write path to MASTER or RAHM.
- IN/OUT/Bridge/Event/Time/Current/Next graph edges all resolve.
- Fresh host recovery and restart are separately tested; a prompt alone never closes those gates.
