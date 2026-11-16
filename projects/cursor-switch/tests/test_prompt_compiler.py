"""Mode prompt + tools.json loading."""

from __future__ import annotations

from cursor_switch.adapters.cursor.prompting.compiler import (
    PromptCompiler,
    enrich_tools_with_catalog,
    tool_definitions_for_mode,
)


def test_agent_tools_nonempty() -> None:
    tools = tool_definitions_for_mode("agent")
    assert tools
    names = {
        (t.get("function") or {}).get("name")
        for t in tools
        if isinstance(t, dict)
    }
    assert "Shell" in names or "shell" in {str(n).lower() for n in names if n}


def test_system_prompt_agent() -> None:
    prompt = PromptCompiler().system_prompt("agent")
    assert len(prompt) > 20


def test_enrich_tools_fills_empty_client_schemas() -> None:
    """Cursor local_loop often advertises tools with empty Struct parameters."""
    client_tools = [
        {
            "type": "function",
            "function": {
                "name": "Read",
                "description": "Reads a file from disk.",
                "parameters": {"type": "object", "properties": {}},
            },
        },
        {
            "type": "function",
            "function": {
                "name": "Glob",
                "description": "Find files",
                "parameters": {"type": "object", "properties": {}},
            },
        },
        {
            "type": "function",
            "function": {
                "name": "CustomThing",
                "description": "unknown",
                "parameters": {"type": "object", "properties": {}},
            },
        },
    ]
    enriched = enrich_tools_with_catalog(client_tools)
    by_name = {
        (t.get("function") or {}).get("name"): (t.get("function") or {}).get("parameters") or {}
        for t in enriched
    }
    assert "path" in (by_name["Read"].get("properties") or {})
    assert "glob_pattern" in (by_name["Glob"].get("properties") or {})
    # Unknown tools stay as-is (still empty).
    assert (by_name["CustomThing"].get("properties") or {}) == {}


def test_enrich_tools_keeps_nonempty_client_schemas() -> None:
    client_tools = [
        {
            "type": "function",
            "function": {
                "name": "Read",
                "description": "custom",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }
    ]
    enriched = enrich_tools_with_catalog(client_tools)
    params = (enriched[0].get("function") or {}).get("parameters") or {}
    assert list((params.get("properties") or {}).keys()) == ["file_path"]


def test_enrich_tools_fills_create_plan_even_when_agent_mode() -> None:
    """Plan-mode tools (CreatePlan) must enrich from full catalog, not agent allow-list."""
    client_tools = [
        {
            "type": "function",
            "function": {
                "name": "CreatePlan",
                "description": "create a plan",
                "parameters": {"type": "object", "properties": {}},
            },
        }
    ]
    # Mimic gateway: agent-mode allow-list does not include CreatePlan.
    agent_only = tool_definitions_for_mode("agent")
    assert not any(
        (t.get("function") or {}).get("name") == "CreatePlan" for t in agent_only
    )
    enriched = enrich_tools_with_catalog(client_tools, catalog=agent_only)
    props = ((enriched[0].get("function") or {}).get("parameters") or {}).get("properties") or {}
    assert "plan" in props
    assert "overview" in props
