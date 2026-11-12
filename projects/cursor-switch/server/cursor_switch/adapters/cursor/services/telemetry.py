"""Null-object telemetry responses for Cursor analytics / observability RPCs."""

from __future__ import annotations


class NullTelemetry:
    def bootstrap_statsig(self) -> bytes:
        return b"{}"

    def empty_ok(self) -> bytes:
        return b""
