---
title: tests/assembly/test_pipeline_cli_schemas.py
description: 8 exact current test nodes
original_path: tests/tests-assembly-test-pipeline-cli-schemas.html
---

<a id="test-test-pipeline-all-three-formats-and-durable-reports"></a>
<a id="test-test-assembly-project-cli-and-all-leaf-help"></a>
<a id="test-test-main-cli-exposes-assembly-capabilities"></a>
<a id="test-test-assembly-schemas-and-symbol-map-contracts"></a>
<a id="test-test-store-keeps-all-prior-schema-layers"></a>
<a id="test-test-pipeline-persists-relocation-evidence"></a>
<a id="test-test-hybrid-generate-keeps-bytes-default-and-allows-explicit-modes"></a>
<a id="test-test-failed-batch-is-recorded-durably"></a>

Section: Source-derived test reference

# `tests/assembly/test_pipeline_cli_schemas.py`

8 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `974f3cdeaa3c9954c08b1244d5a0cbdc71339f8355d0797832ce2967c5acccf2`.

Metadata: Toolkit behavior · line 53

### `test_pipeline_all_three_formats_and_durable_reports`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_manifest`, `AssemblyStore`, `AssemblyPipeline`, `api.batch`, `len`, `read_text`, `api.list_runs`, `api.report`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_pipeline_all_three_formats_and_durable_reports`

Metadata: Toolkit behavior · line 72

### `test_assembly_project_cli_and_all_leaf_help`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `json.loads`, `_leaf_commands`, `main`, `build_parser`, `len`, `capsys.readouterr`, `parse_args`, `str`, `command.split`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_assembly_project_cli_and_all_leaf_help`

Metadata: Toolkit behavior · line 87

### `test_main_cli_exposes_assembly_capabilities`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `set`, `json.loads`, `toolkit_main`, `next`, `capsys.readouterr`, `_build_parser`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_main_cli_exposes_assembly_capabilities`

Metadata: Toolkit behavior · line 97

### `test_assembly_schemas_and_symbol_map_contracts`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `sorted`, `normalize_symbol_map`, `glob`, `len`, `Draft202012Validator.check_schema`, `json.loads`, `supported_relocations`, `path.read_text`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_assembly_schemas_and_symbol_map_contracts`

Metadata: Toolkit behavior · line 108

### `test_store_keeps_all_prior_schema_layers`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `check`, `AssemblyStore`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_store_keeps_all_prior_schema_layers`

Metadata: Toolkit behavior · line 117

### `test_pipeline_persists_relocation_evidence`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_manifest`, `AssemblyStore`, `batch`, `store.connect`, `fetchall`, `AssemblyPipeline`, `connection.execute`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_pipeline_persists_relocation_evidence`

Metadata: Toolkit behavior · line 130

### `test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `artifact.mkdir`, `bytes.fromhex`, `write_bytes`, `write_text`, `generate_hybrid_project`, `json.dumps`, `read_text`, `_assembly_bytes`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes`

Metadata: Toolkit behavior · line 154

### `test_failed_batch_is_recorded_durably`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `manifest.write_text`, `AssemblyPipeline`, `pipeline.list_runs`, `json.dumps`, `AssemblyStore`, `pytest.raises`, `pipeline.batch`, `len`

**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_failed_batch_is_recorded_durably`
