"""CLI: python -m tools.protocol_capture --port 9099."""

from __future__ import annotations

import argparse
from pathlib import Path

import uvicorn

from tools.protocol_capture.server import create_capture_app


def main() -> None:
    parser = argparse.ArgumentParser(description="Cursor protocol capture debug service")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9099)
    parser.add_argument(
        "--db",
        default=str(Path.home() / ".cursor-switch" / "protocol-capture.db"),
    )
    args = parser.parse_args()
    app = create_capture_app(Path(args.db).expanduser())
    print(f"capture UI: http://{args.host}:{args.port}/")
    print(f"sqlite: {args.db}")
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
