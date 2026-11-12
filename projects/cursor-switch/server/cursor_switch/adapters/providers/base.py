"""Shared helpers for upstream provider strategies."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urljoin, urlparse

import httpx

from cursor_switch.runtime.domain.types import Message, MessageRole, ModelEvent, ModelEventKind

RESERVED_BODY_KEYS = frozenset(
    {
        "model",
        "stream",
        "messages",
        "input",
        "tools",
        "system",
        "instructions",
        "prompt_cache_key",
    }
)


@dataclass(frozen=True, slots=True)
class ProviderConfig:
    provider_type: str
    base_url: str
    api_key: str
    model_name: str
    headers: dict[str, str] = field(default_factory=dict)
    extra: dict[str, Any] = field(default_factory=dict)


def resolve_endpoint(base_url: str, suffix: str) -> str:
    raw = base_url.strip()
    if not raw:
        raise ValueError("base_url is required")
    parsed = urlparse(raw)
    path = parsed.path.rstrip("/")
    if path.endswith(suffix.rstrip("/")):
        return raw
    if not path or path == "":
        return urljoin(raw if raw.endswith("/") else raw + "/", suffix.lstrip("/"))
    return raw.rstrip("/") + "/" + suffix.lstrip("/")


def merge_extra(body: dict[str, Any], extra: dict[str, Any]) -> dict[str, Any]:
    for key, value in extra.items():
        if key in RESERVED_BODY_KEYS:
            raise ValueError(f"extra params cannot replace {key}")
        body[key] = value
    return body


def role_name(role: MessageRole) -> str:
    return role.value


def to_openai_messages(messages: list[Message]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for message in messages:
        item: dict[str, Any] = {
            "role": role_name(message.role),
            "content": message.content,
        }
        if message.tool_call_id:
            item["tool_call_id"] = message.tool_call_id
        result.append(item)
    return result


async def iter_sse_json(
    response: httpx.Response,
) -> AsyncIterator[dict[str, Any]]:
    async for line in response.aiter_lines():
        if not line or not line.startswith("data:"):
            continue
        payload = line[5:].strip()
        if payload == "[DONE]":
            break
        try:
            yield json.loads(payload)
        except json.JSONDecodeError:
            continue


def end_event() -> ModelEvent:
    return ModelEvent(kind=ModelEventKind.END)


def error_event(message: str) -> ModelEvent:
    return ModelEvent(kind=ModelEventKind.ERROR, error=message)


def text_event(text: str) -> ModelEvent:
    return ModelEvent(kind=ModelEventKind.TEXT_DELTA, text=text)


def reasoning_event(text: str) -> ModelEvent:
    return ModelEvent(kind=ModelEventKind.REASONING_DELTA, text=text)
