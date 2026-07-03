---
title: tests/assembly/test_pipeline_cli_schemas.py
description: Source-derived reference for 8 collected test nodes.
---

# `tests/assembly/test_pipeline_cli_schemas.py`

**Collected nodes:** 8  
**Source SHA-256:** `86b4e8b989cba611508a13ed2024bba02e187618acf28bc5e090de22a815f8ed`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_pipeline_all_three_formats_and_durable_reports`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'annotated/src/asm/sub_00001000.S').read_text`, `(tmp_path / 'bytes/src/asm/sub_00001000.S').read_text`, `(tmp_path / 'mnemonic/src/asm/sub_00001000.S').read_text`, `AssemblyPipeline`, `AssemblyStore`, `_manifest`, `api.batch`, `api.list_runs`, `api.report`, `len`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_pipeline_all_three_formats_and_durable_reports`  
**Area:** Toolkit behavior  
**Source line:** 53

## `test_assembly_project_cli_and_all_leaf_help`

No test docstring is declared.

**Direct call names in source:** `_leaf_commands`, `build_parser`, `build_parser().parse_args`, `capsys.readouterr`, `command.split`, `json.loads`, `len`, `main`, `str`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_assembly_project_cli_and_all_leaf_help`  
**Area:** Toolkit behavior  
**Source line:** 72

## `test_main_cli_exposes_assembly_capabilities`

No test docstring is declared.

**Direct call names in source:** `_build_parser`, `capsys.readouterr`, `json.loads`, `next`, `set`, `toolkit_main`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_main_cli_exposes_assembly_capabilities`  
**Area:** Toolkit behavior  
**Source line:** 87

## `test_assembly_schemas_and_symbol_map_contracts`

No test docstring is declared.

**Direct call names in source:** `(ROOT / 'schemas/assembly').glob`, `Draft202012Validator.check_schema`, `json.loads`, `len`, `normalize_symbol_map`, `path.read_text`, `sorted`, `supported_relocations`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_assembly_schemas_and_symbol_map_contracts`  
**Area:** Toolkit behavior  
**Source line:** 97

## `test_store_keeps_all_prior_schema_layers`

No test docstring is declared.

**Direct call names in source:** `AssemblyStore`, `AssemblyStore(tmp_path).check`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_store_keeps_all_prior_schema_layers`  
**Area:** Toolkit behavior  
**Source line:** 108

## `test_pipeline_persists_relocation_evidence`

No test docstring is declared.

**Direct call names in source:** `AssemblyPipeline`, `AssemblyPipeline(store).batch`, `AssemblyStore`, `_manifest`, `connection.execute`, `connection.execute('SELECT status,target_symbol,target_rva FROM assembly_relocation_resolutions ORDER BY relocation_offset').fetchall`, `store.connect`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_pipeline_persists_relocation_evidence`  
**Area:** Toolkit behavior  
**Source line:** 117

## `test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes`

No test docstring is declared.

**Direct call names in source:** `(artifact / 'body.bin').write_bytes`, `(artifact / 'function.json').write_text`, `(tmp_path / 'annotated/src/asm/sub_00001000.S').read_text`, `(tmp_path / 'bytes/src/asm/sub_00001000.S').read_text`, `(tmp_path / 'mnemonic/src/asm/sub_00001000.S').read_text`, `_assembly_bytes`, `artifact.mkdir`, `bytes.fromhex`, `generate_hybrid_project`, `json.dumps`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_hybrid_generate_keeps_bytes_default_and_allows_explicit_modes`  
**Area:** Toolkit behavior  
**Source line:** 130

## `test_failed_batch_is_recorded_durably`

No test docstring is declared.

**Direct call names in source:** `AssemblyPipeline`, `AssemblyStore`, `json.dumps`, `len`, `manifest.write_text`, `pipeline.batch`, `pipeline.list_runs`, `pytest.raises`  
**Node ID:** `tests/assembly/test_pipeline_cli_schemas.py::test_failed_batch_is_recorded_durably`  
**Area:** Toolkit behavior  
**Source line:** 154
