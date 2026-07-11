"""Verify the current toolkit behavior covered by `tests/reconstruction/test_real_project_acceleration.py`."""
from __future__ import annotations

import json
import struct
from pathlib import Path

from x86decomp.reconstruction.acceleration import (
    candidate_search,
    compiler_compare_flags,
    compiler_rule_learn,
    decompiler_cleanup,
    function_boundary_reconcile,
    function_discover,
    function_list_classify,
    function_list_sort,
    image_text_compose,
    pattern_catalog,
    pattern_generate,
    pattern_match,
    pattern_scan,
    progress_reconcile,
    project_doctor_paths,
    project_health,
    release_goal_moddable_source,
    runtime_identify,
    script_port_audit,
    source_stage_classify,
    state_machine_detect,
    subsystem_detect,
    text_swap_build,
    toolchain_hash_tree,
    toolchain_redact_package,
    toolchain_verify_local,
)


def _minimal_pe(path: Path, text: bytes) -> None:
    """Write a minimal PE fixture containing the supplied text-section bytes."""
    data = bytearray(0x400 + len(text))
    data[:2] = b"MZ"
    struct.pack_into("<I", data, 0x3C, 0x80)
    data[0x80:0x84] = b"PE\0\0"
    struct.pack_into("<HHIIIHH", data, 0x84, 0x14C, 1, 0, 0, 0, 0xE0, 0x010F)
    optional = 0x98
    struct.pack_into("<H", data, optional, 0x10B)
    section = 0x80 + 24 + 0xE0
    data[section:section+8] = b".text\0\0\0"
    struct.pack_into("<IIIIIIHHI", data, section+8, len(text), 0x1000, len(text), 0x400, 0, 0, 0, 0, 0x60000020)
    data[0x400:0x400+len(text)] = text
    path.write_bytes(data)


def test_universal_function_pattern_and_text_swap(tmp_path: Path) -> None:
    """Verify universal function pattern and text swap behavior."""
    raw = tmp_path / "code.bin"
    raw.write_bytes(bytes.fromhex("55 8B EC 5D C3 33 C0 C3"))
    discovery = function_discover(raw, profile="ret-boundary", architecture="x86")
    assert discovery["candidate_count"] == 1
    rep = tmp_path / "disc.json"; rep.write_text(json.dumps(discovery), encoding="utf-8")
    reconciled = function_boundary_reconcile([rep])
    assert reconciled["function_count"] == 1
    fl = tmp_path / "functions.json"; fl.write_text(json.dumps(reconciled), encoding="utf-8")
    assert function_list_sort(fl)["count"] == 1
    assert function_list_classify(fl)["counts"]["tiny"] == 1

    scan = pattern_scan(raw)
    assert scan["hit_count"] >= 1
    scan_path = tmp_path / "scan.json"; scan_path.write_text(json.dumps(scan), encoding="utf-8")
    generated = pattern_generate(scan_path, tmp_path / "generated")
    assert generated["generated_count"] >= 1
    match = pattern_match(tmp_path / "generated" / "pattern-generation-report.json")
    assert match["results"]
    assert pattern_catalog()["patterns"]

    project = tmp_path / "project"; (project / "functions" / "pe-rva_00000000" / "ranges").mkdir(parents=True)
    (project / "functions" / "pe-rva_00000000" / "ranges" / "00.bin").write_bytes(b"\xC3")
    (project / "functions" / "pe-rva_00000000" / "function.json").write_text(json.dumps({"schema_version": 1, "id": "pe-rva:00000000", "body_ranges": [{"start_rva": 0, "end_rva": 1, "size": 1, "file": "ranges/00.bin"}]}), encoding="utf-8")
    composed = image_text_compose(project, tmp_path / "text.bin")
    assert composed["size"] == 1

    original = tmp_path / "orig.exe"; repl = tmp_path / "repl.bin"; out = tmp_path / "out.exe"
    _minimal_pe(original, b"ABCD")
    repl.write_bytes(b"WXYZ")
    swapped = text_swap_build(project, repl, out, original=original)
    assert swapped["verify"]["valid"] is True


def test_project_health_hygiene_runtime_and_policy(tmp_path: Path) -> None:
    """Verify project health hygiene runtime and policy behavior."""
    project = tmp_path / "project"; (project / "src" / "accepted").mkdir(parents=True)
    src = project / "src" / "accepted" / "pe-rva_00001000.cpp"
    src.write_text("// FUNCTION: GAME 0x00001000 pe-rva:00001000\nvoid f(){ /* DirectSound state transition update */ }\n", encoding="utf-8")
    assert source_stage_classify(project)["counts"]["human_reviewed_source"] == 1
    assert progress_reconcile(project)["source_file_count"] == 1
    assert project_health(project)["healthy"] is True
    assert release_goal_moddable_source(project)["passed"] is True
    assert runtime_identify(project)["hit_count"] >= 1
    assert subsystem_detect(project)["subsystems"]
    assert state_machine_detect(project)["candidate_count"] == 1
    assert candidate_search(project)["steps"]

    script = project / "run.ps1"; script.write_text(r"D:\game\ghidra\support\analyzeHeadless.bat cl.exe", encoding="utf-8")
    assert project_doctor_paths(project)["finding_count"] == 1
    assert script_port_audit(project)["finding_count"] == 1


def test_toolchain_rules_and_cleanup(tmp_path: Path) -> None:
    """Verify toolchain rules and cleanup behavior."""
    tool = tmp_path / "toolchain"; tool.mkdir(); (tool / "cl.exe").write_bytes(b"compiler")
    manifest = toolchain_hash_tree(tool, tmp_path / "toolchain.json")
    assert manifest["file_count"] == 1
    assert toolchain_verify_local(tmp_path / "toolchain.json")["valid"] is True
    redacted = toolchain_redact_package(tool, tmp_path / "redacted", manifest=tmp_path / "toolchain.json")
    assert redacted["redacted_file_count"] == 1

    obs = tmp_path / "obs.json"; obs.write_text(json.dumps({"if_gt_zero": "JBE"}), encoding="utf-8")
    rule = compiler_rule_learn("branch-condition", obs, tmp_path / "rule.json")
    assert rule["rule_id"] == "branch-condition"
    assert compiler_compare_flags([tmp_path / "rule.json"])["rows"]

    decomp = tmp_path / "decompiler.c"; decomp.write_text("undefined4 f(undefined1 x){return x;}", encoding="utf-8")
    clean = decompiler_cleanup(decomp, tmp_path / "clean.c")
    assert clean["replacements"]
