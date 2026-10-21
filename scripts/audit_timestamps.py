#!/usr/bin/env python3
"""Repository-wide timestamp inventory and consistency audit. Never mutates source records."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re, subprocess

ROOT = Path(".")
OUT = ROOT / "audit-output"
OUT.mkdir(exist_ok=True)
RUN_UTC = datetime.now().astimezone().astimezone(__import__("datetime").timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
try:
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
except Exception:
    commit = "UNKNOWN"

TEXT_EXT = {".md", ".txt", ".yml", ".yaml", ".json", ".py", ".html", ".xml", ".csv", ".toml"}
SKIP_PARTS = {".git", "node_modules", ".venv", "venv", "audit-output"}
ISO_RE = re.compile(r"(?<![A-Za-z0-9])20\d{2}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d{1,9})?)?(?:Z|[+-]\d{2}:?\d{2})?)?")
OFFSET_RE = re.compile(r"(?:UTC\s*\+?\d{1,2}(?::\d{2})?|Asia/Tehran|[+-]\d{2}:\d{2})", re.I)
UTC_RE = re.compile(r"\bUTC\b|Z\b|[+-]\d{2}:\d{2}", re.I)
UNKNOWN_RE = re.compile(r"UNKNOWN\s*/\s*UNVERIFIED|UNKNOWN|نامعلوم|ثبت نشده", re.I)
TIME_LABEL_RE = re.compile(r"timestamp|time|زمان|تاریخ|created at|registered at|read.?back|commit", re.I)
ID_RE = re.compile(r"Stable ID|Production ID|Event ID|شناسه پایدار|شناسه تولید", re.I)

records = []
for p in sorted(ROOT.rglob("*")):
    if not p.is_file() or p.suffix.lower() not in TEXT_EXT or any(part in SKIP_PARTS for part in p.parts):
        continue
    try:
        raw = p.read_bytes()
        txt = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError):
        continue
    rel = p.as_posix()
    relevant = (rel.startswith(("docs/reference/REFERENCE-DOCUMENTS/", "docs/architecture/BEHAVIOR-TRACE/",
                                "docs/architecture/INTEGRATION-QUEUE/", "docs/0.0/", "checkpoints/",
                                "provenance/", "recovery/", "docs/architecture/GOVERNANCE/"))
                or bool(ID_RE.search(txt)))
    if not relevant:
        continue
    iso = ISO_RE.findall(txt)
    time_lines = [line.strip() for line in txt.splitlines() if TIME_LABEL_RE.search(line)]
    explicit_unknown = bool(UNKNOWN_RE.search("\n".join(time_lines)))
    has_utc = bool(UTC_RE.search("\n".join(time_lines))) or any(x.endswith("Z") or re.search(r"[+-]\d{2}:\d{2}$", x) for x in iso)
    has_offset_or_zone = bool(OFFSET_RE.search("\n".join(time_lines))) or any(x.endswith("Z") or re.search(r"[+-]\d{2}:\d{2}$", x) for x in iso)
    timestamp_labels = [line[:240] for line in time_lines[:30]]
    missing_time = not iso and not explicit_unknown
    records.append({
        "path": rel, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
        "stable_or_event_id_present": bool(ID_RE.search(txt)),
        "iso_timestamp_count": len(iso), "iso_timestamps": iso[:100],
        "timestamp_label_count": len(time_lines), "timestamp_label_samples": timestamp_labels,
        "has_explicit_utc_or_offset_evidence": has_utc,
        "has_zone_or_offset_evidence": has_offset_or_zone,
        "explicit_unknown_near_time_label": explicit_unknown,
        "missing_iso_and_unknown_marker": missing_time,
        "relevant_scope": rel.startswith(("docs/reference/REFERENCE-DOCUMENTS/", "docs/architecture/BEHAVIOR-TRACE/",
                                           "docs/architecture/INTEGRATION-QUEUE/", "docs/0.0/", "checkpoints/",
                                           "provenance/", "recovery/", "docs/architecture/GOVERNANCE/"))
    })

counts = {
    "repository_commit": commit,
    "audit_execution_utc": RUN_UTC,
    "relevant_documents_scanned": len(records),
    "reference_documents_scanned": sum(r["path"].startswith("docs/reference/REFERENCE-DOCUMENTS/") for r in records),
    "behavior_event_documents_scanned": sum(r["path"].startswith("docs/architecture/BEHAVIOR-TRACE/EVT-") for r in records),
    "zero_zero_and_checkpoint_documents_scanned": sum(r["path"].startswith(("docs/0.0/", "checkpoints/")) for r in records),
    "documents_with_iso_timestamp": sum(r["iso_timestamp_count"] > 0 for r in records),
    "documents_without_iso_or_unknown_marker": sum(r["missing_iso_and_unknown_marker"] for r in records),
    "documents_with_utc_or_offset_evidence": sum(r["has_explicit_utc_or_offset_evidence"] for r in records),
    "documents_with_zone_or_offset_evidence": sum(r["has_zone_or_offset_evidence"] for r in records),
    "documents_with_explicit_unknown_near_time_label": sum(r["explicit_unknown_near_time_label"] for r in records),
}
report = {"schema":"palang-timestamp-audit/v1", "scope_note":"Repository text inventory only. Timestamp strings are detected, not all semantically interpreted; each flagged item requires review. No source file is rewritten.", "counts":counts, "records":records}
(OUT / "timestamp-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
lines = ["# Repository Timestamp Audit", "", f"- Execution UTC: {RUN_UTC}", f"- Repository commit: {commit}", "", "## Counts"]
lines += [f"- {k}: {v}" for k,v in counts.items() if k not in {"repository_commit","audit_execution_utc"}]
lines += ["", "## Files needing review", "Rows are flags for human/semantic review, not proof of error."]
flagged = [r for r in records if r["missing_iso_and_unknown_marker"] or (r["timestamp_label_count"] and not r["has_explicit_utc_or_offset_evidence"])]
if not flagged: lines.append("- No files flagged by the simple detection rules.")
for r in flagged:
    lines.append(f"- `{r['path']}`: iso_count={r['iso_timestamp_count']}; time_labels={r['timestamp_label_count']}; UTC/offset={r['has_utc_or_offset_evidence']}; explicit_unknown={r['explicit_unknown_near_time_label']}")
lines += ["", "## Limits", "- This is a repository-wide automated inventory, not proof that all timestamp pairs describe the same event.", "- UTC/local arithmetic and lineage conflicts require semantic review; no timestamp is inferred from filename or commit time.", "- User-message timestamps remain UNKNOWN unless a trusted source supplies them.", "- No external destination or cross-host persistence is tested."]
(OUT / "timestamp-audit.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("REPOSITORY_TIMESTAMP_AUDIT")
for k,v in counts.items(): print(f"{k}={v}")
print("outputs=audit-output/timestamp-audit.txt,audit-output/timestamp-audit.json")
