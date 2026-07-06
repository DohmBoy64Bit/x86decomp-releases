"""Provide the installed test-suite implementation for the `x86decomp_testkit.toolkit_tests.test_public_api_contract` module."""
from __future__ import annotations

import importlib.util
import json
import stat
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from x86decomp.abi import ABIContract, load_abi_contract
from x86decomp.analysis_db import AnalysisDatabase
from x86decomp.angr_backend import (
    angr_bounded_compare,
    angr_bounded_compare_files,
    angr_memory_alias_compare_files,
)
from x86decomp.benchmarks import classification_metrics, run_benchmark_corpus
from x86decomp.cli import main as cli_main
from x86decomp.coff import (
    FunctionDefinitionAux,
    RawAux,
    SyntheticSectionSpec,
    SyntheticSymbolSpec,
    build_synthetic_coff,
    extract_symbol,
    parse_coff_bytes,
    synthetic_symbol_indices,
    write_synthetic_coff_object,
)
from x86decomp.compiler_lab import run_compiler_lab
from x86decomp.diffing import compare_files
from x86decomp.disassembly import (
    compare_instruction_streams,
    control_flow_edges,
    cross_check_ghidra_instructions,
    decode_instructions,
)
from x86decomp.dynamic import differential_validate_files, load_execution_spec
from x86decomp.dynamorio import run_drcov_trace
from x86decomp.evidence import EvidenceStore
from x86decomp.errors import ExternalToolError
from x86decomp.exe_diff import compare_pe_function_to_coff_symbol, extract_pe_bytes
from x86decomp.ghidra import run_export
from x86decomp.linker_layout import MapContribution
from x86decomp.memory import ProjectMemory
from x86decomp.models import EvidenceKind
from x86decomp.msvc_metadata import PEView
from x86decomp.pe import TLS64Info
from x86decomp.pe32 import (
    DelayImportLibrary,
    ExportSymbol,
    ImportLibrary,
    ImportSymbol,
    LoadConfigInfo,
    ResourceLeaf,
    TLSInfo,
)
from x86decomp.project import initialize_project, require_valid_project
from x86decomp.service import create_app, run_service
from x86decomp.symbolic import SymState, bounded_symbolic_compare_files
from x86decomp.toolchains import register_toolchain, verify_toolchain
from x86decomp.tools import snapshot_tools
from x86decomp.util import require_int, require_mapping, require_string
from x86decomp.work_queue import WorkQueue

from x86decomp_testkit.fixtures import build_minimal_pe32, write_json


ADD = bytes.fromhex("8b44240403442408c3")


def test_unified_canonical_entry_point(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify unified canonical entry point behavior."""
    from x86decomp import canonical

    parser = canonical.build_parser()
    parsed = parser.parse_args(["commands"])
    assert parsed.command == "commands"
    assert canonical.main(["commands"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["release"] == "0.7.10"
    assert payload["group_count"] == 59
    assert payload["route_count"] == 239


def test_abi_contract_loading(tmp_path: Path) -> None:
    """Verify abi contract loading behavior."""
    value = {
        "architecture": "x86",
        "convention": "cdecl",
        "stack_argument_bytes": 0,
        "callee_stack_cleanup": 0,
        "variadic": False,
        "this_register": None,
        "register_arguments": [],
        "return_registers": ["eax"],
        "structure_return": False,
        "floating_point": "none",
    }
    contract = ABIContract.from_dict(value)
    assert contract.architecture == "x86"
    path = write_json(tmp_path / "abi.json", value)
    assert load_abi_contract(path) == contract


def test_analysis_database_complete_public_surface(tmp_path: Path) -> None:
    """Verify analysis database complete public surface behavior."""
    artifact = tmp_path / "artifact"
    artifact.mkdir()
    write_json(
        artifact / "function.json",
        {
            "id": "pe-rva:00001000",
            "entry_rva": 0x1000,
            "name": "f",
            "qualified_name": "f",
            "calling_convention": "cdecl",
            "return_type": "int",
            "signature": "int f(void)",
        },
    )
    (artifact / "references.jsonl").write_text(
        json.dumps({"from": "00401000", "to": "00402000", "type": "CALL", "destination_function": "g"}) + "\n",
        encoding="utf-8",
    )
    with AnalysisDatabase(tmp_path / "analysis.sqlite3") as database:
        database.upsert_entity(entity_id="manual", kind="symbol", name="manual", address_rva=1, provenance="test")
        database.add_reference(source_entity="manual", target_entity=None, source_rva=1, target_rva=2, kind="DATA", provenance="test")
        counts = database.ingest_function_artifact(artifact, image_base=0x400000)
        assert counts == {"functions": 1, "references": 1}
        rows = database.query("SELECT id, kind FROM entities ORDER BY id")
        assert any(row["id"] == "pe-rva:00001000" for row in rows)


def test_angr_public_file_wrappers(tmp_path: Path) -> None:
    """Verify angr wrappers or their explicit optional-dependency error path."""
    target = tmp_path / "target.bin"
    candidate = tmp_path / "candidate.bin"
    target.write_bytes(b"\x31\xc0\xc3")
    candidate.write_bytes(b"\x31\xc0\xc3")
    if importlib.util.find_spec("angr") is None or importlib.util.find_spec("claripy") is None:
        with pytest.raises(ExternalToolError):
            angr_bounded_compare(target.read_bytes(), candidate.read_bytes(), max_steps=20, max_paths=4)
        return
    assert angr_bounded_compare(target.read_bytes(), candidate.read_bytes(), max_steps=20, max_paths=4)["equivalent_within_completed_model"]
    assert angr_bounded_compare_files(target, candidate, max_steps=20, max_paths=4)["equivalent_within_completed_model"]
    harness = write_json(
        tmp_path / "memory.json",
        {
            "architecture": "x86",
            "regions": [{"name": "a", "pointer_register": "eax", "size": 4, "initial": "symbolic"}],
            "observed_regions": ["a"],
            "output_registers": ["eax"],
            "max_steps": 20,
            "max_paths": 4,
        },
    )
    report = angr_memory_alias_compare_files(target, candidate, harness)
    assert report["kind"] == "angr_memory_alias_comparison"


def test_benchmark_metrics_and_runner(tmp_path: Path) -> None:
    """Verify benchmark metrics and runner behavior."""
    metrics = classification_metrics({1, 2}, {2, 3})
    assert metrics["true_positive"] == 1
    target = tmp_path / "a.bin"
    candidate = tmp_path / "b.bin"
    target.write_bytes(b"abc")
    candidate.write_bytes(b"abc")
    manifest = write_json(
        tmp_path / "benchmark.json",
        {"schema_version": 1, "name": "smoke", "cases": [{"id": "bytes", "kind": "byte_pair", "target": "a.bin", "candidate": "b.bin"}]},
    )
    report = run_benchmark_corpus(manifest)
    assert report["counts"]["completed"] == 1


def test_coff_remaining_value_objects_and_writer(tmp_path: Path) -> None:
    """Verify coff remaining value objects and writer behavior."""
    assert FunctionDefinitionAux(1, 2, 3, 4).to_dict()["kind"] == "function_definition"
    assert RawAux("00").to_dict()["kind"] == "raw"
    data = build_synthetic_coff(code=b"\x31\xc0\xc3", symbol_name="f")
    obj = parse_coff_bytes(data)
    symbol = obj.find_symbols("f")[0]
    assert obj.symbol_by_index(symbol.index) == symbol
    extracted = extract_symbol(obj, "f")
    assert extracted.to_dict(obj.machine)["size"] == 3
    assert synthetic_symbol_indices([SyntheticSymbolSpec(name="f", section_number=1)]) == {"f": 0}
    report = write_synthetic_coff_object(
        tmp_path / "x.obj",
        sections=[SyntheticSectionSpec(name=".text", data=b"\xc3", characteristics=0x60000020)],
        symbols=[SyntheticSymbolSpec(name="f", section_number=1, type=0x20, storage_class=2)],
    )
    assert report["architecture"] == "x86"


def test_compiler_lab_with_deterministic_fake_compiler(tmp_path: Path) -> None:
    """Verify compiler lab with deterministic fake compiler behavior."""
    compiler = tmp_path / "compiler.py"
    compiler.write_text(
        "from pathlib import Path\nimport sys\nPath(sys.argv[2]).write_bytes(Path(sys.argv[1]).read_bytes())\n",
        encoding="utf-8",
    )
    source = tmp_path / "source.c"
    source.write_text("int f(void){return 1;}\n", encoding="utf-8")
    profile = write_json(
        tmp_path / "profile.json",
        {
            "schema_version": 2,
            "id": "fake",
            "family": "test",
            "version": "1",
            "executable": sys.executable,
            "arguments": [str(compiler), "{source}", "{output}"],
            "timeout_seconds": 30,
            "output_kind": "opaque",
        },
    )
    lab = write_json(
        tmp_path / "lab.json",
        {
            "schema_version": 1,
            "source": source.name,
            "profiles": [profile.name],
            "matrix": {"axes": {"variant": ["a", "b"]}},
            "max_experiments": 4,
        },
    )
    report = run_compiler_lab(lab)
    assert report["experiment_count"] == 2


def test_diff_disassembly_and_crosscheck(tmp_path: Path) -> None:
    """Verify diff disassembly and crosscheck behavior."""
    left = tmp_path / "left.bin"
    right = tmp_path / "right.bin"
    code = b"\x31\xc0\xc3"
    left.write_bytes(code)
    right.write_bytes(code)
    assert compare_files(left, right)["equal"]
    if importlib.util.find_spec("capstone") is None:
        with pytest.raises(ExternalToolError):
            decode_instructions(code, base_address=0x1000)
        return
    records = decode_instructions(code, base_address=0x1000)
    assert records[0].to_dict()["mnemonic"] == "xor"
    assert isinstance(control_flow_edges(records, base_address=0x1000, code_size=len(code)), list)
    assert compare_instruction_streams(code, code, target_base=0x1000)["normalized_equal"]
    ghidra = tmp_path / "instructions.jsonl"
    ghidra.write_text("\n".join(json.dumps({"bytes_hex": record.bytes_hex, "mnemonic": record.mnemonic}) for record in records) + "\n", encoding="utf-8")
    assert cross_check_ghidra_instructions(ghidra, code, base_address=0x1000)["consistent"]


def test_dynamic_file_wrapper_and_spec_loader(tmp_path: Path) -> None:
    """Verify dynamic file wrapper and spec loader behavior."""
    target = tmp_path / "target.bin"
    candidate = tmp_path / "candidate.bin"
    target.write_bytes(ADD)
    candidate.write_bytes(ADD)
    harness = write_json(
        tmp_path / "harness.json",
        {
            "architecture": "x86",
            "stack_arguments_hex": (3).to_bytes(4, "little").hex() + (4).to_bytes(4, "little").hex(),
            "observe_registers": ["eax", "esp"],
            "max_instructions": 100,
            "timeout_ms": 1000,
        },
    )
    assert load_execution_spec(harness).architecture == "x86"
    if importlib.util.find_spec("unicorn") is None:
        with pytest.raises(ExternalToolError):
            differential_validate_files(target, candidate, harness)
        return
    assert differential_validate_files(target, candidate, harness)["equivalent_for_harness"]


def test_dynamorio_runner_with_fake_subprocess(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify dynamorio runner with fake subprocess behavior."""
    executable = tmp_path / "program"
    drrun = tmp_path / "drrun"
    executable.write_bytes(b"program")
    drrun.write_bytes(b"runner")
    drrun.chmod(drrun.stat().st_mode | stat.S_IXUSR)

    def fake_run(command, **kwargs):
        """Execute the fake run operation for the current toolkit workflow."""
        logdir = Path(command[command.index("-logdir") + 1])
        (logdir / "trace.log").write_text(
            "DRCOV VERSION: 2\nDRCOV FLAVOR: drcov\nModule Table: version 2, count 1\n"
            "Columns: id, base, end, entry, checksum, timestamp, path\n"
            "0, 0x1000, 0x2000, 0x1000, 0x0, 0x0, /tmp/program\n"
            "BB Table: 1 bbs\nmodule[ 0]: 0x10, 1\n",
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr("x86decomp.dynamorio.subprocess.run", fake_run)
    report = run_drcov_trace(executable, drrun=drrun, output_directory=tmp_path / "logs")
    assert report["success"]


def _verified_store(project: Path) -> tuple[EvidenceStore, str, str]:
    """Support verified store processing for internal toolkit callers."""
    store = EvidenceStore(project)
    evidence = [
        store.add_evidence(kind=EvidenceKind.STATIC_ANALYSIS, source="ghidra", locator="f", assertion="x", independent_group="g1"),
        store.add_evidence(kind=EvidenceKind.COMPILER_OUTPUT, source="compiler", locator="f", assertion="x", independent_group="g2"),
        store.add_evidence(kind=EvidenceKind.DYNAMIC_TRACE, source="trace", locator="f", assertion="x", independent_group="g3"),
    ]
    claim = store.create_claim(subject="f", predicate="is", object_value="x", evidence_ids=[item.id for item in evidence[:2]])
    store.attach_evidence(claim.id, evidence[2].id)
    assert store.verify_claim(claim.id)["state"] == "verified"
    return store, claim.id, evidence[0].id


def test_evidence_contradiction_require_verified_and_project_memory(tmp_path: Path) -> None:
    """Verify evidence contradiction require verified and project memory behavior."""
    project = tmp_path / "project"
    initialize_project(build_minimal_pe32(tmp_path / "a.exe"), project)
    store, claim_id, evidence_id = _verified_store(project)
    assert store.require_verified(claim_id).id == claim_id
    contradiction = store.add_evidence(kind=EvidenceKind.HUMAN_REVIEW, source="review", locator="f", assertion="not x", independent_group="g4")
    assert store.add_contradiction(claim_id, contradiction.id).contradiction_ids
    assert require_valid_project(project)["valid"]
    assert ProjectMemory(project).require_valid() is None


def test_exe_diff_extract_and_compare(tmp_path: Path) -> None:
    """Verify exe diff extract and compare behavior."""
    code = b"\x31\xc0\xc3"
    pe = build_minimal_pe32(tmp_path / "a.exe", code)
    coff_path = tmp_path / "a.obj"
    coff_path.write_bytes(build_synthetic_coff(code=code, symbol_name="f"))
    _image, extracted_bytes = extract_pe_bytes(pe, rva=0x1000, size=len(code))
    assert extracted_bytes == code
    report = compare_pe_function_to_coff_symbol(pe_path=pe, function_rva=0x1000, function_size=len(code), coff_path=coff_path, symbol_name="f")
    assert report["classification"] == "byte_matched"


def test_ghidra_run_export_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify ghidra run export success behavior."""
    monkeypatch.setattr(
        "x86decomp.ghidra.subprocess.run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0, stdout="ok", stderr=""),
    )
    assert run_export(["fake"], timeout_seconds=1)["success"]


def test_remaining_value_objects_and_peview(tmp_path: Path) -> None:
    """Verify remaining value objects and peview behavior."""
    symbol = ImportSymbol("f", None, 0, 1, 2)
    assert symbol.to_dict()["name"] == "f"
    assert ImportLibrary("x.dll", (symbol,)).to_dict()["symbols"]
    assert ExportSymbol("f", 1, 0x1000, None).to_dict()["rva_hex"] == "0x00001000"
    assert TLSInfo(1, 2, 3, 4, 0, 0, (5,)).to_dict()["callbacks_va"] == [5]
    assert ResourceLeaf(("type", "1"), 0x2000, 3, 0, "a" * 64).to_dict()["path"] == ["type", "1"]
    assert DelayImportLibrary("x.dll", 1, 2, (symbol,)).to_dict()["symbols"]
    load = LoadConfigInfo(1, None, None, None, None, None, None, None, None, None, None, None, None, None)
    assert load.to_dict()["size"] == 1
    assert TLS64Info(1, 2, 3, 4, 0, 0, (5,)).to_dict()["callbacks_va"] == [5]
    assert MapContribution(1, 2, 3, "a.obj").to_dict()["object"] == "a.obj"
    pe = build_minimal_pe32(tmp_path / "v.exe", b"\x34\x12\xc3")
    view = PEView(pe)
    assert view.u16(0x1000) == 0x1234


def test_service_create_and_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify service create and run behavior."""
    project = tmp_path / "project"
    initialize_project(build_minimal_pe32(tmp_path / "a.exe"), project)
    app = create_app(project)
    assert any(route.path == "/api/project" for route in app.routes)
    calls = []
    monkeypatch.setattr("uvicorn.run", lambda app, host, port: calls.append((app, host, port)))
    run_service(project, host="127.0.0.1", port=9876)
    assert calls and calls[0][2] == 9876


def test_symbolic_clone_and_file_wrapper(tmp_path: Path) -> None:
    # SymState is normally created by the symbolic engine; construction here covers
    # the public cloning contract without bypassing solver semantics.
    """Verify symbolic clone behavior and the optional symbolic backend error path."""
    target = tmp_path / "target.bin"
    candidate = tmp_path / "candidate.bin"
    target.write_bytes(b"\x31\xc0\xc3")
    candidate.write_bytes(b"\x31\xc0\xc3")
    if importlib.util.find_spec("z3") is None or importlib.util.find_spec("capstone") is None:
        state = SymState(pc=0, regs={"eax": 1}, memory={}, constraints=[], flags={}, steps=0)
        clone = state.clone()
        assert clone is not state and clone.regs == state.regs
        with pytest.raises(ExternalToolError):
            bounded_symbolic_compare_files(target, candidate, max_steps=20, max_paths=4)
        return

    import z3

    state = SymState(pc=0, regs={"eax": z3.BitVecVal(1, 32)}, memory={}, constraints=[], flags={}, steps=0)
    clone = state.clone()
    assert clone is not state and clone.regs == state.regs
    assert bounded_symbolic_compare_files(target, candidate, max_steps=20, max_paths=4)["equivalent_within_model"]


def test_toolchain_snapshot_util_contract_and_workqueue(tmp_path: Path) -> None:
    """Verify toolchain snapshot util contract and workqueue behavior."""
    executable = tmp_path / "tool"
    executable.write_bytes(Path(sys.executable).read_bytes())
    executable.chmod(executable.stat().st_mode | stat.S_IXUSR)
    registry = tmp_path / "toolchains.json"
    entry = register_toolchain(registry, toolchain_id="t", family="test", version="1", executables={"compiler": executable})
    assert entry["id"] == "t"
    assert verify_toolchain(registry, "t")["valid"]
    report_path = tmp_path / "tools.json"
    assert snapshot_tools(report_path)["schema_version"] == 1 and report_path.is_file()
    assert require_mapping({}, "x") == {}
    assert require_string({"x": "y"}, "x") == "y"
    assert require_int({"x": 1}, "x", minimum=0) == 1
    queue = WorkQueue(tmp_path / "queue.sqlite3")
    try:
        assert queue.next() is None
        task = queue.create(function_id="f", mode="matching", kind="source", instructions="work", required_validators=["byte"])
        assert queue.next()["id"] == task["id"]
    finally:
        queue.close()


def test_cli_main_executes_public_entrypoint(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Verify cli main executes public entrypoint behavior."""
    left = tmp_path / "a"
    right = tmp_path / "b"
    left.write_bytes(b"x")
    right.write_bytes(b"x")
    assert cli_main(["diff-bytes", str(left), str(right)]) == 0
    assert '"equal": true' in capsys.readouterr().out


def test_streamable_http_mcp_public_methods(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify streamable http mcp public methods behavior."""
    from x86decomp.mcp import StreamableHTTPMCPClient

    class Headers:
        """Coordinate headers behavior for the current toolkit workflow."""
        def get(self, key: str, default=None):
            """Execute the get operation for the current toolkit workflow."""
            return "session-1" if key.lower() == "mcp-session-id" else default

        def get_content_type(self) -> str:
            """Execute the get content type operation for the current toolkit workflow."""
            return "application/json"

    class Response:
        """Coordinate response behavior for the current toolkit workflow."""
        headers = Headers()

        def __init__(self, payload: dict):
            """Initialize the instance with validated constructor state."""
            self.payload = payload

        def __enter__(self):
            """Enter the managed runtime context and return the active resource."""
            return self

        def __exit__(self, exc_type, exc, tb):
            """Exit the managed runtime context and release owned resources."""
            return False

        def read(self) -> bytes:
            """Read read for the current toolkit workflow."""
            return json.dumps(self.payload).encode("utf-8")

    def fake_urlopen(request, timeout=0):
        """Execute the fake urlopen operation for the current toolkit workflow."""
        payload = json.loads(request.data.decode("utf-8"))
        method = payload["method"]
        if method == "notifications/initialized":
            return Response({"jsonrpc": "2.0", "result": {}})
        if method == "initialize":
            return Response({"jsonrpc": "2.0", "id": payload["id"], "result": {"protocolVersion": "2025-06-18"}})
        if method == "tools/list":
            return Response({"jsonrpc": "2.0", "id": payload["id"], "result": {"tools": [{"name": "read", "description": "r", "inputSchema": {}}]}})
        if method == "tools/call":
            return Response({"jsonrpc": "2.0", "id": payload["id"], "result": {"content": [{"type": "text", "text": "ok"}]}})
        raise AssertionError(method)

    monkeypatch.setattr("x86decomp.mcp.urllib.request.urlopen", fake_urlopen)
    client = StreamableHTTPMCPClient("http://127.0.0.1:1/mcp")
    assert client.initialize()["protocolVersion"] == "2025-06-18"
    assert client.list_tools()[0].name == "read"
    assert client.call_tool("read", {})["content"]
    assert client.close() is None


def test_private_function_surface_regression(monkeypatch: pytest.MonkeyPatch) -> None:
    """Exercise the remaining internal function bodies so no defined function is omitted."""
    import argparse
    from types import SimpleNamespace

    from x86decomp import cli as toolkit_cli
    from x86decomp import coff_archive, image_match, symbolic
    from x86decomp.mcp import StdioMCPClient, StreamableHTTPMCPClient
    from x86decomp.pe32 import _Reader

    assert _Reader(b"hello\x00").c_string(0, "test") == "hello"
    assert toolkit_cli._int("0x10") == 16
    assert toolkit_cli._json_object('{"x": 1}') == {"x": 1}
    with pytest.raises(argparse.ArgumentTypeError):
        toolkit_cli._json_object("[]")

    client = toolkit_cli._mcp_client(SimpleNamespace(url="http://localhost:1", command_json=None))
    assert isinstance(client, StreamableHTTPMCPClient)

    if importlib.util.find_spec("z3") is None or importlib.util.find_spec("capstone") is None:
        with pytest.raises(ExternalToolError):
            symbolic._deps()
    else:
        import z3

        state = symbolic.SymState(pc=0, regs={}, memory={})
        symbolic._write_memory(state, 0x1000, 16, z3.BitVecVal(0x1234, 16), z3)
        assert z3.simplify(state.memory[0x1000]).as_long() == 0x34
        flags = {name: z3.BoolVal(False) for name in ("zf", "sf", "cf", "of")}
        assert z3.is_false(z3.simplify(symbolic._condition("je", flags, z3)))
        assert symbolic._is_sat([z3.BoolVal(True)], z3)

    fake_image = SimpleNamespace(base_relocations=(), sections=())
    assert image_match._apply_rebase(b"abc", target_base=2, candidate_base=1, image=fake_image) == b"abc"
    assert coff_archive._long_name(b"long-name/\n", 0) == "long-name"

    stdio = object.__new__(StdioMCPClient)
    closed: list[bool] = []
    monkeypatch.setattr(stdio, "close", lambda: closed.append(True))
    assert stdio.__enter__() is stdio
    stdio.__exit__(None, None, None)
    assert closed == [True]


def test_remaining_current_function_surface(tmp_path: Path) -> None:
    """Verify remaining current function surface behavior."""
    from x86decomp.content_store import StoredArtifact
    from x86decomp.cpp_recovery import _adjustor_thunk_candidate, _function_prefix
    from x86decomp.harness_generator import _deterministic_word, generate_execution_harness_from_files
    from x86decomp.project_state import ProjectStateDatabase
    from x86decomp.security_audit import verify_release_manifest
    from x86decomp.target_pack import SupportingArtifact
    from x86decomp.worker import WorkerLimits, WorkerRequest, _container_command

    artifact = StoredArtifact("0" * 64, 1, tmp_path / "store" / "data", tmp_path / "store" / "meta")
    assert artifact.to_dict()["size"] == 1
    assert artifact.to_dict(root=tmp_path)["data_path"] == "store/data"
    support = SupportingArtifact("pdb", tmp_path / "a.pdb", "1" * 64, 2)
    assert support.to_dict()["role"] == "pdb"

    pe = build_minimal_pe32(tmp_path / "adjustor.exe")
    initial_view = PEView(pe)
    raw = bytearray(pe.read_bytes())
    code_rva = 0x1000
    code_offset = initial_view.rva_to_offset(code_rva)
    raw[code_offset : code_offset + 8] = bytes.fromhex("83c104e900000000")
    pe.write_bytes(raw)
    view = PEView(pe)
    assert _function_prefix(view, code_rva).startswith(bytes.fromhex("83c104"))
    thunk = _adjustor_thunk_candidate(view, code_rva)
    if importlib.util.find_spec("capstone") is None:
        assert thunk is None
    else:
        assert thunk is not None and thunk["classification"] == "adjustor_thunk_candidate"

    abi = write_json(
        tmp_path / "abi.json",
        {
            "architecture": "x86",
            "convention": "cdecl",
            "stack_argument_bytes": 4,
            "callee_stack_cleanup": 0,
            "variadic": False,
            "this_register": None,
            "register_arguments": [],
            "return_registers": ["eax"],
            "structure_return": False,
            "floating_point": "none",
        },
    )
    pointers = write_json(tmp_path / "pointers.json", [{"position": 0, "size": 16}])
    harness = generate_execution_harness_from_files(abi, tmp_path / "harness.json", pointer_parameters_path=pointers)
    assert harness["memory"] and _deterministic_word(0, 32) == 0x2468ACE0

    with ProjectStateDatabase(tmp_path / "state.sqlite3") as database:
        database.upsert_artifact_reference("ref", "2" * 64, kind="test", owner="suite")
        assert database.artifact_digests() == {"2" * 64}

    data = tmp_path / "manifested.txt"
    data.write_text("manifested", encoding="utf-8")
    import hashlib
    manifest = tmp_path / "MANIFEST.sha256"
    manifest.write_text(f"{hashlib.sha256(data.read_bytes()).hexdigest()}  manifested.txt\n", encoding="utf-8")
    assert verify_release_manifest(tmp_path, manifest)["valid"]

    request = WorkerRequest(
        command=("python3", "-c", "print('ok')"),
        working_directory=tmp_path,
        environment={"A": "B"},
        isolation="container",
        container_image="python:3.13",
        limits=WorkerLimits(),
    )
    command = _container_command(request, "docker")
    assert command[:3] == ("docker", "run", "--rm") and "--network=none" in command
