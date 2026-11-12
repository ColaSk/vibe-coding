# 协议开发工具

这两套工具只给开发联调用，不进入用户桌面。

## protocol-extractor

从 Cursor 客户端 JS bundle 提取服务路径与类型名清单，写出：

- `inventory.json`
- `inventory.proto`（库存桩，不是完整字段定义）

```bash
cd projects/cursor-switch
PYTHONPATH=. python -m tools.protocol_extractor \
  --input /Applications/Cursor.app \
  --output protocols/cursor
```

更新真实 protobuf 字段后，再把生成结果接到 `adapters/cursor`。当前运行时的 Agent 上行仍可用 JSON envelope hex 做联调。

## protocol-capture

独立抓包调试服务：把请求转发到 `https://api2.cursor.sh`，落到 SQLite，并提供网页对照。

```bash
cd projects/cursor-switch
PYTHONPATH=. python -m tools.protocol_capture --port 9099
```

打开 `http://127.0.0.1:9099/` 查看交换记录。调试库与生产会话库分离，不改生产配置。
