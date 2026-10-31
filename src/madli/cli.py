# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------

"""The command line of madli."""

import argparse
from collections.abc import Sequence

import madli


def parser() -> argparse.ArgumentParser:
    """Return the argument parser of the madli command line."""
    p = argparse.ArgumentParser(prog="madli", description="madli")
    p.add_argument("--version", action="version", version=f"%(prog)s {madli.__version__}")
    return p


def main(argv: Sequence[str] | None = None) -> int:
    """Run the madli command line and return its exit status."""
    parser().parse_args(argv)
    print("Hello from madli!")
    return 0
