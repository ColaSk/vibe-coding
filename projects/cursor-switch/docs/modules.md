# cursor-switch 模块抽象

本文根据 [`design.md`](./design.md) 做模块切分。目标是：前后端分离、模块彼此解耦、每个模块用明确的设计模式收口职责。

## 1. 前后端分离

系统拆成三条可独立演进的边界，禁止交叉依赖实现细节。

```text
┌──────────────────────────────┐
│ 前端 Frontend                │
│ Electron 主进程 + 渲染进程   │
│ 只认识控制面 HTTP API        │
└──────────────┬───────────────┘
               │ loopback HTTP / JSON
┌──────────────▼───────────────┐
│ 后端 Backend                 │
│ FastAPI 控制面 + Cursor 网关 │
│ 不认识 React / Electron      │
└──────────────┬───────────────┘
               │ 开发期可选
┌──────────────▼───────────────┐
│ 工具 Tools                   │
│ 协议提取 / 抓包调试          │
│ 不进入用户产品路径           │
└──────────────────────────────┘
```

硬规则：

- 渲染进程只调用控制面 API，不 import Python 模块，不直连 SQLite，不接触 Cursor protobuf。
- Electron 主进程只负责窗口、托盘、进程拉起；业务状态仍以后端为准。
- 后端不依赖前端打包产物才能启动；控制面可单独跑。
- Cursor 适配层与上游策略互不 import；它们只通过运行时定义的端口通信。
- 协议工具产出 `.proto` 或生成代码，运行时只消费生成结果，不在请求路径里调用提取器。

## 2. 分层与依赖方向

依赖只能向下。上层可以编排下层，下层不能认识上层。

```text
L4 前端表面
    desktop-shell / desktop-ui
            │
L3 控制面
    control-api
            │
L2 应用服务
    app-models / app-settings / app-usage / app-knowledge / app-harness
            │
L1 领域核心
    session-runtime / domain-types
            │
L0 端口契约
    ports（ModelPort / ToolPort / CheckpointPort / TransportPort ...）
            ▲
            │ 适配器实现端口，互不依赖
L0a 适配器
    cursor-gateway / upstream-providers / persistence / local-access / search-index
```

另外两条平行线：

- `protocol-extractor`、`protocol-capture`：独立工具，只写协议产物或调试库。
- `null-telemetry`：实现 Cursor 遥测接口的空对象，挂在 `cursor-gateway` 路由上，不进入领域核心。

## 3. 模块一览

| 模块 | 侧 | 主模式 | 职责一句话 |
| --- | --- | --- | --- |
| `desktop-shell` | 前端 | 外观 | 窗口、托盘、拉起后端 |
| `desktop-ui` | 前端 | MVC / 单向数据流 | 配置与观察页面 |
| `control-api` | 后端 | 外观 + DTO | 桌面唯一业务入口 |
| `app-models` | 后端 | 应用服务 | 模型 CRUD、测试、目录投影 |
| `app-settings` | 后端 | 应用服务 | 端口、代理、主题相关设置 |
| `app-usage` | 后端 | 应用服务 | 用量、调用记录、概览 |
| `app-knowledge` | 后端 | 应用服务 | 知识库 |
| `app-harness` | 后端 | 应用服务 | CA 状态、接管开关 |
| `session-runtime` | 后端 | 状态机 + 注册表 | Agent 循环 |
| `domain-types` | 后端 | 值对象 | 会话、消息、事件等纯类型 |
| `ports` | 后端 | 端口 | 核心对外契约 |
| `cursor-gateway` | 后端 | 适配器 + 外观 + 空对象 | Cursor 协议进出 |
| `upstream-providers` | 后端 | 策略 | Chat / Responses / Anthropic |
| `persistence` | 后端 | 仓储 + 工作单元 | SQLite |
| `local-access` | 后端 | 外观 | CA、TLS 代理、官方回退 |
| `search-index` | 后端 | 适配器 | 本地代码搜索与网页抓取 |
| `protocol-extractor` | 工具 | 管道 | 从 Cursor 产物生成协议 |
| `protocol-capture` | 工具 | 观察者 / 存储 | 抓包与对照 |

## 4. 前端模块

### 4.1 `desktop-shell`

- **职责**：创建主窗口与托盘，关闭到托盘，打开系统终端和外部链接，启动或探活后端进程，展示启动失败对话框。
- **模式**：外观。把操作系统能力收成少量命令：`startBackend`、`showWindow`、`quit`。
- **解耦**：不实现模型业务；不知道 Cursor 协议。只保存后端回环地址，交给渲染进程。
- **边界输入**：用户点击托盘、开机启动配置。
- **边界输出**：后端进程存活状态、窗口可见性。

### 4.2 `desktop-ui`

- **职责**：首页用量、模型配置、批量修改、拉取模型列表、连通性测试、调用记录、设置页、语言与主题。
- **模式**：单向数据流。页面状态进 store，副作用只通过 `control-api` 客户端。
- **解耦**：所有请求走 TypeScript API client；不直接拼后端内部表结构。错误以 API 返回为准。
- **页面分区**：
  - 首页：时间范围、token、缓存、延迟、贡献日历、估算价值。
  - 模型：CA、接管、增删改、排序、分组、批量改、测试。
  - 调用记录：列表与详情。
  - 设置：端口、出站代理、提交信息模型、计价、观测、语言、主题、开关机、存储清理。
- **明确没有**：广告、插件页、自动更新、外部文档入口。

## 5. 后端控制面与应用服务

### 5.1 `control-api`

- **职责**：对前端暴露 REST。校验入参，调用应用服务，返回 DTO。
- **模式**：外观。前端只看见这一层。
- **解耦**：不直接操作 Cursor 传输；不直接 new 上游客户端。连通性测试委托 `app-models`，再由它走 `ModelPort`。
- **监听**：仅回环地址。

### 5.2 `app-models`

- **职责**：模型配置增删改、排序、分组批量改、从上游发现模型 ID、单次与批量连通性测试、取消测试。
- **模式**：应用服务。事务边界在此开启，细节交给仓储。
- **解耦**：测试时只依赖 `ModelPort`，不依赖某个具体协议实现类。

### 5.3 `app-settings`

- **职责**：代理端口、服务端口、出站代理、提交信息所用模型、计价、观测详细程度、桌面相关设置、存储统计与清理。
- **模式**：应用服务。
- **解耦**：Tab 无自定义/公益模式字段。出站代理配置只影响 `upstream-providers` 的 HTTP 客户端工厂。

### 5.4 `app-usage`

- **职责**：概览统计、调用记录列表与详情、trace 查询。
- **模式**：应用服务 + 查询对象。读多写少，不进入会话写路径。
- **解耦**：只读 `persistence` 查询接口，不订阅运行时事件总线以外的内部对象。

### 5.5 `app-knowledge`

- **职责**：知识库增删改查，供 Cursor 侧接口和应用配置共用。
- **模式**：应用服务。
- **解耦**：Cursor 路由通过此服务访问知识，不各自写 SQL。

### 5.6 `app-harness`

- **职责**：CA 状态、初始化 CA、开启/关闭接管。
- **模式**：应用服务。
- **解耦**：证书文件与系统信任细节封装在 `local-access`；本模块只表达业务状态机：Missing / Untrusted / Ready / Invalid。

## 6. 领域核心

### 6.1 `domain-types`

- **职责**：`Conversation`、`Run`、`Message`、`ToolCall`、`ToolResult`、`ModelEvent`、`Usage` 等纯数据。
- **模式**：值对象 / 封闭联合。
- **解耦**：禁止 import FastAPI、httpx、protobuf 生成类、SQLAlchemy。这是全仓库最稳定的一层。

### 6.2 `ports`

- **职责**：定义核心需要的接口，例如：
  - `ModelPort.stream(invocation) -> AsyncIterator[ModelEvent]`
  - `ToolPort.dispatch(call) -> ToolHandle`
  - `CheckpointPort.save / restore`
  - `TransportPort.append / subscribe`
  - `ClockPort`、`IdPort` 等基础设施端口
- **模式**：端口与适配器中的端口。
- **解耦**：只依赖 `domain-types`。任何适配器替换都不应改运行时。

### 6.3 `session-runtime`

- **职责**：一个会话一个当前 run；处理忽略、插入、打断、取消；模型周期与工具轮次；上下文压缩；前缀稳定；检查点屏障。
- **模式**：
  - 状态机：`Running` / `Finalizing` / `Ended`
  - 注册表：`conversation_id -> ConversationRuntime`
  - 命令对象：`InsertMessages` / `BreakMessages` / `ToolResult` / `Cancel`
- **解耦**：只依赖 `ports` 与 `domain-types`。不知道 Chat 与 Responses 的差异，不知道 protobuf 字段名。
- **不变量**：
  - 同一会话不会有两个 current run。
  - Finalizing 拒绝新的插入与打断以外的业务命令。
  - 收尾前必须等待 Checkpoint 屏障。

## 7. 适配器模块

### 7.1 `cursor-gateway`

- **职责**：Connect/`BidiAppend` 上行、`RunSSE` 下行、动作编译、工具线路编解码、模型目录与账号外观、知识库路由、提交信息、Blob/上下文同步、连通性探测固定已连接、遥测空响应。
- **模式**：
  - 适配器：Cursor 报文 ↔ 领域命令/事件
  - 注册表：`request_id -> Transport`
  - 空对象：遥测与部分兼容接口
  - 外观：把官方回退委托给 `local-access`
- **解耦**：生成的 protobuf 类型只出现在本模块。向运行时只提交 `domain-types` 命令。
- **内部子边界**（仍属本模块，文件可拆，包边界不对外）：
  - transport
  - compile
  - tool-wire
  - cursor-services

### 7.2 `upstream-providers`

- **职责**：三种上游协议的请求组装、SSE 解析、用量归一、重试、调用记录写入钩子。
- **模式**：策略。`ProviderRouter` 按模型配置选择实现。
- **解耦**：实现 `ModelPort`。禁止 import `cursor-gateway`。自定义 Headers/额外参数在此校验保留字段。
- **策略族**：
  - `OpenAiChatStrategy`
  - `OpenAiResponsesStrategy`
  - `AnthropicMessagesStrategy`

### 7.3 `persistence`

- **职责**：会话、检查点、消息、run、工具轮次、模型、设置、调用记录、trace、blob。
- **模式**：仓储 + 工作单元。
- **解耦**：对外只暴露 repository 接口与 unit-of-work。SQLAlchemy 模型不泄漏到 `session-runtime`。

### 7.4 `local-access`

- **职责**：本地 CA 生成与信任判断；只劫持 Cursor 域名的 TLS 代理；本地 token 识别；Tab 与未知 RPC 原样转发官方；出站代理配置落到 HTTP 客户端。
- **模式**：外观。把证书、代理、转发收成 `LocalAccessFacade`。
- **解耦**：不解析 Agent 业务消息。分流规则集中在此，避免各路由各自判断。

### 7.5 `search-index`

- **职责**：本地代码切块与检索、网页搜索与抓取，供工具端口使用。
- **模式**：适配器，实现工具相关端口或被 `ToolPort` 实现调用。
- **解耦**：索引细节不进入会话状态机；失败以工具结果返回。

## 8. 协议工具模块

### 8.1 `protocol-extractor`

- **职责**：从 Cursor 客户端产物提取服务、消息、字段，生成 `.proto` 或 Python 消息类。
- **模式**：管道。输入产物 → 解析 → 归一 → 渲染。
- **解耦**：独立 CLI/包。运行时网关不调用它；CI 或开发者手动更新协议产物。

### 8.2 `protocol-capture`

- **职责**：拦截 Cursor API，解码，存本地库，提供调试页对照上下行。
- **模式**：旁路观察。抓包服务与生产网关进程分离。
- **解耦**：可以复用协议解码代码，但不写入生产会话库，不改生产配置。

## 9. 模块交互图

```text
desktop-ui ──HTTP──► control-api ──► app-* ──► persistence
                         │
                         ├── app-harness ──► local-access
                         └── app-models ──► ModelPort
                                              ▲
session-runtime ──ports──┼────────────────────┤
                         │                    │
                         ▼                    │
                   cursor-gateway ◄── local-access ◄── Cursor 客户端
                         │
                         ▼
                   session-runtime ──► ToolPort ──► search-index / tool adapters
                         │
                         ▼
                   ModelPort ──► upstream-providers ──► 第三方模型
```

生产路径上，前端永远不进入右半边的 Cursor/上游链路；Cursor 永远不进入控制面 DTO。

## 10. 解耦验收标准

一个改动如果违反任一条，说明模块边界破了：

1. 改 Anthropic 字段，不应改 `session-runtime`。
2. 改 React 页面，不应改任何后端领域类型。
3. 改 protobuf 字段名，只应落在 `cursor-gateway` 与生成代码。
4. 换 SQLite 为别的库，只应改 `persistence`。
5. 关掉遥测实现，只应影响空对象适配器，不影响运行时。
6. 协议提取器升级，不应要求重启生产会话逻辑，除非主动替换生成代码并发布。

## 11. 建议目录映射

前后端分仓或单仓都行，逻辑边界如下：

```text
apps/
  desktop/                 # desktop-shell + desktop-ui
server/
  control/                 # control-api
  app/                     # app-models/settings/usage/knowledge/harness
  runtime/                 # session-runtime + domain-types + ports
  adapters/
    cursor/                # cursor-gateway
    providers/             # upstream-providers
    persistence/           # persistence
    local_access/          # local-access
    search/                # search-index
tools/
  protocol_extractor/
  protocol_capture/
protocols/                 # 生成的 .proto 与产物
```

前端与后端通过 OpenAPI 或手写 client 契约同步；不要共享运行时对象模型。
