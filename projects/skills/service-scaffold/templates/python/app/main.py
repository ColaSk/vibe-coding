from fastapi import FastAPI

from app.api.main import api_router
from app.api.routes import health
from app.core.config import get_settings
from app.core.lifespan import lifespan


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(title=settings.title, lifespan=lifespan)
    application.include_router(health.router)
    application.include_router(api_router, prefix="/api/v1")
    return application


app = create_app()
