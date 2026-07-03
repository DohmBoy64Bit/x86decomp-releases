"""Command-line interface for all toolkit architecture components."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .abi import load_abi_contract, validate_abi
from .angr_backend import angr_bounded_compare_files, angr_memory_alias_compare_files
from .analysis_db import AnalysisDatabase
from .artifacts import import_function_artifact, verify_function_artifact
from .benchmarks import run_benchmark_corpus
from .coff import CoffRelocation, extract_symbol, parse_coff, resolve_comdats, write_synthetic_coff
from .coff_archive import parse_coff_archive
from .compiler import run_compiler_profile
from .compiler_lab import run_compiler_lab
from .compiler_worker import run_compiler_worker
from .content_store import ContentStore
from .convergence import analyze_image_convergence, append_convergence_history
from .cpp_recovery import recover_cpp_model
from .decompme import create_decompme_packet
from .diffing import compare_files
from .disassembly import cross_check_ghidra_instructions, decode_instructions
from .dynamic import differential_validate_files
from .dynamorio import parse_drcov_text, run_drcov_trace
from .errors import X86DecompError
from .evidence import EvidenceStore
from .exe_diff import compare_pe_function_to_coff_symbol
from .ghidra import build_export_command, run_export
from .hybrid import generate_hybrid_project
from .harness_generator import generate_execution_harness_from_files
from .ground_truth import build_ground_truth_corpus, compare_ground_truth_corpora, create_builtin_manifest, verify_ground_truth_corpus
from .image_match import compare_whole_images, derive_layout_profile
from .linker_layout import parse_msvc_map, reconstruct_linker_layout
from .linker_reconstruction import build_linker_reconstruction_plan, write_relink_manifest_from_plan
from .msvc_metadata import analyze_msvc_metadata
from .integration import run_integration_scenarios
from .mcp import GhidraMCPGateway, StdioMCPClient, StreamableHTTPMCPClient
from .objdiff_adapter import run_objdiff_manifest
from .memory import ProjectMemory
from .models import EvidenceKind
from .patching import patch_pe_function
from .pe import parse_pe
from .pdb import parse_pdb
from .project import initialize_project, verify_project
from .project_template import derive_template_contract, materialize_project_template
from .project_state import (
    check_project_state, create_project_backup, migrate_project, project_gc,
    repair_project_state, restore_project_backup,
)
from .orchestrator import Orchestrator, create_default_pipeline
from .reproducibility import build_reproduction_manifest, verify_reproduction_manifest
from .release_gate import evaluate_release_gate
from .security_audit import audit_source_tree, generate_sbom, run_dependency_vulnerability_audit, verify_release_manifest
from .target_pack import generate_project_from_target_pack, infer_target_pack, verify_target_pack
from .relink import run_full_relink
from .service import run_service
from .symbolic import bounded_symbolic_compare_files
from .synthetic_corpus import generate_synthetic_corpus, verify_synthetic_corpus
from .test_bundle import create_test_bundle, inspect_test_bundle
from .toolchains import register_toolchain, verify_toolchain
from .tools import snapshot_tools
from .util import load_json
from .work_queue import WorkQueue
from .worker import WorkerLimits, discover_worker_capabilities
from .canonical import dispatch as dispatch_canonical
from .canonical import register_canonical_commands
from .workflow import (
    DecompilationMode,
    FunctionalStatus,
    MatchingStatus,
    SourceStage,
    initialize_function_workflow,
    load_function_workflow,
    update_function_workflow,
)


def _print(value: Any) -> None:
    print(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False))


def _path(value: str) -> Path:
    return Path(value).expanduser()


def _int(value: str) -> int:
    return int(value, 0)


def _json_object(value: str) -> dict[str, Any]:
    parsed = json.loads(value)
    if not isinstance(parsed, dict):
        raise argparse.ArgumentTypeError("value must be a JSON object")
    return parsed


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="x86decomp", description="Evidence-governed x86/x86-64 decompilation toolkit")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="initialize a native PE project")
    p.add_argument("binary", type=_path); p.add_argument("project", type=_path)
    p.add_argument("--reference-binary", action="store_true")
    p = sub.add_parser("inspect-pe", help="parse PE32 or PE32+ metadata"); p.add_argument("binary", type=_path)
    p = sub.add_parser("pdb-inspect", help="inspect an MSF 7.0 PDB and optionally match it to a PE"); p.add_argument("pdb", type=_path); p.add_argument("--pe", type=_path)
    p = sub.add_parser("verify-project"); p.add_argument("project", type=_path)
    p = sub.add_parser("snapshot-tools"); p.add_argument("--output", type=_path); p.add_argument("--ghidra-home", type=_path)

    p = sub.add_parser("compile"); p.add_argument("profile", type=_path); p.add_argument("source", type=_path); p.add_argument("output", type=_path)
    p.add_argument("--report", type=_path); p.add_argument("--extra-arg", action="append", default=[]); p.add_argument("--cache", type=_path)
    p = sub.add_parser("compiler-lab"); p.add_argument("lab", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("objdiff-run"); p.add_argument("manifest", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("toolchain-register"); p.add_argument("registry", type=_path); p.add_argument("toolchain_id"); p.add_argument("family"); p.add_argument("version")
    p.add_argument("--executable", action="append", required=True, help="role=path")
    p = sub.add_parser("toolchain-verify"); p.add_argument("registry", type=_path); p.add_argument("toolchain_id")

    p = sub.add_parser("diff-bytes"); p.add_argument("target", type=_path); p.add_argument("candidate", type=_path); p.add_argument("--report", type=_path); p.add_argument("--max-mismatches", type=int, default=64)
    p = sub.add_parser("diff-function", help="compare a linked PE function to a COFF symbol")
    p.add_argument("pe", type=_path); p.add_argument("rva", type=_int); p.add_argument("size", type=_int); p.add_argument("coff", type=_path); p.add_argument("symbol"); p.add_argument("--report", type=_path)
    p = sub.add_parser("coff-inspect"); p.add_argument("object", type=_path)
    p = sub.add_parser("lib-inspect", help="inspect a COFF archive/static or import library"); p.add_argument("library", type=_path)
    p = sub.add_parser("coff-extract"); p.add_argument("object", type=_path); p.add_argument("symbol"); p.add_argument("output", type=_path); p.add_argument("--size", type=_int)
    p = sub.add_parser("coff-synthesize"); p.add_argument("code", type=_path); p.add_argument("symbol"); p.add_argument("output", type=_path); p.add_argument("--architecture", choices=["x86", "x86_64"], default="x86"); p.add_argument("--relocations", type=_path)
    p = sub.add_parser("coff-comdat-resolve", help="resolve COMDAT groups across COFF objects"); p.add_argument("objects", nargs="+", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("map-inspect", help="parse an MSVC-compatible linker map"); p.add_argument("map", type=_path)
    p = sub.add_parser("layout-reconstruct", help="correlate PE sections, linker map contributions, and COFF objects"); p.add_argument("pe", type=_path); p.add_argument("map", type=_path); p.add_argument("objects", nargs="*", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("image-profile", help="derive a target-specific whole-image profile"); p.add_argument("reference", type=_path); p.add_argument("output", type=_path)
    p = sub.add_parser("image-match", help="compare complete PE images under an explicit layout profile"); p.add_argument("reference", type=_path); p.add_argument("candidate", type=_path); p.add_argument("--profile", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("metadata-scan", help="recover bounded MSVC RTTI, vtables, unwind, TLS, and initializer metadata"); p.add_argument("pe", type=_path); p.add_argument("--object", action="append", type=_path, default=[]); p.add_argument("--map", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("corpus-create-manifest", help="create the bundled compiler ground-truth manifest"); p.add_argument("repository", type=_path); p.add_argument("output", type=_path)
    p = sub.add_parser("corpus-build", help="build a reproducible compiler/version ground-truth corpus"); p.add_argument("manifest", type=_path); p.add_argument("output_directory", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("corpus-verify", help="verify source and output hashes in a ground-truth corpus"); p.add_argument("report", type=_path)
    p = sub.add_parser("corpus-compare", help="compare compiler/version ground-truth corpus reports"); p.add_argument("reports", nargs="+", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("corpus-generate", help="generate a deterministic parameterized C/C++ source corpus"); p.add_argument("output_directory", type=_path); p.add_argument("--cases-per-family", type=int, default=8); p.add_argument("--seed", type=_int, default=0x86DEC0DE); p.add_argument("--c-only", action="store_true"); p.add_argument("--cpp-only", action="store_true"); p.add_argument("--report", type=_path)
    p = sub.add_parser("corpus-generated-verify", help="verify generated corpus source identities"); p.add_argument("report", type=_path)
    p = sub.add_parser("test-bundle-create", help="create a hash-sealed authorized static test bundle"); p.add_argument("output", type=_path); p.add_argument("--artifact", action="append", required=True, help="role=path"); p.add_argument("--authorization", required=True); p.add_argument("--name"); p.add_argument("--description"); p.add_argument("--expected-architecture", choices=["x86", "x86_64"])
    p = sub.add_parser("test-bundle-inspect", help="safely extract, verify, and statically inspect an authorized test bundle"); p.add_argument("bundle", type=_path); p.add_argument("--report", type=_path)

    p = sub.add_parser("disassemble"); p.add_argument("code", type=_path); p.add_argument("--base", type=_int, default=0); p.add_argument("--architecture", choices=["x86", "x86_64"], default="x86"); p.add_argument("--report", type=_path)
    p = sub.add_parser("crosscheck-ghidra"); p.add_argument("instructions_jsonl", type=_path); p.add_argument("code", type=_path); p.add_argument("--base", type=_int, required=True); p.add_argument("--architecture", choices=["x86", "x86_64"], default="x86"); p.add_argument("--report", type=_path)
    p = sub.add_parser("abi-check"); p.add_argument("code", type=_path); p.add_argument("contract", type=_path); p.add_argument("--base", type=_int, default=0); p.add_argument("--report", type=_path)
    p = sub.add_parser("dynamic-validate"); p.add_argument("target", type=_path); p.add_argument("candidate", type=_path); p.add_argument("harness", type=_path); p.add_argument("--target-base", type=_int); p.add_argument("--candidate-base", type=_int); p.add_argument("--report", type=_path)
    p = sub.add_parser("symbolic-validate"); p.add_argument("target", type=_path); p.add_argument("candidate", type=_path); p.add_argument("--architecture", choices=["x86", "x86_64"], default="x86"); p.add_argument("--input-register", action="append", default=[]); p.add_argument("--stack-argument-words", type=int, default=0); p.add_argument("--output-register", action="append"); p.add_argument("--max-steps", type=int, default=1000); p.add_argument("--max-paths", type=int, default=64); p.add_argument("--report", type=_path)
    p = sub.add_parser("angr-validate"); p.add_argument("target", type=_path); p.add_argument("candidate", type=_path); p.add_argument("--architecture", choices=["x86", "x86_64"], default="x86"); p.add_argument("--input-register", action="append", default=[]); p.add_argument("--stack-argument-words", type=int, default=0); p.add_argument("--output-register", action="append"); p.add_argument("--max-steps", type=int, default=1000); p.add_argument("--max-paths", type=int, default=64); p.add_argument("--report", type=_path)
    p = sub.add_parser("symbolic-memory-validate", help="angr comparison with symbolic region bases and alias constraints"); p.add_argument("target", type=_path); p.add_argument("candidate", type=_path); p.add_argument("harness", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("drcov-parse"); p.add_argument("log", type=_path)
    p = sub.add_parser("drcov-run"); p.add_argument("executable", type=_path); p.add_argument("output_directory", type=_path); p.add_argument("--drrun", type=_path); p.add_argument("--program-arg", action="append", default=[]); p.add_argument("--timeout", type=int, default=300); p.add_argument("--report", type=_path)
    p = sub.add_parser("integration-run"); p.add_argument("manifest", type=_path); p.add_argument("--allow-host-execution", action="store_true"); p.add_argument("--report", type=_path)

    p = sub.add_parser("patch-image"); p.add_argument("original", type=_path); p.add_argument("candidate", type=_path); p.add_argument("output", type=_path); p.add_argument("--rva", type=_int, required=True); p.add_argument("--expected-original-sha256"); p.add_argument("--expected-function-sha256"); p.add_argument("--report", type=_path)
    p = sub.add_parser("relink"); p.add_argument("manifest", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("hybrid-generate"); p.add_argument("project", type=_path); p.add_argument("output", type=_path); p.add_argument("--architecture", choices=["x86", "x86_64"], default="x86"); p.add_argument("--asm-format", choices=["bytes", "annotated", "mnemonic"], default="bytes"); p.add_argument("--image-base", type=_int, default=0); p.add_argument("--assembler-command-json"); p.add_argument("--symbol-map"); p.add_argument("--overwrite", action="store_true")

    p = sub.add_parser("workflow-init"); p.add_argument("project", type=_path); p.add_argument("function_id"); p.add_argument("--mode", choices=[m.value for m in DecompilationMode], action="append")
    p = sub.add_parser("workflow-show"); p.add_argument("project", type=_path); p.add_argument("function_id")
    p = sub.add_parser("workflow-update"); p.add_argument("project", type=_path); p.add_argument("function_id"); p.add_argument("--source-stage", choices=[s.value for s in SourceStage]); p.add_argument("--matching-status", choices=[s.value for s in MatchingStatus]); p.add_argument("--functional-status", choices=[s.value for s in FunctionalStatus]); p.add_argument("--candidate"); p.add_argument("--compiler-profile"); p.add_argument("--report-kind"); p.add_argument("--report-path"); p.add_argument("--blocker"); p.add_argument("--allow-regression", action="store_true")

    p = sub.add_parser("db-ingest"); p.add_argument("database", type=_path); p.add_argument("artifact", type=_path); p.add_argument("--image-base", type=_int, default=0)
    p = sub.add_parser("db-query"); p.add_argument("database", type=_path); p.add_argument("sql"); p.add_argument("--parameters-json", default="[]")
    p = sub.add_parser("db-constraint-add"); p.add_argument("database", type=_path); p.add_argument("subject"); p.add_argument("relation"); p.add_argument("object_value"); p.add_argument("provenance"); p.add_argument("--evidence-id"); p.add_argument("--confidence", type=float)
    p = sub.add_parser("db-constraint-conflicts"); p.add_argument("database", type=_path); p.add_argument("subject"); p.add_argument("relation")
    p = sub.add_parser("db-constraint-accept"); p.add_argument("database", type=_path); p.add_argument("constraint_id", type=int)

    p = sub.add_parser("work-create"); p.add_argument("database", type=_path); p.add_argument("function_id"); p.add_argument("mode", choices=["matching", "functional"]); p.add_argument("kind"); p.add_argument("instructions"); p.add_argument("--validator", action="append", required=True); p.add_argument("--priority", type=int, default=0)
    p = sub.add_parser("work-next"); p.add_argument("database", type=_path); p.add_argument("--mode", choices=["matching", "functional"])
    p = sub.add_parser("work-claim"); p.add_argument("database", type=_path); p.add_argument("task_id"); p.add_argument("assignee")
    p = sub.add_parser("work-propose"); p.add_argument("database", type=_path); p.add_argument("task_id"); p.add_argument("proposal", type=_path); p.add_argument("--evidence", action="append", required=True)
    p = sub.add_parser("work-validate"); p.add_argument("database", type=_path); p.add_argument("task_id"); p.add_argument("validator"); p.add_argument("report_path"); p.add_argument("--passed", action="store_true")

    for name in ("mcp-tools", "mcp-read", "mcp-propose", "mcp-commit"):
        p = sub.add_parser(name)
        p.add_argument("--url")
        p.add_argument("--command-json")
        if name != "mcp-tools": p.add_argument("project", type=_path)
        if name in ("mcp-read", "mcp-propose"): p.add_argument("tool"); p.add_argument("arguments", type=_json_object)
        if name == "mcp-propose": p.add_argument("--allow-tool", action="append", required=True); p.add_argument("--rationale", required=True); p.add_argument("--evidence", action="append", required=True)
        if name == "mcp-commit": p.add_argument("approval_hash"); p.add_argument("--allow-tool", action="append", required=True)

    p = sub.add_parser("benchmark-run"); p.add_argument("manifest", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("serve"); p.add_argument("project", type=_path); p.add_argument("--host", default="127.0.0.1"); p.add_argument("--port", type=int, default=8765)

    p = sub.add_parser("evidence-add"); p.add_argument("project", type=_path); p.add_argument("--kind", choices=[k.value for k in EvidenceKind], required=True); p.add_argument("--source", required=True); p.add_argument("--locator", required=True); p.add_argument("--assertion", required=True); p.add_argument("--independent-group", required=True); p.add_argument("--file", type=_path); p.add_argument("--id")
    p = sub.add_parser("claim-create"); p.add_argument("project", type=_path); p.add_argument("--subject", required=True); p.add_argument("--predicate", required=True); p.add_argument("--object", dest="object_value", required=True); p.add_argument("--evidence", action="append", default=[]); p.add_argument("--id")
    p = sub.add_parser("claim-attach"); p.add_argument("project", type=_path); p.add_argument("claim_id"); p.add_argument("evidence_id")
    p = sub.add_parser("claim-verify"); p.add_argument("project", type=_path); p.add_argument("claim_id")
    p = sub.add_parser("claim-contradict"); p.add_argument("project", type=_path); p.add_argument("claim_id"); p.add_argument("evidence_id")
    p = sub.add_parser("memory-add"); p.add_argument("project", type=_path); p.add_argument("--actor", required=True); p.add_argument("--category", required=True); p.add_argument("--summary", required=True); p.add_argument("--details-json", default="{}"); p.add_argument("--evidence", action="append", default=[])
    p = sub.add_parser("memory-verify"); p.add_argument("project", type=_path)
    p = sub.add_parser("memory-render"); p.add_argument("project", type=_path)
    p = sub.add_parser("artifact-import"); p.add_argument("project", type=_path); p.add_argument("exported_dir", type=_path)
    p = sub.add_parser("artifact-verify"); p.add_argument("artifact_dir", type=_path)
    p = sub.add_parser("decompme-pack"); p.add_argument("artifact_dir", type=_path); p.add_argument("output_dir", type=_path); p.add_argument("--overwrite", action="store_true")

    p = sub.add_parser("ghidra-export"); p.add_argument("binary", type=_path); p.add_argument("ghidra_project_dir", type=_path); p.add_argument("ghidra_project_name"); p.add_argument("output_dir", type=_path); p.add_argument("--scripts-dir", type=_path, default=Path("ghidra_scripts")); p.add_argument("--ghidra-home", type=_path); p.add_argument("--overwrite", action="store_true"); p.add_argument("--selector", default="all"); p.add_argument("--timeout", type=int, default=3600); p.add_argument("--report", type=_path); p.add_argument("--print-command", action="store_true")

    p = sub.add_parser("target-pack-infer", help="infer a fact-preserving target pack and template plan")
    p.add_argument("primary_image", type=_path); p.add_argument("output_directory", type=_path); p.add_argument("--name")
    p.add_argument("--pdb", type=_path); p.add_argument("--map", type=_path); p.add_argument("--object", action="append", type=_path, default=[]); p.add_argument("--library", action="append", type=_path, default=[]); p.add_argument("--rebuilt-image", type=_path); p.add_argument("--decisions", type=_path); p.add_argument("--reference-artifacts", action="store_true")
    p = sub.add_parser("target-pack-verify"); p.add_argument("target_pack", type=_path)
    p = sub.add_parser("project-from-target"); p.add_argument("target_pack", type=_path); p.add_argument("project", type=_path); p.add_argument("--reference-binary", action="store_true")
    p = sub.add_parser("template-derive", help="derive a grounded project-template contract from a target pack"); p.add_argument("target_pack", type=_path)
    p = sub.add_parser("template-materialize", help="materialize the grounded working layout for an existing target project"); p.add_argument("project", type=_path)

    p = sub.add_parser("project-check"); p.add_argument("project", type=_path)
    p = sub.add_parser("project-migrate"); p.add_argument("project", type=_path); p.add_argument("--dry-run", action="store_true"); p.add_argument("--backup", type=_path)
    p = sub.add_parser("project-backup"); p.add_argument("project", type=_path); p.add_argument("output", type=_path)
    p = sub.add_parser("project-restore"); p.add_argument("archive", type=_path); p.add_argument("destination", type=_path)
    p = sub.add_parser("project-repair"); p.add_argument("project", type=_path); p.add_argument("--apply", action="store_true")
    p = sub.add_parser("project-gc"); p.add_argument("project", type=_path); p.add_argument("--apply", action="store_true")

    p = sub.add_parser("pipeline-create"); p.add_argument("project", type=_path); p.add_argument("output", type=_path); p.add_argument("--without-ghidra", action="store_true")
    p = sub.add_parser("pipeline-run"); p.add_argument("project", type=_path); p.add_argument("manifest", type=_path); p.add_argument("--continue-on-failure", action="store_true")
    p = sub.add_parser("pipeline-status"); p.add_argument("project", type=_path); p.add_argument("pipeline_id")
    p = sub.add_parser("pipeline-cancel"); p.add_argument("project", type=_path); p.add_argument("pipeline_id"); p.add_argument("--stage-id")
    p = sub.add_parser("pipeline-retry"); p.add_argument("project", type=_path); p.add_argument("pipeline_id"); p.add_argument("stage_id"); p.add_argument("--cascade", action="store_true")
    p = sub.add_parser("pipeline-recover", help="reset jobs with stale durable runner heartbeats"); p.add_argument("project", type=_path); p.add_argument("--pipeline-id"); p.add_argument("--stale-seconds", type=int, default=600)

    sub.add_parser("worker-capabilities")
    p = sub.add_parser("compile-worker"); p.add_argument("profile", type=_path); p.add_argument("source", type=_path); p.add_argument("output", type=_path); p.add_argument("--isolation", choices=["local_bounded", "container"], default="local_bounded"); p.add_argument("--container-image"); p.add_argument("--cache", type=_path); p.add_argument("--report", type=_path)

    p = sub.add_parser("linker-plan"); p.add_argument("pe", type=_path); p.add_argument("map", type=_path); p.add_argument("objects", nargs="+", type=_path); p.add_argument("--library", action="append", type=_path, default=[]); p.add_argument("--linker", default="lld-link"); p.add_argument("--output-image", default="build/reconstructed.exe"); p.add_argument("--report", type=_path); p.add_argument("--write-relink-manifest", type=_path)
    p = sub.add_parser("cpp-recover"); p.add_argument("pe", type=_path); p.add_argument("--metadata-report", type=_path); p.add_argument("--object", action="append", type=_path, default=[]); p.add_argument("--map", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("harness-generate"); p.add_argument("abi_contract", type=_path); p.add_argument("output", type=_path); p.add_argument("--pointer-parameters", type=_path); p.add_argument("--no-observe-pointers", action="store_true"); p.add_argument("--max-instructions", type=int, default=100000); p.add_argument("--timeout-ms", type=int, default=1000)
    p = sub.add_parser("convergence-analyze"); p.add_argument("reference", type=_path); p.add_argument("candidate", type=_path); p.add_argument("--profile", type=_path); p.add_argument("--previous", type=_path); p.add_argument("--report", type=_path); p.add_argument("--history", type=_path)

    p = sub.add_parser("reproduce-create"); p.add_argument("project", type=_path); p.add_argument("output", type=_path); p.add_argument("--required-tool", action="append")
    p = sub.add_parser("reproduce-verify"); p.add_argument("project", type=_path); p.add_argument("manifest", type=_path)
    p = sub.add_parser("release-gate", help="evaluate explicit target release acceptance contracts"); p.add_argument("project", type=_path); p.add_argument("--reproduction-manifest", type=_path); p.add_argument("--security-report", type=_path); p.add_argument("--convergence-report", type=_path); p.add_argument("--require-workflows", action="store_true"); p.add_argument("--require-verified-claims", action="store_true"); p.add_argument("--require-succeeded-pipelines", action="store_true"); p.add_argument("--report", type=_path)
    p = sub.add_parser("security-audit"); p.add_argument("root", type=_path); p.add_argument("--report", type=_path)
    p = sub.add_parser("dependency-audit", help="run an installed pip-audit adapter and preserve exact findings"); p.add_argument("--executable", default="pip-audit"); p.add_argument("--timeout", type=int, default=300); p.add_argument("--report", type=_path)
    p = sub.add_parser("sbom-generate"); p.add_argument("output", type=_path)
    p = sub.add_parser("release-manifest-verify"); p.add_argument("root", type=_path); p.add_argument("--manifest", type=_path)
    p = sub.add_parser("content-put"); p.add_argument("store", type=_path); p.add_argument("file", type=_path); p.add_argument("--media-type", default="application/octet-stream"); p.add_argument("--reference"); p.add_argument("--kind", default="artifact"); p.add_argument("--owner", default="user")
    p = sub.add_parser("content-verify"); p.add_argument("store", type=_path)
    register_canonical_commands(sub)
    return parser


def _mcp_client(args: argparse.Namespace) -> Any:
    if bool(args.url) == bool(args.command_json):
        raise ValueError("exactly one of --url or --command-json is required")
    if args.url:
        return StreamableHTTPMCPClient(args.url)
    command = json.loads(args.command_json)
    if not isinstance(command, list) or not all(isinstance(item, str) for item in command):
        raise ValueError("--command-json must be a JSON string array")
    return StdioMCPClient(command)


def _run(args: argparse.Namespace) -> Any:
    if getattr(args, "_canonical_catalog", False) or getattr(args, "_canonical_owner", None):
        return dispatch_canonical(args)
    c = args.command
    if c == "init": return initialize_project(args.binary, args.project, copy_binary=not args.reference_binary)
    if c == "inspect-pe": return parse_pe(args.binary).to_dict()
    if c == "pdb-inspect": return parse_pdb(args.pdb, pe_path=args.pe).to_dict()
    if c == "verify-project": return verify_project(args.project)
    if c == "snapshot-tools": return snapshot_tools(args.output, args.ghidra_home)
    if c == "compile": return run_compiler_profile(args.profile, args.source, args.output, report_path=args.report, extra_arguments=args.extra_arg, cache_directory=args.cache)
    if c == "compiler-lab": return run_compiler_lab(args.lab, report_path=args.report)
    if c == "objdiff-run": return run_objdiff_manifest(args.manifest, report_path=args.report)
    if c == "toolchain-register":
        values = {}
        for item in args.executable:
            role, separator, value = item.partition("=")
            if not separator: raise ValueError("--executable must use role=path")
            values[role] = Path(value)
        return register_toolchain(args.registry, toolchain_id=args.toolchain_id, family=args.family, version=args.version, executables=values)
    if c == "toolchain-verify": return verify_toolchain(args.registry, args.toolchain_id)
    if c == "diff-bytes": return compare_files(args.target, args.candidate, max_mismatches=args.max_mismatches, report_path=args.report)
    if c == "diff-function": return compare_pe_function_to_coff_symbol(pe_path=args.pe, function_rva=args.rva, function_size=args.size, coff_path=args.coff, symbol_name=args.symbol, report_path=args.report)
    if c == "coff-inspect": return parse_coff(args.object).to_dict()
    if c == "lib-inspect": return parse_coff_archive(args.library).to_dict()
    if c == "coff-extract":
        obj = parse_coff(args.object); extracted = extract_symbol(obj, args.symbol, size=args.size); args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_bytes(extracted.data); return extracted.to_dict(obj.machine)
    if c == "coff-synthesize":
        relocs = []
        if args.relocations:
            for item in load_json(args.relocations): relocs.append(CoffRelocation(offset=int(item["offset"]), symbol_index=int(item.get("symbol_index", 0)), type=int(item["type"]), symbol_name=item.get("symbol_name")))
        return write_synthetic_coff(args.output, code=args.code.read_bytes(), symbol_name=args.symbol, machine=0x014C if args.architecture == "x86" else 0x8664, relocations=relocs)
    if c == "coff-comdat-resolve":
        result = resolve_comdats([parse_coff(path) for path in args.objects]).to_dict()
        if args.report:
            from .util import write_json; write_json(args.report, result)
        return result
    if c == "map-inspect": return parse_msvc_map(args.map).to_dict()
    if c == "layout-reconstruct": return reconstruct_linker_layout(args.pe, args.map, object_paths=args.objects, report_path=args.report)
    if c == "image-profile": return derive_layout_profile(args.reference, output=args.output)
    if c == "image-match": return compare_whole_images(args.reference, args.candidate, profile_path=args.profile, report_path=args.report)
    if c == "metadata-scan": return analyze_msvc_metadata(args.pe, object_paths=args.object, map_path=args.map, report_path=args.report)
    if c == "corpus-create-manifest": return create_builtin_manifest(args.repository, output=args.output)
    if c == "corpus-build": return build_ground_truth_corpus(args.manifest, args.output_directory, report_path=args.report)
    if c == "corpus-verify": return verify_ground_truth_corpus(args.report)
    if c == "corpus-compare": return compare_ground_truth_corpora(args.reports, report_path=args.report)
    if c == "corpus-generate":
        if args.c_only and args.cpp_only: raise ValueError("--c-only and --cpp-only are mutually exclusive")
        return generate_synthetic_corpus(args.output_directory, cases_per_family=args.cases_per_family, seed=args.seed, include_c=not args.cpp_only, include_cpp=not args.c_only, report_path=args.report)
    if c == "corpus-generated-verify": return verify_synthetic_corpus(args.report)
    if c == "test-bundle-create":
        artifacts = []
        for item in args.artifact:
            role, separator, value = item.partition("=")
            if not separator or not role or not value: raise ValueError("--artifact must use role=path")
            artifacts.append((role, Path(value)))
        return create_test_bundle(args.output, artifacts=artifacts, authorization_statement=args.authorization, name=args.name, description=args.description, expected_architecture=args.expected_architecture)
    if c == "test-bundle-inspect": return inspect_test_bundle(args.bundle, report_path=args.report)
    if c == "disassemble":
        result = {"instructions": [record.to_dict() for record in decode_instructions(args.code.read_bytes(), base_address=args.base, architecture=args.architecture)]}
        if args.report:
            from .util import write_json; write_json(args.report, result)
        return result
    if c == "crosscheck-ghidra": return cross_check_ghidra_instructions(args.instructions_jsonl, args.code.read_bytes(), base_address=args.base, architecture=args.architecture, report_path=args.report)
    if c == "abi-check": return validate_abi(args.code.read_bytes(), load_abi_contract(args.contract), base_address=args.base, report_path=args.report)
    if c == "dynamic-validate": return differential_validate_files(args.target, args.candidate, args.harness, target_base=args.target_base, candidate_base=args.candidate_base, report_path=args.report)
    if c == "symbolic-validate": return bounded_symbolic_compare_files(args.target, args.candidate, architecture=args.architecture, input_registers=tuple(args.input_register), stack_argument_words=args.stack_argument_words, output_registers=None if args.output_register is None else tuple(args.output_register), max_steps=args.max_steps, max_paths=args.max_paths, report_path=args.report)
    if c == "angr-validate": return angr_bounded_compare_files(args.target, args.candidate, architecture=args.architecture, input_registers=tuple(args.input_register), stack_argument_words=args.stack_argument_words, output_registers=None if args.output_register is None else tuple(args.output_register), max_steps=args.max_steps, max_paths=args.max_paths, report_path=args.report)
    if c == "symbolic-memory-validate": return angr_memory_alias_compare_files(args.target, args.candidate, args.harness, report_path=args.report)
    if c == "drcov-parse": return parse_drcov_text(args.log)
    if c == "drcov-run": return run_drcov_trace(args.executable, program_arguments=args.program_arg, drrun=args.drrun, output_directory=args.output_directory, timeout_seconds=args.timeout, report_path=args.report)
    if c == "integration-run": return run_integration_scenarios(args.manifest, allow_host_execution=args.allow_host_execution, report_path=args.report)
    if c == "patch-image": return patch_pe_function(args.original, args.candidate, args.output, function_rva=args.rva, expected_original_sha256=args.expected_original_sha256, expected_function_sha256=args.expected_function_sha256, report_path=args.report)
    if c == "relink": return run_full_relink(args.manifest, report_path=args.report)
    if c == "hybrid-generate":
        assembler_command = None if args.assembler_command_json is None else json.loads(args.assembler_command_json)
        if assembler_command is not None and (not isinstance(assembler_command, list) or not assembler_command or not all(isinstance(item, str) for item in assembler_command)):
            raise ValueError("--assembler-command-json must be a non-empty JSON array of strings")
        symbol_map = None if args.symbol_map is None else json.loads(Path(args.symbol_map).read_text(encoding="utf-8"))
        return generate_hybrid_project(args.project, args.output, architecture=args.architecture, overwrite=args.overwrite, asm_format=args.asm_format, image_base=args.image_base, assembler_command=assembler_command, symbol_map=symbol_map)
    if c == "workflow-init": return initialize_function_workflow(args.project, function_id=args.function_id, modes=None if not args.mode else {DecompilationMode(item) for item in args.mode}).to_dict()
    if c == "workflow-show": return load_function_workflow(args.project, args.function_id).to_dict()
    if c == "workflow-update": return update_function_workflow(args.project, args.function_id, source_stage=None if args.source_stage is None else SourceStage(args.source_stage), matching_status=None if args.matching_status is None else MatchingStatus(args.matching_status), functional_status=None if args.functional_status is None else FunctionalStatus(args.functional_status), active_candidate=args.candidate, compiler_profile=args.compiler_profile, report_kind=args.report_kind, report_path=args.report_path, blocker=args.blocker, allow_regression=args.allow_regression).to_dict()
    if c.startswith("db-"):
        with AnalysisDatabase(args.database) as db:
            if c == "db-ingest": return db.ingest_function_artifact(args.artifact, image_base=args.image_base)
            if c == "db-query": return db.query(args.sql, json.loads(args.parameters_json))
            if c == "db-constraint-add": return {"constraint_id": db.add_type_constraint(subject_entity=args.subject, relation=args.relation, object_value=args.object_value, provenance=args.provenance, evidence_id=args.evidence_id, confidence=args.confidence)}
            if c == "db-constraint-conflicts": return db.detect_constraint_conflicts(args.subject, args.relation)
            if c == "db-constraint-accept": db.accept_constraint(args.constraint_id); return {"accepted": args.constraint_id}
    if c.startswith("work-"):
        queue = WorkQueue(args.database)
        try:
            if c == "work-create": return queue.create(function_id=args.function_id, mode=args.mode, kind=args.kind, instructions=args.instructions, required_validators=args.validator, priority=args.priority)
            if c == "work-next": return queue.next(mode=args.mode)
            if c == "work-claim": return queue.claim(args.task_id, args.assignee)
            if c == "work-propose": return queue.propose(args.task_id, load_json(args.proposal), args.evidence)
            if c == "work-validate": return queue.record_validator(args.task_id, args.validator, args.report_path, args.passed)
        finally: queue.close()
    if c.startswith("mcp-"):
        client = _mcp_client(args)
        try:
            if c == "mcp-tools": return [{"name": t.name, "description": t.description, "input_schema": t.input_schema} for t in client.list_tools()]
            gateway = GhidraMCPGateway(args.project, client, mutation_allowlist=set(getattr(args, "allow_tool", []) or []))
            if c == "mcp-read": return gateway.read(args.tool, args.arguments)
            if c == "mcp-propose": return gateway.propose_mutation(tool=args.tool, arguments=args.arguments, rationale=args.rationale, evidence_ids=args.evidence)
            if c == "mcp-commit": return gateway.commit_mutation(args.approval_hash)
        finally: client.close()
    if c == "benchmark-run": return run_benchmark_corpus(args.manifest, report_path=args.report)
    if c == "serve": run_service(args.project, host=args.host, port=args.port); return {"stopped": True}
    if c == "evidence-add": return EvidenceStore(args.project).add_evidence(kind=EvidenceKind(args.kind), source=args.source, locator=args.locator, assertion=args.assertion, independent_group=args.independent_group, file_path=args.file, evidence_id=args.id).to_dict()
    if c == "claim-create": return EvidenceStore(args.project).create_claim(subject=args.subject, predicate=args.predicate, object_value=args.object_value, evidence_ids=args.evidence, claim_id=args.id).to_dict()
    if c == "claim-attach": return EvidenceStore(args.project).attach_evidence(args.claim_id, args.evidence_id).to_dict()
    if c == "claim-verify": return EvidenceStore(args.project).verify_claim(args.claim_id).to_dict()
    if c == "claim-contradict": return EvidenceStore(args.project).add_contradiction(args.claim_id, args.evidence_id).to_dict()
    if c == "memory-add": return ProjectMemory(args.project).append(actor=args.actor, category=args.category, summary=args.summary, details=json.loads(args.details_json), evidence_ids=args.evidence)
    if c == "memory-verify": return ProjectMemory(args.project).verify()
    if c == "memory-render": return {"path": str(ProjectMemory(args.project).rendered_path), "content": ProjectMemory(args.project).render()}
    if c == "artifact-import":
        destination = import_function_artifact(args.project, args.exported_dir); return {"artifact_dir": str(destination), "verification": verify_function_artifact(destination)}
    if c == "artifact-verify": return verify_function_artifact(args.artifact_dir)
    if c == "decompme-pack": return create_decompme_packet(args.artifact_dir, args.output_dir, overwrite=args.overwrite)
    if c == "ghidra-export":
        command = build_export_command(binary=args.binary, ghidra_project_dir=args.ghidra_project_dir, ghidra_project_name=args.ghidra_project_name, scripts_dir=args.scripts_dir, output_dir=args.output_dir, ghidra_home=args.ghidra_home, overwrite=args.overwrite, function_selector=args.selector)
        if args.print_command: return {"command": command}
        return run_export(command, timeout_seconds=args.timeout, report_path=args.report)
    if c == "target-pack-infer":
        decisions = None if args.decisions is None else load_json(args.decisions)
        return infer_target_pack(args.primary_image, args.output_directory, name=args.name, pdb=args.pdb, linker_map=args.map, objects=args.object, libraries=args.library, rebuilt_image=args.rebuilt_image, decisions=decisions, copy_artifacts=not args.reference_artifacts)
    if c == "target-pack-verify": return verify_target_pack(args.target_pack)
    if c == "project-from-target": return generate_project_from_target_pack(args.target_pack, args.project, copy_binary=not args.reference_binary)
    if c == "template-derive": return derive_template_contract(args.target_pack)
    if c == "template-materialize": return materialize_project_template(args.project)
    if c == "project-check": return check_project_state(args.project).to_dict()
    if c == "project-migrate": return migrate_project(args.project, dry_run=args.dry_run, backup_path=args.backup)
    if c == "project-backup": return create_project_backup(args.project, args.output)
    if c == "project-restore": return restore_project_backup(args.archive, args.destination)
    if c == "project-repair": return repair_project_state(args.project, dry_run=not args.apply)
    if c == "project-gc": return project_gc(args.project, dry_run=not args.apply)
    if c == "pipeline-create": return create_default_pipeline(args.project, args.output, include_ghidra=not args.without_ghidra)
    if c.startswith("pipeline-"):
        with Orchestrator(args.project) as orchestrator:
            if c == "pipeline-run": return orchestrator.run(args.manifest, stop_on_failure=not args.continue_on_failure)
            if c == "pipeline-status": return orchestrator.status(args.pipeline_id)
            if c == "pipeline-cancel": return orchestrator.cancel(args.pipeline_id, args.stage_id)
            if c == "pipeline-retry": return orchestrator.retry(args.pipeline_id, args.stage_id, cascade=args.cascade)
            if c == "pipeline-recover": return orchestrator.recover_stale_jobs(pipeline_id=args.pipeline_id, stale_seconds=args.stale_seconds)
    if c == "worker-capabilities": return discover_worker_capabilities()
    if c == "compile-worker": return run_compiler_worker(args.profile, args.source, args.output, isolation=args.isolation, container_image=args.container_image, cache_directory=args.cache, report_path=args.report)
    if c == "linker-plan":
        plan = build_linker_reconstruction_plan(args.pe, args.map, object_paths=args.objects, library_paths=args.library, linker=args.linker, output_path=args.output_image, report_path=args.report)
        if args.write_relink_manifest is not None: write_relink_manifest_from_plan(plan, args.write_relink_manifest)
        return plan
    if c == "cpp-recover": return recover_cpp_model(args.pe, metadata_report=args.metadata_report, object_paths=args.object, map_path=args.map, report_path=args.report)
    if c == "harness-generate": return generate_execution_harness_from_files(args.abi_contract, args.output, pointer_parameters_path=args.pointer_parameters, observe_pointer_parameters=not args.no_observe_pointers, max_instructions=args.max_instructions, timeout_ms=args.timeout_ms)
    if c == "convergence-analyze":
        result = analyze_image_convergence(args.reference, args.candidate, profile_path=args.profile, previous_report=args.previous, report_path=args.report)
        if args.history is not None: result["history"] = append_convergence_history(args.history, result)
        return result
    if c == "reproduce-create": return build_reproduction_manifest(args.project, output=args.output, required_tools=args.required_tool)
    if c == "reproduce-verify": return verify_reproduction_manifest(args.project, args.manifest)
    if c == "release-gate": return evaluate_release_gate(args.project, reproduction_manifest=args.reproduction_manifest, security_report=args.security_report, convergence_report=args.convergence_report, require_workflows=args.require_workflows, require_verified_claims=args.require_verified_claims, require_succeeded_pipelines=args.require_succeeded_pipelines, report_path=args.report)
    if c == "security-audit": return audit_source_tree(args.root, report_path=args.report)
    if c == "dependency-audit": return run_dependency_vulnerability_audit(executable=args.executable, report_path=args.report, timeout_seconds=args.timeout)
    if c == "sbom-generate": return generate_sbom(args.output)
    if c == "release-manifest-verify": return verify_release_manifest(args.root, args.manifest)
    if c == "content-put":
        store = ContentStore(args.store); artifact = store.put_file(args.file, media_type=args.media_type)
        if args.reference: store.add_reference(args.reference, artifact.digest, kind=args.kind, owner=args.owner)
        return artifact.to_dict(root=store.root)
    if c == "content-verify": return ContentStore(args.store).verify()
    raise AssertionError(f"unhandled command: {c}")


def main(argv: list[str] | None = None) -> int:
    effective_argv = list(sys.argv[1:] if argv is None else argv)
    try:
        parser = _build_parser()
        args = parser.parse_args(effective_argv)
        result = _run(args)
        _print(result)
        return 0
    except (X86DecompError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
