"""Tool dispatcher and local search index."""

from __future__ import annotations

from pathlib import Path

from cursor_switch.adapters.search.index import CodeSearchIndex
from cursor_switch.adapters.tools.catalog import tools_for_mode
from cursor_switch.adapters.tools.dispatch import ToolDispatcher
from cursor_switch.adapters.tools.handlers import default_handlers
from cursor_switch.runtime.domain.types import ToolCall, new_id


def test_mode_tool_lists() -> None:
    agent = set(tools_for_mode("agent"))
    ask = set(tools_for_mode("ask"))
    assert "Write" in agent
    assert "Write" not in ask
    assert "Read" in ask


async def test_read_write_roundtrip(tmp_path: Path) -> None:
    target = tmp_path / "note.txt"
    tools = ToolDispatcher(handlers=default_handlers())
    write = await tools.dispatch(
        ToolCall(
            id=new_id("tc"),
            name="Write",
            arguments={"path": str(target), "contents": "hello tools"},
        )
    )
    assert (await write.result()).is_error is False
    read = await tools.dispatch(
        ToolCall(id=new_id("tc"), name="Read", arguments={"path": str(target)})
    )
    result = await read.result()
    assert result.content == "hello tools"


async def test_ask_mode_blocks_write(tmp_path: Path) -> None:
    tools = ToolDispatcher(mode="ask")
    handle = await tools.dispatch(
        ToolCall(
            id=new_id("tc"),
            name="Write",
            arguments={"path": str(tmp_path / "x.txt"), "contents": "nope"},
        )
    )
    result = await handle.result()
    assert result.is_error
    assert "not available" in result.content


async def test_code_search_index(tmp_path: Path) -> None:
    src = tmp_path / "sample.py"
    src.write_text("def greet(name):\n    return f'hi {name}'\n", encoding="utf-8")
    index = CodeSearchIndex(f"sqlite+aiosqlite:///{tmp_path / 'search.db'}")
    await index.init()
    indexed = await index.index_tree(tmp_path, glob="**/*.py")
    assert indexed >= 1
    hits = await index.search("greet")
    assert hits
    assert hits[0].path.endswith("sample.py")
    await index.dispose()
