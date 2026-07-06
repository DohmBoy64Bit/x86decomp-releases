"""Shared command-line JSON parsing and output helpers.

The toolkit has several capability-specific command parsers.  This module keeps
JSON argument diagnostics and deterministic JSON emission consistent across
those CLIs without changing their public command surface.
"""
from __future__ import annotations

import json
from typing import Any

from x86decomp.contracts import ContractError


def parse_json_arg(raw: str | None, default: Any) -> Any:
    """Parse an optional JSON command argument and return a caller-supplied default.

    Raises:
        ContractError: If the provided argument is not valid JSON.
    """
    if raw is None:
        return default
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON argument: {exc}") from exc


def emit_json(value: Any) -> None:
    """Print a deterministic JSON representation of a command result.

    Dataclass-like objects are converted through their instance dictionaries;
    otherwise values are serialized directly with sorted keys and stable
    fallback string conversion for non-JSON-native values.
    """
    if hasattr(value, "__dict__"):
        value = value.__dict__
    print(json.dumps(value, indent=2, sort_keys=True, default=str))
