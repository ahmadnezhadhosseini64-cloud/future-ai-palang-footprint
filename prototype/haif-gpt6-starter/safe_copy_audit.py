"""Structural audit for the Copy 2 candidate workflow and portable package."""
from pathlib import Path
import json
import re


REQUIRED_PACKAGE = (
    "README.md", "manifest.json", "engine.py", "state.schema.json",
    "LIVING_MASTER_REFERENCE.md", "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md",
    "UNIVERSAL_AI_HOST_ENTRY_FA.md", "ONE_MESSAGE_HOST_BOOTSTRAP_FA.md", "safe_points_guard.py",
)
ACTION_LINE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
FULL_COMMIT = re.compile(r"^[0-9a-f]{40}$")
COPY1_BRANCH = "palang-safe-copy-1-baseline-20261126"
COPY2_BRANCH = "palang-safe-copy-2-current-20261127"


def audit_workflow(text: str) -> list[str]:
    failures = []
    lines = text.splitlines()
    if "permissions:" not in lines or "  contents: read" not in lines:
        failures.append("workflow permissions must be contents: read only")
    if any(re.search(r"\b\w+:\s*write\s*(?:#.*)?$", line) for line in lines):
        failures.append("write permission found")
    if "persist-credentials: false" not in text:
        failures.append("checkout credentials must not persist")
    expected_checkout = "ref: " + "$" + "{{ github.event.pull_request.head.sha || github.sha }}"
    if expected_checkout not in text:
        failures.append("checkout is not bound to the exact event head SHA")
    if COPY1_BRANCH not in text or COPY2_BRANCH not in text:
        failures.append("current Copy 1 / Copy 2 branch mapping is missing")
    if "refs/heads/main" not in text or "refs/heads/$copy1_branch" not in text:
        failures.append("workflow does not read both live MAIN and Copy 1 refs")
    if "merge-base --is-ancestor \"$copy1_sha\" \"$head_sha\"" not in text:
        failures.append("candidate is not required to descend from the current Copy 1 SHA")
    if 'test "$main_sha" = "$copy1_sha"' in text:
        failures.append("MAIN and Copy 1 are incorrectly forced to share one SHA")
    if '"diff"' not in text or '"--name-only"' not in text or "unexpected" not in text:
        failures.append("live changed-path allowlist is missing")
    if any(token in text for token in ("git push ", "gh pr merge", "gh api")):
        failures.append("workflow contains a write or promotion command")
    for match in ACTION_LINE.finditer(text):
        action = match.group(1).rstrip(",")
        if "@" not in action or not FULL_COMMIT.fullmatch(action.rsplit("@", 1)[1]):
            failures.append(f"action must be pinned to a full 40-character commit SHA: {action}")
    return failures


def audit_copy3_workflow(text: str) -> list[str]:
    failures = []
    lines = text.splitlines()
    if not any(line.strip() == "pull_request:" for line in lines):
        failures.append("Copy 3 intake must use the safe pull_request event")
    if "pull_request_target:" in text:
        failures.append("unsafe pull_request_target event is forbidden")
    if "  contents: read" not in lines or any(
        re.search(r"\b\w+:\s*write\s*(?:#.*)?$", line) for line in lines
    ):
        failures.append("Copy 3 intake permissions must be read-only")
    if "persist-credentials: false" not in text:
        failures.append("Copy 3 checkout credentials must not persist")
    expected_checkout = "ref: " + "$" + "{{ github.event.pull_request.head.sha }}"
    if expected_checkout not in text:
        failures.append("Copy 3 checkout must bind to the exact PR head SHA")
    if COPY2_BRANCH not in text or "palang-copy3-" not in text:
        failures.append("Copy 3 branch prefix or Copy 2 target is missing")
    if "github.event.pull_request.head.repo.full_name != github.repository" not in text:
        failures.append("Copy 3 PR must originate from an independent fork")
    if 'git show "$LIVE_COPY2_SHA:prototype/haif-gpt6-starter/copy3_intake_guard.py"' not in text:
        failures.append("intake must execute the trusted guard from the Copy 2 base, not PR head")
    if 'python "$RUNNER_TEMP/copy3_intake_guard.py"' not in text:
        failures.append("trusted Copy 3 intake guard is not executed")
    if 'merge-base --is-ancestor "$live_copy2_sha" "$EVENT_HEAD_SHA"' not in text:
        failures.append("Copy 3 proposal must descend from the exact live Copy 2 SHA")
    if any(token in text for token in ("git push ", "gh pr merge", "gh api")):
        failures.append("Copy 3 intake contains a write or promotion command")
    for match in ACTION_LINE.finditer(text):
        action = match.group(1).rstrip(",")
        if "@" not in action or not FULL_COMMIT.fullmatch(action.rsplit("@", 1)[1]):
            failures.append(f"Copy 3 action must be pinned to a full commit SHA: {action}")
    return failures

def audit_recovery_package(root: Path) -> list[str]:
    failures = []
    for name in REQUIRED_PACKAGE:
        if not (root / name).is_file():
            failures.append(f"missing required recovery file: {name}")
    manifest = root / "manifest.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            for key in ("stable_id", "production_id", "current_living_master_version"):
                if not isinstance(data.get(key), str) or not data[key].strip():
                    failures.append(f"manifest missing valid {key}")
        except Exception as exc:
            failures.append(f"manifest invalid: {exc}")
    return failures


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", type=Path)
    parser.add_argument("--copy3-workflow", type=Path)
    parser.add_argument("--package", type=Path)
    args = parser.parse_args()
    failures = []
    if args.workflow:
        failures.extend(audit_workflow(args.workflow.read_text(encoding="utf-8")))
    if args.copy3_workflow:
        failures.extend(audit_copy3_workflow(args.copy3_workflow.read_text(encoding="utf-8")))
    if args.package:
        failures.extend(audit_recovery_package(args.package))
    if failures:
        print("AUDIT=FAIL")
        for issue in failures:
            print(" -", issue)
        return 1
    print("AUDIT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
