"""Mandatory Valuable Finding Recognition gate."""
from dataclasses import dataclass
from enum import Enum

class FindingState(str, Enum):
    CANDIDATE = "CANDIDATE"
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    DUPLICATE = "DUPLICATE"
    NO_VALUE = "NO-VALUE"

@dataclass(frozen=True)
class FindingAssessment:
    kind: str
    state: FindingState
    novel: bool
    potentially_valuable: bool
    preserve: bool

def assess(*, kind: str, novel: bool, potentially_valuable: bool,
           evidence_verified: bool, duplicate: bool = False) -> FindingAssessment:
    if duplicate:
        return FindingAssessment(kind, FindingState.DUPLICATE, novel, potentially_valuable, False)
    if evidence_verified and novel and potentially_valuable:
        return FindingAssessment(kind, FindingState.VERIFIED, True, True, True)
    if novel or potentially_valuable:
        return FindingAssessment(kind, FindingState.PENDING, novel, potentially_valuable, True)
    return FindingAssessment(kind, FindingState.NO_VALUE, novel, potentially_valuable, False)
