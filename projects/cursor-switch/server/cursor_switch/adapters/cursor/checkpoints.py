"""CheckpointPort implementations for conversation recovery."""

from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import DateTime, String, Text, func, select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from cursor_switch.runtime.domain.types import ConversationId, Message, MessageRole


class MemoryCheckpoints:
    def __init__(self) -> None:
        self._saved: dict[ConversationId, list[Message]] = {}

    async def save(self, conversation_id: ConversationId, messages: list[Message]) -> None:
        self._saved[conversation_id] = list(messages)

    async def restore(self, conversation_id: ConversationId) -> list[Message]:
        return list(self._saved.get(conversation_id, []))


class _Base(DeclarativeBase):
    pass


class CheckpointRow(_Base):
    __tablename__ = "conversation_checkpoints"

    conversation_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    messages_json: Mapped[str] = mapped_column(Text, default="[]")
    updated_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now())


def _default_checkpoint_url() -> str:
    root = Path.home() / ".cursor-switch"
    root.mkdir(parents=True, exist_ok=True)
    return f"sqlite+aiosqlite:///{root / 'checkpoints.db'}"


class SqliteCheckpoints:
    """Persist conversation messages for restart / resume."""

    def __init__(self, database_url: str | None = None, engine: AsyncEngine | None = None) -> None:
        self._engine = engine or create_async_engine(database_url or _default_checkpoint_url())
        self._owns_engine = engine is None
        self._sessions = async_sessionmaker(self._engine, expire_on_commit=False)
        self._ready = False

    async def _ensure(self) -> None:
        if self._ready:
            return
        async with self._engine.begin() as conn:
            await conn.run_sync(_Base.metadata.create_all)
        self._ready = True

    async def save(self, conversation_id: ConversationId, messages: list[Message]) -> None:
        await self._ensure()
        payload = json.dumps(
            [
                {
                    "id": m.id,
                    "role": m.role.value,
                    "content": m.content,
                    "tool_call_id": m.tool_call_id,
                    "tool_calls": [
                        {"id": c.id, "name": c.name, "arguments": c.arguments}
                        for c in m.tool_calls
                    ],
                }
                for m in messages
            ],
            separators=(",", ":"),
        )
        async with self._sessions() as session:
            row = await session.get(CheckpointRow, conversation_id)
            if row is None:
                session.add(CheckpointRow(conversation_id=conversation_id, messages_json=payload))
            else:
                row.messages_json = payload
            await session.commit()

    async def restore(self, conversation_id: ConversationId) -> list[Message]:
        await self._ensure()
        async with self._sessions() as session:
            row = await session.get(CheckpointRow, conversation_id)
            if row is None:
                return []
            raw = json.loads(row.messages_json or "[]")
        out: list[Message] = []
        for item in raw:
            try:
                role = MessageRole(str(item.get("role") or "user"))
            except ValueError:
                role = MessageRole.USER
            from cursor_switch.runtime.domain.types import ToolCall

            tool_calls = []
            for call in item.get("tool_calls") or []:
                if not isinstance(call, dict):
                    continue
                tool_calls.append(
                    ToolCall(
                        id=str(call.get("id") or ""),
                        name=str(call.get("name") or ""),
                        arguments=call.get("arguments")
                        if isinstance(call.get("arguments"), dict)
                        else {},
                    )
                )
            out.append(
                Message(
                    id=str(item.get("id") or ""),
                    role=role,
                    content=str(item.get("content") or ""),
                    tool_call_id=item.get("tool_call_id"),
                    tool_calls=tuple(tool_calls),
                )
            )
        return out

    async def dispose(self) -> None:
        if self._owns_engine:
            await self._engine.dispose()
