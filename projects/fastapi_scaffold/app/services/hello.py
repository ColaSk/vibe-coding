from app.schemas.hello import HelloResponse


def build_hello(title: str) -> HelloResponse:
    return HelloResponse(message=f"hello from {title}")
