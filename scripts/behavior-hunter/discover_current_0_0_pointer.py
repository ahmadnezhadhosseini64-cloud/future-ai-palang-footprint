#!/usr/bin/env python3
"""Discover competing live CURRENT declarations without promoting a winner.

This checker intentionally distinguishes historical references from explicit live
claims. A conflict produces AMBIGUOUS/BLOCKED; it never selects by number alone.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/portable/RAHM/CURRENT-065-OVERLAY-MANIFEST.json"
VERIFIER = ROOT / "scripts/behavior-hunter/verify_current_0_0_chain.py"
PORTABLE_MASTER = ROOT / "docs/portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md"
REGISTRY_SOURCES = {
    "0.0 registry": ROOT / "docs/0.0/README.md",
    "integration queue": ROOT / "docs/architecture/INTEGRATION-QUEUE/README.md",
    "reference index": ROOT / "docs/REFERENCE_INDEX.md",
}

CURRENT_PATH = re.compile(r"docs/0\.0/anchors/(PALANG-0\.0-CURRENT-[^\s)`]+\.md)")
CURRENT_ID = re.compile(r"\bCURRENT-(?:\d{8}-)?(\d{3})\b")


def explicit_registry_claims(text: str, source: str) -> list[dict]:
    """Return the latest explicit live pointer claim from one append-only registry.

    Older lines that once said CURRENT-X was live must not compete with a later
    explicit continuation. This chooses only the latest declaration within this
    source and never rewrites or deletes historical records.
    """
    patterns = (
        re.compile(r"\b(CURRENT-(?:\d{8}-)?\d{3})\s+remains current\b", re.I),
        re.compile(r"current point:\s*\[?(CURRENT-(?:\d{8}-)?\d{3})", re.I),
        re.compile(r"current continuation:\s*\[?(CURRENT-(?:\d{8}-)?\d{3})", re.I),
        re.compile(r"canonical live checkpoint is now\s+\[?(CURRENT-(?:\d{8}-)?\d{3})", re.I),
        re.compile(r"current execution continuation remains\s+\[?(CURRENT-(?:\d{8}-)?\d{3})", re.I),
    )
    claims = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for pattern in patterns:
            match = pattern.search(line)
            if match:
                claims.append({
                    "source": source,
                    "line": line_no,
                    "current_id": match.group(1).upper(),
                    "declaration": line.strip(),
                    "scope": "global_project_registry",
                })
                break
    return claims[-1:]

def discover_from_texts(manifest_text: str, verifier_text: str, portable_text: str,
                        registry_texts: dict[str, str]) -> dict:
    failures = []
    declarations = []
    try:
        manifest = json.loads(manifest_text)
        target = manifest.get("current_checkpoint")
        if not isinstance(target, str) or not target:
            failures.append("manifest.current_checkpoint is missing")
        else:
            match = CURRENT_PATH.search(target)
            if not match:
                failures.append("manifest.current_checkpoint is not a recognized CURRENT anchor path")
            else:
                declarations.append({
                    "source": "overlay manifest current_checkpoint",
                    "current_id": "CURRENT-" + CURRENT_ID.search(match.group(1)).group(1),
                    "path": target,
                })
    except (json.JSONDecodeError, AttributeError) as exc:
        failures.append("manifest parse failed: " + str(exc))

    verifier_match = re.search(r'"current"\s*:\s*"([^"]+CURRENT-[^"]+\.md)"', verifier_text)
    if not verifier_match:
        failures.append('verifier FILES["current"] declaration not found')
    else:
        match = CURRENT_PATH.search(verifier_match.group(1))
        if not match:
            failures.append("verifier current path is not a recognized CURRENT anchor")
        else:
            declarations.append({
                "source": 'historical recovery verifier FILES["current"]',
                "current_id": "CURRENT-" + CURRENT_ID.search(match.group(1)).group(1),
                "path": verifier_match.group(1),
            })

    # The portable master has a top-level live pointer distinct from historical
    # mentions later in the document.
    top = portable_text.splitlines()[:30]
    portable_claim = next((line for line in top if re.search(r"Current 0\.0:", line, re.I)), None)
    if not portable_claim:
        failures.append("portable master top-level Current 0.0 declaration not found")
    else:
        match = CURRENT_ID.search(portable_claim)
        if not match:
            failures.append("portable master current declaration has no CURRENT ID")
        else:
            declarations.append({
                "source": "portable master top-level Current 0.0",
                "current_id": "CURRENT-" + match.group(1),
                "declaration": portable_claim.strip(),
            })

    # The manifest, verifier and portable master describe a bounded overlay
    # recovery scope. Append-only registries describe the global project pointer.
    # Different IDs can be valid across these scopes and must not be conflated.
    for declaration in declarations:
        declaration["scope"] = "overlay_recovery"
    overlay_declarations = list(declarations)
    registry_declarations = []
    for source, text in registry_texts.items():
        registry_declarations.extend(explicit_registry_claims(text, source))
    declarations.extend(registry_declarations)

    overlay_ids = sorted({d["current_id"] for d in overlay_declarations})
    registry_ids = sorted({d["current_id"] for d in registry_declarations})
    registry_sources = {d["source"] for d in registry_declarations}
    unique_ids = sorted({d["current_id"] for d in declarations})
    by_source = {}
    for declaration in declarations:
        by_source.setdefault(declaration["source"], []).append(declaration["current_id"])

    if failures:
        status = "BLOCKED"
    elif len(overlay_ids) != 1 or len(registry_ids) > 1:
        status = "AMBIGUOUS"
    elif not registry_ids:
        status = "CONSISTENT" if len(overlay_ids) == 1 else "AMBIGUOUS"
    elif overlay_ids[0] == registry_ids[0]:
        status = "CONSISTENT"
    elif len(registry_sources) == len(REGISTRY_SOURCES):
        status = "SCOPED_CONSISTENT"
    else:
        status = "AMBIGUOUS"

    return {
        "test_id": "HAIF-CURRENT-POINTER-DISCOVERY-0.2",
        "status": status,
        "winner_selected": False,
        "candidate_ids": unique_ids,
        "scopes": {
            "overlay_recovery_current": overlay_ids,
            "global_project_current": registry_ids,
        },
        "declarations": declarations,
        "source_ids": by_source,
        "failures": failures,
        "rule": "Use the latest live declaration per append-only registry. Keep overlay recovery and global project pointers in separate scopes; never choose a winner by numeric order.",
    }


def main() -> int:
    try:
        result = discover_from_texts(
            MANIFEST.read_text(encoding="utf-8"),
            VERIFIER.read_text(encoding="utf-8"),
            PORTABLE_MASTER.read_text(encoding="utf-8"),
            {name: path.read_text(encoding="utf-8") for name, path in REGISTRY_SOURCES.items()},
        )
    except OSError as exc:
        result = {
            "test_id": "HAIF-CURRENT-POINTER-DISCOVERY-0.1",
            "status": "BLOCKED",
            "winner_selected": False,
            "candidate_ids": [],
            "declarations": [],
            "failures": ["source read failed: " + str(exc)],
        }
    out = ROOT / "audit-output" / "current-pointer-discovery.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] in ("CONSISTENT", "SCOPED_CONSISTENT") else 2


if __name__ == "__main__":
    raise SystemExit(main())
