# AGENTS.md — fastapi_scaffold

这是 HTTP 服务脚手架，提供分层和可插拔的基础设施，业务在此之上另写。领域模型、认证、迁移、任务都可以加，只要仍走下面的分层和规范。

机制见 `harness/docs/`。改一个机制时，先改那里对应的文档，再改代码。

## 环境

Python `>=3.12`。虚拟环境是 `.venv`。依赖只写在 `pyproject.toml`，用 `uv` 安装。不 `pip install` 未声明的包。

## 命令

```bash
uv sync
uv run fastapi dev app/main.py
make check
make test
make fmt
uv run pytest tests/api/test_health.py
docker compose up --build
docker compose --profile mysql up --build
```

`make check` 是唯一完成入口。人和 Agent 用同一条命令。某个后端用同名 `--profile`，要同时启动多个就重复该参数。

## 风格

格式和 lint 以 `pyproject.toml` 里的 Ruff 为准。不在这里另写风格手册。

## 服务边界

依赖方向违反即 `make check` 红。

- `app.schemas` 不 import `app.api`、`app.services`、`app.core`。
- `app.services` 不 import `app.api`、`app.core`、`fastapi`。服务函数只接收和返回普通值，不碰请求对象和连接。
- `app.core` 不 import `app.api`、`app.services`。`app.core` 可以 import `app.schemas`。
- `app.core` 里各基础设施模块互不 import。以后新增的同类模块也独立。
- `app.api.routes` 不直接 import 基础设施模块。连接从 `app.api.deps` 注入。

`app.api` 可以 import `app.services`、`app.schemas`、`app.core`。`app.services` 可以 import `app.schemas`。

## 基础规范

- 单文件不超过 300 行。新文件必须立刻减少概念或重复，否则并进既有模块。不新建 `utils/`、`helpers/`、`common/`。
- 全量注解，`mypy --strict`。用 `X | None`，不用 `typing.Optional`、`typing.List`、`typing.Dict`。不写裸 `Any`。

## 测试

测接缝和失败路径，不 mock 内部实现。示例路由不是必须保持的业务规格。修 bug 先留一条改动前会红的测试。

## 安全

不提交 `.env` 和密钥。镜像不打进 `.env`。配置里的默认口令只用于本地。不改 git config，不 force push。

## 提交

提交前 `make check` 全绿。
