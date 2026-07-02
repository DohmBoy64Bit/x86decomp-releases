---
title: tests/assembly/test_annotation_materialize.py
description: 8 exact current test nodes
original_path: tests/tests-assembly-test-annotation-materialize.html
---

<a id="test-test-byte-form-is-exact-native-compatibility-output"></a>
<a id="test-test-annotation-is-idempotent-and-keeps-bytes"></a>
<a id="test-test-x86-external-and-local-calls-roundtrip-exactly"></a>
<a id="test-test-x64-rip-relative-data-reference-roundtrips"></a>
<a id="test-test-noncanonical-instruction-falls-back-per-instruction"></a>
<a id="test-test-unknown-target-uses-byte-fallback-without-false-claim"></a>
<a id="test-test-verify-existing-source-reports-exact-and-mismatch"></a>
<a id="test-test-undecodable-tail-uses-complete-byte-form-fallback"></a>

Section: Source-derived test reference

# `tests/assembly/test_annotation_materialize.py`

8 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `46aeb940a0ccb02b0312ef413ce123c3c647c0224a1f8b1f571d128ab733574f`.

Metadata: Toolkit behavior · line 20

### `test_byte_form_is_exact_native_compatibility_output`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `bytes`, `range`, `render_byte_assembly`, `_assembly_bytes`, `parse_byte_directives`, `pytest.raises`, `validate_symbol`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_byte_form_is_exact_native_compatibility_output`

Metadata: Toolkit behavior · line 30

### `test_annotation_is_idempotent_and_keeps_bytes`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `bytes.fromhex`, `source.write_text`, `annotate_source`, `render_byte_assembly`, `first.read_text`, `second.read_text`, `parse_byte_directives`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_annotation_is_idempotent_and_keeps_bytes`

Metadata: Toolkit behavior · line 61

### `test_x86_external_and_local_calls_roundtrip_exactly`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_materialize`, `bytes.fromhex`, `read_bytes`, `read_text`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_x86_external_and_local_calls_roundtrip_exactly`

Metadata: Toolkit behavior · line 85

### `test_x64_rip_relative_data_reference_roundtrips`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_materialize`, `bytes.fromhex`, `read_text`, `read_bytes`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_x64_rip_relative_data_reference_roundtrips`

Metadata: Toolkit behavior · line 98

### `test_noncanonical_instruction_falls_back_per_instruction`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_materialize`, `read_text`, `bytes.fromhex`, `read_bytes`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_noncanonical_instruction_falls_back_per_instruction`

Metadata: Toolkit behavior · line 113

### `test_unknown_target_uses_byte_fallback_without_false_claim`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_materialize`, `bytes.fromhex`, `read_text`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_unknown_target_uses_byte_fallback_without_false_claim`

Metadata: Toolkit behavior · line 126

### `test_verify_existing_source_reports_exact_and_mismatch`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `bytes.fromhex`, `source.write_text`, `verify_existing_source`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_verify_existing_source_reports_exact_and_mismatch`

Metadata: Toolkit behavior · line 158

### `test_undecodable_tail_uses_complete_byte_form_fallback`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `_materialize`, `bytes.fromhex`, `read_bytes`, `read_text`

**Node ID:** `tests/assembly/test_annotation_materialize.py::test_undecodable_tail_uses_complete_byte_form_fallback`
