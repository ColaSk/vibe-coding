from aiokafka import AIOKafkaProducer

from app.core.config import Settings


async def connect(settings: Settings) -> AIOKafkaProducer:
    producer = AIOKafkaProducer(bootstrap_servers=settings.kafka_bootstrap_servers)
    await producer.start()
    return producer


async def disconnect(producer: AIOKafkaProducer) -> None:
    await producer.stop()


async def ping(producer: AIOKafkaProducer) -> None:
    await producer.client.force_metadata_update()
    if not producer.client.cluster.brokers():
        raise RuntimeError("kafka unavailable")
