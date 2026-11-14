"""Write Cursor User settings so traffic goes through the local MITM proxy."""

from __future__ import annotations

import json
import os
import platform
import re
from pathlib import Path

PROXY_KEYS = (
    "http.proxy",
    "http.proxyKerberosServicePrincipal",
    "http.proxySupport",
    "cursor.general.disableHttp2",
    "http.experimental.systemCertificatesV2",
)
NO_PROXY_KEY = "http.noProxy"


def settings_path() -> Path:
    home = Path.home()
    system = platform.system().lower()
    if system == "darwin":
        return home / "Library/Application Support/Cursor/User/settings.json"
    if system == "windows":
        appdata = Path(os.environ.get("APPDATA") or (home / "AppData/Roaming"))
        return appdata / "Cursor/User/settings.json"
    if system == "linux":
        xdg = Path(os.environ.get("XDG_CONFIG_HOME") or (home / ".config"))
        return xdg / "Cursor/User/settings.json"
    raise RuntimeError(f"Cursor settings unsupported on {system}")


def resolve_settings_path(configured: str | None = None) -> Path:
    """Resolve Cursor settings.json from an optional configured path.

    Empty uses the platform default. A directory may point at the Cursor user
    data root, the User folder, or the file itself.
    """
    raw = (configured or "").strip()
    if not raw:
        return settings_path()
    path = Path(raw).expanduser()
    if path.is_dir():
        if (path / "settings.json").is_file() or path.name == "User":
            return path / "settings.json"
        if (path / "User" / "settings.json").exists() or (path / "User").is_dir():
            return path / "User" / "settings.json"
        return path / "User" / "settings.json"
    return path


def _strip_jsonc(text: str) -> str:
    without_block = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    without_line = re.sub(r"(?m)^\s*//.*?$", "", without_block)
    return without_line


def read_settings(path: Path | None = None) -> dict[str, object]:
    target = path or settings_path()
    if not target.exists():
        return {}
    raw = target.read_text(encoding="utf-8")
    if not raw.strip():
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = json.loads(_strip_jsonc(raw))
    if not isinstance(data, dict):
        raise ValueError("Cursor settings.json must be a JSON object")
    return data


def write_settings(settings: dict[str, object], path: Path | None = None) -> None:
    target = path or settings_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(settings, ensure_ascii=False, indent=2) + "\n"
    temp = target.with_suffix(".json.tmp")
    temp.write_text(payload, encoding="utf-8")
    temp.replace(target)


def apply_proxy(proxy_url: str, path: Path | None = None) -> None:
    settings = read_settings(path)
    settings.pop(NO_PROXY_KEY, None)
    settings["http.proxy"] = proxy_url
    settings["http.proxyKerberosServicePrincipal"] = proxy_url
    settings["http.proxySupport"] = "on"
    settings["cursor.general.disableHttp2"] = True
    settings["http.experimental.systemCertificatesV2"] = True
    write_settings(settings, path)


def clear_proxy(path: Path | None = None) -> None:
    settings = read_settings(path)
    changed = False
    for key in PROXY_KEYS:
        if key in settings:
            settings.pop(key)
            changed = True
    if changed:
        write_settings(settings, path)


def settings_match(proxy_url: str, path: Path | None = None) -> bool:
    settings = read_settings(path)
    return (
        settings.get("http.proxy") == proxy_url
        and settings.get("http.proxyKerberosServicePrincipal") == proxy_url
        and settings.get("http.proxySupport") == "on"
        and settings.get("cursor.general.disableHttp2") is True
        and settings.get("http.experimental.systemCertificatesV2") is True
    )
