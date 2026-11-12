"""OpenAI Chat Completions strategy."""

from __future__ import annotations

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
    to_openai_messages,
)
from cursor_switch.runtime.domain.types import (
    Message,
    ModelEvent,
    ModelEventKind,
    ToolCall,
    Usage,
)
from cursor_switch.runtime.ports.model import ModelInvocation


class OpenAiChatStrategy:
    def __init__(self, config: ProviderConfig, client: httpx.AsyncClient | None = None) -> None:
        self._config = config
        self._client = client

    async def stream(self, invocation: ModelInvocation) -> AsyncIterator[ModelEvent]:
        body: dict[str, Any] = {
            "model": self._config.model_name,
            "messages": to_openai_messages(invocation.messages),
            "stream": True,
            "stream_options": {"include_usage": True},
        }
        if invocation.tools:
            body["tools"] = invocation.tools
        merge_extra(body, {**self._config.extra, **invocation.extra})
        url = resolve_endpoint(self._config.base_url, "chat/completions")
        headers = {
            "Authorization": f"Bearer {self._config.api_key}",
            "Content-Type": "application/json",
            **self._config.headers,
        }
        owns_client = self._client is None
        client = self._client or httpx.AsyncClient(timeout=15.0)
        try:
            async with client.stream("POST", url, headers=headers, json=body) as response:
                if response.status_code >= 400:
                    detail = await response.aread()
                    yield error_event(f"openai chat {response.status_code}: {detail.decode()}")
                    return
                tool_calls: dict[int, dict[str, str]] = {}
                async for event in iter_sse_json(response):
                    if err := event.get("error"):
                        yield error_event(str(err))
                        return
                    usage = event.get("usage")
                    if usage:
                        yield ModelEvent(
                            kind=ModelEventKind.USAGE,
                            usage=Usage(
                                input_tokens=int(usage.get("prompt_tokens") or 0),
                                output_tokens=int(usage.get("completion_tokens") or 0),
                            ),
                        )
                    for choice in event.get("choices") or []:
                        delta = choice.get("delta") or {}
                        if content := delta.get("content"):
                            yield text_event(content)
                        if reasoning := delta.get("reasoning_content"):
                            yield ModelEvent(kind=ModelEventKind.REASONING_DELTA, text=reasoning)
                        for tool in delta.get("tool_calls") or []:
                            index = int(tool.get("index") or 0)
                            state = tool_calls.setdefault(index, {"id": "", "name": "", "arguments": ""})
                            if tool.get("id"):
                                state["id"] = tool["id"]
                            function = tool.get("function") or {}
                            if function.get("name"):
                                state["name"] = function["name"]
                            if function.get("arguments"):
                                state["arguments"] += function["arguments"]
                        if choice.get("finish_reason") == "tool_calls":
                            for state in tool_calls.values():
                                arguments = state["arguments"] or "{}"
                                try:
                                    parsed = __import__("json").loads(arguments)
                                except Exception:
                                    parsed = {"raw": arguments}
                                yield ModelEvent(
                                    kind=ModelEventKind.TOOL_CALL,
                                    tool_call=ToolCall(
                                        id=state["id"] or "tool",
                                        name=state["name"] or "unknown",
                                        arguments=parsed if isinstance(parsed, dict) else {"raw": arguments},
                                    ),
                                )
                yield end_event()
        except httpx.HTTPError as exc:
            yield error_event(str(exc) or type(exc).__name__)
            yield end_event()
        finally:
            if owns_client:
                await client.aclose()
