#!/usr/bin/env python3
"""
RAPP Bible — validate.

Runs the Bible's own test suite plus invokes any cross-validators in
mirrored specs that expose one. Currently RAPP-Network ships
`scripts/cross_validate.py`; if that file is fetched in a future sync it
will be invoked here.

Usage:
    python3 scripts/validate.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_pytest() -> int:
    print("=== Running pytest tests/ ===")
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v"],
        cwd=REPO_ROOT,
    )
    return proc.returncode


def main() -> int:
    rc = run_pytest()
    if rc != 0:
        print(f"\nFAIL: pytest exit code {rc}")
        return rc
    print("\nOK: all validators passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
