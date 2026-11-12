# cursor-switch 实现路线

依据 [`design.md`](./design.md) 与 [`modules.md`](./modules.md)。目标是按解耦边界分阶段交付，每一阶段都能单独验证。

## 阶段 0：仓库骨架

出口条件：后端与前端都能空跑启动；分层目录就位；依赖声明完成。

- 建立目录：`apps/desktop`、`server/{control,app,runtime,adapters}`、`tools/`、`protocols/`。
- 后端：`pyproject.toml`（Python 3.12、FastAPI、httpx、SQLAlchemy、aiosqlite、cryptography、protobuf）。
- 前端：Electron + Vite + React + TypeScript 项目骨架。
- 后端提供 `GET /healthz`；前端能请求该接口。
- 写 `README.md`：如何分别启动前后端。

## 阶段 1：领域核心与端口

出口条件：不依赖 Cursor/上游也能跑通假模型会话循环的单测。

- 实现 `domain-types`：Conversation、Run、Message、ToolCall、ToolResult、ModelEvent、Usage。
- 实现 `ports`：ModelPort、ToolPort、CheckpointPort、TransportPort。
- 实现 `session-runtime` 状态机：Running / Finalizing / Ended。
- 命令：InsertMessages、BreakMessages、ToolResult、Cancel。
- 注册表：conversation_id → runtime。
- 测试用 FakeModel / FakeTool，验证插入、打断、取消、重复命令。

## 阶段 2：持久化与应用服务

出口条件：控制面可对模型与设置做 CRUD；数据进 SQLite。

- `persistence`：仓储 + 工作单元，迁移脚本。
- `app-models`、`app-settings`、`app-usage`、`app-knowledge`、`app-harness`。
- `control-api`：模型、设置、概览、调用记录、CA/接管状态的 REST。
- 前端 API client 对接上述接口；模型配置页最小可用（增删改列表）。

## 阶段 3：本地接入

出口条件：本机 CA 可生成；代理能按 Host 分流；未知路径可转发官方。

- `local-access`：CA 生成与状态、TLS 代理、本地 token 判断、官方回退外观。
- Tab 与未实现 RPC 原样转发官方。
- 桌面 harness 页：初始化 CA、显示状态、开关接管。

## 阶段 4：上游策略

出口条件：三种协议都能流式返回统一 ModelEvent；连通性测试可用。

- `upstream-providers`：Chat、Responses、Anthropic 策略 + Router。
- 地址补全、自定义 Headers、额外参数保留字段校验。
- 重试（最多 8 次 / 5 秒）与调用记录。
- `app-models` 连通性测试走 ModelPort。
- 前端：单模型/批量测试与结果展示。

## 阶段 5：Cursor 网关

出口条件：Cursor 真实 Agent 请求能进入运行时并回下行。

- `cursor-gateway`：BidiAppend、RunSSE、request_id 传输注册表。
- 动作编译：忽略 / 插入 / 打断。
- 工具线路编解码与结果门控。
- 模型目录、账号外观、知识库、提交信息、Blob/上下文同步。
- 遥测空对象；IsConnected 固定已连接。
- 检查点保存与恢复接到 CheckpointPort。

## 阶段 6：工具与搜索

出口条件：文件/终端/MCP/网页/本地搜索/生图在 Agent 中可用。

- ToolPort 适配器：编码类、交互编排、MCP、Web、GenerateImage。
- `search-index`：tree-sitter 切块 + SQLite 词项；网页抓取。
- 按模式选择工具清单。

## 阶段 7：桌面完整体验

出口条件：设计中的桌面页面齐备，无广告/插件/更新入口。

- 首页图表（用量、缓存、延迟、贡献日历）。
- 模型分组、批量改、拉取模型列表。
- 调用记录详情、设置全项、语言与主题、托盘与开关机。
- Electron 主进程稳定拉起/探活后端。

## 阶段 8：协议工具

出口条件：可从 Cursor 产物生成协议；可抓包对照。

- `protocol-extractor` CLI：提取 → 生成 `.proto` / Python 消息。
- `protocol-capture`：独立调试服务 + 网页对照。
- 文档说明如何更新 `protocols/`。

## 实施顺序约束

1. 先 0 → 1 → 2，再并行准备前端页面壳。
2. 3 与 4 可并行，但 5 必须在 1、3、4 之后。
3. 6 依赖 5 的工具线路。
4. 7 可在 2 之后持续补，不阻塞 5。
5. 8 可与 5 并行启动，但生成代码合入要有明确版本点。

## 当前状态

- 阶段 0–8 主干已落地。
- 已知占位：Shell/MCP/生图；AgentClientMessage 完整 protobuf（现用 JSON envelope）；调用记录图表与批量改模型仍可继续打磨。
- 协议工具：`tools/protocol_extractor`、`tools/protocol_capture`；说明见 [`protocol-tools.md`](./protocol-tools.md)。
- 环境约定：conda `cursor-switch`（Python 3.12）、nvm Node `v26.13.0`。
- 验证：`pytest -q`；`apps/desktop` 下 `npm run build`。
