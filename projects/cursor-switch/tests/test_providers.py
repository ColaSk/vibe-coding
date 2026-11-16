"""Upstream provider strategies."""

import json

import httpx
import pytest

from cursor_switch.adapters.providers.anthropic import AnthropicMessagesStrategy
from cursor_switch.adapters.providers.base import ProviderConfig, merge_extra, resolve_endpoint
from cursor_switch.adapters.providers.openai_chat import OpenAiChatStrategy
from cursor_switch.adapters.providers.openai_responses import OpenAiResponsesStrategy
from cursor_switch.runtime.domain.types import (
    Message,
    MessageRole,
    ModelEventKind,
    ToolCall,
    new_id,
)
from cursor_switch.runtime.ports.model import ModelInvocation


def _msg(text: str) -> Message:
    return Message(id=new_id("msg"), role=MessageRole.USER, content=text)


def test_resolve_endpoint_and_reserved_extra() -> None:
    assert resolve_endpoint("https://api.openai.com/v1", "chat/completions").endswith(
        "/v1/chat/completions"
    )
    assert (
        resolve_endpoint("https://api.openai.com/v1/chat/completions", "chat/completions")
        == "https://api.openai.com/v1/chat/completions"
    )
    with pytest.raises(ValueError):
        merge_extra({"model": "x"}, {"model": "y"})


@pytest.mark.asyncio
async def test_openai_chat_streams_text() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/chat/completions")
        body = (
            'data: {"choices":[{"delta":{"content":"pong"}}]}\n\n'
            'data: {"usage":{"prompt_tokens":1,"completion_tokens":1}}\n\n'
            "data: [DONE]\n\n"
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    strategy = OpenAiChatStrategy(
        ProviderConfig(
            provider_type="openai_chat",
            base_url="https://example.com/v1",
            api_key="k",
            model_name="gpt",
        ),
        client=client,
    )
    events = [event async for event in strategy.stream(ModelInvocation(model_id="gpt", messages=[_msg("hi")]))]
    await client.aclose()
    assert any(event.kind is ModelEventKind.TEXT_DELTA and event.text == "pong" for event in events)
    assert events[-1].kind is ModelEventKind.END


@pytest.mark.asyncio
async def test_openai_responses_streams_text() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/responses")
        body = (
            'data: {"type":"response.output_text.delta","delta":"pong"}\n\n'
            'data: {"type":"response.completed","response":{"usage":{"input_tokens":2,"output_tokens":1}}}\n\n'
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strategy = OpenAiResponsesStrategy(
        ProviderConfig(
            provider_type="openai_responses",
            base_url="https://example.com/v1",
            api_key="k",
            model_name="gpt",
        ),
        client=client,
    )
    events = [event async for event in strategy.stream(ModelInvocation(model_id="gpt", messages=[_msg("hi")]))]
    await client.aclose()
    assert any(event.kind is ModelEventKind.TEXT_DELTA and event.text == "pong" for event in events)


@pytest.mark.asyncio
async def test_anthropic_tool_use_seeds_input_from_content_block_start() -> None:
    """Some gateways put the full tool input on content_block_start with no deltas."""

    def handler(request: httpx.Request) -> httpx.Response:
        body = (
            'data: {"type":"content_block_start","content_block":{"type":"tool_use","id":"c1","name":"Read","input":{"path":"README.md","limit":20}}}\n\n'
            'data: {"type":"content_block_stop"}\n\n'
            'data: {"type":"message_delta","usage":{"output_tokens":1}}\n\n'
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strategy = AnthropicMessagesStrategy(
        ProviderConfig(
            provider_type="anthropic",
            base_url="https://api.anthropic.com",
            api_key="k",
            model_name="claude",
        ),
        client=client,
    )
    events = [
        event
        async for event in strategy.stream(ModelInvocation(model_id="claude", messages=[_msg("hi")]))
    ]
    await client.aclose()
    tool_events = [e for e in events if e.kind is ModelEventKind.TOOL_CALL and e.tool_call]
    assert tool_events
    assert tool_events[0].tool_call is not None
    assert tool_events[0].tool_call.arguments == {"path": "README.md", "limit": 20}


@pytest.mark.asyncio
async def test_anthropic_streams_text() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path.endswith("/v1/messages")
        assert request.headers["anthropic-version"] == "2023-06-01"
        body = (
            'data: {"type":"content_block_delta","delta":{"type":"text_delta","text":"pong"}}\n\n'
            'data: {"type":"message_delta","usage":{"output_tokens":1}}\n\n'
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strategy = AnthropicMessagesStrategy(
        ProviderConfig(
            provider_type="anthropic",
            base_url="https://api.anthropic.com",
            api_key="k",
            model_name="claude",
        ),
        client=client,
    )
    events = [event async for event in strategy.stream(ModelInvocation(model_id="claude", messages=[_msg("hi")]))]
    await client.aclose()
    assert any(event.kind is ModelEventKind.TEXT_DELTA and event.text == "pong" for event in events)


@pytest.mark.asyncio
async def test_anthropic_normalizes_tool_input_schema_type() -> None:
    """Cursor tool Structs often omit JSON-Schema type; Anthropic requires object."""
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.content.decode())
        body = (
            'data: {"type":"content_block_delta","delta":{"type":"text_delta","text":"ok"}}\n\n'
            'data: {"type":"message_delta","usage":{"output_tokens":1}}\n\n'
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strategy = AnthropicMessagesStrategy(
        ProviderConfig(
            provider_type="anthropic",
            base_url="https://api.anthropic.com",
            api_key="k",
            model_name="claude",
        ),
        client=client,
    )
    tools = [
        {
            "type": "function",
            "function": {
                "name": "Shell",
                "description": "run",
                "parameters": {"properties": {"command": {"type": "string"}}},
            },
        },
        {"name": "Read", "description": "read", "parameters": None},
    ]
    events = [
        event
        async for event in strategy.stream(
            ModelInvocation(model_id="claude", messages=[_msg("hi")], tools=tools)
        )
    ]
    await client.aclose()
    assert any(event.kind is ModelEventKind.TEXT_DELTA for event in events)
    assert "tools" in seen["body"]
    for tool in seen["body"]["tools"]:
        assert tool["input_schema"]["type"] == "object"
        assert isinstance(tool["input_schema"].get("properties"), dict)


@pytest.mark.asyncio
async def test_anthropic_replays_assistant_tool_use_and_results() -> None:
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.content.decode())
        body = (
            'data: {"type":"content_block_delta","delta":{"type":"text_delta","text":"done"}}\n\n'
            'data: {"type":"message_delta","usage":{"output_tokens":1}}\n\n'
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strategy = AnthropicMessagesStrategy(
        ProviderConfig(
            provider_type="anthropic",
            base_url="https://api.anthropic.com",
            api_key="k",
            model_name="claude",
        ),
        client=client,
    )
    messages = [
        Message(id="u1", role=MessageRole.USER, content="read it"),
        Message(
            id="a1",
            role=MessageRole.ASSISTANT,
            content="",
            tool_calls=(ToolCall(id="call-1", name="Read", arguments={"path": "README.md"}),),
        ),
        Message(
            id="t1",
            role=MessageRole.TOOL,
            content="file body",
            tool_call_id="call-1",
        ),
        Message(id="t-bad", role=MessageRole.TOOL, content="orphan", tool_call_id=""),
    ]
    events = [
        event
        async for event in strategy.stream(
            ModelInvocation(model_id="claude", messages=messages, tools=[])
        )
    ]
    await client.aclose()
    assert any(event.kind is ModelEventKind.TEXT_DELTA for event in events)
    roles = [m["role"] for m in seen["body"]["messages"]]
    assert roles == ["user", "assistant", "user"]
    assistant = seen["body"]["messages"][1]["content"]
    assert any(part.get("type") == "tool_use" and part.get("id") == "call-1" for part in assistant)
    tool_msg = seen["body"]["messages"][2]["content"]
    assert tool_msg[0]["type"] == "tool_result"
    assert tool_msg[0]["tool_use_id"] == "call-1"


@pytest.mark.asyncio
async def test_anthropic_merges_consecutive_tool_results() -> None:
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.content.decode())
        body = (
            'data: {"type":"content_block_delta","delta":{"type":"text_delta","text":"done"}}\n\n'
            'data: {"type":"message_delta","usage":{"output_tokens":1}}\n\n'
        )
        return httpx.Response(200, text=body, headers={"content-type": "text/event-stream"})

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    strategy = AnthropicMessagesStrategy(
        ProviderConfig(
            provider_type="anthropic",
            base_url="https://api.anthropic.com",
            api_key="k",
            model_name="claude",
        ),
        client=client,
    )
    messages = [
        Message(id="u1", role=MessageRole.USER, content=" dig"),
        Message(
            id="a1",
            role=MessageRole.ASSISTANT,
            content="",
            tool_calls=(
                ToolCall(id="c1", name="Grep", arguments={"pattern": "a"}),
                ToolCall(id="c2", name="Grep", arguments={"pattern": "b"}),
            ),
        ),
        Message(id="t1", role=MessageRole.TOOL, content="ra", tool_call_id="c1"),
        Message(id="t2", role=MessageRole.TOOL, content="rb", tool_call_id="c2"),
    ]
    _ = [
        event
        async for event in strategy.stream(
            ModelInvocation(model_id="claude", messages=messages, tools=[])
        )
    ]
    await client.aclose()
    assert [m["role"] for m in seen["body"]["messages"]] == ["user", "assistant", "user"]
    results = seen["body"]["messages"][2]["content"]
    assert [part["tool_use_id"] for part in results] == ["c1", "c2"]
