# 后端插拔

一个后端由三处接上：

- 配置里的开关，以及连接所需的字段。
- `app.core` 里的模块，提供 `connect`、`disconnect`、`ping`。
- `app.api.deps` 里对应的 `get_*`，把连接交给路由。

开关为假时，lifespan 不调用这个模块的 `connect`。`get_*` 返回 503，响应体是失败信封，说明该后端已关闭。开关为真但应用状态里还没有连接时，同样返回 503，说明该后端不可用。

lifespan 按登记顺序启动已启用的后端，并按实际启动顺序的逆序关闭。各基础设施模块互不 import。

MySQL、Redis、Kafka、RabbitMQ 是这个模式的现有实例。新增同类后端时沿用同一组接缝。
