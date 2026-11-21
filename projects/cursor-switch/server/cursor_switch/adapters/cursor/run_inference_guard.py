"""Guards for Cursor RunInference local_loop: tool thrash and history hygiene."""

from __future__ import annotations

import json
from dataclasses import replace
from typing import Any

from cursor_switch.runtime.domain.types import Message, MessageRole, ToolCall


def tool_parameter_schemas(tools: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Name → JSON Schema parameters for tools actually sent upstream."""
    schemas: dict[str, dict[str, Any]] = {}
    for tool in tools:
        if not isinstance(tool, dict):
            continue
        function = tool.get("function", tool)
        if not isinstance(function, dict):
            continue
        name = function.get("name")
        parameters = function.get("parameters")
        if name and isinstance(parameters, dict):
            schemas[str(name)] = parameters
    return schemas


def reject_tool_call(call: ToolCall, schemas: dict[str, dict[str, Any]]) -> str | None:
    """Why this call must not be sent to Cursor, or None when it is safe.

    Cursor aborts the agent websocket when it receives a tool call it cannot
    execute: an unadvertised name, or a call missing required arguments.
    """
    schema = schemas.get(call.name)
    if schema is None:
        return (
            f"Tool {call.name!r} is not available. "
            "Call only tools from the current tool list, with their required arguments."
        )
    arguments = call.arguments if isinstance(call.arguments, dict) else None
    if arguments is None:
        return f"Tool {call.name!r} arguments must be an object."
    required = schema.get("required") or []
    if not isinstance(required, list):
        return None
    missing = [
        str(name)
        for name in required
        if name not in arguments or arguments.get(name) in (None, "", [], {})
    ]
    if missing:
        return f"Tool {call.name!r} is missing required arguments: {', '.join(missing)}."
    return None


def tool_call_fingerprint(call: ToolCall) -> str:
    args = json.dumps(call.arguments or {}, ensure_ascii=False, sort_keys=True, default=str)
    return f"{call.name}:{args}"


def _since_last_user(messages: list[Message]) -> list[Message]:
    """Messages after the latest user turn. A resubmit must not inherit an old loop."""
    last_user = -1
    for index, message in enumerate(messages):
        if message.role is MessageRole.USER:
            last_user = index
    if last_user < 0:
        return messages
    return messages[last_user + 1 :]


def repeated_tool_loop(messages: list[Message], *, threshold: int = 3) -> bool:
    """True when the last `threshold` assistant tool calls in this user turn are identical."""
    fingerprints: list[str] = []
    for message in _since_last_user(messages):
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
    results = [m for m in _since_last_user(messages) if m.role is MessageRole.TOOL]
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


def compact_tool_history(
    messages: list[Message],
    *,
    keep_recent: int = 4,
    limit: int = 1_500,
) -> list[Message]:
    """Shrink older tool results so a long agent run stays small enough to finish.

    Cursor closes the run websocket when an invoke grows to hundreds of KB and
    the model round-trip outlasts the client.
    """
    tool_indexes = [index for index, message in enumerate(messages) if message.role is MessageRole.TOOL]
    stale = set(tool_indexes[:-keep_recent])
    if not stale:
        return messages
    compacted: list[Message] = []
    for index, message in enumerate(messages):
        if index in stale and len(message.content or "") > limit:
            compacted.append(
                replace(
                    message,
                    content=truncate_message_content(message.content, limit=limit),
                )
            )
        else:
            compacted.append(message)
    return compacted


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
