"""Guards for Cursor RunInference local_loop: tool thrash and history hygiene."""

from __future__ import annotations

import json
from typing import Any

from cursor_switch.runtime.domain.types import Message, MessageRole, ToolCall


def tool_call_fingerprint(call: ToolCall) -> str:
    args = json.dumps(call.arguments or {}, ensure_ascii=False, sort_keys=True, default=str)
    return f"{call.name}:{args}"


def repeated_tool_loop(messages: list[Message], *, threshold: int = 3) -> bool:
    """True when the last `threshold` assistant tool calls are identical."""
    fingerprints: list[str] = []
    for message in messages:
        if message.role is not MessageRole.ASSISTANT:
            continue
        for call in message.tool_calls:
            fingerprints.append(tool_call_fingerprint(call))
    if len(fingerprints) < threshold:
        return False
    window = fingerprints[-threshold:]
    return len(set(window)) == 1


def _blank_tool_content(content: str) -> bool:
    text = (content or "").strip()
    return not text or text == "[empty tool result]"


def empty_tool_result_streak(messages: list[Message], *, threshold: int = 3) -> bool:
    """True when recent tool results are empty — usually a decode miss."""
    results = [m for m in messages if m.role is MessageRole.TOOL]
    if len(results) < threshold:
        return False
    return all(_blank_tool_content(m.content) for m in results[-threshold:])


def history_summary(messages: list[Message]) -> list[dict[str, Any]]:
    """Compact log-friendly view of invoke history."""
    out: list[dict[str, Any]] = []
    for message in messages:
        item: dict[str, Any] = {
            "role": message.role.value,
            "content_len": len(message.content or ""),
        }
        if message.tool_call_id:
            item["tool_call_id"] = message.tool_call_id
        if message.tool_calls:
            item["tool_calls"] = [
                {"id": c.id, "name": c.name, "args": c.arguments} for c in message.tool_calls
            ]
        out.append(item)
    return out


# Browser/MCP tool blobs routinely exceed 10–20KB and inflate each RI invoke to
# hundreds of KB, which slows upstream models and makes Cursor abandon the WS.
DEFAULT_TOOL_CONTENT_LIMIT = 12_000
DEFAULT_USER_CONTENT_LIMIT = 48_000


def truncate_message_content(content: str, *, limit: int = DEFAULT_TOOL_CONTENT_LIMIT) -> str:
    """Keep head+tail of oversized tool/user blobs for upstream context."""
    text = content or ""
    if limit <= 0 or len(text) <= limit:
        return text
    marker = f"\n…[truncated {len(text) - limit} chars]…\n"
    keep = max(0, limit - len(marker))
    head = keep // 2
    tail = keep - head
    return text[:head] + marker + text[-tail:]
