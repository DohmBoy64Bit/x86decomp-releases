"""Small, dependency-free utilities shared by all modules."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .errors import ContractError


def utc_now() -> str:
    """Return a stable RFC 3339 UTC timestamp."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    """Execute the sha256 bytes operation for the current toolkit workflow."""
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Execute the sha256 file operation for the current toolkit workflow."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    """Execute the canonical json bytes operation for the current toolkit workflow."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def load_json(path: Path) -> Any:
    """Load and parse JSON content from a filesystem path."""
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Execute the atomic write bytes operation for the current toolkit workflow."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass


def atomic_write_text(path: Path, text: str) -> None:
    """Execute the atomic write text operation for the current toolkit workflow."""
    atomic_write_bytes(path, text.encode("utf-8"))


def write_json(path: Path, value: Any) -> None:
    """Write json for the current toolkit workflow."""
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_text(path, payload)


def copy_file_atomic(source: Path, destination: Path) -> None:
    """Execute the copy file atomic operation for the current toolkit workflow."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent)
    os.close(fd)
    try:
        shutil.copy2(source, temp_name)
        os.replace(temp_name, destination)
    finally:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass


def ensure_relative_path(root: Path, candidate: Path) -> Path:
    """Resolve candidate and reject paths that escape root."""
    root_resolved = root.resolve()
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise ContractError(f"path escapes project root: {candidate}") from exc
    return resolved


def require_mapping(value: Any, name: str) -> dict[str, Any]:
    """Execute the require mapping operation for the current toolkit workflow."""
    if not isinstance(value, dict):
        raise ContractError(f"{name} must be a JSON object")
    return value


def require_string(mapping: dict[str, Any], key: str, *, nonempty: bool = True) -> str:
    """Execute the require string operation for the current toolkit workflow."""
    value = mapping.get(key)
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ContractError(f"{key} must be a{' non-empty' if nonempty else ''} string")
    return value


def require_int(mapping: dict[str, Any], key: str, *, minimum: int | None = None) -> int:
    """Execute the require int operation for the current toolkit workflow."""
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ContractError(f"{key} must be an integer")
    if minimum is not None and value < minimum:
        raise ContractError(f"{key} must be >= {minimum}")
    return value
