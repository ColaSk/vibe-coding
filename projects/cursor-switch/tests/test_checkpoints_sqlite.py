"""SQLite checkpoint save/restore."""

from __future__ import annotations

import pytest

from cursor_switch.adapters.cursor.checkpoints import SqliteCheckpoints
from cursor_switch.runtime.domain.types import Message, MessageRole


@pytest.mark.asyncio
async def test_sqlite_checkpoint_roundtrip(tmp_path) -> None:
    db = tmp_path / "cp.db"
    store = SqliteCheckpoints(f"sqlite+aiosqlite:///{db}")
    messages = [
        Message(id="1", role=MessageRole.USER, content="hi"),
        Message(id="2", role=MessageRole.ASSISTANT, content="hello"),
    ]
    await store.save("conv-a", messages)
    restored = await store.restore("conv-a")
    assert len(restored) == 2
    assert restored[0].content == "hi"
    assert restored[1].role is MessageRole.ASSISTANT
    assert await store.restore("missing") == []
    await store.dispose()
