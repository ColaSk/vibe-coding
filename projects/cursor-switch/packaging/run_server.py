"""PyInstaller entry for the cursor-switch control plane."""

from __future__ import annotations

import multiprocessing
import sys


def main() -> None:
    # Required on Windows when frozen with PyInstaller.
    multiprocessing.freeze_support()
    from cursor_switch.control.main import main as run

    run()


if __name__ == "__main__":
    main()
