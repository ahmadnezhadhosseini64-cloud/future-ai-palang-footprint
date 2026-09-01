from adapters.governance.valuable_finding_gate import FindingState, assess


def test_unresolved_novel_finding_is_preserved_as_pending():
    result = assess(kind="OPEN_PROBLEM", novel=True, potentially_valuable=True,
                     evidence_verified=False)
    assert result.state is FindingState.PENDING
    assert result.preserve is True


def test_verified_novel_finding_can_be_verified():
    result = assess(kind="NEW_FINDING", novel=True, potentially_valuable=True,
                     evidence_verified=True)
    assert result.state is FindingState.VERIFIED


def test_duplicate_is_not_recreated():
    result = assess(kind="RULE", novel=True, potentially_valuable=True,
                     evidence_verified=True, duplicate=True)
    assert result.state is FindingState.DUPLICATE
    assert result.preserve is False


def test_uncertain_low_value_is_not_promoted():
    result = assess(kind="QUESTION", novel=False, potentially_valuable=False,
                     evidence_verified=False)
    assert result.state is FindingState.NO_VALUE
