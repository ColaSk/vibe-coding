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
    CommitSettingsIn,
    CursorPathIn,
    CursorPathOut,
    DesktopSettingsIn,
    HarnessEnabledIn,
    ObservationIn,
    PricingIn,
    TabSettingsIn,
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


@router.get("/settings/observation", response_model=ObservationIn)
async def get_observation(request: Request) -> ObservationIn:
    return ObservationIn(detailed=await request.app.state.services.settings.get_detailed())


@router.put("/settings/observation", response_model=ObservationIn)
async def update_observation(payload: ObservationIn, request: Request) -> ObservationIn:
    detailed = await request.app.state.services.settings.set_detailed(payload.detailed)
    return ObservationIn(detailed=detailed)


@router.get("/settings/tab", response_model=TabSettingsIn)
async def get_tab(request: Request) -> TabSettingsIn:
    tab = await request.app.state.services.settings.get_tab()
    return TabSettingsIn(mode=tab["mode"], address=tab["address"])


@router.put("/settings/tab", response_model=TabSettingsIn)
async def update_tab(payload: TabSettingsIn, request: Request) -> TabSettingsIn:
    if payload.mode not in {"direct", "custom"}:
        raise HTTPException(status_code=400, detail="mode must be direct or custom")
    if payload.mode == "custom" and not payload.address.strip():
        raise HTTPException(status_code=400, detail="TAB 服务地址不能为空")
    saved = await request.app.state.services.settings.set_tab(payload.mode, payload.address.strip())
    proxy = request.app.state.services.local_access.proxy
    proxy.tab_mode = saved["mode"]
    proxy.tab_address = saved["address"]
    return TabSettingsIn(mode=saved["mode"], address=saved["address"])


@router.get("/settings/cursor-path", response_model=CursorPathOut)
async def get_cursor_path(request: Request) -> CursorPathOut:
    from cursor_switch.adapters.local_access.cursor_settings import settings_path

    configured = await request.app.state.services.settings.get_cursor_path()
    request.app.state.services.local_access.set_cursor_settings_configured(configured)
    return CursorPathOut(
        path=configured,
        default_path=str(settings_path()),
        effective_path=str(request.app.state.services.local_access.cursor_settings_path()),
    )


@router.put("/settings/cursor-path", response_model=CursorPathOut)
async def update_cursor_path(payload: CursorPathIn, request: Request) -> CursorPathOut:
    from cursor_switch.adapters.local_access.cursor_settings import settings_path

    if request.app.state.services.harness.status().enabled:
        raise HTTPException(status_code=400, detail="请先关闭接管，再修改 Cursor 路径")
    saved = await request.app.state.services.settings.set_cursor_path(payload.path)
    effective = request.app.state.services.local_access.set_cursor_settings_configured(saved)
    return CursorPathOut(
        path=saved,
        default_path=str(settings_path()),
        effective_path=str(effective),
    )


@router.get("/settings/commit", response_model=CommitSettingsIn)
async def get_commit(request: Request) -> CommitSettingsIn:
    return CommitSettingsIn(model_id=await request.app.state.services.settings.get_commit_model())


@router.put("/settings/commit", response_model=CommitSettingsIn)
async def update_commit(payload: CommitSettingsIn, request: Request) -> CommitSettingsIn:
    model_id = await request.app.state.services.settings.set_commit_model(payload.model_id)
    return CommitSettingsIn(model_id=model_id)


@router.get("/settings/pricing", response_model=PricingIn)
async def get_pricing(request: Request) -> PricingIn:
    raw = await request.app.state.services.settings.get_pricing()
    return PricingIn(
        input_per_million=float(raw.get("input_per_million") or 0),
        output_per_million=float(raw.get("output_per_million") or 0),
        cache_read_per_million=float(raw.get("cache_read_per_million") or 0),
        cache_write_per_million=float(raw.get("cache_write_per_million") or 0),
    )


@router.put("/settings/pricing", response_model=PricingIn)
async def update_pricing(payload: PricingIn, request: Request) -> PricingIn:
    saved = await request.app.state.services.settings.set_pricing(payload.model_dump())
    return PricingIn(**saved)


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
