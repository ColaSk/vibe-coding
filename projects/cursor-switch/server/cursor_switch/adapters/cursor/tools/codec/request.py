"""Encode ToolCall → AgentServerMessage(ExecServerMessage)."""

from __future__ import annotations

from typing import Any

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.runtime.domain.types import ToolCall


def normalize(name: str) -> str:
    return name.strip().lower()


def _arg_str(call: ToolCall, *names: str, default: str | None = None) -> str:
    for name in names:
        value = call.arguments.get(name)
        if isinstance(value, str) and value:
            return value
    if default is not None:
        return default
    raise ValueError(f"{call.name} missing {names[0]}")


def _arg_int(call: ToolCall, name: str) -> int | None:
    value = call.arguments.get(name)
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        return int(value)
    return None


def encode_exec_request(
    call: ToolCall,
    *,
    exec_id_num: int = 1,
    conversation_id: str = "",
) -> pb.AgentServerMessage:
    """Build ExecServerMessage for tools Cursor executes locally."""
    key = normalize(call.name)
    if key in {"shell", "bash"}:
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            accept_hook_additional_contexts=True,
            shell_stream_args=pb.ShellArgs(
                command=_arg_str(call, "command"),
                working_directory=str(call.arguments.get("working_directory") or ""),
                timeout=_arg_int(call, "timeout") or 30_000,
                tool_call_id=call.id,
                description=str(call.arguments.get("description") or "") or None,
                conversation_id=conversation_id or None,
                close_stdin=True,
                file_output_threshold_bytes=40_000,
                hard_timeout=86_400_000,
            ),
        )
    elif key == "read":
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            accept_hook_additional_contexts=True,
            read_args=pb.ReadArgs(
                path=_arg_str(call, "path", "file_path", "filePath"),
                tool_call_id=call.id,
                offset=_arg_int(call, "offset"),
                limit=_arg_int(call, "limit"),
            ),
        )
    elif key == "delete":
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            accept_hook_additional_contexts=True,
            delete_args=pb.DeleteArgs(
                path=_arg_str(call, "path", "file_path", "filePath"),
                tool_call_id=call.id,
            ),
        )
    elif key == "grep":
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            accept_hook_additional_contexts=True,
            grep_args=pb.GrepArgs(
                pattern=_arg_str(call, "pattern"),
                path=str(call.arguments.get("path") or "") or None,
                glob=str(call.arguments.get("glob") or "") or None,
                tool_call_id=call.id,
                head_limit=_arg_int(call, "head_limit"),
            ),
        )
    elif key == "glob":
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            accept_hook_additional_contexts=True,
            grep_args=pb.GrepArgs(
                pattern="",
                path=str(call.arguments.get("target_directory") or "") or None,
                glob=str(call.arguments.get("glob_pattern") or call.arguments.get("pattern") or "")
                or None,
                output_mode="files_with_matches",
                tool_call_id=call.id,
            ),
        )
    elif key in {"getmcptools", "callmcptool"}:
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            mcp_args=pb.McpArgs(
                name=call.name,
                tool_call_id=call.id,
                tool_name=str(call.arguments.get("toolName") or call.arguments.get("tool_name") or call.name),
                provider_identifier=str(call.arguments.get("server") or "mcp"),
                server_identifier=str(call.arguments.get("server") or ""),
            ),
        )
    elif key == "fetchmcpresource":
        message = pb.ExecServerMessage(
            id=exec_id_num,
            exec_id=call.id,
            read_mcp_resource_exec_args=pb.ReadMcpResourceExecArgs(
                server=_arg_str(call, "server"),
                uri=_arg_str(call, "uri"),
                tool_call_id=call.id,
            ),
        )
    else:
        raise ValueError(f"tool {call.name} is not executed through ExecServerMessage")

    return pb.AgentServerMessage(exec_server_message=message)


def is_client_exec_tool(name: str) -> bool:
    key = normalize(name)
    return key in {
        "shell",
        "bash",
        "read",
        "delete",
        "grep",
        "glob",
        "readlints",
        "task",
        "getmcptools",
        "callmcptool",
        "fetchmcpresource",
    }


def is_interaction_tool(name: str) -> bool:
    key = normalize(name)
    return key in {
        "askquestion",
        "websearch",
        "webfetch",
        "switchmode",
        "createplan",
        "generateimage",
    }


def encode_interaction_query(call: ToolCall, *, query_id: int = 1) -> pb.AgentServerMessage:
    """Ask Cursor UI to run an interactive tool (best-effort generic query)."""
    # Prefer a dedicated InteractionQuery shape when present; fall back to MCP args exec.
    args: dict[str, Any] = dict(call.arguments)
    args.setdefault("name", call.name)
    try:
        query = pb.InteractionQuery()
        # Field layout varies; set common string fields if available.
        if hasattr(query, "id"):
            query.id = query_id
        return pb.AgentServerMessage(interaction_query=query)
    except Exception:  # noqa: BLE001
        return encode_exec_request(call, exec_id_num=query_id)
