"""Minimal HAIF prototype: persistent local anchors and event ledger.

This is a development prototype, not a production deployment. It verifies each
SQLite write by reading the record back and checking its canonical SHA-256 hash.
It does not claim any external persistence or automatic capture of chat history.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import uuid
from contextlib import asynccontextmanager, closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


class AnchorCreate(BaseModel):
    resume_summary: str = Field(min_length=1, max_length=12000)
    open_tasks: list[str] = Field(default_factory=list)
    timezone: str = Field(default="Asia/Tehran", min_length=1, max_length=80)
    source_origin: str = Field(default="user interaction", min_length=1, max_length=500)


class EventCreate(BaseModel):
    event_type: str = Field(min_length=1, max_length=120)
    summary: str = Field(min_length=1, max_length=12000)
    anchor_id: str | None = None
    source_origin: str = Field(default="user interaction", min_length=1, max_length=500)
    user_message_time: str | None = None


def create_app(db_path: str | Path | None = None) -> FastAPI:
    configured_path = Path(
        db_path or os.environ.get("HAIF_DB_PATH", Path(__file__).parent / "data" / "haif.sqlite3")
    )

    def connect() -> sqlite3.Connection:
        app.state.db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(app.state.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def init_db() -> None:
        with closing(connect()) as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS anchors (
                    anchor_id TEXT PRIMARY KEY,
                    resume_summary TEXT NOT NULL,
                    open_tasks_json TEXT NOT NULL,
                    timezone TEXT NOT NULL,
                    source_origin TEXT NOT NULL,
                    created_at_utc TEXT NOT NULL,
                    content_sha256 TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS events (
                    event_id TEXT PRIMARY KEY,
                    anchor_id TEXT NULL REFERENCES anchors(anchor_id),
                    event_type TEXT NOT NULL,
                    summary TEXT NOT NULL,
                    source_origin TEXT NOT NULL,
                    user_message_time TEXT NULL,
                    created_at_utc TEXT NOT NULL,
                    content_sha256 TEXT NOT NULL
                );
                """
            )
            conn.commit()

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        init_db()
        yield

    app = FastAPI(
        title="HAIF Initial Prototype",
        version="0.1.0",
        description=(
            "Repository-stage prototype for interaction continuity. "
            "Local SQLite write/read-back is verified; external persistence is not claimed."
        ),
        lifespan=lifespan,
    )
    app.state.db_path = configured_path

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "service": "haif-initial-prototype",
            "status": "RUNNING",
            "persistence_scope": "LOCAL_SQLITE_ONLY",
            "external_persistence": "UNVERIFIED",
        }

    @app.post("/api/v1/anchors", status_code=status.HTTP_201_CREATED)
    def create_anchor(payload: AnchorCreate) -> dict[str, Any]:
        anchor_id = str(uuid.uuid4())
        created_at = utc_now()
        stored = {
            "anchor_id": anchor_id,
            "resume_summary": payload.resume_summary,
            "open_tasks": payload.open_tasks,
            "timezone": payload.timezone,
            "source_origin": payload.source_origin,
            "created_at_utc": created_at,
        }
        digest = sha256_json(stored)
        with closing(connect()) as conn:
            conn.execute(
                """INSERT INTO anchors
                   (anchor_id, resume_summary, open_tasks_json, timezone, source_origin,
                    created_at_utc, content_sha256)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    anchor_id,
                    payload.resume_summary,
                    json.dumps(payload.open_tasks, ensure_ascii=False),
                    payload.timezone,
                    payload.source_origin,
                    created_at,
                    digest,
                ),
            )
            conn.commit()
            row = conn.execute("SELECT * FROM anchors WHERE anchor_id = ?", (anchor_id,)).fetchone()

        if row is None:
            raise HTTPException(status_code=500, detail="READ_BACK_FAILED")
        actual = {
            "anchor_id": row["anchor_id"],
            "resume_summary": row["resume_summary"],
            "open_tasks": json.loads(row["open_tasks_json"]),
            "timezone": row["timezone"],
            "source_origin": row["source_origin"],
            "created_at_utc": row["created_at_utc"],
        }
        if sha256_json(actual) != row["content_sha256"] or row["content_sha256"] != digest:
            raise HTTPException(status_code=500, detail="READ_BACK_HASH_MISMATCH")
        return {**actual, "content_sha256": digest, "status": "WRITE_READBACK_VERIFIED"}

    @app.get("/api/v1/anchors")
    def list_anchors() -> dict[str, Any]:
        with closing(connect()) as conn:
            rows = conn.execute(
                "SELECT * FROM anchors ORDER BY created_at_utc DESC, anchor_id ASC"
            ).fetchall()
        items = []
        for row in rows:
            items.append(
                {
                    "anchor_id": row["anchor_id"],
                    "resume_summary": row["resume_summary"],
                    "open_tasks": json.loads(row["open_tasks_json"]),
                    "timezone": row["timezone"],
                    "source_origin": row["source_origin"],
                    "created_at_utc": row["created_at_utc"],
                    "content_sha256": row["content_sha256"],
                    "status": "STORED",
                }
            )
        return {"items": items, "count": len(items)}

    @app.get("/api/v1/anchors/{anchor_id}")
    def get_anchor(anchor_id: str) -> dict[str, Any]:
        with closing(connect()) as conn:
            row = conn.execute("SELECT * FROM anchors WHERE anchor_id = ?", (anchor_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="ANCHOR_NOT_FOUND")
        return {
            "anchor_id": row["anchor_id"],
            "resume_summary": row["resume_summary"],
            "open_tasks": json.loads(row["open_tasks_json"]),
            "timezone": row["timezone"],
            "source_origin": row["source_origin"],
            "created_at_utc": row["created_at_utc"],
            "content_sha256": row["content_sha256"],
            "status": "STORED_READABLE",
        }

    @app.post("/api/v1/events", status_code=status.HTTP_201_CREATED)
    def create_event(payload: EventCreate) -> dict[str, Any]:
        if payload.anchor_id:
            with closing(connect()) as conn:
                found = conn.execute(
                    "SELECT 1 FROM anchors WHERE anchor_id = ?", (payload.anchor_id,)
                ).fetchone()
            if found is None:
                raise HTTPException(status_code=404, detail="ANCHOR_NOT_FOUND")
        event_id = str(uuid.uuid4())
        created_at = utc_now()
        stored = {
            "event_id": event_id,
            "anchor_id": payload.anchor_id,
            "event_type": payload.event_type,
            "summary": payload.summary,
            "source_origin": payload.source_origin,
            "user_message_time": payload.user_message_time,
            "created_at_utc": created_at,
        }
        digest = sha256_json(stored)
        with closing(connect()) as conn:
            conn.execute(
                """INSERT INTO events
                   (event_id, anchor_id, event_type, summary, source_origin,
                    user_message_time, created_at_utc, content_sha256)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    event_id,
                    payload.anchor_id,
                    payload.event_type,
                    payload.summary,
                    payload.source_origin,
                    payload.user_message_time,
                    created_at,
                    digest,
                ),
            )
            conn.commit()
            row = conn.execute("SELECT * FROM events WHERE event_id = ?", (event_id,)).fetchone()

        if row is None:
            raise HTTPException(status_code=500, detail="READ_BACK_FAILED")
        actual = {
            "event_id": row["event_id"],
            "anchor_id": row["anchor_id"],
            "event_type": row["event_type"],
            "summary": row["summary"],
            "source_origin": row["source_origin"],
            "user_message_time": row["user_message_time"],
            "created_at_utc": row["created_at_utc"],
        }
        if sha256_json(actual) != row["content_sha256"] or row["content_sha256"] != digest:
            raise HTTPException(status_code=500, detail="READ_BACK_HASH_MISMATCH")
        return {**actual, "content_sha256": digest, "status": "WRITE_READBACK_VERIFIED"}

    @app.get("/api/v1/events/{event_id}")
    def get_event(event_id: str) -> dict[str, Any]:
        with closing(connect()) as conn:
            row = conn.execute("SELECT * FROM events WHERE event_id = ?", (event_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="EVENT_NOT_FOUND")
        return {
            "event_id": row["event_id"],
            "anchor_id": row["anchor_id"],
            "event_type": row["event_type"],
            "summary": row["summary"],
            "source_origin": row["source_origin"],
            "user_message_time": row["user_message_time"],
            "created_at_utc": row["created_at_utc"],
            "content_sha256": row["content_sha256"],
            "status": "STORED_READABLE",
        }

    return app


app = create_app()
