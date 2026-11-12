"""Process entry for the control-plane server."""

from __future__ import annotations

import argparse

import uvicorn

from cursor_switch.control.app import create_app


def main() -> None:
    parser = argparse.ArgumentParser(description="cursor-switch control API")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    uvicorn.run(create_app(), host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
