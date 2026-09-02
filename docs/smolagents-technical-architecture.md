# smolagents 技术文档

> 更新时间：2026-09-02
> 文档类型：源码级架构 + 模块参考（Diataxis：explanation + reference）
> 调研对象：Hugging Face `smolagents`（本地 checkout）
>
> **数据来源**（按来源级别排序）：
>
> | # | 来源 | 类型 | 级别 | 日期 / 版本 |
> |---|------|------|------|-------------|
> | S1 | 本地仓库 `/Users/sk/projects/smolagents` @ `30bb116`（`pyproject.toml` `1.27.0.dev0`） | 源码 + 仓库文档 | 一级 | 2026-09-02 |
> | S2 | `src/smolagents/*.py`（18 个模块，约 12.8k LOC）+ 3 份 prompt YAML | 实现 | 一级 | 与 S1 同源 |
> | S3 | `README.md`、`SECURITY.md`、`CONTRIBUTING.md`、`docs/source/en/**` | 官方文档 | 一级 | 与 S1 同源 |
> | S4 | `tests/`（27 个 Python 文件）、`examples/` | 行为证明 | 一级 | 与 S1 同源 |
>
> **时效性**：本文事实均来自 2026-09-02 本地 `main`（`origin/main` 同步，HEAD `30bb116`，提交 *Update contribution guidelines (#2679)*，2026-08-22）。
>
> **信心评级**：高 = 源码与官方文档一致；中 = 有源码依据但文档未写清或行为有缺口；低 = 仅从示例/注释推断。

---

## 目录

1. [核心结论速览](#1-核心结论速览)
2. [概述与定位](#2-概述与定位)
3. [仓库地图与分层](#3-仓库地图与分层)
4. [一次 `run()` 的数据路径](#4-一次-run-的数据路径)
5. [Agent 运行时](#5-agent-运行时)
6. [Prompt 契约](#6-prompt-契约)
7. [Memory 与观测](#7-memory-与观测)
8. [工具系统](#8-工具系统)
9. [模型层](#9-模型层)
10. [Python 执行器与沙箱](#10-python-执行器与沙箱)
11. [多模态类型](#11-多模态类型)
12. [Hub 序列化与安全反序列化](#12-hub-序列化与安全反序列化)
13. [CLI、Web Agent、Gradio UI](#13-cliweb-agentgradio-ui)
14. [安全模型](#14-安全模型)
15. [测试、示例与文档 IA](#15-测试示例与文档-ia)
16. [已知实现缺口](#16-已知实现缺口)
17. [适用场景](#17-适用场景)
18. [参考资料](#18-参考资料)

---

## 1. 核心结论速览

smolagents 不是常驻助手平台，而是一个 **进程内、可嵌入的 ReAct Agent 库**：模型产出动作，库负责解析、执行、记记忆、再喂回模型。核心卖点是 **Code Agent**——动作用 Python 代码写，而不是 JSON tool call。

| # | 结论 | 信心 |
|---|------|------|
| 1 | **核心循环在 `MultiStepAgent`**。`run()` 驱动 `PlanningStep?` → `ActionStep` → `FinalAnswerStep`，默认最多 20 个 action step | 高 |
| 2 | **两种动作范式**：`CodeAgent` 解析代码块并交给 `PythonExecutor`；`ToolCallingAgent` 走原生 / JSON tool call，可并行 | 高 |
| 3 | **本地执行器不是安全边界**。`LocalPythonExecutor` 是受限 AST 解释器；隔离必须用 E2B / Docker / Modal / Blaxel | 高 |
| 4 | **模型无关、工具无关**。9 个 `Model` 子类覆盖 HF / LiteLLM / OpenAI / Azure / Bedrock / 本地；工具可来自 `@tool`、Hub Space、LangChain、MCP | 高 |
| 5 | **没有 Gateway、没有持久会话库**。记忆是进程内 `AgentMemory`；跨 run 靠 `reset=False`。要持久化只能自己包一层 | 高 |
| 6 | **Hub 分享走 Gradio Space**。`push_to_hub` / `from_hub` 要求 `trust_remote_code=True`；反序列化只允许 `AGENT_REGISTRY` / `MODEL_REGISTRY` | 高 |
| 7 | **库刻意保持小**。生产 Python 约 12.8k 行、18 个模块；主循环 `agents.py` 1813 行。可选能力全部 extra | 高 |
| 8 | **许可证 Apache-2.0**。Python ≥ 3.10。默认模型 `Qwen/Qwen3-Next-80B-A3B-Thinking` | 高 |

---

## 2. 概述与定位

### 2.1 是什么

`smolagents` 是 Hugging Face 的开源 Python 库：用很少的代码跑多步 Agent。官方口号是 *Agents that think in code*。

最小路径：

```python
from smolagents import CodeAgent, WebSearchTool, InferenceClientModel

agent = CodeAgent(tools=[WebSearchTool()], model=InferenceClientModel(), stream_outputs=True)
agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
```

### 2.2 解决什么问题

经典 tool-calling Agent 每一步只能发一个（或一组）结构化调用，组合逻辑要靠多轮 LLM。Code Agent 把工具暴露成 Python 函数，模型可以在 **同一步** 里写循环、条件、嵌套调用。论文依据见 README：代码动作相对 JSON 调用可减少约 30% 步数。

它 **不** 解决：多渠道接入、常驻 Gateway、多租户、审批、SQLite 会话、插件生命周期。那些是 OpenClaw 一类运行时的问题。

### 2.3 运行时形状

一次 `agent.run(task)` 是同步调用（可 `stream=True` 返回 generator）。没有后台 worker，没有跨进程协议。要接到 HTTP，仓库示例用 Starlette + `anyio.to_thread.run_sync` 把同步 `run()` 丢到线程里。

---

## 3. 仓库地图与分层

### 3.1 目录

```
smolagents/
├── src/smolagents/          # 唯一生产包
│   ├── agents.py            # 1813  MultiStepAgent / CodeAgent / ToolCallingAgent
│   ├── models.py            # 2102  Model 基类与全部供应商适配
│   ├── local_python_executor.py  # 1768  AST 解释器
│   ├── tools.py             # 1422  Tool / @tool / Hub / LangChain / Gradio
│   ├── remote_executors.py  # 1076  E2B / Docker / Modal / Blaxel
│   ├── default_tools.py     #  698  内置工具
│   ├── utils.py             #  606  错误、解析、源码提取、限流
│   ├── serialization.py     #  514  远程变量安全序列化
│   ├── gradio_ui.py         #  464  聊天 UI
│   ├── _function_type_hints_utils.py  # 431  @tool schema
│   ├── memory.py            #  316  步骤记忆
│   ├── cli.py               #  294  smolagent 入口
│   ├── agent_types.py       #  284  Text/Image/Audio
│   ├── monitoring.py        #  273  日志 / token / 树可视化
│   ├── tool_validation.py   #  263  Hub 工具静态检查
│   ├── vision_web_browser.py # 247  webagent
│   ├── mcp_client.py        #  171  MCPAdapt 封装
│   └── prompts/*.yaml       #  3 份 Jinja prompt
├── tests/                   # 27 个测试文件
├── examples/                # RAG / SQL / 多层 Agent / 沙箱 / 服务
└── docs/source/{en,zh,ko,hi,es}/
```

包数据：`smolagents.prompts` 随包分发 YAML（`pyproject.toml` `package-data`）。

入口脚本：

| 命令 | 入口 |
|------|------|
| `smolagent` | `smolagents.cli:main` |
| `webagent` | `smolagents.vision_web_browser:main` |

### 3.2 分层（从下到上）

```
┌─────────────────────────────────────────────────────────┐
│  CLI / GradioUI / examples.server / webagent            │  产品表面
├─────────────────────────────────────────────────────────┤
│  CodeAgent / ToolCallingAgent  (ReAct 循环)             │  编排
├──────────────┬──────────────────┬───────────────────────┤
│  AgentMemory │  Model.generate  │  Tool / PythonExecutor│  三件套
├──────────────┴──────────────────┴───────────────────────┤
│  ChatMessage · Prompt YAML · SafeSerializer · AgentType │  契约
└─────────────────────────────────────────────────────────┘
```

Core 依赖（必装）：`huggingface-hub`、`requests`、`rich`、`jinja2`、`pillow>=10.0.1`、`python-dotenv`。其余全部 extra。

### 3.3 Extra 地图

| Extra | 打开的能力 |
|-------|------------|
| `toolkit` | DuckDuckGo 搜索、`VisitWebpageTool`（ddgs + markdownify） |
| `litellm` / `openai` / `bedrock` | 对应 Model 子类 |
| `transformers` / `torch` / `vllm` / `mlx-lm` | 本地推理 |
| `e2b` / `docker` / `modal` / `blaxel` | 远程沙箱 |
| `mcp` | MCPClient / ToolCollection.from_mcp |
| `gradio` | GradioUI、工具 demo、Hub Space 导出 |
| `vision` | Helium + Selenium（webagent） |
| `audio` | AgentAudio / soundfile |
| `telemetry` | OpenTelemetry + Arize Phoenix |
| `all` | 上述几乎全部（不含 vllm） |

---

## 4. 一次 `run()` 的数据路径

以 `CodeAgent.run("计算 1 到 10 的和")` 为例（非 stream）。

```
run(task)
  │
  ├─ max_steps = max_steps or self.max_steps     # 0 会回落到 20
  ├─ interrupt_switch = False
  ├─ additional_args → self.state，并追加到 task 文本
  ├─ 刷新 SystemPromptStep
  ├─ reset=True → memory.reset() + monitor.reset()
  ├─ append TaskStep(task, images)
  ├─ 若有 python_executor：send_variables(state) + send_tools(tools ∪ managed_agents)
  │
  └─ 排干 _run_stream()
        while step_number ≤ max_steps:
          若 interrupt_switch → AgentError
          若 planning_interval 且 (step==1 或 (step-1) % N == 0):
              PlanningStep（不消耗 step_number）
          ActionStep
              _step_stream:  model.generate → 解析代码 → executor(code)
              ActionOutput(is_final_answer) → final_answer_checks
              AgentGenerationError → 中止整个 run
              其他 AgentError → 记到 step.error，继续
          step_number += 1
        若仍无 final：provide_final_answer + AgentMaxStepsError
        yield FinalAnswerStep(handle_agent_output_types(output))
```

非 stream 路径取最后一个 `FinalAnswerStep.output`。`return_full_result=True` 时包成 `RunResult`（output、state、steps、token_usage、timing）。`state` 为 `"max_steps_error"` 当且仅当最后一步的 error 是 `AgentMaxStepsError`。

**规划不占 step 号。** 是否「首次规划」看 `len(memory.steps) == 1`（只有 TaskStep）。`reset=False` 续跑时会走「更新规划」模板。

---

## 5. Agent 运行时

### 5.1 `MultiStepAgent`（抽象基类）

文件：`src/smolagents/agents.py:268`。

构造参数与默认值：

| 参数 | 默认 | 作用 |
|------|------|------|
| `tools` | 必填 | `BaseTool` 列表，存成 `{name: tool}` |
| `model` | 必填 | `Model` 实例 |
| `prompt_templates` | 空模板 | 必须含 `EMPTY_PROMPT_TEMPLATES` 全部键 |
| `instructions` | `None` | 注入 system prompt 的 `custom_instructions` |
| `max_steps` | **20** | Action 步上限 |
| `add_base_tools` | `False` | 合并 `TOOL_MAPPING`；`python_interpreter` 只给 ToolCallingAgent |
| `verbosity_level` | `LogLevel.INFO` | 仅在未传入 `logger` 时生效 |
| `managed_agents` | `None` | 子 Agent，必须有 `name` + `description` |
| `step_callbacks` | `None` | list → 只挂 `ActionStep`；dict → 按步骤类型 |
| `planning_interval` | `None` | 每隔 N 个 action step 做一次规划 |
| `name` / `description` | `None` | 作为 managed agent 时必填；name 须是合法 Python 标识符 |
| `provide_run_summary` | `False` | 被调用时附加截断记忆摘要 |
| `final_answer_checks` | `[]` | `(answer, memory, agent) -> bool` |
| `return_full_result` | `False` | 返回 `RunResult` |
| `logger` | 自动建 | `AgentLogger` |

硬约束：

- 始终 `setdefault("final_answer", FinalAnswerTool())`（`agents.py:402`）
- tools、managed agents、自身 `name` 必须唯一（`agents.py:404-414`）
- `system_prompt` 是只读 property，子类实现 `initialize_system_prompt()`
- 每次 `run()` 会用当前 tools/instructions **重算** system prompt 并写回 memory

公共方法：`run`、`interrupt`、`visualize`、`replay`、`save`、`to_dict` / `from_dict`、`from_hub` / `from_folder`、`push_to_hub`。Managed agent 通过 `__call__(task)` 包装任务模板再 `run()`。

`interrupt()` 只把 `interrupt_switch` 设为 True，**只在 while 下一轮开头检查**，生成和工具执行中途不停。

### 5.2 `ToolCallingAgent`

文件：`agents.py:1215`。Prompt：`prompts/toolcalling_agent.yaml`。

一步：

1. `write_memory_to_messages()` → `model.generate(..., tools_to_call_from=tools+managed_agents)`，stop 于 `Observation:` / `Calling tools:`
2. 无原生 `tool_calls` 时 `model.parse_tool_calls`
3. `process_tool_calls`：单调用同步；多调用 `ThreadPoolExecutor` + `copy_context()`，观察结果按 tool-call id 排序拼接
4. 工具名 `final_answer` 视为结束；**不能与其他 tool call 同轮混用**

字符串参数若等于 `state` 的 key，会被替换成 state 值。图像/音频结果写入 `state`（`image.png` / `audio.mp3`）。参数校验失败 → `AgentToolCallError`；执行失败 → `AgentToolExecutionError`。

`max_tool_threads` 控制并行度，默认跟随 `ThreadPoolExecutor`。

### 5.3 `CodeAgent`

文件：`agents.py:1505`。Prompt：`code_agent.yaml` 或（`use_structured_outputs_internally=True`）`structured_code_agent.yaml`。

一步：

1. 生成文本；非结构化用 `parse_code_blobs` 抽代码；结构化用 `CODEAGENT_RESPONSE_FORMAT`（`{"thought","code"}` JSON schema）
2. `fix_final_answer_code`：避免 `final_answer = ...` 遮蔽 `final_answer()` 调用
3. 合成一个 `ToolCall(name="python_interpreter", arguments=code)`
4. `python_executor(code)` → logs + 截断后的最后输出；`is_final_answer` 来自执行器里对 `final_answer()` 的捕获

代码块标签默认 `("<code>", "</code>")`；`code_block_tags="markdown"` 则用 ` ```python ` / ` ``` `。若闭标签是开标签的子串，则 **不加** 闭标签 stop sequence，以免截断生成。

`executor_type`：`local`（默认）/ `blaxel` / `e2b` / `modal` / `docker`。远程执行器 + managed agents 直接抛 `Exception`（`agents.py:1608-1609`）。作为 context manager 时会 `cleanup()` 远程沙箱。

`add_base_tools=True` 时 **不会** 再加 `python_interpreter` 工具，因为执行循环本身就是解释器。

### 5.4 多层 Agent

Manager 把子 Agent 当工具：注入 `inputs={task, additional_args}`、`output_type="string"`。`__call__` 用 `managed_agent.task` / `.report` 模板包一层。可选 `provide_run_summary` 追加 `<summary_of_work>`。

远程沙箱不能带 managed agents：工具要以源码重建到远端，子 Agent 不是可序列化 Tool。

### 5.5 `RunResult` 与 stream

`RunResult` 字段：`output`、`state`（`success` | `max_steps_error`）、`steps`、`token_usage`、`timing`。`messages` 是 `steps` 的弃用别名，注释写 1.25 删除。

`run(stream=True)` 返回 generator，调用方必须迭代。事件类型 `StreamEvent`：`ChatMessageStreamDelta`、`ChatMessageToolCall`、`ActionOutput`、`ToolCall`、`ToolOutput`、`PlanningStep`、`ActionStep`、`FinalAnswerStep`。

---

## 6. Prompt 契约

三份 YAML 共享同一 TypedDict（`agents.py:125-192`）：

```
system_prompt
planning:
  initial_plan
  update_plan_pre_messages
  update_plan_post_messages
managed_agent:
  task
  report
final_answer:
  pre_messages
  post_messages
```

渲染：`populate_template` + Jinja **`StrictUndefined`**，缺变量直接失败。

| 模板 | 变量 | 时机 |
|------|------|------|
| ToolCalling `system_prompt` | tools, managed_agents, custom_instructions | 每次 run 刷新 |
| Code `system_prompt` | 上列 + authorized_imports, code_block_*_tag | 同上 |
| `planning.initial_plan` | task, tools, managed_agents | 首次规划 |
| `planning.update_plan_*` | task, tools, managed_agents, remaining_steps | 后续规划 |
| `managed_agent.*` | name, task / final_answer | 子 Agent 调用 |
| `final_answer.pre_messages` | **无**（字面量） | 步数耗尽兜底 |
| `final_answer.post_messages` | task | 同上 |

行为约定：

- Tool-calling：每步必须发 tool call；只能靠 `final_answer` 结束
- Code：Thought + 代码块；工具通过 `tool.to_code_prompt()` 写成函数签名
- Structured code：JSON `{thought, code}`，schema 强制形状
- Planning：事实盘点 + 计划，模型 stop 于 `<end_plan>`

---

## 7. Memory 与观测

### 7.1 步骤类型（`memory.py`）

| 类型 | 写入时机 | `to_messages` |
|------|----------|----------------|
| `SystemPromptStep` | 每次 run 刷新 | SYSTEM；`summary_mode` 下为空 |
| `TaskStep` | run 开始 | USER `"New task:\n..."` + 可选图片 |
| `PlanningStep` | 规划间隔 | ASSISTANT 计划 + USER 继续指令；summary 下为空 |
| `ActionStep` | 每步 | 见下 |
| `FinalAnswerStep` | 循环结束 | **没有** `to_messages`，不进对话重建 |

`ActionStep.to_messages` 顺序：模型输出（非 summary）→ `Calling tools:` → 观察图片 → `Observation:` → error（带重试提示）。

`AgentMemory.reset()` 只清 steps，保留 system prompt。`return_full_code()` 拼接所有 `ActionStep.code_action`。

`CallbackRegistry` 按步骤类的 MRO 分发。1 参回调只收 step；多参再传 `agent=`。Monitor 的 `update_metrics` 默认挂在每个 `ActionStep` 上。

### 7.2 日志与指标（`monitoring.py`）

- `LogLevel`：OFF=-1, ERROR=0, INFO=1, DEBUG=2
- `TokenUsage`：input / output / total
- `Timing`：start / end / duration
- `Monitor`：累计 ActionStep 时长与 token；**规划步不计入** Monitor 合计
- `AgentLogger`：Rich 面板；`visualize_agent_tree` 画 tools + 嵌套 managed agents（CodeAgent 会列出 imports）

注意：`log_rule` 的 `level` 参数被忽略，始终按 INFO 打（`monitoring.py:190-198`）。

---

## 8. 工具系统

### 8.1 `Tool` 契约（`tools.py`）

必填类属性：`name`（合法标识符）、`description`、`inputs`（每项含 `type`+`description`）、`output_type`。

授权类型：`string | boolean | integer | number | image | audio | array | object | any | null`。

调用：`__call__` 懒 `setup()`；`sanitize_inputs_outputs=True` 时走 `handle_agent_input_types` / `handle_agent_output_types`。`output_schema` 只进文档，**不做运行时输出校验**。

两种 prompt 形态：

- `to_code_prompt()`：Python `def` 风格（CodeAgent）
- `to_tool_calling_prompt()`：一行 name/description/inputs

### 8.2 定义工具的四条路

1. **继承 `Tool`**，实现 `forward`
2. **`@tool`**：从类型注解 + Google docstring 生成 schema（`_function_type_hints_utils.get_json_schema`）。必须有返回类型；Args 描述必填；`(choices: [...])` → enum
3. **`PipelineTool`**：Transformers pipeline（encode → forward → decode），需 `smolagents[transformers]`
4. **适配外部**：`from_hub` / `from_space` / `from_gradio` / `from_langchain` / MCP

Hub 工具 `to_dict` / `from_code` 会 `exec` 源码。Space / LangChain / Gradio wrapper **不能** `to_dict`（明确拒绝）。`from_hub` 要求 `trust_remote_code=True`。

`validate_tool_attributes`（`tool_validation.py`）在序列化前做 AST 检查：`__init__` 参数必须有字面量默认值；类属性只能是常量容器；方法里不能引用未定义名字。文档声称禁 local import，但 `check_imports` **从未被咨询**——只靠名字是否已定义。

### 8.3 内置工具（`default_tools.py`）

| 类 | `name` | 后端 | 备注 |
|----|--------|------|------|
| `FinalAnswerTool` | `final_answer` | 恒等 | Agent 强制注入 |
| `PythonInterpreterTool` | `python_interpreter` | 本地 AST，超时 30s | 默认 import = `BASE_BUILTIN_MODULES` |
| `UserInputTool` | `user_input` | `input()` | 交互 stdin |
| `DuckDuckGoSearchTool` | `web_search` | `ddgs` | 默认 1 qps |
| `GoogleSearchTool` | `web_search` | SerpAPI / Serper | 环境变量 API key |
| `ApiWebSearchTool` | `web_search` | 默认 Brave | `BRAVE_API_KEY`，1 qps |
| `WebSearchTool` | `web_search` | duckduckgo HTML / Bing RSS / Exa | Exa 需 `EXA_API_KEY` |
| `VisitWebpageTool` | `visit_webpage` | requests + markdownify | 20s 超时，截断 40k |
| `WikipediaSearchTool` | `wikipedia_search` | wikipediaapi | 必须传 `user_agent` |
| `SpeechToTextTool` | `transcriber` | Whisper pipeline | 默认 `openai/whisper-large-v3-turbo` |

`TOOL_MAPPING`（`add_base_tools` / CLI 可选表）**只有** PythonInterpreter、DuckDuckGoSearch、VisitWebpage 三个。其余要显式传入。多个搜索工具同名 `web_search`，不能同时放进同一个 Agent。

### 8.4 MCP（`mcp_client.py`）

`MCPClient` 在 `__init__` 就 `connect()`。传输：

- `StdioServerParameters`：子进程 stdio
- `{"url", "transport"}`：`streamable-http`（默认）或遗留 `sse`

`structured_output=False` 为当前默认（纯文本）；`True` 启用 outputSchema / structuredContent。未指定时 FutureWarning：1.25 将默认改为 True。依赖 `smolagents[mcp]`（mcpadapt）。

`ToolCollection.from_mcp` 是 context manager，同样要求 `trust_remote_code=True`。可一次接多个 server。

---

## 9. 模型层

### 9.1 基类 `Model`（`models.py:452`）

必须实现 `generate(messages, **kwargs) -> ChatMessage`。部分子类另有 `generate_stream`。

`_prepare_completion_kwargs` 优先级：特定参数 ← 调用 kwargs ← `self.kwargs`。`REMOVE_PARAMETER` 可删键。`tool_choice` 默认 `"required"`。

`parse_tool_calls`：没有结构化 tool_calls 时，从文本 JSON 用 `tool_name_key`/`tool_arguments_key`（默认 `name`/`arguments`）解析。

`supports_stop_parameter`：对 o3\* / o4\* / gpt-5\* / grok-\*（除 `o3-mini`）返回 False。

消息类型：`ChatMessage`（role、content、tool_calls、raw、token_usage）。Role：`user | assistant | system | tool-call | tool-response`。`agglomerate_stream_deltas` 按 index 合并流式 tool_call。

`get_tool_json_schema` 把工具编成 OpenAI function schema；参数里 `"any"` 变成 `"string"`。

API 模型共用 `ApiModel`：`RateLimiter`（`requests_per_minute`）+ `Retrying`（最多 3 次，底 60s，指数 2，jitter）。429 / “rate limit” 视为可重试。

`to_dict` **拒绝导出** `token` / `api_key`（打印警告）。

### 9.2 子类对照

| 类 | 后端 | Extra | Stream | 原生 tool_calls | 要点 |
|----|------|-------|--------|-----------------|------|
| `InferenceClientModel` | HF Inference Providers | 核心依赖 | 是 | 是 | 默认 Qwen3-Next-80B-A3B-Thinking；timeout=120；结构化输出仅 cerebras / fireworks-ai |
| `LiteLLMModel` | LiteLLM | `litellm` | 是 | 是 | 未指定模型时警告并落到 claude-3-5-sonnet；ollama/groq/cerebras flatten 文本 |
| `LiteLLMRouterModel` | LiteLLM Router | `litellm` | 继承 | 继承 | `model_list` + 路由策略 |
| `OpenAIModel` | OpenAI 兼容 | `openai` | 是 | 是 | Together / OpenRouter 改 `api_base` |
| `AzureOpenAIModel` | Azure OpenAI | `openai` | 继承 | 继承 | `azure_endpoint` + `api_version` |
| `AmazonBedrockModel` | Bedrock Converse | `bedrock` | **否** | 弹出 `toolConfig`；角色默认全映射为 user | **拒** `response_format` |
| `TransformersModel` | 本地 HF | `transformers` | 是（线程 + TextIteratorStreamer） | 模板内嵌，返回文本 | 自动选 VLM；默认 max_new_tokens=4096 |
| `VLLMModel` | vLLM | `vllm` | 无 generate_stream | 模板内嵌，返回文本 | 支持 structured outputs params |
| `MLXModel` | mlx_lm | `mlx-lm` | 内部 stream_generate，对外仍 `generate` | 模板内嵌 | **拒** `response_format`；flatten 文本 |

别名：`OpenAIServerModel`、`AzureOpenAIServerModel`、`AmazonBedrockServerModel`。

`MODEL_REGISTRY` 只包含上表实体类（不含 ApiModel 基类）。Hub 反序列化只能实例化注册表里的类。

---

## 10. Python 执行器与沙箱

### 10.1 接口

```python
class PythonExecutor(ABC):
    def send_tools(self, tools: dict[str, Tool]) -> None: ...
    def send_variables(self, variables: dict[str, Any]) -> None: ...
    def __call__(self, code_action: str) -> CodeOutput: ...  # output, logs, is_final_answer
```

### 10.2 `LocalPythonExecutor`

**不是沙箱**（类文档与 `SECURITY.md` 一致）。机制是自定义 AST 解释器，不是 CPython `exec`。

白名单模块 `BASE_BUILTIN_MODULES`：`collections datetime itertools math queue random re stat statistics time unicodedata`。

限额：输出 50_000 字符；操作 10_000_000；while 1_000_000 次；默认超时 30s（线程池；超时后 worker **可能继续跑**，见 `local_python_executor.py:298-301`）。

允许的静态内建在 `BASE_PYTHON_TOOLS`（print 重定向到 state、isinstance、range、容器、受限 getattr 等）。禁止：

- 危险模块：`os sys io socket subprocess multiprocessing pathlib shutil pty builtins`
- 危险函数：`eval exec compile __import__ globals locals os.system` 等
- dunder 属性访问；dunder 调用除 `__init__/__str__/__repr__`
- 覆盖 static tool 名
- 未授权 import（`*` 等于放开全部，有日志警告）

支持的 AST：赋值、循环、推导、函数/类定义、try/raise/assert/with、import、lambda 等。**不支持** async / yield / match / global / nonlocal / await。

`final_answer` 被包成抛 `FinalAnswerException`（`BaseException`，普通 `except Exception` 接不住）。

状态跨多次 `__call__` 保留，这是 CodeAgent「变量在步骤间还在」的来源。

### 10.3 远程执行器（`remote_executors.py`）

基类 `RemotePythonExecutor`：`send_tools` 把工具源码重建到远端（`get_tools_definition_code`），必要时 `!pip install`；`send_variables` 用 `SafeSerializer`；`final_answer` 同样改成可跨进程识别的异常。默认 **禁止 pickle**（`allow_pickle=False`）。

| 执行器 | 隔离 | 运行模型 | Extra | 差异 |
|--------|------|----------|-------|------|
| `E2BExecutor` | E2B 云沙箱 | `sandbox.run_code` | `e2b` | 非 Jupyter；结果 MIME（图/表/html）最全；`sandbox.kill()` |
| `DockerExecutor` | 本机 Docker | Jupyter Kernel Gateway + WS | `docker` | 默认 python:3.12 + jupyter_kernel_gateway；`KG_AUTH_TOKEN` |
| `ModalExecutor` | Modal 云 | 同上 WSS tunnel | `modal` | 默认 5 分钟 sandbox |
| `BlaxelExecutor` | Blaxel VM | Jupyter WS + Blaxel 鉴权 | `blaxel` | 装包走 Blaxel process API 而非 `!pip`；默认 4096MB |

Docker / Modal / Blaxel 共用 Jupyter execute_request 协议。工具必须能通过 `validate_tool_attributes`（可源码重建），不能 pickle 任意闭包。

`SafeSerializer`（`serialization.py`）：JSON + `__type__` 标记（tuple/set/bytes/datetime/PIL/numpy/dataclass）。`allow_pickle=True` 才回落到 pickle，并 FutureWarning。

---

## 11. 多模态类型

`agent_types.py`：`AgentType` 同时当原生对象和展示包装。

| 类型 | 行为像 | 输入 | `to_string` |
|------|--------|------|-------------|
| `AgentText` | `str` | 任意 | `str(_value)` |
| `AgentImage` | `PIL.Image` | Image / bytes / path / tensor | 临时 `.png` 路径 |
| `AgentAudio` | `str` | path / tensor / `(sr, array)` | 临时 `.wav`；需 `[audio]`；默认 16 kHz |

`handle_agent_input_types` 在进工具前拆成 raw；`handle_agent_output_types` 按声明类型或运行时类再包回去。

`run(..., images=[...])` 把同一列表设到 **每个** ActionStep 的 `observations_images`，因此图片会在每步记忆里再出现一次，除非调用方自己清。

---

## 12. Hub 序列化与安全反序列化

### 12.1 Agent `save` / Hub

`save(output_dir)` 写出：

- `tools/{name}.py`
- `managed_agents/{name}/`（递归）
- `agent.json`、`prompts.yaml`
- `requirements.txt`（静态扫描 import）
- Gradio `app.py`（供 Space）

`push_to_hub` 建成 Gradio Space，打 tag `smolagents`、`agent`。`from_hub` 下载 Space 后 `from_folder`，**必须** `trust_remote_code=True`。旧名 `HfApiModel` 会 remap 成 `InferenceClientModel`。

### 12.2 注册表白名单

```python
AGENT_REGISTRY = {"ToolCallingAgent": ToolCallingAgent, "CodeAgent": CodeAgent}
MODEL_REGISTRY = {VLLM, MLX, Transformers, LiteLLM, LiteLLMRouter,
                  InferenceClient, OpenAI, AzureOpenAI, AmazonBedrock}
```

`from_dict` **不用** `importlib` 加载任意类。`to_dict` 不序列化：`final_answer_checks`、`step_callbacks`、`instructions`、`return_full_result`、`stream_outputs`、`use_structured_outputs_internally`；CodeAgent 的 `code_block_tags` `from_dict` 能读，但 `to_dict` 不写。

工具 `from_code` 仍是 `exec`。信任边界是「你选择加载的 Hub 仓库」，与 SECURITY 的 artifact 信任模型一致。

---

## 13. CLI、Web Agent、Gradio UI

### 13.1 `smolagent`

| 参数 | 默认 | 作用 |
|------|------|------|
| 位置参数 `prompt` | 无则进入交互向导 | 任务 |
| `--model-type` | `InferenceClientModel` | |
| `--action-type` | `code` | `code` / `tool_calling` |
| `--model-id` | `Qwen/Qwen3-Next-80B-A3B-Thinking` | |
| `--imports` | `[]` | CodeAgent 额外 import |
| `--tools` | `["web_search"]` | `TOOL_MAPPING` 名或 Hub `user/space` |
| `--provider` / `--api-base` / `--api-key` | 可选 | |
| `--verbosity-level` | `1` | **解析了但没传给 `run_smolagent`** |

`load_model` 支持 InferenceClient / OpenAI / LiteLLM / Transformers。Agent 固定 `stream_outputs=True`。

交互模式会问 action type，但随后把 `action_type = "code"` 写死（`cli.py:168`），**交互里选 tool_calling 无效**。这是实现缺口，见 §16。

### 13.2 `webagent`

默认 `LiteLLMModel` + `gpt-4o`。Helium 驱非无头 Chrome；工具：`WebSearchTool`、`go_back`、`close_popups`、`search_item_ctrl_f`；`additional_authorized_imports` 含 helium；`step_callbacks` 存截图并丢掉更早的图以控制上下文。`max_steps=20`。

### 13.3 `GradioUI`

`gradio_ui.py`：ChatInterface 包 `MultiStepAgent`。可上传文件、每轮 `reset_agent_memory`、流式渲染 Action/Planning/Final。Final 按 `AgentText` / `AgentImage` / `AgentAudio` 分支。`launch` 默认 `share=True, debug=True`。兼容 Gradio 5/6 的 `type="messages"`。

---

## 14. 安全模型

官方威胁模型（`SECURITY.md`）：

1. **加载你未创建的 artifact 是信任决策。** 恶意模型/工具执行代码属于文档化风险，不是漏洞。`safetensors`、钉 revision、`trust_remote_code` 只给已审查仓库。
2. **本地执行器不是安全边界。** 逃逸、读宿主机文件、出网 = 预期行为，**不在漏洞范围**。沙箱后端的真实逃逸才 in-scope。
3. CLI / 示例 / 测试不是库 API 攻击面。

库内具体控制：

| 控制 | 做什么 | 不做什么 |
|------|--------|----------|
| AST 白名单 | 挡住常见 `os.system` / `__import__` | 不隔离进程、FS、网络 |
| 远程沙箱 | 真隔离 | 工具源码仍在沙箱内执行 |
| `trust_remote_code` | Hub 加载显式同意 | 同意后仍 `exec` |
| AGENT/MODEL_REGISTRY | 反序列化不能任意 import | 不保护 Tool `from_code` |
| SafeSerializer | 默认禁 pickle | `allow_pickle=True` 即回到 pickle |
| RateLimiter / Retrying | API 429 | 不是授权 |
| `FinalAnswerException` 用 BaseException | 用户代码 `except Exception` 拦不住结束 | |

报告漏洞：GitHub Security tab 或 `security@huggingface.co`。无赏金。必须带可复现 PoC + 版本 + 跨越的信任边界。

---

## 15. 测试、示例与文档 IA

### 15.1 测试（`tests/`，27 个文件）

核心：`test_agents.py`（循环、RunResult、多层、错误）、`test_local_python_executor.py`（含 `TestLocalPythonExecutorSecurity`）、`test_models.py`、`test_tools.py`、`test_memory.py`、`test_remote_executors.py`、`test_mcp_client.py`、`test_serialization.py`。

表面：`test_cli.py`、`test_gradio_ui.py`、`test_vision_web_browser.py`、`test_all_docs.py`（文档片段可执行）、`test_telemetry.py`、`test_import.py`（无 extra 也能 import）。

命令：`make test` → `pytest ./tests`；`make quality` / `style` → ruff。

### 15.2 示例

| 路径 | 证明的能力 |
|------|------------|
| `agent_from_any_llm.py` | 换模型后端 |
| `multiple_tools.py` | `@tool` |
| `text_to_sql.py` | 自纠正 SQL |
| `rag.py` / `rag_using_chromadb.py` | Agentic RAG |
| `sandboxed_execution.py` | 四种远程 executor |
| `structured_output_tool.py` | MCP structured output |
| `plan_customization/` | HITL：打断 PlanningStep、改计划、`reset=False` |
| `async_agent/` | Starlette + 线程跑同步 `run()` |
| `server/` | 聊天 HTTP + MCPClient |
| `open_deep_research/` | 多层研究 Agent、GAIA、视觉浏览 |
| `smolagents_benchmark/` | 基准跑分 |
| `inspect_multiagent_run.py` | Phoenix telemetry |
| `gradio_ui.py` | 最小 UI + planning_interval |

### 15.3 文档

`docs/source/en/_toctree.yml`：Get started → Tutorials → Conceptual → Examples → Reference。

语言：en（最全）/ zh / ko / hi / es（es 基本只有入门；zh/hi 缺部分新页）。发布：https://huggingface.co/docs/smolagents

贡献：大于 typo 的改动要先 issue 且 maintainer 打 `status:accepted` 再写 PR（`CONTRIBUTING.md`）。核心保持原语，集成放 Hub。

---

## 16. 已知实现缺口

以下均有源码依据，不是猜测。

| ID | 现象 | 位置 | 影响 |
|----|------|------|------|
| G1 | CLI `--verbosity-level` 解析后丢弃 | `cli.py:85-89` vs `280-289` | 命令行无法改日志级别 |
| G2 | 交互向导把 `action_type` 重置为 `"code"` | `cli.py:168` | 交互选 ToolCallingAgent 无效 |
| G3 | `run(max_steps=0)` 因 `max_steps or self.max_steps` 变成 20 | `agents.py:468` | 0 被当成未传 |
| G4 | `images=` 每步重复写入 `observations_images` | `agents.py:574` | 视觉上下文膨胀 |
| G5 | `interrupt` 只在步间生效 | `agents.py:754` | 长工具调用停不下来 |
| G6 | Monitor 不含 PlanningStep token/时长 | `monitoring.py` + 只挂 ActionStep callback | 指标偏低 |
| G7 | `to_dict` 漏掉若干运行时字段 | `agents.py` save 路径 | Hub 往返丢失 instructions / stream / structured / tags |
| G8 | Tool validation 的 `check_imports` 未使用 | `tool_validation.py` | 文档与实现不符 |
| G9 | 远程 CodeAgent 禁止 managed agents | `agents.py:1608` | 沙箱里不能多层 |
| G10 | Bedrock / MLX / Transformers 对 structured output 支持不完整 | 各 Model 子类 | CodeAgent `use_structured_outputs_internally` 不能随便换后端 |
| G11 | 超时后本地 worker 可能继续执行 | `local_python_executor.py:298-301` | 超时不是硬杀 |

`RunResult.messages` 弃用（目标 1.25）；MCP `structured_output` 默认将在 1.25 改为 True。写集成时按即将变化处理。

---

## 17. 适用场景

**适合**

- 在应用进程里嵌一个会写代码的 Agent（数据分析、SQL、RAG、浏览）
- 需要在单步里组合多个工具（循环/条件），而不是每步一次 JSON call
- 已有 MCP / LangChain / Gradio Space 工具，想直接接上
- 用 E2B/Docker/Modal/Blaxel 跑不信任代码

**不适合**

- 常驻多渠道助手、审批、多租户、持久会话（那是 OpenClaw 的问题域）
- 把 `LocalPythonExecutor` 当生产隔离
- 需要异步原生 `run()`（只有示例级的线程包装）
- 需要稳定的跨版本 Agent JSON 契约（`to_dict` 不完整）

**和 OpenClaw 的边界一句话**：smolagents 是 **库**（调用 `run()` 得到答案）；OpenClaw 是 **运行时**（Gateway 常驻、渠道、状态库、插件）。可以把 smolagents 当 OpenClaw 里某一种 harness，但两者默认产品形状不同。

---

## 18. 参考资料

| 资源 | URL / 路径 |
|------|------------|
| 源码 HEAD | `30bb1161095dbae2271e6bc3cc4c219cc3897a57` |
| 官方文档 | https://huggingface.co/docs/smolagents |
| Launch blog | https://huggingface.co/blog/smolagents |
| 安全策略 | `SECURITY.md` |
| 贡献 | `CONTRIBUTING.md` |
| Code Agent 论文（README 引用） | https://huggingface.co/papers/2402.01030 、 https://huggingface.co/papers/2411.01747 |
| 主循环 | `src/smolagents/agents.py` |
| 执行器 | `src/smolagents/local_python_executor.py`、`remote_executors.py` |
| 模型 | `src/smolagents/models.py` |
| 工具 | `src/smolagents/tools.py`、`default_tools.py` |

---

## 自检记录

- 覆盖生产包全部 18 个 `.py` + 3 份 prompt YAML + `pyproject.toml` extras/scripts
- Agent 循环、工具、模型、执行器、CLI/UI 均有文件:行依据
- 安全结论与 `SECURITY.md` 对齐
- 明确标出 CLI 交互 bug、verbosity 丢弃、`max_steps=0`、序列化缺口
- 未声称 LocalPythonExecutor 为沙箱
- 未把 examples 里的能力写成核心库 API
- 版本：`1.27.0.dev0` @ `30bb116`（2026-08-22），文档日期 2026-09-02
