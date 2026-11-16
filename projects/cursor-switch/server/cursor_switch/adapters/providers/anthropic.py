"""Anthropic Messages strategy."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from typing import Any

import httpx

from cursor_switch.adapters.providers.base import (
    ProviderConfig,
    default_httpx_timeout,
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


def _is_tool_result_user_message(message: dict[str, Any]) -> bool:
    content = message.get("content")
    return (
        message.get("role") == "user"
        and isinstance(content, list)
        and bool(content)
        and all(isinstance(part, dict) and part.get("type") == "tool_result" for part in content)
    )


def _split_system(messages: list[Message]) -> tuple[str | None, list[dict[str, Any]]]:
    system_parts: list[str] = []
    body: list[dict[str, Any]] = []
    for message in messages:
        if message.role is MessageRole.SYSTEM:
            system_parts.append(message.content)
            continue
        if message.role is MessageRole.TOOL:
            if not message.tool_call_id:
                continue
            part = {
                "type": "tool_result",
                "tool_use_id": message.tool_call_id,
                "content": message.content or "[empty tool result]",
            }
            # Anthropic expects one user message with all tool_result blocks
            # after an assistant tool_use turn.
            if body and _is_tool_result_user_message(body[-1]):
                content = body[-1]["content"]
                assert isinstance(content, list)
                content.append(part)
            else:
                body.append({"role": "user", "content": [part]})
            continue
        if message.role is MessageRole.ASSISTANT and message.tool_calls:
            content: list[dict[str, Any]] = []
            if message.content:
                content.append({"type": "text", "text": message.content})
            for call in message.tool_calls:
                content.append(
                    {
                        "type": "tool_use",
                        "id": call.id,
                        "name": call.name,
                        "input": call.arguments or {},
                    }
                )
            body.append({"role": "assistant", "content": content})
            continue
        role = "user" if message.role is MessageRole.USER else "assistant"
        body.append({"role": role, "content": message.content})
    system = "\n\n".join(system_parts) if system_parts else None
    return system, body


def _normalize_input_schema(parameters: Any) -> dict[str, Any]:
    """Anthropic requires input_schema.type == \"object\"."""
    if not isinstance(parameters, dict):
        return {"type": "object", "properties": {}}
    schema = dict(parameters)
    if schema.get("type") != "object":
        schema["type"] = "object"
    if not isinstance(schema.get("properties"), dict):
        schema["properties"] = {}
    return schema


def _anthropic_tools(tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for tool in tools:
        fn = tool.get("function", tool) if isinstance(tool, dict) else {}
        if not isinstance(fn, dict):
            fn = tool if isinstance(tool, dict) else {}
        name = fn.get("name") or (tool.get("name") if isinstance(tool, dict) else None)
        if not name:
            continue
        out.append(
            {
                "name": str(name),
                "description": str(fn.get("description") or ""),
                "input_schema": _normalize_input_schema(fn.get("parameters")),
            }
        )
    return out


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
            body["tools"] = _anthropic_tools(invocation.tools)
        merge_extra(body, {**self._config.extra, **invocation.extra})
        url = resolve_endpoint(self._config.base_url, "v1/messages")
        headers = {
            "x-api-key": self._config.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
            **self._config.headers,
        }
        owns_client = self._client is None
        client = self._client or httpx.AsyncClient(timeout=default_httpx_timeout())
        tool_state: dict[str, Any] = {"id": "", "name": "", "arguments": "", "seed": None}
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
                            initial = block.get("input")
                            seed: dict[str, Any] | None = None
                            if isinstance(initial, dict) and initial:
                                seed = initial
                            tool_state = {
                                "id": block.get("id") or "",
                                "name": block.get("name") or "",
                                "arguments": "",
                                "seed": seed,
                            }
                    elif kind == "content_block_stop" and tool_state["name"]:
                        raw_args = tool_state["arguments"]
                        if raw_args:
                            try:
                                parsed = json.loads(raw_args)
                            except Exception:
                                parsed = {"raw": raw_args}
                        elif isinstance(tool_state.get("seed"), dict):
                            parsed = tool_state["seed"]
                        else:
                            parsed = {}
                        yield ModelEvent(
                            kind=ModelEventKind.TOOL_CALL,
                            tool_call=ToolCall(
                                id=tool_state["id"] or "tool",
                                name=tool_state["name"],
                                arguments=parsed if isinstance(parsed, dict) else {"raw": raw_args},
                            ),
                        )
                        tool_state = {"id": "", "name": "", "arguments": "", "seed": None}
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
