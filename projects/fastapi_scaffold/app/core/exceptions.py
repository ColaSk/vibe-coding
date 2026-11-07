import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.context import get_context
from app.schemas.response import fail

logger = logging.getLogger(__name__)


class AppError(Exception):
    def __init__(self, status_code: int, msg: str) -> None:
        self.status_code = status_code
        self.msg = msg
        super().__init__(msg)


def _error(status_code: int, msg: str) -> JSONResponse:
    body = fail(msg=msg, code=status_code)
    return JSONResponse(status_code=status_code, content=body.model_dump())


def _validation_message(exc: RequestValidationError) -> str:
    parts: list[str] = []
    for err in exc.errors():
        loc = ".".join(str(item) for item in err.get("loc", ()))
        parts.append(f"{loc}: {err.get('msg', 'invalid')}")
    return "; ".join(parts) or "validation error"


async def app_error_handler(request: Request, exc: Exception) -> JSONResponse:
    if not isinstance(exc, AppError):
        raise exc
    return _error(exc.status_code, exc.msg)


async def http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    if not isinstance(exc, HTTPException):
        raise exc
    detail = exc.detail
    msg = detail if isinstance(detail, str) else str(detail)
    return _error(exc.status_code, msg)


async def validation_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    if not isinstance(exc, RequestValidationError):
        raise exc
    return _error(422, _validation_message(exc))


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    ctx = get_context()
    request_id = ctx.request_id if ctx is not None else "-"
    logger.exception("unhandled error request_id=%s", request_id)
    return _error(500, "internal server error")


def register_exception_handlers(application: FastAPI) -> None:
    application.add_exception_handler(AppError, app_error_handler)
    application.add_exception_handler(HTTPException, http_exception_handler)
    application.add_exception_handler(RequestValidationError, validation_exception_handler)
    application.add_exception_handler(Exception, unhandled_exception_handler)
