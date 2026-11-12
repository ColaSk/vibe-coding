# cursor-byok 模块与功能点

cursor-byok 是运行在本机的 Cursor 网关。Cursor 的 Agent 请求进入本地服务，服务再把请求转到用户配置的模型。Tab 补全走独立通道。桌面程序负责配置、观察和本机接入。

代码主要在四块：

- `server/`：Rust 本地服务。
- `apps/desktop/`：Tauri 窗口加 Web 控制台。
- `server/plugins/build-in/`：内置登录插件。
- `protocols/cursor/`、`support/`、`crates/semble-core/`：协议、抓取工具和本地代码搜索。

## 1. 本机接入 `server/src/local_app`

| 模块 | 功能点 |
| --- | --- |
| `ca` | 生成本地 CA，判断未生成、未信任、就绪、无效，并给出安装命令。Windows 有单独的证书安装路径。 |
| `proxy` | 只劫持 Cursor 域名，把 HTTPS 流量转到本机服务。 |
| `account` | 识别本地 Cursor token，用来区分走本机还是官方。 |
| `settings` | 读取接管开关和 Tab 模式，供代理决定是否拦截。 |
| `process` | 管理本地服务进程。 |

## 2. HTTP 入口 `server/src/api`

### `api/cursor`

| 模块 | 功能点 |
| --- | --- |
| `handlers` | 注册 Cursor 会调用的 HTTP 路由，并在未命中时回退到官方转发。 |
| `bidi` | 接收 `BidiAppend` 上行，解出 `request_id`、序号和客户端消息。 |
| `run_sse` | 提供 `RunSSE` 下行订阅。 |
| `proxy` | 按路径把 Tab 或未实现的 RPC 原样转发到官方。 |

固定由本机应答的接口包括：可用模型、默认可选模型、CLI 默认模型、默认模型提示、账号与额度外观、Stripe 资料、服务配置、隐私模式、插件列表、文档列表、会话元数据、知识库、Git 提交信息、连通性探测、Statsig bootstrap。连通性探测固定返回已连接，避免慢请求被 Cursor 取消。

### `api/byok`

对外兼容接口，带开关和本机密钥校验：

- `GET /byok/v1/models`
- `POST /byok/v1/chat/completions`
- `POST /byok/v1/responses`
- `POST /byok/v1/messages`

## 3. Cursor 适配层 `server/src/cursor`

### 传输 `transport`

- 按 `request_id` 登记传输通道。
- 上行按序号排序。
- 下行缓存、广播、断线重放和关闭。

### 会话 `conversation`

- `conversation_id` 对应一个会话运行时，同时只有一个当前 run。
- 命令分为开始、动作、取消、断开。
- 投递结果分为忽略、插入、打断。
- 插入在当前模型周期结束后追加，不新开 run。
- 打断取消当前模型或工具周期，不取消整段会话。
- run 状态为进行中、收尾、结束。命令结果包含已应用、重复、正在关闭、已结束、目标过期。

### 编译 `compile`

- 把 Cursor 动作编译成内部消息。
- 收集 rules、skills、MCP 和环境。
- 处理图片和 blob。
- 把 Cursor 模型名映射到已配置的上游模型。

### 提示词 `prompting`

- 按模式加载提示词：agent、ask、plan、debug、multitask、subagent。
- 另有压缩提示词和提交信息提示词。
- 维护稳定的派生上下文，供前缀稳定使用。

### 检查点 `checkpoint`

- 把消息编成稳定根消息、turns、steps、工具状态、Todo、Plan 和已读路径。
- 从 Cursor 的 ConversationState 恢复会话。
- 异步写入，run 收尾前等待落盘完成。

### 工具 `tools`

工具清单在 `server/prompt/cursor/tools.json`，按模式挑选。

- 文件与检索：Read、Write、StrReplace、Delete、EditNotebook、Glob、Grep、Shell、ReadLints。
- 交互与编排：AskQuestion、TodoWrite、SwitchMode、Task、CreatePlan、UpdateCurrentStep。
- MCP：GetMcpTools、FetchMcpResource、CallMcpTool。
- 网页：WebSearch、WebFetch。
- 本地代码搜索：SembleSearch、SembleFindRelated。
- 其它：GenerateImage。

线路功能：

- `codec`：执行请求、执行响应、交互查询、工具卡片。
- `tool_call_dispatch`：分发到本地、命令执行、编辑、交互、搜索。
- `tool_call_result`：结果门控、命令输出、MCP 状态、搜索结果。
- `stream`、`schedule`：流式参数和后台任务。

### Cursor 侧服务 `services`

| 模块 | 功能点 |
| --- | --- |
| `model_catalog` | 把本机模型塞进 Cursor 模型列表，带显示名、说明和上下文窗口。 |
| `account` | 邮箱、用户信息、团队、资料、当期用量、额度和 Stripe 资料。 |
| `server_config` | 返回服务配置。 |
| `compatibility` | 隐私模式、插件列表、文档列表、会话元数据等兼容响应。 |
| `knowledge` | 知识库增加、列出、更新、删除。 |
| `commit_message` | 生成 Git 提交说明。 |
| `blob_sync`、`context_sync` | Blob 和上下文同步。 |
| `tab` | Tab 与文件同步相关路径。按设置转到公益服务、官方直连或自定义地址。 |
| `analytics` | Statsig bootstrap。 |
| `usage` | 用量统计。 |
| `observability` | Cursor trace。 |
| `entitlement` | 免费额度外观。 |

## 4. 会话循环 `server/src/run`

与 Cursor 报文解耦的 Agent 循环。

- 单次模型调用、单轮工具调用。
- 幂等追加消息。
- 显式上下文压缩。
- 可重试失败最多 8 次，间隔 5 秒。
- 向外暴露端口，由 Cursor 适配层和上游策略实现。

## 5. 公共数据类型 `server/src/model`

会话、检查点、消息、run、工具调用与结果、模型请求和响应、上游输入投影、模型配置、调用观测、token 统计、工具结果恢复。

## 6. 上游协议 `server/src/provider`

| 模块 | 功能点 |
| --- | --- |
| `openai_chat` | OpenAI Chat Completions：流式文本、推理、工具调用、用量。 |
| `openai_responses` | OpenAI Responses：流式事件、工具调用、提示词缓存字段、用量。 |
| `anthropic` | Anthropic Messages：流式文本、thinking、工具调用、用量。 |
| `event`、`normalize` | 收成统一事件：文本增量、推理增量、工具调用、结束、错误。用量分成输入、输出、缓存读、缓存写。 |
| `router` | 按模型协议类型选择实现。插件模型不走这三种 HTTP 协议。 |
| `request_template` | 基础地址补标准端点，完整 URL 原样使用。自定义 Headers 和额外 JSON 参数不能覆盖 model、stream、messages、input、tools、system 等保留字段。 |
| `attempt` | 记录单次尝试。 |
| `recorder` | 保存请求、响应、耗时和用量。 |

## 7. 持久化 `server/src/store`

SQLite 仓储：

- 会话、检查点、消息、run、工具轮次、输入去重。
- 模型配置、应用设置、调用记录、Cursor trace。
- Blob 存储、控制台概览查询。
- 串行写事务和并发写检查。

设置项包括端口、出站代理、Tab 模式、桌面行为、提交信息所用模型、计价、外部 API 开关、观测详细程度。

## 8. 控制面 `server/src/control`

桌面调用的管理 API，挂在 `/__byok-api__/api/`。

| 模块 | 功能点 |
| --- | --- |
| `models` | 模型增删改、排序、从上游拉取模型 ID、单次和批量连通性测试、取消测试、预览并导入 v0.0.49 配置。 |
| `calls` | 调用记录列表和详情。 |
| `overview` | 首页用量、缓存、延迟和趋势。 |
| `settings` | 端口、出站代理、Tab、桌面、提交信息、计价、外部 API、观测、存储统计和清理。 |
| `harness` | Cursor 接管状态、初始化 CA、开关接管。 |
| `plugins` | 插件列表、运行时初始化、OAuth、资源导入导出、刷新、同步模型、启用模型。 |
| `ads` | 从公益服务域名拉取菜单广告、图片和关闭记录。 |

## 9. 搜索 `server/src/search`

- 搜索入口和可配置的搜索服务目录。
- 多来源聚合。
- 网页抓取和结果缓存。
- 本地代码搜索接到 `crates/semble-core`：语法切块、词法索引、向量与重排。

## 10. 插件 `server/src/plugin` 与 `server/plugins/build-in`

运行时负责安装、加载、状态、OAuth 回调和资源动作。

内置插件：

- `grok-auth`：Grok 登录、资源和模型同步。
- `codex-auth`：Codex 登录、资源和模型同步。
- `antigravity-auth`：Antigravity 登录、资源和模型同步。

## 11. 桌面 `apps/desktop`

Web 控制台页面：

| 页面 | 功能点 |
| --- | --- |
| 首页 | 时间范围、token、缓存命中、延迟、365 天贡献日历、估算价值。 |
| Cursor 配置 | CA、接管开关、模型增删改、复制、排序、分组、批量改地址和密钥、拉取模型 ID、连通性测试、旧配置导入。 |
| 调用记录 | 列表和单次详情。 |
| 插件管理 | 运行时、资源导入导出、OAuth、刷新、同步和启用模型。 |
| 设置 | 端口、出站代理、Tab 三种去向、提交信息模型、计价、外部 API、观测详细程度、语言、主题、开关机、存储清理、检查更新。 |

语言为简体中文、英文、葡萄牙语。

`apps/desktop/src-tauri` 提供窗口、托盘、关闭到托盘、用系统终端打开命令、打开外部链接、内嵌前端、拉起本地服务、启动失败对话框、便携更新和失败回滚。

## 12. 协议与辅助工具

| 位置 | 功能点 |
| --- | --- |
| `protocols/cursor` | Cursor protobuf 定义。 |
| `support/cursor-protocol-extractor` | 从 Cursor 产物提取协议并生成代码。 |
| `support/cursor-capture` | 抓取和调试 Cursor 协议。 |
| `support/benchmarks/semble` | 本地代码搜索的基准测试。 |

## 13. 功能关系

```text
Cursor 客户端
    │ HTTPS
    ▼
local_app 代理与 CA
    │
    ├── Tab、未知 RPC ──► 官方或公益 Tab 或自定义地址
    └── Agent 与账号、模型接口
            ▼
        api/cursor
            ▼
        cursor 适配层
            ▼
        run 循环 ──► provider 上游协议
            │
            ▼
          store
            ▲
            │
     control API ◄── 桌面控制台
```
