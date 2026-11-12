"""Local CA, TLS proxy, and official fallback."""

from cursor_switch.adapters.local_access.ca import CaManager, CaState
from cursor_switch.adapters.local_access.cursor_settings import apply_proxy, clear_proxy
from cursor_switch.adapters.local_access.facade import LocalAccessFacade, LocalAccessStatus
from cursor_switch.adapters.local_access.proxy import CursorProxy
from cursor_switch.adapters.local_access.routing import is_cursor_host, should_route_locally

__all__ = [
    "CaManager",
    "CaState",
    "CursorProxy",
    "LocalAccessFacade",
    "LocalAccessStatus",
    "apply_proxy",
    "clear_proxy",
    "is_cursor_host",
    "should_route_locally",
]
