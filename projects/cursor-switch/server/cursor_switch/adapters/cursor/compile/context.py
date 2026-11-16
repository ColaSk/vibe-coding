"""Hydrate rules / skills / MCP / blob text from AgentRunRequest-shaped bytes."""

from __future__ import annotations

from dataclasses import dataclass, field

from cursor_switch.adapters.cursor.pb import agent_v1_pb2 as pb
from cursor_switch.adapters.cursor.proto_min import iter_fields


@dataclass
class ContextBundle:
    rules_xml: str = ""
    skills_xml: str = ""
    mcp_xml: str = ""
    environment_xml: str = ""
    user_text: str = ""
    system_suffix: str = ""
    images: list[bytes] = field(default_factory=list)

    def as_system_suffix(self) -> str:
        parts = [
            p
            for p in (
                self.rules_xml,
                self.skills_xml,
                self.mcp_xml,
                self.environment_xml,
                self.system_suffix,
            )
            if p.strip()
        ]
        return "\n\n".join(parts)


def _field_bytes(data: bytes, field_no: int) -> bytes | None:
    for field, wire, value in iter_fields(data):
        if field == field_no and wire == 2 and isinstance(value, bytes):
            return value
    return None


def _field_string(data: bytes, field_no: int) -> str:
    raw = _field_bytes(data, field_no)
    return raw.decode("utf-8", errors="replace") if raw else ""


def _safe_has(msg: object, name: str) -> bool:
    try:
        return bool(msg.HasField(name))  # type: ignore[attr-defined]
    except Exception:  # noqa: BLE001
        return hasattr(msg, name) and bool(getattr(msg, name))


def hydrate_request_context(
    *,
    run_request: bytes | None = None,
    agent_client: pb.AgentClientMessage | None = None,
    blob_lookup: dict[str, bytes] | None = None,
) -> ContextBundle:
    """Best-effort context hydration from AgentRunRequest / ConversationAction."""
    bundle = ContextBundle()
    blobs = dict(blob_lookup or {})

    request: pb.AgentRunRequest | None = None
    if agent_client is not None and agent_client.WhichOneof("message") == "run_request":
        request = agent_client.run_request
    elif run_request:
        try:
            request = pb.AgentRunRequest()
            request.ParseFromString(run_request)
        except Exception:  # noqa: BLE001
            request = None

    if request is None:
        return bundle

    # Prefetched blobs on the run request (when present).
    for blob in getattr(request, "pre_fetched_blobs", []) or []:
        blob_id = getattr(blob, "blob_id", "") or getattr(blob, "id", "") or ""
        data = getattr(blob, "data", b"") or b""
        if blob_id and data:
            blobs[blob_id] = data

    action = request.action if _safe_has(request, "action") else None
    if action is not None and _safe_has(action, "user_message_action"):
        user_action = action.user_message_action
        user_msg = user_action.user_message if _safe_has(user_action, "user_message") else None
        if user_msg is not None:
            bundle.user_text = getattr(user_msg, "text", "") or ""
            blob_id = getattr(user_msg, "text_blob_id", "") or ""
            if not bundle.user_text and blob_id and blob_id in blobs:
                bundle.user_text = blobs[blob_id].decode("utf-8", errors="replace")
            for image in getattr(user_msg, "images", []) or []:
                data = getattr(image, "data", b"") or b""
                if data:
                    bundle.images.append(data)

    # Custom system prompt on the run request.
    custom = getattr(request, "custom_system_prompt", "") or ""
    if custom:
        bundle.system_suffix = custom

    # MCP tools advertised on the run request (message or repeated).
    mcp_bits = []
    mcp_tools = getattr(request, "mcp_tools", None)
    tool_iter = []
    if mcp_tools is None:
        tool_iter = []
    elif isinstance(mcp_tools, (list, tuple)):
        tool_iter = list(mcp_tools)
    else:
        nested = getattr(mcp_tools, "tools", None) or getattr(mcp_tools, "mcp_tools", None)
        if nested is not None:
            try:
                tool_iter = list(nested)
            except TypeError:
                tool_iter = []
        else:
            name = getattr(mcp_tools, "name", "") or ""
            if name:
                tool_iter = [mcp_tools]
    for tool in tool_iter:
        name = getattr(tool, "name", "") or getattr(tool, "tool_name", "") or "mcp"
        mcp_bits.append(f"<mcp_tool>{name}</mcp_tool>")
    if mcp_bits:
        bundle.mcp_xml = "<mcp>\n" + "\n".join(mcp_bits) + "\n</mcp>"

    # ConversationAction may carry request_context_* parts on some builds.
    if action is not None:
        for attr in ("request_context", "request_context_parts"):
            if not hasattr(action, attr):
                continue
            ctx = getattr(action, attr)
            if ctx is None:
                continue
            rules = []
            for rule in getattr(ctx, "rules", []) or []:
                content = getattr(rule, "content", "") or getattr(rule, "body", "") or ""
                name = getattr(rule, "name", "") or getattr(rule, "full_path", "") or "rule"
                if content:
                    rules.append(f'<rule name="{name}">\n{content}\n</rule>')
            if rules:
                bundle.rules_xml = "<rules>\n" + "\n".join(rules) + "\n</rules>"
            skills = []
            for skill in getattr(ctx, "agent_skills", []) or []:
                content = getattr(skill, "content", "") or ""
                path = getattr(skill, "full_path", "") or "skill"
                if content:
                    skills.append(f'<agent_skill path="{path}">\n{content}\n</agent_skill>')
            if skills:
                bundle.skills_xml = "<agent_skills>\n" + "\n".join(skills) + "\n</agent_skills>"

    return bundle


def extract_user_text_with_blobs(
    user_message_action: bytes,
    *,
    blob_lookup: dict[str, bytes] | None = None,
) -> str:
    """Legacy path: walk UserMessageAction bytes for text / text_blob_id."""
    blobs = blob_lookup or {}
    user_message = _field_bytes(user_message_action, 1) or b""
    text = _field_string(user_message, 1)
    if text:
        return text
    blob_id = _field_string(user_message, 18)
    if blob_id and blob_id in blobs:
        return blobs[blob_id].decode("utf-8", errors="replace")
    return ""
