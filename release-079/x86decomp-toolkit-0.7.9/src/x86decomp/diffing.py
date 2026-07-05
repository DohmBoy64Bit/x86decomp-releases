"""Exact byte comparison and transparent similarity reporting."""

from __future__ import annotations

from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .errors import ContractError
from .util import sha256_bytes, utc_now, write_json


def compare_bytes(target: bytes, candidate: bytes, *, max_mismatches: int = 64) -> dict[str, Any]:
    """Compare bytes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if max_mismatches < 1:
        raise ContractError("max_mismatches must be positive")
    common = min(len(target), len(candidate))
    mismatches: list[dict[str, int]] = []
    for offset in range(common):
        if target[offset] != candidate[offset]:
            mismatches.append(
                {"offset": offset, "target": target[offset], "candidate": candidate[offset]}
            )
            if len(mismatches) >= max_mismatches:
                break
    if len(target) != len(candidate) and len(mismatches) < max_mismatches:
        mismatches.append(
            {
                "offset": common,
                "target": target[common] if common < len(target) else -1,
                "candidate": candidate[common] if common < len(candidate) else -1,
            }
        )
    prefix = 0
    while prefix < common and target[prefix] == candidate[prefix]:
        prefix += 1
    suffix = 0
    while (
        suffix < common - prefix
        and target[len(target) - 1 - suffix] == candidate[len(candidate) - 1 - suffix]
    ):
        suffix += 1
    ratio = SequenceMatcher(None, target, candidate, autojunk=False).ratio()
    return {
        "schema_version": 1,
        "created_at": utc_now(),
        "equal": target == candidate,
        "target_size": len(target),
        "candidate_size": len(candidate),
        "target_sha256": sha256_bytes(target),
        "candidate_sha256": sha256_bytes(candidate),
        "matching_prefix_bytes": prefix,
        "matching_suffix_bytes": suffix,
        "sequence_similarity": ratio,
        "reported_mismatches": mismatches,
        "mismatch_report_truncated": len(mismatches) >= max_mismatches,
        "semantic_equivalence_claimed": False,
    }


def compare_files(
    target_path: Path,
    candidate_path: Path,
    *,
    max_mismatches: int = 64,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Compare files.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not target_path.is_file() or not candidate_path.is_file():
        raise ContractError("both target and candidate must be existing files")
    report = compare_bytes(
        target_path.read_bytes(), candidate_path.read_bytes(), max_mismatches=max_mismatches
    )
    report["target_path"] = str(target_path.resolve())
    report["candidate_path"] = str(candidate_path.resolve())
    if report_path is not None:
        write_json(report_path, report)
    return report
