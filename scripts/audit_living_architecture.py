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
    ("docs/reference/REFERENCE_INDEX.md", "REFERENCE_INDEX"),
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

print("LIVING_ARCHITECTURE_AUDIT")
print(f"required_files_checked={len(required)}")
print("external_persistence_tested=false")
print("chatgpt_all_conversation_capture_tested=false")
if errors:
    print(f"result=FAIL errors={len(errors)}")
    for error in errors:
        print(error)
    sys.exit(1)
print("result=PASS structural_repository_checks")
