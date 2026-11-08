# 后端插拔

一条连接有自己的名字、开关和配置。MySQL、Redis、Kafka、RabbitMQ 各自有一个连接类，客户端记在实例上。`open` 在第一次调用时建立客户端。多个协程可以同时 `open`：MySQL 每次借出新的会话，另外三种返回同一个客户端。

默认四条名字是 `db`、`redis`、`kafka`、`rabbitmq`，分别对应原来的 `MYSQL_*`、`REDIS_*`、`KAFKA_*`、`RABBITMQ_*`。同一种要再加一条时，用双下划线写下名字，例如 `MYSQL__ANALYTICS__ENABLED` 和 `MYSQL__ANALYTICS__SERVER`。名字在全部连接里必须唯一。

开关为假时，按名字取连接会返回 503，响应体是失败信封，说明该连接已关闭。各基础设施模块互不 import。连接不放在 FastAPI 应用对象上。

`get_db`、`get_redis`、`get_kafka`、`get_rabbitmq` 是默认名字的简写。数据库用 `get_db_connection(名字)` 借出会话，另外三种用同名的 `get_*_connection(名字)`。
