"""Verify the current toolkit behavior covered by `tests/test_production.py`."""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

from pe_fixture import build_minimal_pe32
from x86decomp.abi import ABIContract, CallingConvention, FloatMode
from x86decomp.compiler_worker import run_compiler_worker
from x86decomp.content_store import ContentStore
from x86decomp.errors import ExternalToolError
from x86decomp.convergence import analyze_image_convergence, append_convergence_history
from x86decomp.cpp_recovery import recover_cpp_model
from x86decomp.harness_generator import generate_execution_harness
from x86decomp.linker_reconstruction import build_linker_reconstruction_plan, write_relink_manifest_from_plan
from x86decomp.coff import write_synthetic_coff
from x86decomp.orchestrator import Orchestrator, PipelineManifest
from x86decomp.project import initialize_project
from x86decomp.project_state import (
    check_project_state,
    create_project_backup,
    migrate_project,
    project_gc,
    repair_project_state,
    restore_project_backup,
)
from x86decomp.reproducibility import build_reproduction_manifest, verify_reproduction_manifest
from x86decomp.security_audit import audit_source_tree, generate_sbom
from x86decomp.target_pack import generate_project_from_target_pack, infer_target_pack, verify_target_pack
from x86decomp.util import load_json, write_json
from x86decomp.worker import WorkerLimits, WorkerRequest, discover_worker_capabilities, execute_worker_request


def test_content_store_roundtrip_and_gc(tmp_path: Path) -> None:
    """Verify content store roundtrip and gc behavior."""
    source = tmp_path / "source.bin"
    source.write_bytes(b"artifact")
    store = ContentStore(tmp_path / "store")
    artifact = store.put_file(source)
    assert store.read_bytes(artifact.digest) == b"artifact"
    store.add_reference("functions/f", artifact.digest, kind="function", owner="test")
    assert store.verify()["valid"]
    assert project_gc_like(store, dry_run=True)["candidate_count"] == 0
    assert store.remove_reference("functions/f")
    assert store.garbage_collect(dry_run=True)["candidate_count"] == 1
    assert store.garbage_collect(dry_run=False)["candidate_count"] == 1


def project_gc_like(store: ContentStore, *, dry_run: bool) -> dict:
    """Run project garbage collection while preserving the test helper call contract."""
    return store.garbage_collect(dry_run=dry_run)


def test_worker_executes_bounded_command_and_hashes_outputs(tmp_path: Path) -> None:
    """Verify worker executes bounded command and hashes outputs behavior."""
    work = tmp_path / "work"
    work.mkdir()
    input_path = work / "input.txt"
    input_path.write_text("hello", encoding="utf-8")
    output_path = work / "output.txt"
    request = WorkerRequest(
        command=(sys.executable, "-c", "from pathlib import Path;Path('output.txt').write_text(Path('input.txt').read_text().upper())"),
        working_directory=work,
        input_files=(Path("input.txt"),),
        expected_outputs=(Path("output.txt"),),
        limits=WorkerLimits(timeout_seconds=10, cpu_seconds=10, memory_bytes=512 * 1024 * 1024),
    )
    result = execute_worker_request(request, log_directory=tmp_path / "logs")
    assert result.status == "passed"
    assert output_path.read_text() == "HELLO"
    assert result.input_hashes and result.output_hashes
    capabilities = discover_worker_capabilities()
    assert capabilities["local_bounded"] is True
    assert capabilities["network_namespace_enforced_in_local_mode"] is False


def test_target_pack_auto_template_and_project(tmp_path: Path) -> None:
    """Verify target pack auto template and project behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    pack_dir = tmp_path / "pack"
    result = infer_target_pack(
        image,
        pack_dir,
        name="Grounded target",
        decisions={"preferred_mode": "both", "compiler_family": "unknown"},
    )
    assert result["target_pack"]["architecture"] == "x86"
    verification = verify_target_pack(pack_dir)
    assert verification["valid"], verification
    project_root = tmp_path / "project"
    project_result = generate_project_from_target_pack(pack_dir, project_root)
    assert project_result["project"]["target_id"] == result["target_pack"]["target_id"]
    assert (project_root / "target-pack" / "target.toml").is_file()
    assert check_project_state(project_root).valid


def test_project_migration_backup_restore_repair_and_gc(tmp_path: Path) -> None:
    """Verify project migration backup restore repair and gc behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    project_root = tmp_path / "project"
    initialize_project(image, project_root)
    project = load_json(project_root / "project.json")
    project["schema_version"] = 2
    for key in ("project_state_database", "content_store", "target_pack", "orchestration_root", "toolkit_release"):
        project.pop(key, None)
    write_json(project_root / "project.json", project)
    (project_root / "state" / "project-state.sqlite3").unlink()
    # Content-store directory can exist empty; migration reinitializes it.
    dry = migrate_project(project_root, dry_run=True)
    assert dry["to_version"] == 3
    backup = tmp_path / "backup.tar.gz"
    migrated = migrate_project(project_root, backup_path=backup)
    assert migrated["changed"]
    assert check_project_state(project_root).valid
    restore_root = tmp_path / "restored"
    restored = restore_project_backup(backup, restore_root)
    assert restored["restored"]
    # The backup is pre-migration by design, so it is valid input for a migration.
    assert load_json(restore_root / "project.json")["schema_version"] == 2
    assert repair_project_state(project_root, dry_run=True)["dry_run"]
    assert project_gc(project_root, dry_run=True)["dry_run"]
    second_backup = create_project_backup(project_root, tmp_path / "post.tar.gz")
    assert second_backup["file_count"] > 0


def test_orchestrator_resume_failure_retry_and_cancel(tmp_path: Path) -> None:
    """Verify orchestrator resume failure retry and cancel behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    project_root = tmp_path / "project"
    initialize_project(image, project_root)
    manifest = project_root / "orchestration" / "pipelines" / "test.json"
    write_json(
        manifest,
        {
            "schema_version": 1,
            "pipeline_id": "test-pipeline",
            "project_root": str(project_root),
            "stages": [
                {
                    "id": "one",
                    "kind": "command",
                    "command": [sys.executable, "-c", "from pathlib import Path;Path(r'{work}/outputs/one.txt').write_text('one')"],
                    "outputs": ["one.txt"],
                },
                {
                    "id": "two",
                    "kind": "command",
                    "depends_on": ["one"],
                    "command": [sys.executable, "-c", "from pathlib import Path;Path(r'{work}/outputs/two.txt').write_text('two')"],
                    "outputs": ["two.txt"],
                },
            ],
        },
    )
    parsed = PipelineManifest.load(manifest)
    assert len(parsed.stages) == 2
    with Orchestrator(project_root) as orchestrator:
        status = orchestrator.run(manifest)
        assert status["status"] == "succeeded"
        attempts = [job["attempt"] for job in status["jobs"]]
        status2 = orchestrator.run(manifest)
        assert [job["attempt"] for job in status2["jobs"]] == attempts
        retried = orchestrator.retry("test-pipeline", "two")
        assert retried["jobs_reset"] == 1
        status3 = orchestrator.run(manifest)
        assert status3["status"] == "succeeded"
        cancelled = orchestrator.cancel("test-pipeline")
        assert cancelled["cancel_requests"] == 0


def test_compiler_worker_uses_real_subprocess_contract(tmp_path: Path) -> None:
    """Verify compiler worker uses real subprocess contract behavior."""
    source = tmp_path / "input.c"
    source.write_text("int value;\n", encoding="utf-8")
    profile = tmp_path / "profile.json"
    write_json(
        profile,
        {
            "schema_version": 2,
            "id": "python-copy",
            "family": "test",
            "version": sys.version.split()[0],
            "executable": sys.executable,
            "arguments": [
                "-S",
                "-c",
                "import shutil,sys;shutil.copyfile(sys.argv[1],sys.argv[2])",
                "{source}",
                "{output}",
            ],
            "timeout_seconds": 30,
            "output_kind": "copied_source",
            "inherit_environment": False,
        },
    )
    output = tmp_path / "output.obj"
    report = run_compiler_worker(profile, source, output)
    assert report["success"]
    assert output.read_bytes() == source.read_bytes()
    assert report["worker"]["isolation_strength"] == "resource_bounded_not_security_boundary"


def test_harness_generation_is_deterministic_and_explicit(tmp_path: Path) -> None:
    """Verify harness generation is deterministic and explicit behavior."""
    contract = ABIContract(
        architecture="x86",
        convention=CallingConvention.THISCALL,
        stack_argument_bytes=4,
        callee_stack_cleanup=4,
        variadic=False,
        this_register="ecx",
        register_arguments=(),
        return_registers=("eax",),
        structure_return=False,
        floating_point=FloatMode.NONE,
    )
    first = generate_execution_harness(contract, pointer_parameters=[{"position": 0, "size": 8}])
    second = generate_execution_harness(contract, pointer_parameters=[{"position": 0, "size": 8}])
    for value in (first, second):
        value.pop("created_at")
    assert first == second
    assert first["generation"]["original_runtime_inputs_claimed"] is False
    assert first["observe_memory"]


def test_convergence_and_history(tmp_path: Path) -> None:
    """Verify convergence and history behavior."""
    reference = build_minimal_pe32(tmp_path / "reference.exe")
    candidate = tmp_path / "candidate.exe"
    data = bytearray(reference.read_bytes())
    data[0x200] ^= 0xFF
    candidate.write_bytes(data)
    report_path = tmp_path / "convergence.json"
    report = analyze_image_convergence(reference, candidate, report_path=report_path)
    assert not report["complete"]
    assert report["totals"]["executable_mismatch_bytes"] == 1
    history = append_convergence_history(tmp_path / "history.jsonl", report)
    assert history["entry_count"] == 1
    same = analyze_image_convergence(reference, reference, previous_report=report_path)
    assert same["complete"]
    assert same["delta_from_previous"]["normalized_mismatch_count"] < 0


def test_linker_reconstruction_plan_is_evidence_limited(tmp_path: Path) -> None:
    """Verify linker reconstruction plan is evidence limited behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    obj = tmp_path / "entry.obj"
    write_synthetic_coff(obj, code=b"\x31\xc0\xc3", symbol_name="_entry")
    map_path = tmp_path / "target.map"
    map_path.write_text(
        """target\n Preferred load address is 00400000\n\n Start         Length     Name                   Class\n 0001:00000000 00000003H .text                  CODE\n 0001:00000000 00000003H entry.obj\n\n Address         Publics by Value              Rva+Base       Lib:Object\n 0001:00000000       _entry                     00401000 f   entry.obj\n\n entry point at        0001:00000000\n""",
        encoding="utf-8",
    )
    plan = build_linker_reconstruction_plan(image, map_path, object_paths=[obj])
    assert plan["placements"][0]["exact_extent"]
    assert plan["ready_for_relink"]
    manifest = tmp_path / "relink.json"
    write_relink_manifest_from_plan(plan, manifest)
    assert load_json(manifest)["objects"]


def test_cpp_recovery_empty_metadata_is_truthful(tmp_path: Path) -> None:
    """Verify cpp recovery empty metadata is truthful behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    report = recover_cpp_model(image)
    assert report["kind"] == "bounded_cpp_recovery"
    assert report["claims"]["original_source_declarations_recovered"] is False
    assert report["counts"]["classes"] == 0


def test_reproduction_and_security_reports(tmp_path: Path) -> None:
    """Verify reproduction and security reports behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    project_root = tmp_path / "project"
    initialize_project(image, project_root)
    reproduction_path = tmp_path / "reproduction.json"
    manifest = build_reproduction_manifest(project_root, output=reproduction_path, required_tools=["python"])
    assert manifest["binary"]["sha256"] == manifest["binary"]["expected_sha256"]
    check = verify_reproduction_manifest(project_root, reproduction_path)
    assert check["reproducible"], check
    audit_root = tmp_path / "audit"
    audit_root.mkdir()
    (audit_root / "safe.txt").write_text("safe", encoding="utf-8")
    audit = audit_source_tree(audit_root)
    assert audit["passed"]
    sbom = generate_sbom()
    assert sbom["bomFormat"] == "CycloneDX"
    assert sbom["metadata"]["properties"][1]["value"] == "false"


def test_generated_template_is_grounded_and_executable(tmp_path: Path) -> None:
    """Verify generated template is grounded and executable behavior."""
    from x86decomp.project_template import derive_template_contract, materialize_project_template

    image = build_minimal_pe32(tmp_path / "target.exe")
    pack = tmp_path / "pack"
    infer_target_pack(image, pack, decisions={"preferred_mode": "matching"})
    contract = derive_template_contract(pack)
    assert contract["selected_modes"] == ["matching"]
    assert contract["truth_policy"]["generated_source_claimed"] is False
    project = tmp_path / "project"
    generate_project_from_target_pack(pack, project)
    materialized = materialize_project_template(project)
    assert Path(project / materialized["helper"]).is_file()
    assert load_json(project / "config" / "project-template.json")["blockers"]
    assert (project / "src" / "matching").is_dir()
    assert not list((project / "src" / "matching").glob("*.c"))

    # The generated helper must remain executable when the console-script entry
    # point is not on PATH, as long as the Python package is importable.
    env = dict(os.environ)
    env["PATH"] = str(tmp_path / "empty-path")
    source_root = Path(__file__).resolve().parents[1] / "src"
    current_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(source_root) + (os.pathsep + current_pythonpath if current_pythonpath else "")
    completed = subprocess.run(
        [sys.executable, str(project / "scripts" / "project.py"), "check"],
        cwd=project,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr


def test_orchestrator_materializes_and_revalidates_outputs(tmp_path: Path) -> None:
    """Verify orchestrator materializes and revalidates outputs behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    project_root = tmp_path / "project"
    initialize_project(image, project_root)
    manifest = project_root / "orchestration" / "pipelines" / "materialize.json"
    write_json(
        manifest,
        {
            "schema_version": 1,
            "pipeline_id": "materialize",
            "project_root": str(project_root),
            "stages": [
                {
                    "id": "write",
                    "kind": "command",
                    "command": [
                        sys.executable,
                        "-c",
                        "from pathlib import Path;Path(r'{work}/outputs/value.txt').write_text('verified')",
                    ],
                    "outputs": ["value.txt"],
                }
            ],
        },
    )
    with Orchestrator(project_root) as orchestrator:
        first = orchestrator.run(manifest)
        assert first["status"] == "succeeded"
        row = orchestrator.connection.execute("SELECT attempt,result_json FROM jobs WHERE pipeline_id='materialize'").fetchone()
        payload = json.loads(row["result_json"])
        output = project_root / payload["materialized_outputs"][0]["path"]
        assert output.read_text() == "verified"
        assert row["attempt"] == 1
        output.write_text("tampered", encoding="utf-8")
        second = orchestrator.run(manifest)
        assert second["status"] == "succeeded"
        row2 = orchestrator.connection.execute("SELECT attempt,result_json FROM jobs WHERE pipeline_id='materialize'").fetchone()
        assert row2["attempt"] == 2
        assert output.read_text() == "verified"
    assert ContentStore(project_root / "artifacts").verify()["valid"]


def test_extended_symbolic_conditions_adc_sbb_setcc_cmovcc() -> None:
    """Verify extended symbolic conditions adc sbb setcc cmovcc behavior."""
    from x86decomp.symbolic import bounded_symbolic_compare

    # cmp edx,0; stc; adc eax,ecx; sbb eax,ecx; sete al; cmove eax,ecx; ret
    code = bytes.fromhex("83fa00f911c819c80f94c00f44c1c3")
    if importlib.util.find_spec("capstone") is None or importlib.util.find_spec("z3") is None:
        import pytest

        with pytest.raises(ExternalToolError, match="Capstone and z3-solver are required"):
            bounded_symbolic_compare(
                code,
                code,
                architecture="x86",
                input_registers=("eax", "ecx", "edx"),
                output_registers=("eax",),
                max_steps=64,
                max_paths=8,
            )
        return
    report = bounded_symbolic_compare(
        code,
        code,
        architecture="x86",
        input_registers=("eax", "ecx", "edx"),
        output_registers=("eax",),
        max_steps=64,
        max_paths=8,
    )
    assert report["equivalent_within_model"]
    assert report["solver_result"] == "unsat"


def test_service_snapshot_exposes_control_plane(tmp_path: Path) -> None:
    """Verify service snapshot exposes control plane behavior."""
    from x86decomp.service import service_snapshot

    image = build_minimal_pe32(tmp_path / "target.exe")
    project_root = tmp_path / "project"
    initialize_project(image, project_root)
    snapshot = service_snapshot(project_root)
    assert snapshot["read_only"] is True
    assert snapshot["verification"]["valid"]
    assert snapshot["state_check"]["valid"]
    assert "container_runtime" in snapshot["worker_capabilities"]


def test_project_backup_is_deterministic(tmp_path: Path) -> None:
    """Verify project backup is deterministic behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    project = tmp_path / "project"
    initialize_project(image, project)
    first = create_project_backup(project, tmp_path / "first.tar.gz")
    second = create_project_backup(project, tmp_path / "second.tar.gz")
    assert first["sha256"] == second["sha256"]


def test_active_pipeline_cancellation_is_observed(tmp_path: Path) -> None:
    """Verify active pipeline cancellation is observed behavior."""
    import threading
    import time

    image = build_minimal_pe32(tmp_path / "target.exe")
    project = tmp_path / "project"
    initialize_project(image, project)
    manifest = project / "orchestration" / "pipelines" / "cancel.json"
    write_json(
        manifest,
        {
            "schema_version": 1,
            "pipeline_id": "cancel-active",
            "project_root": str(project),
            "stages": [
                {
                    "id": "sleep",
                    "kind": "command",
                    "command": [sys.executable, "-c", "import time;time.sleep(30)"],
                    "outputs": [],
                    "limits": {"timeout_seconds": 60},
                }
            ],
        },
    )
    result: dict[str, object] = {}

    def run_pipeline() -> None:
        """Run pipeline."""
        with Orchestrator(project) as orchestrator:
            result.update(orchestrator.run(manifest))

    thread = threading.Thread(target=run_pipeline)
    thread.start()
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        with Orchestrator(project) as observer:
            try:
                status = observer.status("cancel-active")
            except Exception:
                status = {"jobs": []}
            if status.get("jobs") and status["jobs"][0]["state"] == "running":
                observer.cancel("cancel-active", "sleep")
                break
        time.sleep(0.05)
    thread.join(timeout=10)
    assert not thread.is_alive()
    assert result["status"] == "cancelled"


def test_dependency_audit_adapter_parsing(tmp_path: Path) -> None:
    """Verify dependency audit adapter parsing behavior."""
    from x86decomp.security_audit import run_dependency_vulnerability_audit

    tool = tmp_path / "pip-audit"
    tool.write_text(
        "#!/usr/bin/env python3\nimport json\nprint(json.dumps({'dependencies':[{'name':'safe','version':'1','vulns':[]}]}))\n",
        encoding="utf-8",
    )
    tool.chmod(0o755)
    report = run_dependency_vulnerability_audit(executable=str(tool))
    assert report["passed"]
    assert report["dependency_count"] == 1
    assert report["vulnerability_count"] == 0


def test_pipeline_stale_heartbeat_recovery(tmp_path: Path) -> None:
    """Verify pipeline stale heartbeat recovery behavior."""
    image = build_minimal_pe32(tmp_path / "target.exe")
    project = tmp_path / "project"
    initialize_project(image, project)
    manifest = project / "orchestration" / "pipelines" / "recover.json"
    write_json(
        manifest,
        {
            "schema_version": 1,
            "pipeline_id": "recover",
            "project_root": str(project),
            "stages": [{"id": "one", "kind": "command", "command": [sys.executable, "-c", "pass"], "outputs": []}],
        },
    )
    with Orchestrator(project) as orchestrator:
        orchestrator.register(manifest)
        orchestrator.connection.execute(
            "UPDATE jobs SET state='running',runner_id='dead',heartbeat_at='2000-01-01T00:00:00Z' WHERE pipeline_id='recover'"
        )
        recovered = orchestrator.recover_stale_jobs(pipeline_id="recover", stale_seconds=1)
        assert recovered["jobs_recovered"] == 1
        assert orchestrator.status("recover")["jobs"][0]["state"] == "pending"


def test_release_gate_is_explicit_and_truth_scoped(tmp_path: Path) -> None:
    """Verify release gate is explicit and truth scoped behavior."""
    from x86decomp.release_gate import evaluate_release_gate

    image = build_minimal_pe32(tmp_path / "target.exe")
    pack = tmp_path / "pack"
    infer_target_pack(image, pack)
    project = tmp_path / "project"
    generate_project_from_target_pack(pack, project)
    baseline = evaluate_release_gate(project)
    assert baseline["passed"]
    assert "not proof" in baseline["truth_statement"]
    strict = evaluate_release_gate(
        project,
        require_workflows=True,
        require_verified_claims=True,
        require_succeeded_pipelines=True,
    )
    assert not strict["passed"]
    assert any("no function workflows" in item for item in strict["failures"])


def test_synthetic_corpus_generation_is_reproducible_and_hash_checked(tmp_path: Path) -> None:
    """Verify synthetic corpus generation is reproducible and hash checked behavior."""
    from x86decomp.synthetic_corpus import generate_synthetic_corpus, verify_synthetic_corpus

    first_root = tmp_path / "first"
    second_root = tmp_path / "second"
    first = generate_synthetic_corpus(first_root, cases_per_family=2, seed=12345)
    second = generate_synthetic_corpus(second_root, cases_per_family=2, seed=12345)
    assert first["case_count"] == 24
    assert [item["source_sha256"] for item in first["cases"]] == [
        item["source_sha256"] for item in second["cases"]
    ]
    verified = verify_synthetic_corpus(first_root / "corpus-generation.json")
    assert verified == {"valid": True, "case_count": 24, "failures": []}
    source = first_root / first["cases"][0]["source"]
    source.write_text(source.read_text(encoding="utf-8") + "\n/* tampered */\n", encoding="utf-8")
    tampered = verify_synthetic_corpus(first_root / "corpus-generation.json")
    assert not tampered["valid"]
    assert any("hash mismatch" in item for item in tampered["failures"])


def test_target_decisions_example_preserves_unknowns() -> None:
    """Verify target decisions example preserves unknowns behavior."""
    decisions = load_json(Path(__file__).resolve().parents[1] / "examples/release/target-decisions.json")
    assert decisions["preferred_mode"] == "both"
    assert decisions["compiler_family"] == "unknown"
    assert decisions["compiler_version"] == "unknown"
    assert decisions["linker_family"] == "unknown"
    assert decisions["source_language"] == "unknown"
    assert decisions["allow_host_execution"] is False
