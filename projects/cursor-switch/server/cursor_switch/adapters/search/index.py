"""Local code search index: line-based chunks + SQLite FTS."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


_TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]{1,}")


@dataclass(frozen=True, slots=True)
class SearchHit:
    path: str
    start_line: int
    end_line: int
    snippet: str
    score: float


class CodeSearchIndex:
    def __init__(self, database_url: str = "sqlite+aiosqlite:///:memory:") -> None:
        self._engine: AsyncEngine = create_async_engine(database_url)

    async def init(self) -> None:
        async with self._engine.begin() as conn:
            await conn.execute(
                text(
                    """
                    CREATE VIRTUAL TABLE IF NOT EXISTS code_chunks USING fts5(
                        path,
                        start_line UNINDEXED,
                        end_line UNINDEXED,
                        body,
                        tokenize = 'porter'
                    )
                    """
                )
            )

    async def index_tree(self, root: Path, *, glob: str = "**/*.{py,ts,tsx,js,rs,go,md}") -> int:
        root = root.resolve()
        # Expand a simple brace glob into multiple patterns.
        patterns = _expand_brace_glob(glob)
        files: list[Path] = []
        for pattern in patterns:
            files.extend(p for p in root.glob(pattern) if p.is_file())
        count = 0
        async with self._engine.begin() as conn:
            await conn.execute(text("DELETE FROM code_chunks"))
            for path in sorted(set(files)):
                try:
                    text_body = path.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
                for start, end, chunk in _chunk_lines(text_body):
                    await conn.execute(
                        text(
                            "INSERT INTO code_chunks(path, start_line, end_line, body) "
                            "VALUES (:path, :start_line, :end_line, :body)"
                        ),
                        {
                            "path": str(path.relative_to(root)),
                            "start_line": start,
                            "end_line": end,
                            "body": chunk,
                        },
                    )
                    count += 1
        return count

    async def search(self, query: str, *, limit: int = 20) -> list[SearchHit]:
        tokens = _TOKEN.findall(query)
        if not tokens:
            return []
        match = " ".join(tokens)
        async with self._engine.connect() as conn:
            rows = (
                await conn.execute(
                    text(
                        """
                        SELECT path, start_line, end_line, body,
                               bm25(code_chunks) AS score
                        FROM code_chunks
                        WHERE code_chunks MATCH :match
                        ORDER BY score
                        LIMIT :limit
                        """
                    ),
                    {"match": match, "limit": limit},
                )
            ).all()
        return [
            SearchHit(
                path=row.path,
                start_line=int(row.start_line),
                end_line=int(row.end_line),
                snippet=row.body[:500],
                score=float(row.score),
            )
            for row in rows
        ]

    async def dispose(self) -> None:
        await self._engine.dispose()


def _chunk_lines(text_body: str, *, size: int = 40, overlap: int = 5) -> list[tuple[int, int, str]]:
    lines = text_body.splitlines()
    if not lines:
        return []
    chunks: list[tuple[int, int, str]] = []
    step = max(size - overlap, 1)
    for start in range(0, len(lines), step):
        end = min(start + size, len(lines))
        chunk = "\n".join(lines[start:end])
        chunks.append((start + 1, end, chunk))
        if end >= len(lines):
            break
    return chunks


def _expand_brace_glob(pattern: str) -> list[str]:
    if "{" not in pattern or "}" not in pattern:
        return [pattern]
    prefix, rest = pattern.split("{", 1)
    body, suffix = rest.split("}", 1)
    return [f"{prefix}{part}{suffix}" for part in body.split(",")]
