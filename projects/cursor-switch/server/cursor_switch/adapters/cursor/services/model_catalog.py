"""Project configured models into Cursor AvailableModels / GetUsableModels protobuf.

Official Cursor catalog is fetched upstream and local models are appended
(merge/add), matching cursor-byok behavior.
"""

from __future__ import annotations

import logging
import struct
from collections.abc import Awaitable, Callable, Mapping
from urllib.parse import urlparse

import httpx

from cursor_switch.adapters.cursor.proto_min import (
    encode_bool,
    encode_int64,
    encode_message_field,
    encode_string,
)
from cursor_switch.adapters.local_access.routing import UPSTREAM_URL_HEADER, is_cursor_host
from cursor_switch.adapters.persistence.repositories import ModelRecord

logger = logging.getLogger("cursor_switch.model_catalog")

CLI_LOCAL_API_KEY = "cursor-switch-local"
CURSOR_UPSTREAM = "https://api2.cursor.sh"

_HOP_BY_HOP = frozenset(
    {
        "proxy-connection",
        "connection",
        "keep-alive",
        "transfer-encoding",
        "te",
        "trailer",
        "upgrade",
        "host",
        "content-length",
        UPSTREAM_URL_HEADER,
    }
)

_CONTEXTS: tuple[tuple[str, str], ...] = (
    ("200k", "200K"),
    ("356k", "356K"),
    ("500k", "500K"),
    ("800k", "800K"),
    ("1m", "1M"),
)
_EFFORTS: tuple[tuple[str, str], ...] = (
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
    ("xhigh", "Extra High"),
    ("max", "Max"),
)
_DEFAULT_CONTEXT = "200k"


def _provider_host(base_url: str) -> str:
    host = urlparse(base_url.strip()).hostname
    return (host or base_url.strip() or "local").lower()


def _context_options(context_tokens: int) -> list[tuple[str, str]]:
    contexts = list(_CONTEXTS)
    if context_tokens > 0:
        value = str(context_tokens)
        if not any(existing == value for existing, _ in contexts):
            contexts.append((value, f"{context_tokens // 1000}K (Custom)"))
    return contexts


def _tooltip(display: str) -> bytes:
    return encode_string(7, f"**{display}**\n\nLocal model via cursor-switch.")


def _param_value(param_id: str, value: str) -> bytes:
    return encode_string(1, param_id) + encode_string(2, value)


def _enum_value(value: str, display: str) -> bytes:
    return encode_string(1, value) + encode_string(2, display)


def _boolean_parameter() -> bytes:
    false_value = encode_string(1, "false")
    true_value = (
        encode_string(1, "true")
        + encode_string(2, "Fast")
        + encode_bool(3, True)
    )
    values = encode_message_field(1, false_value) + encode_message_field(1, true_value)
    return encode_message_field(1, values)


def _enum_parameter(values: list[tuple[str, str]]) -> bytes:
    payload = bytearray()
    for value, display in values:
        payload.extend(encode_message_field(1, _enum_value(value, display)))
    return encode_message_field(2, bytes(payload))


def _parameter_definition(
    param_id: str,
    name: str,
    tooltip: str,
    parameter_type: bytes,
    *,
    cycleable: bool,
) -> bytes:
    parts = bytearray()
    parts.extend(encode_string(1, param_id))
    parts.extend(encode_string(2, name))
    parts.extend(encode_string(3, tooltip))
    parts.extend(encode_message_field(4, parameter_type))
    parts.extend(encode_bool(5, cycleable))
    return bytes(parts)


def _parameter_definitions(contexts: list[tuple[str, str]]) -> list[bytes]:
    return [
        _parameter_definition(
            "context",
            "Context",
            "Context size used to trigger conversation compaction.",
            _enum_parameter(contexts),
            cycleable=False,
        ),
        _parameter_definition(
            "reasoning",
            "Effort",
            "Effort the model uses to generate its response.",
            _enum_parameter(list(_EFFORTS)),
            cycleable=True,
        ),
        _parameter_definition(
            "fast",
            "Fast",
            "Significantly faster but consumes more usage",
            _boolean_parameter(),
            cycleable=False,
        ),
    ]


def _model_variant(
    name: str,
    display: str,
    tooltip: bytes,
    context: str,
    context_name: str,
    effort: str,
    effort_name: str,
    *,
    fast: bool,
) -> bytes:
    suffix_parts: list[str] = []
    if context != _DEFAULT_CONTEXT:
        suffix_parts.append(context_name)
    suffix_parts.append(effort_name)
    if fast:
        suffix_parts.append("Fast")
    suffix = " ".join(suffix_parts)
    shown = (
        display
        if not suffix
        else f'{display} <span style="color: var(--cursor-text-tertiary);">{suffix}</span>'
    )
    is_default = context == _DEFAULT_CONTEXT and effort == "high" and not fast
    parts = bytearray()
    parts.extend(encode_message_field(1, _param_value("context", context)))
    parts.extend(encode_message_field(1, _param_value("reasoning", effort)))
    parts.extend(encode_message_field(1, _param_value("fast", "true" if fast else "false")))
    parts.extend(encode_string(2, shown))
    parts.extend(encode_bool(3, False))  # is_max_mode
    if is_default:
        parts.extend(encode_bool(4, True))
        parts.extend(encode_bool(5, True))
    parts.extend(encode_message_field(6, tooltip))
    parts.extend(encode_string(8, shown))
    parts.extend(
        encode_string(
            9,
            f"{name}[context={context},reasoning={effort},fast={'true' if fast else 'false'}]",
        )
    )
    parts.extend(
        encode_string(
            11,
            f"{name}-{context}-{effort}{'-fast' if fast else ''}",
        )
    )
    return bytes(parts)


def _variants(name: str, display: str, tooltip: bytes, contexts: list[tuple[str, str]]) -> list[bytes]:
    out: list[bytes] = []
    for context, context_name in contexts:
        for effort, effort_name in _EFFORTS:
            for fast in (False, True):
                out.append(
                    _model_variant(
                        name,
                        display,
                        tooltip,
                        context,
                        context_name,
                        effort,
                        effort_name,
                        fast=fast,
                    )
                )
    return out


def _encode_available_model(row: ModelRecord) -> bytes:
    name = row.id
    display = row.display_name or row.model_name
    contexts = _context_options(row.context_tokens)
    tooltip = _tooltip(display)
    variants = _variants(name, display, tooltip, contexts)
    parts = bytearray()
    parts.extend(encode_string(1, name))
    parts.extend(encode_bool(2, True))  # default_on
    parts.extend(encode_bool(5, True))  # supports_agent
    parts.extend(encode_int64(6, 0))  # degradation_status
    parts.extend(encode_message_field(8, tooltip))
    parts.extend(encode_bool(9, True))  # supports_thinking
    parts.extend(encode_bool(10, True))  # supports_images
    parts.extend(encode_bool(14, True))  # supports_max_mode
    parts.extend(encode_string(17, display))  # client_display_name
    parts.extend(encode_string(18, name))  # server_model_name
    parts.extend(encode_bool(19, True))  # supports_non_max_mode
    parts.extend(encode_message_field(20, tooltip))
    parts.extend(encode_bool(21, False))  # background composer
    parts.extend(encode_bool(22, True))  # supports_plan_mode
    parts.extend(encode_string(24, display))  # inputbox_short_model_name
    parts.extend(encode_bool(25, True))  # supports_sandboxing
    parts.extend(encode_bool(26, False))  # supports_cmd_k
    for definition in _parameter_definitions(contexts):
        parts.extend(encode_message_field(29, definition))
    for variant in variants:
        parts.extend(encode_message_field(30, variant))
    for context, _ in contexts:
        for effort, _ in _EFFORTS:
            for fast in (False, True):
                parts.extend(
                    encode_string(
                        36,
                        f"{name}-{context}-{effort}{'-fast' if fast else ''}",
                    )
                )
    parts.extend(encode_int64(38, 1))  # named_model_section_index
    vendor_label = _provider_host(row.base_url)
    parts.extend(encode_string(41, vendor_label))
    parts.extend(
        encode_message_field(
            42,
            encode_int64(1, 6) + encode_string(2, vendor_label),
        )
    )
    badge = (
        encode_string(1, vendor_label)
        + encode_int64(2, 1)
        + encode_bool(3, False)
    )
    parts.extend(encode_message_field(48, badge))
    return bytes(parts)


def _encode_model_details(row: ModelRecord) -> bytes:
    name = row.id
    display = row.display_name or row.model_name
    credentials = encode_string(1, CLI_LOCAL_API_KEY)
    parts = bytearray()
    parts.extend(encode_string(1, name))  # model_id
    parts.extend(encode_message_field(2, b""))  # thinking_details empty
    parts.extend(encode_string(3, name))  # display_model_id
    parts.extend(encode_string(4, display))
    parts.extend(encode_string(5, display))
    parts.extend(encode_message_field(8, credentials))  # api_key_credentials
    return bytes(parts)


def encode_available_models(rows: list[ModelRecord]) -> bytes:
    parts = bytearray()
    for row in rows:
        parts.extend(encode_string(1, row.id))
    for row in rows:
        parts.extend(encode_message_field(2, _encode_available_model(row)))
    return bytes(parts)


def encode_usable_models(rows: list[ModelRecord]) -> bytes:
    parts = bytearray()
    for row in rows:
        parts.extend(encode_message_field(1, _encode_model_details(row)))
    return bytes(parts)


def encode_default_model(rows: list[ModelRecord]) -> bytes:
    model_id = rows[0].id if rows else ""
    parts = bytearray()
    if model_id:
        parts.extend(encode_string(1, model_id))
        parts.extend(encode_string(2, model_id))
    parts.extend(encode_bool(3, False))
    parts.extend(encode_string(4, ""))
    return bytes(parts)


def encode_default_model_for_cli(rows: list[ModelRecord]) -> bytes:
    if not rows:
        return b""
    return encode_message_field(1, _encode_model_details(rows[0]))


def encode_default_model_nudge(rows: list[ModelRecord]) -> bytes:
    parts = bytearray()
    parts.extend(encode_string(1, "0"))
    parts.extend(encode_bool(2, False))
    for row in rows:
        parts.extend(encode_string(3, row.id))
    parts.extend(encode_string(4, ""))
    return bytes(parts)


def merge_catalog_payload(upstream_body: bytes, local_addition: bytes) -> bytes:
    """Append local protobuf fields onto an upstream catalog body.

    Preserves Connect unary framing when present. Falls back to raw concat when
    the body is unframed. Raises ValueError for compressed frames.
    """
    if not local_addition:
        return upstream_body
    if len(upstream_body) >= 5:
        flags = upstream_body[0]
        length = struct.unpack(">I", upstream_body[1:5])[0]
        if length == len(upstream_body) - 5:
            if flags != 0:
                raise ValueError(f"cannot merge compressed catalog frame: flags={flags}")
            payload = upstream_body[5:]
            merged = payload + local_addition
            return bytes([0]) + struct.pack(">I", len(merged)) + merged
    return upstream_body + local_addition


def _header(headers: Mapping[str, str], name: str) -> str:
    wanted = name.lower()
    for key, value in headers.items():
        if key.lower() == wanted:
            return value
    return ""


def resolve_upstream_url(path: str, headers: Mapping[str, str]) -> str:
    stamped = _header(headers, UPSTREAM_URL_HEADER).strip()
    if stamped:
        parsed = urlparse(stamped)
        host = (parsed.hostname or "").lower()
        if parsed.scheme == "https" and is_cursor_host(host):
            return stamped
    route = path if path.startswith("/") else f"/{path}"
    return f"{CURSOR_UPSTREAM}{route}"


async def fetch_upstream_catalog(
    *,
    path: str,
    headers: Mapping[str, str],
    body: bytes,
    client: httpx.AsyncClient | None = None,
) -> bytes | None:
    """Fetch official Cursor catalog; return None when upstream is unavailable."""
    url = resolve_upstream_url(path, headers)
    outbound = {
        key: value
        for key, value in headers.items()
        if key.lower() not in _HOP_BY_HOP
    }
    outbound["connect-accept-encoding"] = "identity"
    outbound["accept-encoding"] = "identity"
    owns_client = client is None
    http = client or httpx.AsyncClient(timeout=20.0, follow_redirects=False)
    try:
        response = await http.post(url, headers=outbound, content=body)
        if response.status_code >= 400:
            logger.warning(
                "Cursor catalog upstream rejected %s with %s",
                path,
                response.status_code,
            )
            return None
        return response.content
    except httpx.HTTPError as exc:
        logger.warning("Cursor catalog upstream unavailable for %s: %s", path, exc)
        return None
    finally:
        if owns_client:
            await http.aclose()


class ModelCatalog:
    def __init__(
        self,
        list_models: Callable[[], Awaitable[list[ModelRecord]]],
        *,
        upstream_fetch: Callable[..., Awaitable[bytes | None]] | None = None,
    ) -> None:
        self._list_models = list_models
        self._upstream_fetch = upstream_fetch or fetch_upstream_catalog

    async def _enabled(self) -> list[ModelRecord]:
        return [row for row in await self._list_models() if row.enabled]

    async def _merged(
        self,
        local: bytes,
        *,
        path: str,
        headers: Mapping[str, str],
        body: bytes,
    ) -> bytes:
        upstream = await self._upstream_fetch(path=path, headers=headers, body=body)
        if upstream is None:
            return local
        try:
            return merge_catalog_payload(upstream, local)
        except ValueError as exc:
            logger.warning("cannot merge Cursor catalog for %s: %s", path, exc)
            return local

    async def available_models_proto(
        self,
        *,
        path: str = "/aiserver.v1.AiService/AvailableModels",
        headers: Mapping[str, str] | None = None,
        body: bytes = b"",
    ) -> bytes:
        local = encode_available_models(await self._enabled())
        return await self._merged(local, path=path, headers=headers or {}, body=body)

    async def usable_models_proto(
        self,
        *,
        path: str = "/aiserver.v1.AiService/GetUsableModels",
        headers: Mapping[str, str] | None = None,
        body: bytes = b"",
    ) -> bytes:
        local = encode_usable_models(await self._enabled())
        return await self._merged(local, path=path, headers=headers or {}, body=body)

    async def default_model_proto(self) -> bytes:
        return encode_default_model(await self._enabled())

    async def default_model_for_cli_proto(self) -> bytes:
        return encode_default_model_for_cli(await self._enabled())

    async def default_model_nudge_proto(self) -> bytes:
        return encode_default_model_nudge(await self._enabled())
