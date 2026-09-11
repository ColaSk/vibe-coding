# littleagent

一个进程内、async-first、协议驱动的极简 Agent 框架。

模型产出动作，框架负责解析、执行、记忆、再喂回模型。整个循环只有一份实现，动作范式、模型后端、工具、记忆都是注入的协议实现。

> 当前状态：设计定稿，实现按 `docs/roadmap.md` 分阶段进行。

## 设计取向

- **async 为核心**。流式、并行工具调用、取消传播本质都是异步的。同步入口只是一层薄包装。
- **一个循环，多种范式**。「模型如何表达动作」是注入的 `ActionStrategy`，不是 Agent 子类。新增范式是新增文件，不改循环。
- **协议优先于继承**。模型、工具、记忆、动作范式全部是 `Protocol`，实现可替换、可单测。
- **极简是硬指标**。核心运行时依赖只有 `httpx` 与 `pydantic`；单文件 ≤300 行；新增文件必须立刻抵租。
- **库，不是运行时**。不做常驻服务、多租户、审批流、渠道接入。

## 环境

**Python 3.14.7**，用 conda 建独立环境。

```bash
conda create -n littleagent -c conda-forge --override-channels python=3.14.7 pip
conda activate littleagent
pip install -e . --group dev
```

分工：conda 只提供解释器与环境隔离，依赖声明全部在 `pyproject.toml`——运行时依赖在 `[project].dependencies`，开发依赖在 `[dependency-groups].dev`（PEP 735，需要 pip ≥ 25.1）。新增依赖要先写进 `pyproject.toml` 再安装，不要直接 `pip install`。

可编辑安装是必需的，不只是图方便：分层检查要求 `littleagent` 是可导入的已安装包。

完整规则——版本策略、依赖约束写法、锁定策略、升级与重建流程、禁止事项——见 `docs/python-environment.md`。

## 快速开始

```python
import asyncio
from littleagent import Agent, OpenAICompatModel, tool


@tool
async def get_weather(city: str) -> str:
    """查询城市当前天气。

    Args:
        city: 城市名，例如「杭州」。
    """
    return f"{city} 晴，24℃，东南风 2 级"


async def main() -> None:
    agent = Agent(
        model=OpenAICompatModel(model="your-model"),
        tools=[get_weather],
    )
    result = await agent.arun("杭州现在适合出门跑步吗？")
    print(result.status, result.answer)


asyncio.run(main())
```

`arun` 返回 `RunResult`，包含最终答案、封闭的 `status`（`succeeded` / `max_steps_exceeded` / `failed` / `cancelled`）、完整步骤记录、token 用量与耗时。

## 开发命令

```bash
make check    # format 检查 + lint + mypy --strict + 分层检查 + 测试
make test     # 只跑测试
make fmt      # 就地格式化
```

`make check` 是唯一入口。不要绕过它单跑某个工具就宣称完成。

## 文档

- `AGENTS.md` — 硬约束与不变量，改代码前必读
- `docs/architecture.md` — 分层、核心契约、数据路径、扩展点
- `docs/roadmap.md` — 阶段划分与出口条件
