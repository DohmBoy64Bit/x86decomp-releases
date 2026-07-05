"""Provide test-suite.x86decomp_testkit.timeutil functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

from datetime import datetime, timezone


def utc_now() -> str:
    """Implement utc now.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
