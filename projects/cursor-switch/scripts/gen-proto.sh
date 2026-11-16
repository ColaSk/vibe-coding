#!/usr/bin/env bash
# Regenerate Python bindings from protocols/cursor/agent_v1.proto.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
OUT="$ROOT/server/cursor_switch/adapters/cursor/pb"
mkdir -p "$OUT"
PROTO_INC="$(python -c 'import grpc_tools, pathlib; print(pathlib.Path(grpc_tools.__file__).parent / "_proto")')"
python -m grpc_tools.protoc \
  -I "$ROOT/protocols/cursor" \
  -I "$PROTO_INC" \
  --python_out="$OUT" \
  --pyi_out="$OUT" \
  "$ROOT/protocols/cursor/agent_v1.proto"
echo "wrote $OUT/agent_v1_pb2.py"
