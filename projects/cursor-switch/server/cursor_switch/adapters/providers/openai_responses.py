"""OpenAI Responses API strategy."""

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


def _responses_input(messages: list[Message]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for message in messages:
        if message.role is MessageRole.SYSTEM:
            continue
        if message.role is MessageRole.TOOL:
            items.append(
                {
                    "type": "function_call_output",
                    "call_id": message.tool_call_id or "",
                    "output": message.content,
                }
            )
            continue
        role = "user" if message.role is MessageRole.USER else "assistant"
        items.append(
            {
                "role": role,
                "content": [{"type": "input_text" if role == "user" else "output_text", "text": message.content}],
            }
        )
    return items


class OpenAiResponsesStrategy:
    def __init__(self, config: ProviderConfig, client: httpx.AsyncClient | None = None) -> None:
        self._config = config
        self._client = client

    async def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        body: dict[str, Any] = {
            "model": self._config.model_name,
            "input": _responses_input(invocation.messages),
            "stream": True,
        }
        if invocation.tools:
            body["tools"] = [
                {
                    "type": "function",
                    "name": tool.get("function", tool).get("name", tool.get("name")),
                    "description": tool.get("function", tool).get("description", ""),
                    "parameters": tool.get("function", tool).get("parameters", {}),
                }
                for tool in invocation.tools
            ]
        merge_extra(body, {**self._config.extra, **invocation.extra})
        url = resolve_endpoint(self._config.base_url, "responses")
        headers = {
            "Authorization": f"Bearer {self._config.api_key}",
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
                    yield error_event(f"openai responses {response.status_code}: {detail.decode()}")
                    return
                async for event in iter_sse_json(response):
                    kind = event.get("type")
                    if kind in {"error", "response.failed"} or event.get("error"):
                        message = (
                            event.get("message")
                            or (event.get("error") or {}).get("message")
                            or "provider error"
                        )
                        yield error_event(str(message))
                        return
                    if kind in {"response.output_text.delta", "response.reasoning_summary_text.delta"}:
                        delta = event.get("delta") or ""
                        if kind.endswith("reasoning_summary_text.delta"):
                            yield ModelEvent(kind=ModelEventKind.REASONING_DELTA, text=delta)
                        else:
                            yield text_event(delta)
                    elif kind == "response.output_item.added":
                        item = event.get("item") or {}
                        if item.get("type") == "function_call":
                            tool_state = {
                                "id": item.get("call_id") or item.get("id") or "",
                                "name": item.get("name") or "",
                                "arguments": item.get("arguments") or "",
                            }
                    elif kind == "response.function_call_arguments.delta":
                        tool_state["arguments"] += event.get("delta") or ""
                    elif kind == "response.function_call_arguments.done":
                        arguments = event.get("arguments") or tool_state["arguments"] or "{}"
                        try:
                            parsed = json.loads(arguments)
                        except Exception:
                            parsed = {"raw": arguments}
                        yield ModelEvent(
                            kind=ModelEventKind.TOOL_CALL,
                            tool_call=ToolCall(
                                id=tool_state["id"] or "tool",
                                name=tool_state["name"] or "unknown",
                                arguments=parsed if isinstance(parsed, dict) else {"raw": arguments},
                            ),
                        )
                    elif kind == "response.completed":
                        usage = (event.get("response") or {}).get("usage") or event.get("usage")
                        if usage:
                            yield ModelEvent(
                                kind=ModelEventKind.USAGE,
                                usage=Usage(
                                    input_tokens=int(usage.get("input_tokens") or 0),
                                    output_tokens=int(usage.get("output_tokens") or 0),
                                    cache_read_tokens=int(
                                        (usage.get("input_tokens_details") or {}).get("cached_tokens")
                                        or 0
                                    ),
                                ),
                            )
                yield end_event()
        except httpx.HTTPError as exc:
            yield error_event(str(exc) or type(exc).__name__)
            yield end_event()
        finally:
            if owns_client:
                await client.aclose()
