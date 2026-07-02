---
title: tests/test_production.py
description: 22 exact current test nodes
original_path: tests/tests-test-production.html
---

<a id="test-test-content-store-roundtrip-and-gc"></a>
<a id="test-test-worker-executes-bounded-command-and-hashes-outputs"></a>
<a id="test-test-target-pack-auto-template-and-project"></a>
<a id="test-test-project-migration-backup-restore-repair-and-gc"></a>
<a id="test-test-orchestrator-resume-failure-retry-and-cancel"></a>
<a id="test-test-compiler-worker-uses-real-subprocess-contract"></a>
<a id="test-test-harness-generation-is-deterministic-and-explicit"></a>
<a id="test-test-convergence-and-history"></a>
<a id="test-test-linker-reconstruction-plan-is-evidence-limited"></a>
<a id="test-test-cpp-recovery-empty-metadata-is-truthful"></a>
<a id="test-test-reproduction-and-security-reports"></a>
<a id="test-test-generated-template-is-grounded-and-executable"></a>
<a id="test-test-orchestrator-materializes-and-revalidates-outputs"></a>
<a id="test-test-extended-symbolic-conditions-adc-sbb-setcc-cmovcc"></a>
<a id="test-test-service-snapshot-exposes-control-plane"></a>
<a id="test-test-project-backup-is-deterministic"></a>
<a id="test-test-active-pipeline-cancellation-is-observed"></a>
<a id="test-test-dependency-audit-adapter-parsing"></a>
<a id="test-test-pipeline-stale-heartbeat-recovery"></a>
<a id="test-test-release-gate-is-explicit-and-truth-scoped"></a>
<a id="test-test-synthetic-corpus-generation-is-reproducible-and-hash-checked"></a>
<a id="test-test-target-decisions-example-preserves-unknowns"></a>

Section: Source-derived test reference

# `tests/test_production.py`

22 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89`.

Metadata: Toolkit behavior · line 35

### `test_content_store_roundtrip_and_gc`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `source.write_bytes`, `ContentStore`, `store.put_file`, `store.add_reference`, `store.remove_reference`, `store.read_bytes`, `store.verify`, `project_gc_like`, `store.garbage_collect`

**Node ID:** `tests/test_production.py::test_content_store_roundtrip_and_gc`

Metadata: Toolkit behavior · line 53

### `test_worker_executes_bounded_command_and_hashes_outputs`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `work.mkdir`, `input_path.write_text`, `WorkerRequest`, `execute_worker_request`, `discover_worker_capabilities`, `output_path.read_text`, `WorkerLimits`, `Path`

**Node ID:** `tests/test_production.py::test_worker_executes_bounded_command_and_hashes_outputs`

Metadata: Toolkit behavior · line 75

### `test_target_pack_auto_template_and_project`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `infer_target_pack`, `verify_target_pack`, `generate_project_from_target_pack`, `is_file`, `check_project_state`

**Node ID:** `tests/test_production.py::test_target_pack_auto_template_and_project`

Metadata: Toolkit behavior · line 94

### `test_project_migration_backup_restore_repair_and_gc`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `load_json`, `write_json`, `unlink`, `migrate_project`, `restore_project_backup`, `create_project_backup`, `project.pop`, `check_project_state`, `repair_project_state`, `project_gc`

**Node ID:** `tests/test_production.py::test_project_migration_backup_restore_repair_and_gc`

Metadata: Toolkit behavior · line 122

### `test_orchestrator_resume_failure_retry_and_cancel`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `write_json`, `PipelineManifest.load`, `len`, `Orchestrator`, `orchestrator.run`, `orchestrator.retry`, `orchestrator.cancel`, `str`

**Node ID:** `tests/test_production.py::test_orchestrator_resume_failure_retry_and_cancel`

Metadata: Toolkit behavior · line 166

### `test_compiler_worker_uses_real_subprocess_contract`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `source.write_text`, `write_json`, `run_compiler_worker`, `output.read_bytes`, `source.read_bytes`, `sys.version.split`

**Node ID:** `tests/test_production.py::test_compiler_worker_uses_real_subprocess_contract`

Metadata: Toolkit behavior · line 197

### `test_harness_generation_is_deterministic_and_explicit`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ABIContract`, `generate_execution_harness`, `value.pop`

**Node ID:** `tests/test_production.py::test_harness_generation_is_deterministic_and_explicit`

Metadata: Toolkit behavior · line 219

### `test_convergence_and_history`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `bytearray`, `candidate.write_bytes`, `analyze_image_convergence`, `append_convergence_history`, `reference.read_bytes`

**Node ID:** `tests/test_production.py::test_convergence_and_history`

Metadata: Toolkit behavior · line 236

### `test_linker_reconstruction_plan_is_evidence_limited`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `write_synthetic_coff`, `map_path.write_text`, `build_linker_reconstruction_plan`, `write_relink_manifest_from_plan`, `load_json`

**Node ID:** `tests/test_production.py::test_linker_reconstruction_plan_is_evidence_limited`

Metadata: Toolkit behavior · line 253

### `test_cpp_recovery_empty_metadata_is_truthful`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `recover_cpp_model`

**Node ID:** `tests/test_production.py::test_cpp_recovery_empty_metadata_is_truthful`

Metadata: Toolkit behavior · line 261

### `test_reproduction_and_security_reports`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `build_reproduction_manifest`, `verify_reproduction_manifest`, `audit_root.mkdir`, `write_text`, `audit_source_tree`, `generate_sbom`

**Node ID:** `tests/test_production.py::test_reproduction_and_security_reports`

Metadata: Toolkit behavior · line 280

### `test_generated_template_is_grounded_and_executable`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `infer_target_pack`, `derive_template_contract`, `generate_project_from_target_pack`, `materialize_project_template`, `is_file`, `is_dir`, `dict`, `str`, `env.get`, `subprocess.run`, `load_json`, `list`, `Path`, `glob`, `resolve`

**Node ID:** `tests/test_production.py::test_generated_template_is_grounded_and_executable`

Metadata: Toolkit behavior · line 316

### `test_orchestrator_materializes_and_revalidates_outputs`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `write_json`, `Orchestrator`, `orchestrator.run`, `fetchone`, `json.loads`, `output.write_text`, `verify`, `str`, `output.read_text`, `orchestrator.connection.execute`, `ContentStore`

**Node ID:** `tests/test_production.py::test_orchestrator_materializes_and_revalidates_outputs`

Metadata: Toolkit behavior · line 358

### `test_extended_symbolic_conditions_adc_sbb_setcc_cmovcc`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `bytes.fromhex`, `bounded_symbolic_compare`

**Node ID:** `tests/test_production.py::test_extended_symbolic_conditions_adc_sbb_setcc_cmovcc`

Metadata: Toolkit behavior · line 376

### `test_service_snapshot_exposes_control_plane`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `service_snapshot`

**Node ID:** `tests/test_production.py::test_service_snapshot_exposes_control_plane`

Metadata: Toolkit behavior · line 389

### `test_project_backup_is_deterministic`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `create_project_backup`

**Node ID:** `tests/test_production.py::test_project_backup_is_deterministic`

Metadata: Toolkit behavior · line 398

### `test_active_pipeline_cancellation_is_observed`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `write_json`, `threading.Thread`, `thread.start`, `thread.join`, `time.monotonic`, `time.sleep`, `thread.is_alive`, `str`, `Orchestrator`, `result.update`, `orchestrator.run`, `observer.status`, `status.get`, `observer.cancel`

**Node ID:** `tests/test_production.py::test_active_pipeline_cancellation_is_observed`

Metadata: Toolkit behavior · line 447

### `test_dependency_audit_adapter_parsing`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tool.write_text`, `tool.chmod`, `run_dependency_vulnerability_audit`, `str`

**Node ID:** `tests/test_production.py::test_dependency_audit_adapter_parsing`

Metadata: Toolkit behavior · line 462

### `test_pipeline_stale_heartbeat_recovery`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `write_json`, `Orchestrator`, `orchestrator.register`, `orchestrator.connection.execute`, `orchestrator.recover_stale_jobs`, `str`, `orchestrator.status`

**Node ID:** `tests/test_production.py::test_pipeline_stale_heartbeat_recovery`

Metadata: Toolkit behavior · line 486

### `test_release_gate_is_explicit_and_truth_scoped`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `infer_target_pack`, `generate_project_from_target_pack`, `evaluate_release_gate`, `any`

**Node ID:** `tests/test_production.py::test_release_gate_is_explicit_and_truth_scoped`

Metadata: Toolkit behavior · line 507

### `test_synthetic_corpus_generation_is_reproducible_and_hash_checked`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `generate_synthetic_corpus`, `verify_synthetic_corpus`, `source.write_text`, `any`, `source.read_text`

**Node ID:** `tests/test_production.py::test_synthetic_corpus_generation_is_reproducible_and_hash_checked`

Metadata: Toolkit behavior · line 527

### `test_target_decisions_example_preserves_unknowns`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `load_json`, `resolve`, `Path`

**Node ID:** `tests/test_production.py::test_target_decisions_example_preserves_unknowns`
