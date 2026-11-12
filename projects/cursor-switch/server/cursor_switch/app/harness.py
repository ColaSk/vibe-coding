"""Harness application service for Cursor takeover."""

from __future__ import annotations

from cursor_switch.adapters.local_access.facade import LocalAccessFacade, LocalAccessStatus
from cursor_switch.adapters.local_access.proxy import ProxyTrafficMode
from cursor_switch.adapters.persistence.unit_of_work import UnitOfWorkFactory

DEFAULT_PROXY_PORT = 8788
DEFAULT_SERVICE_PORT = 8787


class HarnessService:
    def __init__(
        self,
        local_access: LocalAccessFacade,
        uow_factory: UnitOfWorkFactory,
    ) -> None:
        self._local_access = local_access
        self._uow_factory = uow_factory

    def status(self) -> LocalAccessStatus:
        return self._local_access.status()

    def initialize_ca(self) -> LocalAccessStatus:
        return self._local_access.initialize_ca()

    async def set_mode(self, mode: ProxyTrafficMode) -> LocalAccessStatus:
        async with self._uow_factory.begin() as uow:
            current = await uow.settings.get_json("harness", {"enabled": False, "mode": "passthrough"})
            current["mode"] = mode.value
            await uow.settings.put_json("harness", current)
        return self._local_access.set_mode(mode)

    async def set_enabled(self, enabled: bool) -> LocalAccessStatus:
        async with self._uow_factory.begin() as uow:
            ports = await uow.settings.get_json(
                "ports",
                {"proxy_port": DEFAULT_PROXY_PORT, "service_port": DEFAULT_SERVICE_PORT},
            )
            harness = await uow.settings.get_json(
                "harness", {"enabled": False, "mode": ProxyTrafficMode.PASSTHROUGH.value}
            )
            mode_raw = str(harness.get("mode") or ProxyTrafficMode.PASSTHROUGH.value)
            try:
                mode = ProxyTrafficMode(mode_raw)
            except ValueError:
                mode = ProxyTrafficMode.PASSTHROUGH
            self._local_access.set_mode(mode)
            proxy_port = int(ports.get("proxy_port", DEFAULT_PROXY_PORT) or DEFAULT_PROXY_PORT)
            service_port = int(ports.get("service_port", DEFAULT_SERVICE_PORT) or DEFAULT_SERVICE_PORT)
            status = await self._local_access.set_enabled(
                enabled,
                proxy_port=proxy_port,
                service_port=service_port,
            )
            await uow.settings.put_json(
                "harness",
                {"enabled": enabled, "mode": self._local_access.proxy.mode.value},
            )
        return status
