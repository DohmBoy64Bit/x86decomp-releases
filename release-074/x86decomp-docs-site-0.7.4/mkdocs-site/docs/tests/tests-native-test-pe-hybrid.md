---
title: tests/native/test_pe_hybrid.py
description: 4 exact current test nodes
original_path: tests/tests-native-test-pe-hybrid.html
---

<a id="test-test-safe-patch-and-text-swap-preserve-pe-container"></a>
<a id="test-test-section-export-and-synthetic-coff-for-pe32-and-pe64"></a>
<a id="test-test-hybrid-composer-promotes-only-verified-candidates"></a>
<a id="test-test-hybrid-composer-rejects-candidate-changed-after-match"></a>

Section: Source-derived test reference

# `tests/native/test_pe_hybrid.py`

4 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `f348168b73353f4da20583dc0c5b4e2d1dfb9e052dc185f236098ff4898cfc1e`.

Metadata: Toolkit behavior · line 11

### `test_safe_patch_and_text_swap_preserve_pe_container`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `NativeStore`, `PEReconstruction`, `replacement.write_bytes`, `api.text_swap`, `original.read_bytes`, `parse_pe`, `hex`, `apply_operations`, `plan_patch`

**Node ID:** `tests/native/test_pe_hybrid.py::test_safe_patch_and_text_swap_preserve_pe_container`

Metadata: Toolkit behavior · line 22

### `test_section_export_and_synthetic_coff_for_pe32_and_pe64`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `builder`, `PEReconstruction`, `api.export_sections`, `api.export_coff`, `NativeStore`, `len`

**Node ID:** `tests/native/test_pe_hybrid.py::test_section_export_and_synthetic_coff_for_pe32_and_pe64`

Metadata: Toolkit behavior · line 29

### `test_hybrid_composer_promotes_only_verified_candidates`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `good.write_bytes`, `bad.write_bytes`, `NativeStore`, `batch`, `compose`, `read_bytes`, `good.read_bytes`, `FunctionMatching`, `HybridComposer`, `original.read_bytes`, `str`

**Node ID:** `tests/native/test_pe_hybrid.py::test_hybrid_composer_promotes_only_verified_candidates`

Metadata: Toolkit behavior · line 42

### `test_hybrid_composer_rejects_candidate_changed_after_match`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `candidate.write_bytes`, `NativeStore`, `batch`, `pytest.raises`, `compose`, `FunctionMatching`, `str`, `HybridComposer`

**Node ID:** `tests/native/test_pe_hybrid.py::test_hybrid_composer_rejects_candidate_changed_after_match`
