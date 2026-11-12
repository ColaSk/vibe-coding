"""Protocol extractor / capture unit checks."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from tools.protocol_capture.server import create_capture_app
from tools.protocol_extractor.scan import extract, render_proto_inventory, scan_text


def test_scan_text_finds_service_paths() -> None:
    sample = 'fetch("/aiserver.v1.BidiService/BidiAppend") + agent.v1.AgentClientMessage'
    services, messages = scan_text(sample)
    assert "/aiserver.v1.BidiService/BidiAppend" in services
    assert "agent.v1.AgentClientMessage" in messages


def test_extract_writes_inventory(tmp_path: Path) -> None:
    bundle = tmp_path / "workbench.desktop.main.js"
    bundle.write_text(
        'const x = "/agent.v1.AgentService/RunSSE"; const y = aiserver.v1.BidiAppendRequest;',
        encoding="utf-8",
    )
    result = extract([bundle])
    assert "/agent.v1.AgentService/RunSSE" in result.services
    proto = render_proto_inventory(result)
    assert "RunSSE" in proto
    assert "service AgentServiceInventory" in proto


def test_capture_ui_and_store(tmp_path: Path) -> None:
    app = create_capture_app(tmp_path / "cap.db")
    with TestClient(app) as client:
        home = client.get("/")
        assert home.status_code == 200
        assert "protocol capture" in home.text
        listed = client.get("/api/exchanges")
        assert listed.status_code == 200
        assert listed.json() == []
