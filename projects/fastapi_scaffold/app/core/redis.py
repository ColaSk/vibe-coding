from redis.asyncio import Redis

from app.core.config import Settings


async def connect(settings: Settings) -> Redis:
    return Redis(host=settings.redis_host, port=settings.redis_port, decode_responses=True)


async def disconnect(client: Redis) -> None:
    await client.aclose()


async def ping(client: Redis) -> None:
    if not await client.ping():
        raise RuntimeError("redis unavailable")
