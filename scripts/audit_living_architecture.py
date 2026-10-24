#!/usr/bin/env python3
"""Structural audit for canonical living-architecture records.
This checks repository structure only; it does not prove external persistence.
"""
from pathlib import Path
import sys

ROOT = Path(".")
required = {
    "reference index": "docs/REFERENCE_INDEX.md",
    "master reference contract": "docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md",
    "current 0.0 anchor": "checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md",
    "architecture queue": "docs/architecture/INTEGRATION-QUEUE/README.md",
    "open gaps register": "docs/architecture/INTEGRATION-QUEUE/OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001.md",
    "behavior trace index": "docs/architecture/BEHAVIOR-TRACE/README.md",
    "excavation contract": "docs/architecture/INTEGRATION-QUEUE/EXCAVATION-ROUTINE-EXECUTION-CONTRACT-2026-10-20-001.md",
    "comprehensive excavation reference": "docs/reference/REFERENCE-DOCUMENTS/COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001.md",
    "living automation contract": "docs/reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md",
    "architecture verification event": "docs/architecture/BEHAVIOR-TRACE/EVT-0024-ARCHITECTURE-BUILD-VERIFICATION-2026-10-20.md",
    "behavior trace log": "docs/architecture/BEHAVIOR-TRACE/INTERACTION-BEHAVIOR-TRACE-2026-10-19-001.md",
    "0.0 registry": "docs/0.0/README.md",
    "architecture lesson registry": "docs/architecture/ARCHITECTURE-LESSONS/README.md",
    "current architecture lesson": "docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md",
    "lesson lifecycle event": "docs/architecture/BEHAVIOR-TRACE/EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23.md",
}
errors = []
for label, rel in required.items():
    if not (ROOT / rel).is_file():
        errors.append(f"MISSING_REQUIRED_FILE label={label!r} path={rel}")

expected_ids = (
    "COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001",
    "LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001",
)
for rel, label in (
    ("docs/REFERENCE_INDEX.md", "REFERENCE_INDEX"),
    ("docs/architecture/INTEGRATION-QUEUE/README.md", "ARCHITECTURE_QUEUE"),
):
    path = ROOT / rel
    if path.is_file():
        content = path.read_text(encoding="utf-8")
        for stable_id in expected_ids:
            if stable_id not in content:
                errors.append(f"{label}_MISSING_ID id={stable_id}")

integration_id = "ARCHITECTURE-BUILD-VERIFICATION-2026-10-20-001"
integration_surfaces = (
    ("docs/REFERENCE_INDEX.md", "REFERENCE_INDEX"),
    ("docs/architecture/INTEGRATION-QUEUE/README.md", "ARCHITECTURE_QUEUE"),
    ("docs/architecture/BEHAVIOR-TRACE/README.md", "BEHAVIOR_TRACE_INDEX"),
    ("docs/architecture/BEHAVIOR-TRACE/INTERACTION-BEHAVIOR-TRACE-2026-10-19-001.md", "BEHAVIOR_TRACE_LOG"),
    ("docs/0.0/README.md", "ZERO_ZERO_REGISTRY"),
    ("checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md", "CURRENT_ZERO_ZERO_ANCHOR"),
    ("docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md", "MASTER_REFERENCE_VAULT"),
    ("docs/reference/REFERENCE-DOCUMENTS/COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001.md", "EXCAVATION_REFERENCE"),
    ("docs/architecture/BEHAVIOR-TRACE/EVT-0024-ARCHITECTURE-BUILD-VERIFICATION-2026-10-20.md", "ARCHITECTURE_VERIFICATION_EVENT"),
    ("recovery/PENDING_REGISTRATION_QUEUE.md", "PENDING_REGISTRATION_QUEUE"),
    ("docs/architecture/INTEGRATION-QUEUE/OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001.md", "OPEN_GAPS_REGISTER"),
)
for rel, label in integration_surfaces:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"{label}_MISSING_FILE path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    if integration_id not in content:
        errors.append(f"{label}_MISSING_ID id={integration_id}")


lesson_id = "LAL-20261023-001"
lesson_surfaces = (
    ("docs/architecture/ARCHITECTURE-LESSONS/README.md", "LESSON_REGISTRY"),
    ("docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md", "LESSON_RECORD"),
    ("docs/architecture/BEHAVIOR-TRACE/EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23.md", "LESSON_EVENT"),
    ("docs/REFERENCE_INDEX.md", "REFERENCE_INDEX"),
    ("docs/architecture/BEHAVIOR-TRACE/README.md", "BEHAVIOR_TRACE_INDEX"),
    ("docs/architecture/INTEGRATION-QUEUE/README.md", "ARCHITECTURE_QUEUE"),
    ("docs/0.0/README.md", "ZERO_ZERO_REGISTRY"),
    ("docs/architecture/LIVE-INBOX/README.md", "LIVE_INBOX"),
    ("docs/reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md", "LIVING_MASTER"),
)
for rel, label in lesson_surfaces:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"{label}_MISSING_FILE path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    if lesson_id not in content:
        errors.append(f"{label}_MISSING_LESSON_ID id={lesson_id}")


# Universal living component governance integration gate.
# This verifies repository structure/links only; it does not prove host-wide capture.
ulcg_required = {
    "universal living component governance master": "docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md",
    "universal governance event": "docs/architecture/BEHAVIOR-TRACE/EVT-0110-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-2026-10-23.md",
    "universal governance lesson": "docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-008-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md",
    "source rule component test map": "docs/architecture/ARCHITECTURE-LESSONS/SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md",
    "historic lesson migration ledger": "docs/architecture/ARCHITECTURE-LESSONS/HISTORIC-LESSON-MIGRATION-LEDGER-2026-10-23-001.md",
    "current IN-021 anchor": "docs/0.0/anchors/PALANG-0.0-IN-20261023-021-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md",
    "current OUT-021 anchor": "docs/0.0/anchors/PALANG-0.0-OUT-20261023-021-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md",
    "next 0.0 source excavation anchor": "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-022-HISTORIC-SOURCE-GRAPH-EXCAVATION.md",
    "verification checkpoint": "docs/architecture/BEHAVIOR-TRACE/VERIFICATION-CHECKPOINT-INT-20261023-021.md",
    "time binding": "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261023-021.md",
    "current live inbox item": "docs/architecture/LIVE-INBOX/entries/INBOX-20261023-007.md",
    "bounded rollback test event": "docs/architecture/BEHAVIOR-TRACE/EVT-0109-CONTROLLED-GIT-ROLLBACK-RECOVERY-TEST-2026-10-23.md",
    "rollback lineage lesson": "docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-007-ROLLBACK-AS-NEW-LINEAGE-EVENT.md",
}
for label, rel in ulcg_required.items():
    if not (ROOT / rel).is_file():
        errors.append(f"ULCG_MISSING_REQUIRED_FILE label={label!r} path={rel}")

ulcg_surfaces = (
    ("docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md", "ULCG_MASTER"),
    ("docs/REFERENCE_INDEX.md", "REFERENCE_INDEX"),
    ("docs/architecture/BEHAVIOR-TRACE/README.md", "BEHAVIOR_TRACE_INDEX"),
    ("docs/architecture/ARCHITECTURE-LESSONS/README.md", "LESSON_REGISTRY"),
    ("docs/architecture/ARCHITECTURE-LESSONS/HISTORIC-LESSON-MIGRATION-LEDGER-2026-10-23-001.md", "HISTORIC_LESSON_LEDGER"),
    ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md", "SOURCE_RULE_MAP"),
    ("docs/architecture/INTEGRATION-QUEUE/README.md", "ARCHITECTURE_QUEUE"),
    ("docs/0.0/README.md", "ZERO_ZERO_REGISTRY"),
    ("docs/architecture/LIVE-INBOX/README.md", "LIVE_INBOX"),
    ("docs/reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md", "CONTINUATION_MASTER"),
)
required_link_ids = {
    "ULCG_MASTER": ("PALANG-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-2026-10-23-001", "SRCMAP-2026-10-23-001", "EVT-0110", "EVT-0109", "LAL-20261023-007"),
    "SOURCE_RULE_MAP": ("SRCMAP-2026-10-23-001", "EVT-0109", "LAL-20261023-007"),
    "REFERENCE_INDEX": ("UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001", "SRCMAP-2026-10-23-001", "EVT-0110", "LAL-20261023-008"),
    "BEHAVIOR_TRACE_INDEX": ("EVT-0110", "LAL-20261023-008"),
    "LESSON_REGISTRY": ("SRCMAP-2026-10-23-001", "LAL-20261023-008", "LAL-20261023-007"),
    "HISTORIC_LESSON_LEDGER": ("SRCMAP-2026-10-23-001", "Issue #21"),
    "ARCHITECTURE_QUEUE": ("SRCMAP-2026-10-23-001", "NEXT-0.0-20261023-022", "Issue #20", "Issue #21", "EVT-0109", "LAL-20261023-007"),
    "ZERO_ZERO_REGISTRY": ("IN-021", "OUT-021", "NEXT-0.0-20261023-022", "EVT-0110"),
    "LIVE_INBOX": ("INBOX-20261023-007", "NEXT-0.0-20261023-022"),
    "CONTINUATION_MASTER": ("EVT-0110", "LAL-20261023-008", "NEXT-0.0-20261023-022"),
}
for rel, label in ulcg_surfaces:
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"ULCG_SURFACE_MISSING_FILE label={label} path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    for required_id in required_link_ids[label]:
        if required_id not in content:
            errors.append(f"ULCG_SURFACE_MISSING_ID surface={label} id={required_id}")


# Current point 0 / next 0.0 continuity gate.
# This is structural policy verification, not runtime-wide capture or cold-start proof.
continuity_required = {
    "legacy current pointer reconciled": "checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md",
    "current point 0": "docs/0.0/anchors/PALANG-0.0-CURRENT-20261023-023-USER-CHECKPOINT-AND-CONTINUATION.md",
    "next 0.0 checkpoint": "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md",
    "current input anchor": "docs/0.0/anchors/PALANG-0.0-IN-20261023-023-REGISTER-CURRENT-POINT-0.md",
    "current output anchor": "docs/0.0/anchors/PALANG-0.0-OUT-20261023-023-REGISTER-CURRENT-POINT-0.md",
    "current point event": "docs/architecture/BEHAVIOR-TRACE/EVT-0112-CURRENT-POINT-0-AND-NEXT-0.0-2026-10-23.md",
    "current point lesson": "docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-010-CURRENT-POINT-AND-NEXT-CHECKPOINT.md",
    "current point time binding": "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261023-023.md",
}
for label, rel in continuity_required.items():
    if not (ROOT / rel).is_file():
        errors.append(f"CONTINUITY_MISSING_REQUIRED_FILE label={label!r} path={rel}")

continuity_surfaces = {
    "LEGACY_CURRENT_POINTER": ("checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md", ("CURRENT-023", "NEXT-024", "HISTORICAL / PRESERVED")),
    "ULCG_MASTER": ("docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md", ("Version: 1.2.5", "CURRENT-023", "NEXT-024", "EVT-0112", "LAL-20261023-010")),
    "REFERENCE_INDEX": ("docs/REFERENCE_INDEX.md", ("CURRENT-023", "NEXT-024", "TIME-BINDING-INT-20261023-023")),
    "ZERO_ZERO_REGISTRY": ("docs/0.0/README.md", ("CURRENT-023", "NEXT-024", "IN-023", "OUT-023", "EVT-0112")),
    "SOURCE_RULE_MAP": ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md", ("CURRENT-023", "NEXT-024", "EVT-0112", "LAL-20261023-010")),
    "ARCHITECTURE_QUEUE": ("docs/architecture/INTEGRATION-QUEUE/README.md", ("CURRENT-023", "NEXT-024", "Issue #20", "Issue #21")),
    "LESSON_REGISTRY": ("docs/architecture/ARCHITECTURE-LESSONS/README.md", ("LAL-20261023-010", "EVT-0112", "NEXT-024")),
    "BEHAVIOR_TRACE_INDEX": ("docs/architecture/BEHAVIOR-TRACE/README.md", ("EVT-0112", "LAL-20261023-010", "CURRENT-023", "NEXT-024")),
    "INITIAL_MODEL_MASTER": ("docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md", ("CURRENT-023", "NEXT-024", "EVT-0112", "LAL-20261023-010")),
}
for label, (rel, required_ids) in continuity_surfaces.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"CONTINUITY_SURFACE_MISSING_FILE surface={label} path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    for required_id in required_ids:
        if required_id not in content:
            errors.append(f"CONTINUITY_SURFACE_MISSING_ID surface={label} id={required_id}")

# Interaction visibility and clause-level source crosswalk gate.
# Structural presence/links are not runtime capture or cold-start proof.
interaction_required = {
    "current user input IN-024": "docs/0.0/anchors/PALANG-0.0-IN-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md",
    "current assistant output OUT-024": "docs/0.0/anchors/PALANG-0.0-OUT-20261023-024-EXECUTION-VISIBILITY-AND-CONTINUATION.md",
    "visibility event EVT-0113": "docs/architecture/BEHAVIOR-TRACE/EVT-0113-VISIBLE-CONTINUATION-AND-SOURCE-CLAUSE-EXCAVATION-2026-10-23.md",
    "visibility lesson LAL-011": "docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-011-VISIBLE-CONTINUATION-AND-RESUMABLE-WORK.md",
    "successor checkpoint NEXT-025": "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-025-SOURCE-RULE-TEST-CROSSWALK-AND-COLD-START.md",
    "source clause crosswalk batch 2": "docs/architecture/ARCHITECTURE-LESSONS/SOURCE-CLAUSE-CROSSWALK-BATCH-2-2026-10-23-001.md",
    "current user input IN-025": "docs/0.0/anchors/PALANG-0.0-IN-20261023-025-STATUS-AND-VISIBLE-CONTINUATION.md",
    "current assistant output OUT-025": "docs/0.0/anchors/PALANG-0.0-OUT-20261023-025-STATUS-AND-VISIBLE-CONTINUATION.md",
    "status transparency event EVT-0114": "docs/architecture/BEHAVIOR-TRACE/EVT-0114-STATUS-TRANSPARENCY-AND-RESUMABLE-EXECUTION-2026-10-23.md",
    "status transparency lesson LAL-012": "docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261023-012-STATUS-TRANSPARENCY-AND-RESUMABLE-EXECUTION.md",
    "time binding INT-025": "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261023-025.md",
}
for label, rel in interaction_required.items():
    if not (ROOT / rel).is_file():
        errors.append(f"INTERACTION_MISSING_REQUIRED_FILE label={label!r} path={rel}")

interaction_surfaces = {
    "ULCG_MASTER": ("docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md", ("Version: 1.2.5", "IN-024", "OUT-024", "EVT-0113", "LAL-20261023-011", "SCRTC-B2", "NEXT-025", "IN-025", "OUT-025", "EVT-0114", "LAL-20261023-012", "TIME-BINDING-INT-20261023-025")),
    "REFERENCE_INDEX": ("docs/REFERENCE_INDEX.md", ("IN-024", "OUT-024", "EVT-0113", "LAL-20261023-011", "NEXT-025", "IN-025", "OUT-025", "EVT-0114", "LAL-20261023-012", "SOURCE-CLAUSE-CROSSWALK-BATCH-2-2026-10-23-001.md", "IN-025", "OUT-025", "EVT-0114", "LAL-20261023-012")),
    "ZERO_ZERO_REGISTRY": ("docs/0.0/README.md", ("IN-024", "OUT-024", "EVT-0113", "LAL-20261023-011", "NEXT-025")),
    "SOURCE_RULE_MAP": ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md", ("Version: 1.1.0", "SCRTC-B2", "PIATGCG", "UIALAC", "ICMCRR", "H0GLMR", "STAR-HCR")),
    "SOURCE_CLAUSE_MATRIX": ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-CLAUSE-CROSSWALK-BATCH-2-2026-10-23-001.md", ("SCRTC-B2-2026-10-23-001", "2212b390634a8a9530a3dce15fabd53762e478cd", "12a37ffb1ba86080abfb39462468ac7c99f8125d", "438c7c75577800da0b7eb33ca88dc9a743f1e7fd", "6c746acb5d2ab9edff4b22fe42f8489335c123a3", "cef495e5dc9c27ddfc10dbcb43396a907cdf3c92", "NEXT-025")),
    "ARCHITECTURE_QUEUE": ("docs/architecture/INTEGRATION-QUEUE/README.md", ("IN-024", "OUT-024", "EVT-0113", "SCRTC-B2", "NEXT-025", "Issue #20", "Issue #21", "IN-025", "OUT-025", "EVT-0114", "LAL-20261023-012")),
    "LESSON_REGISTRY": ("docs/architecture/ARCHITECTURE-LESSONS/README.md", ("LAL-20261023-011", "EVT-0113", "NEXT-025", "LAL-20261023-012", "EVT-0114")),
    "BEHAVIOR_TRACE_INDEX": ("docs/architecture/BEHAVIOR-TRACE/README.md", ("EVT-0113", "LAL-20261023-011", "IN-024", "OUT-024", "NEXT-025", "EVT-0114", "LAL-20261023-012", "IN-025", "OUT-025")),
    "NEXT_024": ("docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md", ("SCRTC-B2", "IN-024", "OUT-024", "NEXT-025", "Issue #20", "Issue #21")),
    "NEXT_025": ("docs/0.0/anchors/PALANG-0.0-NEXT-20261023-025-SOURCE-RULE-TEST-CROSSWALK-AND-COLD-START.md", ("IN-024", "OUT-024", "EVT-0113", "LAL-20261023-011", "NEXT-022", "NEXT-023", "NEXT-024", "Issue #20", "Issue #21", "IN-025", "OUT-025", "EVT-0114", "LAL-20261023-012")),
}
for label, (rel, required_ids) in interaction_surfaces.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"INTERACTION_SURFACE_MISSING_FILE surface={label} path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    for required_id in required_ids:
        if required_id not in content:
            errors.append(f"INTERACTION_SURFACE_MISSING_ID surface={label} id={required_id}")

# Verification/time-binding evidence gate for the latest material interaction.
verification_required = {
    "IN-024 verification checkpoint": "docs/architecture/BEHAVIOR-TRACE/VERIFICATION-CHECKPOINT-INT-20261023-024.md",
    "IN-024 time binding": "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261023-024.md",
}
for label, rel in verification_required.items():
    if not (ROOT / rel).is_file():
        errors.append(f"VERIFICATION_MISSING_REQUIRED_FILE label={label!r} path={rel}")

verification_surfaces = {
    "ULCG_MASTER": ("docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md", ("VERIFICATION-CHECKPOINT-INT-20261023-024", "TIME-BINDING-INT-20261023-024", "39972058925", "39971900914")),
    "REFERENCE_INDEX": ("docs/REFERENCE_INDEX.md", ("VERIFICATION-CHECKPOINT-INT-20261023-024", "TIME-BINDING-INT-20261023-024")),
    "ZERO_ZERO_REGISTRY": ("docs/0.0/README.md", ("VERIFICATION-CHECKPOINT-INT-20261023-024", "TIME-BINDING-INT-20261023-024")),
    "BEHAVIOR_TRACE_INDEX": ("docs/architecture/BEHAVIOR-TRACE/README.md", ("VERIFICATION-CHECKPOINT-INT-20261023-024", "TIME-BINDING-INT-20261023-024")),
    "VERIFICATION_CHECKPOINT": ("docs/architecture/BEHAVIOR-TRACE/VERIFICATION-CHECKPOINT-INT-20261023-024.md", ("39972058925", "7e46b8a2d9062753dd6be2759c2fe03233a4b33b", "f3474ba4e1275b2b12b8ebdf99c77087e836ad57", "OPEN / NOT CONFIRMED")),
    "TIME_BINDING": ("docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261023-024.md", ("2026-10-23T14:44:05Z", "2026-10-23T18:14:05+03:30", "UNKNOWN / UNVERIFIED")),
}
for label, (rel, required_ids) in verification_surfaces.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"VERIFICATION_SURFACE_MISSING_FILE surface={label} path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    for required_id in required_ids:
        if required_id not in content:
            errors.append(f"VERIFICATION_SURFACE_MISSING_ID surface={label} id={required_id}")


# Current point 0 / next 0.0 graph gate (CURRENT-036)
current_point_surfaces = {
    "CURRENT_036": ("docs/0.0/anchors/PALANG-0.0-CURRENT-20261024-036-USER-REQUEST-AND-LIVING-REGISTRATION.md", ("CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "LAL-20261024-013", "NEXT-036", "Issue #20", "Issue #21")),
    "IN_026": ("docs/0.0/anchors/PALANG-0.0-IN-20261024-026-REGISTER-CURRENT-POINT-0.md", ("IN-026", "OUT-026", "CURRENT-036", "EVT-0134", "NEXT-036")),
    "OUT_026": ("docs/0.0/anchors/PALANG-0.0-OUT-20261024-026-REGISTER-CURRENT-POINT-0.md", ("OUT-026", "IN-026", "CURRENT-036", "EVT-0134", "NEXT-036")),
    "NEXT_036": ("docs/0.0/anchors/PALANG-0.0-NEXT-20261024-036-HISTORIC-SOURCE-CENSUS-AND-COLD-START.md", ("NEXT-036", "CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "LAL-20261024-013", "Issue #20", "Issue #21")),
    "EVT_0134": ("docs/architecture/BEHAVIOR-TRACE/EVT-0134-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION-2026-10-24.md", ("EVT-0134", "IN-026", "OUT-026", "CURRENT-036", "NEXT-036", "LAL-20261024-013")),
    "LAL_013": ("docs/architecture/ARCHITECTURE-LESSONS/lessons/LAL-20261024-013-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION.md", ("LAL-20261024-013", "EVT-0134", "IN-026", "OUT-026", "CURRENT-036", "NEXT-036")),
    "TIME_BINDING_026": ("docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261024-026.md", ("TIME-BINDING-INT-20261024-026", "IN-026", "OUT-026", "EVT-0134", "CURRENT-036", "NEXT-036", "UTC+03:30")),
    "VERIFICATION_CHECKPOINT_026": ("docs/architecture/BEHAVIOR-TRACE/VERIFICATION-CHECKPOINT-INT-20261024-026.md", ("VERIFICATION-CHECKPOINT-INT-20261024-026", "CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "LAL-20261024-013", "NEXT-036", "Issue #20", "Issue #21", "PENDING")),
    "ULCG_MASTER": ("docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md", ("Version: 1.2.5", "CURRENT-036", "NEXT-036", "EVT-0134", "LAL-20261024-013")),
    "REFERENCE_INDEX": ("docs/REFERENCE_INDEX.md", ("CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "NEXT-036")),
    "ZERO_ZERO_REGISTRY": ("docs/0.0/README.md", ("CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "NEXT-036")),
    "BEHAVIOR_TRACE_INDEX": ("docs/architecture/BEHAVIOR-TRACE/README.md", ("CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "NEXT-036")),
    "LESSON_REGISTRY": ("docs/architecture/ARCHITECTURE-LESSONS/README.md", ("LAL-20261024-013", "EVT-0134", "CURRENT-036", "NEXT-036")),
    "SOURCE_RULE_MAP": ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md", ("CURRENT-036", "NEXT-036", "Issue #20", "Issue #21")),
    "ARCHITECTURE_QUEUE": ("docs/architecture/INTEGRATION-QUEUE/README.md", ("CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "NEXT-036", "Issue #20", "Issue #21")),
    "INITIAL_MODEL_MASTER": ("docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md", ("CURRENT-036", "IN-026", "OUT-026", "EVT-0134", "NEXT-036")),
}
for label, (rel, required_ids) in current_point_surfaces.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"CURRENT_POINT_MISSING_FILE surface={label} path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    for required_id in required_ids:
        if required_id not in content:
            errors.append(f"CURRENT_POINT_MISSING_ID surface={label} id={required_id}")


# Source-clause crosswalk batch 3 gate
source_batch3_surfaces = {
    "SOURCE_CLAUSE_CROSSWALK_BATCH3": ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-CLAUSE-CROSSWALK-BATCH-3-2026-10-24-001.md", ("SCRTC-B3-2026-10-24-001", "EXC-REG-GATE", "AUTO-FINAL-REG", "3LR-GOVREG", "EIO-ANCHOR", "EI-ANCHOR", "Issue #20", "Issue #21")),
    "ULCG_MASTER_BATCH3": ("docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md", ("Version: 1.2.5", "SCRTC-B3-2026-10-24-001", "NEXT-036")),
    "SOURCE_RULE_MAP_BATCH3": ("docs/architecture/ARCHITECTURE-LESSONS/SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md", ("SCRTC-B3-2026-10-24-001", "Issue #20", "Issue #21")),
    "HISTORIC_LEDGER_BATCH3": ("docs/architecture/ARCHITECTURE-LESSONS/HISTORIC-LESSON-MIGRATION-LEDGER-2026-10-23-001.md", ("SCRTC-B3-2026-10-24-001", "EXC-REG-GATE-2026-09-02-001", "AUTO-FINAL-REG-ORCH-2026-08-30-001")),
    "INTEGRATION_QUEUE_BATCH3": ("docs/architecture/INTEGRATION-QUEUE/README.md", ("SCRTC-B3-2026-10-24-001", "NEXT-036", "Issue #20", "Issue #21")),
    "REFERENCE_INDEX_BATCH3": ("docs/REFERENCE_INDEX.md", ("SCRTC-B3-2026-10-24-001", "NEXT-036")),
    "ZERO_ZERO_REGISTRY_BATCH3": ("docs/0.0/README.md", ("SCRTC-B3-2026-10-24-001", "NEXT-036", "Issue #21")),
    "NEXT_036_BATCH3": ("docs/0.0/anchors/PALANG-0.0-NEXT-20261024-036-HISTORIC-SOURCE-CENSUS-AND-COLD-START.md", ("SCRTC-B3-2026-10-24-001", "ULCG v1.2.5", "Issue #20", "Issue #21")),
}
for label, (rel, required_ids) in source_batch3_surfaces.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"SOURCE_BATCH3_MISSING_FILE surface={label} path={rel}")
        continue
    content = path.read_text(encoding="utf-8")
    for required_id in required_ids:
        if required_id not in content:
            errors.append(f"SOURCE_BATCH3_MISSING_ID surface={label} id={required_id}")

print("LIVING_ARCHITECTURE_AUDIT")
print(f"required_files_checked={len(required)}")
print(f"ulcg_required_files_checked={len(ulcg_required)}")
print(f"ulcg_surfaces_checked={len(ulcg_surfaces)}")
print(f"continuity_required_files_checked={len(continuity_required)}")
print(f"continuity_surfaces_checked={len(continuity_surfaces)}")
print("external_persistence_tested=false")
print("chatgpt_all_conversation_capture_tested=false")
if errors:
    print(f"result=FAIL errors={len(errors)}")
    for error in errors:
        print(error)
    sys.exit(1)
print("result=PASS structural_repository_checks")
