"""Decode ExecClientMessage → ToolResult."""

from __future__ import annotations

import json

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.runtime.domain.types import ToolResult


def decode_exec_result(message: pb.ExecClientMessage, *, tool_call_id: str) -> ToolResult | None:
    """Return a ToolResult when the client message completes a tool; None if still streaming."""
    kind = message.WhichOneof("message")
    if kind is None:
        return None

    if kind == "read_result":
        result = message.read_result
        which = result.WhichOneof("result") or result.WhichOneof("message")
        # Generated oneof name may be empty; check known fields.
        if result.HasField("success") if _has(result, "success") else False:
            success = result.success
            content = getattr(success, "content", None) or getattr(success, "data", "") or ""
            if isinstance(content, bytes):
                content = content.decode("utf-8", errors="replace")
            return ToolResult(tool_call_id=tool_call_id, content=str(content))
        for err_field in ("error", "rejected", "file_not_found", "permission_denied", "invalid_file"):
            if _has(result, err_field) and result.HasField(err_field):
                return ToolResult(
                    tool_call_id=tool_call_id,
                    content=str(getattr(result, err_field)),
                    is_error=True,
                )
        return ToolResult(tool_call_id=tool_call_id, content=str(result), is_error=True)

    if kind == "shell_result":
        result = message.shell_result
        if _has(result, "success") and result.HasField("success"):
            success = result.success
            stdout = getattr(success, "stdout", "") or getattr(success, "output", "") or ""
            stderr = getattr(success, "stderr", "") or ""
            exit_code = getattr(success, "exit_code", 0)
            payload = {"exit_code": exit_code, "stdout": stdout, "stderr": stderr}
            return ToolResult(tool_call_id=tool_call_id, content=json.dumps(payload))
        for err_field in ("failure", "timeout", "rejected", "spawn_error", "permission_denied"):
            if _has(result, err_field) and result.HasField(err_field):
                return ToolResult(
                    tool_call_id=tool_call_id,
                    content=str(getattr(result, err_field)),
                    is_error=True,
                )
        return None  # may still be streaming via shell_stream

    if kind == "shell_stream":
        return None

    if kind == "delete_result":
        result = message.delete_result
        if _has(result, "success") and result.HasField("success"):
            return ToolResult(tool_call_id=tool_call_id, content="deleted")
        return ToolResult(tool_call_id=tool_call_id, content=str(result), is_error=True)

    if kind == "grep_result":
        result = message.grep_result
        if _has(result, "success") and result.HasField("success"):
            success = result.success
            # Prefer workspace_result / content fields when present.
            content = getattr(success, "workspace_result", None) or getattr(success, "content", None)
            if content is None:
                content = str(success)
            return ToolResult(tool_call_id=tool_call_id, content=str(content))
        return ToolResult(tool_call_id=tool_call_id, content=str(result), is_error=True)

    if kind == "write_result":
        result = message.write_result
        if _has(result, "success") and result.HasField("success"):
            return ToolResult(tool_call_id=tool_call_id, content="wrote")
        return ToolResult(tool_call_id=tool_call_id, content=str(result), is_error=True)

    if kind in {"mcp_result", "read_mcp_resource_exec_result", "list_mcp_resources_exec_result"}:
        return ToolResult(tool_call_id=tool_call_id, content=str(getattr(message, kind)))

    # Unknown completion shapes: treat as opaque content.
    return ToolResult(tool_call_id=tool_call_id, content=f"{kind}:{getattr(message, kind)}")


def _has(message: object, field: str) -> bool:
    try:
        return field in message.DESCRIPTOR.fields_by_name  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        return hasattr(message, field)
