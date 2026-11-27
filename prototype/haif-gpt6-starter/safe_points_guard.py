"""Failure-first guard for two safe points and an owner-only bridge."""
from dataclasses import dataclass
from enum import Enum

class Gate(str, Enum):
    BLOCKED = "BLOCKED"
    OWNER_REVIEW = "OWNER_REVIEW_ONLY"

@dataclass(frozen=True)
class Evidence:
    main_sha: str
    copy1_sha: str
    copy2_base_sha: str
    copy2_head_sha: str
    tests_pass: bool
    paths_authorized: bool
    bridge_matches: bool

def evaluate(e: Evidence, golden_sha: str) -> Gate:
    # No positive proof => block. This module has no write/merge function.
    if not golden_sha or e.main_sha != golden_sha or e.copy1_sha != golden_sha:
        return Gate.BLOCKED
    if e.copy2_base_sha != golden_sha or not e.copy2_head_sha:
        return Gate.BLOCKED
    if not e.tests_pass or not e.paths_authorized or not e.bridge_matches:
        return Gate.BLOCKED
    return Gate.OWNER_REVIEW

def bridge_destination() -> str:
    return "OWNER_REVIEW_ONLY"
