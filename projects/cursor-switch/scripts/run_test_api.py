#!/usr/bin/env python3
"""Run control API bound to Cursor-SwitchTest settings (manual test harness)."""

from __future__ import annotations

import logging
import os
from pathlib import Path

import uvicorn

from cursor_switch.control.app import create_app


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("cursor_switch.proxy").setLevel(logging.INFO)
    logging.getLogger("cursor_switch.gateway").setLevel(logging.INFO)
    logging.getLogger("cursor_switch.agent_ws").setLevel(logging.INFO)

    settings = Path(
        os.environ.get(
            "CURSOR_SWITCH_TEST_SETTINGS",
            str(
                Path.home()
                / "Library/Application Support/Cursor-SwitchTest/User/settings.json"
            ),
        )
    )
    app = create_app(cursor_settings_path=settings)
    uvicorn.run(app, host="127.0.0.1", port=8787, log_level="info")


if __name__ == "__main__":
    main()
