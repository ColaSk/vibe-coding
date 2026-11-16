"""Convert runtime ModelEvent values into AgentServerMessage frames.

Mirrors cursor-byok server/src/cursor/protocol/events.rs for the Agent path.
"""

from __future__ import annotations

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.runtime.domain.types import ModelEvent, ModelEventKind, ToolCall, Usage


def server_interaction(update: pb.InteractionUpdate) -> pb.AgentServerMessage:
    return pb.AgentServerMessage(interaction_update=update)


def text_delta(text: str, *, is_server_notice: bool = False) -> pb.AgentServerMessage:
    return server_interaction(
        pb.InteractionUpdate(
            text_delta=pb.TextDeltaUpdate(text=text, is_server_notice=is_server_notice)
        )
    )


def thinking_delta(text: str) -> pb.AgentServerMessage:
    return server_interaction(
        pb.InteractionUpdate(
            thinking_delta=pb.ThinkingDeltaUpdate(
                text=text,
                thinking_style=pb.ThinkingStyle.THINKING_STYLE_DEFAULT,
            )
        )
    )


def heartbeat() -> pb.AgentServerMessage:
    return server_interaction(pb.InteractionUpdate(heartbeat=pb.HeartbeatUpdate()))


def turn_ended(usage: Usage | None = None) -> pb.AgentServerMessage:
    ended = pb.TurnEndedUpdate()
    if usage is not None:
        ended.input_tokens = usage.input_tokens
        ended.output_tokens = usage.output_tokens
        ended.cache_read_tokens = usage.cache_read_tokens
        ended.cache_write_tokens = usage.cache_write_tokens
    return server_interaction(pb.InteractionUpdate(turn_ended=ended))


_COMPAT_PROVIDER = "cursor-switch-compat"


def tool_placeholder(name: str, call_id: str) -> pb.ToolCall:
    """Wire/UI ToolCall card. Unknown tools use an MCP-shaped placeholder (byok compat)."""
    key = name.strip().lower()
    tool = pb.ToolCall(tool_call_id=call_id)
    if key in {"shell", "bash"}:
        tool.shell_tool_call.SetInParent()
    elif key == "read":
        tool.read_tool_call.SetInParent()
    elif key == "grep":
        tool.grep_tool_call.SetInParent()
    elif key == "glob":
        tool.glob_tool_call.SetInParent()
    elif key == "delete":
        tool.delete_tool_call.SetInParent()
    elif key in {"write", "strreplace", "editnotebook"}:
        tool.edit_tool_call.SetInParent()
    elif key in {"todowrite", "updatetodos"}:
        tool.update_todos_tool_call.SetInParent()
    elif key == "askquestion":
        tool.ask_question_tool_call.SetInParent()
    elif key == "websearch":
        tool.web_search_tool_call.SetInParent()
    elif key in {"webfetch", "fetch"}:
        tool.web_fetch_tool_call.SetInParent()
    elif key == "createplan":
        tool.create_plan_tool_call.SetInParent()
    elif key == "switchmode":
        tool.switch_mode_tool_call.SetInParent()
    elif key == "task":
        tool.task_tool_call.SetInParent()
    elif key == "generateimage":
        tool.generate_image_tool_call.SetInParent()
    elif key in {"getmcptools", "callmcptool", "fetchmcpresource"}:
        tool.mcp_tool_call.args.name = name
        tool.mcp_tool_call.args.tool_call_id = call_id
        tool.mcp_tool_call.args.tool_name = name
        tool.mcp_tool_call.args.provider_identifier = _COMPAT_PROVIDER
        tool.mcp_tool_call.args.server_identifier = _COMPAT_PROVIDER
    else:
        tool.mcp_tool_call.args.name = name
        tool.mcp_tool_call.args.tool_call_id = call_id
        tool.mcp_tool_call.args.tool_name = name
        tool.mcp_tool_call.args.provider_identifier = _COMPAT_PROVIDER
        tool.mcp_tool_call.args.server_identifier = _COMPAT_PROVIDER
        tool.mcp_tool_call.description = "Unavailable or pending tool"
    return tool


def partial_tool_call(
    call: ToolCall,
    *,
    model_call_id: str = "",
    args_text_delta: str = "",
) -> pb.AgentServerMessage:
    return server_interaction(
        pb.InteractionUpdate(
            partial_tool_call=pb.PartialToolCallUpdate(
                call_id=call.id,
                tool_call=tool_placeholder(call.name, call.id),
                args_text_delta=args_text_delta,
                model_call_id=model_call_id or call.id,
            )
        )
    )


def tool_call_started(call: ToolCall) -> pb.AgentServerMessage:
    return server_interaction(
        pb.InteractionUpdate(
            tool_call_started=pb.ToolCallStartedUpdate(
                call_id=call.id,
                tool_call=tool_placeholder(call.name, call.id),
                model_call_id=call.id,
            )
        )
    )


def tool_call_completed(call: ToolCall, *, content: str = "", is_error: bool = False) -> pb.AgentServerMessage:
    del content, is_error  # result payload filled by tool codec when available
    return server_interaction(
        pb.InteractionUpdate(
            tool_call_completed=pb.ToolCallCompletedUpdate(
                call_id=call.id,
                tool_call=tool_placeholder(call.name, call.id),
                model_call_id=call.id,
            )
        )
    )

def from_model_event(
    event: ModelEvent,
    *,
    model_call_id: str = "",
) -> pb.AgentServerMessage | None:
    """Map a normalized ModelEvent to an AgentServerMessage, or None to skip."""
    if event.kind is ModelEventKind.TEXT_DELTA and event.text:
        return text_delta(event.text)
    if event.kind is ModelEventKind.REASONING_DELTA and event.text:
        return thinking_delta(event.text)
    if event.kind is ModelEventKind.TOOL_CALL and event.tool_call is not None:
        return partial_tool_call(event.tool_call, model_call_id=model_call_id)
    if event.kind is ModelEventKind.END:
        return turn_ended(event.usage)
    if event.kind is ModelEventKind.USAGE and event.usage is not None:
        return None
    if event.kind is ModelEventKind.ERROR:
        # Surface as a text notice; dedicated error frames vary by Cursor build.
        return text_delta(event.error or "model error", is_server_notice=True)
    return None
