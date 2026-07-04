"""Compiler-profile experiment matrix, caching, ranking, and provenance."""

from __future__ import annotations

import itertools
from pathlib import Path
from typing import Any

from .compiler import run_compiler_profile
from .diffing import compare_files
from .errors import ContractError, ExternalToolError
from .exe_diff import compare_pe_function_to_coff_symbol
from .util import load_json, utc_now, write_json


def _variant_arguments(matrix: dict[str, Any]) -> list[tuple[str, list[str]]]:
    axes = matrix.get("axes", {})
    if not isinstance(axes, dict):
        raise ContractError("compiler lab matrix.axes must be an object")
    normalized: list[tuple[str, list[str]]] = []
    for key, values in axes.items():
        if not isinstance(key, str) or not isinstance(values, list) or not values or not all(isinstance(item, str) for item in values):
            raise ContractError("each compiler lab axis must be a non-empty string array")
        normalized.append((key, values))
    return normalized


def run_compiler_lab(
    lab_path: Path,
    *,
    report_path: Path | None = None,
) -> dict[str, Any]:
    lab = load_json(lab_path)
    if not isinstance(lab, dict):
        raise ContractError("compiler lab document must be an object")
    base = lab_path.resolve().parent
    source = (base / str(lab["source"])).resolve()
    output_root = (base / str(lab.get("output_root", "compiler-lab-output"))).resolve()
    cache_root = (base / str(lab.get("cache_root", ".compiler-cache"))).resolve()
    profiles_raw = lab.get("profiles")
    if not isinstance(profiles_raw, list) or not profiles_raw:
        raise ContractError("compiler lab profiles must be a non-empty array")
    profiles = [(base / str(item)).resolve() for item in profiles_raw]
    axes = _variant_arguments(lab.get("matrix", {}))
    combinations = list(itertools.product(*[values for _name, values in axes])) if axes else [()]
    max_experiments = lab.get("max_experiments", 256)
    if not isinstance(max_experiments, int) or max_experiments <= 0:
        raise ContractError("max_experiments must be positive")
    if len(profiles) * len(combinations) > max_experiments:
        raise ContractError("compiler lab matrix exceeds max_experiments")
    output_root.mkdir(parents=True, exist_ok=True)
    experiments: list[dict[str, Any]] = []
    target = lab.get("target", {})
    for profile_index, profile in enumerate(profiles):
        for combination_index, combination in enumerate(combinations):
            selections = {axes[index][0]: value for index, value in enumerate(combination)}
            extra_arguments = list(combination)
            experiment_id = f"p{profile_index:03d}-v{combination_index:04d}"
            output = output_root / experiment_id / str(lab.get("output_name", "candidate.obj"))
            compile_report_path = output.parent / "compile.json"
            try:
                compile_report = run_compiler_profile(
                    profile,
                    source,
                    output,
                    report_path=compile_report_path,
                    extra_arguments=extra_arguments,
                    cache_directory=cache_root,
                )
                error = None
            except ExternalToolError as exc:
                compile_report = None
                error = str(exc)
            comparison: dict[str, Any] | None = None
            score = -1.0
            if compile_report is not None:
                kind = target.get("kind")
                if kind == "pe_function":
                    comparison = compare_pe_function_to_coff_symbol(
                        pe_path=(base / str(target["pe"])).resolve(),
                        function_rva=int(target["rva"]),
                        function_size=int(target["size"]),
                        coff_path=output,
                        symbol_name=str(target["symbol"]),
                        report_path=output.parent / "comparison.json",
                    )
                    classification_scores = {
                        "byte_matched": 4.0,
                        "relocation_normalized_match": 3.0,
                        "instruction_similar": 2.0,
                        "mismatch": 0.0,
                    }
                    score = classification_scores[comparison["classification"]]
                    instruction = comparison.get("instruction_comparison")
                    if instruction is not None:
                        score += float(instruction["normalized_similarity"])
                elif kind == "file":
                    comparison = compare_files((base / str(target["path"])).resolve(), output, report_path=output.parent / "comparison.json")
                    score = 2.0 if comparison["equal"] else float(comparison["sequence_similarity"])
                elif kind is not None:
                    raise ContractError(f"unsupported compiler lab target kind: {kind}")
            experiments.append(
                {
                    "id": experiment_id,
                    "profile": str(profile),
                    "selections": selections,
                    "extra_arguments": extra_arguments,
                    "compile": compile_report,
                    "comparison": comparison,
                    "error": error,
                    "score": score,
                }
            )
    experiments.sort(key=lambda item: (-item["score"], item["id"]))
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "source": str(source),
        "experiment_count": len(experiments),
        "best_experiment": experiments[0]["id"] if experiments else None,
        "experiments": experiments,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
