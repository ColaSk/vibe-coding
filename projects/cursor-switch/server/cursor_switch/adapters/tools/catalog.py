"""Mode → tool name allow-lists."""

from __future__ import annotations

from typing import Literal

AgentMode = Literal["agent", "ask", "plan", "debug", "multitask", "subagent"]

CORE_READ = (
    "Read",
    "Glob",
    "Grep",
    "ReadLints",
    "SembleSearch",
    "SembleFindRelated",
    "WebSearch",
    "WebFetch",
)

CORE_WRITE = (
    "Write",
    "StrReplace",
    "Delete",
    "EditNotebook",
    "Shell",
)

ORCHESTRATION = (
    "AskQuestion",
    "TodoWrite",
    "SwitchMode",
    "Task",
    "CreatePlan",
    "UpdateCurrentStep",
)

MCP = ("GetMcpTools", "FetchMcpResource", "CallMcpTool")

EXTRA = ("GenerateImage",)

_MODE_TOOLS: dict[AgentMode, tuple[str, ...]] = {
    "agent": CORE_READ + CORE_WRITE + ORCHESTRATION + MCP + EXTRA,
    "ask": CORE_READ + ("AskQuestion", "WebSearch", "WebFetch"),
    "plan": CORE_READ + ("CreatePlan", "AskQuestion", "TodoWrite", "UpdateCurrentStep"),
    "debug": CORE_READ + CORE_WRITE + ("Shell", "AskQuestion", "TodoWrite"),
    "multitask": CORE_READ + CORE_WRITE + ORCHESTRATION + MCP + EXTRA,
    "subagent": CORE_READ + CORE_WRITE + ("TodoWrite", "UpdateCurrentStep") + MCP,
}


def tools_for_mode(mode: AgentMode) -> list[str]:
    return list(_MODE_TOOLS[mode])
