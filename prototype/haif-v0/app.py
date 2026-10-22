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

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from jsonschema import Draft202012Validator


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


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    source_path: str = Field(min_length=1, max_length=2000)
    version: str = Field(default="1.0.0", min_length=1, max_length=80)
    content: str = Field(min_length=1, max_length=200000)
    source_origin: str = Field(default="repository document", min_length=1, max_length=500)


class InteractionPairCreate(BaseModel):
    interaction_id: str = Field(pattern=r"^INT-[0-9]{8}-[0-9]{3}$")
    input_id: str = Field(pattern=r"^IN-[0-9]{8}-[0-9]{3}$")
    output_id: str = Field(pattern=r"^OUT-[0-9]{8}-[0-9]{3}$")
    sequence: int = Field(ge=1)
    version: str = Field(pattern=r"^[0-9]+\\.[0-9]+\\.[0-9]+$")
    status: str = Field(pattern=r"^(DRAFT|OBSERVED|VALIDATED|REGISTERED|AMENDED|REJECTED)$")
    time_evidence: dict[str, Any]
    input: dict[str, Any]
    output: dict[str, Any]
    behavior_analysis: list[dict[str, Any]]
    lineage: dict[str, Any]
    verification: dict[str, Any]


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
                CREATE TABLE IF NOT EXISTS documents (
                    document_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    source_path TEXT NOT NULL,
                    version TEXT NOT NULL,
                    content TEXT NOT NULL,
                    source_origin TEXT NOT NULL,
                    created_at_utc TEXT NOT NULL,
                    content_sha256 TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS interaction_pairs (
                    interaction_id TEXT PRIMARY KEY,
                    input_id TEXT NOT NULL UNIQUE,
                    output_id TEXT NOT NULL UNIQUE,
                    sequence INTEGER NOT NULL,
                    record_json TEXT NOT NULL,
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

    @app.post("/api/v1/documents", status_code=status.HTTP_201_CREATED)
    def ingest_document(payload: DocumentCreate) -> dict[str, Any]:
        document_id = str(uuid.uuid4())
        created_at = utc_now()
        stored = {
            "document_id": document_id,
            "title": payload.title,
            "source_path": payload.source_path,
            "version": payload.version,
            "content": payload.content,
            "source_origin": payload.source_origin,
            "created_at_utc": created_at,
        }
        digest = sha256_json(stored)
        with closing(connect()) as conn:
            conn.execute(
                """INSERT INTO documents
                   (document_id, title, source_path, version, content, source_origin,
                    created_at_utc, content_sha256)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (document_id, payload.title, payload.source_path, payload.version,
                 payload.content, payload.source_origin, created_at, digest),
            )
            conn.commit()
            row = conn.execute("SELECT * FROM documents WHERE document_id = ?", (document_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=500, detail="READ_BACK_FAILED")
        actual = {
            "document_id": row["document_id"], "title": row["title"],
            "source_path": row["source_path"], "version": row["version"],
            "content": row["content"], "source_origin": row["source_origin"],
            "created_at_utc": row["created_at_utc"],
        }
        if sha256_json(actual) != row["content_sha256"] or row["content_sha256"] != digest:
            raise HTTPException(status_code=500, detail="READ_BACK_HASH_MISMATCH")
        return {**actual, "content_sha256": digest, "status": "WRITE_READBACK_VERIFIED"}

    def validate_interaction_record(record: dict[str, Any]) -> None:
        schema_path = Path(__file__).resolve().parents[2] / "docs" / "architecture" / "BEHAVIOR-TRACE" / "interaction-pair-ledger.schema.json"
        if not schema_path.is_file():
            raise HTTPException(status_code=503, detail="INTERACTION_SCHEMA_UNAVAILABLE")
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER).validate(record)
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(status_code=422, detail={"error": "INTERACTION_SCHEMA_VALIDATION_FAILED", "reason": str(exc)[:500]}) from exc

    @app.post("/api/v1/interactions", status_code=status.HTTP_201_CREATED)
    def create_interaction_pair(payload: InteractionPairCreate) -> dict[str, Any]:
        record = payload.model_dump()
        suffixes = [record["interaction_id"].split("-", 1)[1], record["input_id"].split("-", 1)[1], record["output_id"].split("-", 1)[1]]
        if len(set(suffixes)) != 1 or record["sequence"] != int(record["interaction_id"].rsplit("-", 1)[1]):
            raise HTTPException(status_code=422, detail="INTERACTION_ID_PAIR_MISMATCH")
        validate_interaction_record(record)
        record_text = canonical_json(record)
        digest = sha256_json(record)
        with closing(connect()) as conn:
            existing = conn.execute(
                "SELECT * FROM interaction_pairs WHERE interaction_id = ? OR input_id = ? OR output_id = ?",
                (record["interaction_id"], record["input_id"], record["output_id"]),
            ).fetchone()
            if existing is not None:
                if (existing["interaction_id"] == record["interaction_id"] and
                    existing["input_id"] == record["input_id"] and
                    existing["output_id"] == record["output_id"] and
                    existing["record_json"] == record_text and
                    existing["content_sha256"] == digest):
                    return {**record, "created_at_utc": existing["created_at_utc"], "content_sha256": digest, "status": "IDEMPOTENT_REPLAY_READBACK_VERIFIED"}
                raise HTTPException(status_code=409, detail="INTERACTION_ID_CONFLICT")
            created_at = utc_now()
            conn.execute(
                "INSERT INTO interaction_pairs (interaction_id, input_id, output_id, sequence, record_json, created_at_utc, content_sha256) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (record["interaction_id"], record["input_id"], record["output_id"], record["sequence"], record_text, created_at, digest),
            )
            conn.commit()
            row = conn.execute("SELECT * FROM interaction_pairs WHERE interaction_id = ?", (record["interaction_id"],)).fetchone()
        if row is None:
            raise HTTPException(status_code=500, detail="INTERACTION_READ_BACK_FAILED")
        stored = json.loads(row["record_json"])
        if canonical_json(stored) != record_text or sha256_json(stored) != row["content_sha256"] or row["content_sha256"] != digest:
            raise HTTPException(status_code=500, detail="INTERACTION_READ_BACK_HASH_MISMATCH")
        return {**stored, "created_at_utc": row["created_at_utc"], "content_sha256": digest, "status": "WRITE_READBACK_VERIFIED"}

    @app.get("/api/v1/interactions/{lookup_id}")
    def get_interaction_pair(lookup_id: str) -> dict[str, Any]:
        with closing(connect()) as conn:
            row = conn.execute(
                "SELECT * FROM interaction_pairs WHERE interaction_id = ? OR input_id = ? OR output_id = ?",
                (lookup_id, lookup_id, lookup_id),
            ).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="INTERACTION_NOT_FOUND")
        record = json.loads(row["record_json"])
        if sha256_json(record) != row["content_sha256"]:
            raise HTTPException(status_code=500, detail="INTERACTION_HASH_MISMATCH")
        return {**record, "created_at_utc": row["created_at_utc"], "content_sha256": row["content_sha256"], "status": "STORED_READBACK_VERIFIED"}

    @app.get("/api/v1/search")
    def search_documents(q: str = Query(min_length=1, max_length=200)) -> dict[str, Any]:
        term = q.strip().casefold()
        if not term:
            raise HTTPException(status_code=422, detail="SEARCH_QUERY_REQUIRED")
        with closing(connect()) as conn:
            rows = conn.execute(
                """SELECT document_id, title, source_path, version, source_origin,
                          created_at_utc, content_sha256, content
                   FROM documents ORDER BY created_at_utc DESC, document_id ASC"""
            ).fetchall()
        matches = []
        for row in rows:
            if term in row["title"].casefold() or term in row["content"].casefold():
                matches.append({
                    "document_id": row["document_id"], "title": row["title"],
                    "source_path": row["source_path"], "version": row["version"],
                    "source_origin": row["source_origin"], "created_at_utc": row["created_at_utc"],
                    "content_sha256": row["content_sha256"],
                    "excerpt": row["content"][:500], "retrieval_method": "CASEFOLD_SUBSTRING",
                })
        return {"query": q, "items": matches, "count": len(matches),
                "status": "RETRIEVED_WITH_PROVENANCE"}

    return app


app = create_app()
