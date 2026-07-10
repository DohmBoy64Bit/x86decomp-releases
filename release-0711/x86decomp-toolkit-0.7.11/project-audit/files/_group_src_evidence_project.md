# Grouped audit — evidence, project, orchestration & tooling modules (B06g-core)

Depth: full read of the security-critical (worker.py, project_state.py, integration.py) per B06 deep dives (R-014/R-015); others structurally digested with full risk-pattern sweep. Hashes in FILE_INVENTORY.csv.

## evidence.py (264) — Evidence store + strict three-independent-source claim verification
EvidenceStore with _validate_id; enforces the three-independent-group gate that is the project's core evidence-governance mechanism. verify_claim requires ≥3 independent groups (matches FEATURE_PARITY/SKILL claims). Uses contracts primitives. tests/test_evidence.py green (R-013). Central to the product thesis; implementation matches documented policy. No findings beyond DOC-001. Status: Audited — complete.

## memory.py (138) — Append-only, hash-chained project memory
ProjectMemory.append/verify/render; hash chain for tamper evidence. Degenerate docstrings ('Append append...', 'Verify verify...', 'Render render...') — DOC-001 instances (memory.py:44,77,102). tests/test_memory.py green. No functional findings. Status: Audited — complete.

## project.py (232) — Project init, architecture dispatch, integrity verification
initialize_project/verify_project/require_valid_project; _resolve_binary_path. Dispatches PE32/PE32+ via audited parsers. tests/test_project.py present. No findings. Status: Audited — complete.

## project_state.py (570) — Transactional state DB, migrations, backup, recovery
FULL READ (B06). create_project_backup (tar PAX, refuses output inside root), restore_project_backup (SEC-hardened: rejects absolute/.., symlink/hardlink/dev members, member-count 100k cap, per-member 2GiB + total 8GiB caps, single-root enforcement, extractall(filter="data")), _migration_2_to_3, project_gc/repair. **Model-safe tar restore.** No findings beyond DOC-001. Status: Audited — complete.

## project_template.py (194) — Grounded project-template generation
derive_template_contract/materialize_project_template; subprocess for a project helper (argv). Generates layout from verified target pack. No findings. Status: Audited — complete.

## content_store.py (389) — Content-addressed immutable artifact storage
StoredArtifact/ContentStore put_file/add_reference/verify; sha256-addressed; unlink on failure paths. Degenerate 'Verify verify...' docstring (content_store.py:200, DOC-001). Immutable-by-hash design sound. tests/test_artifacts.py-adjacent coverage. No functional findings. Status: Audited — complete.

## store_utils.py (23) — Shared SQLite persistence helpers
decode_json_fields. Trivial, correct. Status: Audited — complete.

## artifacts.py (118) — Function artifact import + validation
function_id_from_rva/validate_function_manifest/import_function_artifact/verify_function_artifact; rmtree on cleanup of a temp/dest (import path) — scoped to destination. No findings. Status: Audited — complete.

## work_queue.py (131) — Evidence-gated human/AI work queue
WorkQueue create/next/claim/propose/record_validator; validator-acceptance rules; parameterized SQL. Degenerate 'Create create...' docstring (work_queue.py:49). No functional findings. Status: Audited — complete.

## worker.py (365) — Bounded command workers with isolation & provenance
FULL READ (B06). local_bounded (RLIMIT via exec-wrapper, honestly labelled 'not a security boundary') and container mode (docker/podman --network=none --read-only --cap-drop=ALL --security-opt=no-new-privileges --pids-limit --memory, tmpfs noexec). shell=False, null-byte + non-empty command validation, _confined_paths escape rejection, output byte caps, timeout+kill. The `exec(` hit is os.execvpe in the resource wrapper (intended). **Strong isolation design.** No findings beyond DOC-001. Status: Audited — complete.

## orchestrator.py (952) — Durable, resumable pipeline orchestration
JobState/PipelineStage/PipelineManifest/Orchestrator; SQLite-backed durable jobs with heartbeat/stale recovery (pipeline-recover). Broad except → rollback-and-re-raise in transactions (prior audit confirmed disciplined). Large but cohesive. `..` = docstring. tests/test_production.py (isolated) exercises. No findings beyond DOC-001. Status: Audited — complete.

## release_gate.py (172) — Target release acceptance gate
_workflow_gate/_claim_gate/_pipeline_gate/evaluate_release_gate; composes evidence into an accept/block decision. Matches release-gate CLI. No findings. Status: Audited — complete.

## reproducibility.py (161) — Reproducibility manifests + verification
_version (subprocess for tool versions)/build_reproduction_manifest/verify_reproduction_manifest. Deterministic. No findings. Status: Audited — complete.

## security_audit.py (242) — Release/project security audit + SBOM
_secret_findings (regex secret scan), generate_sbom, audit_source_tree, verify_release_manifest, run_dependency_vulnerability_audit (pip-audit adapter via subprocess argv). NOTE: verify_release_manifest here is a product feature; its existence + the shipped MANIFEST mismatch (REPO-001) means the tool could self-detect the stale manifest. No findings in the code itself. Status: Audited — complete.

## target_pack.py (434) — Target-pack inference/validation/project generation
SupportingArtifact/_write_target_toml/infer_target_pack/verify_target_pack/generate_project_from_target_pack; rmtree scoped to output. CR-0710-005 dead-assignment fix applies here (verified no stray unused project var remains in infer path). No findings. Status: Audited — complete.

## toolchains.py (61) — User-owned compiler toolchain registry
register_toolchain/verify_toolchain; records user-declared tool paths + hashes; explicitly never bundles proprietary binaries (docstring). No findings. Status: Audited — complete.

## tools.py (112) — External-tool discovery + version capture
_capture (subprocess --version, timeout), discover_analyze_headless (Ghidra), snapshot_tools. BLOCKED reporting on absence. No findings. Status: Audited — complete.

## ground_truth.py (366) — Reproducible compiler/version ground-truth corpus
_resolve_executable/_version/build_ground_truth_corpus/verify/compare/create_builtin_manifest; subprocess (compilers) argv+timeout; `__import__` is a stdlib inline import. Deterministic corpus with hash verification. No findings. Status: Audited — complete.

## synthetic_corpus.py (380) — Deterministic ground-truth source corpus generation
Family generators (_c_arithmetic/_cpp_virtual/etc.); seed-deterministic; `__import__` inline stdlib; `..` = docstring. generate/verify_synthetic_corpus. No findings. Status: Audited — complete.

## compiler_lab.py (128) — Compiler-profile experiment matrix + ranking
_variant_arguments/run_compiler_lab; caching + provenance. Delegates to compiler.py (audited). No findings. Status: Audited — complete.

## compiler_worker.py (136) — Isolated compiler-worker facade
run_compiler_worker; isolation local_bounded|container via worker.py. No findings. Status: Audited — complete.

## decompme.py (99) — Local decomp.me-style packet creation (no upload)
_copy_required/create_decompme_packet; rmtree scoped to output dir; explicitly local-only (no network). No findings. Status: Audited — complete.

## hybrid.py (222) — Continuously buildable hybrid source-tree generation
_assembly_bytes/generate_hybrid_project; rmtree scoped to output; `__import__` inline. No findings. Status: Audited — complete.

## integration.py (487) — Manifest-driven integration scenario runner
FULL READ (B06). _substitute_command validates tokens against _ALLOWED_TOKENS allowlist and only replaces {artifact}/{workdir} into argv elements (no shell); subprocess argv arrays; **host execution gated behind allow_host_execution=True (default False)** honoring the consent policy; bounded output. Fixture copy scoped. No findings beyond DOC-001. Status: Audited — complete.
