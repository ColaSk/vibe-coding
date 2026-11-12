"""Tool dispatch port."""

from __future__ import annotations

from typing import Protocol

from cursor_switch.runtime.domain.types import ToolCall, ToolResult


class ToolHandle(Protocol):
    async def result(self) -> ToolResult:
        """Wait for the tool to finish."""

    async def cancel(self) -> None:
        """Request cancellation of the in-flight tool."""


class ToolPort(Protocol):
    async def dispatch(self, call: ToolCall) -> ToolHandle:
        """Start a tool call and return a handle."""
