"""Ground-truth corpus runner and decomposed benchmark metrics."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Hashable

from .diffing import compare_files
from .dynamic import differential_validate_files
from .errors import ContractError
from .exe_diff import compare_pe_function_to_coff_symbol
from .integration import run_integration_scenarios
from .symbolic import bounded_symbolic_compare_files
from .util import load_json, utc_now, write_json


def classification_metrics(expected: set[Hashable], observed: set[Hashable]) -> dict[str, Any]:
    """Implement classification metrics.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    true_positive = len(expected & observed)
    false_positive = len(observed - expected)
    false_negative = len(expected - observed)
    precision = true_positive / (true_positive + false_positive) if true_positive + false_positive else 1.0
    recall = true_positive / (true_positive + false_negative) if true_positive + false_negative else 1.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def _resolve(base: Path, value: Any) -> Path:
    """Resolve the requested operation.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not isinstance(value, str):
        raise ContractError("benchmark path value must be a string")
    return (base / value).resolve()


def run_benchmark_corpus(manifest_path: Path, *, report_path: Path | None = None) -> dict[str, Any]:
    """Run benchmark corpus.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ContractError("benchmark manifest must be an object")
    base = manifest_path.resolve().parent
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        raise ContractError("benchmark cases must be an array")
    results: list[dict[str, Any]] = []
    counts = {
        "cases": 0,
        "completed": 0,
        "failed": 0,
        "byte_matched": 0,
        "instruction_similar": 0,
        "differentially_validated": 0,
        "symbolically_bounded": 0,
        "integration_validated": 0,
        "human_interventions": 0,
    }
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise ContractError(f"benchmark case {index} must be an object")
        case_id = str(case.get("id", f"case-{index}"))
        kind = case.get("kind")
        counts["cases"] += 1
        counts["human_interventions"] += int(case.get("human_interventions", 0))
        try:
            if kind == "byte_pair":
                result = compare_files(_resolve(base, case["target"]), _resolve(base, case["candidate"]))
                passed = bool(result["equal"])
                counts["byte_matched"] += int(passed)
            elif kind == "pe_coff":
                result = compare_pe_function_to_coff_symbol(
                    pe_path=_resolve(base, case["pe"]),
                    function_rva=int(case["rva"]),
                    function_size=int(case["size"]),
                    coff_path=_resolve(base, case["coff"]),
                    symbol_name=str(case["symbol"]),
                )
                passed = result["classification"] in ("byte_matched", "relocation_normalized_match", "instruction_similar")
                counts["byte_matched"] += int(result["classification"] == "byte_matched")
                counts["instruction_similar"] += int(result["classification"] in ("relocation_normalized_match", "instruction_similar"))
            elif kind == "dynamic":
                result = differential_validate_files(_resolve(base, case["target"]), _resolve(base, case["candidate"]), _resolve(base, case["harness"]))
                passed = bool(result["equivalent_for_harness"])
                counts["differentially_validated"] += int(passed)
            elif kind == "symbolic":
                result = bounded_symbolic_compare_files(
                    _resolve(base, case["target"]),
                    _resolve(base, case["candidate"]),
                    architecture=str(case.get("architecture", "x86")),
                    input_registers=tuple(case.get("input_registers", [])),
                    stack_argument_words=int(case.get("stack_argument_words", 0)),
                    output_registers=tuple(case["output_registers"]) if "output_registers" in case else None,
                    max_steps=int(case.get("max_steps", 1000)),
                    max_paths=int(case.get("max_paths", 64)),
                )
                passed = bool(result["equivalent_within_model"])
                counts["symbolically_bounded"] += int(passed)
            elif kind == "integration":
                result = run_integration_scenarios(
                    _resolve(base, case["manifest"]),
                    allow_host_execution=bool(case.get("allow_host_execution", False)),
                )
                passed = bool(result["all_scenarios_equivalent"])
                counts["integration_validated"] += int(passed)
            elif kind == "discovery_metrics":
                expected = load_json(_resolve(base, case["expected"]))
                observed = load_json(_resolve(base, case["observed"]))
                result = {
                    "function_boundaries": classification_metrics(
                        {tuple(item) for item in expected.get("function_boundaries", [])},
                        {tuple(item) for item in observed.get("function_boundaries", [])},
                    ),
                    "cfg_edges": classification_metrics(
                        {tuple(item) for item in expected.get("cfg_edges", [])},
                        {tuple(item) for item in observed.get("cfg_edges", [])},
                    ),
                    "call_targets": classification_metrics(
                        set(expected.get("call_targets", [])), set(observed.get("call_targets", []))
                    ),
                }
                passed = all(value["f1"] >= float(case.get("minimum_f1", 0.0)) for value in result.values())
            else:
                raise ContractError(f"unsupported benchmark case kind: {kind}")
            counts["completed"] += 1
            results.append({"id": case_id, "kind": kind, "passed": passed, "result": result, "error": None})
        except Exception as exc:
            counts["failed"] += 1
            results.append({"id": case_id, "kind": kind, "passed": False, "result": None, "error": str(exc)})
    denominator = counts["completed"] or 1
    report = {
        "schema_version": 1,
        "created_at": utc_now(),
        "corpus": manifest.get("name"),
        "counts": counts,
        "rates": {
            "completion_rate": counts["completed"] / counts["cases"] if counts["cases"] else 1.0,
            "byte_match_rate": counts["byte_matched"] / denominator,
            "differential_pass_rate": counts["differentially_validated"] / denominator,
            "symbolic_pass_rate": counts["symbolically_bounded"] / denominator,
            "integration_pass_rate": counts["integration_validated"] / denominator,
        },
        "cases": results,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
