"""Safe, static-only ingestion and analysis of user-supplied test bundles.

A test bundle is a ZIP archive containing an explicit ``x86decomp-test-bundle.json``
manifest.  The default runner never executes any supplied binary or build script.
It performs integrity verification and invokes the toolkit's bounded static parsers.

This module is intentionally strict because ZIP archives and native binaries are
untrusted input even when the user has authorization to analyze them.
"""

from __future__ import annotations

import json
import os
import stat
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from .coff import parse_coff, resolve_comdats
from .coff_archive import parse_coff_archive
from .errors import ContractError, FormatError, VerificationError
from .image_match import compare_whole_images
from .linker_layout import parse_msvc_map, reconstruct_linker_layout
from .msvc_metadata import analyze_msvc_metadata
from .pe import parse_pe
from .pdb import parse_pdb
from .util import load_json, sha256_file, utc_now, write_json

MANIFEST_NAME = "x86decomp-test-bundle.json"
_ALLOWED_ROLES = {
    "primary_image",
    "reference_image",
    "candidate_image",
    "pdb",
    "linker_map",
    "coff_object",
    "static_library",
    "source",
    "compiler_profile",
    "image_profile",
    "documentation",
}


@dataclass(frozen=True)
class BundleLimits:
    """Store validated bundle limits fields used by toolkit reports and adapters."""
    max_files: int = 4096
    max_member_bytes: int = 512 * 1024 * 1024
    max_total_bytes: int = 2 * 1024 * 1024 * 1024
    max_compression_ratio: int = 200


def _safe_member_path(name: str) -> PurePosixPath:
    """Support safe member path processing for internal toolkit callers."""
    if "\\" in name:
        raise ContractError(f"ZIP member uses a backslash path separator: {name!r}")
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts:
        raise ContractError(f"unsafe ZIP member path: {name!r}")
    if any(part in ("", ".", "..") for part in path.parts):
        raise ContractError(f"unsafe ZIP member path: {name!r}")
    if ":" in path.parts[0]:
        raise ContractError(f"drive-qualified ZIP member path is forbidden: {name!r}")
    return path


def _is_symlink(info: zipfile.ZipInfo) -> bool:
    """Support is symlink processing for internal toolkit callers."""
    mode = (info.external_attr >> 16) & 0xFFFF
    return stat.S_ISLNK(mode)


def _validate_archive_infos(infos: list[zipfile.ZipInfo], limits: BundleLimits) -> None:
    """Support validate archive infos processing for internal toolkit callers."""
    if len(infos) > limits.max_files:
        raise ContractError(f"bundle has {len(infos)} members; maximum is {limits.max_files}")
    total = 0
    seen: set[str] = set()
    for info in infos:
        path = _safe_member_path(info.filename)
        normalized = path.as_posix()
        if normalized in seen:
            raise ContractError(f"duplicate ZIP member: {normalized}")
        seen.add(normalized)
        if _is_symlink(info):
            raise ContractError(f"symlink ZIP member is forbidden: {normalized}")
        if info.is_dir():
            continue
        if info.file_size > limits.max_member_bytes:
            raise ContractError(f"ZIP member exceeds size limit: {normalized}")
        total += info.file_size
        if total > limits.max_total_bytes:
            raise ContractError("bundle exceeds total uncompressed size limit")
        if info.compress_size == 0:
            if info.file_size > 0:
                raise ContractError(f"invalid zero compressed size for non-empty member: {normalized}")
        elif info.file_size / info.compress_size > limits.max_compression_ratio:
            raise ContractError(f"ZIP member exceeds compression-ratio limit: {normalized}")
    if MANIFEST_NAME not in seen:
        raise ContractError(f"bundle is missing required root manifest {MANIFEST_NAME}")


def _extract_safely(archive: Path, destination: Path, limits: BundleLimits) -> None:
    """Support extract safely processing for internal toolkit callers."""
    destination.mkdir(parents=True, exist_ok=False)
    root = destination.resolve()
    with zipfile.ZipFile(archive, "r") as handle:
        infos = handle.infolist()
        _validate_archive_infos(infos, limits)
        for info in infos:
            relative = _safe_member_path(info.filename)
            output = destination.joinpath(*relative.parts)
            resolved_parent = output.parent.resolve()
            try:
                resolved_parent.relative_to(root)
            except ValueError as exc:  # defensive, in addition to PurePosixPath checks
                raise ContractError(f"ZIP member escapes extraction root: {info.filename}") from exc
            if info.is_dir():
                output.mkdir(parents=True, exist_ok=True)
                continue
            output.parent.mkdir(parents=True, exist_ok=True)
            # Stream instead of ZipFile.extract to retain explicit control.
            with handle.open(info, "r") as source, output.open("xb") as target:
                remaining = info.file_size
                while remaining:
                    chunk = source.read(min(1024 * 1024, remaining))
                    if not chunk:
                        raise FormatError(f"truncated ZIP member: {info.filename}")
                    target.write(chunk)
                    remaining -= len(chunk)
                if source.read(1):
                    raise FormatError(f"ZIP member expanded past declared size: {info.filename}")


def _manifest_artifacts(manifest: dict[str, Any], root: Path) -> list[dict[str, Any]]:
    """Support manifest artifacts processing for internal toolkit callers."""
    if manifest.get("schema_version") != 1:
        raise ContractError("test-bundle schema_version must be 1")
    authorization = manifest.get("authorization")
    if not isinstance(authorization, dict) or authorization.get("owner_or_authorized") is not True:
        raise ContractError("authorization.owner_or_authorized must be true")
    statement = authorization.get("statement")
    if not isinstance(statement, str) or not statement.strip():
        raise ContractError("authorization.statement must be a non-empty string")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ContractError("artifacts must be a non-empty array")
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    root_resolved = root.resolve()
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            raise ContractError(f"artifacts[{index}] must be an object")
        raw_path = item.get("path")
        role = item.get("role")
        if not isinstance(raw_path, str):
            raise ContractError(f"artifacts[{index}].path must be a string")
        if role not in _ALLOWED_ROLES:
            raise ContractError(f"artifacts[{index}].role is unsupported: {role!r}")
        rel = _safe_member_path(raw_path)
        normalized = rel.as_posix()
        if normalized == MANIFEST_NAME:
            raise ContractError("manifest cannot also be listed as an artifact")
        if normalized in seen:
            raise ContractError(f"duplicate artifact path: {normalized}")
        seen.add(normalized)
        path = root.joinpath(*rel.parts).resolve()
        try:
            path.relative_to(root_resolved)
        except ValueError as exc:
            raise ContractError(f"artifact path escapes bundle root: {raw_path}") from exc
        if not path.is_file() or path.is_symlink():
            raise ContractError(f"artifact is missing or is not a regular file: {raw_path}")
        actual_hash = sha256_file(path)
        expected_hash = item.get("sha256")
        if expected_hash is not None:
            if not isinstance(expected_hash, str) or len(expected_hash) != 64:
                raise ContractError(f"artifacts[{index}].sha256 must be a 64-character hex digest")
            try:
                int(expected_hash, 16)
            except ValueError as exc:
                raise ContractError(f"artifacts[{index}].sha256 is not hexadecimal") from exc
            if actual_hash != expected_hash.lower():
                raise VerificationError(f"artifact hash mismatch: {raw_path}")
        result.append({**item, "path": normalized, "resolved_path": str(path), "sha256": actual_hash})
    return result


def _single_role(artifacts: list[dict[str, Any]], role: str) -> Path | None:
    """Support single role processing for internal toolkit callers."""
    matches = [Path(item["resolved_path"]) for item in artifacts if item["role"] == role]
    if len(matches) > 1:
        raise ContractError(f"test bundle may contain at most one {role}")
    return matches[0] if matches else None


def create_test_bundle(
    output: Path,
    *,
    artifacts: list[tuple[str, Path]],
    authorization_statement: str,
    name: str | None = None,
    description: str | None = None,
    expected_architecture: str | None = None,
) -> dict[str, Any]:
    """Create a deterministic authorized static test bundle.

    Each artifact tuple is ``(role, path)``. Files are copied into the archive;
    no supplied content is executed. The archive is validated after creation.
    """
    if not authorization_statement.strip():
        raise ContractError("authorization statement must be non-empty")
    if expected_architecture not in (None, "x86", "x86_64"):
        raise ContractError("expected architecture must be x86 or x86_64")
    if not artifacts:
        raise ContractError("at least one artifact is required")
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    sources: list[tuple[Path, str]] = []
    used_names: set[str] = set()
    for index, (role, raw_path) in enumerate(artifacts):
        if role not in _ALLOWED_ROLES:
            raise ContractError(f"unsupported artifact role: {role}")
        path = raw_path.expanduser().resolve()
        if not path.is_file() or path.is_symlink():
            raise ContractError(f"artifact must be a regular non-symlink file: {path}")
        if path == output:
            raise ContractError("output archive cannot also be an input artifact")
        basename = path.name
        archive_name = f"files/{basename}"
        if archive_name in used_names:
            archive_name = f"files/{index:03d}-{role}-{basename}"
        used_names.add(archive_name)
        records.append({"path": archive_name, "role": role, "sha256": sha256_file(path)})
        sources.append((path, archive_name))
    manifest: dict[str, Any] = {
        "schema_version": 1,
        "authorization": {
            "owner_or_authorized": True,
            "statement": authorization_statement.strip(),
        },
        "artifacts": records,
    }
    if name:
        manifest["name"] = name
    if description:
        manifest["description"] = description
    if expected_architecture:
        manifest["expected_architecture"] = expected_architecture
    payload = (json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    fd, temporary_name = tempfile.mkstemp(prefix=f".{output.name}.", dir=output.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            manifest_info = zipfile.ZipInfo(MANIFEST_NAME, date_time=(1980, 1, 1, 0, 0, 0))
            manifest_info.compress_type = zipfile.ZIP_DEFLATED
            manifest_info.external_attr = 0o100644 << 16
            archive.writestr(manifest_info, payload)
            for path, archive_name in sources:
                info = zipfile.ZipInfo(archive_name, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        os.replace(temporary, output)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
    verification = inspect_test_bundle(output)
    return {
        "schema_version": 1,
        "kind": "test_bundle_creation",
        "output": str(output),
        "sha256": sha256_file(output),
        "manifest": manifest,
        "static_verification_passed": verification["passed"],
        "supplied_code_executed": False,
    }


def inspect_test_bundle(
    archive: Path,
    *,
    report_path: Path | None = None,
    limits: BundleLimits | None = None,
) -> dict[str, Any]:
    """Verify and statically inspect a test bundle without executing its contents."""

    resolved_archive = archive.resolve()
    if not resolved_archive.is_file():
        raise ContractError(f"test bundle does not exist: {resolved_archive}")
    selected_limits = limits or BundleLimits()
    with tempfile.TemporaryDirectory(prefix="x86decomp-test-bundle-") as temp:
        root = Path(temp) / "bundle"
        _extract_safely(resolved_archive, root, selected_limits)
        manifest = load_json(root / MANIFEST_NAME)
        if not isinstance(manifest, dict):
            raise ContractError("test-bundle manifest must be a JSON object")
        artifacts = _manifest_artifacts(manifest, root)

        pe_reports: list[dict[str, Any]] = []
        object_reports: list[dict[str, Any]] = []
        map_reports: list[dict[str, Any]] = []
        archive_reports: list[dict[str, Any]] = []
        errors: list[dict[str, str]] = []
        object_paths = [Path(item["resolved_path"]) for item in artifacts if item["role"] == "coff_object"]
        map_path = _single_role(artifacts, "linker_map")
        primary = _single_role(artifacts, "primary_image")
        reference = _single_role(artifacts, "reference_image")
        candidate = _single_role(artifacts, "candidate_image")
        profile = _single_role(artifacts, "image_profile")
        pdb_path = _single_role(artifacts, "pdb")

        for item in artifacts:
            path = Path(item["resolved_path"])
            role = item["role"]
            try:
                if role in {"primary_image", "reference_image", "candidate_image"}:
                    parsed = parse_pe(path)
                    metadata = analyze_msvc_metadata(
                        path,
                        object_paths=object_paths if path == (primary or reference) else (),
                        map_path=map_path if path == (primary or reference) else None,
                    )
                    pe_reports.append({"role": role, "path": item["path"], "pe": parsed.to_dict(), "msvc_metadata": metadata})
                elif role == "coff_object":
                    object_reports.append({"path": item["path"], "coff": parse_coff(path).to_dict()})
                elif role == "linker_map":
                    map_reports.append({"path": item["path"], "map": parse_msvc_map(path).to_dict()})
                elif role == "static_library":
                    archive_reports.append({"path": item["path"], "archive": parse_coff_archive(path).to_dict()})
            except Exception as exc:  # preserve per-artifact diagnostics while keeping report deterministic
                errors.append({"path": item["path"], "role": role, "error_type": type(exc).__name__, "message": str(exc)})

        pdb_reports: list[dict[str, Any]] = []
        if pdb_path is not None:
            try:
                correlated_image = primary or reference
                pdb_reports.append({
                    "path": next(item["path"] for item in artifacts if item["role"] == "pdb"),
                    "pdb": parse_pdb(pdb_path, pe_path=correlated_image).to_dict(),
                })
            except Exception as exc:
                errors.append({"path": str(pdb_path), "role": "pdb", "error_type": type(exc).__name__, "message": str(exc)})

        comdat_report: dict[str, Any] | None = None
        if object_paths:
            try:
                comdat_report = resolve_comdats([parse_coff(path) for path in object_paths]).to_dict()
            except Exception as exc:
                errors.append({"path": "<coff-set>", "role": "coff_object", "error_type": type(exc).__name__, "message": str(exc)})

        layout_report: dict[str, Any] | None = None
        layout_image = primary or reference
        if layout_image is not None and map_path is not None:
            try:
                layout_report = reconstruct_linker_layout(layout_image, map_path, object_paths=object_paths)
            except Exception as exc:
                errors.append({"path": "<layout>", "role": "linker_map", "error_type": type(exc).__name__, "message": str(exc)})

        image_match_report: dict[str, Any] | None = None
        if reference is not None and candidate is not None:
            try:
                image_match_report = compare_whole_images(reference, candidate, profile_path=profile)
            except Exception as exc:
                errors.append({"path": "<image-pair>", "role": "candidate_image", "error_type": type(exc).__name__, "message": str(exc)})

        report = {
            "schema_version": 1,
            "kind": "static_test_bundle_report",
            "created_at": utc_now(),
            "archive": {"path": str(resolved_archive), "sha256": sha256_file(resolved_archive)},
            "bundle": {
                "name": manifest.get("name"),
                "description": manifest.get("description"),
                "authorization": manifest["authorization"],
                "expected_architecture": manifest.get("expected_architecture"),
                "artifact_count": len(artifacts),
            },
            "artifacts": [
                {key: value for key, value in item.items() if key != "resolved_path"}
                for item in artifacts
            ],
            "analyses": {
                "pe_images": pe_reports,
                "coff_objects": object_reports,
                "linker_maps": map_reports,
                "coff_archives": archive_reports,
                "pdb_files": pdb_reports,
                "comdat_resolution": comdat_report,
                "linker_layout": layout_report,
                "whole_image_match": image_match_report,
            },
            "errors": errors,
            "static_analysis_only": True,
            "supplied_code_executed": False,
            "passed": not errors,
            "limitations": [
                "No native executable, DLL, object, library, source file, or script from the bundle was executed.",
                "PDB MSF/PDB/TPI/IPI/DBI inventory is bounded; complete CodeView type and symbol records are not reconstructed.",
                "A successful bounded parser report is not a malware-safety or semantic-equivalence result.",
            ],
        }
    if report_path is not None:
        write_json(report_path, report)
    return report
