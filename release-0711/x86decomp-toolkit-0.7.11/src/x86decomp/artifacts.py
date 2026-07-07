"""Function artifact import and validation."""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Any

from .errors import ContractError
from .util import ensure_relative_path, load_json, sha256_file, write_json

_FUNCTION_ID = re.compile(r"^pe-rva:[0-9a-fA-F]{8}$")


def function_id_from_rva(rva: int) -> str:
    """Execute the function id from rva operation for the current toolkit workflow."""
    if not 0 <= rva <= 0xFFFFFFFF:
        raise ContractError("RVA must fit in 32 bits")
    return f"pe-rva:{rva:08x}"


def validate_function_manifest(value: Any) -> dict[str, Any]:
    """Validate function manifest for the current toolkit workflow."""
    if not isinstance(value, dict):
        raise ContractError("function manifest must be an object")
    function_id = value.get("id")
    if not isinstance(function_id, str) or not _FUNCTION_ID.fullmatch(function_id):
        raise ContractError("function id must use pe-rva:XXXXXXXX")
    ranges = value.get("body_ranges")
    if not isinstance(ranges, list) or not ranges:
        raise ContractError("body_ranges must be a non-empty array")
    previous_end = -1
    for index, item in enumerate(ranges):
        if not isinstance(item, dict):
            raise ContractError(f"body_ranges[{index}] must be an object")
        start = item.get("start_rva")
        end = item.get("end_rva")
        if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end <= start:
            raise ContractError(f"body_ranges[{index}] is invalid")
        if start < previous_end:
            raise ContractError("body_ranges must be sorted and non-overlapping")
        previous_end = end
    return value


def import_function_artifact(project_root: Path, exported_dir: Path) -> Path:
    """Execute the import function artifact operation for the current toolkit workflow."""
    exported_dir = exported_dir.resolve()
    for path in exported_dir.rglob("*"):
        if path.is_symlink():
            raise ContractError(f"function artifact may not contain symlinks: {path}")
    manifest_path = exported_dir / "function.json"
    if not manifest_path.is_file():
        raise ContractError(f"missing function manifest: {manifest_path}")
    manifest = validate_function_manifest(load_json(manifest_path))
    destination = project_root.resolve() / "functions" / manifest["id"].replace(":", "_")
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(exported_dir, destination)
    recorded_files: list[dict[str, Any]] = []
    for path in sorted(destination.rglob("*")):
        if path.is_file() and path.name != "integrity.json":
            recorded_files.append(
                {
                    "path": str(path.relative_to(destination)).replace("\\", "/"),
                    "size": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    write_json(
        destination / "integrity.json",
        {"schema_version": 1, "function_id": manifest["id"], "files": recorded_files},
    )
    return destination


def verify_function_artifact(artifact_dir: Path) -> dict[str, Any]:
    """Verify function artifact for the current toolkit workflow."""
    integrity_path = artifact_dir / "integrity.json"
    if not integrity_path.is_file():
        raise ContractError("function artifact has no integrity.json")
    integrity = load_json(integrity_path)
    failures: list[str] = []
    records = integrity.get("files")
    if not isinstance(records, list):
        raise ContractError("integrity.files must be an array")
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            failures.append(f"invalid integrity record at index {index}")
            continue
        relative = record.get("path")
        expected_size = record.get("size")
        expected_hash = record.get("sha256")
        if not isinstance(relative, str) or not relative:
            failures.append(f"invalid path at integrity record {index}")
            continue
        try:
            path = ensure_relative_path(artifact_dir, artifact_dir / relative)
        except ContractError:
            failures.append(f"path escapes artifact directory: {relative}")
            continue
        if not isinstance(expected_size, int) or expected_size < 0:
            failures.append(f"invalid size for: {relative}")
        elif not isinstance(expected_hash, str) or len(expected_hash) != 64:
            failures.append(f"invalid hash for: {relative}")
        elif not path.is_file():
            failures.append(f"missing file: {relative}")
        elif path.stat().st_size != expected_size:
            failures.append(f"size changed: {relative}")
        elif sha256_file(path) != expected_hash:
            failures.append(f"hash changed: {relative}")
    return {
        "function_id": integrity.get("function_id"),
        "valid": not failures,
        "failures": failures,
    }
