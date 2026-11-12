"""Pydantic DTOs for the control plane."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ModelInput(BaseModel):
    display_name: str
    provider_type: str = Field(pattern="^(openai_chat|openai_responses|anthropic)$")
    base_url: str
    api_key: str = ""
    model_name: str
    notes: str = ""
    context_tokens: int = 128_000
    max_output_tokens: int = 8_192
    enabled: bool = True
    sort_order: int = 0
    extra: dict[str, object] = Field(default_factory=dict)
    headers: dict[str, str] = Field(default_factory=dict)


class ModelOut(ModelInput):
    id: str


class ReorderInput(BaseModel):
    ordered_ids: list[str]


class PortSettingsIn(BaseModel):
    proxy_port: int = 8788
    service_port: int = 8787


class ProxySettingsIn(BaseModel):
    mode: str = "default"
    address: str = ""
    auth_enabled: bool = False
    username: str = ""
    password: str = ""


class DesktopSettingsIn(BaseModel):
    silent_start: bool = False
    show_dock_icon: bool = True


class HarnessStatusOut(BaseModel):
    enabled: bool
    ca: str = "missing"
    integration: str = "disabled"
    mode: str = "passthrough"
    proxy_url: str | None = None
    proxy_port: int | None = None
    ca_install_command: str | None = None


class HarnessEnabledIn(BaseModel):
    enabled: bool


class HarnessModeIn(BaseModel):
    mode: str = "passthrough"


class TrafficEventOut(BaseModel):
    ts: float
    event: str
    host: str
    port: int
    mode: str
    cursor_host: bool
    bytes_up: int = 0
    bytes_down: int = 0
    path: str | None = None
    status: int | None = None
    error: str | None = None


class TrafficLogOut(BaseModel):
    events: list[TrafficEventOut]


class ConnectivityResultOut(BaseModel):
    ok: bool
    first_token_ms: int | None
    total_ms: int
    text: str
    error: str | None
    usage: dict[str, int] | None = None
