#!/usr/bin/env python3
"""Generate or verify deterministic SHA-256 manifests for the current source tree."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

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
IGNORED_FILE_NAMES = {".coverage", "MANIFEST.sha256", "PKG-INFO"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}


def _is_ignored(relative: Path) -> bool:
    """Implement is ignored.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if any(part in IGNORED_DIRECTORY_NAMES or part.endswith(".egg-info") for part in relative.parts[:-1]):
        return True
    return relative.name in IGNORED_FILE_NAMES or relative.suffix in IGNORED_SUFFIXES


def source_files(root: Path) -> tuple[Path, ...]:
    """Return the exact deterministic file inventory covered by a source manifest."""
    root = root.resolve()
    return tuple(
        path
        for path in sorted(root.rglob("*"))
        if path.is_file() and not path.is_symlink() and not _is_ignored(path.relative_to(root))
    )


def _digest(path: Path) -> str:
    """Implement digest.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def manifest_text(root: Path) -> str:
    """Implement manifest text.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = root.resolve()
    return "".join(
        f"{_digest(path)}  {path.relative_to(root).as_posix()}\n"
        for path in source_files(root)
    )


def write_manifest(root: Path) -> Path:
    """Write manifest.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = root.resolve()
    manifest = root / "MANIFEST.sha256"
    manifest.write_text(manifest_text(root), encoding="utf-8", newline="\n")
    return manifest


def _read_manifest(manifest: Path) -> tuple[dict[str, str], list[str]]:
    """Read manifest.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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
    """Verify manifest.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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


def generate_all(root: Path) -> dict[str, str]:
    """Generate all.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = root.resolve()
    suite_root = root / "test-suite"
    if not suite_root.is_dir():
        raise FileNotFoundError(f"test-suite directory is missing: {suite_root}")
    suite_manifest = write_manifest(suite_root)
    root_manifest = write_manifest(root)
    return {
        "root": str(root_manifest),
        "test_suite": str(suite_manifest),
    }


def verify_all(root: Path) -> dict[str, Any]:
    """Verify all.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    root = root.resolve()
    result = {
        "root": verify_manifest(root),
        "test_suite": verify_manifest(root / "test-suite"),
    }
    result["valid"] = bool(result["root"]["valid"] and result["test_suite"]["valid"])
    return result


def main(argv: Iterable[str] | None = None) -> int:
    """Run the command-line entry point.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
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
