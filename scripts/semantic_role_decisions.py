#!/usr/bin/env python3
"""Apply source-backed role decisions to graph collision groups without hiding raw counts."""
import json
from pathlib import Path

def apply_role_decisions(groups, nodes, decisions, identifier_type=None):
    node_by_path = {node.get("path"): node for node in nodes}
    accepted, rejected = [], []
    enriched = []
    for group in groups:
        item = dict(group)
        item["semantic_review"] = {"status": "UNREVIEWED"}
        for decision in decisions:
            if decision.get("status") != "ROLE-ADJUDICATED":
                continue
            if identifier_type is not None and decision.get("identifier_type") != identifier_type:
                continue
            if decision.get("identifier_value") != group.get("key"):
                continue
            decision_paths = decision.get("paths", [])
            expected_paths = sorted(p.get("path", "") for p in decision_paths if isinstance(p, dict))
            group_paths = sorted(group.get("paths", []))
            if expected_paths != group_paths or len(expected_paths) != len(decision_paths):
                rejected.append({"decision_id": decision.get("decision_id"), "reason": "path_set_mismatch", "identifier_value": group.get("key")})
                continue
            failures = []
            for record in decision_paths:
                node = node_by_path.get(record.get("path"))
                if not node:
                    failures.append({"path": record.get("path"), "reason": "source_node_missing"})
                elif node.get("sha256") != record.get("content_sha256"):
                    failures.append({"path": record.get("path"), "reason": "source_sha256_mismatch", "expected": record.get("content_sha256"), "actual": node.get("sha256")})
            if failures:
                rejected.append({"decision_id": decision.get("decision_id"), "reason": "source_hash_verification_failed", "failures": failures})
                continue
            item["semantic_review"] = {
                "status": "ROLE-ADJUDICATED",
                "decision_id": decision.get("decision_id"),
                "decision_type": decision.get("decision_type"),
                "roles": [{"path": p["path"], "role": p.get("role")} for p in decision_paths],
                "rationale": decision.get("rationale"),
                "source_manifest_commit": decision.get("source_manifest_commit"),
                "evidence_refs": decision.get("evidence_refs", []),
                "history_preserved": bool(decision.get("preserve_history")),
                "no_rename": bool(decision.get("no_rename")),
                "no_delete": bool(decision.get("no_delete")),
            }
            accepted.append(decision.get("decision_id"))
            break
        enriched.append(item)
    return enriched, {"decisions_loaded": len(decisions), "decisions_accepted": len(set(accepted)), "accepted_decision_ids": sorted(set(accepted)), "decisions_rejected": rejected,
                      "groups_reviewed": sum(g["semantic_review"]["status"] == "ROLE-ADJUDICATED" for g in enriched),
                      "groups_unreviewed": sum(g["semantic_review"]["status"] != "ROLE-ADJUDICATED" for g in enriched)}

def load_decisions(path):
    decisions, errors = [], []
    p = Path(path)
    if not p.exists():
        return [], [{"line": 0, "reason": "decision_ledger_missing"}]
    for line_no, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            decisions.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append({"line": line_no, "reason": "invalid_json", "detail": str(exc)})
    return decisions, errors
