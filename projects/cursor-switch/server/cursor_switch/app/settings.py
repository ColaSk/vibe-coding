"""Application service for ports, proxy, desktop, and harness settings."""

from __future__ import annotations

from cursor_switch.adapters.persistence.repositories import (
    DesktopSettings,
    HarnessSettings,
    PortSettings,
    ProxySettings,
)
from cursor_switch.adapters.persistence.unit_of_work import UnitOfWorkFactory


class SettingsService:
    def __init__(self, uow_factory: UnitOfWorkFactory) -> None:
        self._uow_factory = uow_factory

    async def get_ports(self) -> PortSettings:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json(
                "ports", {"proxy_port": 8788, "service_port": 8787}
            )
            return PortSettings(**raw)  # type: ignore[arg-type]

    async def update_ports(self, ports: PortSettings) -> PortSettings:
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json(
                "ports",
                {"proxy_port": ports.proxy_port, "service_port": ports.service_port},
            )
            return ports

    async def get_proxy(self) -> ProxySettings:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json(
                "proxy",
                {
                    "mode": "default",
                    "address": "",
                    "auth_enabled": False,
                    "username": "",
                    "password": "",
                },
            )
            return ProxySettings(**raw)  # type: ignore[arg-type]

    async def update_proxy(self, proxy: ProxySettings) -> ProxySettings:
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json(
                "proxy",
                {
                    "mode": proxy.mode,
                    "address": proxy.address,
                    "auth_enabled": proxy.auth_enabled,
                    "username": proxy.username,
                    "password": proxy.password,
                },
            )
            return proxy

    async def get_desktop(self) -> DesktopSettings:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json(
                "desktop", {"silent_start": False, "show_dock_icon": True}
            )
            return DesktopSettings(**raw)  # type: ignore[arg-type]

    async def update_desktop(self, desktop: DesktopSettings) -> DesktopSettings:
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json(
                "desktop",
                {
                    "silent_start": desktop.silent_start,
                    "show_dock_icon": desktop.show_dock_icon,
                },
            )
            return desktop

    async def get_harness(self) -> HarnessSettings:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json("harness", {"enabled": False})
            return HarnessSettings(**raw)  # type: ignore[arg-type]

    async def set_harness_enabled(self, enabled: bool) -> HarnessSettings:
        settings = HarnessSettings(enabled=enabled)
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("harness", {"enabled": enabled})
            return settings
