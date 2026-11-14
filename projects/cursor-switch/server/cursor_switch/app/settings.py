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

    async def get_detailed(self) -> bool:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json("observation", {"detailed": False})
            return bool(raw.get("detailed"))

    async def set_detailed(self, detailed: bool) -> bool:
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("observation", {"detailed": detailed})
            return detailed

    async def get_tab(self) -> dict[str, str]:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json("tab", {"mode": "direct", "address": ""})
            mode = str(raw.get("mode") or "direct")
            if mode == "public":
                mode = "direct"
            return {"mode": mode, "address": str(raw.get("address") or "")}

    async def set_tab(self, mode: str, address: str) -> dict[str, str]:
        value = {"mode": mode, "address": address}
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("tab", value)
            return value

    async def get_cursor_path(self) -> str:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json("cursor_path", {"path": ""})
            return str(raw.get("path") or "")

    async def set_cursor_path(self, path: str) -> str:
        value = path.strip()
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("cursor_path", {"path": value})
            return value

    async def get_commit_model(self) -> str:
        async with self._uow_factory.begin() as uow:
            raw = await uow.settings.get_json("commit", {"model_id": ""})
            return str(raw.get("model_id") or "")

    async def set_commit_model(self, model_id: str) -> str:
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("commit", {"model_id": model_id})
            return model_id

    async def get_pricing(self) -> dict[str, object]:
        async with self._uow_factory.begin() as uow:
            return await uow.settings.get_json(
                "pricing",
                {
                    "input_per_million": 5.0,
                    "output_per_million": 25.0,
                    "cache_read_per_million": 0.5,
                    "cache_write_per_million": 6.25,
                },
            )

    async def set_pricing(self, pricing: dict[str, object]) -> dict[str, object]:
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("pricing", pricing)
            return pricing

    async def set_harness_enabled(self, enabled: bool) -> HarnessSettings:
        settings = HarnessSettings(enabled=enabled)
        async with self._uow_factory.begin() as uow:
            await uow.settings.put_json("harness", {"enabled": enabled})
            return settings
