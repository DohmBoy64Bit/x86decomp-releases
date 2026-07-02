---
title: test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py
description: 21 exact current test nodes
original_path: tests/test-suite-src-x86decomp-testkit-toolkit-tests-test-public-api-contract.html
---

<a id="test-test-unified-canonical-entry-point"></a>
<a id="test-test-abi-contract-loading"></a>
<a id="test-test-analysis-database-complete-public-surface"></a>
<a id="test-test-angr-public-file-wrappers"></a>
<a id="test-test-benchmark-metrics-and-runner"></a>
<a id="test-test-coff-remaining-value-objects-and-writer"></a>
<a id="test-test-compiler-lab-with-deterministic-fake-compiler"></a>
<a id="test-test-diff-disassembly-and-crosscheck"></a>
<a id="test-test-dynamic-file-wrapper-and-spec-loader"></a>
<a id="test-test-dynamorio-runner-with-fake-subprocess"></a>
<a id="test-test-evidence-contradiction-require-verified-and-project-memory"></a>
<a id="test-test-exe-diff-extract-and-compare"></a>
<a id="test-test-ghidra-run-export-success"></a>
<a id="test-test-remaining-value-objects-and-peview"></a>
<a id="test-test-service-create-and-run"></a>
<a id="test-test-symbolic-clone-and-file-wrapper"></a>
<a id="test-test-toolchain-snapshot-util-contract-and-workqueue"></a>
<a id="test-test-cli-main-executes-public-entrypoint"></a>
<a id="test-test-streamable-http-mcp-public-methods"></a>
<a id="test-test-private-function-surface-regression"></a>
<a id="test-test-remaining-current-function-surface"></a>

Section: Source-derived test reference

# `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`

21 current test nodes in the Public-surface contract inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `0db55c2047f507a231d9738d8dc5710114a13726768e81aa0160c3fa5b3ff3eb`.

Metadata: Public-surface contract · line 75

### `test_unified_canonical_entry_point`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `canonical.build_parser`, `parser.parse_args`, `json.loads`, `canonical.main`, `capsys.readouterr`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_unified_canonical_entry_point`

Metadata: Public-surface contract · line 88

### `test_abi_contract_loading`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ABIContract.from_dict`, `write_json`, `load_abi_contract`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_abi_contract_loading`

Metadata: Public-surface contract · line 107

### `test_analysis_database_complete_public_surface`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `artifact.mkdir`, `write_json`, `write_text`, `AnalysisDatabase`, `database.upsert_entity`, `database.add_reference`, `database.ingest_function_artifact`, `database.query`, `any`, `json.dumps`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_analysis_database_complete_public_surface`

Metadata: Public-surface contract · line 135

### `test_angr_public_file_wrappers`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `target.write_bytes`, `candidate.write_bytes`, `write_json`, `angr_memory_alias_compare_files`, `angr_bounded_compare`, `angr_bounded_compare_files`, `target.read_bytes`, `candidate.read_bytes`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_angr_public_file_wrappers`

Metadata: Public-surface contract · line 157

### `test_benchmark_metrics_and_runner`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `classification_metrics`, `target.write_bytes`, `candidate.write_bytes`, `write_json`, `run_benchmark_corpus`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_benchmark_metrics_and_runner`

Metadata: Public-surface contract · line 172

### `test_coff_remaining_value_objects_and_writer`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_synthetic_coff`, `parse_coff_bytes`, `extract_symbol`, `write_synthetic_coff_object`, `obj.find_symbols`, `obj.symbol_by_index`, `synthetic_symbol_indices`, `to_dict`, `extracted.to_dict`, `SyntheticSymbolSpec`, `SyntheticSectionSpec`, `FunctionDefinitionAux`, `RawAux`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_coff_remaining_value_objects_and_writer`

Metadata: Public-surface contract · line 190

### `test_compiler_lab_with_deterministic_fake_compiler`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `compiler.write_text`, `source.write_text`, `write_json`, `run_compiler_lab`, `str`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_compiler_lab_with_deterministic_fake_compiler`

Metadata: Public-surface contract · line 225

### `test_diff_disassembly_and_crosscheck`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `left.write_bytes`, `right.write_bytes`, `decode_instructions`, `isinstance`, `ghidra.write_text`, `compare_files`, `control_flow_edges`, `compare_instruction_streams`, `cross_check_ghidra_instructions`, `to_dict`, `join`, `len`, `json.dumps`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_diff_disassembly_and_crosscheck`

Metadata: Public-surface contract · line 241

### `test_dynamic_file_wrapper_and_spec_loader`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `target.write_bytes`, `candidate.write_bytes`, `write_json`, `differential_validate_files`, `load_execution_spec`, `hex`, `to_bytes`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_dynamic_file_wrapper_and_spec_loader`

Metadata: Public-surface contract · line 260

### `test_dynamorio_runner_with_fake_subprocess`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `executable.write_bytes`, `drrun.write_bytes`, `drrun.chmod`, `monkeypatch.setattr`, `run_drcov_trace`, `Path`, `write_text`, `SimpleNamespace`, `drrun.stat`, `command.index`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_dynamorio_runner_with_fake_subprocess`

Metadata: Public-surface contract · line 296

### `test_evidence_contradiction_require_verified_and_project_memory`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `initialize_project`, `_verified_store`, `store.add_evidence`, `build_minimal_pe32`, `store.add_contradiction`, `require_valid_project`, `require_valid`, `store.require_verified`, `ProjectMemory`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_evidence_contradiction_require_verified_and_project_memory`

Metadata: Public-surface contract · line 307

### `test_exe_diff_extract_and_compare`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `coff_path.write_bytes`, `extract_pe_bytes`, `compare_pe_function_to_coff_symbol`, `build_synthetic_coff`, `len`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_exe_diff_extract_and_compare`

Metadata: Public-surface contract · line 318

### `test_ghidra_run_export_success`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `monkeypatch.setattr`, `run_export`, `SimpleNamespace`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_ghidra_run_export_success`

Metadata: Public-surface contract · line 326

### `test_remaining_value_objects_and_peview`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ImportSymbol`, `LoadConfigInfo`, `build_minimal_pe32`, `PEView`, `to_dict`, `view.u16`, `symbol.to_dict`, `load.to_dict`, `ImportLibrary`, `DelayImportLibrary`, `ExportSymbol`, `TLSInfo`, `ResourceLeaf`, `TLS64Info`, `MapContribution`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_remaining_value_objects_and_peview`

Metadata: Public-surface contract · line 343

### `test_service_create_and_run`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `initialize_project`, `create_app`, `any`, `monkeypatch.setattr`, `run_service`, `build_minimal_pe32`, `calls.append`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_service_create_and_run`

Metadata: Public-surface contract · line 354

### `test_symbolic_clone_and_file_wrapper`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `SymState`, `state.clone`, `target.write_bytes`, `candidate.write_bytes`, `bounded_symbolic_compare_files`, `z3.BitVecVal`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_symbolic_clone_and_file_wrapper`

Metadata: Public-surface contract · line 369

### `test_toolchain_snapshot_util_contract_and_workqueue`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `executable.write_bytes`, `executable.chmod`, `register_toolchain`, `WorkQueue`, `read_bytes`, `verify_toolchain`, `report_path.is_file`, `require_mapping`, `require_string`, `require_int`, `queue.create`, `queue.close`, `queue.next`, `Path`, `executable.stat`, `snapshot_tools`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_toolchain_snapshot_util_contract_and_workqueue`

Metadata: Public-surface contract · line 391

### `test_cli_main_executes_public_entrypoint`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `left.write_bytes`, `right.write_bytes`, `cli_main`, `capsys.readouterr`, `str`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_cli_main_executes_public_entrypoint`

Metadata: Public-surface contract · line 400

### `test_streamable_http_mcp_public_methods`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `monkeypatch.setattr`, `StreamableHTTPMCPClient`, `Headers`, `json.loads`, `AssertionError`, `client.call_tool`, `client.close`, `encode`, `request.data.decode`, `Response`, `client.initialize`, `client.list_tools`, `key.lower`, `json.dumps`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_streamable_http_mcp_public_methods`

Metadata: Public-surface contract · line 446

### `test_private_function_surface_regression`

Exercise the remaining internal function bodies so no defined function is omitted.

**Direct call names in source:** `toolkit_cli._mcp_client`, `isinstance`, `symbolic.SymState`, `symbolic._write_memory`, `z3.is_false`, `symbolic._is_sat`, `SimpleNamespace`, `object.__new__`, `monkeypatch.setattr`, `stdio.__exit__`, `c_string`, `toolkit_cli._int`, `toolkit_cli._json_object`, `pytest.raises`, `z3.BitVecVal`, `as_long`, `z3.BoolVal`, `z3.simplify`, `image_match._apply_rebase`, `coff_archive._long_name`, `stdio.__enter__`, `symbolic._condition`, `closed.append`, `_Reader`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_private_function_surface_regression`

Metadata: Public-surface contract · line 485

### `test_remaining_current_function_surface`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `StoredArtifact`, `SupportingArtifact`, `build_minimal_pe32`, `PEView`, `bytearray`, `initial_view.rva_to_offset`, `bytes.fromhex`, `pe.write_bytes`, `startswith`, `_adjustor_thunk_candidate`, `write_json`, `generate_execution_harness_from_files`, `data.write_text`, `manifest.write_text`, `WorkerRequest`, `_container_command`, `pe.read_bytes`, `ProjectStateDatabase`, `database.upsert_artifact_reference`, `verify_release_manifest`, `artifact.to_dict`, `support.to_dict`, `_function_prefix`, `_deterministic_word`, `database.artifact_digests`, `WorkerLimits`, `hexdigest`, `hashlib.sha256`, `data.read_bytes`

**Node ID:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_remaining_current_function_surface`
