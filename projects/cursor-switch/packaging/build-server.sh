#!/usr/bin/env bash
# Build the frozen control-plane sidecar into packaging/dist/cursor-switch-server/
# Freezes from a neutral /tmp tree so the binary does not embed developer home paths.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_ROOT="${CURSOR_SWITCH_BUILD_ROOT:-/tmp/cursor-switch-build}"
SRC="$BUILD_ROOT/src"
OUT="$ROOT/packaging/dist/cursor-switch-server"
# Capture the developer home prefix before we override HOME for the freeze.
DEVELOPER_HOME_PREFIX="$(printf '%s\n' "$ROOT" | sed -E 's#^(/Users/[^/]+|/home/[^/]+).*#\1#')"

path_is_neutral() {
  case "$1" in
    */Users/*|*/home/*) return 1 ;;
    *) return 0 ;;
  esac
}

micromamba_url() {
  local arch
  arch="$(uname -m)"
  case "$(uname -s)-${arch}" in
    Darwin-arm64) echo "https://micro.mamba.pm/api/micromamba/osx-arm64/latest" ;;
    Darwin-x86_64) echo "https://micro.mamba.pm/api/micromamba/osx-64/latest" ;;
    Linux-x86_64) echo "https://micro.mamba.pm/api/micromamba/linux-64/latest" ;;
    Linux-aarch64) echo "https://micro.mamba.pm/api/micromamba/linux-aarch64/latest" ;;
    *)
      echo "Unsupported platform for micromamba bootstrap: $(uname -s) $(uname -m)" >&2
      exit 1
      ;;
  esac
}

bootstrap_python() {
  if [[ -n "${CURSOR_SWITCH_BUILD_PYTHON:-}" ]]; then
    if ! path_is_neutral "${CURSOR_SWITCH_BUILD_PYTHON}"; then
      echo "CURSOR_SWITCH_BUILD_PYTHON must not live under a user home path." >&2
      exit 1
    fi
    echo "${CURSOR_SWITCH_BUILD_PYTHON}"
    return
  fi

  local mamba_bin="$BUILD_ROOT/bin/micromamba"
  local env_prefix="$BUILD_ROOT/env"
  mkdir -p "$BUILD_ROOT/bin"
  echo "Bootstrapping isolated Python under $BUILD_ROOT via micromamba..." >&2
  curl -fsSL "$(micromamba_url)" | tar -xvj -C "$BUILD_ROOT/bin" --strip-components=1 bin/micromamba >/dev/null
  export MAMBA_ROOT_PREFIX="$BUILD_ROOT/mamba"
  "$mamba_bin" create -y -p "$env_prefix" "python=3.12" pip >/dev/null
  echo "$env_prefix/bin/python"
}

echo "Build root: $BUILD_ROOT"
rm -rf "$BUILD_ROOT"
mkdir -p "$SRC"

rsync -a \
  --exclude '.git/' \
  --exclude '.venv/' \
  --exclude 'apps/desktop/node_modules/' \
  --exclude 'apps/desktop/dist/' \
  --exclude 'apps/desktop/release/' \
  --exclude 'packaging/build/' \
  --exclude 'packaging/dist/' \
  --exclude '__pycache__/' \
  --exclude '.pytest_cache/' \
  --exclude '*.db' \
  "$ROOT/" "$SRC/"

export HOME="$BUILD_ROOT/home"
export USER="builder"
export LOGNAME="builder"
export PYTHONNOUSERSITE=1
unset PYTHONPATH || true
mkdir -p "$HOME"

BUILD_PYTHON="$(bootstrap_python)"
echo "Build python: $BUILD_PYTHON"
if ! path_is_neutral "$BUILD_PYTHON"; then
  echo "ERROR: build python path is not neutral: $BUILD_PYTHON" >&2
  exit 1
fi

"$BUILD_PYTHON" -m pip install -U pip
"$BUILD_PYTHON" -m pip install -e "$SRC"
"$BUILD_PYTHON" -m pip install "pyinstaller>=6.11"

ACTIVE_PREFIX="$("$BUILD_PYTHON" -c 'import sys; print(sys.prefix)')"
LIBDIR="$("$BUILD_PYTHON" -c 'import sysconfig; print(sysconfig.get_config_var("LIBDIR") or "")')"
if ! path_is_neutral "$ACTIVE_PREFIX"; then
  echo "ERROR: python prefix is not neutral: $ACTIVE_PREFIX" >&2
  exit 1
fi
if [[ -n "$LIBDIR" ]] && ! path_is_neutral "$LIBDIR"; then
  echo "ERROR: python LIBDIR is not neutral: $LIBDIR" >&2
  exit 1
fi

rm -rf "$SRC/packaging/build" "$SRC/packaging/dist"
cd "$SRC"
PYTHONPATH=server "$BUILD_PYTHON" -m PyInstaller \
  --noconfirm \
  --clean \
  --distpath packaging/dist \
  --workpath packaging/build \
  packaging/cursor-switch-server.spec

rm -rf "$ROOT/packaging/build" "$ROOT/packaging/dist"
mkdir -p "$ROOT/packaging/dist"
cp -R "$SRC/packaging/dist/cursor-switch-server" "$ROOT/packaging/dist/"

# Only reject THIS developer's home path (e.g. /Users/sk). Upstream libs may
# contain unrelated example/CI paths such as /Users/runner or C:/Users/Barney.
if [[ "$DEVELOPER_HOME_PREFIX" == /Users/* || "$DEVELOPER_HOME_PREFIX" == /home/* ]]; then
  if command -v rg >/dev/null 2>&1; then
    if rg -a -F -n --no-filename "$DEVELOPER_HOME_PREFIX" "$OUT" >/tmp/cursor-switch-path-leak.txt 2>/dev/null; then
      echo "ERROR: packaged sidecar embeds developer home path $DEVELOPER_HOME_PREFIX:" >&2
      head -50 /tmp/cursor-switch-path-leak.txt >&2
      exit 1
    fi
  else
    if grep -R -a -F "$DEVELOPER_HOME_PREFIX" "$OUT" >/tmp/cursor-switch-path-leak.txt 2>/dev/null; then
      echo "ERROR: packaged sidecar embeds developer home path $DEVELOPER_HOME_PREFIX:" >&2
      head -50 /tmp/cursor-switch-path-leak.txt >&2
      exit 1
    fi
  fi
fi

echo "Built: $OUT"
