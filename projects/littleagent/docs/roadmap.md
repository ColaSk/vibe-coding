# littleagent 路线

> 每个阶段有可验证的出口条件。出口条件没达成就不进下一阶段。
> 架构见 `docs/architecture.md`，约束见 `AGENTS.md`。

阶段划分遵循一条节奏：**契约优先，一次一层**。先落数据形状，再写表达期望的测试，最后写实现。

## P0 环境与护栏

建立能约束后续所有产出的地基。这一阶段不写任何业务逻辑。

- conda 环境：`python=3.14.7` + `pip`，落 `environment.yml`。规则见 `docs/python-environment.md`。
- `pyproject.toml`：`hatchling` 构建后端 + src 布局、`requires-python = ">=3.14"`、核心依赖 `httpx>=0.28,<1` + `pydantic>=2.13,<3`、`[dependency-groups].dev` 放 `ruff` / `mypy` / `pytest` / `pytest-asyncio` / `import-linter`。不生成锁文件，触发条件见环境文档第 7 节。
- 可编辑安装：`pip install -e . --group dev`。分层检查要求 `littleagent` 可导入，这一步是后续检查的前置条件。
- `ruff` 配置：format + lint，开启未使用代码检查。
- `mypy --strict` 配置。
- `import-linter` 契约：一个 `layers` 契约同时表达四层单向与 L1 内部互相独立（同层用 `|` 分隔）。
- `Makefile`：`make check` / `make test` / `make fmt`。
- `AGENTS.md`、`README.md`、本文件、`docs/architecture.md` 与 `docs/python-environment.md`。
- `src/littleagent/__init__.py` 与各层空包。

**出口条件**：新环境里 `python -c "import littleagent"` 通过；`make check` 全绿；故意加一条反向 import（让 `contracts/` import `model/`）能被 `lint-imports` 抓到，删掉后恢复全绿。

## P1 最小闭环

跑通「任务进去，多步工具调用，最终答案出来」，且不需要真实 API key 就能验证。

- `contracts/`：`message` / `step` / `event` / `errors` 四件套，配序列化 round-trip 属性测试。
- `model/base.py`：`Model` 协议、`ModelRequest`、`ToolSchema`。
- `model/openai_compat.py`：唯一内置后端，`agenerate` 先行。
- `tool/`：`Tool` 抽象、`@tool` 从签名与 docstring 生成 pydantic 参数模型与 JSON Schema、`ToolRegistry` 的唯一名校验与边界校验调度。
- `tool/builtin/final_answer.py`。
- `memory/steps.py`：`AgentMemory` 与 steps → messages 投影。
- `action/base.py`：`ActionStrategy` 协议与 `ActionOutcome` 封闭联合。
- `action/toolcall.py`：Tool Calling 范式。
- `agent.py`：唯一推理循环。
- `tests/fakes.py`：脚本化 `FakeModel`。

**出口条件**：用 `FakeModel` 跑通一个多步闭环（至少两次工具调用后给出最终答案），并覆盖四条失败路径——步数耗尽、工具参数不合法、工具内部报错、模型调用失败。四条路径都要断言产生了对应的 `ActionStep` 记录与正确的 `status`。

本次落地范围建议到这里为止。P0 + P1 是一个自洽的可用框架。

## P2 可观测与可取消

让运行过程可见、可中断。

- `contracts/event.py` 的 `StreamEvent` 投入使用，`Model.agenerate_stream` 实装。
- `Agent.astream`：产出文本增量、工具调用请求、工具结果、步骤完成、运行完成。
- `observe/logging.py`：结构化日志与计量收口（token、耗时在步骤记录构造处统一收集）。
- 取消：asyncio 原生取消贯穿模型请求与工具执行；超时即取消，语义为「已请求取消」。

**出口条件**：流式事件序列有断言测试（事件类型与顺序）；在模型生成中途和工具执行中途分别触发取消，都能立即返回且产生 `cancelled` 状态与该步记录。

## P3 表面

让人能用手跑起来。

- `cli.py`：命令行入口。
- 同步入口包装：全仓库唯一的 `asyncio.run` 出现在这里。
- `examples/`：至少一个真实模型可跑的示例。
- `README.md` 的快速开始与真实输出对齐。

**出口条件**：在干净环境里按 README 步骤走一遍，用真实模型跑通一个 example。

## P4 补齐基础能力

每一项独立进入，且除规划步外都不触碰 `agent.py`。进入顺序按需要决定，不必全做。

- **规划步**：以可选 planner 协议注入。这是唯一需要在循环里加一处分支的能力，实现时要明确记录这处例外。
- **多层 Agent**：让 `Agent` 实现 `Tool` 协议，作为工具注入上层 Agent。不引入「子 Agent」这个额外概念。
- **外部工具协议客户端**：产出 `Tool` 列表的工厂，接进 `ToolRegistry`。
- **代码动作范式**：新增 `ActionStrategy` 实现 + 执行器。默认走进程或容器隔离；本地执行永不宣称隔离，威胁模型写进文档。
- **持久化记忆**：`AgentMemory` 的另一个实现。
- **更多模型后端**：各自一个 `Model` 实现，一律 extras。

**每项的通用出口条件**：不改动 `agent.py`（规划步除外）；有边界测试与故障注入测试；`make check` 全绿；新增依赖进 extras 而非核心。
