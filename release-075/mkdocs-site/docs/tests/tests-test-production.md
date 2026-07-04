---
title: tests/test_production.py
description: Source-derived reference for 22 collected test nodes.
---

# `tests/test_production.py`

**Collected nodes:** 22  
**Source SHA-256:** `da0d4bd57f7f4bb68957fa8aa42a67f7eb34347f35137849e360dc95e796db89`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_content_store_roundtrip_and_gc`

No test docstring is declared.

**Direct call names in source:** `ContentStore`, `project_gc_like`, `source.write_bytes`, `store.add_reference`, `store.garbage_collect`, `store.put_file`, `store.read_bytes`, `store.remove_reference`, `store.verify`  
**Node ID:** `tests/test_production.py::test_content_store_roundtrip_and_gc`  
**Area:** Toolkit behavior  
**Source line:** 35

## `test_worker_executes_bounded_command_and_hashes_outputs`

No test docstring is declared.

**Direct call names in source:** `Path`, `WorkerLimits`, `WorkerRequest`, `discover_worker_capabilities`, `execute_worker_request`, `input_path.write_text`, `output_path.read_text`, `work.mkdir`  
**Node ID:** `tests/test_production.py::test_worker_executes_bounded_command_and_hashes_outputs`  
**Area:** Toolkit behavior  
**Source line:** 53

## `test_target_pack_auto_template_and_project`

No test docstring is declared.

**Direct call names in source:** `(project_root / 'target-pack' / 'target.toml').is_file`, `build_minimal_pe32`, `check_project_state`, `generate_project_from_target_pack`, `infer_target_pack`, `verify_target_pack`  
**Node ID:** `tests/test_production.py::test_target_pack_auto_template_and_project`  
**Area:** Toolkit behavior  
**Source line:** 75

## `test_project_migration_backup_restore_repair_and_gc`

No test docstring is declared.

**Direct call names in source:** `(project_root / 'state' / 'project-state.sqlite3').unlink`, `build_minimal_pe32`, `check_project_state`, `create_project_backup`, `initialize_project`, `load_json`, `migrate_project`, `project.pop`, `project_gc`, `repair_project_state`, `restore_project_backup`, `write_json`  
**Node ID:** `tests/test_production.py::test_project_migration_backup_restore_repair_and_gc`  
**Area:** Toolkit behavior  
**Source line:** 94

## `test_orchestrator_resume_failure_retry_and_cancel`

No test docstring is declared.

**Direct call names in source:** `Orchestrator`, `PipelineManifest.load`, `build_minimal_pe32`, `initialize_project`, `len`, `orchestrator.cancel`, `orchestrator.retry`, `orchestrator.run`, `str`, `write_json`  
**Node ID:** `tests/test_production.py::test_orchestrator_resume_failure_retry_and_cancel`  
**Area:** Toolkit behavior  
**Source line:** 122

## `test_compiler_worker_uses_real_subprocess_contract`

No test docstring is declared.

**Direct call names in source:** `output.read_bytes`, `run_compiler_worker`, `source.read_bytes`, `source.write_text`, `sys.version.split`, `write_json`  
**Node ID:** `tests/test_production.py::test_compiler_worker_uses_real_subprocess_contract`  
**Area:** Toolkit behavior  
**Source line:** 166

## `test_harness_generation_is_deterministic_and_explicit`

No test docstring is declared.

**Direct call names in source:** `ABIContract`, `generate_execution_harness`, `value.pop`  
**Node ID:** `tests/test_production.py::test_harness_generation_is_deterministic_and_explicit`  
**Area:** Toolkit behavior  
**Source line:** 197

## `test_convergence_and_history`

No test docstring is declared.

**Direct call names in source:** `analyze_image_convergence`, `append_convergence_history`, `build_minimal_pe32`, `bytearray`, `candidate.write_bytes`, `reference.read_bytes`  
**Node ID:** `tests/test_production.py::test_convergence_and_history`  
**Area:** Toolkit behavior  
**Source line:** 219

## `test_linker_reconstruction_plan_is_evidence_limited`

No test docstring is declared.

**Direct call names in source:** `build_linker_reconstruction_plan`, `build_minimal_pe32`, `load_json`, `map_path.write_text`, `write_relink_manifest_from_plan`, `write_synthetic_coff`  
**Node ID:** `tests/test_production.py::test_linker_reconstruction_plan_is_evidence_limited`  
**Area:** Toolkit behavior  
**Source line:** 236

## `test_cpp_recovery_empty_metadata_is_truthful`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `recover_cpp_model`  
**Node ID:** `tests/test_production.py::test_cpp_recovery_empty_metadata_is_truthful`  
**Area:** Toolkit behavior  
**Source line:** 253

## `test_reproduction_and_security_reports`

No test docstring is declared.

**Direct call names in source:** `(audit_root / 'safe.txt').write_text`, `audit_root.mkdir`, `audit_source_tree`, `build_minimal_pe32`, `build_reproduction_manifest`, `generate_sbom`, `initialize_project`, `verify_reproduction_manifest`  
**Node ID:** `tests/test_production.py::test_reproduction_and_security_reports`  
**Area:** Toolkit behavior  
**Source line:** 261

## `test_generated_template_is_grounded_and_executable`

No test docstring is declared.

**Direct call names in source:** `(project / 'src' / 'matching').glob`, `(project / 'src' / 'matching').is_dir`, `Path`, `Path(__file__).resolve`, `Path(project / materialized['helper']).is_file`, `build_minimal_pe32`, `derive_template_contract`, `dict`, `env.get`, `generate_project_from_target_pack`, `infer_target_pack`, `list`, `load_json`, `materialize_project_template`, `str`, `subprocess.run`  
**Node ID:** `tests/test_production.py::test_generated_template_is_grounded_and_executable`  
**Area:** Toolkit behavior  
**Source line:** 280

## `test_orchestrator_materializes_and_revalidates_outputs`

No test docstring is declared.

**Direct call names in source:** `ContentStore`, `ContentStore(project_root / 'artifacts').verify`, `Orchestrator`, `build_minimal_pe32`, `initialize_project`, `json.loads`, `orchestrator.connection.execute`, `orchestrator.connection.execute("SELECT attempt,result_json FROM jobs WHERE pipeline_id='materialize'").fetchone`, `orchestrator.run`, `output.read_text`, `output.write_text`, `str`, `write_json`  
**Node ID:** `tests/test_production.py::test_orchestrator_materializes_and_revalidates_outputs`  
**Area:** Toolkit behavior  
**Source line:** 316

## `test_extended_symbolic_conditions_adc_sbb_setcc_cmovcc`

No test docstring is declared.

**Direct call names in source:** `bounded_symbolic_compare`, `bytes.fromhex`  
**Node ID:** `tests/test_production.py::test_extended_symbolic_conditions_adc_sbb_setcc_cmovcc`  
**Area:** Toolkit behavior  
**Source line:** 358

## `test_service_snapshot_exposes_control_plane`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `service_snapshot`  
**Node ID:** `tests/test_production.py::test_service_snapshot_exposes_control_plane`  
**Area:** Toolkit behavior  
**Source line:** 376

## `test_project_backup_is_deterministic`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `create_project_backup`, `initialize_project`  
**Node ID:** `tests/test_production.py::test_project_backup_is_deterministic`  
**Area:** Toolkit behavior  
**Source line:** 389

## `test_active_pipeline_cancellation_is_observed`

No test docstring is declared.

**Direct call names in source:** `Orchestrator`, `build_minimal_pe32`, `initialize_project`, `observer.cancel`, `observer.status`, `orchestrator.run`, `result.update`, `status.get`, `str`, `thread.is_alive`, `thread.join`, `thread.start`, `threading.Thread`, `time.monotonic`, `time.sleep`, `write_json`  
**Node ID:** `tests/test_production.py::test_active_pipeline_cancellation_is_observed`  
**Area:** Toolkit behavior  
**Source line:** 398

## `test_dependency_audit_adapter_parsing`

No test docstring is declared.

**Direct call names in source:** `run_dependency_vulnerability_audit`, `str`, `tool.chmod`, `tool.write_text`  
**Node ID:** `tests/test_production.py::test_dependency_audit_adapter_parsing`  
**Area:** Toolkit behavior  
**Source line:** 447

## `test_pipeline_stale_heartbeat_recovery`

No test docstring is declared.

**Direct call names in source:** `Orchestrator`, `build_minimal_pe32`, `initialize_project`, `orchestrator.connection.execute`, `orchestrator.recover_stale_jobs`, `orchestrator.register`, `orchestrator.status`, `str`, `write_json`  
**Node ID:** `tests/test_production.py::test_pipeline_stale_heartbeat_recovery`  
**Area:** Toolkit behavior  
**Source line:** 462

## `test_release_gate_is_explicit_and_truth_scoped`

No test docstring is declared.

**Direct call names in source:** `any`, `build_minimal_pe32`, `evaluate_release_gate`, `generate_project_from_target_pack`, `infer_target_pack`  
**Node ID:** `tests/test_production.py::test_release_gate_is_explicit_and_truth_scoped`  
**Area:** Toolkit behavior  
**Source line:** 486

## `test_synthetic_corpus_generation_is_reproducible_and_hash_checked`

No test docstring is declared.

**Direct call names in source:** `any`, `generate_synthetic_corpus`, `source.read_text`, `source.write_text`, `verify_synthetic_corpus`  
**Node ID:** `tests/test_production.py::test_synthetic_corpus_generation_is_reproducible_and_hash_checked`  
**Area:** Toolkit behavior  
**Source line:** 507

## `test_target_decisions_example_preserves_unknowns`

No test docstring is declared.

**Direct call names in source:** `Path`, `Path(__file__).resolve`, `load_json`  
**Node ID:** `tests/test_production.py::test_target_decisions_example_preserves_unknowns`  
**Area:** Toolkit behavior  
**Source line:** 527
