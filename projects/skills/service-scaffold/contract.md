# 契约

语言包和 Python 后端模块都按本节扩展。agent 只读这一层，不要再跳到更深的文档。

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

| 模块 | `app.state` 属性 | 开关 |
|------|------------------|------|
| `app/core/db.py` | `db` | `MYSQL_ENABLED` |
| `app/core/redis.py` | `redis` | `REDIS_ENABLED` |
| `app/core/kafka.py` | `kafka` | `KAFKA_ENABLED` |
| `app/core/rabbitmq.py` | `rabbitmq` | `RABBITMQ_ENABLED` |

每个后端模块提供三个异步函数：

- `connect(settings)`：建立连接并返回连接对象。开关为 `False` 时不会被调用。
- `disconnect(client)`：关闭 `connect` 返回的对象。
- `ping(client)`：失败时抛异常。`GET /ready` 捕获异常并返回 503。

`app/core/lifespan.py` 按登记顺序调用 `connect`，关闭时逆序调用 `disconnect`。连接对象放在 `app.state` 的上表属性上。

`app/api/deps.py` 提供 `get_db`、`get_redis`、`get_kafka`、`get_rabbitmq`。对应开关为 `False`，或 `app.state` 上还没有连接时，依赖抛出 `HTTPException(status_code=503)`。路由不要直接 import 某一个后端模块来建连。

`GET /health` 不探后端。`GET /ready` 只对开关为 `True` 的模块调用 `ping`。失败响应写明模块名（`db`、`redis`、`kafka`、`rabbitmq`）。四个开关都关着时 ready 直接成功。

新增一种后端时：

1. 在 `app/core/` 增加 snake_case 模块，实现 `connect`、`disconnect`、`ping`。
2. 在 `Settings` 增加 `*_ENABLED` 以及该后端自己的连接字段。字段用 SCREAMING_SNAKE 环境变量。
3. 在 `lifespan.py` 登记模块、状态属性名和开关。
4. 在 `app/api/deps.py` 增加 `get_*`。
5. 在 `compose.yml` 增加同名 profile 和 healthcheck，并让 `app` 以 `required: false` 依赖它。
6. 依赖写进 `pyproject.toml`。不要因为开关默认关闭就删掉依赖。

不改 `create_app()` 的形状：它仍然只创建 `FastAPI`、挂上 lifespan、挂上 `/health` 与 `/ready`，并把业务路由挂到 `/api/v1`。
