"""Target-pack inference, validation, and project-template generation.

A target pack records observed facts and user-supplied decisions separately.
Inferences never invent compiler versions, linker flags, names, or source layout.
"""

from __future__ import annotations

import json
import shutil
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .coff import parse_coff
from .coff_archive import parse_coff_archive
from .errors import ContractError, VerificationError
from .image_match import derive_layout_profile
from .linker_layout import parse_msvc_map
from .pdb import parse_pdb
from .pe import parse_pe
from .project import initialize_project
from .util import copy_file_atomic, load_json, sha256_file, utc_now, write_json

TARGET_PACK_SCHEMA_VERSION = 1


@dataclass(frozen=True)
class SupportingArtifact:
    """Store validated supporting artifact fields used by toolkit reports and adapters."""
    role: str
    path: Path
    sha256: str
    size: int

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable dictionary representation."""
        return {"role": self.role, "path": str(self.path), "sha256": self.sha256, "size": self.size}


def _toml_string(value: str) -> str:
    """Escape a string for deterministic TOML output."""
    return json.dumps(value, ensure_ascii=False)


def _write_target_toml(path: Path, pack: dict[str, Any]) -> None:
    """Write target toml."""
    lines = [
        f"schema_version = {pack['schema_version']}",
        f"target_id = {_toml_string(pack['target_id'])}",
        f"name = {_toml_string(pack['name'])}",
        f"created_at = {_toml_string(pack['created_at'])}",
        f"architecture = {_toml_string(pack['architecture'])}",
        f"image_kind = {_toml_string(pack['image_kind'])}",
        f"primary_image = {_toml_string(pack['primary_image'])}",
        f"primary_sha256 = {_toml_string(pack['primary_sha256'])}",
        f"default_modes = [{', '.join(_toml_string(item) for item in pack['default_modes'])}]",
        "",
        "[scope]",
    ]
    for key, value in pack["scope"].items():
        lines.append(f"{key} = {'true' if value is True else 'false' if value is False else _toml_string(str(value))}")
    lines.extend(["", "[decisions]"])
    for key, value in sorted(pack["decisions"].items()):
        if isinstance(value, bool):
            rendered = "true" if value else "false"
        elif isinstance(value, int):
            rendered = str(value)
        elif isinstance(value, list):
            rendered = "[" + ", ".join(_toml_string(str(item)) for item in value) + "]"
        else:
            rendered = _toml_string(str(value))
        lines.append(f"{key} = {rendered}")
    for artifact in pack["artifacts"]:
        lines.extend(
            [
                "",
                "[[artifacts]]",
                f"role = {_toml_string(artifact['role'])}",
                f"path = {_toml_string(artifact['path'])}",
                f"sha256 = {_toml_string(artifact['sha256'])}",
                f"size = {artifact['size']}",
            ]
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _safe_artifact(path: Path) -> Path:
    """Resolve an artifact path and require it to remain inside the project."""
    resolved = path.resolve()
    if not resolved.is_file() or resolved.is_symlink():
        raise ContractError(f"target-pack artifact must be a regular file: {resolved}")
    return resolved


def infer_target_pack(
    primary_image: Path,
    output_directory: Path,
    *,
    name: str | None = None,
    pdb: Path | None = None,
    linker_map: Path | None = None,
    objects: Iterable[Path] = (),
    libraries: Iterable[Path] = (),
    rebuilt_image: Path | None = None,
    decisions: dict[str, Any] | None = None,
    copy_artifacts: bool = True,
) -> dict[str, Any]:
    """Infer target pack."""
    image_path = _safe_artifact(primary_image)
    image = parse_pe(image_path)
    output = output_directory.resolve()
    if output.exists() and any(output.iterdir()):
        raise ContractError(f"target-pack output directory is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)
    artifact_dir = output / "artifacts"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    supplied: list[tuple[str, Path]] = [("primary_image", image_path)]
    if pdb is not None:
        supplied.append(("pdb", _safe_artifact(pdb)))
    if linker_map is not None:
        supplied.append(("linker_map", _safe_artifact(linker_map)))
    supplied.extend(("coff_object", _safe_artifact(path)) for path in objects)
    supplied.extend(("static_library", _safe_artifact(path)) for path in libraries)
    if rebuilt_image is not None:
        supplied.append(("rebuilt_image", _safe_artifact(rebuilt_image)))
    records: list[dict[str, Any]] = []
    used_names: set[str] = set()
    for index, (role, source) in enumerate(supplied):
        filename = source.name
        if filename in used_names:
            filename = f"{index:03d}-{filename}"
        used_names.add(filename)
        destination = artifact_dir / filename if copy_artifacts else source
        if copy_artifacts:
            copy_file_atomic(source, destination)
        records.append(
            {
                "role": role,
                "path": str(destination.relative_to(output)) if copy_artifacts else str(destination),
                "sha256": sha256_file(source),
                "size": source.stat().st_size,
            }
        )
    target_id = f"{image.to_dict()['architecture']}-{image.file_sha256[:20]}"
    explicit = decisions or {}
    permitted_decisions = {
        "preferred_mode",
        "compiler_family",
        "compiler_version",
        "linker_family",
        "source_language",
        "allow_host_execution",
        "target_description",
    }
    unknown = set(explicit) - permitted_decisions
    if unknown:
        raise ContractError(f"unknown target decisions: {sorted(unknown)}")
    normalized_decisions = {
        "preferred_mode": explicit.get("preferred_mode", "both"),
        "compiler_family": explicit.get("compiler_family", "unknown"),
        "compiler_version": explicit.get("compiler_version", "unknown"),
        "linker_family": explicit.get("linker_family", "unknown"),
        "source_language": explicit.get("source_language", "unknown"),
        "allow_host_execution": bool(explicit.get("allow_host_execution", False)),
        "target_description": explicit.get("target_description", "No target-specific description supplied."),
    }
    if normalized_decisions["preferred_mode"] not in ("matching", "functional", "both"):
        raise ContractError("preferred_mode must be matching, functional, or both")
    pack = {
        "schema_version": TARGET_PACK_SCHEMA_VERSION,
        "target_id": target_id,
        "name": name or image_path.stem,
        "created_at": utc_now(),
        "architecture": image.to_dict()["architecture"],
        "image_kind": "dll" if image.to_dict().get("characteristics", 0) & 0x2000 else "exe",
        "primary_image": records[0]["path"],
        "primary_sha256": image.file_sha256,
        "default_modes": ["matching", "functional"],
        "scope": {
            "native_windows_pe": True,
            "packed_or_virtualized_claimed": False,
            "self_modifying_code_claimed": False,
            "authorization_required": True,
        },
        "decisions": normalized_decisions,
        "artifacts": records,
    }
    _write_target_toml(output / "target.toml", pack)
    observations: dict[str, Any] = {
        "schema_version": 1,
        "target_id": target_id,
        "observations": {
            "pe": image.to_dict(),
            "pdb": None,
            "linker_map": None,
            "coff_objects": [],
            "libraries": [],
            "rebuilt_image": None,
        },
        "inference_policy": {
            "compiler_identity_inferred": False,
            "source_file_layout_inferred": False,
            "original_names_inferred": False,
            "unknown_values_preserved": True,
        },
    }
    source_language_evidence: dict[str, set[str]] = {"c": set(), "c++": set()}
    if pdb is not None:
        pdb_record = next(item for item in records if item["role"] == "pdb")
        pdb_path = output / pdb_record["path"] if copy_artifacts else Path(pdb_record["path"])
        pdb_document = parse_pdb(pdb_path, pe_path=(output / records[0]["path"] if copy_artifacts else image_path)).to_dict()
        observations["observations"]["pdb"] = pdb_document
        source_info = ((pdb_document.get("dbi") or {}).get("source_info") or {})
        for filename in source_info.get("unique_files", []):
            suffix = Path(str(filename)).suffix.lower()
            if suffix == ".c":
                source_language_evidence["c"].add(str(filename))
            elif suffix in {".cc", ".cpp", ".cxx", ".c++"}:
                source_language_evidence["c++"].add(str(filename))
    if linker_map is not None:
        map_record = next(item for item in records if item["role"] == "linker_map")
        map_path = output / map_record["path"] if copy_artifacts else Path(map_record["path"])
        observations["observations"]["linker_map"] = parse_msvc_map(map_path).to_dict()
    for record in (item for item in records if item["role"] == "coff_object"):
        path = output / record["path"] if copy_artifacts else Path(record["path"])
        obj = parse_coff(path)
        observations["observations"]["coff_objects"].append(
            {
                "path": record["path"],
                "architecture": obj.architecture,
                "section_count": len(obj.sections),
                "symbol_count": len(obj.symbols),
                "comdat_sections": [section.name for section in obj.sections if section.is_comdat],
            }
        )
    for record in (item for item in records if item["role"] == "static_library"):
        path = output / record["path"] if copy_artifacts else Path(record["path"])
        archive = parse_coff_archive(path)
        observations["observations"]["libraries"].append(
            {
                "path": record["path"],
                "member_count": len(archive.members),
                "symbol_count": len(archive.linker_symbols),
                "import_object_count": sum(1 for member in archive.members if member.kind == "import_object"),
                "coff_object_count": sum(1 for member in archive.members if member.kind == "coff_object"),
            }
        )
    if rebuilt_image is not None:
        rebuilt_record = next(item for item in records if item["role"] == "rebuilt_image")
        rebuilt_path = output / rebuilt_record["path"] if copy_artifacts else Path(rebuilt_record["path"])
        rebuilt = parse_pe(rebuilt_path).to_dict()
        observations["observations"]["rebuilt_image"] = {
            "path": rebuilt_record["path"],
            "sha256": rebuilt_record["sha256"],
            "architecture": rebuilt["architecture"],
            "same_architecture": rebuilt["architecture"] == image.to_dict()["architecture"],
        }
    observations["observations"]["source_language_candidates"] = [
        {"language": language, "evidence_files": sorted(files), "source": "pdb_dbi_source_file_extensions"}
        for language, files in sorted(source_language_evidence.items())
        if files
    ]
    write_json(output / "observations.json", observations)
    primary_stored = output / records[0]["path"] if copy_artifacts else image_path
    derive_layout_profile(primary_stored, output=output / "image-profile.json")
    write_json(
        output / "acceptance.json",
        {
            "schema_version": 1,
            "matching": {
                "minimum_state": "byte_matched",
                "whole_image_required": False,
                "normalizations_must_be_declared": True,
            },
            "functional": {
                "minimum_state": "differentially_validated",
                "integration_scenarios_required": [],
                "symbolic_bounds_must_be_recorded": True,
            },
        },
    )
    write_json(
        output / "template-plan.json",
        {
            "schema_version": 1,
            "target_id": target_id,
            "project_template": "hybrid" if normalized_decisions["preferred_mode"] == "both" else normalized_decisions["preferred_mode"],
            "required_external_adapters": sorted(
                {"ghidra", "capstone"}
                | ({"unicorn", "z3"} if normalized_decisions["preferred_mode"] in {"functional", "both"} else set())
            ),
            "optional_external_adapters": sorted(
                ({"angr", "dynamorio"} if normalized_decisions["preferred_mode"] in {"functional", "both"} else set())
                | ({"objdiff"} if normalized_decisions["preferred_mode"] in {"matching", "both"} else set())
            ),
            "facts_needing_user_confirmation": [
                key for key in ("compiler_family", "compiler_version", "linker_family", "source_language")
                if normalized_decisions[key] == "unknown"
            ],
        },
    )
    return {"target_pack": pack, "observations": observations, "output_directory": str(output)}


def load_target_pack(path: Path) -> dict[str, Any]:
    """Load target pack."""
    target_path = path.resolve()
    if target_path.is_dir():
        target_path = target_path / "target.toml"
    with target_path.open("rb") as handle:
        value = tomllib.load(handle)
    if value.get("schema_version") != TARGET_PACK_SCHEMA_VERSION:
        raise ContractError("unsupported target-pack schema_version")
    return value


def verify_target_pack(path: Path) -> dict[str, Any]:
    """Verify target pack."""
    target_path = path.resolve()
    root = target_path if target_path.is_dir() else target_path.parent
    pack = load_target_pack(target_path)
    failures: list[str] = []
    artifacts = pack.get("artifacts", [])
    if not isinstance(artifacts, list) or not artifacts:
        failures.append("target pack has no artifacts")
    else:
        for record in artifacts:
            try:
                artifact = Path(record["path"])
                if not artifact.is_absolute():
                    artifact = root / artifact
                resolved = artifact.resolve()
                if not resolved.is_file() or resolved.is_symlink():
                    failures.append(f"artifact missing or unsafe: {record.get('path')}")
                    continue
                if sha256_file(resolved) != record["sha256"]:
                    failures.append(f"artifact hash mismatch: {record.get('path')}")
                if resolved.stat().st_size != record["size"]:
                    failures.append(f"artifact size mismatch: {record.get('path')}")
            except Exception as exc:
                failures.append(f"invalid artifact record: {exc}")
    primary = next((item for item in artifacts if item.get("role") == "primary_image"), None)
    if primary is None or primary.get("sha256") != pack.get("primary_sha256"):
        failures.append("primary image record does not match primary_sha256")
    return {"valid": not failures, "target_id": pack.get("target_id"), "failures": failures, "artifact_count": len(artifacts)}


def generate_project_from_target_pack(
    target_pack: Path,
    project_root: Path,
    *,
    copy_binary: bool = True,
    overwrite_empty: bool = False,
) -> dict[str, Any]:
    """Generate project from target pack."""
    pack_root = target_pack.resolve() if target_pack.is_dir() else target_pack.resolve().parent
    verification = verify_target_pack(pack_root)
    if not verification["valid"]:
        raise VerificationError("target-pack verification failed: " + "; ".join(verification["failures"]))
    pack = load_target_pack(pack_root)
    primary_record = next(item for item in pack["artifacts"] if item["role"] == "primary_image")
    primary = Path(primary_record["path"])
    if not primary.is_absolute():
        primary = pack_root / primary
    project_root = project_root.resolve()
    if project_root.exists() and any(project_root.iterdir()):
        raise ContractError(f"project output is not empty: {project_root}")
    initialize_project(primary, project_root, copy_binary=copy_binary)
    destination = project_root / "target-pack"
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(pack_root, destination, symlinks=False)
    project_json = load_json(project_root / "project.json")
    project_json["target_pack"] = "target-pack/target.toml"
    project_json["target_id"] = pack["target_id"]
    project_json["template_kind"] = load_json(pack_root / "template-plan.json")["project_template"]
    write_json(project_root / "project.json", project_json)
    # Copy Ghidra scripts into the project so generated pipelines are self-contained.
    repository_scripts = Path(__file__).resolve().parents[2] / "ghidra_scripts"
    if repository_scripts.is_dir():
        shutil.copytree(repository_scripts, project_root / "ghidra_scripts", dirs_exist_ok=True)
    write_json(
        project_root / "config" / "target-decisions.json",
        {
            "schema_version": 1,
            "target_id": pack["target_id"],
            "decisions": pack["decisions"],
            "source": "target-pack/target.toml",
        },
    )
    from .orchestrator import create_default_pipeline
    pipeline_path = project_root / "orchestration" / "pipelines" / "default.json"
    pipeline = create_default_pipeline(project_root, pipeline_path, include_ghidra=True)
    lines = [
        f"# Target project: {pack['name']}",
        "",
        f"- Target ID: `{pack['target_id']}`",
        f"- Architecture: `{pack['architecture']}`",
        f"- Template: `{project_json['template_kind']}`",
        "- Modes: matching and functional are tracked independently.",
        "",
        "## Grounded unknowns",
        "",
    ]
    unknowns = [key for key, value in pack["decisions"].items() if value == "unknown"]
    if unknowns:
        lines.extend(f"- `{item}` is unknown and must be established by evidence." for item in unknowns)
    else:
        lines.append("- No declared decision is currently marked unknown.")
    lines.extend(
        [
            "",
            "## Start",
            "",
            "```bash",
            "x86decomp pipeline-run . orchestration/pipelines/default.json",
            "```",
            "",
        ]
    )
    (project_root / "TARGET.md").write_text("\n".join(lines), encoding="utf-8")
    from .project_template import materialize_project_template
    template = materialize_project_template(project_root)
    return {
        "project": project_json,
        "target_pack_verification": verification,
        "project_root": str(project_root),
        "pipeline": pipeline,
        "template": template,
    }
