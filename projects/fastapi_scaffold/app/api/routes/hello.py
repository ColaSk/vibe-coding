from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.hello import HelloResponse
from app.schemas.response import ApiResponse, ok
from app.services.hello import build_hello

router = APIRouter(tags=["hello"])


@router.get("/hello", response_model=ApiResponse[HelloResponse])
async def read_hello() -> ApiResponse[HelloResponse]:
    return ok(build_hello(get_settings().title))
