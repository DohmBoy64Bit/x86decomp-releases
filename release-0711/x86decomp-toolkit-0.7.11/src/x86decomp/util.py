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
    """Return the hex-encoded SHA-256 digest of a byte string.

    Args:
        data: The bytes to hash.

    Returns:
        The lowercase hexadecimal SHA-256 digest.
    """
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Return the hex-encoded SHA-256 digest of a file, read in chunks.

    Args:
        path: Path to the file to hash.
        chunk_size: Number of bytes read per iteration (default 1 MiB).

    Returns:
        The lowercase hexadecimal SHA-256 digest of the file contents.
    """
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize a value to canonical, deterministic JSON bytes.

    Keys are sorted and the tightest separators are used so the output is stable across
    runs, suitable for hashing.

    Args:
        value: Any JSON-serializable value.

    Returns:
        The UTF-8 encoded canonical JSON representation.
    """
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def load_json(path: Path) -> Any:
    """Load and parse JSON content from a filesystem path."""
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Write bytes to a path atomically via a temp file, fsync, and rename.

    Creates parent directories as needed and replaces any existing file only after the
    data is fully flushed and fsynced, so readers never observe a partial write.

    Args:
        path: Destination file path.
        data: Bytes to write.
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
    """Write UTF-8 text to a path atomically.

    Args:
        path: Destination file path.
        text: Text to encode as UTF-8 and write.
    """
    atomic_write_bytes(path, text.encode("utf-8"))


def write_json(path: Path, value: Any) -> None:
    """Serialize a value to indented, sorted JSON and write it atomically.

    A trailing newline is appended to the two-space-indented, key-sorted output.

    Args:
        path: Destination file path.
        value: Any JSON-serializable value.
    """
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_text(path, payload)


def copy_file_atomic(source: Path, destination: Path) -> None:
    """Copy a file to a destination atomically, preserving metadata.

    Copies into a temp file in the destination directory (via ``shutil.copy2``) and then
    renames it into place, creating parent directories as needed.

    Args:
        source: Path to the file to copy.
        destination: Path the file is copied to.
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
    """Assert that a value is a JSON object and return it.

    Args:
        value: The value to validate.
        name: Field name used in the error message.

    Returns:
        The value, typed as a ``dict``.

    Raises:
        ContractError: If ``value`` is not a ``dict``.
    """
    if not isinstance(value, dict):
        raise ContractError(f"{name} must be a JSON object")
    return value


def require_string(mapping: dict[str, Any], key: str, *, nonempty: bool = True) -> str:
    """Return a required string field from a mapping, validating its type.

    Args:
        mapping: The mapping to read from.
        key: The key to look up.
        nonempty: If True (default), reject strings that are empty or whitespace-only.

    Returns:
        The string value at ``key``.

    Raises:
        ContractError: If the value is missing, not a string, or empty when
            ``nonempty`` is set.
    """
    value = mapping.get(key)
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ContractError(f"{key} must be a{' non-empty' if nonempty else ''} string")
    return value


def require_int(mapping: dict[str, Any], key: str, *, minimum: int | None = None) -> int:
    """Return a required integer field from a mapping, validating its type and bound.

    Booleans are rejected even though they are ``int`` subclasses.

    Args:
        mapping: The mapping to read from.
        key: The key to look up.
        minimum: Optional inclusive lower bound the value must satisfy.

    Returns:
        The integer value at ``key``.

    Raises:
        ContractError: If the value is missing, not an ``int`` (or is a ``bool``), or is
            below ``minimum``.
    """
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ContractError(f"{key} must be an integer")
    if minimum is not None and value < minimum:
        raise ContractError(f"{key} must be >= {minimum}")
    return value
