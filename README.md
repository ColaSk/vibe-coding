# vibe-coding

用 AI 写项目的实验容器：代码、约束、调研笔记放在同一仓库。

长期要活的项目走约束驱动——先写 `AGENTS.md`、阶段出口和单一检查入口，再让 Agent 在护栏里写。一次性原型可以纯 vibe，到期要么删，要么补护栏再留下。方法与落地建议见 [docs/ai-assisted-project-landscape.md](docs/ai-assisted-project-landscape.md)。

## 仓库结构

```
vibe-coding/
├── projects/
│   ├── littleagent/      # 极简 Agent 框架（设计定稿，按路线实现）
│   ├── auto-reverser/    # Electron 浏览器自动逆向
│   ├── vibe-vue/         # Vue 3 + Vite 前端实验
│   └── skills/           # Agent Skills（tech-research、service-scaffold）
├── docs/                 # 调研、对比、设计概览
└── README.md
```

各子项目自带 README；根文件只做导航，不重复维护细节。

## 项目

### littleagent

进程内、async-first、协议驱动的极简 Agent 框架。库，不是运行时：模型产出动作，框架解析、执行、记忆、再喂回模型。

当前状态：设计定稿，实现按 `docs/roadmap.md` 分阶段进行。动手前先读项目内 `AGENTS.md`。

```bash
cd projects/littleagent
conda activate littleagent
make check    # 唯一完成入口：format + lint + mypy --strict + 分层检查 + 测试
```

环境与依赖规则见 `projects/littleagent/docs/python-environment.md`。概览见 [docs/littleagent-design-overview.md](docs/littleagent-design-overview.md)。

### auto-reverser

Electron 桌面工具：加载页面、捕获请求、定位数据接口、分析并尝试破解常见加密参数，可导出脚本。仅供合法安全研究与授权测试。

```bash
cd projects/auto-reverser
npm install
npm run dev     # 开发
npm start       # 运行
```

### vibe-vue

Vue 3 + Vite（rolldown-vite）前端实验，带 ESLint / Stylelint / Prettier 规范。

```bash
cd projects/vibe-vue
npm install
npm run dev     # http://localhost:5173/
npm run lint && npm run lint:style && npm run format
```

规范入口：`projects/vibe-vue/docs/`。

### skills/tech-research

技术调研 Skill：对比、深度调研、选型评估、全景扫描四种模式，输出结构化中文文档。`docs/` 里多数调研笔记按这套流程写成。

### skills/service-scaffold

服务脚手架 Skill：新建 HTTP 服务。当前语言是 Python/FastAPI，MySQL、Redis、Kafka、RabbitMQ 放在 `app/core`，用 `*_ENABLED` 开关插拔，并用同名 Docker Compose profile 启动对应后端。

## 文档

| 文档 | 类型 |
|------|------|
| [ai-assisted-project-landscape.md](docs/ai-assisted-project-landscape.md) | 用 AI 写项目的方案全景与本仓库推荐路径 |
| [littleagent-design-overview.md](docs/littleagent-design-overview.md) | littleagent 定位、决策与阶段 |
| [openclaw-architecture-deep-dive.md](docs/openclaw-architecture-deep-dive.md) | OpenClaw 架构调研 |
| [smolagents-technical-architecture.md](docs/smolagents-technical-architecture.md) | Hugging Face smolagents 源码级架构 |
| [hermes-agent-vs-openclaw.md](docs/hermes-agent-vs-openclaw.md) | Hermes Agent 与 OpenClaw 对比 |
| [tdsql-deep-dive.md](docs/tdsql-deep-dive.md) | TDSQL 深度调研 |
| [tdsql-vs-mysql.md](docs/tdsql-vs-mysql.md) | TDSQL 与 MySQL 对比 |
| [tdsql-mysql-deep-dive.md](docs/tdsql-mysql-deep-dive.md) | TDSQL-MySQL 兼容层 |
| [mysql-to-tdsql-migration.md](docs/mysql-to-tdsql-migration.md) | MySQL 迁 TDSQL 注意事项 |
| [meituan-data-governance-deep-dive.md](docs/meituan-data-governance-deep-dive.md) | 美团酒旅数据治理实践 |
| [data-warehouse-modeling-deep-dive.md](docs/data-warehouse-modeling-deep-dive.md) | 数仓建模基础知识与名词 |

`docs/vibecoding方法论.md` 不再平行维护第二套方法，只指向全景扫描。

## 新开项目

复制 littleagent 的顺序：先 P0 护栏（约束 + 检查入口），再规格与契约，最后实现。不要先让 Agent「搭一个能跑的框架」。细节见全景扫描第 10、11 节。
