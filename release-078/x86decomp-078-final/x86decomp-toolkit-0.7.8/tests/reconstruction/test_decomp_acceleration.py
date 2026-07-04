from __future__ import annotations

import json
from pathlib import Path

from x86decomp.reconstruction.acceleration import (
    asset_inventory,
    candidate_promote,
    llm_job_from_function_packet,
    llm_job_from_range,
    module_assign,
    playability_smoke_plan,
    source_map_annotate,
    source_map_verify,
    triage_next,
)


def _packet(tmp_path: Path) -> Path:
    d = tmp_path / "packet"
    (d / "ranges").mkdir(parents=True)
    (d / "ranges" / "00.bin").write_bytes(b"\x55\x8b\xec\xc3")
    (d / "function.json").write_text(json.dumps({
        "schema_version": 1,
        "id": "pe-rva:00001000",
        "body_ranges": [{"start_rva": 0x1000, "end_rva": 0x1004, "size": 4, "file": "ranges/00.bin"}],
        "abi": {"calling_convention": "cdecl"},
    }), encoding="utf-8")
    (d / "listing.asm").write_text("push ebp\nmov ebp, esp\nret\n", encoding="utf-8")
    return d


def test_llm_job_create_and_range(tmp_path: Path) -> None:
    packet = _packet(tmp_path)
    report = llm_job_from_function_packet(packet, tmp_path / "jobs" / "f.json", architecture="x86")
    assert report["eligible"] is True
    job = json.loads((tmp_path / "jobs" / "f.json").read_text(encoding="utf-8"))
    assert job["base_rva"] == 0x1000
    assert (tmp_path / "jobs" / "f.bin").read_bytes() == b"\x55\x8b\xec\xc3"

    raw = tmp_path / "raw.bin"
    raw.write_bytes(b"ABCDEF")
    r = llm_job_from_range(raw, tmp_path / "range" / "r.json", rva=1, size=3, architecture="x86", function_name="sub_1")
    assert r["target_size"] == 3
    assert (tmp_path / "range" / "r.bin").read_bytes() == b"BCD"


def test_source_map_and_candidate_promotion(tmp_path: Path) -> None:
    project = tmp_path / "project"
    src = project / "src" / "matched"
    src.mkdir(parents=True)
    c = src / "pe-rva_00001000.c"
    c.write_text("int sub_00001000(void) { return 0; }\n", encoding="utf-8")
    annotated = source_map_annotate(project, src)
    assert annotated["changed_count"] == 1
    verified = source_map_verify(project, src)
    assert verified["valid"] is True

    report = tmp_path / "match.json"
    report.write_text(json.dumps({"status": "accepted", "accepted": {"path": str(c)}}), encoding="utf-8")
    promoted = candidate_promote(project, "pe-rva:00001000", c, report, stage="accepted", overwrite=True)
    assert Path(promoted["accepted_source"]).is_file()


def test_planning_helpers(tmp_path: Path) -> None:
    project = tmp_path / "project"
    (project / "functions" / "pe-rva_00001000").mkdir(parents=True)
    (project / "functions" / "pe-rva_00001000" / "function.json").write_text(json.dumps({
        "schema_version": 1,
        "id": "pe-rva:00001000",
        "body_ranges": [{"start_rva": 0x1000, "end_rva": 0x1001}],
    }), encoding="utf-8")
    assert module_assign(project, "pe-rva:00001000", module="Gameplay", class_name="Player", header="include/Player.hpp", source="src/Player.cpp")["assignment"]["module"] == "Gameplay"
    assert triage_next(project, goal="playable", limit=5)["candidate_function_ids"] == ["pe-rva:00001000"]
    target = tmp_path / "game.exe"; target.write_bytes(b"MZ")
    assert playability_smoke_plan(project, target, tmp_path / "smoke")["checks"]
    asset_root = tmp_path / "assets"; asset_root.mkdir(); (asset_root / "sound.wav").write_bytes(b"RIFF")
    inv = asset_inventory(asset_root)
    assert inv["counts"]["audio"] == 1
