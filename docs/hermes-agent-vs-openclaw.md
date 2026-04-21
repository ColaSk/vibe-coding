# Hermes Agent vs OpenClaw 深度对比

> 更新时间：2026-04-13
> 数据来源：GitHub 官方仓库、The New Stack（2026-04-02）、Medium（Bibek Poudel, Feb 2026）、Nous Research 官方文档

---

## 目录

1. [项目概述](#1-项目概述)
2. [基本信息](#2-基本信息)
3. [核心架构](#3-核心架构)
4. [记忆系统](#4-记忆系统)
5. [技能 / 工具生态](#5-技能--工具生态)
6. [平台集成](#6-平台集成)
7. [模型支持](#7-模型支持)
8. [部署方式](#8-部署方式)
9. [安全性](#9-安全性)
10. [学习与自进化](#10-学习与自进化)
11. [社区与生态](#11-社区与生态)
12. [适用场景](#12-适用场景)
13. [综合对比速查表](#13-综合对比速查表)

---

## 1. 项目概述

当前 AI 编程助手生态正在经历一次分化：以 Claude Code、Cursor 为代表的"会话型"工具在单次会话内能力强大，但每次新建会话后上下文几乎归零；另一类工具则以常驻进程、持久记忆为核心设计目标，力图成为真正"不会遗忘"的个人 AI 助理。**OpenClaw** 与 **Hermes Agent** 是后者中最具代表性的两个开源项目，但它们在实现路径上选择了截然不同的方向。

| | OpenClaw | Hermes Agent |
|---|---|---|
| **一句话定位** | 生态优先的常驻 AI 助理平台 | 研究驱动的自进化 AI Agent 框架 |
| **核心命题** | 连接一切消息平台、拥抱开放生态 | 从每次交互中学习、越用越聪明 |
| **类比** | Android for AI Agents | 带自学习能力的个人知识工作者 |

---

## 2. 基本信息

| 维度 | OpenClaw | Hermes Agent |
|---|---|---|
| **开发方** | Peter Steinberger（个人）→ 独立基金会 | Nous Research（开源 LLM 研究实验室） |
| **前身** | Clawdbot → Moltbot → OpenClaw | — |
| **首次发布** | 2025 年底 | 2026 年 2 月 |
| **最新版本（截至 2026-04）** | — | v0.8.0（3,496+ commits） |
| **许可证** | MIT | MIT |
| **主要编程语言** | JavaScript / Node.js | Python |
| **GitHub Stars** | 356,254 ★ | 74,790 ★ |
| **官网 / 文档** | [docs.openclaw.ai](https://docs.openclaw.ai/) | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/) |
| **GitHub** | [openclaw/openclaw](https://github.com/openclaw/openclaw) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |

---

## 3. 核心架构

### OpenClaw

OpenClaw 的核心是一个 **WebSocket Gateway 进程**（默认监听 `ws://127.0.0.1:18789`），作为整个系统的"神经中枢"负责会话管理、渠道路由和工具编排。消息进入后经过以下七个阶段：

```
渠道适配（Channel Normalization）
    ↓
路由 / 会话分配（Routing & Session）
    ↓
上下文组装（Context Assembly）
    ↓
模型推理（LLM Inference）
    ↓
ReAct 工具循环（Tool Execution Loop）
    ↓
技能加载（On-demand Skill Loading）
    ↓
记忆持久化（Memory & Persistence）
```

关键设计原则：
- **同一会话串行处理**：通过 Command Queue 保证每个会话同一时刻只处理一条消息，防止工具状态冲突。
- **渠道适配层**：所有来源（WhatsApp、Telegram、Slack…）在到达模型前统一归一化为相同的消息对象。
- **文件即状态**：`SOUL.md`（人格）、`MEMORY.md`（长期记忆）、`HEARTBEAT.md`（主动任务）均为纯 Markdown 文件，完全可读、可审计。

### Hermes Agent

Hermes Agent 围绕**封闭学习循环（Closed Learning Loop）**构建，三个关键组件相互配合：

```
用户交互 / 任务执行
    ↓
[技能自动生成]  →  ~/.hermes/skills/（持久化技能库）
    ↓
[记忆写入]      →  SQLite FTS5 全文索引 + LLM 摘要
    ↓
[用户建模]      →  Honcho 辩证用户画像
    ↓
下次类似任务时优先检索技能库 + 历史记忆
```

关键设计原则：
- **学习优先**：架构的核心目标是让 Agent 从每次交互中积累可复用的知识，而非单纯扩展连接数量。
- **研究级基础设施**：内置 Atropos RL 集成，可生成批量 tool-calling 轨迹用于模型微调。
- **多实例 Profiles**：v0.6.0 起支持单一安装下运行多个隔离的 Hermes 实例（独立配置、记忆、技能）。

---

## 4. 记忆系统

| 维度 | OpenClaw | Hermes Agent |
|---|---|---|
| **存储介质** | Markdown 文件 + SQLite（可选 sqlite-vec） | SQLite FTS5 + Markdown 文件 |
| **记忆文件结构** | `MEMORY.md`（长期事实）、`memory/YYYY-MM-DD.md`（每日日志） | `~/.hermes/` 下的 SQLite 数据库，LLM 定期摘要 |
| **检索方式** | 向量检索（sqlite-vec）+ 关键词检索 | FTS5 全文搜索 + LLM 摘要 |
| **上下文压缩** | 超出 context window 时自动摘要旧对话轮次 | 支持 `/compress` 命令手动压缩；LLM 定期摘要 |
| **用户建模** | 无专门模块（依赖 SOUL.md 手动维护） | **Honcho 辩证用户建模**：自动推断用户偏好、工作方式 |
| **记忆注入时机** | Agent 按需读取（避免每轮注入造成 token 浪费） | 同样按需，FTS5 搜索相关片段后注入 |
| **可审计性** | 极高（纯 Markdown，人可直接读写） | 中（SQLite + 摘要，需工具查看） |

**核心差异**：OpenClaw 的记忆是**人工可直接编辑的文件**，透明度最高；Hermes Agent 的记忆由**系统自主维护**，随时间积累更深的用户理解，但可读性稍低。

---

## 5. 技能 / 工具生态

### OpenClaw 技能系统

- **格式**：每个技能是一个包含 `SKILL.md` 的文件夹（YAML frontmatter + 自然语言指令）。
- **加载方式**：上下文组装时只注入技能摘要（名称 + 描述 + 路径），模型主动判断是否需要加载完整技能文件——保持基础 prompt 精简。
- **注册表**：[ClawHub](https://clawhub.ai/) 社区市场，数千个社区贡献技能。
- **安全警告**：Koi Security 在 ClawHub 2,857 个技能中发现 341 个恶意条目（ClawHavoc 攻击活动）；OpenClaw 已与 VirusTotal 合作扫描，但信任模型仍在完善中。
- **内置工具**：文件读写、Shell 命令、Web 浏览、日历、邮件等。

### Hermes Agent 工具系统

- **内置工具**：40+ 开箱即用工具，覆盖 GitHub 操作、Shell 执行、Python RPC、Docker、Web 搜索与抓取、图像生成、TTS、MLOps 等。
- **MCP 支持**：完整支持 Model Context Protocol，可接入任意 MCP Server，理论上工具数量无上限。
- **技能标准**：遵循开放的 [agentskills.io](https://agentskills.io/) 标准，技能具备跨平台可移植性。
- **技能注册表**：规模较小，社区仍在成长；可直接安装 ClawHub 技能。
- **自动技能创建**：完成复杂任务后，Agent 可自动将解题路径提炼为结构化技能文档，下次遇到类似问题时直接复用。

| 维度 | OpenClaw | Hermes Agent |
|---|---|---|
| **内置工具数** | 核心工具集（文件/Shell/Web/通讯） | 40+ |
| **社区技能数量** | 数千（ClawHub） | 较少（agentskills.io） |
| **MCP 支持** | 部分支持（社区适配器） | 完整原生支持 |
| **自动技能生成** | 否 | 是 |
| **跨平台技能标准** | ClawHub 私有格式 | agentskills.io 开放标准 |

---

## 6. 平台集成

| 平台 | OpenClaw | Hermes Agent |
|---|---|---|
| **CLI 终端** | ✅ | ✅ |
| **Telegram** | ✅ | ✅ |
| **Discord** | ✅ | ✅ |
| **Slack** | ✅ | ✅ |
| **WhatsApp** | ✅ | ✅ |
| **Signal** | ✅ | ✅ |
| **iMessage** | ✅ | ❌ |
| **Matrix** | ✅ | ✅ |
| **Mattermost** | ✅ | ✅ |
| **邮件 / SMS** | ✅ | ✅ |
| **Home Assistant** | ❌（需技能） | ✅（原生支持） |
| **WebChat** | ✅ | ❌ |
| **总计** | 50+ 平台 | 14 个平台 |

OpenClaw 在平台覆盖宽度上具有明显优势；Hermes Agent 对 Home Assistant 的原生集成是面向智能家居场景的差异化特性。

---

## 7. 模型支持

两个项目都强调**模型无关（Model-Agnostic）**，不绑定任何单一 LLM 提供商。

| 提供商 | OpenClaw | Hermes Agent |
|---|---|---|
| OpenAI（GPT 系列） | ✅ | ✅ |
| Anthropic Claude | ✅ | ✅ |
| Google Gemini | ✅ | ✅ |
| Nous Portal | ❌ | ✅（官方首选） |
| OpenRouter（200+ 模型） | ✅ | ✅ |
| 本地模型（Ollama） | ✅ | ✅ |
| 自定义 OpenAI 兼容端点 | ✅ | ✅ |
| z.ai / GLM / Kimi / MiniMax | ❌ | ✅ |

**切换方式**：
- OpenClaw：通过配置文件或环境变量切换，无需重启。
- Hermes Agent：`hermes model` 命令一键切换，会话内可用 `/model` 即时切换，零代码改动。

---

## 8. 部署方式

### OpenClaw

- **运行时依赖**：Node.js 22+
- **安装方式**：`npm install -g openclaw@latest`
- **服务化**：通过 `systemd`（Linux）或 `LaunchAgent`（macOS）注册为长驻后台服务
- **配置路径**：`~/.openclaw/`
- **容器化**：推荐在 Docker 容器或独立 VM 中运行（安全考虑）
- **托管方案**：多家第三方托管提供商，以及官方 macOS / iOS 伴侣 App

### Hermes Agent

- **运行时依赖**：Python（无版本特殊要求）
- **安装方式**：`curl -fsSL .../install.sh | bash`
- **支持的 6 种执行后端**：

| 后端 | 适用场景 |
|---|---|
| Local | 本机直接运行 |
| Docker | 隔离环境，本地或服务器 |
| SSH | 远程机器执行 |
| Daytona | 云端可休眠开发环境 |
| Singularity | HPC / GPU 集群 |
| Modal | Serverless，闲置时接近零成本 |

- **多实例支持**：Profiles 机制，单次安装运行多个独立实例
- **MCP 服务模式**：`hermes mcp serve` 将会话暴露给 Claude Desktop、Cursor、VS Code 等 MCP 客户端

**关键差异**：Hermes Agent 的 Serverless 支持（Modal）可将 24/7 个人助理的成本降至每月数美元；OpenClaw 更依赖常驻进程，适合拥有独立服务器的用户。

---

## 9. 安全性

### OpenClaw 安全现状

OpenClaw 因其爆炸式增长和开放的 ClawHub 生态，面临较为严峻的安全挑战：

- **CVE-2026-25253**（CVSS 8.8）：不安全的 WebSocket 自动连接行为可泄露认证 Token，存在一键沦陷场景。
- **ClawHavoc 供应链攻击**：Koi Security 在 ClawHub 的 2,857 个技能中发现 341 个恶意条目（含提示注入、恶意软件、凭证窃取）。
- **公网暴露实例**：SecurityScorecard 报告数万个 OpenClaw 实例直接暴露在互联网上。
- **改进措施**：与 VirusTotal 合作扫描技能包；发布安全操作指南；成立独立基金会加强治理。
- **外部评价**：Microsoft 建议不要在标准个人或企业工作站上运行；Cisco 称其为"安全噩梦"。

### Hermes Agent 安全现状

Hermes Agent 采用更为保守的安全架构：

- **容器加固**：只读根文件系统、最小权限 capabilities、命名空间隔离。
- **文件系统快照**：破坏性操作前自动创建检查点，支持 `rollback` 命令恢复。
- **Tirith 预执行扫描器**：在终端命令执行前进行静态分析，拦截高危操作。
- **技能生态**：遵循 agentskills.io 标准，生态规模小、审查成本低；目前尚无公开的供应链攻击记录。
- **局限性**：更小的攻击面（74k stars vs 356k stars）使其对攻击者吸引力较低，但随规模增长安全压力将加大。

| 安全维度 | OpenClaw | Hermes Agent |
|---|---|---|
| **已知 CVE** | CVE-2026-25253（CVSS 8.8） | 暂无公开记录 |
| **供应链安全** | 曾遭受大规模攻击，修复进行中 | 生态较小，风险较低 |
| **沙箱隔离** | 推荐 Docker/VM，非强制 | 容器加固 + 命名空间隔离 |
| **预执行扫描** | 无内置 | Tirith 扫描器 |
| **文件系统回滚** | 无 | 自动快照 + rollback |
| **安全审计工具** | `openclaw security audit --deep` | 内置 Tirith |
| **推荐运行环境** | 隔离容器 / VM | 本机或容器均可 |

---

## 10. 学习与自进化

这是两个项目**差距最大**的维度。

### OpenClaw

- **会话记忆**：通过 `MEMORY.md` 在会话间保留长期事实。
- **主动行为**：Heartbeat 机制（默认 30 分钟触发一次）读取 `HEARTBEAT.md` 检查任务列表，可主动推送通知。
- **自动学习**：**无**。技能需用户手动创建或从 ClawHub 安装；知识积累依赖用户主动维护。

### Hermes Agent

Hermes 的学习循环由三层组成：

1. **自动技能创建**：完成复杂任务后，Agent 自动将解题路径提炼为结构化 `SKILL.md` 文件，存入 `~/.hermes/skills/`。
2. **技能自我改进**：遇到类似任务时，在已有技能基础上总结新的经验并修订技能文档。
3. **Atropos RL 集成**：可批量生成 tool-calling 轨迹并导出，用于对更小、更便宜的模型进行 RL 微调——这是研究级基础设施，OpenClaw 中完全没有对应能力。

另外，基于 **Honcho 辩证用户建模**，Agent 会逐步推断并记录用户偏好（如"用户喜欢简洁回复"、"用户的项目在 ~/code/"），使其随时间使用越来越"懂你"。

| 学习能力 | OpenClaw | Hermes Agent |
|---|---|---|
| 跨会话记忆 | ✅（文件） | ✅（SQLite + 摘要） |
| 用户画像建模 | ❌ | ✅（Honcho） |
| 自动技能生成 | ❌ | ✅ |
| 技能自我迭代改进 | ❌ | ✅ |
| RL 轨迹生成 / 模型微调 | ❌ | ✅（Atropos） |
| 主动任务执行（Heartbeat） | ✅ | ✅（Cron 调度器） |

---

## 11. 社区与生态

### OpenClaw

- **规模**：356k+ GitHub Stars，是目前增长最快的 AI Agent 开源项目之一。
- **治理**：2026 年 2 月，创始人 Peter Steinberger 加入 OpenAI 后，OpenClaw 迁移至独立基金会管理。
- **技能市场**：[ClawHub](https://clawhub.ai/)，数千个社区技能，支持一键安装。
- **第三方生态**：多家托管服务商、macOS 和 iOS 伴侣 App、企业支持方案。
- **迁移工具**：暂无官方向 Hermes 的迁移路径（反向有）。

### Hermes Agent

- **规模**：74k+ GitHub Stars；v0.8.0 已有 3,496+ commits，迭代活跃。
- **背书**：由 Nous Research 主导，该团队以 Hermes / Nomos / Psyche 等开源模型系列著称。
- **技能标准**：采用 [agentskills.io](https://agentskills.io/) 开放标准，设计上与其他兼容平台互通。
- **迁移工具**：提供 `hermes claw migrate` 命令，可一键从 OpenClaw 导入 SOUL.md、记忆、技能、API Key、消息平台配置等；支持 `--dry-run` 预览。
- **社区规模**：相对较小，但因 Nous Research 的研究背景吸引了不少 AI/ML 研究者。

---

## 12. 适用场景

### 选择 OpenClaw 当你需要：

- **覆盖尽可能多的消息平台**（50+ 集成，包括 iMessage、WebChat 等 Hermes 不支持的渠道）
- **快速上手并利用现成技能**：ClawHub 数千个社区技能可直接安装，无需从零开发
- **团队 Slack/Discord 机器人**：多渠道同时在线、多 Agent 路由能力成熟
- **接受社区管理风险**：理解供应链安全挑战，有能力审查第三方技能
- **需要官方托管或原生 App 体验**：第三方托管 + macOS/iOS 伴侣 App

### 选择 Hermes Agent 当你需要：

- **真正会学习的长期助理**：希望 Agent 从每次交互中积累技能、越用越懂你
- **研究 / MLOps 场景**：需要 RL 轨迹生成、模型微调支持（Atropos 集成）
- **跨平台跨 IDE 整合**：通过 MCP 服务模式接入 Claude Desktop、Cursor、VS Code
- **最小化基础设施成本**：Serverless 后端（Modal）支持，闲置时接近零成本
- **更高的安全基线**：容器加固、Tirith 预执行扫描、文件系统快照回滚
- **Home Assistant 智能家居场景**：原生集成，开箱即用
- **从 OpenClaw 迁移**：官方 `hermes claw migrate` 工具支持无缝迁移

### 两者并用

实际上两者并不互斥。The New Stack 的分析指出，生产环境可能同时用到两者：用 OpenClaw 覆盖广泛的平台集成，用 Hermes Agent 作为深度学习的"大脑"。Hermes 已支持直接从 ClawHub 安装技能，agentskills.io 标准也在推动跨平台技能互通。

---

## 13. 综合对比速查表

| 对比维度 | OpenClaw | Hermes Agent |
|---|---|---|
| **开发语言** | JavaScript / Node.js | Python |
| **GitHub Stars** | 356k ★ | 74k ★ |
| **许可证** | MIT | MIT |
| **发布时间** | 2025 年底 | 2026 年 2 月 |
| **核心哲学** | 生态广度、平台覆盖 | 学习深度、自我进化 |
| **运行模式** | 常驻 Gateway 进程 | 常驻进程 / Serverless |
| **消息平台数** | 50+ | 14 |
| **内置工具数** | 核心工具集 | 40+ |
| **MCP 支持** | 部分（社区适配） | 完整原生 |
| **技能注册表** | ClawHub（数千条） | agentskills.io（较少） |
| **自动技能生成** | ❌ | ✅ |
| **用户建模** | ❌ | ✅（Honcho） |
| **RL / 模型微调** | ❌ | ✅（Atropos） |
| **记忆存储** | Markdown 文件 | SQLite FTS5 + 摘要 |
| **记忆可读性** | 极高（纯文本） | 中 |
| **文件系统回滚** | ❌ | ✅ |
| **预执行安全扫描** | ❌ | ✅（Tirith） |
| **已知 CVE** | CVE-2026-25253（CVSS 8.8） | 暂无 |
| **供应链攻击** | 已发生（ClawHavoc） | 暂无记录 |
| **部署后端数** | 1（Node.js 进程） | 6（Local/Docker/SSH/Daytona/Singularity/Modal） |
| **Home Assistant** | 需技能 | ✅ 原生 |
| **迁移工具** | 无（向 Hermes 迁移） | `hermes claw migrate`（从 OpenClaw 迁入） |
| **推荐人群** | 需要广覆盖、快上手的开发者 | 需要深度学习、研究场景的开发者 |

---

*本文档基于 2026 年 4 月公开资料整理，两个项目均处于活跃迭代阶段，具体功能和数据以各自官方文档为准。*
