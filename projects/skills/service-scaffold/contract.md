# 契约

语言包和 Python 后端模块都按本节扩展。agent 只读这一层，不要再跳到更深的文档。生成出的项目里，机制说明在 `harness/docs/`，约束在 `AGENTS.md`。改机制时先改对应文档，再改代码。

## 语言包

每个 `languages/<id>.md` 固定这些节：

- 标识与触发词
- 运行时、框架、生成命令、检查命令
- 必填输入与命名规则
- 模板目录到目标树的文件映射
- 占位符替换规则
- 完成标准：哪些命令必须退出码为 0

新增语言时同时增加模板目录和渲染脚本，并在 [SKILL.md](./SKILL.md) 的「已实现的语言」中登记。不改总流程的形状：确认输入、拒绝非空目录、运行该语言的渲染脚本、跑完检查命令、回报启动方式。

## Python 后端模块

生成出的 FastAPI 服务把外部连接放在 `app/core/`。目录名使用官方模板和常见实践里的名字：`api`、`core`、`schemas`、`services`。不要新增 `components`、`plugins` 或其他同义包名。

已有模块：

| 模块 | 连接类 | 默认名字 | 开关 |
|------|--------|----------|------|
| `app/core/db.py` | `Database` | `db` | `MYSQL_ENABLED` |
| `app/core/redis.py` | `RedisConnection` | `redis` | `REDIS_ENABLED` |
| `app/core/kafka.py` | `KafkaConnection` | `kafka` | `KAFKA_ENABLED` |
| `app/core/rabbitmq.py` | `RabbitMQConnection` | `rabbitmq` | `RABBITMQ_ENABLED` |

连接不放在 FastAPI 应用对象上，也不在进程启动时统一建连。每个连接类保存自己的客户端。`open` 第一次调用时建立客户端，并留在实例上。MySQL 每次 `open` 借出新的会话；另外三种返回同一个客户端。多个协程可以同时 `open`。

`Settings` 把原来的扁平环境变量挂成默认名字，再用 `env_nested_delimiter="__"` 接收同一种的额外连接，例如 `MYSQL__ANALYTICS__ENABLED`。全部连接名字必须唯一。

`app/api/deps.py` 提供默认名字的 `get_db`、`get_redis`、`get_kafka`、`get_rabbitmq`，以及 `get_*_connection(名字)`。对应开关为 `False`，或没有这个名字时，依赖抛出 `HTTPException(status_code=503)`。路由不要直接 import 某一个后端模块来建连。503 和其他错误一样走失败信封。

`GET /health` 和 `GET /ready` 都不探后端。存活返回 `{"status": "ok"}`，就绪返回 `{"status": "ready"}`。

每个连接类还提供：

- `startup()`：建立客户端。
- `shutdown()`：关闭客户端。
- `ping()`：失败时抛异常。探针当前不调用它。

新增一种后端时：

1. 在 `app/core/` 增加 snake_case 模块，实现连接类和按名字取实例的函数。各基础设施模块互不 import。
2. 在 `Settings` 增加该后端自己的嵌套配置、默认 `*_ENABLED` 和连接字段。字段用 SCREAMING_SNAKE 环境变量。
3. 在 `app/api/deps.py` 增加 `get_*` 和 `get_*_connection`。
4. 在 `compose.yml` 增加同名 profile 和 healthcheck，并让 `app` 以 `required: false` 依赖它。
5. 依赖写进 `pyproject.toml`。不要因为开关默认关闭就删掉依赖。
6. 把新模块加进 import-linter 的基础设施独立契约，以及「路由不直接 import 基础设施」契约。

不改 `create_app()` 的形状：它读取配置、注册异常处理、挂上请求上下文中间件、挂上不带前缀的探针，并把业务路由挂到 `/api/v1`。

## 请求与错误

请求上下文在 `app/core/context.py`。中间件写入当前请求，响应头带回 `X-Request-ID`，并在 `finally` 里结束和 `reset`。

成功响应用 `app/schemas/response.py` 的 `ok`，字段是 `success`、`code`、`msg`、`data`。`AppError`、`HTTPException`、校验错误和未捕获异常都由 `app/core/exceptions.py` 收成失败信封。未捕获异常记日志，响应 `msg` 固定为 `internal server error`。
