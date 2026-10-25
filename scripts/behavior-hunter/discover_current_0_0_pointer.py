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
    """Return only lines that assert a live/current execution pointer.

    Historical headings and ordinary links are deliberately ignored. The rules
    are narrow and reviewable; new registry wording must be added with a fixture.
    """
    claims = []
    for line_no, line in enumerate(text.splitlines(), 1):
        lower = line.lower()
        explicit = (
            "remains current" in lower
            or "current point:" in lower
            or "current continuation:" in lower
            or "canonical live checkpoint is now" in lower
            or "current execution continuation remains" in lower
        )
        if not explicit:
            continue
        for match in CURRENT_ID.finditer(line):
            claims.append({
                "source": source,
                "line": line_no,
                "current_id": "CURRENT-" + match.group(1),
                "declaration": line.strip(),
            })
    return claims


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

    for source, text in registry_texts.items():
        declarations.extend(explicit_registry_claims(text, source))

    by_source = {}
    for declaration in declarations:
        by_source.setdefault(declaration["source"], []).append(declaration["current_id"])
    unique_ids = sorted({d["current_id"] for d in declarations})
    status = "BLOCKED" if failures else ("CONSISTENT" if len(unique_ids) == 1 else "AMBIGUOUS")
    return {
        "test_id": "HAIF-CURRENT-POINTER-DISCOVERY-0.1",
        "status": status,
        "winner_selected": False,
        "candidate_ids": unique_ids,
        "declarations": declarations,
        "source_ids": by_source,
        "failures": failures,
        "rule": "A conflict is evidence of ambiguity, not permission to choose the numerically largest anchor.",
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
    return 0 if result["status"] == "CONSISTENT" else 2


if __name__ == "__main__":
    raise SystemExit(main())
