"""Outbound transport port for streaming events to a client."""

from __future__ import annotations

from typing import Protocol

from cursor_switch.runtime.domain.types import ModelEvent


class TransportPort(Protocol):
    async def publish(self, request_id: str, event: ModelEvent) -> None:
        """Send one normalized event to the bound client stream."""

    async def close(self, request_id: str) -> None:
        """Close the client stream for a request."""
