---
title: tests/assembly/test_annotation_materialize.py
description: Source-derived reference for 8 collected test nodes.
---

# `tests/assembly/test_annotation_materialize.py`

**Collected nodes:** 8  
**Source SHA-256:** `46aeb940a0ccb02b0312ef413ce123c3c647c0224a1f8b1f571d128ab733574f`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_byte_form_is_exact_native_compatibility_output`

No test docstring is declared.

**Direct call names in source:** `_assembly_bytes`, `bytes`, `parse_byte_directives`, `pytest.raises`, `range`, `render_byte_assembly`, `validate_symbol`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_byte_form_is_exact_native_compatibility_output`  
**Area:** Toolkit behavior  
**Source line:** 20

## `test_annotation_is_idempotent_and_keeps_bytes`

No test docstring is declared.

**Direct call names in source:** `annotate_source`, `bytes.fromhex`, `first.read_text`, `parse_byte_directives`, `render_byte_assembly`, `second.read_text`, `source.write_text`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_annotation_is_idempotent_and_keeps_bytes`  
**Area:** Toolkit behavior  
**Source line:** 30

## `test_x86_external_and_local_calls_roundtrip_exactly`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'external/candidate.S').read_text`, `(tmp_path / 'external/candidate.bin').read_bytes`, `(tmp_path / 'local/candidate.S').read_text`, `(tmp_path / 'local/candidate.bin').read_bytes`, `_materialize`, `bytes.fromhex`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_x86_external_and_local_calls_roundtrip_exactly`  
**Area:** Toolkit behavior  
**Source line:** 61

## `test_x64_rip_relative_data_reference_roundtrips`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'candidate.S').read_text`, `(tmp_path / 'candidate.bin').read_bytes`, `_materialize`, `bytes.fromhex`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_x64_rip_relative_data_reference_roundtrips`  
**Area:** Toolkit behavior  
**Source line:** 85

## `test_noncanonical_instruction_falls_back_per_instruction`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'candidate.S').read_text`, `(tmp_path / 'candidate.bin').read_bytes`, `_materialize`, `bytes.fromhex`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_noncanonical_instruction_falls_back_per_instruction`  
**Area:** Toolkit behavior  
**Source line:** 98

## `test_unknown_target_uses_byte_fallback_without_false_claim`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'candidate.S').read_text`, `_materialize`, `bytes.fromhex`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_unknown_target_uses_byte_fallback_without_false_claim`  
**Area:** Toolkit behavior  
**Source line:** 113

## `test_verify_existing_source_reports_exact_and_mismatch`

No test docstring is declared.

**Direct call names in source:** `bytes.fromhex`, `source.write_text`, `verify_existing_source`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_verify_existing_source_reports_exact_and_mismatch`  
**Area:** Toolkit behavior  
**Source line:** 126

## `test_undecodable_tail_uses_complete_byte_form_fallback`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'candidate.S').read_text`, `(tmp_path / 'candidate.bin').read_bytes`, `_materialize`, `bytes.fromhex`  
**Node ID:** `tests/assembly/test_annotation_materialize.py::test_undecodable_tail_uses_complete_byte_form_fallback`  
**Area:** Toolkit behavior  
**Source line:** 158
