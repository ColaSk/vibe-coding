# 探针

探针不带 `/api/v1` 前缀，也不检查后端。

存活探针 `GET /health` 成功时返回 `{"status": "ok"}`。

就绪探针 `GET /ready` 成功时返回 `{"status": "ready"}`。
