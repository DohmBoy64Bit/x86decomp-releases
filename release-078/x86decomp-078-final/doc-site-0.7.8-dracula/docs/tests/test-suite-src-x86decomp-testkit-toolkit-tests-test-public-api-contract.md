---
title: test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py
description: Source-derived reference for 21 collected test nodes.
---

# `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`

**Collected nodes:** 21  
**Source SHA-256:** `7b6ccbb1f762b12ed3139d0188e36e5d29810248dd98d89b19a3e95fcf4ae27a`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_unified_canonical_entry_point`

No test docstring is declared.

**Direct call names in source:** `canonical.build_parser`, `canonical.main`, `capsys.readouterr`, `json.loads`, `parser.parse_args`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_unified_canonical_entry_point`  
**Area:** Bundled public contract  
**Source line:** 75

## `test_abi_contract_loading`

No test docstring is declared.

**Direct call names in source:** `ABIContract.from_dict`, `load_abi_contract`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_abi_contract_loading`  
**Area:** Bundled public contract  
**Source line:** 88

## `test_analysis_database_complete_public_surface`

No test docstring is declared.

**Direct call names in source:** `(artifact / 'references.jsonl').write_text`, `AnalysisDatabase`, `any`, `artifact.mkdir`, `database.add_reference`, `database.ingest_function_artifact`, `database.query`, `database.upsert_entity`, `json.dumps`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_analysis_database_complete_public_surface`  
**Area:** Bundled public contract  
**Source line:** 107

## `test_angr_public_file_wrappers`

No test docstring is declared.

**Direct call names in source:** `angr_bounded_compare`, `angr_bounded_compare_files`, `angr_memory_alias_compare_files`, `candidate.read_bytes`, `candidate.write_bytes`, `target.read_bytes`, `target.write_bytes`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_angr_public_file_wrappers`  
**Area:** Bundled public contract  
**Source line:** 135

## `test_benchmark_metrics_and_runner`

No test docstring is declared.

**Direct call names in source:** `candidate.write_bytes`, `classification_metrics`, `run_benchmark_corpus`, `target.write_bytes`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_benchmark_metrics_and_runner`  
**Area:** Bundled public contract  
**Source line:** 157

## `test_coff_remaining_value_objects_and_writer`

No test docstring is declared.

**Direct call names in source:** `FunctionDefinitionAux`, `FunctionDefinitionAux(1, 2, 3, 4).to_dict`, `RawAux`, `RawAux('00').to_dict`, `SyntheticSectionSpec`, `SyntheticSymbolSpec`, `build_synthetic_coff`, `extract_symbol`, `extracted.to_dict`, `obj.find_symbols`, `obj.symbol_by_index`, `parse_coff_bytes`, `synthetic_symbol_indices`, `write_synthetic_coff_object`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_coff_remaining_value_objects_and_writer`  
**Area:** Bundled public contract  
**Source line:** 172

## `test_compiler_lab_with_deterministic_fake_compiler`

No test docstring is declared.

**Direct call names in source:** `compiler.write_text`, `run_compiler_lab`, `source.write_text`, `str`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_compiler_lab_with_deterministic_fake_compiler`  
**Area:** Bundled public contract  
**Source line:** 190

## `test_diff_disassembly_and_crosscheck`

No test docstring is declared.

**Direct call names in source:** `'\n'.join`, `compare_files`, `compare_instruction_streams`, `control_flow_edges`, `cross_check_ghidra_instructions`, `decode_instructions`, `ghidra.write_text`, `isinstance`, `json.dumps`, `left.write_bytes`, `len`, `records[0].to_dict`, `right.write_bytes`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_diff_disassembly_and_crosscheck`  
**Area:** Bundled public contract  
**Source line:** 225

## `test_dynamic_file_wrapper_and_spec_loader`

No test docstring is declared.

**Direct call names in source:** `3 .to_bytes`, `3 .to_bytes(4, 'little').hex`, `4 .to_bytes`, `4 .to_bytes(4, 'little').hex`, `candidate.write_bytes`, `differential_validate_files`, `load_execution_spec`, `target.write_bytes`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_dynamic_file_wrapper_and_spec_loader`  
**Area:** Bundled public contract  
**Source line:** 241

## `test_dynamorio_runner_with_fake_subprocess`

No test docstring is declared.

**Direct call names in source:** `(logdir / 'trace.log').write_text`, `Path`, `SimpleNamespace`, `command.index`, `drrun.chmod`, `drrun.stat`, `drrun.write_bytes`, `executable.write_bytes`, `monkeypatch.setattr`, `run_drcov_trace`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_dynamorio_runner_with_fake_subprocess`  
**Area:** Bundled public contract  
**Source line:** 260

## `test_evidence_contradiction_require_verified_and_project_memory`

No test docstring is declared.

**Direct call names in source:** `ProjectMemory`, `ProjectMemory(project).require_valid`, `_verified_store`, `build_minimal_pe32`, `initialize_project`, `require_valid_project`, `store.add_contradiction`, `store.add_evidence`, `store.require_verified`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_evidence_contradiction_require_verified_and_project_memory`  
**Area:** Bundled public contract  
**Source line:** 296

## `test_exe_diff_extract_and_compare`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `build_synthetic_coff`, `coff_path.write_bytes`, `compare_pe_function_to_coff_symbol`, `extract_pe_bytes`, `len`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_exe_diff_extract_and_compare`  
**Area:** Bundled public contract  
**Source line:** 307

## `test_ghidra_run_export_success`

No test docstring is declared.

**Direct call names in source:** `SimpleNamespace`, `monkeypatch.setattr`, `run_export`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_ghidra_run_export_success`  
**Area:** Bundled public contract  
**Source line:** 318

## `test_remaining_value_objects_and_peview`

No test docstring is declared.

**Direct call names in source:** `DelayImportLibrary`, `DelayImportLibrary('x.dll', 1, 2, (symbol,)).to_dict`, `ExportSymbol`, `ExportSymbol('f', 1, 4096, None).to_dict`, `ImportLibrary`, `ImportLibrary('x.dll', (symbol,)).to_dict`, `ImportSymbol`, `LoadConfigInfo`, `MapContribution`, `MapContribution(1, 2, 3, 'a.obj').to_dict`, `PEView`, `ResourceLeaf`, `ResourceLeaf(('type', '1'), 8192, 3, 0, 'a' * 64).to_dict`, `TLS64Info`, `TLS64Info(1, 2, 3, 4, 0, 0, (5,)).to_dict`, `TLSInfo`, `TLSInfo(1, 2, 3, 4, 0, 0, (5,)).to_dict`, `build_minimal_pe32`, `load.to_dict`, `symbol.to_dict`, `view.u16`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_remaining_value_objects_and_peview`  
**Area:** Bundled public contract  
**Source line:** 326

## `test_service_create_and_run`

No test docstring is declared.

**Direct call names in source:** `any`, `build_minimal_pe32`, `calls.append`, `create_app`, `initialize_project`, `monkeypatch.setattr`, `run_service`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_service_create_and_run`  
**Area:** Bundled public contract  
**Source line:** 343

## `test_symbolic_clone_and_file_wrapper`

No test docstring is declared.

**Direct call names in source:** `SymState`, `bounded_symbolic_compare_files`, `candidate.write_bytes`, `state.clone`, `target.write_bytes`, `z3.BitVecVal`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_symbolic_clone_and_file_wrapper`  
**Area:** Bundled public contract  
**Source line:** 354

## `test_toolchain_snapshot_util_contract_and_workqueue`

No test docstring is declared.

**Direct call names in source:** `Path`, `Path(sys.executable).read_bytes`, `WorkQueue`, `executable.chmod`, `executable.stat`, `executable.write_bytes`, `queue.close`, `queue.create`, `queue.next`, `register_toolchain`, `report_path.is_file`, `require_int`, `require_mapping`, `require_string`, `snapshot_tools`, `verify_toolchain`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_toolchain_snapshot_util_contract_and_workqueue`  
**Area:** Bundled public contract  
**Source line:** 369

## `test_cli_main_executes_public_entrypoint`

No test docstring is declared.

**Direct call names in source:** `capsys.readouterr`, `cli_main`, `left.write_bytes`, `right.write_bytes`, `str`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_cli_main_executes_public_entrypoint`  
**Area:** Bundled public contract  
**Source line:** 391

## `test_streamable_http_mcp_public_methods`

No test docstring is declared.

**Direct call names in source:** `AssertionError`, `Headers`, `Response`, `StreamableHTTPMCPClient`, `client.call_tool`, `client.close`, `client.initialize`, `client.list_tools`, `json.dumps`, `json.dumps(self.payload).encode`, `json.loads`, `key.lower`, `monkeypatch.setattr`, `request.data.decode`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_streamable_http_mcp_public_methods`  
**Area:** Bundled public contract  
**Source line:** 400

## `test_private_function_surface_regression`

Exercise the remaining internal function bodies so no defined function is omitted.

**Direct call names in source:** `SimpleNamespace`, `_Reader`, `_Reader(b'hello\x00').c_string`, `closed.append`, `coff_archive._long_name`, `image_match._apply_rebase`, `isinstance`, `monkeypatch.setattr`, `object.__new__`, `pytest.raises`, `stdio.__enter__`, `stdio.__exit__`, `symbolic.SymState`, `symbolic._condition`, `symbolic._is_sat`, `symbolic._write_memory`, `toolkit_cli._int`, `toolkit_cli._json_object`, `toolkit_cli._mcp_client`, `z3.BitVecVal`, `z3.BoolVal`, `z3.is_false`, `z3.simplify`, `z3.simplify(state.memory[4096]).as_long`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_private_function_surface_regression`  
**Area:** Bundled public contract  
**Source line:** 446

## `test_remaining_current_function_surface`

No test docstring is declared.

**Direct call names in source:** `PEView`, `ProjectStateDatabase`, `StoredArtifact`, `SupportingArtifact`, `WorkerLimits`, `WorkerRequest`, `_adjustor_thunk_candidate`, `_container_command`, `_deterministic_word`, `_function_prefix`, `_function_prefix(view, code_rva).startswith`, `artifact.to_dict`, `build_minimal_pe32`, `bytearray`, `bytes.fromhex`, `data.read_bytes`, `data.write_text`, `database.artifact_digests`, `database.upsert_artifact_reference`, `generate_execution_harness_from_files`, `hashlib.sha256`, `hashlib.sha256(data.read_bytes()).hexdigest`, `initial_view.rva_to_offset`, `manifest.write_text`, `pe.read_bytes`, `pe.write_bytes`, `support.to_dict`, `verify_release_manifest`, `write_json`  
**Node ID:** `src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py::test_remaining_current_function_surface`  
**Area:** Bundled public contract  
**Source line:** 485
