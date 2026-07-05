"""Provide test-suite.x86decomp_testkit.adapters functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from .catalog import adapter_catalog
from .capabilities import CapabilityResult, capabilities_from_adapters, capability_map
from .detection import detect_adapter, detect_all
from .installation import resolve_missing_adapters

__all__ = [
    "adapter_catalog",
    "CapabilityResult",
    "capabilities_from_adapters",
    "capability_map",
    "detect_adapter",
    "detect_all",
    "resolve_missing_adapters",
]
