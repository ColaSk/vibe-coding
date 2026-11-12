"""Cursor-facing service facades."""

from cursor_switch.adapters.cursor.services.account import AccountFacade
from cursor_switch.adapters.cursor.services.knowledge import KnowledgeStore
from cursor_switch.adapters.cursor.services.model_catalog import ModelCatalog
from cursor_switch.adapters.cursor.services.telemetry import NullTelemetry

__all__ = [
    "AccountFacade",
    "KnowledgeStore",
    "ModelCatalog",
    "NullTelemetry",
]
