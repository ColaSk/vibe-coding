"""Load mode prompts and OpenAI-style tool definitions from prompt/cursor assets."""

from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any, Literal

AgentMode = Literal["agent", "ask", "plan", "debug", "multitask", "subagent"]


def _assets_root() -> Path:
    # Prefer packaged path under cursor_switch/prompt/cursor
    try:
        root = resources.files("cursor_switch.prompt.cursor")
        return Path(str(root))
    except Exception:  # noqa: BLE001
        return Path(__file__).resolve().parents[3] / "prompt" / "cursor"


@lru_cache(maxsize=1)
def _tools_catalog() -> dict[str, Any]:
    path = _assets_root() / "tools.json"
    if not path.is_file():
        return {"tools": [], "variants": {}}
    return json.loads(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=8)
def _mode_manifest(mode: AgentMode) -> list[str]:
    path = _assets_root() / "modes" / f"{mode}.json"
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    tools = data.get("tools") or []
    names: list[str] = []
    for entry in tools:
        if isinstance(entry, str):
            names.append(entry)
        elif isinstance(entry, dict) and entry.get("name"):
            names.append(str(entry["name"]))
    return names


def all_tool_definitions() -> list[dict[str, Any]]:
    """Return every tool schema in tools.json (all modes)."""
    catalog = _tools_catalog()
    out: list[dict[str, Any]] = []
    for tool in catalog.get("tools") or []:
        function = tool.get("function") if isinstance(tool, dict) else None
        if not isinstance(function, dict):
            continue
        if function.get("name"):
            out.append(tool)
    return out


def tool_definitions_for_mode(mode: AgentMode = "agent") -> list[dict[str, Any]]:
    """Return OpenAI function-calling tool schemas for the mode."""
    by_name: dict[str, dict[str, Any]] = {}
    for tool in all_tool_definitions():
        function = tool.get("function") if isinstance(tool, dict) else None
        if not isinstance(function, dict):
            continue
        name = function.get("name")
        if name:
            by_name[str(name)] = tool
    selected = _mode_manifest(mode)
    if not selected:
        return list(by_name.values())
    out: list[dict[str, Any]] = []
    for name in selected:
        tool = by_name.get(name)
        if tool is not None:
            out.append(tool)
    return out


def _tool_function(tool: dict[str, Any]) -> dict[str, Any] | None:
    if not isinstance(tool, dict):
        return None
    function = tool.get("function")
    if isinstance(function, dict):
        return function
    if tool.get("name"):
        return tool
    return None


def _parameters_properties(parameters: Any) -> dict[str, Any]:
    if not isinstance(parameters, dict):
        return {}
    props = parameters.get("properties")
    return props if isinstance(props, dict) else {}


def enrich_tools_with_catalog(
    tools: list[dict[str, Any]],
    *,
    mode: AgentMode = "agent",
    catalog: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Fill empty client tool schemas from the local catalog.

    Cursor RunInference advertises tools with name/description but often an
    empty protobuf Struct for parameters. Upstream models then emit args={}.

    Always index the full tools.json first so Plan-mode tools (CreatePlan, …)
    enrich even when the gateway is stuck on agent allow-lists.
    """
    del mode  # enrichment is mode-agnostic; keep kw for call-site compat
    by_name: dict[str, dict[str, Any]] = {}

    def _index(source: list[dict[str, Any]]) -> None:
        for tool in source:
            function = _tool_function(tool if isinstance(tool, dict) else {})
            if not function:
                continue
            name = function.get("name")
            params = function.get("parameters")
            if name and _parameters_properties(params):
                by_name[str(name)] = params if isinstance(params, dict) else {}

    _index(all_tool_definitions())
    if catalog is not None:
        _index(catalog)

    out: list[dict[str, Any]] = []
    for tool in tools:
        if not isinstance(tool, dict):
            continue
        cloned = dict(tool)
        function = _tool_function(cloned)
        if function is None:
            out.append(cloned)
            continue
        fn = dict(function)
        name = str(fn.get("name") or "")
        params = fn.get("parameters")
        if name and not _parameters_properties(params) and name in by_name:
            fn["parameters"] = dict(by_name[name])
            if "function" in cloned:
                cloned["function"] = fn
            else:
                cloned = fn
        out.append(cloned)
    return out


class PromptCompiler:
    def __init__(self, root: Path | None = None) -> None:
        self._root = root or _assets_root()

    def system_prompt(self, mode: AgentMode = "agent") -> str:
        prompt_path = self._root / mode / "prompt.md"
        runtime_path = self._root / mode / "runtime.md"
        parts: list[str] = []
        if prompt_path.is_file():
            parts.append(prompt_path.read_text(encoding="utf-8"))
        if runtime_path.is_file():
            parts.append(runtime_path.read_text(encoding="utf-8"))
        return "\n\n".join(parts).strip()

    def tools(self, mode: AgentMode = "agent") -> list[dict[str, Any]]:
        return tool_definitions_for_mode(mode)
