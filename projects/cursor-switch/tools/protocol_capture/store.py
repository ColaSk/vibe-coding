"""SQLite storage for captured Cursor exchanges."""

from __future__ import annotations

import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Exchange:
    id: int
    created_at: float
    method: str
    path: str
    request_headers: str
    request_body: bytes
    status_code: int
    response_headers: str
    response_body: bytes


class CaptureStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS exchanges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at REAL NOT NULL,
                method TEXT NOT NULL,
                path TEXT NOT NULL,
                request_headers TEXT NOT NULL,
                request_body BLOB NOT NULL,
                status_code INTEGER NOT NULL,
                response_headers TEXT NOT NULL,
                response_body BLOB NOT NULL
            )
            """
        )
        self._conn.commit()

    def add(
        self,
        *,
        method: str,
        path: str,
        request_headers: str,
        request_body: bytes,
        status_code: int,
        response_headers: str,
        response_body: bytes,
    ) -> int:
        cursor = self._conn.execute(
            """
            INSERT INTO exchanges(
                created_at, method, path, request_headers, request_body,
                status_code, response_headers, response_body
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                time.time(),
                method,
                path,
                request_headers,
                request_body,
                status_code,
                response_headers,
                response_body,
            ),
        )
        self._conn.commit()
        return int(cursor.lastrowid)

    def list(self, *, limit: int = 100) -> list[Exchange]:
        rows = self._conn.execute(
            """
            SELECT * FROM exchanges
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [self._row(row) for row in rows]

    def get(self, exchange_id: int) -> Exchange | None:
        row = self._conn.execute(
            "SELECT * FROM exchanges WHERE id = ?",
            (exchange_id,),
        ).fetchone()
        return None if row is None else self._row(row)

    def close(self) -> None:
        self._conn.close()

    @staticmethod
    def _row(row: sqlite3.Row) -> Exchange:
        return Exchange(
            id=int(row["id"]),
            created_at=float(row["created_at"]),
            method=str(row["method"]),
            path=str(row["path"]),
            request_headers=str(row["request_headers"]),
            request_body=bytes(row["request_body"] or b""),
            status_code=int(row["status_code"]),
            response_headers=str(row["response_headers"]),
            response_body=bytes(row["response_body"] or b""),
        )
