"""FastAPI application factory for the control plane."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cursor_switch.adapters.cursor.routes import router as cursor_router
from cursor_switch.control.deps import AppServices, build_services
from cursor_switch.control.routes import health, models, settings, usage
from cursor_switch.runtime.ports.model import ModelPort


def create_app(
    database_url: str | None = None,
    *,
    services: AppServices | None = None,
    ca_dir: Path | None = None,
    cursor_settings_path: Path | None = None,
    model: ModelPort | None = None,
) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.services = services or await build_services(
            database_url,
            ca_dir=ca_dir,
            cursor_settings_path=cursor_settings_path,
            model=model,
        )
        try:
            yield
        finally:
            current = app.state.services
            await current.local_access.proxy.stop()
            await current.search_index.dispose()
            await current.engine.dispose()

    app = FastAPI(title="cursor-switch", version="0.1.0", lifespan=lifespan)
    app.state = SimpleNamespace(services=services)
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router)
    app.include_router(models.router)
    app.include_router(settings.router)
    app.include_router(usage.router)
    app.include_router(cursor_router)
    return app
