# Python / FastAPI

## 标识与触发词

- id：`python`
- 触发：FastAPI、Python HTTP 服务、给这种服务接 MySQL、Redis、Kafka、RabbitMQ

## 运行时与命令

- Python `>=3.12`，依赖由 `uv` 安装。
- 框架：FastAPI。入口是 `app/main.py` 的 `create_app()`，模块级实例名叫 `app`。
- 导入包永远是 `app`，不随项目名变化。
- 生成：

```bash
python3 scripts/render_python.py \
  --dest "<目标目录>" \
  --project "<项目名>" \
  --title "<服务标题>" \
  --enable "<mysql,redis,kafka,rabbitmq 的子集>"
```

- 检查：`uv sync`、`make check`。有 Docker 时加 `docker compose config`。
- 本地启动：`uv run fastapi dev app/main.py`。
- 容器：`docker compose up --build`。某个后端再加 `--profile mysql` 这类同名 profile。

`make check` 依次执行 `ruff format --check`、`ruff check`、`mypy app tests`、`lint-imports`、`pytest`。

## 必填输入与命名

- 项目名：`^[a-z][a-z0-9_]*$`，同时作为目录名和 `[project].name`。
- 服务标题：一行人类可读文字，写入 `Settings.title`，默认等于项目名。
- 模块和函数用 snake_case：`read_health`、`read_ready`、`read_hello`、`get_db`。
- 类用 PascalCase：`Settings`、`HelloResponse`、`Database`、`ApiResponse`。
- 环境变量用 SCREAMING_SNAKE。

MySQL 沿用官方模板拆开的字段：`MYSQL_SERVER`、`MYSQL_PORT`、`MYSQL_USER`、`MYSQL_PASSWORD`、`MYSQL_DB`。Redis 用 `REDIS_HOST`、`REDIS_PORT`。Kafka 用 `KAFKA_BOOTSTRAP_SERVERS`。RabbitMQ 用 `RABBITMQ_HOST`、`RABBITMQ_PORT`、`RABBITMQ_USER`、`RABBITMQ_PASSWORD`。同一种再加一条时用双下划线，例如 `MYSQL__ANALYTICS__SERVER`。

## 文件映射

`templates/python/` 复制到目标目录。三个无点文件名在复制时改名：`gitignore` → `.gitignore`，`dockerignore` → `.dockerignore`，`env.example` → `.env.example`。

```
app/main.py                      # create_app、模块级 app
app/api/main.py                  # 聚合 /api/v1 路由
app/api/deps.py                  # get_db、get_redis、get_kafka、get_rabbitmq
app/api/routes/health.py         # GET /health、GET /ready
app/api/routes/hello.py          # GET /api/v1/hello
app/core/config.py               # Settings 与按名字挂载的连接
app/core/context.py              # 请求上下文中间件
app/core/exceptions.py           # AppError 与失败信封
app/core/db.py                   # MySQL
app/core/redis.py                # Redis
app/core/kafka.py                # Kafka
app/core/rabbitmq.py             # RabbitMQ
app/schemas/response.py          # ApiResponse、ok、fail
app/schemas/hello.py             # HelloResponse
app/services/hello.py            # build_hello
harness/docs/                    # 请求、错误、探针、后端
tests/api/                       # 探针、hello、错误信封、关闭时的依赖
tests/core/                      # 数据库 open 只启动一次
AGENTS.md
Makefile
Dockerfile
compose.yml
pyproject.toml
```

业务路由前缀是 `/api/v1`。探针不带这个前缀。

## 占位符

只替换两个：

- `{{project}}`：项目名
- `{{title}}`：服务标题

`.env` 不从模板原样保留，渲染脚本按 `--enable` 重写开关。未出现在 `--enable` 里的后端保持 `false`。

## 后端行为

依赖始终安装：`fastapi[standard]`、`pydantic-settings`、`sqlalchemy[asyncio]`、`asyncmy`、`redis`、`aiokafka`、`aio-pika`。开发依赖：`pytest`、`ruff`、`httpx`、`mypy`、`import-linter`。

开关为 `False` 时不调用对应的 `startup`。`GET /api/v1/hello` 的实现函数是 `read_hello`，它只调用 `build_hello`，响应是成功信封，不取数据库或消息连接。

`Database.ping` 执行 `SELECT 1`。不生成表、模型或迁移。Redis 的 `ping` 执行 `PING`。Kafka 使用 `aiokafka` producer，compose profile 是单节点 KRaft 的 `apache/kafka`，不带 ZooKeeper。RabbitMQ 使用 `aio-pika`，镜像是 `rabbitmq:3-management`。

依赖方向由 import-linter 执行，和 `AGENTS.md` 一致：`schemas` 不依赖 `api`、`services`、`core`；`services` 不依赖 `api`、`core`、`fastapi`；`core` 不依赖 `api`、`services`；四个基础设施模块互相独立；路由不直接 import 这四个模块。

## 完成标准

在生成目录中，下面的命令退出码都是 0：

- `uv sync`
- `make check`

有 `docker` 可执行文件时，`docker compose config` 也必须是 0。
