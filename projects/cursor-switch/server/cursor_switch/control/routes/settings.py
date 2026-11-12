"""Settings and harness routes."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request

from cursor_switch.adapters.persistence.repositories import (
    DesktopSettings,
    PortSettings,
    ProxySettings,
)
from cursor_switch.adapters.local_access.proxy import ProxyTrafficMode
from cursor_switch.control.schemas import (
    DesktopSettingsIn,
    HarnessEnabledIn,
    HarnessModeIn,
    HarnessStatusOut,
    PortSettingsIn,
    ProxySettingsIn,
    TrafficEventOut,
    TrafficLogOut,
)

router = APIRouter(prefix="/api", tags=["settings"])


def _harness_out(request: Request) -> HarnessStatusOut:
    status = request.app.state.services.harness.status()
    return HarnessStatusOut(
        enabled=status.enabled,
        ca=status.ca.value,
        integration="enabled" if status.enabled else "disabled",
        mode=status.mode.value,
        proxy_url=status.proxy.url,
        proxy_port=status.proxy.port,
        ca_install_command=status.ca_install_command,
    )


@router.get("/settings/ports", response_model=PortSettingsIn)
async def get_ports(request: Request) -> PortSettingsIn:
    ports = await request.app.state.services.settings.get_ports()
    return PortSettingsIn(proxy_port=ports.proxy_port, service_port=ports.service_port)


@router.put("/settings/ports", response_model=PortSettingsIn)
async def update_ports(payload: PortSettingsIn, request: Request) -> PortSettingsIn:
    ports = await request.app.state.services.settings.update_ports(
        PortSettings(proxy_port=payload.proxy_port, service_port=payload.service_port)
    )
    return PortSettingsIn(proxy_port=ports.proxy_port, service_port=ports.service_port)


@router.get("/settings/proxy", response_model=ProxySettingsIn)
async def get_proxy(request: Request) -> ProxySettingsIn:
    proxy = await request.app.state.services.settings.get_proxy()
    return ProxySettingsIn(
        mode=proxy.mode,
        address=proxy.address,
        auth_enabled=proxy.auth_enabled,
        username=proxy.username,
        password=proxy.password,
    )


@router.put("/settings/proxy", response_model=ProxySettingsIn)
async def update_proxy(payload: ProxySettingsIn, request: Request) -> ProxySettingsIn:
    proxy = await request.app.state.services.settings.update_proxy(
        ProxySettings(
            mode=payload.mode,
            address=payload.address,
            auth_enabled=payload.auth_enabled,
            username=payload.username,
            password=payload.password,
        )
    )
    return ProxySettingsIn(
        mode=proxy.mode,
        address=proxy.address,
        auth_enabled=proxy.auth_enabled,
        username=proxy.username,
        password=proxy.password,
    )


@router.get("/settings/desktop", response_model=DesktopSettingsIn)
async def get_desktop(request: Request) -> DesktopSettingsIn:
    desktop = await request.app.state.services.settings.get_desktop()
    return DesktopSettingsIn(
        silent_start=desktop.silent_start, show_dock_icon=desktop.show_dock_icon
    )


@router.put("/settings/desktop", response_model=DesktopSettingsIn)
async def update_desktop(payload: DesktopSettingsIn, request: Request) -> DesktopSettingsIn:
    desktop = await request.app.state.services.settings.update_desktop(
        DesktopSettings(
            silent_start=payload.silent_start, show_dock_icon=payload.show_dock_icon
        )
    )
    return DesktopSettingsIn(
        silent_start=desktop.silent_start, show_dock_icon=desktop.show_dock_icon
    )


@router.get("/harness/cursor/status", response_model=HarnessStatusOut)
async def harness_status(request: Request) -> HarnessStatusOut:
    return _harness_out(request)


@router.post("/harness/cursor/ca/initialize", response_model=HarnessStatusOut)
async def initialize_ca(request: Request) -> HarnessStatusOut:
    try:
        request.app.state.services.harness.initialize_ca()
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return _harness_out(request)


@router.put("/harness/cursor/enabled", response_model=HarnessStatusOut)
async def set_harness_enabled(payload: HarnessEnabledIn, request: Request) -> HarnessStatusOut:
    try:
        await request.app.state.services.harness.set_enabled(payload.enabled)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return _harness_out(request)


@router.put("/harness/cursor/mode", response_model=HarnessStatusOut)
async def set_harness_mode(payload: HarnessModeIn, request: Request) -> HarnessStatusOut:
    try:
        mode = ProxyTrafficMode(payload.mode)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail="mode must be passthrough or intercept",
        ) from error
    if request.app.state.services.harness.status().enabled and mode is ProxyTrafficMode.INTERCEPT:
        raise HTTPException(
            status_code=400,
            detail="disable takeover before switching to intercept",
        )
    await request.app.state.services.harness.set_mode(mode)
    return _harness_out(request)


@router.get("/harness/cursor/traffic", response_model=TrafficLogOut)
async def harness_traffic(request: Request, limit: int = 100) -> TrafficLogOut:
    events = request.app.state.services.local_access.proxy.traffic(limit=limit)
    return TrafficLogOut(events=[TrafficEventOut(**item) for item in events])


@router.delete("/harness/cursor/traffic", response_model=TrafficLogOut)
async def clear_harness_traffic(request: Request) -> TrafficLogOut:
    request.app.state.services.local_access.proxy.clear_traffic()
    return TrafficLogOut(events=[])
