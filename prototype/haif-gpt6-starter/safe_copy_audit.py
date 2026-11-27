"""Fail-closed structural audit for Copy-2 workflow and portable recovery package."""
from pathlib import Path
import json

REQUIRED_PACKAGE = (
    "README.md", "manifest.json", "engine.py", "state.schema.json",
    "LIVING_MASTER_REFERENCE.md", "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md",
    "UNIVERSAL_AI_HOST_ENTRY_FA.md", "safe_points_guard.py",
)

def audit_workflow(text: str) -> list[str]:
    failures = []
    lines = text.splitlines()
    if "permissions:" not in lines or "  contents: read" not in lines:
        failures.append("workflow permissions must be contents: read only")
    if any(line.strip().endswith(": write") for line in lines):
        failures.append("write permission found")
    if "persist-credentials: false" not in text:
        failures.append("checkout credentials must not persist in git config")
    expected_checkout = "ref: " + "$" + "{{ github.event.pull_request.head.sha || github.sha }}"
    if expected_checkout not in text:
        failures.append("checkout is not bound to event head SHA")
    if "palang-safe-copy-2-test-20261126" not in text or "palang-safe-copy-1-baseline-20261126" not in text:
        failures.append("copy branch trigger/base missing")
    if any(line.strip().startswith("uses:") and any(line.strip().endswith("@" + floating) for floating in ("main", "master", "latest")) for line in lines):
        failures.append("floating action reference found")
    if any("git push" in line or "gh pr merge" in line for line in lines):
        failures.append("promotion/write command found")
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

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", type=Path)
    parser.add_argument("--package", type=Path)
    args = parser.parse_args()
    failures = []
    if args.workflow:
        failures.extend(audit_workflow(args.workflow.read_text(encoding="utf-8")))
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
