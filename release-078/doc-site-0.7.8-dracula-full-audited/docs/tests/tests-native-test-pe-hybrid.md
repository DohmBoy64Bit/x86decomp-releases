---
title: tests/native/test_pe_hybrid.py
description: Source-derived reference for 4 collected test nodes.
---

# `tests/native/test_pe_hybrid.py`

**Collected nodes:** 4  
**Source SHA-256:** `f348168b73353f4da20583dc0c5b4e2d1dfb9e052dc185f236098ff4898cfc1e`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_safe_patch_and_text_swap_preserve_pe_container`

No test docstring is declared.

**Direct call names in source:** `NativeStore`, `PEReconstruction`, `api.text_swap`, `apply_operations`, `build_minimal_pe32`, `original.read_bytes`, `original_bytes[512:514].hex`, `parse_pe`, `plan_patch`, `replacement.write_bytes`  
**Node ID:** `tests/native/test_pe_hybrid.py::test_safe_patch_and_text_swap_preserve_pe_container`  
**Area:** Toolkit behavior  
**Source line:** 11

## `test_section_export_and_synthetic_coff_for_pe32_and_pe64`

No test docstring is declared.

**Direct call names in source:** `NativeStore`, `PEReconstruction`, `api.export_coff`, `api.export_sections`, `builder`, `len`  
**Node ID:** `tests/native/test_pe_hybrid.py::test_section_export_and_synthetic_coff_for_pe32_and_pe64`  
**Area:** Toolkit behavior  
**Source line:** 22

## `test_hybrid_composer_promotes_only_verified_candidates`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'hybrid.exe').read_bytes`, `FunctionMatching`, `FunctionMatching(store).batch`, `HybridComposer`, `HybridComposer(store).compose`, `NativeStore`, `bad.write_bytes`, `build_minimal_pe32`, `good.read_bytes`, `good.write_bytes`, `original.read_bytes`, `str`  
**Node ID:** `tests/native/test_pe_hybrid.py::test_hybrid_composer_promotes_only_verified_candidates`  
**Area:** Toolkit behavior  
**Source line:** 29

## `test_hybrid_composer_rejects_candidate_changed_after_match`

No test docstring is declared.

**Direct call names in source:** `FunctionMatching`, `FunctionMatching(store).batch`, `HybridComposer`, `HybridComposer(store).compose`, `NativeStore`, `build_minimal_pe32`, `candidate.write_bytes`, `pytest.raises`, `str`  
**Node ID:** `tests/native/test_pe_hybrid.py::test_hybrid_composer_rejects_candidate_changed_after_match`  
**Area:** Toolkit behavior  
**Source line:** 42
