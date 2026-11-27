"""Fail-closed, repository-backed gate. Caller-supplied PASS booleans are never accepted."""
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import re
import subprocess

class Gate(str, Enum):
    BLOCKED = "BLOCKED"
    OWNER_REVIEW = "OWNER_REVIEW_ONLY"

FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
DEFAULT_ALLOWED_PATHS = frozenset({
    "README.md",
    "docs/architecture/SAFE-COPY/COPY2-OWNER-COMMAND-CONTROL-PLANE.md",
    ".github/workflows/palang-safe-copy2-validation.yml",
    "prototype/haif-gpt6-starter/safe_copy_audit.py",
    "prototype/haif-gpt6-starter/test_safe_copy_audit.py",
    "prototype/haif-gpt6-starter/safe_points_guard.py",
    "prototype/haif-gpt6-starter/test_safe_points_guard.py",
})

@dataclass(frozen=True)
class Evidence:
    repo_root: Path
    main_ref: str
    copy1_ref: str
    copy2_base_sha: str
    copy2_head_sha: str
    allowed_paths: frozenset[str] = DEFAULT_ALLOWED_PATHS

def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if result.returncode:
        raise ValueError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()

def _commit(root: Path, ref: str) -> str:
    value = _git(root, "rev-parse", "--verify", f"{ref}^{{commit}}")
    if not FULL_SHA.fullmatch(value):
        raise ValueError(f"ref did not resolve to a full commit SHA: {ref}")
    return value

def evaluate(e: Evidence, golden_sha: str) -> Gate:
    """Return OWNER_REVIEW_ONLY only from live Git object/ref evidence."""
    try:
        if not FULL_SHA.fullmatch(golden_sha or ""):
            return Gate.BLOCKED
        if not FULL_SHA.fullmatch(e.copy2_base_sha or "") or not FULL_SHA.fullmatch(e.copy2_head_sha or ""):
            return Gate.BLOCKED
        root = Path(e.repo_root).resolve()
        if _git(root, "rev-parse", "--is-inside-work-tree") != "true":
            return Gate.BLOCKED
        main_sha = _commit(root, e.main_ref)
        copy1_sha = _commit(root, e.copy1_ref)
        head_sha = _commit(root, e.copy2_head_sha)
        base_sha = _commit(root, e.copy2_base_sha)
        if main_sha != golden_sha or copy1_sha != golden_sha or base_sha != golden_sha:
            return Gate.BLOCKED
        if _git(root, "merge-base", golden_sha, head_sha) != golden_sha:
            return Gate.BLOCKED
        changed_raw = _git(root, "diff", "--name-only", f"{golden_sha}...{head_sha}")
        changed = frozenset(line for line in changed_raw.splitlines() if line)
        if not changed or not changed.issubset(e.allowed_paths):
            return Gate.BLOCKED
        # This gate never merges, pushes, creates a PR, or writes to either reference.
        return Gate.OWNER_REVIEW
    except (OSError, ValueError, subprocess.SubprocessError):
        return Gate.BLOCKED

def bridge_destination() -> str:
    return "OWNER_REVIEW_ONLY"
