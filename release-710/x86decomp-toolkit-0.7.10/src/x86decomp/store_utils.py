"""Shared persistence helpers for SQLite-backed toolkit stores."""
from __future__ import annotations

import json
from typing import Any


def decode_json_fields(row: Any, *json_fields: str) -> dict[str, Any]:
    """Return a row dictionary with selected ``*_json`` columns decoded.

    Each named field is removed from the result and reinserted under the field
    name without a ``_json`` suffix.  ``NULL`` database values remain ``None``;
    non-null values are decoded as JSON text.
    """
    result = dict(row)
    for field in json_fields:
        if field in result:
            raw = result.pop(field)
            result[field[:-5] if field.endswith("_json") else field] = (
                None if raw is None else json.loads(raw)
            )
    return result
