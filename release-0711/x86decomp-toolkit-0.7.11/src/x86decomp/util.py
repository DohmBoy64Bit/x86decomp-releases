"""Compatibility utilities backed by the toolkit's canonical contract primitives.

New code should import deterministic hashing, JSON, time, path, and atomic-write
helpers from :mod:`x86decomp.contracts`.  This module preserves the original
public signatures while delegating those operations to one implementation.
"""
from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path
from typing import Any

from .contracts import (
    atomic_write_bytes as _atomic_write_bytes,
    atomic_write_json,
    canonical_json,
    read_json,
    resolve_within,
    sha256_bytes as _sha256_bytes,
    sha256_file as _sha256_file,
    utc_now as _utc_now,
)
from .errors import ContractError


def utc_now() -> str:
    """Return the current UTC timestamp through the canonical contract helper."""
    return _utc_now()


def sha256_bytes(data: bytes) -> str:
    """Return the SHA-256 digest of ``data`` through the canonical helper."""
    return _sha256_bytes(data)


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Return the SHA-256 digest of ``path`` using ``chunk_size`` byte reads."""
    return _sha256_file(path, chunk_size=chunk_size)


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize ``value`` to deterministic UTF-8 JSON bytes."""
    return canonical_json(value).encode("utf-8")


def load_json(path: Path) -> Any:
    """Read and decode the JSON document at ``path``."""
    return read_json(path)


def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Atomically write ``data`` with consistent user-readable permissions."""
    _atomic_write_bytes(path, data)


def atomic_write_text(path: Path, text: str) -> None:
    """Atomically write UTF-8 ``text`` to ``path``."""
    _atomic_write_bytes(path, text.encode("utf-8"))


def write_json(path: Path, value: Any) -> None:
    """Atomically write indented, sorted UTF-8 JSON with a trailing newline."""
    atomic_write_json(path, value)


def copy_file_atomic(source: Path, destination: Path) -> None:
    """Copy ``source`` to ``destination`` atomically while preserving metadata."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent)
    os.close(fd)
    try:
        shutil.copy2(source, temp_name)
        Path(temp_name).replace(destination)
    finally:
        Path(temp_name).unlink(missing_ok=True)


def ensure_relative_path(root: Path, candidate: Path) -> Path:
    """Resolve ``candidate`` and reject any path that escapes ``root``."""
    return resolve_within(root, candidate)


def require_mapping(value: Any, name: str) -> dict[str, Any]:
    """Return ``value`` as a JSON object or raise ``ContractError``."""
    if not isinstance(value, dict):
        raise ContractError(f"{name} must be a JSON object")
    return value


def require_string(mapping: dict[str, Any], key: str, *, nonempty: bool = True) -> str:
    """Return a required string field, optionally rejecting blank values."""
    value = mapping.get(key)
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ContractError(f"{key} must be a{' non-empty' if nonempty else ''} string")
    return value


def require_int(mapping: dict[str, Any], key: str, *, minimum: int | None = None) -> int:
    """Return a required integer field after type and lower-bound validation."""
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ContractError(f"{key} must be an integer")
    if minimum is not None and value < minimum:
        raise ContractError(f"{key} must be >= {minimum}")
    return value
