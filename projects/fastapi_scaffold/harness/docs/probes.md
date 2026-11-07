# 探针

探针不带 `/api/v1` 前缀。

存活探针 `GET /health` 不检查后端，成功时返回 `{"status": "ok"}`。

就绪探针 `GET /ready` 只对已启用的后端调用 `ping`。全部通过时返回 `{"status": "ready"}`。任一失败时返回 503，正文包含 `status` 为 `unavailable` 以及失败的后端名称。
