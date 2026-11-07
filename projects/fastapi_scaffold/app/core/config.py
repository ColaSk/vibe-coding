from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    title: str = "fastapi-scaffold"

    mysql_enabled: bool = False
    mysql_server: str = "localhost"
    mysql_port: int = 3306
    mysql_user: str = "app"
    mysql_password: str = "app"
    mysql_db: str = "app"

    redis_enabled: bool = False
    redis_host: str = "localhost"
    redis_port: int = 6379

    kafka_enabled: bool = False
    kafka_bootstrap_servers: str = "localhost:9092"

    rabbitmq_enabled: bool = False
    rabbitmq_host: str = "localhost"
    rabbitmq_port: int = 5672
    rabbitmq_user: str = "guest"
    rabbitmq_password: str = "guest"


def get_settings() -> Settings:
    return Settings()
