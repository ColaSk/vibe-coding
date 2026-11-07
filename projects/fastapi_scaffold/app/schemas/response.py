from pydantic import BaseModel


class ApiResponse[T](BaseModel):
    success: bool
    code: int
    msg: str
    data: T | None = None


def ok[T](data: T, msg: str = "ok", code: int = 200) -> ApiResponse[T]:
    return ApiResponse(success=True, code=code, msg=msg, data=data)


def fail(msg: str, code: int, data: object | None = None) -> ApiResponse[object]:
    return ApiResponse(success=False, code=code, msg=msg, data=data)
