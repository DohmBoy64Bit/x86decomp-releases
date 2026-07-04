from __future__ import annotations

import json
from pathlib import Path

from pe_fixture import build_minimal_pe32
from x86decomp.native import cli as native_cli
from x86decomp.native.closed_loop import ClosedLoop
from x86decomp.native.hybrid_composer import HybridComposer
from x86decomp.native.matching import FunctionMatching
from x86decomp.native.pe_reconstruction import PEReconstruction
from x86decomp.native.slots import FunctionSlots, inventory_from_project
from x86decomp.native.store import NativeStore
from x86decomp.native.windows_tools import WindowsTools


def test_native_cli_json_helpers(tmp_path: Path) -> None:
    data = tmp_path / "input.json"
    data.write_text('{"value": 7}', encoding="utf-8")
    assert native_cli._json(None, [1]) == [1]
    assert native_cli._json('[2]', []) == [2]
    assert native_cli._json_file(str(data)) == {"value": 7}


def test_project_inventory_audit_pe_inventory_reports_and_doctor(tmp_path: Path) -> None:
    image = build_minimal_pe32(tmp_path / "target.exe", b"\x55\xc3\xcc\xcc")
    artifact = tmp_path / "artifacts"
    function_dir = artifact / "functions" / "pe-rva_00001000"
    function_dir.mkdir(parents=True)
    (function_dir / "body.bin").write_bytes(b"\x55\xc3")
    (function_dir / "function.json").write_text(json.dumps({
        "id": "entry",
        "entry_rva": "0x1000",
        "body_ranges": [{"file": "body.bin", "size": 2}],
    }), encoding="utf-8")
    inventory = inventory_from_project(artifact)
    assert inventory[0]["body_size"] == 2
    store = NativeStore(tmp_path / "project")
    audit = FunctionSlots(store).audit_project(artifact, image)
    assert audit["function_count"] == 1
    pe_info = PEReconstruction(store).inventory(image)
    assert pe_info["entry_rva"] == 0x1000
    doctor = WindowsTools(store).doctor(ghidra_home=tmp_path / "missing-ghidra")
    assert "tools" in doctor and any(item["tool_name"] == "ghidra" for item in doctor["tools"])


def test_native_list_and_verify_paths(tmp_path: Path) -> None:
    import sys

    image = build_minimal_pe32(tmp_path / "target.exe", b"\x55\xc3")
    candidate = tmp_path / "candidate.bin"
    candidate.write_bytes(b"\x55\xc3")
    store = NativeStore(tmp_path / "project")
    run = FunctionMatching(store).batch(image, [{
        "function_id": "entry", "rva": 0x1000, "slot_size": 2, "candidate_path": str(candidate)
    }])
    composition = HybridComposer(store).compose(run["run_id"], tmp_path / "hybrid.exe")
    assert HybridComposer(store).verify(composition["composition_id"])["passed"]

    source = tmp_path / "source.c"
    source.write_text("int f(void){return 0;}", encoding="utf-8")
    loop_candidate = tmp_path / "loop.bin"
    command = [sys.executable, "-c", f"from pathlib import Path; Path(r'{loop_candidate}').write_bytes(bytes.fromhex('55c3'))"]
    loop = ClosedLoop(store)
    loop.run("entry", source, command, loop_candidate, image, 0x1000, 2, execute=True)
    assert len(loop.list()) == 1
