"""Target-specific whole-image convergence analysis.

The engine classifies observed differences and ranks next actions.  It never
claims causality unless the mismatch falls inside a declared PE field or
normalization range.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import ContractError
from .image_match import compare_whole_images
from .pe import parse_pe
from .util import load_json, sha256_file, utc_now, write_json


def _section_kind(name: str, characteristics: int) -> str:
    """Support section kind processing for internal toolkit callers."""
    lower = name.lower()
    if characteristics & 0x20000000:
        return "executable"
    if lower.startswith(".rdata") or lower.startswith(".pdata") or lower.startswith(".xdata"):
        return "read_only_data"
    if lower.startswith(".data") or lower.startswith(".bss"):
        return "writable_data"
    if lower.startswith(".rsrc"):
        return "resources"
    if lower.startswith(".reloc"):
        return "relocations"
    return "other"


def analyze_image_convergence(
    reference: Path,
    candidate: Path,
    *,
    profile_path: Path | None = None,
    previous_report: Path | None = None,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Execute the analyze image convergence operation for the current toolkit workflow."""
    base = compare_whole_images(reference, candidate, profile_path=profile_path)
    ref_image = parse_pe(reference)
    section_by_name = {section.name: section for section in ref_image.sections}
    totals = {
        "section_count": len(base["sections"]),
        "matching_sections": 0,
        "layout_mismatches": 0,
        "executable_mismatch_bytes": 0,
        "read_only_data_mismatch_bytes": 0,
        "writable_data_mismatch_bytes": 0,
        "resource_mismatch_bytes": 0,
        "relocation_mismatch_bytes": 0,
        "other_mismatch_bytes": 0,
    }
    classified_sections: list[dict[str, Any]] = []
    for section_report in base["sections"]:
        name = section_report["name"]
        section = section_by_name.get(name)
        kind = "missing_section" if not section_report.get("present_in_both") else _section_kind(name, section.characteristics if section else 0)
        mismatch_count = int(section_report.get("byte_mismatch_count", 0))
        if section_report.get("present_in_both") and mismatch_count == 0 and section_report.get("layout_match"):
            totals["matching_sections"] += 1
        if section_report.get("present_in_both") and not section_report.get("layout_match"):
            totals["layout_mismatches"] += 1
        key = {
            "executable": "executable_mismatch_bytes",
            "read_only_data": "read_only_data_mismatch_bytes",
            "writable_data": "writable_data_mismatch_bytes",
            "resources": "resource_mismatch_bytes",
            "relocations": "relocation_mismatch_bytes",
        }.get(kind, "other_mismatch_bytes")
        totals[key] += mismatch_count
        classified_sections.append({**section_report, "classification": kind})
    actions: list[dict[str, Any]] = []
    if totals["layout_mismatches"]:
        actions.append(
            {
                "priority": 100,
                "category": "linker_layout",
                "reason": f"{totals['layout_mismatches']} section layouts differ",
                "recommended_command": "layout-reconstruct",
                "claim_strength": "direct_layout_observation",
            }
        )
    if totals["executable_mismatch_bytes"]:
        actions.append(
            {
                "priority": 90,
                "category": "code_generation",
                "reason": f"{totals['executable_mismatch_bytes']} executable-section bytes differ",
                "recommended_command": "diff-function",
                "claim_strength": "section_classification_not_root_cause",
            }
        )
    if totals["read_only_data_mismatch_bytes"]:
        actions.append(
            {
                "priority": 80,
                "category": "read_only_data",
                "reason": f"{totals['read_only_data_mismatch_bytes']} read-only bytes differ",
                "recommended_command": "metadata-scan",
                "claim_strength": "section_classification_not_root_cause",
            }
        )
    if totals["relocation_mismatch_bytes"]:
        actions.append(
            {
                "priority": 75,
                "category": "relocations",
                "reason": f"{totals['relocation_mismatch_bytes']} relocation-section bytes differ",
                "recommended_command": "layout-reconstruct",
                "claim_strength": "section_classification_not_root_cause",
            }
        )
    if totals["resource_mismatch_bytes"]:
        actions.append(
            {
                "priority": 60,
                "category": "resources",
                "reason": f"{totals['resource_mismatch_bytes']} resource bytes differ",
                "recommended_command": "inspect-pe",
                "claim_strength": "section_classification_not_root_cause",
            }
        )
    actions.sort(key=lambda item: (-item["priority"], item["category"]))
    previous: dict[str, Any] | None = None
    delta: dict[str, Any] | None = None
    if previous_report is not None:
        previous = load_json(previous_report)
        if not isinstance(previous, dict) or previous.get("kind") != "image_convergence_report":
            raise ContractError("previous convergence report has an invalid kind")
        previous_totals = previous.get("totals", {})
        delta = {
            key: totals[key] - int(previous_totals.get(key, 0))
            for key in totals
            if isinstance(totals[key], int)
        }
        delta["normalized_mismatch_count"] = base["normalized_mismatch_count"] - int(previous.get("image_match", {}).get("normalized_mismatch_count", 0))
    report = {
        "schema_version": 1,
        "kind": "image_convergence_report",
        "created_at": utc_now(),
        "reference_sha256": sha256_file(reference),
        "candidate_sha256": sha256_file(candidate),
        "image_match": base,
        "totals": totals,
        "sections": classified_sections,
        "next_actions": actions,
        "delta_from_previous": delta,
        "complete": base["raw_exact_match"],
        "normalized_complete": base["normalized_match"],
        "root_cause_claimed": False,
        "limitations": [
            "Section classification does not identify the compiler or linker decision that caused a difference.",
            "Declared normalizations remain visible and never convert a normalized match into byte identity.",
        ],
    }
    if report_path is not None:
        write_json(report_path, report)
    return report


def append_convergence_history(history_path: Path, report: dict[str, Any]) -> dict[str, Any]:
    """Append convergence history for the current toolkit workflow."""
    if report.get("kind") != "image_convergence_report":
        raise ContractError("only image_convergence_report values may be appended")
    history_path.parent.mkdir(parents=True, exist_ok=True)
    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(report, sort_keys=True, ensure_ascii=False) + "\n")
        handle.flush()
    count = sum(1 for line in history_path.read_text(encoding="utf-8").splitlines() if line.strip())
    return {"history_path": str(history_path.resolve()), "entry_count": count}
