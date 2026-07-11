#!/usr/bin/env python3
"""Generate or verify deterministic SHA-256 manifests for the current source tree."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

ALL_FILE_MANIFEST_NAME = "ALL_FILE_MANIFEST_0.7.11.json"
IGNORED_DIRECTORY_NAMES = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    ".x86decomp-test-tools",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "test-results",
    "tools",
    "venv",
}
IGNORED_FILE_NAMES = {".coverage", ALL_FILE_MANIFEST_NAME, "MANIFEST.sha256", "PKG-INFO"}
ALL_FILE_IGNORED_NAMES = {".coverage", ALL_FILE_MANIFEST_NAME, "PKG-INFO"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}


def _has_ignored_directory(relative: Path) -> bool:
    """Return whether a relative path traverses a transient directory."""
    return any(
        part in IGNORED_DIRECTORY_NAMES or part.endswith(".egg-info")
        for part in relative.parts[:-1]
    )


def _is_ignored(relative: Path) -> bool:
    """Return whether a path is excluded from a source-specific manifest."""
    if _has_ignored_directory(relative):
        return True
    return relative.name in IGNORED_FILE_NAMES or relative.suffix in IGNORED_SUFFIXES


def _is_all_file_ignored(relative: Path) -> bool:
    """Return whether a path is transient or is the self-excluded all-file manifest."""
    if _has_ignored_directory(relative):
        return True
    return relative.name in ALL_FILE_IGNORED_NAMES or relative.suffix in IGNORED_SUFFIXES


def source_files(root: Path) -> tuple[Path, ...]:
    """Return the exact deterministic file inventory covered by a source manifest."""
    root = root.resolve()
    return tuple(
        path
        for path in sorted(root.rglob("*"))
        if path.is_file() and not path.is_symlink() and not _is_ignored(path.relative_to(root))
    )


def all_release_files(root: Path) -> tuple[Path, ...]:
    """Return every non-transient release file except the all-file manifest itself."""
    root = root.resolve()
    return tuple(
        path
        for path in sorted(root.rglob("*"))
        if path.is_file()
        and not path.is_symlink()
        and not _is_all_file_ignored(path.relative_to(root))
    )


def _digest(path: Path) -> str:
    """Calculate a file's SHA-256 digest without loading it all into memory."""
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def manifest_text(root: Path) -> str:
    """Render a deterministic sha256sum-compatible source manifest."""
    root = root.resolve()
    return "".join(
        f"{_digest(path)}  {path.relative_to(root).as_posix()}\n"
        for path in source_files(root)
    )


def write_manifest(root: Path) -> Path:
    """Write the source-specific SHA-256 manifest for a tree."""
    root = root.resolve()
    manifest = root / "MANIFEST.sha256"
    manifest.write_text(manifest_text(root), encoding="utf-8", newline="\n")
    return manifest


def _release_version(root: Path) -> str:
    """Read the release version from pyproject.toml when one is available."""
    pyproject = root / "pyproject.toml"
    if not pyproject.is_file():
        return "unknown"
    try:
        import tomllib

        payload = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        return str(payload.get("project", {}).get("version", "unknown"))
    except (OSError, ValueError):
        return "unknown"


def all_file_payload(root: Path) -> dict[str, Any]:
    """Build the deterministic all-release-file manifest payload."""
    root = root.resolve()
    files = all_release_files(root)
    return {
        "schema_version": 1,
        "release": _release_version(root),
        "scope": (
            "all non-transient release files except this manifest; "
            "includes source MANIFEST.sha256 files"
        ),
        "file_count": len(files),
        "files": [
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": _digest(path),
            }
            for path in files
        ],
    }


def write_all_file_manifest(root: Path) -> Path:
    """Write the self-excluding JSON manifest for every release file."""
    root = root.resolve()
    manifest = root / ALL_FILE_MANIFEST_NAME
    manifest.write_text(
        json.dumps(all_file_payload(root), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def _read_manifest(manifest: Path) -> tuple[dict[str, str], list[str]]:
    """Parse a sha256sum-compatible manifest and collect structural failures."""
    entries: dict[str, str] = {}
    failures: list[str] = []
    for line_number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        digest, separator, relative = line.partition("  ")
        if not separator or len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            failures.append(f"invalid line {line_number}: {line}")
            continue
        if not relative or relative in entries:
            failures.append(f"invalid or duplicate path on line {line_number}: {relative}")
            continue
        entries[relative] = digest
    return entries, failures


def verify_manifest(root: Path) -> dict[str, Any]:
    """Verify exact inventory and hashes for one source-specific manifest."""
    root = root.resolve()
    manifest = root / "MANIFEST.sha256"
    if not manifest.is_file():
        return {"valid": False, "checked": 0, "failures": ["MANIFEST.sha256 is missing"]}
    entries, failures = _read_manifest(manifest)
    expected = {path.relative_to(root).as_posix(): path for path in source_files(root)}
    missing_entries = sorted(set(expected) - set(entries))
    stale_entries = sorted(set(entries) - set(expected))
    failures.extend(f"unlisted source file: {relative}" for relative in missing_entries)
    failures.extend(f"stale manifest entry: {relative}" for relative in stale_entries)
    for relative in sorted(set(entries) & set(expected)):
        actual = _digest(expected[relative])
        if actual != entries[relative]:
            failures.append(f"hash mismatch: {relative}")
    return {
        "valid": not failures,
        "checked": len(set(entries) & set(expected)),
        "expected": len(expected),
        "failures": failures,
    }


def verify_all_file_manifest(root: Path) -> dict[str, Any]:
    """Verify the exact inventory, sizes, and hashes in the all-file JSON manifest."""
    root = root.resolve()
    manifest = root / ALL_FILE_MANIFEST_NAME
    if not manifest.is_file():
        return {"valid": False, "checked": 0, "failures": [f"{ALL_FILE_MANIFEST_NAME} is missing"]}
    failures: list[str] = []
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"valid": False, "checked": 0, "failures": [f"invalid JSON manifest: {exc}"]}
    raw_entries = payload.get("files")
    if not isinstance(raw_entries, list):
        return {"valid": False, "checked": 0, "failures": ["files must be a list"]}
    entries: dict[str, tuple[int, str]] = {}
    for index, entry in enumerate(raw_entries):
        if not isinstance(entry, dict):
            failures.append(f"invalid entry {index}: expected object")
            continue
        relative = entry.get("path")
        size = entry.get("bytes")
        digest = entry.get("sha256")
        if not isinstance(relative, str) or not relative or relative in entries:
            failures.append(f"invalid or duplicate path at entry {index}: {relative!r}")
            continue
        if not isinstance(size, int) or size < 0:
            failures.append(f"invalid byte count for {relative}")
            continue
        if not isinstance(digest, str) or len(digest) != 64 or any(
            char not in "0123456789abcdef" for char in digest
        ):
            failures.append(f"invalid SHA-256 for {relative}")
            continue
        entries[relative] = (size, digest)
    expected = {path.relative_to(root).as_posix(): path for path in all_release_files(root)}
    failures.extend(f"unlisted release file: {relative}" for relative in sorted(set(expected) - set(entries)))
    failures.extend(f"stale all-file entry: {relative}" for relative in sorted(set(entries) - set(expected)))
    for relative in sorted(set(entries) & set(expected)):
        path = expected[relative]
        expected_size, expected_digest = entries[relative]
        if path.stat().st_size != expected_size:
            failures.append(f"size mismatch: {relative}")
        if _digest(path) != expected_digest:
            failures.append(f"hash mismatch: {relative}")
    if payload.get("file_count") != len(raw_entries):
        failures.append("file_count does not match the number of entries")
    return {
        "valid": not failures,
        "checked": len(set(entries) & set(expected)),
        "expected": len(expected),
        "failures": failures,
    }


def generate_all(root: Path) -> dict[str, str]:
    """Generate suite, root, and all-release-file manifests in dependency order."""
    root = root.resolve()
    suite_root = root / "test-suite"
    if not suite_root.is_dir():
        raise FileNotFoundError(f"test-suite directory is missing: {suite_root}")
    suite_manifest = write_manifest(suite_root)
    root_manifest = write_manifest(root)
    all_file_manifest = write_all_file_manifest(root)
    return {
        "root": str(root_manifest),
        "test_suite": str(suite_manifest),
        "all_files": str(all_file_manifest),
    }


def verify_all(root: Path) -> dict[str, Any]:
    """Verify every deterministic source and all-release-file manifest."""
    root = root.resolve()
    result = {
        "root": verify_manifest(root),
        "test_suite": verify_manifest(root / "test-suite"),
        "all_files": verify_all_file_manifest(root),
    }
    result["valid"] = bool(
        result["root"]["valid"]
        and result["test_suite"]["valid"]
        and result["all_files"]["valid"]
    )
    return result


def main(argv: Iterable[str] | None = None) -> int:
    """Run the command-line entry point and return its process status."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("generate", "verify"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        payload: dict[str, Any]
        if args.action == "generate":
            payload = {"generated": generate_all(args.root), "verification": verify_all(args.root)}
        else:
            payload = verify_all(args.root)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("valid", payload.get("verification", {}).get("valid", False)) else 2


if __name__ == "__main__":
    raise SystemExit(main())
