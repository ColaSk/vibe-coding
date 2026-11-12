"""Upstream provider strategies."""

import httpx
import pytest

from cursor_switch.adapters.providers.anthropic import AnthropicMessagesStrategy
from cursor_switch.adapters.providers.base import ProviderConfig, merge_extra, resolve_endpoint
from cursor_switch.adapters.providers.openai_chat import OpenAiChatStrategy
from cursor_switch.adapters.providers.openai_responses import OpenAiResponsesStrategy
from cursor_switch.runtime.domain.types import Message, MessageRole, ModelEventKind, new_id
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
