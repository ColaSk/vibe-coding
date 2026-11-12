"""Anthropic Messages strategy."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any

import httpx

from cursor_switch.adapters.providers.base import (
    ProviderConfig,
    end_event,
    error_event,
    iter_sse_json,
    merge_extra,
    resolve_endpoint,
    text_event,
)
from cursor_switch.runtime.domain.types import (
    Message,
    MessageRole,
    ModelEvent,
    ModelEventKind,
    ToolCall,
    Usage,
)
from cursor_switch.runtime.ports.model import ModelInvocation


def _split_system(messages: list[Message]) -> tuple[str | None, list[dict[str, Any]]]:
    system_parts: list[str] = []
    body: list[dict[str, Any]] = []
    for message in messages:
        if message.role is MessageRole.SYSTEM:
            system_parts.append(message.content)
            continue
        if message.role is MessageRole.TOOL:
            body.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": message.tool_call_id or "",
                            "content": message.content,
                        }
                    ],
                }
            )
            continue
        role = "user" if message.role is MessageRole.USER else "assistant"
        body.append({"role": role, "content": message.content})
    system = "\n\n".join(system_parts) if system_parts else None
    return system, body


class AnthropicMessagesStrategy:
    def __init__(self, config: ProviderConfig, client: httpx.AsyncClient | None = None) -> None:
        self._config = config
        self._client = client

    async def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        system, messages = _split_system(invocation.messages)
        body: dict[str, Any] = {
            "model": self._config.model_name,
            "messages": messages,
            "stream": True,
            "max_tokens": 4096,
        }
        if system:
            body["system"] = system
        if invocation.tools:
            body["tools"] = [
                {
                    "name": tool.get("function", tool).get("name", tool.get("name")),
                    "description": tool.get("function", tool).get("description", ""),
                    "input_schema": tool.get("function", tool).get("parameters", {}),
                }
                for tool in invocation.tools
            ]
        merge_extra(body, {**self._config.extra, **invocation.extra})
        url = resolve_endpoint(self._config.base_url, "v1/messages")
        headers = {
            "x-api-key": self._config.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            **self._config.headers,
        }
        owns_client = self._client is None
        client = self._client or httpx.AsyncClient(timeout=15.0)
        tool_state: dict[str, Any] = {"id": "", "name": "", "arguments": ""}
        try:
            async with client.stream("POST", url, headers=headers, json=body) as response:
                if response.status_code >= 400:
                    detail = await response.aread()
                    yield error_event(f"anthropic {response.status_code}: {detail.decode()}")
                    return
                async for event in iter_sse_json(response):
                    kind = event.get("type")
                    if kind == "error":
                        yield error_event(str((event.get("error") or {}).get("message") or event))
                        return
                    if kind == "content_block_delta":
                        delta = event.get("delta") or {}
                        if delta.get("type") == "text_delta" and delta.get("text"):
                            yield text_event(delta["text"])
                        if delta.get("type") == "thinking_delta" and delta.get("thinking"):
                            yield ModelEvent(
                                kind=ModelEventKind.REASONING_DELTA, text=delta["thinking"]
                            )
                        if delta.get("type") == "input_json_delta" and delta.get("partial_json"):
                            tool_state["arguments"] += delta["partial_json"]
                    elif kind == "content_block_start":
                        block = event.get("content_block") or {}
                        if block.get("type") == "tool_use":
                            tool_state = {
                                "id": block.get("id") or "",
                                "name": block.get("name") or "",
                                "arguments": "",
                            }
                    elif kind == "content_block_stop" and tool_state["name"]:
                        try:
                            parsed = json.loads(tool_state["arguments"] or "{}")
                        except Exception:
                            parsed = {"raw": tool_state["arguments"]}
                        yield ModelEvent(
                            kind=ModelEventKind.TOOL_CALL,
                            tool_call=ToolCall(
                                id=tool_state["id"] or "tool",
                                name=tool_state["name"],
                                arguments=parsed if isinstance(parsed, dict) else {"raw": tool_state["arguments"]},
                            ),
                        )
                        tool_state = {"id": "", "name": "", "arguments": ""}
                    elif kind == "message_delta":
                        usage = (event.get("usage") or {})
                        if usage:
                            yield ModelEvent(
                                kind=ModelEventKind.USAGE,
                                usage=Usage(
                                    input_tokens=int(usage.get("input_tokens") or 0),
                                    output_tokens=int(usage.get("output_tokens") or 0),
                                    cache_read_tokens=int(usage.get("cache_read_input_tokens") or 0),
                                    cache_write_tokens=int(usage.get("cache_creation_input_tokens") or 0),
                                ),
                            )
                yield end_event()
        except httpx.HTTPError as exc:
            yield error_event(str(exc) or type(exc).__name__)
            yield end_event()
        finally:
            if owns_client:
                await client.aclose()
