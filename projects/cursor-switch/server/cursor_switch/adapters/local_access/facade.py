"""Facade over CA and Cursor TLS proxy."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cursor_switch.adapters.local_access.ca import CaManager, CaState
from cursor_switch.adapters.local_access.cursor_settings import apply_proxy, clear_proxy
from cursor_switch.adapters.local_access.proxy import CursorProxy, ProxyStatus, ProxyTrafficMode


@dataclass(frozen=True, slots=True)
class LocalAccessStatus:
    ca: CaState
    ca_install_command: str | None
    proxy: ProxyStatus
    enabled: bool
    mode: ProxyTrafficMode


class LocalAccessFacade:
    def __init__(
        self,
        ca: CaManager | None = None,
        proxy: CursorProxy | None = None,
        *,
        cursor_settings_path: Path | None = None,
    ) -> None:
        self.ca = ca or CaManager()
        self.proxy = proxy or CursorProxy(self.ca)
        self._cursor_settings_path = cursor_settings_path
        self._enabled = False

    def status(self) -> LocalAccessStatus:
        return LocalAccessStatus(
            ca=self.ca.state(),
            ca_install_command=self.ca.install_command(),
            proxy=self.proxy.status,
            enabled=self._enabled,
            mode=self.proxy.mode,
        )

    def initialize_ca(self) -> LocalAccessStatus:
        self.ca.initialize()
        return self.status()

    def set_mode(self, mode: ProxyTrafficMode) -> LocalAccessStatus:
        self.proxy.set_mode(mode)
        return self.status()

    async def set_enabled(self, enabled: bool, *, proxy_port: int, service_port: int) -> LocalAccessStatus:
        self.proxy.set_backend("127.0.0.1", service_port)
        if enabled:
            if self.proxy.mode is ProxyTrafficMode.INTERCEPT:
                state = self.ca.state()
                if state is CaState.MISSING:
                    self.ca.initialize()
                    state = self.ca.state()
                if state in {CaState.MISSING, CaState.INVALID}:
                    raise ValueError("CA is not ready")
                if state is CaState.UNTRUSTED:
                    command = self.ca.install_command() or ""
                    raise ValueError(
                        "CA is generated but not trusted by the system. "
                        f"Install it first, then enable intercept. {command}".strip()
                    )
            await self.proxy.start(proxy_port)
            url = self.proxy.status.url
            if not url:
                await self.proxy.stop()
                raise ValueError("proxy started without a URL")
            try:
                apply_proxy(url, self._cursor_settings_path)
            except Exception:
                await self.proxy.stop()
                raise
            self._enabled = True
        else:
            clear_proxy(self._cursor_settings_path)
            await self.proxy.stop()
            self._enabled = False
        return self.status()
