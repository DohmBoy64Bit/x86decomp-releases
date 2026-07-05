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
    """Implement sha256 bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Implement sha256 file.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    """Implement canonical json bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def load_json(path: Path) -> Any:
    """Load json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Implement atomic write bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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
    """Implement atomic write text.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    atomic_write_bytes(path, text.encode("utf-8"))


def write_json(path: Path, value: Any) -> None:
    """Write json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_text(path, payload)


def copy_file_atomic(source: Path, destination: Path) -> None:
    """Copy file atomic.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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
    """Implement require mapping.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not isinstance(value, dict):
        raise ContractError(f"{name} must be a JSON object")
    return value


def require_string(mapping: dict[str, Any], key: str, *, nonempty: bool = True) -> str:
    """Implement require string.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    value = mapping.get(key)
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ContractError(f"{key} must be a{' non-empty' if nonempty else ''} string")
    return value


def require_int(mapping: dict[str, Any], key: str, *, minimum: int | None = None) -> int:
    """Implement require int.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ContractError(f"{key} must be an integer")
    if minimum is not None and value < minimum:
        raise ContractError(f"{key} must be >= {minimum}")
    return value
