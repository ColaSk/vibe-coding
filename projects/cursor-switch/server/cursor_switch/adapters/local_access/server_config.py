"""One gate for Cursor GetServerConfig.

The desktop restarts its extension host whenever a refreshed server config
carries a different agent URL. Every config response this process returns is
the first normalized body, with the agent host pinned to the client's default.
"""

from __future__ import annotations

import gzip

# Built-in default the running Cursor desktop already uses.
CLIENT_AGENT_HOST = b"agentn.api5.cursor.sh"
_UPSTREAM_AGENT_HOST = b"agentn.global.api5.cursor.sh"


def _pin_host(payload: bytes) -> bytes:
    pairs = (
        (b"https://" + _UPSTREAM_AGENT_HOST, b"https://" + CLIENT_AGENT_HOST),
        (_UPSTREAM_AGENT_HOST, CLIENT_AGENT_HOST),
    )
    current = payload
    for old, new in pairs:
        if old not in current:
            continue
        out = bytearray()
        index = 0
        while True:
            found = current.find(old, index)
            if found < 0:
                out.extend(current[index:])
                break
            if found > 0 and current[found - 1] == len(old):
                out.extend(current[index : found - 1])
                out.append(len(new))
            else:
                out.extend(current[index:found])
            out.extend(new)
            index = found + len(old)
        current = bytes(out)
    return current


def _rewrite_frame(payload: bytes) -> bytes:
    if len(payload) >= 5 and payload[0] in (0, 1):
        message_len = int.from_bytes(payload[1:5], "big")
        if message_len == len(payload) - 5:
            message = payload[5:]
            compressed = payload[0] == 1
            if compressed:
                try:
                    message = gzip.decompress(message)
                except OSError:
                    compressed = False
            rewritten = _pin_host(message)
            if compressed:
                rewritten = gzip.compress(rewritten)
            return bytes([payload[0]]) + len(rewritten).to_bytes(4, "big") + rewritten
    return _pin_host(payload)


class ServerConfigGate:
    """Return one stable GetServerConfig body for the life of the proxy."""

    def __init__(self) -> None:
        self._body: bytes | None = None

    def response(self, upstream: bytes) -> bytes:
        if self._body is None and upstream:
            self._body = _rewrite_frame(upstream)
        return self._body if self._body is not None else upstream
