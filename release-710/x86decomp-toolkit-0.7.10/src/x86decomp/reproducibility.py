"""Reproducibility manifests and verification.

The report records what can be reproduced, what is missing, and why.  A missing
external tool is never treated as a successful reproduction.
"""

from __future__ import annotations

import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from .content_store import ContentStore
from .errors import ContractError
from .project import verify_project
from .project_state import check_project_state
from .target_pack import verify_target_pack
from .util import load_json, sha256_file, utc_now, write_json


def _version(executable: str) -> dict[str, Any]:
    """Support version processing for internal toolkit callers."""
    path = shutil.which(executable)
    if path is None:
        return {"available": False, "requested": executable}
    resolved = Path(path).resolve()
    attempts = ([path, "--version"], [path, "-version"], [path, "/?"])
    output = ""
    returncode: int | None = None
    for command in attempts:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=10, shell=False)
        except (OSError, subprocess.TimeoutExpired):
            continue
        returncode = proc.returncode
        output = (proc.stdout + "\n" + proc.stderr).strip()
        if output:
            break
    return {
        "available": True,
        "path": str(resolved),
        "sha256": sha256_file(resolved) if resolved.is_file() else None,
        "version_output": output[:4096],
        "version_returncode": returncode,
    }


def build_reproduction_manifest(
    project_root: Path,
    *,
    output: Path | None = None,
    required_tools: list[str] | None = None,
) -> dict[str, Any]:
    """Build reproduction manifest for the current toolkit workflow."""
    root = project_root.resolve()
    project = load_json(root / "project.json")
    binary = Path(project["binary"]["path"])
    if not binary.is_absolute():
        binary = root / binary
    files: list[dict[str, Any]] = []
    critical_paths = [
        root / "project.json",
        root / project.get("program_manifest", "analysis/program.json"),
        root / project.get("memory_ledger", "memory/events.jsonl"),
    ]
    target_pack = root / project.get("target_pack", "target-pack/target.toml")
    if target_pack.exists():
        critical_paths.extend(path for path in sorted(target_pack.parent.rglob("*")) if path.is_file() and not path.is_symlink())
    for path in critical_paths:
        if path.is_file():
            files.append(
                {
                    "path": str(path.relative_to(root)),
                    "sha256": sha256_file(path),
                    "size": path.stat().st_size,
                }
            )
    tools = required_tools or ["python", "java", "gcc", "clang", "lld-link", "objdiff-cli", "analyzeHeadless"]
    tool_records: dict[str, Any] = {}
    for tool in tools:
        command = sys.executable if tool == "python" else tool
        tool_records[tool] = _version(command)
    store_path = root / project.get("content_store", "artifacts")
    content_store = ContentStore(store_path).export_index() if store_path.exists() else None
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "project_id": project["project_id"],
        "project_schema_version": project["schema_version"],
        "toolkit_release": project.get("toolkit_release", "unknown"),
        "host": {
            "python": sys.version,
            "platform": platform.platform(),
            "implementation": platform.python_implementation(),
        },
        "binary": {
            "path": str(binary),
            "sha256": sha256_file(binary) if binary.is_file() else None,
            "expected_sha256": project["binary"]["sha256"],
        },
        "critical_files": files,
        "tools": tool_records,
        "content_store": content_store,
        "project_check": check_project_state(root).to_dict() if project.get("schema_version") == 3 else verify_project(root),
        "target_pack_check": verify_target_pack(target_pack.parent) if target_pack.exists() else None,
        "limitations": [
            "Tool availability is host-specific and missing tools remain unresolved.",
            "A matching hash proves byte identity, not semantic correctness.",
            "External tool version output is preserved verbatim and is not interpreted as provenance by itself.",
        ],
    }
    if output is not None:
        write_json(output, report)
    return report


def verify_reproduction_manifest(project_root: Path, manifest_path: Path) -> dict[str, Any]:
    """Verify reproduction manifest for the current toolkit workflow."""
    root = project_root.resolve()
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ContractError("reproduction manifest schema_version must be 1")
    failures: list[str] = []
    warnings: list[str] = []
    for record in manifest.get("critical_files", []):
        path = (root / record["path"]).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            failures.append(f"critical path escapes project: {record['path']}")
            continue
        if not path.is_file():
            failures.append(f"critical file missing: {record['path']}")
        elif sha256_file(path) != record["sha256"]:
            failures.append(f"critical file changed: {record['path']}")
    project = load_json(root / "project.json")
    binary = Path(project["binary"]["path"])
    if not binary.is_absolute():
        binary = root / binary
    if not binary.is_file() or sha256_file(binary) != manifest.get("binary", {}).get("expected_sha256"):
        failures.append("primary binary is unavailable or changed")
    for name, expected in manifest.get("tools", {}).items():
        if not expected.get("available"):
            warnings.append(f"tool was unavailable when manifest was created: {name}")
            continue
        current = _version(sys.executable if name == "python" else name)
        if not current.get("available"):
            failures.append(f"required tool is now unavailable: {name}")
        elif expected.get("sha256") and current.get("sha256") != expected.get("sha256"):
            failures.append(f"tool executable changed: {name}")
    return {
        "reproducible": not failures,
        "failures": failures,
        "warnings": warnings,
        "checked_at": utc_now(),
        "manifest": str(manifest_path.resolve()),
    }
