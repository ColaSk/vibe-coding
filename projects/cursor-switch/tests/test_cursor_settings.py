"""Cursor settings.json proxy helpers."""

from pathlib import Path

from cursor_switch.adapters.local_access.cursor_settings import (
    apply_proxy,
    clear_proxy,
    settings_match,
)


def test_apply_and_clear_proxy(tmp_path: Path) -> None:
    path = tmp_path / "settings.json"
    path.write_text('{\n  "editor.fontSize": 14\n}\n', encoding="utf-8")
    apply_proxy("http://127.0.0.1:54321", path)
    assert settings_match("http://127.0.0.1:54321", path)
    text = path.read_text(encoding="utf-8")
    assert '"editor.fontSize": 14' in text
    assert '"http.proxySupport": "on"' in text
    clear_proxy(path)
    assert not settings_match("http://127.0.0.1:54321", path)
    assert '"editor.fontSize": 14' in path.read_text(encoding="utf-8")
