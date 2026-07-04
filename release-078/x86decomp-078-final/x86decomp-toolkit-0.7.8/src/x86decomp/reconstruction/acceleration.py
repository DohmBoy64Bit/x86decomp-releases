"""Human-readable decompilation acceleration helpers.

These helpers deliberately create reviewable manifests, source annotations, and
triage reports.  They do not claim original source recovery or validator success;
state-changing commands require concrete input reports and emit auditable JSON.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Iterable

from x86decomp.artifacts import function_id_from_rva, validate_function_manifest
from x86decomp.contracts import ContractError, utc_now
from x86decomp.cpp_recovery import recover_cpp_model
from x86decomp.local_llm.matching import run_match_loop
from x86decomp.local_llm.prompts import load_job
from x86decomp.util import load_json, sha256_bytes, sha256_file, write_json
from x86decomp.workflow import MatchingStatus, SourceStage, update_function_workflow

_HEX_RE = re.compile(r"^[0-9A-Fa-f\s]+$")
_ANNOTATION_RE = re.compile(r"^\s*//\s*FUNCTION:\s+(?P<binary>\S+)\s+0x(?P<rva>[0-9A-Fa-f]{1,16})(?:\s+(?P<function_id>pe-rva:[0-9A-Fa-f]{8}))?\s*$")
_FUNC_DEF_RE = re.compile(r"(?m)^\s*(?:[A-Za-z_][\w:\<\>\*&\s~]+\s+)+(?P<name>[A-Za-z_~][\w:~]*)\s*\([^;{}]*\)\s*(?:const\s*)?\{")


def _safe_rel(root: Path, target: Path) -> Path:
    root = root.resolve()
    resolved = target.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ContractError(f"path escapes project root: {target}") from exc
    return resolved


def _read_text_if_exists(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def _body_ranges(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    validate_function_manifest(manifest)
    ranges = manifest["body_ranges"]
    normalized: list[dict[str, Any]] = []
    for item in ranges:
        normalized.append({
            "start_rva": item["start_rva"],
            "end_rva": item["end_rva"],
            "size": int(item.get("size", item["end_rva"] - item["start_rva"])),
            "file": item.get("file"),
        })
    return normalized


def _contiguous_single_range(manifest: dict[str, Any]) -> dict[str, Any]:
    ranges = _body_ranges(manifest)
    if len(ranges) != 1:
        raise ContractError("local-LLM job requires exactly one contiguous function body range")
    item = ranges[0]
    if item["size"] != item["end_rva"] - item["start_rva"]:
        raise ContractError("body range size does not match start/end RVA span")
    return item


def _read_range_bytes(artifact_dir: Path, manifest: dict[str, Any], range_record: dict[str, Any]) -> bytes:
    rel = range_record.get("file")
    if rel:
        path = _safe_rel(artifact_dir, artifact_dir / rel)
        if not path.is_file():
            raise ContractError(f"body range file does not exist: {rel}")
        data = path.read_bytes()
        if len(data) != range_record["size"]:
            raise ContractError("body range file size does not match manifest size")
        return data
    raw_hex = manifest.get("target_bytes_hex") or manifest.get("bytes_hex")
    if isinstance(raw_hex, str) and _HEX_RE.fullmatch(raw_hex):
        data = bytes.fromhex("".join(raw_hex.split()))
        if len(data) == range_record["size"]:
            return data
    raise ContractError("function artifact must provide a body range file or matching inline bytes")


def _read_mnemonics(artifact_dir: Path) -> str:
    candidates = [
        "listing.asm", "instructions.asm", "mnemonics.asm", "disassembly.asm", "instructions.txt",
        "decompiler.asm", "body.asm",
    ]
    for name in candidates:
        text = _read_text_if_exists(artifact_dir / name)
        if text.strip():
            return text
    jsonl = artifact_dir / "instructions.jsonl"
    if jsonl.is_file():
        lines: list[str] = []
        for raw in jsonl.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            try:
                item = json.loads(raw)
            except json.JSONDecodeError:
                lines.append(raw)
                continue
            if isinstance(item, dict):
                mnemonic = item.get("mnemonic") or item.get("op") or item.get("text")
                operands = item.get("op_str") or item.get("operands") or ""
                address = item.get("address") or item.get("rva")
                prefix = f"{address}: " if address is not None else ""
                lines.append(f"{prefix}{mnemonic} {operands}".strip())
        if lines:
            return "\n".join(lines)
    raise ContractError("function artifact does not contain a mnemonic listing")


def _function_name(function_id: str, explicit: str | None = None) -> str:
    if explicit:
        return explicit
    if function_id.startswith("pe-rva:"):
        return "sub_" + function_id.split(":", 1)[1]
    return re.sub(r"\W+", "_", function_id).strip("_") or "sub_unknown"


def llm_job_from_function_packet(
    artifact_dir: Path,
    output: Path,
    *,
    architecture: str,
    image_base: int = 0,
    function_name: str | None = None,
    symbol: str | None = None,
    max_attempts: int = 4,
    inline: bool = False,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Create one local-LLM job from a verified function artifact directory."""
    if architecture not in {"x86", "x86_64"}:
        raise ContractError("architecture must be x86 or x86_64")
    artifact_dir = artifact_dir.resolve()
    manifest_path = artifact_dir / "function.json"
    if not manifest_path.is_file():
        raise ContractError("function packet must contain function.json")
    manifest = validate_function_manifest(load_json(manifest_path))
    range_record = _contiguous_single_range(manifest)
    target_bytes = _read_range_bytes(artifact_dir, manifest, range_record)
    mnemonics = _read_mnemonics(artifact_dir)
    fid = manifest["id"]
    name = _function_name(fid, function_name)
    sym = symbol or name
    evidence = {
        "decompiler_c": _read_text_if_exists(artifact_dir / "decompiler.c"),
        "pcode": _read_text_if_exists(artifact_dir / "high-pcode.jsonl") or _read_text_if_exists(artifact_dir / "raw-pcode.jsonl"),
        "references": _read_text_if_exists(artifact_dir / "references.json") or _read_text_if_exists(artifact_dir / "references.jsonl"),
        "analyst_notes": _read_text_if_exists(artifact_dir / "notes.md"),
    }
    evidence = {k: v for k, v in evidence.items() if v.strip()}
    job: dict[str, Any] = {
        "schema_version": 1,
        "id": fid.replace(":", "_"),
        "function_name": name,
        "symbol": sym,
        "architecture": architecture,
        "base_rva": range_record["start_rva"],
        "image_base": image_base,
        "abi": manifest.get("abi", {}),
        "evidence": evidence,
        "max_attempts": max_attempts,
        "provenance": {
            "kind": "function_packet",
            "artifact_dir": str(artifact_dir),
            "function_id": fid,
            "function_manifest_sha256": sha256_file(manifest_path),
        },
    }
    output = output.resolve()
    if output.exists() and not overwrite:
        raise ContractError(f"job file already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    if inline:
        job["mnemonics"] = mnemonics
        job["target_bytes_hex"] = target_bytes.hex()
    else:
        stem = output.stem
        bytes_path = output.parent / f"{stem}.bin"
        asm_path = output.parent / f"{stem}.asm"
        if (bytes_path.exists() or asm_path.exists()) and not overwrite:
            raise ContractError("job sidecar files already exist; use --overwrite")
        bytes_path.write_bytes(target_bytes)
        asm_path.write_text(mnemonics, encoding="utf-8")
        job["target_bytes_file"] = bytes_path.name
        job["mnemonics_file"] = asm_path.name
    write_json(output, job)
    normalized = load_job(output)
    return {
        "schema_version": 1,
        "kind": "local_llm_job_create_report",
        "created_at": utc_now(),
        "job_path": str(output),
        "job_id": normalized["id"],
        "function_name": normalized["function_name"],
        "architecture": normalized["architecture"],
        "base_rva": normalized["base_rva"],
        "target_size": len(normalized["target_bytes"]),
        "target_sha256": normalized["target_sha256"],
        "eligible": True,
        "claim": "job_materialized_only",
    }


def llm_job_from_range(
    image: Path,
    output: Path,
    *,
    rva: int,
    size: int,
    architecture: str,
    function_name: str,
    symbol: str | None = None,
    image_base: int = 0,
    mnemonics: Path | None = None,
    max_attempts: int = 4,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Create one local-LLM job from an explicitly supplied file offset/RVA range.

    This command treats the supplied file as a raw byte carrier. It does not parse
    PE section mappings; callers must provide the correct range bytes.
    """
    if architecture not in {"x86", "x86_64"}:
        raise ContractError("architecture must be x86 or x86_64")
    if rva < 0 or size <= 0:
        raise ContractError("rva must be >= 0 and size must be > 0")
    data = image.read_bytes()
    if rva + size > len(data):
        raise ContractError("requested range extends beyond input file; use extracted range bytes or a function packet")
    target = data[rva:rva + size]
    output = output.resolve()
    if output.exists() and not overwrite:
        raise ContractError(f"job file already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    stem = output.stem
    bytes_path = output.parent / f"{stem}.bin"
    asm_path = output.parent / f"{stem}.asm"
    if (bytes_path.exists() or asm_path.exists()) and not overwrite:
        raise ContractError("job sidecar files already exist; use --overwrite")
    bytes_path.write_bytes(target)
    if mnemonics is None:
        asm_text = "; mnemonic listing was not supplied; range bytes are recorded only\n"
    else:
        asm_text = mnemonics.read_text(encoding="utf-8")
        if not asm_text.strip():
            raise ContractError("mnemonics file must not be empty")
    asm_path.write_text(asm_text, encoding="utf-8")
    fid = function_id_from_rva(rva)
    job = {
        "schema_version": 1,
        "id": fid.replace(":", "_"),
        "function_name": function_name,
        "symbol": symbol or function_name,
        "architecture": architecture,
        "mnemonics_file": asm_path.name,
        "target_bytes_file": bytes_path.name,
        "base_rva": rva,
        "image_base": image_base,
        "abi": {},
        "evidence": {"analyst_notes": "Job was created from an explicit byte range; no PE section mapping was inferred."},
        "max_attempts": max_attempts,
        "provenance": {"kind": "explicit_range", "image": str(image.resolve()), "image_sha256": sha256_file(image), "rva": rva, "size": size},
    }
    write_json(output, job)
    normalized = load_job(output)
    return {
        "schema_version": 1,
        "kind": "local_llm_job_from_range_report",
        "created_at": utc_now(),
        "job_path": str(output),
        "job_id": normalized["id"],
        "target_size": len(normalized["target_bytes"]),
        "target_sha256": normalized["target_sha256"],
        "claim": "explicit_range_job_materialized_only",
    }


def llm_batch_create(project: Path, output: Path, *, architecture: str, image_base: int = 0, max_bytes: int = 256, max_attempts: int = 4, overwrite: bool = False) -> dict[str, Any]:
    functions_root = project.resolve() / "functions"
    if not functions_root.is_dir():
        raise ContractError("project has no functions directory")
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    created: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    for manifest_path in sorted(functions_root.glob("*/function.json")):
        artifact = manifest_path.parent
        try:
            manifest = validate_function_manifest(load_json(manifest_path))
            rg = _contiguous_single_range(manifest)
            if rg["size"] > max_bytes:
                raise ContractError(f"function body size {rg['size']} exceeds max_bytes {max_bytes}")
            out = output / f"{manifest['id'].replace(':', '_')}.json"
            report = llm_job_from_function_packet(artifact, out, architecture=architecture, image_base=image_base, max_attempts=max_attempts, overwrite=overwrite)
            created.append(report)
        except Exception as exc:
            fid = None
            try: fid = load_json(manifest_path).get("id")
            except Exception: pass
            blocked.append({"artifact_dir": str(artifact), "function_id": fid, "reason": str(exc)})
    report = {"schema_version": 1, "kind": "local_llm_batch_create_report", "created_at": utc_now(), "created_count": len(created), "blocked_count": len(blocked), "created": created, "blocked": blocked}
    write_json(output / "batch-create-report.json", report)
    return report


def llm_batch_match(profile: Path, compiler_profile: Path, jobs: Path, output: Path, *, max_workers: int = 1, max_attempts: int | None = None, overwrite: bool = False) -> dict[str, Any]:
    if max_workers != 1:
        raise ContractError("v0.7.8 batch-match is deterministic and single-worker; pass --max-workers 1")
    job_paths = sorted(jobs.glob("*.json")) if jobs.is_dir() else [jobs]
    output.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []
    summary = {"accepted": 0, "blocked": 0, "rejected": 0, "error": 0}
    for job_path in job_paths:
        if job_path.name == "batch-create-report.json":
            continue
        out = output / job_path.stem
        try:
            result = run_match_loop(profile, compiler_profile, job_path, out, max_attempts=max_attempts, overwrite=overwrite)
            status = result.get("status", "unknown")
            if status == "accepted": summary["accepted"] += 1
            elif status == "blocked": summary["blocked"] += 1
            else: summary["rejected"] += 1
            results.append({"job": str(job_path), "output_directory": str(out), "status": status, "report": result})
        except Exception as exc:
            summary["error"] += 1
            results.append({"job": str(job_path), "output_directory": str(out), "status": "error", "error": str(exc)})
    report = {"schema_version": 1, "kind": "local_llm_batch_match_report", "created_at": utc_now(), "summary": summary, "results": results, "claim": "batch_reports_only"}
    write_json(output / "batch-match-report.json", report)
    return report


def candidate_promote(project: Path, function_id: str, candidate: Path, report: Path, *, stage: str, update_build: bool = False, update_workflow: bool = False, overwrite: bool = False) -> dict[str, Any]:
    project = project.resolve(); candidate = candidate.resolve(); report = report.resolve()
    if not candidate.is_file(): raise ContractError("candidate source does not exist")
    if not report.is_file(): raise ContractError("validation report does not exist")
    data = load_json(report)
    acceptable = False
    reasons: list[str] = []
    if data.get("status") == "accepted" and data.get("accepted"):
        acceptable = True; reasons.append("local LLM match report accepted candidate")
    if data.get("equal") is True or data.get("byte_matched") is True:
        acceptable = True; reasons.append("report declares byte equality")
    if data.get("valid") is True and data.get("status") in {"integration_validated", "symbolically_bounded", "byte_matched"}:
        acceptable = True; reasons.append("report declares accepted validation status")
    if not acceptable:
        raise ContractError("candidate report does not prove an accepted validation gate")
    ext = candidate.suffix or ".c"
    dest = project / "src" / stage / f"{function_id.replace(':','_')}{ext}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and not overwrite: raise ContractError(f"accepted source already exists: {dest}")
    shutil.copy2(candidate, dest)
    provenance = {"schema_version": 1, "kind": "candidate_promotion", "created_at": utc_now(), "function_id": function_id, "candidate": str(candidate), "candidate_sha256": sha256_file(candidate), "accepted_source": str(dest), "report": str(report), "report_sha256": sha256_file(report), "stage": stage, "reasons": reasons, "update_build_requested": update_build}
    write_json(dest.with_suffix(dest.suffix + ".promotion.json"), provenance)
    workflow_result = None
    if update_workflow:
        mstatus = MatchingStatus.BYTE_MATCHED if stage in {"matched", "accepted", "llm-accepted"} else None
        workflow_result = update_function_workflow(project, function_id, source_stage=SourceStage.ACCEPTED_SOURCE, matching_status=mstatus, active_candidate=str(dest), report_kind="candidate-promotion", report_path=str(report), allow_regression=False).to_dict()
    return {**provenance, "workflow": workflow_result}


def source_map_annotate(project: Path, source_root: Path, *, binary: str = "GAME", report_path: Path | None = None) -> dict[str, Any]:
    root = source_root.resolve(); changed=[]; skipped=[]
    for path in sorted([p for p in root.rglob("*") if p.suffix.lower() in {".c", ".cc", ".cpp", ".h", ".hpp"}]):
        text = path.read_text(encoding="utf-8")
        if _ANNOTATION_RE.search(text):
            skipped.append({"path": str(path), "reason": "already annotated"}); continue
        m = re.search(r"pe[-_]?rva[:_]?([0-9A-Fa-f]{8})", str(path))
        if not m:
            skipped.append({"path": str(path), "reason": "no function id in path"}); continue
        rva = int(m.group(1), 16)
        annotation = f"// FUNCTION: {binary} 0x{rva:08X} pe-rva:{rva:08x}\n"
        path.write_text(annotation + text, encoding="utf-8")
        changed.append({"path": str(path), "function_id": f"pe-rva:{rva:08x}", "rva": rva})
    report={"schema_version":1,"kind":"source_map_annotation_report","created_at":utc_now(),"changed_count":len(changed),"skipped_count":len(skipped),"changed":changed,"skipped":skipped}
    if report_path: write_json(report_path, report)
    return report


def source_map_verify(project: Path, source_root: Path, *, report_path: Path | None = None) -> dict[str, Any]:
    seen: dict[str, str] = {}; errors=[]; annotations=[]
    for path in sorted([p for p in source_root.resolve().rglob("*") if p.is_file() and p.suffix.lower() in {".c", ".cc", ".cpp", ".h", ".hpp"}]):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            m = _ANNOTATION_RE.match(line)
            if not m: continue
            rva = int(m.group("rva"), 16); fid = m.group("function_id") or f"pe-rva:{rva:08x}"
            record = {"path": str(path), "line": lineno, "function_id": fid, "rva": rva, "binary": m.group("binary")}
            annotations.append(record)
            if fid in seen:
                errors.append(f"duplicate annotation for {fid}: {seen[fid]} and {path}")
            seen[fid] = str(path)
    report={"schema_version":1,"kind":"source_map_verification_report","created_at":utc_now(),"valid":not errors,"annotation_count":len(annotations),"errors":errors,"annotations":annotations}
    if report_path: write_json(report_path, report)
    return report


def module_assign(project: Path, function_id: str, *, module: str, class_name: str | None, header: str | None, source: str | None, report_path: Path | None = None) -> dict[str, Any]:
    manifest_path = project.resolve()/"reconstruction"/"module-assignments.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = load_json(manifest_path) if manifest_path.is_file() else {"schema_version":1,"assignments":{}}
    manifest["assignments"][function_id] = {"module": module, "class": class_name, "header": header, "source": source, "updated_at": utc_now()}
    write_json(manifest_path, manifest)
    report={"schema_version":1,"kind":"module_assignment_report","function_id":function_id,"assignment":manifest["assignments"][function_id],"manifest":str(manifest_path)}
    if report_path: write_json(report_path, report)
    return report


def module_suggest(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    functions = project.resolve()/"functions"; clusters: dict[str, list[str]] = {}
    if functions.is_dir():
        for manifest_path in sorted(functions.glob("*/function.json")):
            fid = load_json(manifest_path).get("id", manifest_path.parent.name)
            evidence = (manifest_path.parent/"references.json").read_text(encoding="utf-8") if (manifest_path.parent/"references.json").is_file() else ""
            key="general"
            lowered=evidence.lower()
            for candidate in ("audio","render","graphics","input","network","file","resource","physics","ai"):
                if candidate in lowered:
                    key=candidate; break
            clusters.setdefault(key,[]).append(fid)
    suggestions=[{"module":k,"function_ids":v,"basis":"keyword evidence from references where available; otherwise general bucket","original_names_claimed":False} for k,v in sorted(clusters.items())]
    report={"schema_version":1,"kind":"module_suggestion_report","created_at":utc_now(),"suggestions":suggestions}
    if output: write_json(output, report)
    return report


def type_propagate(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    # Bounded manifest generator: it reports accepted ABI/header records and files to update; no silent source edits.
    db = project.resolve()/"reconstruction.sqlite"
    observations=[]
    # The toolkit commonly stores reconstruction state in governance.db; avoid assuming schema location.
    for p in [project.resolve()/"project.sqlite", project.resolve()/"state.sqlite", project.resolve()/"reconstruction.sqlite"]:
        if p.is_file(): observations.append({"database":str(p),"action":"available_for_external_type_propagation"})
    report={"schema_version":1,"kind":"type_propagation_plan","created_at":utc_now(),"source_edits_performed":False,"observations":observations,"claim":"plan_only_no_silent_overwrite"}
    if output: write_json(output, report)
    return report


def header_synthesize_project(project: Path, output: Path, *, module: str | None = None) -> dict[str, Any]:
    output = output.resolve(); output.mkdir(parents=True, exist_ok=True)
    assignments_path = project.resolve()/"reconstruction"/"module-assignments.json"
    assignments = load_json(assignments_path).get("assignments", {}) if assignments_path.is_file() else {}
    headers: dict[str, list[str]] = {}
    for fid, item in assignments.items():
        if module and item.get("module") != module: continue
        header = item.get("header") or f"{item.get('module','general')}.hpp"
        symbol = fid.replace(':','_')
        headers.setdefault(header, []).append(f"// {fid}\nvoid {symbol}(void);")
    written=[]
    if not headers:
        path=output/"reconstruction_provisional.hpp"; path.write_text("#pragma once\n// No module assignments were available for declaration synthesis.\n",encoding="utf-8"); written.append(str(path))
    else:
        for header, decls in headers.items():
            path=_safe_rel(output, output/header); path.parent.mkdir(parents=True,exist_ok=True); path.write_text("#pragma once\n\n"+"\n".join(decls)+"\n",encoding="utf-8"); written.append(str(path))
    return {"schema_version":1,"kind":"header_synthesis_report","created_at":utc_now(),"written":written,"verified_declarations_claimed":False}


def vtable_recover(project: Path, image: Path, output: Path, *, metadata_report: Path | None = None) -> dict[str, Any]:
    report = recover_cpp_model(image, metadata_report=metadata_report, report_path=output)
    return report


def class_scaffold(project: Path, vtable_report: Path, output: Path, headers: Path | None = None) -> dict[str, Any]:
    data=load_json(vtable_report); output.mkdir(parents=True,exist_ok=True); written=[]
    header_root=headers or output; header_root.mkdir(parents=True,exist_ok=True)
    for cls in data.get("classes",[]):
        name = re.sub(r"\W+","_",str(cls.get("type_name") or "RecoveredClass")).strip("_") or "RecoveredClass"
        slots=[]
        for vt in cls.get("vtables",[]):
            for i,_ in enumerate(vt.get("function_rvas",[])):
                slots.append(f"    virtual void slot_{i:03d}();")
        if not slots: slots=["    virtual ~%s();"%name]
        text="#pragma once\n\n// Provisional scaffold from emitted metadata; not original source.\nclass %s {\npublic:\n%s\n};\n"%(name,"\n".join(slots))
        path=header_root/f"{name}.hpp"; path.write_text(text,encoding="utf-8"); written.append(str(path))
    report={"schema_version":1,"kind":"class_scaffold_report","created_at":utc_now(),"written":written,"original_source_claimed":False}
    write_json(output/"class-scaffold-report.json",report)
    return report


def diff_explain(diff_report: Path, source: Path | None = None, output: Path | None = None) -> dict[str, Any]:
    data=load_json(diff_report); hints=[]
    mismatches=data.get("reported_mismatches") or data.get("mismatches") or []
    if data.get("candidate_size") != data.get("target_size"): hints.append("candidate and target sizes differ")
    if any(isinstance(m,dict) and str(m.get("candidate","")) in {"90","cc"} for m in mismatches): hints.append("padding or trap-byte difference near a mismatch")
    if data.get("unresolved_relocations") or data.get("unresolved_count"): hints.append("unresolved relocation prevents exact-byte acceptance")
    if not hints and mismatches: hints.append("instruction selection, register allocation, or constant materialization differs")
    if not hints: hints.append("no common mismatch category detected from this report")
    report={"schema_version":1,"kind":"diff_explanation_report","created_at":utc_now(),"diff_report":str(diff_report),"source":None if source is None else str(source),"hints":hints,"claim":"diagnostic_hints_only"}
    if output:
        output.write_text("# Diff explanation\n\n"+"\n".join(f"- {h}" for h in hints)+"\n",encoding="utf-8")
    return report


def triage_next(project: Path, *, goal: str, limit: int, output: Path | None = None) -> dict[str, Any]:
    priorities = ["entry point", "static initialization", "resource loading", "window creation", "main loop", "input", "render init", "audio init", "map loading"] if goal == "playable" else ["small leaf functions", "known ABI", "known compiler profile", "few relocations"]
    candidates=[]
    functions=project.resolve()/"functions"
    if functions.is_dir():
        for p in sorted(functions.glob("*/function.json"))[:limit]: candidates.append(load_json(p).get("id",p.parent.name))
    report={"schema_version":1,"kind":"triage_next_report","goal":goal,"created_at":utc_now(),"priorities":priorities,"candidate_function_ids":candidates,"claim":"planning_only"}
    if output: write_json(output, report)
    return report


def playability_smoke_plan(project: Path, target: Path, output: Path, *, profile: str = "windows-game") -> dict[str, Any]:
    output.mkdir(parents=True,exist_ok=True)
    checks=["process_starts","imports_resolve","window_or_main_loop_survives","expected_files_observed","clean_exit_or_timeout"]
    manifest={"schema_version":1,"kind":"integration_scenario_manifest","profile":profile,"target":str(target.resolve()),"checks":[{"id":c,"status":"requires_operator_binding"} for c in checks],"host_execution_allowed":False}
    path=output/"smoke-plan.json"; write_json(path,manifest)
    return {"schema_version":1,"kind":"playability_smoke_plan_report","created_at":utc_now(),"manifest":str(path),"checks":checks,"claim":"scaffold_only_requires_human_refinement"}


def asset_inventory(root: Path, output: Path | None = None) -> dict[str, Any]:
    categories={"textures":[],"audio":[],"models":[],"maps":[],"scripts":[],"archives":[],"configs":[],"unknown":[]}
    mapping={".png":"textures",".dds":"textures",".tga":"textures",".wav":"audio",".mp3":"audio",".ogg":"audio",".obj":"models",".3ds":"models",".map":"maps",".lua":"scripts",".py":"scripts",".rfa":"archives",".zip":"archives",".ini":"configs",".cfg":"configs",".json":"configs"}
    for p in sorted(root.rglob("*")):
        if not p.is_file(): continue
        cat=mapping.get(p.suffix.lower(),"unknown"); categories[cat].append({"path":str(p.relative_to(root)),"size":p.stat().st_size,"sha256":sha256_file(p)})
    report={"schema_version":1,"kind":"asset_inventory_report","created_at":utc_now(),"root":str(root.resolve()),"counts":{k:len(v) for k,v in categories.items()},"categories":categories}
    if output: write_json(output, report)
    return report


def mod_branch_init(project: Path, name: str, *, baseline: Path, output: Path | None = None) -> dict[str, Any]:
    manifest={"schema_version":1,"kind":"mod_branch_manifest","created_at":utc_now(),"name":name,"baseline_report":str(baseline.resolve()),"baseline_sha256":sha256_file(baseline),"intentional_diffs":[],"required_validation":["functional","integration"],"matching_required_for_changed_functions":False}
    out=output or project.resolve()/"mods"/name/"mod-branch.json"; out.parent.mkdir(parents=True,exist_ok=True); write_json(out,manifest)
    return {"schema_version":1,"kind":"mod_branch_init_report","manifest":str(out),"name":name}


def regression_compare(baseline: Path, modded: Path, *, allow: Path | None = None, output: Path | None = None) -> dict[str, Any]:
    allowed=load_json(allow) if allow and allow.is_file() else {"intentional_diffs":[]}
    report={"schema_version":1,"kind":"regression_compare_report","created_at":utc_now(),"baseline":str(baseline.resolve()),"modded":str(modded.resolve()),"allowance":allowed,"claim":"manifest_comparison_scaffold_only"}
    if output: write_json(output, report)
    return report


# ---- v0.7.8 universal decompilation acceleration layer ----

_COMMON_PROLOGUES: dict[str, list[bytes]] = {
    "x86": [bytes.fromhex("55 8B EC"), bytes.fromhex("55 89 E5"), bytes.fromhex("56 8B F1"), bytes.fromhex("53 56 57")],
    "x86_64": [bytes.fromhex("40 55"), bytes.fromhex("48 89 5C 24"), bytes.fromhex("48 83 EC")],
}

_ASSET_HINTS = {
    "audio": ("wav", "mp3", "ogg", "miles", "ail", "dsound", "sound", "music"),
    "video": ("bink", "smk", "avi", "movie", "video"),
    "render": ("d3d", "directdraw", "opengl", "shader", "texture", "mesh"),
    "input": ("dinput", "keyboard", "mouse", "joystick", "controller"),
    "network": ("winsock", "socket", "packet", "server", "client", "udp", "tcp"),
    "resource": ("resource", "archive", "pak", "rfa", "asset", "load"),
    "physics": ("physics", "collision", "rigid", "velocity", "accel"),
    "ai": ("ai", "path", "nav", "goal", "behavior", "state"),
}

_SIMPLE_PATTERN_CATALOG = [
    {"id": "x86-return-zero", "architecture": "x86", "hex": "33 C0 C3", "source_template": "int {symbol}(void) {{ return 0; }}", "classification": "return_constant"},
    {"id": "x86-ret", "architecture": "x86", "hex": "C3", "source_template": "void {symbol}(void) {{ }}", "classification": "empty_return"},
    {"id": "x86-frame-ret", "architecture": "x86", "hex": "55 8B EC 5D C3", "source_template": "void {symbol}(void) {{ }}", "classification": "empty_frame_return"},
    {"id": "x86-return-one", "architecture": "x86", "hex": "B8 01 00 00 00 C3", "source_template": "int {symbol}(void) {{ return 1; }}", "classification": "return_constant"},
]


def _json_out(path: Path | None, value: dict[str, Any]) -> dict[str, Any]:
    if path is not None:
        write_json(path, value)
    return value


def _read_any_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except UnicodeDecodeError:
        return ""


def _file_report(path: Path, root: Path | None = None) -> dict[str, Any]:
    rel = str(path if root is None else path.relative_to(root))
    return {"path": rel, "size": path.stat().st_size, "sha256": sha256_file(path)}


def function_discover(image: Path, *, output: Path | None = None, profile: str = "prologue", architecture: str = "x86", min_size: int = 1, max_size: int = 1048576, align: int = 1) -> dict[str, Any]:
    """Discover candidate function entry offsets using architecture profiles.

    The command is deliberately generic: profile names describe the heuristic, not
    a compiler or game. It reports candidates and confidence, but never asserts
    complete function coverage or authoritative boundaries.
    """
    if profile not in {"prologue", "ret-boundary"}:
        raise ContractError("profile must be 'prologue' or 'ret-boundary'")
    if architecture not in _COMMON_PROLOGUES:
        raise ContractError("architecture must be x86 or x86_64")
    data = image.read_bytes()
    prologues = _COMMON_PROLOGUES[architecture]
    candidates: list[dict[str, Any]] = []
    for index in range(0, len(data)):
        if align > 1 and index % align != 0:
            continue
        matched = next((p for p in prologues if data.startswith(p, index)), None)
        if matched is None:
            continue
        end = None
        if profile == "ret-boundary":
            for off in range(index + len(matched), min(len(data), index + max_size)):
                if data[off] in {0xC3, 0xC2, 0xCC}:
                    end = off + 1
                    break
        size = None if end is None else end - index
        if size is not None and size < min_size:
            continue
        candidates.append({
            "offset": index,
            "rva": index,
            "function_id": function_id_from_rva(index),
            "matched_prologue_hex": matched.hex(),
            "estimated_end_offset": end,
            "estimated_size": size,
            "confidence": "medium" if end is not None else "low",
            "claim": "heuristic_entry_candidate_not_authoritative_boundary",
        })
    report = {"schema_version": 1, "kind": "function_discovery_report", "created_at": utc_now(), "image": str(image.resolve()), "image_sha256": sha256_file(image), "profile": profile, "architecture": architecture, "candidate_count": len(candidates), "candidates": candidates}
    return _json_out(output, report)


def function_boundary_reconcile(reports: list[Path], *, output: Path | None = None) -> dict[str, Any]:
    entries: dict[str, dict[str, Any]] = {}
    conflicts: list[dict[str, Any]] = []
    for report_path in reports:
        report = load_json(report_path)
        for item in report.get("candidates", []):
            fid = item.get("function_id") or function_id_from_rva(int(item.get("rva", item.get("offset", 0))))
            key = str(fid)
            prior = entries.get(key)
            record = {"source_report": str(report_path), **item}
            if prior is not None:
                if prior.get("estimated_end_offset") != item.get("estimated_end_offset"):
                    conflicts.append({"function_id": key, "left": prior, "right": record, "reason": "estimated_end_disagreement"})
                prior.setdefault("sources", []).append(str(report_path))
            else:
                record["sources"] = [str(report_path)]
                entries[key] = record
    reconciled = sorted(entries.values(), key=lambda r: int(r.get("rva", r.get("offset", 0))))
    report = {"schema_version": 1, "kind": "function_boundary_reconciliation_report", "created_at": utc_now(), "function_count": len(reconciled), "conflict_count": len(conflicts), "functions": reconciled, "conflicts": conflicts, "claim": "reconciled_candidates_not_final_boundaries"}
    return _json_out(output, report)


def function_list_sort(functions_json: Path, *, output: Path | None = None, key: str = "rva") -> dict[str, Any]:
    data = load_json(functions_json)
    items = data if isinstance(data, list) else (data.get("functions") or data.get("candidates") or [])
    if not isinstance(items, list):
        raise ContractError("function list must be an array or contain functions/candidates")
    if key not in {"rva", "offset", "estimated_size", "function_id"}:
        raise ContractError("unsupported sort key")
    def sort_key(item: Any) -> Any:
        if not isinstance(item, dict):
            return 0
        value = item.get(key)
        if value is None:
            return -1 if key != "function_id" else ""
        return value
    sorted_items = sorted(items, key=sort_key)
    report = {"schema_version": 1, "kind": "function_list_sort_report", "created_at": utc_now(), "key": key, "count": len(sorted_items), "functions": sorted_items}
    return _json_out(output, report)


def function_list_classify(functions_json: Path, *, output: Path | None = None) -> dict[str, Any]:
    data = load_json(functions_json)
    items = data if isinstance(data, list) else (data.get("functions") or data.get("candidates") or [])
    classes: dict[str, list[dict[str, Any]]] = {"tiny": [], "small": [], "medium": [], "large": [], "unknown": []}
    for item in items:
        if not isinstance(item, dict):
            continue
        size = item.get("estimated_size") or item.get("size")
        if size is None:
            bucket = "unknown"
        elif int(size) <= 8:
            bucket = "tiny"
        elif int(size) <= 64:
            bucket = "small"
        elif int(size) <= 512:
            bucket = "medium"
        else:
            bucket = "large"
        classes[bucket].append(item)
    report = {"schema_version": 1, "kind": "function_list_classification_report", "created_at": utc_now(), "counts": {k: len(v) for k, v in classes.items()}, "classes": classes}
    return _json_out(output, report)


def pattern_catalog(*, output: Path | None = None) -> dict[str, Any]:
    report = {"schema_version": 1, "kind": "pattern_catalog", "created_at": utc_now(), "patterns": _SIMPLE_PATTERN_CATALOG, "acceptance_rule": "generated candidates require compiler/matcher verification before promotion"}
    return _json_out(output, report)


def pattern_scan(root: Path, *, output: Path | None = None, architecture: str | None = None) -> dict[str, Any]:
    if root.is_file():
        files = [root]
        scan_root = root.parent
    else:
        files = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".bin", ".bytes", ".text"})
        scan_root = root
    hits: list[dict[str, Any]] = []
    for file in files:
        data = file.read_bytes()
        for pat in _SIMPLE_PATTERN_CATALOG:
            if architecture and pat["architecture"] != architecture:
                continue
            needle = bytes.fromhex(pat["hex"])
            start = 0
            while True:
                idx = data.find(needle, start)
                if idx < 0:
                    break
                hits.append({"path": str(file.relative_to(scan_root)), "offset": idx, "pattern_id": pat["id"], "classification": pat["classification"], "size": len(needle), "claim": "byte_pattern_hit_requires_compile_match"})
                start = idx + 1
    report = {"schema_version": 1, "kind": "pattern_scan_report", "created_at": utc_now(), "root": str(root.resolve()), "hit_count": len(hits), "hits": hits}
    return _json_out(output, report)


def pattern_generate(scan_report: Path, output: Path, *, symbol_prefix: str = "sub") -> dict[str, Any]:
    scan = load_json(scan_report)
    output.mkdir(parents=True, exist_ok=True)
    pattern_by_id = {p["id"]: p for p in _SIMPLE_PATTERN_CATALOG}
    generated: list[dict[str, Any]] = []
    for hit in scan.get("hits", []):
        pat = pattern_by_id.get(hit.get("pattern_id"))
        if pat is None:
            continue
        symbol = f"{symbol_prefix}_{int(hit.get('offset', 0)):08x}"
        source = pat["source_template"].format(symbol=symbol) + "\n"
        path = output / f"{symbol}.c"
        path.write_text(source, encoding="utf-8")
        generated.append({"hit": hit, "source": str(path), "source_sha256": sha256_file(path), "symbol": symbol, "claim": "pattern_candidate_unvalidated"})
    report = {"schema_version": 1, "kind": "pattern_generation_report", "created_at": utc_now(), "generated_count": len(generated), "generated": generated}
    write_json(output / "pattern-generation-report.json", report)
    return report


def pattern_match(generation_report: Path, *, output: Path | None = None) -> dict[str, Any]:
    data = load_json(generation_report)
    results = []
    for item in data.get("generated", []):
        source = Path(item["source"])
        results.append({"source": str(source), "source_sha256": sha256_file(source), "status": "candidate_generated", "accepted": False, "required_next_step": "compile and compare with diff-function or local-LLM match loop"})
    report = {"schema_version": 1, "kind": "pattern_match_triage_report", "created_at": utc_now(), "result_count": len(results), "results": results, "claim": "triage_only_no_byte_match_claimed"}
    return _json_out(output, report)


def pattern_promote(project: Path, function_id: str, candidate: Path, report: Path, *, stage: str = "pattern", output: Path | None = None, overwrite: bool = False) -> dict[str, Any]:
    promoted = candidate_promote(project, function_id, candidate, report, stage=stage, overwrite=overwrite)
    if output:
        write_json(output, promoted)
    return promoted


def image_text_compose(project: Path, output: Path, *, function_list: Path | None = None, fallback_byte: int = 0xCC) -> dict[str, Any]:
    project = project.resolve()
    records: list[dict[str, Any]] = []
    if function_list is not None:
        data = load_json(function_list)
        records = data.get("functions") or data.get("candidates") or data
    else:
        functions = project / "functions"
        for manifest in sorted(functions.glob("*/function.json")) if functions.is_dir() else []:
            item = load_json(manifest)
            ranges = item.get("body_ranges", [])
            if ranges:
                first = ranges[0]
                records.append({"function_id": item.get("id", manifest.parent.name), "rva": first.get("start_rva", 0), "size": first.get("size", first.get("end_rva", 0) - first.get("start_rva", 0)), "artifact_dir": str(manifest.parent)})
    if not isinstance(records, list):
        raise ContractError("function records must be a list")
    pieces = bytearray()
    composed: list[dict[str, Any]] = []
    cursor = 0
    for raw in sorted(records, key=lambda x: int(x.get("rva", x.get("offset", 0))) if isinstance(x, dict) else 0):
        if not isinstance(raw, dict):
            continue
        rva = int(raw.get("rva", raw.get("offset", cursor)))
        size = int(raw.get("size") or raw.get("estimated_size") or 0)
        if size < 0:
            raise ContractError("function size must not be negative")
        if rva > cursor:
            pieces.extend(bytes([fallback_byte]) * (rva - cursor))
            cursor = rva
        payload = None
        artifact_dir = raw.get("artifact_dir")
        if artifact_dir:
            p = Path(artifact_dir) / "ranges" / "00.bin"
            if p.is_file():
                payload = p.read_bytes()
        if payload is None:
            payload = bytes([fallback_byte]) * size
        pieces.extend(payload)
        cursor += len(payload)
        composed.append({"function_id": raw.get("function_id"), "rva": rva, "size": len(payload), "source": "artifact_range" if artifact_dir else "fallback_fill"})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(bytes(pieces))
    report = {"schema_version": 1, "kind": "image_text_compose_report", "created_at": utc_now(), "output": str(output.resolve()), "output_sha256": sha256_file(output), "size": output.stat().st_size, "composed": composed, "claim": "section_blob_composed_from_declared_records"}
    write_json(output.with_suffix(output.suffix + ".compose.json"), report)
    return report


def _pe_section(data: bytes, section_name: str) -> dict[str, Any]:
    if len(data) < 0x40 or data[:2] != b"MZ":
        raise ContractError("not a PE image")
    pe = int.from_bytes(data[0x3C:0x40], "little")
    if pe + 24 > len(data) or data[pe:pe+4] != b"PE\0\0":
        raise ContractError("invalid PE signature")
    section_count = int.from_bytes(data[pe+6:pe+8], "little")
    optional_size = int.from_bytes(data[pe+20:pe+22], "little")
    table = pe + 24 + optional_size
    for idx in range(section_count):
        off = table + idx * 40
        name = data[off:off+8].split(b"\0", 1)[0].decode("ascii", errors="replace")
        if name == section_name:
            virtual_size = int.from_bytes(data[off+8:off+12], "little")
            virtual_address = int.from_bytes(data[off+12:off+16], "little")
            raw_size = int.from_bytes(data[off+16:off+20], "little")
            raw_offset = int.from_bytes(data[off+20:off+24], "little")
            return {"index": idx, "name": name, "virtual_size": virtual_size, "virtual_address": virtual_address, "raw_size": raw_size, "raw_offset": raw_offset}
    raise ContractError(f"PE section not found: {section_name}")


def text_swap_plan(original: Path, replacement: Path, output: Path, *, section_name: str = ".text") -> dict[str, Any]:
    original_data = original.read_bytes()
    repl = replacement.read_bytes()
    section = _pe_section(original_data, section_name)
    if len(repl) > section["raw_size"]:
        raise ContractError("replacement section exceeds original raw allocation")
    plan = {"schema_version": 1, "kind": "text_swap_plan", "created_at": utc_now(), "original": str(original.resolve()), "original_sha256": sha256_file(original), "replacement": str(replacement.resolve()), "replacement_sha256": sha256_file(replacement), "section": section, "output": str(output.resolve()), "claim": "container_preserving_section_replacement_plan"}
    write_json(output, plan)
    return plan


def text_swap_inject(plan: Path, *, output: Path | None = None) -> dict[str, Any]:
    p = load_json(plan)
    original = Path(p["original"])
    replacement = Path(p["replacement"])
    if sha256_file(original) != p["original_sha256"]:
        raise ContractError("original image hash differs from plan")
    if sha256_file(replacement) != p["replacement_sha256"]:
        raise ContractError("replacement hash differs from plan")
    data = bytearray(original.read_bytes())
    section = p["section"]
    repl = replacement.read_bytes()
    raw_offset = int(section["raw_offset"]); raw_size = int(section["raw_size"])
    original_section = bytes(data[raw_offset:raw_offset+raw_size])
    full = repl + original_section[len(repl):]
    data[raw_offset:raw_offset+raw_size] = full
    out = output or Path(p["output"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(bytes(data))
    report = {"schema_version": 1, "kind": "text_swap_inject_report", "created_at": utc_now(), "plan": str(plan.resolve()), "output": str(out.resolve()), "output_sha256": sha256_file(out), "size_preserved": out.stat().st_size == original.stat().st_size, "section": section["name"]}
    write_json(out.with_suffix(out.suffix + ".text-swap.json"), report)
    return report


def text_swap_verify(plan: Path, image: Path, *, output: Path | None = None) -> dict[str, Any]:
    p = load_json(plan)
    section = p["section"]
    image_data = image.read_bytes()
    repl = Path(p["replacement"]).read_bytes()
    actual = image_data[int(section["raw_offset"]):int(section["raw_offset"])+len(repl)]
    valid = actual == repl
    report = {"schema_version": 1, "kind": "text_swap_verify_report", "created_at": utc_now(), "valid": valid, "image": str(image.resolve()), "image_sha256": sha256_file(image), "checked_size": len(repl), "section": section["name"], "errors": [] if valid else ["replacement bytes not present at planned section offset"]}
    return _json_out(output, report)


def text_swap_build(project: Path, replacement: Path, output: Path, *, original: Path, section_name: str = ".text") -> dict[str, Any]:
    plan_path = output.with_suffix(output.suffix + ".plan.json")
    plan = text_swap_plan(original, replacement, plan_path, section_name=section_name)
    inject = text_swap_inject(plan_path, output=output)
    verify = text_swap_verify(plan_path, output)
    return {"schema_version": 1, "kind": "text_swap_build_report", "created_at": utc_now(), "plan": plan, "inject": inject, "verify": verify}


def progress_reconcile(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    project = project.resolve()
    workflow_files = sorted((project / "state" / "workflows").glob("*.json")) if (project / "state" / "workflows").is_dir() else sorted(project.glob("**/workflow.json"))
    source_files = sorted(p for p in (project / "src").rglob("*") if p.is_file() and p.suffix.lower() in {".c", ".cc", ".cpp", ".s", ".asm"}) if (project / "src").is_dir() else []
    by_status: dict[str, int] = {}
    inconsistencies: list[str] = []
    for p in workflow_files:
        try:
            data = load_json(p)
        except Exception as exc:
            inconsistencies.append(f"unreadable workflow {p}: {exc}")
            continue
        status = data.get("matching_status") or data.get("matching", {}).get("state") or "unknown"
        by_status[str(status)] = by_status.get(str(status), 0) + 1
    stages = source_stage_classify(project)["counts"]
    report = {"schema_version": 1, "kind": "progress_reconciliation_report", "created_at": utc_now(), "workflow_file_count": len(workflow_files), "source_file_count": len(source_files), "matching_status_counts": by_status, "source_stage_counts": stages, "inconsistencies": inconsistencies, "claim": "project_accounting_report"}
    return _json_out(output, report)


def project_health(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    progress = progress_reconcile(project)
    errors = list(progress.get("inconsistencies", []))
    warnings: list[str] = []
    if progress["workflow_file_count"] == 0:
        warnings.append("no workflow files found")
    if progress["source_file_count"] == 0:
        warnings.append("no source files found")
    report = {"schema_version": 1, "kind": "project_health_report", "created_at": utc_now(), "healthy": not errors, "warnings": warnings, "errors": errors, "progress": progress}
    return _json_out(output, report)


def source_stage_classify(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    root = project.resolve() / "src"
    rules = [
        ("assembly_fallback", ("asm", "fallback")),
        ("naked_byte_wrapper", ("byte", "wrapper", "naked")),
        ("pattern_generated_source", ("pattern",)),
        ("llm_generated_source", ("llm",)),
        ("human_reviewed_source", ("reviewed", "matched", "accepted")),
    ]
    records: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    if root.is_dir():
        for p in sorted(f for f in root.rglob("*") if f.is_file() and f.suffix.lower() in {".c", ".cc", ".cpp", ".h", ".hpp", ".s", ".asm"}):
            rel = p.relative_to(root).as_posix().lower()
            text = _read_any_text(p).lower()[:4096]
            stage = "unknown_source"
            for candidate, hints in rules:
                if any(h in rel or h in text for h in hints):
                    stage = candidate; break
            if p.suffix.lower() in {".s", ".asm"}:
                stage = "assembly_fallback"
            counts[stage] = counts.get(stage, 0) + 1
            records.append({"path": str(p.relative_to(project)), "stage": stage, "sha256": sha256_file(p)})
    report = {"schema_version": 1, "kind": "source_stage_classification_report", "created_at": utc_now(), "counts": counts, "files": records}
    return _json_out(output, report)


def ghidra_mcp_probe(url: str, *, output: Path | None = None, timeout: float = 5.0) -> dict[str, Any]:
    req = urllib.request.Request(url, method="GET")
    status = None; error = None
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            status = response.status
    except Exception as exc:
        error = str(exc)
    report = {"schema_version": 1, "kind": "ghidra_mcp_probe_report", "created_at": utc_now(), "url": url, "reachable": error is None, "status": status, "error": error}
    return _json_out(output, report)


def _json_rpc(url: str, method: str, params: dict[str, Any] | None, timeout: float) -> dict[str, Any]:
    payload = json.dumps({"jsonrpc": "2.0", "id": "x86decomp", "method": method, "params": params or {}}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def ghidra_mcp_functions(url: str, *, output: Path | None = None, timeout: float = 30.0) -> dict[str, Any]:
    result = _json_rpc(url, "list_functions", {}, timeout)
    report = {"schema_version": 1, "kind": "ghidra_mcp_functions_report", "created_at": utc_now(), "url": url, "response": result}
    return _json_out(output, report)


def ghidra_mcp_decompile(url: str, address: str, *, output: Path | None = None, timeout: float = 60.0) -> dict[str, Any]:
    result = _json_rpc(url, "decompile", {"address": address}, timeout)
    report = {"schema_version": 1, "kind": "ghidra_mcp_decompile_report", "created_at": utc_now(), "url": url, "address": address, "response": result, "claim": "mcp_response_captured_unverified"}
    return _json_out(output, report)


def ghidra_mcp_batch_decompile(url: str, addresses: Path, output: Path, *, timeout: float = 60.0) -> dict[str, Any]:
    raw = load_json(addresses)
    if not isinstance(raw, list):
        raise ContractError("addresses file must be a JSON array")
    output.mkdir(parents=True, exist_ok=True)
    results = []
    for address in raw:
        report = ghidra_mcp_decompile(url, str(address), output=output / f"{str(address).replace(':','_').replace('/','_')}.json", timeout=timeout)
        results.append({"address": str(address), "report": report})
    summary = {"schema_version": 1, "kind": "ghidra_mcp_batch_decompile_report", "created_at": utc_now(), "count": len(results), "results": results}
    write_json(output / "batch-decompile-report.json", summary)
    return summary


def ghidra_mcp_sync_names(project: Path, names_json: Path, *, output: Path | None = None) -> dict[str, Any]:
    names = load_json(names_json)
    if not isinstance(names, dict):
        raise ContractError("names JSON must map function IDs or RVAs to names")
    manifest = project.resolve() / "reconstruction" / "ghidra-name-sync.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    write_json(manifest, {"schema_version": 1, "created_at": utc_now(), "names": names, "claim": "name_observations_not_original_source_proof"})
    report = {"schema_version": 1, "kind": "ghidra_mcp_name_sync_report", "created_at": utc_now(), "manifest": str(manifest), "name_count": len(names)}
    return _json_out(output, report)


def compiler_rule_learn(rule_id: str, observations: Path, output: Path) -> dict[str, Any]:
    data = load_json(observations)
    if not isinstance(data, (dict, list)):
        raise ContractError("observations must be JSON object or array")
    report = {"schema_version": 1, "kind": "compiler_rule_record", "created_at": utc_now(), "rule_id": rule_id, "observations": data, "claim": "empirical_rule_requires_project_corroboration"}
    write_json(output, report)
    return report


def compiler_rule_report(rules: list[Path], *, output: Path | None = None) -> dict[str, Any]:
    loaded = [load_json(p) for p in rules]
    report = {"schema_version": 1, "kind": "compiler_rule_report", "created_at": utc_now(), "rule_count": len(loaded), "rules": loaded}
    return _json_out(output, report)


def compiler_compare_flags(reports: list[Path], *, output: Path | None = None) -> dict[str, Any]:
    loaded = [load_json(p) for p in reports]
    rows = []
    for report in loaded:
        rows.append({"path": report.get("profile") or report.get("compiler_profile") or "unknown", "status": report.get("status"), "equal": report.get("equal"), "byte_matched": report.get("byte_matched")})
    result = {"schema_version": 1, "kind": "compiler_flag_comparison_report", "created_at": utc_now(), "rows": rows, "claim": "comparison_of_reported_results_only"}
    return _json_out(output, result)


def runtime_identify(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    root = project.resolve()
    hits = []
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".json", ".txt", ".asm", ".c", ".cpp", ".h", ".hpp"}:
            text = _read_any_text(p).lower()
            for runtime in ("msvcrt", "libc", "crt", "bink", "miles", "ail", "directsound", "directx", "d3d", "opengl"):
                if runtime in text:
                    hits.append({"path": str(p.relative_to(root)), "runtime_hint": runtime})
    report = {"schema_version": 1, "kind": "runtime_identification_report", "created_at": utc_now(), "hit_count": len(hits), "hits": hits, "claim": "string_and_metadata_hints_only"}
    return _json_out(output, report)


def runtime_quarantine(project: Path, identification_report: Path, *, output: Path | None = None) -> dict[str, Any]:
    data = load_json(identification_report)
    manifest = project.resolve() / "reconstruction" / "runtime-quarantine.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    hits = data.get("hits", [])
    write_json(manifest, {"schema_version": 1, "created_at": utc_now(), "runtime_candidates": hits, "policy": "exclude_from_human_game_code_progress_until_reviewed"})
    report = {"schema_version": 1, "kind": "runtime_quarantine_report", "created_at": utc_now(), "manifest": str(manifest), "candidate_count": len(hits)}
    return _json_out(output, report)


def runtime_match_library(project: Path, library_inventory: Path, *, output: Path | None = None) -> dict[str, Any]:
    inv = load_json(library_inventory)
    report = {"schema_version": 1, "kind": "runtime_library_match_report", "created_at": utc_now(), "inventory": inv, "claim": "library_match_candidates_require_review"}
    return _json_out(output, report)


def subsystem_detect(root: Path, *, output: Path | None = None) -> dict[str, Any]:
    scores = {key: [] for key in _ASSET_HINTS}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        hay = (str(p.relative_to(root)) + "\n" + (_read_any_text(p)[:4096] if p.suffix.lower() in {".txt", ".json", ".c", ".cpp", ".h", ".hpp", ".asm", ".ini", ".cfg"} else "")).lower()
        for name, hints in _ASSET_HINTS.items():
            matched = [h for h in hints if h in hay]
            if matched:
                scores[name].append({"path": str(p.relative_to(root)), "hints": matched[:5]})
    report = {"schema_version": 1, "kind": "subsystem_detection_report", "created_at": utc_now(), "subsystems": [{"name": k, "evidence_count": len(v), "evidence": v[:100]} for k, v in scores.items() if v], "claim": "subsystem_hints_only"}
    return _json_out(output, report)


def state_machine_detect(root: Path, *, output: Path | None = None) -> dict[str, Any]:
    candidates = []
    terms = ("state", "transition", "enter", "exit", "update", "callback")
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".c", ".cpp", ".h", ".hpp", ".asm", ".json", ".txt"}:
            text = _read_any_text(p).lower()
            matched = [t for t in terms if t in text]
            if len(matched) >= 2:
                candidates.append({"path": str(p.relative_to(root)), "matched_terms": matched})
    report = {"schema_version": 1, "kind": "state_machine_detection_report", "created_at": utc_now(), "candidate_count": len(candidates), "candidates": candidates, "claim": "pattern_candidates_require_human_review"}
    return _json_out(output, report)


def project_doctor_paths(root: Path, *, output: Path | None = None) -> dict[str, Any]:
    absolute = []
    drive_re = re.compile(r"[A-Za-z]:\\[^\s\"']+")
    unix_re = re.compile(r"(?<![\w.])/(?:home|mnt|opt|usr|Users)/[^\s\"']+")
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".py", ".ps1", ".sh", ".json", ".md", ".txt", ".yml", ".yaml", ".cmake", ".cfg", ".ini"}:
            text = _read_any_text(p)
            matches = drive_re.findall(text) + unix_re.findall(text)
            if matches:
                absolute.append({"path": str(p.relative_to(root)), "absolute_paths": sorted(set(matches))})
    report = {"schema_version": 1, "kind": "project_path_doctor_report", "created_at": utc_now(), "finding_count": len(absolute), "findings": absolute, "claim": "portability_findings_only"}
    return _json_out(output, report)


def script_port_audit(root: Path, *, output: Path | None = None) -> dict[str, Any]:
    findings = []
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".py", ".ps1", ".sh", ".bat", ".cmd"}:
            text = _read_any_text(p)
            markers = []
            if "D:\\" in text or "C:\\" in text: markers.append("windows_absolute_path")
            if "ghidra" in text.lower(): markers.append("ghidra_dependency")
            if "cl.exe" in text.lower() or "msvc" in text.lower(): markers.append("compiler_dependency")
            if markers:
                findings.append({"path": str(p.relative_to(root)), "markers": markers})
    report = {"schema_version": 1, "kind": "script_portability_audit_report", "created_at": utc_now(), "finding_count": len(findings), "findings": findings}
    return _json_out(output, report)


def toolchain_hash_tree(root: Path, output: Path) -> dict[str, Any]:
    files = [_file_report(p, root) for p in sorted(root.rglob("*")) if p.is_file()]
    manifest = {"schema_version": 1, "kind": "toolchain_hash_tree", "created_at": utc_now(), "root": str(root.resolve()), "files": files, "file_count": len(files), "redistribution_claimed": False}
    write_json(output, manifest)
    return manifest


def toolchain_verify_local(manifest: Path, *, output: Path | None = None) -> dict[str, Any]:
    data = load_json(manifest)
    root = Path(data["root"])
    failures = []
    for item in data.get("files", []):
        p = root / item["path"]
        if not p.is_file(): failures.append(f"missing: {item['path']}")
        elif sha256_file(p) != item["sha256"]: failures.append(f"hash mismatch: {item['path']}")
    report = {"schema_version": 1, "kind": "toolchain_local_verification_report", "created_at": utc_now(), "valid": not failures, "failures": failures, "checked_count": len(data.get("files", []))}
    return _json_out(output, report)


def toolchain_redact_package(root: Path, output: Path, *, manifest: Path | None = None) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for p in sorted(root.rglob("*")):
        if p.is_file():
            rel = p.relative_to(root)
            records.append({"path": str(rel), "size": p.stat().st_size, "sha256": sha256_file(p), "redacted": True})
    redacted_manifest = {"schema_version": 1, "kind": "toolchain_redacted_package_manifest", "created_at": utc_now(), "source_root": str(root.resolve()), "files": records, "instructions": "Install the toolchain locally and verify with the recorded hashes; binaries are intentionally not included."}
    write_json(output / "TOOLCHAIN_REDACTED_MANIFEST.json", redacted_manifest)
    if manifest is not None:
        write_json(output / "SOURCE_TOOLCHAIN_HASH_TREE.json", load_json(manifest))
    return {"schema_version": 1, "kind": "toolchain_redact_package_report", "output": str(output.resolve()), "redacted_file_count": len(records)}


def decompiler_cleanup(input_file: Path, output: Path, *, compiler: str = "generic", language: str = "cpp", locals_at_top: bool = False) -> dict[str, Any]:
    text = input_file.read_text(encoding="utf-8", errors="replace")
    replacements = {
        "undefined4": "uint32_t",
        "undefined2": "uint16_t",
        "undefined1": "uint8_t",
        "undefined8": "uint64_t",
        "undefined": "void",
    }
    changed = []
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new); changed.append({"from": old, "to": new})
    prefix = "#include <stdint.h>\n\n" if "uint" in text and "stdint.h" not in text else ""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(prefix + text, encoding="utf-8")
    report = {"schema_version": 1, "kind": "decompiler_cleanup_report", "created_at": utc_now(), "input": str(input_file.resolve()), "output": str(output.resolve()), "output_sha256": sha256_file(output), "compiler": compiler, "language": language, "locals_at_top_requested": locals_at_top, "replacements": changed, "claim": "syntax_cleanup_only_not_validated_source"}
    write_json(output.with_suffix(output.suffix + ".cleanup.json"), report)
    return report


def candidate_search(project: Path, *, output: Path | None = None, phases: list[str] | None = None) -> dict[str, Any]:
    phases = phases or ["recipe-patterns", "compiler-variants", "decompiler-cleanup", "llm", "human-queue"]
    if not set(phases).issubset({"recipe-patterns", "compiler-variants", "decompiler-cleanup", "llm", "human-queue"}):
        raise ContractError("unsupported candidate-search phase")
    steps = []
    for phase in phases:
        steps.append({"phase": phase, "status": "planned", "acceptance": "requires compile/match or functional validation report"})
    report = {"schema_version": 1, "kind": "candidate_search_plan", "created_at": utc_now(), "project": str(project.resolve()), "steps": steps, "claim": "ordered_candidate_search_plan_only"}
    return _json_out(output, report)


def release_goal_moddable_source(project: Path, *, output: Path | None = None) -> dict[str, Any]:
    stages = source_stage_classify(project)
    rejected = {k: v for k, v in stages["counts"].items() if k in {"assembly_fallback", "naked_byte_wrapper", "unknown_source"} and v}
    report = {"schema_version": 1, "kind": "moddable_source_goal_report", "created_at": utc_now(), "passed": not rejected, "rejected_stage_counts": rejected, "source_stage_counts": stages["counts"], "claim": "source_stage_policy_check_only"}
    return _json_out(output, report)
