"""Concrete tool handlers. Phase 6 starts with safe local stubs / httpx fetch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Protocol

import httpx

from cursor_switch.runtime.domain.types import ToolCall, ToolResult


class ToolHandler(Protocol):
    async def run(self, call: ToolCall) -> ToolResult: ...


class EchoHandler:
    """Fallback for not-yet-wired tools."""

    async def run(self, call: ToolCall) -> ToolResult:
        return ToolResult(
            tool_call_id=call.id,
            content=json.dumps(
                {"ok": False, "error": f"handler not implemented: {call.name}"},
                separators=(",", ":"),
            ),
            is_error=True,
        )


class ReadFileHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        path = Path(str(call.arguments.get("path") or ""))
        if not path.is_file():
            return ToolResult(
                tool_call_id=call.id,
                content=f"file not found: {path}",
                is_error=True,
            )
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            return ToolResult(tool_call_id=call.id, content=str(exc), is_error=True)
        limit = int(call.arguments.get("limit") or 0)
        if limit > 0:
            lines = text.splitlines()
            text = "\n".join(lines[:limit])
        return ToolResult(tool_call_id=call.id, content=text)


class GlobHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        pattern = str(call.arguments.get("glob_pattern") or call.arguments.get("pattern") or "*")
        root = Path(str(call.arguments.get("target_directory") or ".")).resolve()
        matches = sorted(str(p) for p in root.glob(pattern) if p.is_file())[:500]
        return ToolResult(tool_call_id=call.id, content="\n".join(matches))


class GrepHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        pattern = str(call.arguments.get("pattern") or "")
        root = Path(str(call.arguments.get("path") or ".")).resolve()
        if not pattern:
            return ToolResult(tool_call_id=call.id, content="pattern required", is_error=True)
        hits: list[str] = []
        files = [root] if root.is_file() else list(root.rglob("*"))
        for path in files:
            if not path.is_file():
                continue
            try:
                for lineno, line in enumerate(
                    path.read_text(encoding="utf-8", errors="ignore").splitlines(),
                    start=1,
                ):
                    if pattern in line:
                        hits.append(f"{path}:{lineno}:{line}")
                        if len(hits) >= 200:
                            break
            except OSError:
                continue
            if len(hits) >= 200:
                break
        return ToolResult(tool_call_id=call.id, content="\n".join(hits))


class WriteFileHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        path = Path(str(call.arguments.get("path") or ""))
        contents = str(call.arguments.get("contents") or "")
        if not path.parts:
            return ToolResult(tool_call_id=call.id, content="path required", is_error=True)
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(contents, encoding="utf-8")
        except OSError as exc:
            return ToolResult(tool_call_id=call.id, content=str(exc), is_error=True)
        return ToolResult(tool_call_id=call.id, content=f"wrote {path}")


class StrReplaceHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        path = Path(str(call.arguments.get("path") or ""))
        old = str(call.arguments.get("old_string") or "")
        new = str(call.arguments.get("new_string") or "")
        if not path.is_file():
            return ToolResult(tool_call_id=call.id, content=f"file not found: {path}", is_error=True)
        text = path.read_text(encoding="utf-8")
        if old not in text:
            return ToolResult(tool_call_id=call.id, content="old_string not found", is_error=True)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return ToolResult(tool_call_id=call.id, content=f"updated {path}")


class DeleteFileHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        path = Path(str(call.arguments.get("path") or ""))
        if not path.exists():
            return ToolResult(tool_call_id=call.id, content=f"missing: {path}", is_error=True)
        path.unlink()
        return ToolResult(tool_call_id=call.id, content=f"deleted {path}")


class ShellHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        # Intentionally deferred: shell execution needs sandbox policy in Phase 6 polish.
        return ToolResult(
            tool_call_id=call.id,
            content="Shell handler reserved; not enabled yet",
            is_error=True,
        )


class WebFetchHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        url = str(call.arguments.get("url") or "")
        if not url.startswith(("http://", "https://")):
            return ToolResult(tool_call_id=call.id, content="invalid url", is_error=True)
        try:
            async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
                response = await client.get(url)
            text = response.text[:100_000]
            return ToolResult(
                tool_call_id=call.id,
                content=json.dumps(
                    {"status": response.status_code, "body": text},
                    separators=(",", ":"),
                ),
            )
        except httpx.HTTPError as exc:
            return ToolResult(tool_call_id=call.id, content=str(exc), is_error=True)


class WebSearchHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        query = str(call.arguments.get("search_term") or call.arguments.get("query") or "")
        return ToolResult(
            tool_call_id=call.id,
            content=json.dumps(
                {"query": query, "results": [], "note": "configure search provider"},
                separators=(",", ":"),
            ),
        )


class LocalSearchHandler:
    def __init__(self, search_index: Any | None = None) -> None:
        self._index = search_index

    async def run(self, call: ToolCall) -> ToolResult:
        if self._index is None:
            return ToolResult(
                tool_call_id=call.id,
                content="local search index is not configured",
                is_error=True,
            )
        query = str(call.arguments.get("query") or call.arguments.get("search_term") or "")
        hits = await self._index.search(query)
        payload = [
            {
                "path": hit.path,
                "start_line": hit.start_line,
                "end_line": hit.end_line,
                "snippet": hit.snippet,
                "score": hit.score,
            }
            for hit in hits
        ]
        return ToolResult(
            tool_call_id=call.id,
            content=json.dumps({"results": payload}, separators=(",", ":")),
        )


class TodoWriteHandler:
    async def run(self, call: ToolCall) -> ToolResult:
        todos: Any = call.arguments.get("todos") or []
        return ToolResult(
            tool_call_id=call.id,
            content=json.dumps({"ok": True, "todos": todos}, separators=(",", ":")),
        )


def default_handlers(*, search_index: Any | None = None) -> dict[str, ToolHandler]:
    local = LocalSearchHandler(search_index)
    return {
        "Read": ReadFileHandler(),
        "Glob": GlobHandler(),
        "Grep": GrepHandler(),
        "Write": WriteFileHandler(),
        "StrReplace": StrReplaceHandler(),
        "Delete": DeleteFileHandler(),
        "Shell": ShellHandler(),
        "WebFetch": WebFetchHandler(),
        "WebSearch": WebSearchHandler(),
        "TodoWrite": TodoWriteHandler(),
        "SembleSearch": local,
        "SembleFindRelated": local,
    }
