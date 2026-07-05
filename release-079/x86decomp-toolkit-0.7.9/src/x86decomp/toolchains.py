"""User-owned compiler toolchain registry; proprietary binaries are never copied."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .errors import ContractError
from .util import load_json, sha256_file, utc_now, write_json


def register_toolchain(
    registry_path: Path,
    *,
    toolchain_id: str,
    family: str,
    version: str,
    executables: dict[str, Path],
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Register toolchain.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not toolchain_id or not family or not version:
        raise ContractError("toolchain id, family, and version are required")
    registry = load_json(registry_path) if registry_path.is_file() else {"schema_version": 1, "toolchains": {}}
    if not isinstance(registry, dict) or not isinstance(registry.get("toolchains"), dict):
        raise ContractError("invalid toolchain registry")
    records: dict[str, Any] = {}
    for role, path in executables.items():
        resolved = path.expanduser().resolve()
        if not resolved.is_file():
            raise ContractError(f"toolchain executable is missing: {resolved}")
        records[role] = {"path": str(resolved), "sha256": sha256_file(resolved), "size": resolved.stat().st_size}
    entry = {
        "id": toolchain_id,
        "family": family,
        "version": version,
        "registered_at": utc_now(),
        "ownership": "user_supplied_external_reference",
        "executables": records,
        "metadata": metadata or {},
    }
    registry["toolchains"][toolchain_id] = entry
    write_json(registry_path, registry)
    return entry


def verify_toolchain(registry_path: Path, toolchain_id: str) -> dict[str, Any]:
    """Verify toolchain.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    registry = load_json(registry_path)
    entry = registry.get("toolchains", {}).get(toolchain_id)
    if not isinstance(entry, dict):
        raise ContractError(f"toolchain is not registered: {toolchain_id}")
    failures: list[str] = []
    for role, record in entry.get("executables", {}).items():
        path = Path(record["path"])
        if not path.is_file():
            failures.append(f"{role}: missing {path}")
        elif sha256_file(path) != record.get("sha256"):
            failures.append(f"{role}: hash changed")
    return {"toolchain_id": toolchain_id, "valid": not failures, "failures": failures}
