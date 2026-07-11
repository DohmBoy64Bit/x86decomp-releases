"""Provide timeutil support for the standalone verification harness."""
from __future__ import annotations

from datetime import datetime, timezone


def utc_now() -> str:
    """Return the current UTC timestamp in the harness serialization format."""
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
