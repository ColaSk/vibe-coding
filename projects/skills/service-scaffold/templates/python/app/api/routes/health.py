from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.core.lifespan import enabled_backends

router = APIRouter(tags=["health"])


@router.get("/health")
async def read_health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready", response_model=None)
async def read_ready(request: Request) -> JSONResponse | dict[str, str]:
    failed: list[str] = []
    for name, module in enabled_backends():
        client = getattr(request.app.state, name, None)
        try:
            await module.ping(client)
        except Exception:
            failed.append(name)
    if failed:
        return JSONResponse(
            status_code=503,
            content={"status": "unavailable", "failed": failed},
        )
    return {"status": "ready"}
