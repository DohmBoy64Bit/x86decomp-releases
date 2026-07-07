"""Project initialization, architecture dispatch, and integrity verification."""

from __future__ import annotations

import platform
import sys
import uuid
from pathlib import Path
from typing import Any

from .analysis_db import AnalysisDatabase
from .errors import ContractError, VerificationError
from .memory import ProjectMemory
from .pe import parse_pe
from .util import copy_file_atomic, load_json, sha256_file, utc_now, write_json
from .work_queue import WorkQueue

PROJECT_SCHEMA_VERSION = 3

PROJECT_DIRS = (
    "analysis/ghidra",
    "artifacts",
    "orchestration/pipelines",
    "orchestration/logs",
    "orchestration/work",
    "state",
    "target-pack",
    "templates",
    "analysis/exports",
    "analysis/mcp-transactions",
    "analysis/database",
    "build/compiler",
    "build/candidates",
    "build/cache",
    "build/patches",
    "build/relink",
    "config/compiler-profiles",
    "config/toolchains",
    "config/harnesses",
    "evidence/items",
    "evidence/claims",
    "evidence/files",
    "functions",
    "memory",
    "original/resources",
    "reports/matching",
    "reports/functional",
    "reports/benchmarks",
    "reports/convergence",
    "reports/reproducibility",
    "reports/security",
    "src/asm",
    "src/staging",
    "src/matched",
    "src/functional",
    "tests/harnesses",
    "work",
)


def initialize_project(binary: Path, project_root: Path, *, copy_binary: bool = True) -> dict[str, Any]:
    """Initialize project for the current toolkit workflow."""
    source = binary.resolve()
    root = project_root.resolve()
    if root.exists() and any(root.iterdir()):
        raise ContractError(f"project directory is not empty: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for directory in PROJECT_DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)

    image = parse_pe(source)
    architecture = image.to_dict()["architecture"]
    binary_name = source.name
    if copy_binary:
        stored_binary = root / "original" / binary_name
        copy_file_atomic(source, stored_binary)
        source_kind = "copied"
    else:
        stored_binary = source
        source_kind = "external_reference"

    prefix = "x86d" if architecture == "x86" else "x64d"
    project_id = f"{prefix}-{image.file_sha256[:16]}-{uuid.uuid4().hex[:8]}"
    project = {
        "schema_version": PROJECT_SCHEMA_VERSION,
        "project_id": project_id,
        "created_at": utc_now(),
        "supported_scope": "native Windows PE32 x86" if architecture == "x86" else "native Windows PE32+ x86-64",
        "architecture": architecture,
        "default_modes": ["matching", "functional"],
        "binary": {
            "name": binary_name,
            "source_kind": source_kind,
            "path": str(stored_binary if source_kind == "external_reference" else stored_binary.relative_to(root)),
            "sha256": image.file_sha256,
            "size": source.stat().st_size,
        },
        "program_manifest": "analysis/program.json",
        "analysis_database": "analysis/database/analysis.sqlite3",
        "work_queue": "work/tasks.sqlite3",
        "memory_ledger": "memory/events.jsonl",
        "function_root": "functions",
        "evidence_root": "evidence",
        "project_state_database": "state/project-state.sqlite3",
        "content_store": "artifacts",
        "target_pack": "target-pack/target.toml",
        "orchestration_root": "orchestration",
        "toolkit_release": "0.7.11",
        "status": "initialized",
    }
    write_json(root / "project.json", project)
    program_manifest = image.to_dict()
    program_manifest["source_path"] = project["binary"]["path"]
    write_json(root / "analysis" / "program.json", program_manifest)
    write_json(
        root / "analysis" / "host.json",
        {
            "schema_version": 2,
            "captured_at": utc_now(),
            "python": sys.version,
            "platform": platform.platform(),
            "implementation": platform.python_implementation(),
        },
    )
    with AnalysisDatabase(root / project["analysis_database"]):
        pass
    from .project_state import ProjectStateDatabase
    from .content_store import ContentStore
    with ProjectStateDatabase(root / project["project_state_database"]):
        pass
    ContentStore(root / project["content_store"])
    queue = WorkQueue(root / project["work_queue"])
    queue.close()

    memory = ProjectMemory(root)
    memory.append(
        actor="x86decomp",
        category="project",
        summary=f"Initialized a native {architecture} PE decompilation project with matching and functional modes.",
        details={
            "project_id": project_id,
            "binary_sha256": image.file_sha256,
            "binary_name": binary_name,
            "copy_binary": copy_binary,
            "architecture": architecture,
            "default_modes": project["default_modes"],
        },
    )
    return project


def _resolve_binary_path(root: Path, project: dict[str, Any]) -> Path:
    """Support resolve binary path processing for internal toolkit callers."""
    binary = project.get("binary")
    if not isinstance(binary, dict):
        raise ContractError("project.binary must be an object")
    value = binary.get("path")
    if not isinstance(value, str) or not value:
        raise ContractError("project.binary.path must be a non-empty string")
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    return path.resolve()


def verify_project(project_root: Path) -> dict[str, Any]:
    """Verify project for the current toolkit workflow."""
    root = project_root.resolve()
    project_path = root / "project.json"
    if not project_path.is_file():
        raise ContractError(f"missing project.json: {project_path}")
    project = load_json(project_path)
    if not isinstance(project, dict):
        raise ContractError("project.json must contain an object")
    failures: list[str] = []
    if project.get("schema_version") not in (1, 2, PROJECT_SCHEMA_VERSION):
        failures.append("unsupported project schema version")
    binary_path = _resolve_binary_path(root, project)
    expected_hash = project.get("binary", {}).get("sha256")
    if not binary_path.is_file():
        failures.append(f"binary is missing: {binary_path}")
    elif sha256_file(binary_path) != expected_hash:
        failures.append("binary SHA-256 does not match project.json")

    program_path = root / str(project.get("program_manifest", "analysis/program.json"))
    if not program_path.is_file():
        failures.append(f"program manifest is missing: {program_path}")
    elif binary_path.is_file():
        try:
            current = parse_pe(binary_path).to_dict()
            recorded = load_json(program_path)
            for key in ("file_sha256", "machine", "image_base", "entry_rva", "number_of_sections", "size_of_image", "architecture"):
                if recorded.get(key) != current.get(key):
                    failures.append(f"program manifest mismatch: {key}")
        except Exception as exc:
            failures.append(f"unable to reparse binary: {exc}")

    if project.get("schema_version") in (2, PROJECT_SCHEMA_VERSION):
        for key in ("analysis_database", "work_queue"):
            value = project.get(key)
            if not isinstance(value, str) or not (root / value).is_file():
                failures.append(f"missing project component: {key}")
        modes = project.get("default_modes")
        if modes != ["matching", "functional"]:
            failures.append("default_modes must contain matching and functional")
    if project.get("schema_version") == PROJECT_SCHEMA_VERSION:
        for key in ("project_state_database",):
            value = project.get(key)
            if not isinstance(value, str) or not (root / value).is_file():
                failures.append(f"missing project component: {key}")
        store = project.get("content_store")
        if not isinstance(store, str) or not (root / store).is_dir():
            failures.append("missing project component: content_store")
    memory_result = ProjectMemory(root).verify()
    failures.extend(f"memory: {failure}" for failure in memory_result["failures"])
    return {
        "project_id": project.get("project_id"),
        "architecture": project.get("architecture", "x86"),
        "valid": not failures,
        "failures": failures,
        "binary_path": str(binary_path),
        "memory_event_count": memory_result["event_count"],
    }


def require_valid_project(project_root: Path) -> dict[str, Any]:
    """Execute the require valid project operation for the current toolkit workflow."""
    result = verify_project(project_root)
    if not result["valid"]:
        raise VerificationError("project verification failed: " + "; ".join(result["failures"]))
    return result
