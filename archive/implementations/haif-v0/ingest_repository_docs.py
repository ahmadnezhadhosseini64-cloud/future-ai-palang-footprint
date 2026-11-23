"""Controlled, provenance-preserving ingestion of selected repository references into HAIF v0.

Run from a checked-out repository with the HAIF API running:
    python prototype/haif-v0/ingest_repository_docs.py --base-url http://127.0.0.1:8000

This imports only the explicit allowlist below. It never deletes or overwrites stored
records; reruns may create new records, so inspect the report before repeating.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPOSITORY = "ahmadnezhadhosseini64-cloud/future-ai-palang-footprint"
ALLOWLIST = (
    "docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md",
    "docs/architecture/مدل اولیه AI/سند مرجع مادر — الگوریتم استخراج مدل و محصول رایگان HAIF.md",
    "docs/architecture/مدل اولیه AI/صف گام‌های بعدی و موارد باز.md",
    "docs/reference/REFERENCE-DOCUMENTS/PALANG-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21-001.md",
    "docs/architecture/BEHAVIOR-TRACE/EVT-0064-HAIF-DOCUMENT-RETRIEVAL-PROVENANCE-2026-10-21.md",
    "docs/architecture/BEHAVIOR-TRACE/EVT-0065-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21.md",
)


def repository_root(start: Path | None = None) -> Path:
    """Resolve the checkout root without assuming the caller's current directory."""
    candidate = (start or Path(__file__)).resolve()
    for parent in (candidate, *candidate.parents):
        if (parent / ".git").exists() or (parent / "docs").is_dir():
            return parent
    raise RuntimeError("REPOSITORY_ROOT_NOT_FOUND")


def current_commit(root: Path) -> str:
    """Use explicit CI provenance first, then local git; never invent a commit."""
    supplied = os.environ.get("GITHUB_SHA", "").strip()
    if supplied:
        return supplied
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN_COMMIT"


def document_version(content: str) -> str:
    """Read a declared version when available; otherwise label it as unversioned."""
    match = re.search(
        r"(?im)^\s*(?:[-*]\s*)?(?:Version|Version / نسخه|نسخه)\s*[:：]\s*`?([^\s`]+)",
        content,
    )
    return match.group(1).rstrip(".,;") if match else "UNDECLARED"


def ingest(base_url: str, root: Path) -> dict:
    base_url = base_url.rstrip("/")
    commit = current_commit(root)
    results = []
    for relative_path in ALLOWLIST:
        path = root / relative_path
        if not path.is_file():
            results.append({"source_path": relative_path, "status": "SOURCE_MISSING"})
            continue
        content = path.read_text(encoding="utf-8")
        title = next((line.lstrip("# ").strip() for line in content.splitlines() if line.startswith("# ")), path.name)
        payload = {
            "title": title,
            "source_path": relative_path,
            "version": document_version(content),
            "content": content,
            "source_origin": f"GitHub repository {REPOSITORY}; commit={commit}; allowlisted repository document",
        }
        request = Request(
            f"{base_url}/api/v1/documents",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=20) as response:
                saved = json.loads(response.read().decode("utf-8"))
            if saved.get("status") != "WRITE_READBACK_VERIFIED" or not saved.get("content_sha256"):
                results.append({"source_path": relative_path, "status": "WRITE_READBACK_UNVERIFIED"})
            else:
                results.append({
                    "source_path": relative_path,
                    "version": payload["version"],
                    "document_id": saved.get("document_id"),
                    "content_sha256": saved["content_sha256"],
                    "status": "WRITE_READBACK_VERIFIED",
                })
        except HTTPError as exc:
            results.append({"source_path": relative_path, "status": "HTTP_ERROR", "detail": exc.code})
        except (URLError, TimeoutError, json.JSONDecodeError) as exc:
            results.append({"source_path": relative_path, "status": "REQUEST_FAILED", "detail": str(exc)})
    return {
        "repository": REPOSITORY,
        "source_commit": commit,
        "target": f"{base_url}/api/v1/documents",
        "allowlist_count": len(ALLOWLIST),
        "results": results,
        "verified_count": sum(item["status"] == "WRITE_READBACK_VERIFIED" for item in results),
        "complete": len(results) == len(ALLOWLIST) and all(
            item["status"] == "WRITE_READBACK_VERIFIED" for item in results
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--root", type=Path, default=None)
    args = parser.parse_args()
    root = repository_root(args.root)
    report = ingest(args.base_url, root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
