# Python 管理

> 本文是 Python 解释器、环境与依赖的 **唯一权威定义**。其它文档只引用，不重复。
> 硬约束见 `AGENTS.md`，架构见 `docs/architecture.md`。

## 1. 职责划分

一件事只有一个所有者，这是整套规则的出发点。

- **conda** 只管两件事：提供解释器、隔离环境。不用它装 Python 包。
- **`pyproject.toml`** 是依赖的唯一声明来源，运行时依赖与 dev 依赖都在这里。
- **`environment.yml`** 只记解释器与 `pip`，不记任何 Python 包。
- **`pip`** 只负责按 `pyproject.toml` 安装，不作为决策者。要求 pip ≥ 25.1（`--group` 从该版本引入）。

为什么划这条线：conda 和 pip 都能装 Python 包，一旦两边都装，同一个包会有两份元数据，升级时互相覆盖，且故障现象是「明明装了却 import 不到」。把包的所有权完全交给 pip + pyproject，这类问题就不存在。

## 2. 解释器

**Python 3.14.7**，来自 conda-forge。

版本策略分两层，刻意不同：

- **库的兼容声明**：`pyproject.toml` 写 `requires-python = ">=3.14"`。这是对使用者的承诺，宽范围。
- **开发环境**：钉到精确的 `3.14.7`。开发与验证应当在确定的解释器上进行，`make check` 的绿色才有意义。

两条选择的理由：

- **不用系统 Python**。本机系统 Python 是 3.9.6，conda base 是 3.9.12，都太旧且是共享的。项目不碰它们。
- **不用 3.15**。目前只有 `rc2`，预发布版不做地基。3.15 正式发布后按第 9 节的升级流程走。
- **选最新稳定版的代价是要核实 wheel 覆盖**，已逐个确认：`grimp`（分层检查的分析后端）与 `mypy` 有 `cp314` wheel，`pydantic`、`import-linter`、`pytest-asyncio`、`ruff` 均声明支持 3.14，`httpx` 是纯 Python 包。

## 3. 环境

一个项目一个 conda 环境，名字与项目同名：`littleagent`。

```bash
conda create -n littleagent -c conda-forge --override-channels python=3.14.7 pip
conda activate littleagent
pip install -e . --group dev
```

`-c conda-forge --override-channels` 不是可选的：它把求解范围限制到单一 channel。本机 conda 是 4.12.0，经典 solver 很慢（一次 `conda search python` 实测 91 秒），缩小 channel 范围是最直接的提速手段。若建环境仍然卡住，装 `conda-libmamba-solver` 或升级 conda，不要盲等。

`pip` 显式列在创建命令里——它是安装器，属于环境的地基，不是项目依赖。装好后确认 `pip --version` ≥ 25.1，否则 `--group` 不可用。

## 4. pip 与 pyproject.toml 如何配合

### 4.1 pip 只读文件的一部分

`pyproject.toml` 里有两类互不相干的内容，读者不同：

- **pip 读**：`[build-system]`（用哪个构建后端）、`[project]`（包名、版本、`requires-python`、`dependencies`）、`[dependency-groups]`（本地开发依赖）。
- **pip 完全不读**：`[tool.ruff]`、`[tool.mypy]`、`[tool.pytest.ini_options]`、`[tool.importlinter]`。这些由各工具自己读自己那一段。

所以这个文件同时是依赖声明和全工具配置中心，但两件事走的是不同读者。这正是它能当「唯一声明来源」的原因——不需要再散落 `setup.cfg`、`.importlinter`、`pytest.ini` 之类的文件。

### 4.2 `pip install -e .` 实际做了什么

1. 读 `[build-system].requires`，在隔离环境里装构建后端（`hatchling`）。
2. 调用后端的 PEP 660 `build_editable` 钩子，生成一个 editable wheel。
3. 这个 wheel 不含源码，只含一个把 `littleagent` 指向 `src/littleagent` 的导入钩子。
4. 按 `[project].dependencies` 装运行时依赖；加了 `--group dev` 则一并装开发依赖。

### 4.3 这次安装是刚需，不只是便利

可编辑安装让源码改动立即生效，这是次要收益。真正的原因是 `make check` 的两项检查都建立在「`littleagent` 是一个已安装的可导入包」之上：

- `import-linter` 要求 `root_package` 必须可导入，它靠真实导入来构建依赖图。没装就无法做分层检查。
- pytest 从已安装包导入 `littleagent`，而不是靠 `sys.path` 碰巧命中。src 布局下这能避免「测试导入的是另一份代码」这类假绿。

### 4.4 什么时候需要重新安装

- **需要**：改了依赖声明，或改了 `[project.scripts]` 入口点。
- **不需要**：改源码、新增模块、改 `[tool.*]` 配置（pip 不参与这些）。

### 4.5 src 布局要告诉后端包在哪

构建后端用 `hatchling`：配置最少，PEP 660 原生支持，不需要 `setup.py`。

```toml
[build-system]
requires = ["hatchling>=1.32"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/littleagent"]
```

版本号只放 `[project].version` 一处，不在 `__init__.py` 里再写一份 `__version__`——需要时用 `importlib.metadata.version("littleagent")` 读。两处版本号必然会不同步。

## 5. 依赖声明

全部写在 `pyproject.toml`，分三组：

- **运行时依赖**（`[project].dependencies`）：`httpx`（异步 HTTP）、`pydantic`（边界校验与 JSON Schema 导出）。核心预算 ≤3 个。
- **开发依赖**（`[dependency-groups].dev`）：`ruff`、`mypy`、`pytest`、`pytest-asyncio`、`import-linter`。
- **能力 extras**（`[project.optional-dependencies]`）：将来的可选后端各自一组，永不进核心。

开发依赖用 PEP 735 的 `[dependency-groups]`，**不用 extras**。理由是 extras 会被打进发布的包元数据——放成 extras，使用者 `pip install littleagent[dev]` 就能装到我们的 ruff 和 mypy，那是开发工具向下游泄漏。dependency groups 只存在于源码树，不进 wheel。extras 留给真正面向使用者的可选能力。

版本约束的写法是有规则的，不是随手写：

```toml
dependencies = [
  "httpx>=0.28,<1",
  "pydantic>=2.13,<3",
]
```

下界取实际需要的最低可用版本，上界按主版本封顶。**不钉死精确版本**——littleagent 是库，会被装进别人的环境，钉死必然引发版本冲突；封顶主版本则挡住破坏性变更。这是库项目的标准做法，不是图省事。

开发依赖同样写范围，当前可用版本：`ruff 0.16.7`、`mypy 2.3.1`、`pytest 9.1.1`、`pytest-asyncio 1.4.0`、`import-linter 2.15`。

## 6. 分层检查的配置落点

`import-linter` 的配置也在 `pyproject.toml`。它的 `layers` 契约支持用 `|` 分隔同层兄弟模块，语义正好是「同层，且互相不许 import」，所以架构文档里「四层单向 + L1 内部互相独立」两条不变量能用 **一个** 契约表达：

```toml
[tool.importlinter]
root_package = "littleagent"

[[tool.importlinter.contracts]]
name = "四层单向依赖，L1 内部互相独立"
type = "layers"
layers = [
  "littleagent.cli",
  "littleagent.agent",
  "littleagent.model | littleagent.tool | littleagent.memory | littleagent.action | littleagent.observe | littleagent.prompt",
  "littleagent.contracts",
]
```

同层用 `|`（互相独立）还是 `:`（允许互相 import）是语义选择，不能混用。这里必须是 `|`。

## 7. 锁定策略

**现阶段不生成锁文件。** 这是一个有明确前提的决定，不是遗漏。

前提：当前共 2 个运行时依赖 + 5 个 dev 工具，全部是成熟且向后兼容良好的包；维护锁文件的成本高于它带来的收益。`AGENTS.md` 要求新增文件必须立刻抵租，锁文件现在租不上。

**触发条件**——出现下列任一情况就引入锁定，不要再拖：

- 接入 CI，需要保证 CI 与本地跑的是同一批版本。
- 出现第二台开发机器或第二个协作者。
- 某次依赖升级导致 `make check` 意外变红，说明漂移已经在造成成本。

**届时的方案**：引入 `pip-tools`，用 `pip-compile` 从 `pyproject.toml` 生成并提交 `requirements-dev.lock`，`Makefile` 加一个 `make lock` 目标。只锁开发与 CI 环境，运行时依赖仍然保持范围约束——库不锁运行时依赖这条不会因为引入锁文件而改变。

## 8. environment.yml 的边界

只记解释器与安装器：

```yaml
name: littleagent
channels:
  - conda-forge
dependencies:
  - python=3.14.7
  - pip
```

它的用途是让别人一条命令拿到正确的解释器，不是描述完整依赖。`pip` 在这里是环境地基而非项目依赖。**任何 Python 包都不写进这里**——写进去就重新制造了第 1 节要避免的双所有权问题。

## 9. 常用操作

**新增一个依赖**：先写进 `pyproject.toml` 的对应分组，再 `pip install -e . --group dev`。顺序不能反——直接 `pip install` 一个未声明的包，会造成「本机能跑、别人装不上」，且下次重建环境就消失。

**升级 Python 小版本**：不做原地升级，新建环境替换。原地升 Python 容易留下旧版本的编译产物与残留路径。

```bash
conda create -n littleagent-3148 -c conda-forge --override-channels python=3.14.8 pip
conda activate littleagent-3148
pip install -e . --group dev
make check
```

全绿后更新 `environment.yml` 与文档里的版本号，删掉旧环境；不绿就留在旧环境上排查，不要带着红色切换。

**重建环境**（依赖装坏、状态可疑时的首选手段，比逐个排查便宜）：

```bash
conda env remove -n littleagent
conda create -n littleagent -c conda-forge --override-channels python=3.14.7 pip
conda activate littleagent
pip install -e . --group dev
```

## 10. 禁止事项

违反其中任何一条都会把环境问题变成难排查的问题。

- 不在 conda `base` 环境里装本项目的任何依赖。
- 不用 `conda install` 装 Python 包，解释器之外一律走 pip。
- 不在 conda 环境里再建 `venv` 或 `.venv`——两层环境嵌套会让「当前用的是哪个解释器」变得不可预测。
- 不叠第三方项目管理器（uv、poetry、pdm）。conda 已负责环境，pyproject 已负责依赖，再加一层只会制造所有权争夺。
- 不把 Python 包写进 `environment.yml`。
- 不 `pip install` 未写进 `pyproject.toml` 的包。
- 不把开发工具放进 `[project.optional-dependencies]`。extras 会进发布元数据，开发工具会因此泄漏给使用者；它们属于 `[dependency-groups]`。
- 不修改系统 Python 或 conda base 的 Python。
- 不为了让某个依赖装上而放宽 `mypy` / lint 配置，或降级 Python 版本；先判断这个依赖是否真的必要——核心依赖预算只有 3 个。

## 11. 故障处理

- **conda 建环境或 search 很慢**：确认带了 `-c conda-forge --override-channels`；仍慢就装 `conda-libmamba-solver` 或升级 conda。本机 conda 4.12.0 的经典 solver 是已知瓶颈。
- **`no such option: --group`**：pip 低于 25.1。`pip install -U pip` 后重试。
- **某依赖没有 cp314 wheel**：先查 PyPI 确认是否真的缺。缺就不引入它——不要把「用 sdist 现场编译」当常态，那会让环境搭建在每台机器上变成不确定过程。依赖预算本来就紧，删掉需求比迁就依赖更符合项目取向。
- **装了包却 import 不到**：通常是激活了错误的环境，或曾经用 conda 装过同名包。`python -c "import sys; print(sys.executable)"` 确认解释器路径；有双所有权嫌疑就直接按第 9 节重建环境。
- **`import-linter` 报找不到 `littleagent`**：`root_package` 必须可导入，说明没做可编辑安装。跑 `pip install -e . --group dev`。
- **`make check` 在新环境变红但代码没动**：说明依赖漂移已经产生成本，按第 7 节的触发条件引入锁定。
