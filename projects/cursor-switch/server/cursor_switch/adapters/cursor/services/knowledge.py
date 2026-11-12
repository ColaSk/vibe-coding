"""In-memory knowledge base until app-knowledge persistence lands."""

from __future__ import annotations

import json
from dataclasses import dataclass, field

from cursor_switch.runtime.domain.types import new_id


@dataclass
class KnowledgeEntry:
    id: str
    title: str
    content: str


@dataclass
class KnowledgeStore:
    entries: dict[str, KnowledgeEntry] = field(default_factory=dict)

    def list_json(self) -> bytes:
        payload = {
            "knowledgeBaseItems": [
                {"id": item.id, "title": item.title, "content": item.content}
                for item in self.entries.values()
            ]
        }
        return json.dumps(payload, separators=(",", ":")).encode("utf-8")

    def add(self, title: str, content: str) -> bytes:
        entry = KnowledgeEntry(id=new_id("kb"), title=title, content=content)
        self.entries[entry.id] = entry
        return json.dumps(
            {"id": entry.id, "title": entry.title, "content": entry.content},
            separators=(",", ":"),
        ).encode("utf-8")

    def update(self, entry_id: str, title: str, content: str) -> bytes:
        entry = self.entries.get(entry_id) or KnowledgeEntry(id=entry_id, title="", content="")
        entry.title = title
        entry.content = content
        self.entries[entry_id] = entry
        return json.dumps(
            {"id": entry.id, "title": entry.title, "content": entry.content},
            separators=(",", ":"),
        ).encode("utf-8")

    def remove(self, entry_id: str) -> bytes:
        self.entries.pop(entry_id, None)
        return b"{}"
