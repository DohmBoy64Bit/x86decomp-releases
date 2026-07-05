"""Local-model C generation and deterministic byte-match verification loop."""

from __future__ import annotations

import json
import re
import shutil
import tempfile
from pathlib import Path
from typing import Any

from x86decomp.assembly.relocations import RelocationResolver
from x86decomp.coff import extract_symbol, parse_coff
from x86decomp.compiler import run_compiler_profile
from x86decomp.contracts import ContractError
from x86decomp.diffing import compare_bytes
from x86decomp.errors import ExternalToolError
from x86decomp.util import load_json, sha256_bytes, sha256_file, utc_now, write_json

from .profiles import load_profile, public_profile
from .prompts import build_messages, load_job, prompt_record
from .transport import chat

_MAX_C_SOURCE_BYTES = 1024 * 1024
_FORBIDDEN_SOURCE_PATTERNS = (
    (re.compile(r"\b(?:TODO|FIXME|XXX)\b", re.IGNORECASE), "unfinished marker"),
    (re.compile(r"\bnot\s+implemented\b", re.IGNORECASE), "unfinished marker"),
    (re.compile(r"\.\.\."), "ellipsis/variadic placeholder"),
    (re.compile(r"\b(?:__asm__|__asm|asm)\s*(?:\(|\{)", re.IGNORECASE), "inline assembly"),
    (re.compile(r"\b(?:__emit|_emit)\s*\(", re.IGNORECASE), "machine-byte emission"),
    (re.compile(r"#\s*pragma\s+comment\s*\(\s*linker", re.IGNORECASE), "linker directive"),
    (re.compile(r"\b__declspec\s*\(\s*naked\s*\)", re.IGNORECASE), "naked function"),
)


def _parse_candidate(content: str, *, function_name: str) -> dict[str, Any]:
    """Parse candidate.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if len(content.encode("utf-8")) > _MAX_C_SOURCE_BYTES:
        raise ContractError("local-model candidate exceeded maximum C source size")
    try:
        value = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ContractError("local-model response was not exactly one valid JSON object") from exc
    if not isinstance(value, dict) or set(value) != {"status", "c_source", "assumptions", "rationale"}:
        raise ContractError(
            "local-model response keys must be exactly status, c_source, assumptions, rationale"
        )
    if value["status"] not in {"proposed", "blocked"}:
        raise ContractError("candidate status must be proposed or blocked")
    if not isinstance(value["c_source"], str):
        raise ContractError("candidate c_source must be a string")
    if not isinstance(value["assumptions"], list) or not all(
        isinstance(item, str) for item in value["assumptions"]
    ):
        raise ContractError("candidate assumptions must be an array of strings")
    if not isinstance(value["rationale"], str) or not value["rationale"].strip():
        raise ContractError("candidate rationale must be a non-empty string")
    source = value["c_source"]
    if value["status"] == "blocked":
        if source.strip():
            raise ContractError("blocked candidate must have an empty c_source")
        return value
    if not source.strip():
        raise ContractError("proposed candidate must contain C source")
    for pattern, label in _FORBIDDEN_SOURCE_PATTERNS:
        if pattern.search(source):
            raise ContractError(f"candidate C rejected: {label}")
    escaped = re.escape(function_name)
    requested_definition = re.compile(
        rf"\b{escaped}\s*\([^;{{}}]*\)\s*(?:__attribute__\s*\(\([^{{}}]*\)\)\s*)?\{{",
        re.MULTILINE,
    )
    if len(requested_definition.findall(source)) != 1:
        raise ContractError(
            f"candidate C must define exactly one function named {function_name}"
        )
    broad_matches = re.finditer(
        r"\b(?P<name>[A-Za-z_]\w*)\s*\([^;{}]*\)\s*(?:__attribute__\s*\(\([^{}]*\)\)\s*)?\{",
        source,
        re.MULTILINE,
    )
    broad_definitions = [
        match.group("name")
        for match in broad_matches
        if match.group("name") not in {"if", "for", "while", "switch"}
    ]
    if broad_definitions != [function_name]:
        raise ContractError("candidate C must contain exactly one function definition")
    return value


def _prepare_output(output_directory: Path, *, overwrite: bool) -> Path:
    """Prepare output.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    resolved = output_directory.resolve()
    if resolved.exists():
        if not overwrite:
            raise ContractError(f"output directory already exists: {resolved}")
        if not resolved.is_dir():
            raise ContractError(f"output path is not a directory: {resolved}")
        shutil.rmtree(resolved)
    resolved.parent.mkdir(parents=True, exist_ok=True)
    resolved.mkdir()
    return resolved


def _feedback_from_compile(report: dict[str, Any] | None, error: Exception) -> dict[str, Any]:
    """Implement feedback from compile.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    stderr = "" if report is None else str(report.get("stderr", ""))
    return {
        "gate": "compile",
        "passed": False,
        "error": str(error),
        "compiler_stderr": stderr[-12000:],
    }


def _feedback_from_diff(comparison: dict[str, Any], relocation: dict[str, Any]) -> dict[str, Any]:
    """Implement feedback from diff.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return {
        "gate": "byte_match",
        "passed": False,
        "candidate_size": comparison["candidate_size"],
        "target_size": comparison["target_size"],
        "matching_prefix_bytes": comparison["matching_prefix_bytes"],
        "matching_suffix_bytes": comparison["matching_suffix_bytes"],
        "reported_mismatches": comparison["reported_mismatches"][:32],
        "unresolved_relocations": relocation["unresolved_count"],
    }


def generate_candidate(
    profile_path: Path,
    job_path: Path,
    output: Path,
    *,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Generate and validate one uncompiled C proposal."""
    if output.exists() and not overwrite:
        raise ContractError(f"candidate output already exists: {output.resolve()}")
    profile = load_profile(profile_path)
    job = load_job(job_path)
    prompt = prompt_record(job)
    response = chat(profile, prompt["messages"])
    candidate = _parse_candidate(response.content, function_name=job["function_name"])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(candidate["c_source"], encoding="utf-8")
    report = {
        "schema_version": 1,
        "kind": "local_llm_generation",
        "created_at": utc_now(),
        "status": candidate["status"],
        "profile": public_profile(profile),
        "job": {
            "id": job["id"],
            "function_name": job["function_name"],
            "symbol": job["symbol"],
            "architecture": job["architecture"],
            "target_sha256": job["target_sha256"],
        },
        "prompt_sha256": prompt["prompt_sha256"],
        "structured_output_requested": response.structured_output_requested,
        "structured_output_fallback": response.structured_output_fallback,
        "candidate": {
            "path": str(output.resolve()),
            "sha256": sha256_file(output),
            "assumptions": candidate["assumptions"],
            "rationale": candidate["rationale"],
        },
        "claim": "proposal_only",
    }
    return report


def run_match_loop(
    profile_path: Path,
    compiler_profile_path: Path,
    job_path: Path,
    output_directory: Path,
    *,
    max_attempts: int | None = None,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Run bounded local generation, compilation, relocation, and exact comparison."""
    profile = load_profile(profile_path)
    job = load_job(job_path)
    attempts_limit = job["max_attempts"] if max_attempts is None else max_attempts
    if isinstance(attempts_limit, bool) or not isinstance(attempts_limit, int) or not 1 <= attempts_limit <= 32:
        raise ContractError("max_attempts must be an integer between 1 and 32")
    output_root = _prepare_output(output_directory, overwrite=overwrite)
    attempts_root = output_root / "attempts"
    attempts_root.mkdir()
    feedback: list[dict[str, Any]] = []
    attempts: list[dict[str, Any]] = []
    accepted: dict[str, Any] | None = None
    expected_machine = 0x014C if job["architecture"] == "x86" else 0x8664

    for number in range(1, attempts_limit + 1):
        attempt_root = attempts_root / f"{number:02d}"
        attempt_root.mkdir()
        prompt = prompt_record(job, feedback)
        write_json(attempt_root / "prompt.json", prompt)
        response = chat(profile, prompt["messages"])
        (attempt_root / "response.json.txt").write_text(response.content, encoding="utf-8")
        attempt: dict[str, Any] = {
            "attempt": number,
            "prompt_sha256": prompt["prompt_sha256"],
            "structured_output_requested": response.structured_output_requested,
            "structured_output_fallback": response.structured_output_fallback,
            "status": "rejected",
        }
        try:
            candidate = _parse_candidate(response.content, function_name=job["function_name"])
        except ContractError as exc:
            attempt["gate"] = "candidate_contract"
            attempt["error"] = str(exc)
            feedback.append({"gate": "candidate_contract", "passed": False, "error": str(exc)})
            attempts.append(attempt)
            write_json(attempt_root / "attempt.json", attempt)
            continue
        attempt["candidate_status"] = candidate["status"]
        attempt["assumptions"] = candidate["assumptions"]
        attempt["rationale"] = candidate["rationale"]
        if candidate["status"] == "blocked":
            attempt["gate"] = "model_blocked"
            attempt["status"] = "blocked"
            attempts.append(attempt)
            write_json(attempt_root / "attempt.json", attempt)
            break
        source_path = attempt_root / "candidate.c"
        object_path = attempt_root / "candidate.obj"
        compile_report_path = attempt_root / "compile.json"
        source_path.write_text(candidate["c_source"], encoding="utf-8")
        attempt["source_sha256"] = sha256_file(source_path)
        compile_report: dict[str, Any] | None = None
        try:
            compile_report = run_compiler_profile(
                compiler_profile_path,
                source_path,
                object_path,
                report_path=compile_report_path,
            )
        except (ExternalToolError, ContractError, OSError) as exc:
            if compile_report_path.is_file():
                loaded = load_json(compile_report_path)
                if isinstance(loaded, dict):
                    compile_report = loaded
            attempt["gate"] = "compile"
            attempt["error"] = str(exc)
            feedback.append(_feedback_from_compile(compile_report, exc))
            attempts.append(attempt)
            write_json(attempt_root / "attempt.json", attempt)
            continue
        attempt["compile_report"] = str(compile_report_path.relative_to(output_root))
        obj = parse_coff(object_path)
        if obj.machine != expected_machine:
            message = (
                f"compiler produced machine 0x{obj.machine:04x}; expected 0x{expected_machine:04x}"
            )
            attempt["gate"] = "architecture"
            attempt["error"] = message
            feedback.append({"gate": "architecture", "passed": False, "error": message})
            attempts.append(attempt)
            write_json(attempt_root / "attempt.json", attempt)
            continue
        extracted = extract_symbol(obj, job["symbol"])
        relocation_output = attempt_root / "candidate-resolved.bin"
        relocation = RelocationResolver().resolve(
            object_path,
            symbol=job["symbol"],
            base_rva=job["base_rva"],
            image_base=job["image_base"],
            symbol_map=job["symbol_map"],
            section_placements=job["section_placements"],
            output_path=relocation_output,
            expected_bytes=job["target_bytes"],
        )
        relocation_report = {
            key: value for key, value in relocation.items() if key != "resolved_bytes"
        }
        write_json(attempt_root / "relocation.json", relocation_report)
        comparison = compare_bytes(job["target_bytes"], relocation["resolved_bytes"])
        write_json(attempt_root / "byte-comparison.json", comparison)
        attempt["candidate_object_sha256"] = sha256_file(object_path)
        attempt["candidate_symbol"] = extracted.to_dict(obj.machine)
        attempt["relocation_report"] = str((attempt_root / "relocation.json").relative_to(output_root))
        attempt["byte_comparison"] = str((attempt_root / "byte-comparison.json").relative_to(output_root))
        exact = (
            relocation["unresolved_count"] == 0
            and len(relocation["resolved_bytes"]) == len(job["target_bytes"])
            and comparison["equal"]
        )
        if exact:
            attempt["gate"] = "byte_identity"
            attempt["status"] = "accepted"
            accepted_source = output_root / "accepted.c"
            accepted_object = output_root / "accepted.obj"
            accepted_bytes = output_root / "accepted-resolved.bin"
            shutil.copy2(source_path, accepted_source)
            shutil.copy2(object_path, accepted_object)
            shutil.copy2(relocation_output, accepted_bytes)
            accepted = {
                "attempt": number,
                "source": "accepted.c",
                "source_sha256": sha256_file(accepted_source),
                "object": "accepted.obj",
                "object_sha256": sha256_file(accepted_object),
                "resolved_bytes": "accepted-resolved.bin",
                "resolved_sha256": sha256_file(accepted_bytes),
                "target_sha256": job["target_sha256"],
                "byte_identical": True,
                "unresolved_relocations": 0,
            }
            attempts.append(attempt)
            write_json(attempt_root / "attempt.json", attempt)
            break
        attempt["gate"] = "byte_identity"
        feedback.append(_feedback_from_diff(comparison, relocation))
        attempts.append(attempt)
        write_json(attempt_root / "attempt.json", attempt)

    status = "byte_matched" if accepted is not None else (
        "blocked" if attempts and attempts[-1]["status"] == "blocked" else "exhausted"
    )
    report = {
        "schema_version": 1,
        "kind": "local_llm_byte_match",
        "created_at": utc_now(),
        "status": status,
        "profile": public_profile(profile),
        "compiler_profile": {
            "path": str(compiler_profile_path.resolve()),
            "sha256": sha256_file(compiler_profile_path),
        },
        "job": {
            "path": str(job_path.resolve()),
            "sha256": sha256_file(job_path),
            "id": job["id"],
            "function_name": job["function_name"],
            "symbol": job["symbol"],
            "architecture": job["architecture"],
            "base_rva": job["base_rva"],
            "image_base": job["image_base"],
            "target_size": len(job["target_bytes"]),
            "target_sha256": job["target_sha256"],
        },
        "attempt_limit": attempts_limit,
        "attempt_count": len(attempts),
        "attempts": attempts,
        "accepted": accepted,
        "claim": (
            "relocation-resolved candidate bytes are exactly identical to the declared contiguous target function range"
            if accepted is not None
            else "no byte-identity claim"
        ),
        "limitations": [
            "The model output is an untrusted proposal until deterministic gates accept it.",
            "Byte identity applies only to the declared contiguous function range, compiler profile, and relocation inputs.",
            "Byte identity does not prove recovery of original source text, names, comments, or unique semantics.",
            "Exhausting the attempt limit does not prove that no matching C source exists.",
        ],
    }
    write_json(output_root / "report.json", report)
    return report


def verify_match_report(report_path: Path) -> dict[str, Any]:
    """Verify report invariants and every referenced accepted artifact hash."""
    report = load_json(report_path)
    if not isinstance(report, dict) or report.get("schema_version") != 1:
        raise ContractError("unsupported local-LLM match report")
    if report.get("kind") != "local_llm_byte_match":
        raise ContractError("report kind is not local_llm_byte_match")
    status = report.get("status")
    if status not in {"byte_matched", "blocked", "exhausted"}:
        raise ContractError("invalid local-LLM report status")
    attempts = report.get("attempts")
    if not isinstance(attempts, list) or report.get("attempt_count") != len(attempts):
        raise ContractError("local-LLM report attempt_count is inconsistent")
    accepted = report.get("accepted")
    root = report_path.resolve().parent
    verified: list[dict[str, Any]] = []
    if status == "byte_matched":
        if not isinstance(accepted, dict) or accepted.get("byte_identical") is not True:
            raise ContractError("byte_matched report lacks accepted byte-identical artifact")
        if accepted.get("unresolved_relocations") != 0:
            raise ContractError("byte_matched report contains unresolved relocations")
        if accepted.get("target_sha256") != report.get("job", {}).get("target_sha256"):
            raise ContractError("accepted target hash differs from job target hash")
        for path_key, hash_key in (
            ("source", "source_sha256"),
            ("object", "object_sha256"),
            ("resolved_bytes", "resolved_sha256"),
        ):
            relative = accepted.get(path_key)
            expected = accepted.get(hash_key)
            if not isinstance(relative, str) or not isinstance(expected, str):
                raise ContractError(f"accepted artifact lacks {path_key}/{hash_key}")
            candidate = (root / relative).resolve()
            try:
                candidate.relative_to(root)
            except ValueError as exc:
                raise ContractError("accepted artifact path escapes report directory") from exc
            if not candidate.is_file():
                raise ContractError(f"accepted artifact is missing: {relative}")
            actual = sha256_file(candidate)
            if actual != expected:
                raise ContractError(f"accepted artifact hash mismatch: {relative}")
            verified.append({"path": relative, "sha256": actual})
        if accepted["resolved_sha256"] != accepted["target_sha256"]:
            raise ContractError("accepted resolved bytes are not identical to target hash")
        if not any(item.get("status") == "accepted" for item in attempts):
            raise ContractError("byte_matched report has no accepted attempt")
    elif accepted is not None:
        raise ContractError("non-matched report must not contain accepted artifacts")
    return {
        "schema_version": 1,
        "report": str(report_path.resolve()),
        "valid": True,
        "status": status,
        "verified_artifacts": verified,
    }
