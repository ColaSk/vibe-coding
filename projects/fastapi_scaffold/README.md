# fastapi-scaffold

FastAPI 服务。导入包是 `app`。

| 目录 | 内容 |
|------|------|
| `app/api` | 路由和 `get_db`、`get_redis`、`get_kafka`、`get_rabbitmq` |
| `app/core` | `Settings`、lifespan，以及 MySQL、Redis、Kafka、RabbitMQ |
| `app/schemas` | Pydantic 模型 |
| `app/services` | 业务函数 |

## 本地

```bash
uv sync
uv run fastapi dev app/main.py
make check
```

## 开关

`.env` 里的 `MYSQL_ENABLED`、`REDIS_ENABLED`、`KAFKA_ENABLED`、`RABBITMQ_ENABLED` 默认是 `false`。改成 `true` 后重启进程，lifespan 才会连接对应后端。开关关掉时，对应的 `get_*` 依赖返回 503。

## Docker

先在本目录执行 `uv lock`，镜像会按锁文件安装依赖。

```bash
docker compose up --build
docker compose --profile mysql up --build
```

`mysql`、`redis`、`kafka`、`rabbitmq` 是同名 profile。要同时启动多个后端，就重复 `--profile`。
