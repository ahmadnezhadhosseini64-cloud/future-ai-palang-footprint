#!/usr/bin/env python3
"""Apply source-backed role decisions without hiding raw collision groups.

A decision may cover a verified subset of a collision group. Covered paths receive
role annotations, but the group remains PARTIALLY-ROLE-ADJUDICATED until every
member is covered without role conflicts. Stale hashes and paths outside the group
are rejected.
"""
from pathlib import Path
import json


def apply_role_decisions(groups, nodes, decisions, identifier_type=None):
    node_by_path = {node.get("path"): node for node in nodes}
    accepted_ids, rejected, enriched = set(), [], []

    for group in groups:
        item = dict(group)
        group_paths = sorted(set(group.get("paths", [])))
        roles_by_path = {}
        decisions_by_path = {}
        accepted_for_group = []

        for decision in decisions:
            if decision.get("status") != "ROLE-ADJUDICATED":
                continue
            if identifier_type is not None and decision.get("identifier_type") != identifier_type:
                continue
            if decision.get("identifier_value") != group.get("key"):
                continue

            records = decision.get("paths", [])
            expected_paths = [p.get("path", "") for p in records if isinstance(p, dict)]
            unique_paths = set(expected_paths)
            if (not records or len(expected_paths) != len(records) or
                    len(unique_paths) != len(expected_paths) or
                    not unique_paths.issubset(set(group_paths))):
                rejected.append({
                    "decision_id": decision.get("decision_id"),
                    "reason": "path_set_mismatch",
                    "identifier_value": group.get("key"),
                    "decision_paths": sorted(unique_paths),
                    "group_paths": group_paths,
                })
                continue

            failures = []
            for record in records:
                path = record.get("path")
                node = node_by_path.get(path)
                if not node:
                    failures.append({"path": path, "reason": "source_node_missing"})
                elif node.get("sha256") != record.get("content_sha256"):
                    failures.append({
                        "path": path,
                        "reason": "source_sha256_mismatch",
                        "expected": record.get("content_sha256"),
                        "actual": node.get("sha256"),
                    })
            if failures:
                rejected.append({
                    "decision_id": decision.get("decision_id"),
                    "reason": "source_hash_verification_failed",
                    "failures": failures,
                })
                continue

            conflicts = []
            for record in records:
                path, role = record["path"], record.get("role")
                if path in roles_by_path and roles_by_path[path] != role:
                    conflicts.append({
                        "path": path,
                        "existing_role": roles_by_path[path],
                        "proposed_role": role,
                    })
            if conflicts:
                rejected.append({
                    "decision_id": decision.get("decision_id"),
                    "reason": "role_conflict",
                    "conflicts": conflicts,
                })
                continue

            for record in records:
                path = record["path"]
                roles_by_path[path] = record.get("role")
                decisions_by_path.setdefault(path, []).append(decision.get("decision_id"))
            accepted_for_group.append(decision)
            accepted_ids.add(decision.get("decision_id"))

        covered = set(roles_by_path)
        resolution_classes = {
            d.get("resolution_class", "FULLY_ROLE_ADJUDICATED")
            for d in accepted_for_group
        }
        if not accepted_for_group:
            status = "UNREVIEWED"
        elif covered != set(group_paths):
            status = "PARTIALLY-ROLE-ADJUDICATED"
        elif "REKEY_REQUIRED" in resolution_classes:
            status = "ROLE-ADJUDICATED-REKEY-REQUIRED"
        elif "LINEAGE_REVIEW_REQUIRED" in resolution_classes:
            status = "ROLE-ADJUDICATED-OPEN-LINEAGE"
        else:
            status = "ROLE-ADJUDICATED"

        item["semantic_review"] = {
            "status": status,
            "resolution_classes": sorted(resolution_classes),
            "decision_ids": sorted({d.get("decision_id") for d in accepted_for_group}),
            "roles": [
                {
                    "path": path,
                    "role": roles_by_path[path],
                    "decision_ids": sorted(set(decisions_by_path[path])),
                }
                for path in sorted(roles_by_path)
            ],
            "covered_paths": sorted(covered),
            "unreviewed_paths": sorted(set(group_paths) - covered),
            "rationales": [d.get("rationale") for d in accepted_for_group if d.get("rationale")],
            "source_manifest_commits": sorted({
                d.get("source_manifest_commit") for d in accepted_for_group
                if d.get("source_manifest_commit")
            }),
            "evidence_refs": sorted({
                ref for d in accepted_for_group for ref in d.get("evidence_refs", [])
            }),
            "history_preserved": all(bool(d.get("preserve_history")) for d in accepted_for_group),
            "no_rename": all(bool(d.get("no_rename")) for d in accepted_for_group),
            "no_delete": all(bool(d.get("no_delete")) for d in accepted_for_group),
        }
        enriched.append(item)

    statuses = [g["semantic_review"]["status"] for g in enriched]
    reviewed = sum(s == "ROLE-ADJUDICATED" for s in statuses)
    partial = sum(s == "PARTIALLY-ROLE-ADJUDICATED" for s in statuses)
    rekey = sum(s == "ROLE-ADJUDICATED-REKEY-REQUIRED" for s in statuses)
    lineage = sum(s == "ROLE-ADJUDICATED-OPEN-LINEAGE" for s in statuses)
    unreviewed = sum(s == "UNREVIEWED" for s in statuses)
    return enriched, {
        "decisions_loaded": len(decisions),
        "decisions_accepted": len(accepted_ids),
        "accepted_decision_ids": sorted(accepted_ids),
        "decisions_rejected": rejected,
        "groups_reviewed": reviewed,
        "groups_partially_reviewed": partial,
        "groups_rekey_required": rekey,
        "groups_lineage_review_required": lineage,
        "groups_unreviewed": unreviewed,
        "groups_open": len(enriched) - reviewed,
    }


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
