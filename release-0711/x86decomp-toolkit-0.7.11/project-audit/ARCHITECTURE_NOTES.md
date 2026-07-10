# Architecture Notes — x86decomp-toolkit 0.7.11

STATUS: INITIAL MODEL (Phase 4), built from pyproject.toml, Makefile, README.md, package listing, and a complete read of src/x86decomp/cli.py, __init__.py, __main__.py. Everything below is Probable unless marked Verified. Update as per-file audits land.

## Entry points (Verified)
- Console script `x86decomp = x86decomp.cli:main` (pyproject) and `python -m x86decomp` (`__main__.py` → `cli.main`).
- Second package in-tree: `test-suite/` = `x86decomp_testkit` with its own CLI `x86decomp-test` (per README; pyproject for it lives in test-suite/ — verify in B09).
- Public API surface (`__init__.py`, Verified): PE32Image/PE64Image, parse_pe/parse_pe32/parse_pe64, initialize_project, verify_project, workflow enums. `__version__ = "0.7.11"` matches pyproject.

## Command registration and dispatch (Verified for cli.py; canonical.py pending)
- `cli._build_parser()` registers ~100 flat argparse subcommands, then `canonical.register_canonical_commands(sub)` adds the "canonical" group/action routes (README's claimed 59 groups / 239 routes — to be counted mechanically in Phase 6).
- `cli._run()` is a giant if-chain mapping command name → library function call; canonical commands short-circuit to `canonical.dispatch`. Two compatibility aliases (`hybrid-generate`, `project-check`) bridge flat names onto canonical routes.
- Output contract: every command's return value printed as sorted, indented JSON to stdout; exit 0. Handled errors (X86DecompError, ValueError, KeyError, TypeError, JSONDecodeError) print `error: ...` to stderr, exit 2. OSError/FileNotFoundError NOT in the handled set (potential traceback on missing input files — flagged for verification in Phase 10, candidate CLI/COR finding).

## Module structure (src/x86decomp, 117 modules, ~31k LOC) (Verified listing; roles Probable)
- Binary parsing layer: pe.py (PE64), pe32.py, coff.py, coff_archive.py, pdb.py, binary_reader.py, msvc_metadata.py — stdlib-only parsers for adversarial input (key security review surface).
- Analysis/validation: disassembly.py (capstone optional), symbolic.py (z3 optional), angr_backend.py, dynamic.py (unicorn), dynamorio.py (drcov), diffing.py, exe_diff.py, image_match.py, convergence.py, abi.py, harness_generator.py.
- Reconstruction pipeline: reconstruction/ (12 modules incl. acceleration.py at 1,984 LOC — largest file), linker_layout.py, linker_reconstruction.py, relink.py, patching.py, cpp_recovery.py, hybrid.py, native/ (11 modules: PE reconstruction, staging, closed loop, windows_tools), assembly/ (7 modules).
- Evidence governance: evidence.py, memory.py, models.py, contracts.py, governance/ (15 modules: campaigns, candidates, hypotheses, proofs, consensus, knowledge_graph, plugins, workers, store...), analysis_db.py (SQL — verify injection surface for db-query which takes raw SQL by design), work_queue.py, worker.py.
- External tool integration: ghidra.py (headless export), objdiff_adapter.py, decompme.py, mcp.py (MCP client/gateway with mutation allowlist + approval-hash commit flow), local_llm/ (4 modules; transport), tools.py, toolchains.py, compiler.py, compiler_lab.py, compiler_worker.py (isolation modes local_bounded|container).
- Project/data plane: project.py, project_state.py (backup/restore/migrate/repair/gc), project_template.py, target_pack.py, content_store.py (content-addressed store), artifacts.py, store_utils.py.
- Release/repro: release_gate.py, reproducibility.py, security_audit.py (SBOM, release-manifest-verify, pip-audit adapter), ground_truth.py, synthetic_corpus.py, benchmarks.py, test_bundle.py (hash-sealed authorized bundles — RE-ethics mechanism), integration.py (has --allow-host-execution gate).
- Service/orchestration: service.py (fastapi, default 127.0.0.1:8765), orchestrator.py (pipelines with heartbeat recovery), workflow.py (function-level state machine), util.py, errors.py, canonical.py (route registry).

## Data flow (Probable, from CLI signatures)
binary (.exe/.dll) → init/inspect (pe/pe32) → project dir with evidence store, claims, memory journal → analysis (disassemble, metadata-scan, cpp-recover) → candidate source → compile (profiles/toolchains) → COFF → diff (bytes/function/objdiff) → image-match/convergence → patch/relink → release-gate. Reports are JSON files written via `--report` throughout; provenance via content_store + evidence IDs.

## Trust boundaries (Probable — key audit surfaces)
1. Untrusted binaries into pure-Python parsers (pe/pe32/coff/pdb/archive).
2. Subprocess boundaries: ghidra headless, drrun, compilers, objdiff, pip-audit, local LLM transport, container isolation.
3. Network: service.py (localhost default), StreamableHTTPMCPClient (user-supplied URL), local_llm transport.
4. db-query accepts raw SQL against project DB (by design; scriptability vs safety trade-off — assess).
5. test_bundle authorization statements + hash sealing; integration-run gated by --allow-host-execution flag.

## Configuration flow (Probable)
No global config file observed yet; per-command JSON manifests/profiles + schemas/ (97 JSON schemas). Env vars unknown — inventory in Phase 6.

## Test organization (Verified counts)
tests/ (102 files, subdirs mirror subsystems: governance, native, reconstruction, assembly) run via scripts/run-pytest-partitions.py with PYTEST_DISABLE_PLUGIN_AUTOLOAD=1. test-suite/ (115 files) is a separately packaged live verification harness (x86decomp_testkit) with adapters, feature catalog JSON, its own docs/. Root x86decomp-test.json appears to be a machine-written result file (mtime hours after tree) — classification pending.

## Open questions carried forward
- OQ-1: canonical.py mechanism and exact route/group counts vs README claim.
- OQ-2: Which manifest does scripts/source_hashes.py verify — MANIFEST.sha256 or ALL_FILE_MANIFEST_0.7.11.json? (REPO-001 dependency)
- OQ-3: Is x86decomp-test.json a committed test artifact that should be gitignored (test-suite/x86decomp-test.json IS ignored, root copy is not)?
- OQ-4: Why does root-level `.x86decomp-test-tools/` exist when .gitignore only covers `test-suite/.x86decomp-test-tools/`?
- OQ-5: service.py auth story (any token?), mcp.py approval-hash mechanics.
- OQ-6: dist/ contains 2 files despite being gitignored — stale build artifacts in release tree?
