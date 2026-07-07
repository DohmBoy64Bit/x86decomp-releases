"""Provide the installed test-suite implementation for the `x86decomp_testkit.timeutil` module."""
from __future__ import annotations

from datetime import datetime, timezone


def utc_now() -> str:
    """Execute the utc now operation for the current toolkit workflow."""
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
