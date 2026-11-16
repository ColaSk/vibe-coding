"""Cursor gateway: BidiAppend → compile → runtime → RunSSE."""

from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Awaitable, Callable
from dataclasses import replace

from cursor_switch.adapters.cursor.checkpoints import MemoryCheckpoints
from cursor_switch.adapters.cursor.compile import MessageDelivery, compile_append
from cursor_switch.adapters.cursor.envelope import (
    ClientActionKind,
    ClientAppend,
    parse_client_append,
)
from cursor_switch.adapters.cursor.prompting.compiler import PromptCompiler, tool_definitions_for_mode
from cursor_switch.adapters.cursor.proto_min import BidiAppendRequest
from cursor_switch.adapters.cursor.publishing_model import PublishingModel
from cursor_switch.adapters.cursor.tools.client_exec import ClientExecDispatcher
from cursor_switch.adapters.cursor.transport import TransportRegistry, TransportRoute
from cursor_switch.adapters.providers.base import ProviderConfig
from cursor_switch.adapters.providers.router import ProviderRouter
from cursor_switch.adapters.tools.dispatch import ToolDispatcher
from cursor_switch.runtime.domain.types import ModelEvent, ModelEventKind
from cursor_switch.runtime.ports.checkpoint import CheckpointPort
from cursor_switch.runtime.ports.model import ModelPort
from cursor_switch.runtime.ports.tool import ToolPort
from cursor_switch.runtime.session.registry import ConversationRegistry

logger = logging.getLogger("cursor_switch.gateway")


def normalize_model_id(model_id: str) -> str:
    """Strip Cursor variant suffixes: `{id}[context=…,…]` or `{id}-200k-high-fast`."""
    raw = model_id.strip()
    if not raw:
        return raw
    if "[" in raw:
        return raw.split("[", 1)[0].strip()
    return raw


class CursorGateway:
    def __init__(
        self,
        *,
        transport: TransportRegistry | None = None,
        model: ModelPort | None = None,
        tools: ToolPort | None = None,
        model_lookup: Callable[[str], ProviderConfig | None] | None = None,
        known_model_ids: Callable[[], set[str]] | None = None,
        accept_all_models: bool = False,
        on_call_finished: Callable[..., Awaitable[None]] | None = None,
        checkpoints: CheckpointPort | None = None,
        agent_mode: str = "agent",
    ) -> None:
        self.transport = transport or TransportRegistry()
        if model is not None:
            self._model: ModelPort = model
        elif model_lookup is not None:
            self._model = ProviderRouter(model_lookup, on_call_finished)
        else:
            self._model = ProviderRouter(lambda _model_id: None, on_call_finished)
        self._known_model_ids = known_model_ids or (lambda: set())
        self._accept_all_models = accept_all_models or model is not None
        self._prompt = PromptCompiler()
        self._agent_mode = agent_mode  # type: ignore[assignment]
        self._tool_defs = tool_definitions_for_mode(self._agent_mode)  # type: ignore[arg-type]
        self._system_prompt = self._prompt.system_prompt(self._agent_mode)  # type: ignore[arg-type]
        if tools is not None:
            self._tools = tools
        else:
            self._tools = ClientExecDispatcher(mode=self._agent_mode)  # type: ignore[arg-type]
        self._checkpoints = checkpoints or MemoryCheckpoints()
        self._conversations = ConversationRegistry(
            model=self._model,
            tools=self._tools,
            checkpoints=self._checkpoints,
            model_id="default",
            tool_definitions=self._tool_defs,
            system_prompt=self._system_prompt,
        )
        self._close_tasks: dict[str, asyncio.Task[None]] = {}

    def is_local_model(self, model_id: str) -> bool:
        if not model_id:
            return False
        if self._accept_all_models:
            return True
        known = self._known_model_ids()
        if model_id in known:
            return True
        base = normalize_model_id(model_id)
        if base in known:
            return True
        for known_id in known:
            if model_id.startswith(f"{known_id}-") or base.startswith(f"{known_id}-"):
                return True
        return False

    def resolve_local_model_id(self, model_id: str) -> str | None:
        if not self.is_local_model(model_id):
            return None
        known = self._known_model_ids()
        if model_id in known:
            return model_id
        base = normalize_model_id(model_id)
        if base in known:
            return base
        for known_id in known:
            if model_id.startswith(f"{known_id}-") or base.startswith(f"{known_id}-"):
                return known_id
        return base if self._accept_all_models else None

    async def handle_bidi_append(self, request: BidiAppendRequest) -> None:
        if not request.request_id:
            raise ValueError("BidiAppend request_id is required")

        raw: bytes | None = None
        if request.data:
            try:
                raw = bytes.fromhex(request.data)
            except ValueError:
                raw = None
        elif request.data_binary:
            raw = request.data_binary
        else:
            raise ValueError("BidiAppend contains no AgentClientMessage")

        # Client-exec tool results arrive as AgentClientMessage.exec_client_message.
        if raw and await self._maybe_complete_exec(raw):
            return

        # Prefer hex `data` (captured protocol). Some clients also send raw
        # AgentClientMessage bytes in `data_binary`.
        if request.data:
            append = parse_client_append(
                request_id=request.request_id,
                seqno=request.append_seqno,
                data_hex=request.data,
            )
        else:
            from cursor_switch.adapters.cursor.envelope import decode_agent_client_message

            append = decode_agent_client_message(
                request.data_binary,
                request_id=request.request_id,
                seqno=request.append_seqno,
            )

        logger.info(
            "bidi append id=%s seq=%s action=%s model=%r text_len=%s",
            append.request_id,
            append.seqno,
            append.action.value,
            append.model_id,
            len(append.text),
        )

        # Heartbeats / unhandled client frames must not fail the session.
        if append.action in {ClientActionKind.HEARTBEAT, ClientActionKind.UNKNOWN} and not append.model_id:
            return

        handle = await self.transport.get_or_create(append.request_id)
        if append.protocol == "run_inference":
            handle.protocol = "run_inference"

        if append.model_id:
            resolved = self.resolve_local_model_id(append.model_id)
            if resolved is not None:
                await self.transport.mark_local(append.request_id)
                append = replace(append, model_id=resolved)
                handle.model_id = resolved
                logger.info("bidi route=local model=%s protocol=%s", resolved, handle.protocol)
            else:
                await self.transport.mark_upstream(append.request_id)
                logger.warning(
                    "bidi route=upstream model=%r (not in local catalog; append ignored)",
                    append.model_id,
                )
                return
        elif handle.route is TransportRoute.UNKNOWN:
            raise ValueError("first BidiAppend message must select a model")
        elif handle.route is TransportRoute.UPSTREAM:
            return

        if append.conversation_id:
            handle.conversation_id = append.conversation_id
        if append.action is ClientActionKind.RUN_INFERENCE_START and append.text:
            handle.routing_text = append.text

        if append.action is ClientActionKind.RUN_INFERENCE_START:
            await self.transport.ensure_run_ready(append.request_id)
            return

        if append.action is ClientActionKind.RUN_INFERENCE_FINISH:
            await self.transport.close(append.request_id)
            return

        # RunInference uses unordered invoke/finish frames; skip seq mailbox.
        if append.protocol == "run_inference":
            await self._dispatch(append)
            return

        ready = await handle.append(append.seqno, append.to_json_bytes())
        for payload in ready:
            item = _client_append_from_payload(payload, fallback=append)
            await self._dispatch(item)

    async def _dispatch(self, append: ClientAppend) -> None:
        if append.protocol == "run_inference" and append.action is ClientActionKind.RUN_INFERENCE_INVOKE:
            await self._dispatch_run_inference(append)
            return

        compiled = compile_append(append)
        if compiled.delivery is MessageDelivery.IGNORE or compiled.command is None:
            return
        conversation_id = append.conversation_id or append.request_id
        model_id = append.model_id or "default"
        handle = await self.transport.get_or_create(append.request_id)
        if handle.model_id and model_id == "default":
            model_id = handle.model_id

        publishing = PublishingModel(self._model, self.transport, append.request_id)
        await self._bind_tool_publish(append.request_id, conversation_id)
        runtime = self._conversations.get_or_create(
            conversation_id,
            model_id=model_id,
            model=publishing,
            tool_definitions=self._tool_defs,
            system_prompt=self._system_prompt,
        )
        await runtime.handle(compiled.command)

        async def _finalize() -> None:
            await runtime.wait_until_idle()
            await self.transport.publish(
                append.request_id,
                ModelEvent(kind=ModelEventKind.END),
            )
            await self.transport.close(append.request_id)

        existing = self._close_tasks.get(append.request_id)
        if existing is None or existing.done():
            self._close_tasks[append.request_id] = asyncio.create_task(_finalize())

    async def _dispatch_run_inference(self, append: ClientAppend) -> None:
        from cursor_switch.adapters.cursor.prompting.compiler import enrich_tools_with_catalog
        from cursor_switch.adapters.cursor.run_inference import (
            encode_invocation_end,
            encode_text_part,
            encode_tool_call_part,
        )
        from cursor_switch.adapters.cursor.run_inference_guard import (
            DEFAULT_TOOL_CONTENT_LIMIT,
            DEFAULT_USER_CONTENT_LIMIT,
            empty_tool_result_streak,
            history_summary,
            repeated_tool_loop,
            truncate_message_content,
        )
        from cursor_switch.runtime.domain.types import Message, MessageRole, ToolCall
        from cursor_switch.runtime.ports.model import ModelInvocation

        handle = await self.transport.get_or_create(append.request_id)
        await self.transport.ensure_run_ready(append.request_id)
        model_id = append.model_id or handle.model_id or "default"
        text = append.text or handle.routing_text or ""
        invocation_id = append.invocation_id or f"inv-{append.request_id}-{append.seqno}"
        role_map = {
            "user": MessageRole.USER,
            "assistant": MessageRole.ASSISTANT,
            "tool": MessageRole.TOOL,
            "system": MessageRole.SYSTEM,
        }
        messages: list[Message] = []
        # Client local_loop already ships mode/system context + tool schemas.
        # Prefacing our catalog prompt makes the model thrash on search tools.
        if self._system_prompt and not append.tools:
            messages.append(
                Message(
                    id=f"sys-{invocation_id}",
                    role=MessageRole.SYSTEM,
                    content=self._system_prompt,
                )
            )
        if append.messages:
            for index, raw_msg in enumerate(append.messages):
                if not isinstance(raw_msg, dict):
                    continue
                role = role_map.get(str(raw_msg.get("role") or "user"), MessageRole.USER)
                tool_call_id = raw_msg.get("tool_call_id")
                if role is MessageRole.TOOL and not tool_call_id:
                    continue
                tool_calls_raw = raw_msg.get("tool_calls") or []
                tool_calls: list[ToolCall] = []
                for call in tool_calls_raw:
                    if not isinstance(call, dict):
                        continue
                    call_id = str(call.get("id") or "")
                    name = str(call.get("name") or "")
                    if not call_id and not name:
                        continue
                    args = call.get("arguments") if isinstance(call.get("arguments"), dict) else {}
                    tool_calls.append(
                        ToolCall(id=call_id or name, name=name or "tool", arguments=args)
                    )
                content = str(raw_msg.get("content") or "")
                if role is MessageRole.TOOL and not content.strip():
                    content = "[empty tool result]"
                if role is MessageRole.TOOL:
                    content = truncate_message_content(
                        content, limit=DEFAULT_TOOL_CONTENT_LIMIT
                    )
                elif role is MessageRole.USER and len(content) > DEFAULT_USER_CONTENT_LIMIT:
                    content = truncate_message_content(
                        content, limit=DEFAULT_USER_CONTENT_LIMIT
                    )
                messages.append(
                    Message(
                        id=f"msg-{invocation_id}-{index}",
                        role=role,
                        content=content,
                        tool_call_id=str(tool_call_id) if tool_call_id else None,
                        tool_calls=tuple(tool_calls),
                    )
                )
        else:
            messages.append(
                Message(
                    id=f"msg-{invocation_id}",
                    role=MessageRole.USER,
                    content=text or "hello",
                )
            )
        tools = list(append.tools) if append.tools else list(self._tool_defs)
        if append.tools:
            # Full tools.json — not mode allow-list — so CreatePlan/AskQuestion/etc. get schemas.
            tools = enrich_tools_with_catalog(tools)

        disable_tools = repeated_tool_loop(messages) or empty_tool_result_streak(messages)
        if disable_tools:
            logger.warning(
                "run_inference tool loop detected id=%s; forcing text-only turn",
                invocation_id,
            )
            tools = []
            messages.append(
                Message(
                    id=f"loop-{invocation_id}",
                    role=MessageRole.USER,
                    content=(
                        "Stop calling tools. Using only information already in this "
                        "conversation, give the final answer now."
                    ),
                )
            )
        tool_props = []
        for tool in tools[:8]:
            fn = tool.get("function", tool) if isinstance(tool, dict) else {}
            if not isinstance(fn, dict):
                continue
            props = (fn.get("parameters") or {}).get("properties") if isinstance(fn.get("parameters"), dict) else {}
            tool_props.append(
                {
                    "name": fn.get("name"),
                    "props": len(props) if isinstance(props, dict) else 0,
                }
            )
        logger.info(
            "run_inference invoke id=%s model=%s text_len=%s tools=%s tool_props=%s messages=%s history=%s",
            invocation_id,
            model_id,
            len(text),
            len(tools),
            tool_props,
            len(messages),
            history_summary(messages)[-8:],
        )
        invocation = ModelInvocation(
            model_id=model_id,
            messages=messages,
            tools=tools,
        )
        try:
            tool_index = 0
            emitted_text = False
            async for event in self._model.stream(invocation):
                if event.kind is ModelEventKind.TEXT_DELTA and event.text:
                    emitted_text = True
                    await handle.publish_payload(
                        encode_text_part(
                            invocation_id=invocation_id,
                            text=event.text,
                            is_final=False,
                        )
                    )
                elif event.kind is ModelEventKind.TOOL_CALL and event.tool_call is not None:
                    call = event.tool_call
                    logger.info(
                        "run_inference tool_call id=%s name=%s args=%s",
                        call.id,
                        call.name,
                        call.arguments,
                    )
                    await handle.publish_payload(
                        encode_tool_call_part(
                            invocation_id=invocation_id,
                            tool_call_id=call.id,
                            tool_name=call.name,
                            args=call.arguments,
                            is_complete=True,
                            tool_index=tool_index,
                        )
                    )
                    tool_index += 1
                elif event.kind is ModelEventKind.ERROR:
                    logger.warning("run_inference model error: %s", event.error)
                    err_text = f"模型调用失败：{event.error}"
                    emitted_text = True
                    await handle.publish_payload(
                        encode_text_part(
                            invocation_id=invocation_id,
                            text=err_text,
                            is_final=False,
                        )
                    )
            if not emitted_text and tool_index == 0:
                await handle.publish_payload(
                    encode_text_part(
                        invocation_id=invocation_id,
                        text="（本轮没有生成文本）",
                        is_final=False,
                    )
                )
            await handle.publish_payload(
                encode_text_part(invocation_id=invocation_id, text="", is_final=True)
            )
            await handle.publish_payload(encode_invocation_end(invocation_id=invocation_id))
        except Exception as exc:  # noqa: BLE001
            logger.exception("run_inference invoke failed: %s", exc)
            try:
                await handle.publish_payload(
                    encode_text_part(
                        invocation_id=invocation_id,
                        text=f"模型调用异常：{exc}",
                        is_final=True,
                    )
                )
                await handle.publish_payload(encode_invocation_end(invocation_id=invocation_id))
            except Exception:  # noqa: BLE001
                await self.transport.close_error(append.request_id, str(exc))


    async def _bind_tool_publish(self, request_id: str, conversation_id: str) -> None:
        tools = self._tools
        if not isinstance(tools, ClientExecDispatcher):
            return

        async def _publish(message: object) -> None:
            await self.transport.publish_agent_message(request_id, message)

        tools.set_publish(_publish)
        tools.set_conversation_id(conversation_id)

    async def _maybe_complete_exec(self, raw: bytes) -> bool:
        if not isinstance(self._tools, ClientExecDispatcher):
            return False
        try:
            from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb

            client = pb.AgentClientMessage()
            client.ParseFromString(raw)
        except Exception:  # noqa: BLE001 — not a generated AgentClientMessage
            return False
        if client.WhichOneof("message") != "exec_client_message":
            return False
        return await self._tools.complete_exec(client.exec_client_message)


def _client_append_from_payload(payload: bytes, *, fallback: ClientAppend) -> ClientAppend:
    data = json.loads(payload.decode("utf-8"))
    action_raw = str(data.get("action") or ClientActionKind.UNKNOWN.value)
    try:
        action = ClientActionKind(action_raw)
    except ValueError:
        action = ClientActionKind.UNKNOWN
    messages_raw = data.get("messages") or fallback.messages
    tools_raw = data.get("tools") or fallback.tools
    messages: list[dict] = []
    for item in messages_raw:
        if isinstance(item, dict):
            messages.append(item)
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            tool_call_id = item[2] if len(item) > 2 else None
            messages.append(
                {
                    "role": str(item[0]),
                    "content": str(item[1]),
                    "tool_call_id": tool_call_id,
                    "tool_calls": [],
                }
            )
    return ClientAppend(
        request_id=str(data.get("request_id") or fallback.request_id),
        seqno=int(data.get("seqno") or fallback.seqno),
        conversation_id=str(data.get("conversation_id") or fallback.conversation_id),
        model_id=str(data.get("model_id") or fallback.model_id),
        action=action,
        text=str(data.get("text") or ""),
        command_id=str(data.get("command_id") or fallback.command_id),
        target_run_id=data.get("target_run_id"),
        invocation_id=str(data.get("invocation_id") or fallback.invocation_id),
        protocol=str(data.get("protocol") or fallback.protocol),
        messages=messages,
        tools=list(tools_raw) if isinstance(tools_raw, list) else [],
    )
