from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def read_health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready")
async def read_ready() -> dict[str, str]:
    return {"status": "ready"}
