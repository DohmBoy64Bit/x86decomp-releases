"""Provide x86decomp.contracts functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable

_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")


class ContractError(ValueError):
    """Raised when an input violates a stable project contract."""


def utc_now() -> str:
    """Implement utc now.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    """Implement canonical json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    """Implement sha256 bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: str | Path, *, chunk_size: int = 1024 * 1024) -> str:
    """Implement sha256 file.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def stable_id(prefix: str, *parts: Any) -> str:
    """Implement stable id.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    body = "\0".join(canonical_json(part) for part in parts).encode("utf-8")
    return f"{prefix}-{sha256_bytes(body)[:20]}"


def random_id(prefix: str) -> str:
    """Implement random id.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return f"{prefix}-{uuid.uuid4().hex[:20]}"


def validate_id(value: str, *, field: str = "id") -> str:
    """Validate id.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not _ID_RE.fullmatch(value):
        raise ContractError(f"{field} must match {_ID_RE.pattern!r}")
    return value


def ensure_relative_path(value: str | Path) -> Path:
    """Ensure relative path.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    raw = str(value).replace("\\", "/")
    path = Path(raw)
    if not raw or path.is_absolute() or ".." in path.parts or re.match(r"^[A-Za-z]:", raw):
        raise ContractError(f"unsafe relative path: {value!s}")
    return path


def atomic_write_bytes(path: str | Path, data: bytes, *, mode: int = 0o644) -> None:
    """Implement atomic write bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{destination.name}.", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temp_name, mode)
        os.replace(temp_name, destination)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def atomic_write_json(path: str | Path, value: Any) -> None:
    """Implement atomic write json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    atomic_write_bytes(path, (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8"))


def read_json(path: str | Path) -> Any:
    """Read json.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    with Path(path).open("r", encoding="utf-8") as stream:
        return json.load(stream)


def dedupe_preserve(values: Iterable[str]) -> list[str]:
    """Implement dedupe preserve.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
