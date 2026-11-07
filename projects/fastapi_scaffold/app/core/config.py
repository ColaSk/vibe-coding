from pydantic import BaseModel, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class MySQLSettings(BaseModel):
    enabled: bool = False
    server: str = "localhost"
    port: int = 3306
    user: str = "app"
    password: str = "app"
    db: str = "app"


class RedisSettings(BaseModel):
    enabled: bool = False
    host: str = "localhost"
    port: int = 6379


class KafkaSettings(BaseModel):
    enabled: bool = False
    bootstrap_servers: str = "localhost:9092"


class RabbitMQSettings(BaseModel):
    enabled: bool = False
    host: str = "localhost"
    port: int = 5672
    user: str = "guest"
    password: str = "guest"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    title: str = "fastapi-scaffold"

    mysql_enabled: bool = False
    mysql_server: str = "localhost"
    mysql_port: int = 3306
    mysql_user: str = "app"
    mysql_password: str = "app"
    mysql_db: str = "app"
    mysql: dict[str, MySQLSettings] = Field(default_factory=dict)

    redis_enabled: bool = False
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis: dict[str, RedisSettings] = Field(default_factory=dict)

    kafka_enabled: bool = False
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka: dict[str, KafkaSettings] = Field(default_factory=dict)

    rabbitmq_enabled: bool = False
    rabbitmq_host: str = "localhost"
    rabbitmq_port: int = 5672
    rabbitmq_user: str = "guest"
    rabbitmq_password: str = "guest"
    rabbitmq: dict[str, RabbitMQSettings] = Field(default_factory=dict)

    @model_validator(mode="after")
    def mount_named_connections(self) -> "Settings":
        self.mysql = {
            "db": MySQLSettings(
                enabled=self.mysql_enabled,
                server=self.mysql_server,
                port=self.mysql_port,
                user=self.mysql_user,
                password=self.mysql_password,
                db=self.mysql_db,
            ),
            **{name: cfg for name, cfg in self.mysql.items() if name != "db"},
        }
        self.redis = {
            "redis": RedisSettings(
                enabled=self.redis_enabled,
                host=self.redis_host,
                port=self.redis_port,
            ),
            **{name: cfg for name, cfg in self.redis.items() if name != "redis"},
        }
        self.kafka = {
            "kafka": KafkaSettings(
                enabled=self.kafka_enabled,
                bootstrap_servers=self.kafka_bootstrap_servers,
            ),
            **{name: cfg for name, cfg in self.kafka.items() if name != "kafka"},
        }
        self.rabbitmq = {
            "rabbitmq": RabbitMQSettings(
                enabled=self.rabbitmq_enabled,
                host=self.rabbitmq_host,
                port=self.rabbitmq_port,
                user=self.rabbitmq_user,
                password=self.rabbitmq_password,
            ),
            **{name: cfg for name, cfg in self.rabbitmq.items() if name != "rabbitmq"},
        }
        names = [
            *self.mysql,
            *self.redis,
            *self.kafka,
            *self.rabbitmq,
        ]
        if len(names) != len(set(names)):
            raise ValueError("connection names must be unique")
        return self


def get_settings() -> Settings:
    return Settings()
