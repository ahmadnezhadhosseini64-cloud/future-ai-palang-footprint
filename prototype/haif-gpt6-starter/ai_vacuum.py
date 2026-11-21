#!/usr/bin/env python3
"""Evidence-only AI Vacuum interval helpers. Never records private model reasoning."""
from __future__ import annotations
from datetime import datetime
from typing import Any

FORBIDDEN_KEYS = {"chain_of_thought", "private_reasoning", "scratchpad", "hidden_prompt", "internal_deliberation"}

def _parse(anchor: dict[str, Any]) -> datetime | None:
    value = anchor.get("timestamp")
    if not value or anchor.get("status") != "OBSERVED":
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("anchor timestamp must include an explicit UTC offset")
    return parsed

def compute_interval(stop_anchor: dict[str, Any], thinking_start_anchor: dict[str, Any]) -> dict[str, Any]:
    if stop_anchor.get("event") != "STOP" or thinking_start_anchor.get("event") != "THINKING_START":
        raise ValueError("anchor event labels do not match")
    start = _parse(stop_anchor)
    end = _parse(thinking_start_anchor)
    if start is None or end is None:
        return {"status": "UNMEASURABLE", "duration_ms": None, "reason": "one or both anchors are not observed"}
    if stop_anchor.get("clock_source") != thinking_start_anchor.get("clock_source"):
        return {"status": "CLOCK_CONFLICT", "duration_ms": None, "reason": "anchor clock sources differ; synchronization evidence required"}
    delta_ms = int((end - start).total_seconds() * 1000)
    if delta_ms < 0:
        return {"status": "CLOCK_CONFLICT", "duration_ms": None, "reason": "thinking start precedes stop"}
    return {"status": "MEASURABLE", "duration_ms": delta_ms, "reason": None}

def validate_behavior_event(event: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if any(str(key).lower() in FORBIDDEN_KEYS for key in event):
        errors.append("private reasoning fields are forbidden")
    if not event.get("event_type"):
        errors.append("event_type is required")
    if "timestamp" not in event:
        errors.append("timestamp field is required; use null when unavailable")
    return errors
