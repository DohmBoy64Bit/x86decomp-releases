"""Reproducible compiler/version ground-truth corpus builder.

The corpus records source hashes, compiler hashes and versions, complete command
lines, environment policy, COFF structure, symbols, COMDAT metadata, and output
hashes.  It is designed to compare compiler generations without redistributing
proprietary toolchains: users register their own compiler executables.
"""

from __future__ import annotations

import itertools
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .coff import parse_coff
from .errors import ContractError, ExternalToolError
from .util import load_json, sha256_file, utc_now, write_json


def _resolve_executable(value: str, base: Path) -> Path:
    candidate = Path(value).expanduser()
    if not candidate.is_absolute() and candidate.parent != Path("."):
        candidate = (base / candidate).resolve()
    if candidate.is_file():
        return candidate.resolve()
    found = shutil.which(value)
    if found is None:
        raise ExternalToolError(f"compiler executable is unavailable: {value}")
    return Path(found).resolve()


def _version(executable: Path, arguments: list[str]) -> str:
    completed = subprocess.run(
        [str(executable), *arguments], capture_output=True, text=True, timeout=30, check=False
    )
    text = (completed.stdout or completed.stderr).strip()
    if completed.returncode != 0 or not text:
        raise ExternalToolError(f"failed to query compiler version: {executable}")
    return text


def _expand_flag_matrix(matrix: dict[str, Any]) -> list[tuple[str, list[str]]]:
    if not matrix:
        return [("default", [])]
    names = sorted(matrix)
    values: list[list[dict[str, Any]]] = []
    for name in names:
        entries = matrix[name]
        if not isinstance(entries, list) or not entries:
            raise ContractError(f"flag matrix {name} must be a non-empty array")
        normalized: list[dict[str, Any]] = []
        for entry in entries:
            if isinstance(entry, str):
                normalized.append({"id": entry.replace("/", "_").replace("-", ""), "args": [entry]})
            elif isinstance(entry, dict) and isinstance(entry.get("id"), str) and isinstance(entry.get("args"), list):
                normalized.append(entry)
            else:
                raise ContractError(f"invalid flag matrix entry in {name}")
        values.append(normalized)
    variants: list[tuple[str, list[str]]] = []
    for combination in itertools.product(*values):
        variant_id = "__".join(str(item["id"]) for item in combination)
        args = [str(argument) for item in combination for argument in item["args"]]
        variants.append((variant_id, args))
    return variants


def build_ground_truth_corpus(
    manifest_path: Path,
    output_directory: Path,
    *,
    report_path: Path | None = None,
) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ContractError("ground-truth manifest must be an object")
    base = manifest_path.resolve().parent
    compilers_raw = manifest.get("compilers")
    cases_raw = manifest.get("cases")
    if not isinstance(compilers_raw, list) or not compilers_raw:
        raise ContractError("ground-truth manifest requires compilers")
    if not isinstance(cases_raw, list) or not cases_raw:
        raise ContractError("ground-truth manifest requires cases")
    output_directory = output_directory.resolve()
    output_directory.mkdir(parents=True, exist_ok=True)
    compiler_records: dict[str, dict[str, Any]] = {}
    for item in compilers_raw:
        if not isinstance(item, dict):
            raise ContractError("compiler entries must be objects")
        compiler_id = str(item["id"])
        executable = _resolve_executable(str(item["executable"]), base)
        version_args = [str(value) for value in item.get("version_args", ["--version"])]
        compiler_records[compiler_id] = {
            "id": compiler_id,
            "executable": str(executable),
            "sha256": sha256_file(executable),
            "version": _version(executable, version_args),
            "base_args": [str(value) for value in item.get("base_args", [])],
            "environment": {str(k): str(v) for k, v in item.get("environment", {}).items()},
            "inherit_environment": bool(item.get("inherit_environment", True)),
        }
    build_records: list[dict[str, Any]] = []
    for case in cases_raw:
        if not isinstance(case, dict):
            raise ContractError("case entries must be objects")
        case_id = str(case["id"])
        source = (base / str(case["source"])).resolve()
        if not source.is_file():
            raise ContractError(f"ground-truth source is missing: {source}")
        compiler_ids = case.get("compilers", list(compiler_records))
        if not isinstance(compiler_ids, list) or not compiler_ids:
            raise ContractError(f"case {case_id} compilers must be a non-empty array")
        variants = _expand_flag_matrix(case.get("flag_matrix", manifest.get("flag_matrix", {})))
        case_args = [str(value) for value in case.get("arguments", [])]
        for compiler_id in compiler_ids:
            if compiler_id not in compiler_records:
                raise ContractError(f"case {case_id} names unknown compiler {compiler_id}")
            compiler = compiler_records[compiler_id]
            for variant_id, variant_args in variants:
                build_id = f"{case_id}__{compiler_id}__{variant_id}"
                build_dir = output_directory / "builds" / build_id
                build_dir.mkdir(parents=True, exist_ok=True)
                output = build_dir / str(case.get("output_name", f"{case_id}.obj"))
                command = [
                    compiler["executable"],
                    *compiler["base_args"],
                    *case_args,
                    *variant_args,
                    str(source),
                    "-o",
                    str(output),
                ]
                environment = os.environ.copy() if compiler["inherit_environment"] else {}
                environment.update(compiler["environment"])
                completed = subprocess.run(
                    command,
                    cwd=build_dir,
                    env=environment,
                    capture_output=True,
                    text=True,
                    timeout=int(manifest.get("timeout_seconds", 120)),
                    check=False,
                )
                record: dict[str, Any] = {
                    "build_id": build_id,
                    "case_id": case_id,
                    "compiler_id": compiler_id,
                    "variant_id": variant_id,
                    "source": str(source),
                    "source_sha256": sha256_file(source),
                    "compiler_sha256": compiler["sha256"],
                    "command": command,
                    "return_code": completed.returncode,
                    "stdout": completed.stdout,
                    "stderr": completed.stderr,
                    "success": completed.returncode == 0 and output.is_file(),
                    "output": str(output),
                }
                if record["success"]:
                    record["output_sha256"] = sha256_file(output)
                    try:
                        record["coff"] = parse_coff(output).to_dict()
                    except Exception as exc:
                        record["coff_error"] = f"{type(exc).__name__}: {exc}"
                build_records.append(record)
                write_json(build_dir / "record.json", record)
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "compiler_ground_truth_corpus",
        "manifest": str(manifest_path.resolve()),
        "manifest_sha256": sha256_file(manifest_path),
        "compilers": list(compiler_records.values()),
        "builds": build_records,
        "summary": {
            "total": len(build_records),
            "succeeded": sum(1 for record in build_records if record["success"]),
            "failed": sum(1 for record in build_records if not record["success"]),
        },
        "proprietary_toolchains_redistributed": False,
    }
    destination = report_path or output_directory / "corpus.json"
    write_json(destination, report)
    return report


def verify_ground_truth_corpus(report_path: Path) -> dict[str, Any]:
    report = load_json(report_path)
    if not isinstance(report, dict) or report.get("kind") != "compiler_ground_truth_corpus":
        raise ContractError("not a compiler ground-truth corpus report")
    failures: list[str] = []
    for build in report.get("builds", []):
        if not isinstance(build, dict):
            failures.append("malformed build record")
            continue
        source = Path(str(build.get("source", "")))
        if not source.is_file() or sha256_file(source) != build.get("source_sha256"):
            failures.append(f"source hash mismatch: {build.get('build_id')}")
        if build.get("success"):
            output = Path(str(build.get("output", "")))
            if not output.is_file() or sha256_file(output) != build.get("output_sha256"):
                failures.append(f"output hash mismatch: {build.get('build_id')}")
    return {"valid": not failures, "failures": failures, "build_count": len(report.get("builds", []))}



def compare_ground_truth_corpora(
    report_paths: list[Path], *, report_path: Path | None = None
) -> dict[str, Any]:
    """Compare successful corpus builds across compiler/version reports.

    Builds are aligned by ``case_id`` and ``variant_id``.  Exact output hashes,
    COFF section layouts, symbol sets, and compiler identities are reported.
    No semantic-equivalence claim is inferred from identical or different
    object bytes.
    """
    if len(report_paths) < 2:
        raise ContractError("at least two corpus reports are required")
    reports: list[dict[str, Any]] = []
    for path in report_paths:
        value = load_json(path)
        if not isinstance(value, dict) or value.get("kind") != "compiler_ground_truth_corpus":
            raise ContractError(f"not a compiler ground-truth report: {path}")
        reports.append(value)
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for report_index, (path, report) in enumerate(zip(report_paths, reports)):
        compiler_lookup = {item["id"]: item for item in report.get("compilers", []) if isinstance(item, dict)}
        for build in report.get("builds", []):
            if not isinstance(build, dict) or not build.get("success"):
                continue
            key = (str(build.get("case_id")), str(build.get("variant_id")))
            compiler = compiler_lookup.get(build.get("compiler_id"), {})
            coff = build.get("coff") if isinstance(build.get("coff"), dict) else {}
            groups.setdefault(key, []).append(
                {
                    "report_index": report_index,
                    "report": str(path.resolve()),
                    "build_id": build.get("build_id"),
                    "compiler_id": build.get("compiler_id"),
                    "compiler_sha256": build.get("compiler_sha256"),
                    "compiler_version": compiler.get("version"),
                    "output_sha256": build.get("output_sha256"),
                    "architecture": coff.get("architecture"),
                    "section_fingerprint": [
                        (section.get("name"), section.get("size"), section.get("sha256"), section.get("characteristics"))
                        for section in coff.get("sections", []) if isinstance(section, dict)
                    ],
                    "symbols": sorted(
                        symbol.get("name") for symbol in coff.get("symbols", [])
                        if isinstance(symbol, dict) and isinstance(symbol.get("name"), str)
                    ),
                }
            )
    comparisons: list[dict[str, Any]] = []
    for (case_id, variant_id), builds in sorted(groups.items()):
        output_hashes = {item["output_sha256"] for item in builds}
        section_fingerprints = {json.dumps(item["section_fingerprint"], sort_keys=True) for item in builds}
        symbol_fingerprints = {tuple(item["symbols"]) for item in builds}
        comparisons.append(
            {
                "case_id": case_id,
                "variant_id": variant_id,
                "build_count": len(builds),
                "builds": builds,
                "all_object_bytes_identical": len(output_hashes) == 1 and None not in output_hashes,
                "all_section_layouts_identical": len(section_fingerprints) == 1,
                "all_symbol_sets_identical": len(symbol_fingerprints) == 1,
            }
        )
    result = {
        "schema_version": 1,
        "created_at": utc_now(),
        "kind": "compiler_ground_truth_comparison",
        "reports": [
            {"path": str(path.resolve()), "sha256": sha256_file(path)} for path in report_paths
        ],
        "comparisons": comparisons,
        "summary": {
            "aligned_case_variants": len(comparisons),
            "byte_identical_groups": sum(1 for item in comparisons if item["all_object_bytes_identical"]),
            "layout_identical_groups": sum(1 for item in comparisons if item["all_section_layouts_identical"]),
        },
        "semantic_equivalence_claimed": False,
    }
    if report_path is not None:
        write_json(report_path, result)
    return result

def create_builtin_manifest(root: Path, *, output: Path) -> dict[str, Any]:
    root = root.resolve()
    source_root = root / "corpus" / "ground_truth_sources"
    if not source_root.is_dir():
        source_root = Path(__file__).resolve().parent / "corpus" / "ground_truth_sources"
    if not source_root.is_dir():
        raise ContractError("built-in ground-truth sources are unavailable")
    clang = shutil.which("clang")
    clangxx = shutil.which("clang++")
    if clang is None or clangxx is None:
        raise ExternalToolError("clang and clang++ are required to create the built-in manifest")
    c_cases = [
        "arithmetic", "branches", "switch_dense", "structs", "aliasing",
        "calling_conventions", "globals", "tls", "bitfields", "floating_point",
        "loops", "varargs", "indirect_calls", "tail_calls", "vectorizable", "unions",
    ]
    cpp_cases = [
        "classes", "multiple_inheritance", "exceptions", "static_initializers",
        "virtual_inheritance", "templates", "member_pointers", "eh_multiple",
    ]
    version_text = _version(Path(clang).resolve(), ["--version"])
    match = __import__("re").search(r"clang version\s+(\d+)", version_text)
    clang_generation = f"clang{match.group(1)}" if match else "clang"
    manifest = {
        "schema_version": 1,
        "timeout_seconds": 120,
        "compilers": [
            {"id": f"{clang_generation}-msvc-x86-c", "executable": clang, "base_args": ["-target", "i686-pc-windows-msvc", "-c"]},
            {"id": f"{clang_generation}-msvc-x64-c", "executable": clang, "base_args": ["-target", "x86_64-pc-windows-msvc", "-c"]},
            {"id": f"{clang_generation}-msvc-x86-cxx", "executable": clangxx, "base_args": ["-target", "i686-pc-windows-msvc", "-c"]},
            {"id": f"{clang_generation}-msvc-x64-cxx", "executable": clangxx, "base_args": ["-target", "x86_64-pc-windows-msvc", "-c"]},
        ],
        "flag_matrix": {
            "optimization": [
                {"id": "O0", "args": ["-O0"]},
                {"id": "O1", "args": ["-O1"]},
                {"id": "O2", "args": ["-O2"]},
                {"id": "Os", "args": ["-Os"]},
            ],
            "frame_pointer": [
                {"id": "default_fp", "args": []},
                {"id": "keep_fp", "args": ["-fno-omit-frame-pointer"]}
            ]
        },
        "cases": [
            *[
                {
                    "id": case,
                    "source": os.path.relpath(source_root / f"{case}.c", output.parent.resolve()),
                    "compilers": [f"{clang_generation}-msvc-x86-c", f"{clang_generation}-msvc-x64-c"],
                }
                for case in c_cases
            ],
            *[
                {
                    "id": case,
                    "source": os.path.relpath(source_root / f"{case}.cpp", output.parent.resolve()),
                    "compilers": [f"{clang_generation}-msvc-x86-cxx", f"{clang_generation}-msvc-x64-cxx"],
                    "arguments": ["-fexceptions", "-frtti"],
                }
                for case in cpp_cases
            ],
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    write_json(output, manifest)
    return manifest
