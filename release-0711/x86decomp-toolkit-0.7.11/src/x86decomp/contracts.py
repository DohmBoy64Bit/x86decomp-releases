"""Foundational input-contract primitives shared across the toolkit.

Provides deterministic identifiers, canonical JSON serialization, content
hashing, path-safety validation, and atomic file writes. These helpers enforce
the stable data contracts that governance, evidence, and reconstruction records
depend on, and raise :class:`ContractError` when an input violates them.
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

from .errors import ContractError

_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")


def utc_now() -> str:
    """Return the current UTC time as an ISO-8601 string with a ``Z`` suffix.

    The value is truncated to whole seconds so timestamps embedded in records
    remain stable and comparable.
    """
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical_json(value: Any) -> str:
    """Serialize ``value`` to a canonical JSON string.

    Keys are sorted and separators are compact so that logically equal values
    always produce byte-identical output, which is required for deterministic
    hashing and identifier generation.
    """
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    """Return the lowercase hex SHA-256 digest of ``data``."""
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: str | Path, *, chunk_size: int = 1024 * 1024) -> str:
    """Return the lowercase hex SHA-256 digest of a file.

    The file is read in ``chunk_size``-byte blocks so arbitrarily large inputs
    can be hashed without loading them fully into memory.
    """
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def stable_id(prefix: str, *parts: Any) -> str:
    """Build a deterministic identifier from ``prefix`` and ``parts``.

    The parts are canonically serialized and hashed, so the same inputs always
    yield the same identifier. Useful for content-addressed records.
    """
    body = "\0".join(canonical_json(part) for part in parts).encode("utf-8")
    return f"{prefix}-{sha256_bytes(body)[:20]}"


def random_id(prefix: str) -> str:
    """Build a random, collision-resistant identifier prefixed with ``prefix``."""
    return f"{prefix}-{uuid.uuid4().hex[:20]}"


def validate_id(value: str, *, field: str = "id") -> str:
    """Validate ``value`` as a well-formed toolkit identifier.

    Args:
        value: The candidate identifier string.
        field: Field name used in the error message.

    Returns:
        The validated identifier unchanged.

    Raises:
        ContractError: If ``value`` does not match the identifier grammar.
    """
    if not _ID_RE.fullmatch(value):
        raise ContractError(f"{field} must match {_ID_RE.pattern!r}")
    return value


def ensure_relative_path(value: str | Path) -> Path:
    """Normalize ``value`` to a safe, project-relative path.

    Backslashes are normalized to forward slashes. The path is rejected if it is
    empty, absolute, drive-qualified, or contains a ``..`` component, preventing
    directory traversal outside the project root.

    Raises:
        ContractError: If the path is unsafe.
    """
    raw = str(value).replace("\\", "/")
    path = Path(raw)
    if not raw or path.is_absolute() or ".." in path.parts or re.match(r"^[A-Za-z]:", raw):
        raise ContractError(f"unsafe relative path: {value!s}")
    return path



def resolve_within(root: str | Path, candidate: str | Path) -> Path:
    """Resolve ``candidate`` and require it to remain within ``root``.

    This rooted containment primitive complements :func:`ensure_relative_path`:
    callers may supply either an absolute candidate or one relative to ``root``,
    and receive a normalized absolute path only when no traversal escapes the
    declared root.

    Raises:
        ContractError: If the resolved candidate is outside ``root``.
    """
    root_path = Path(root).resolve()
    candidate_path = Path(candidate)
    resolved = (root_path / candidate_path).resolve() if not candidate_path.is_absolute() else candidate_path.resolve()
    try:
        resolved.relative_to(root_path)
    except ValueError as exc:
        raise ContractError(f"path escapes project root: {candidate}") from exc
    return resolved

def atomic_write_bytes(path: str | Path, data: bytes, *, mode: int = 0o644) -> None:
    """Atomically write ``data`` to ``path``.

    The bytes are written to a temporary file in the destination directory,
    flushed and fsynced, and then renamed over the target so readers never
    observe a partially written file. The temporary file is removed if the
    write fails.

    Args:
        path: Destination file path.
        data: Bytes to write.
        mode: POSIX permission bits applied to the file before the rename.
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
    """Atomically write ``value`` to ``path`` as UTF-8, indented, sorted JSON."""
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_bytes(path, payload.encode("utf-8"))


def read_json(path: str | Path) -> Any:
    """Read and decode the JSON document stored at ``path``."""
    with Path(path).open("r", encoding="utf-8") as stream:
        return json.load(stream)


def dedupe_preserve(values: Iterable[str]) -> list[str]:
    """Return the values with duplicates removed, preserving first-seen order."""
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
