"""CLI: python -m tools.protocol_extractor --input Cursor.app --output protocols/cursor."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.protocol_extractor.scan import discover_bundles, extract, render_proto_inventory


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract Cursor protocol inventory from JS bundles")
    parser.add_argument(
        "--input",
        action="append",
        dest="inputs",
        required=True,
        help="Cursor.app / bundle file; repeatable",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for inventory.json and inventory.proto",
    )
    args = parser.parse_args(argv)

    bundles: list[Path] = []
    for raw in args.inputs:
        bundles.extend(discover_bundles(Path(raw).expanduser()))
    if not bundles:
        print("No Cursor JS bundles found under the given inputs.", file=sys.stderr)
        return 1

    output = Path(args.output).expanduser().resolve()
    if output in {Path("/"), Path.home(), Path.cwd()}:
        print(f"Refusing unsafe output directory: {output}", file=sys.stderr)
        return 1
    output.mkdir(parents=True, exist_ok=True)

    result = extract(bundles)
    (output / "inventory.json").write_text(
        json.dumps(
            {
                "inputs": result.inputs,
                "services": result.services,
                "messages": result.messages,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (output / "inventory.proto").write_text(render_proto_inventory(result), encoding="utf-8")
    print(f"Wrote {len(result.services)} services and {len(result.messages)} message names to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
