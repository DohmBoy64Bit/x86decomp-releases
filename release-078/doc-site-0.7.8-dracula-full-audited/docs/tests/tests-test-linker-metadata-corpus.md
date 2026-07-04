---
title: tests/test_linker_metadata_corpus.py
description: Source-derived reference for 10 collected test nodes.
---

# `tests/test_linker_metadata_corpus.py`

**Collected nodes:** 10  
**Source SHA-256:** `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_bigobj_and_comdat_resolution`

No test docstring is declared.

**Direct call names in source:** `_minimal_bigobj`, `build_comdat_coff`, `parse_coff_bytes`, `resolve_comdats`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_bigobj_and_comdat_resolution`  
**Area:** Toolkit behavior  
**Source line:** 58

## `test_map_parser_and_layout_reconstruction`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `map_path.write_text`, `parse_msvc_map_text`, `reconstruct_linker_layout`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_map_parser_and_layout_reconstruction`  
**Area:** Toolkit behavior  
**Source line:** 82

## `test_target_specific_image_normalization`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `bytearray`, `candidate.write_bytes`, `compare_whole_images`, `derive_layout_profile`, `reference.read_bytes`, `struct.pack_into`, `struct.unpack_from`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_target_specific_image_normalization`  
**Area:** Toolkit behavior  
**Source line:** 109

## `test_msvc_rtti_unwind_and_static_initializer_recovery`

No test docstring is declared.

**Direct call names in source:** `analyze_msvc_metadata`, `any`, `item['section'].upper`, `item['section'].upper().startswith`, `len`, `pytest.mark.skipif`, `scan_static_initializers`, `shutil.which`, `source.write_text`, `str`, `subprocess.run`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_msvc_rtti_unwind_and_static_initializer_recovery`  
**Area:** Toolkit behavior  
**Source line:** 126

## `test_compiler_ground_truth_corpus`

No test docstring is declared.

**Direct call names in source:** `all`, `build.get`, `build.get('coff', {}).get`, `build_ground_truth_corpus`, `json.dumps`, `manifest.write_text`, `pytest.mark.skipif`, `shutil.which`, `source.write_text`, `verify_ground_truth_corpus`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_compiler_ground_truth_corpus`  
**Area:** Toolkit behavior  
**Source line:** 162

## `test_symbolic_memory_alias_model`

No test docstring is declared.

**Direct call names in source:** `angr_memory_alias_compare`, `bytes.fromhex`, `pytest.importorskip`, `pytest.mark.skipif`, `shutil.which`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_symbolic_memory_alias_model`  
**Area:** Toolkit behavior  
**Source line:** 185

## `test_real_clang_weak_external_and_tls_coff`

No test docstring is declared.

**Direct call names in source:** `__import__`, `__import__('x86decomp.coff', fromlist=['parse_coff']).parse_coff`, `any`, `item['section'].upper`, `item['section'].upper().startswith`, `next`, `pytest.mark.skipif`, `scan_coff_tls`, `shutil.which`, `str`, `subprocess.run`, `tls_source.write_text`, `weak_source.write_text`, `weak_symbol.weak_external.to_dict`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_real_clang_weak_external_and_tls_coff`  
**Area:** Toolkit behavior  
**Source line:** 208

## `test_builtin_corpus_manifest_is_expanded_and_sources_compile`

No test docstring is declared.

**Direct call names in source:** `(manifest_path.parent / case['source']).resolve`, `(manifest_path.parent / case['source']).resolve().is_file`, `Path`, `Path(__file__).resolve`, `create_builtin_manifest`, `len`, `pytest.mark.skipif`, `set`, `shutil.which`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_builtin_corpus_manifest_is_expanded_and_sources_compile`  
**Area:** Toolkit behavior  
**Source line:** 239

## `test_ground_truth_cross_report_comparison`

No test docstring is declared.

**Direct call names in source:** `compare_ground_truth_corpora`, `enumerate`, `json.dumps`, `path.write_text`, `reports.append`, `str`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_ground_truth_cross_report_comparison`  
**Area:** Toolkit behavior  
**Source line:** 251

## `test_image_profile_can_explicitly_normalize_debug_records`

No test docstring is declared.

**Direct call names in source:** `any`, `bytearray`, `candidate.write_bytes`, `compare_whole_images`, `derive_layout_profile`, `item['reason'].startswith`, `json.dumps`, `parse_pe`, `profile_path.write_text`, `pytest.mark.skipif`, `reference.read_bytes`, `shutil.which`, `source.write_text`, `str`, `subprocess.run`  
**Node ID:** `tests/test_linker_metadata_corpus.py::test_image_profile_can_explicitly_normalize_debug_records`  
**Area:** Toolkit behavior  
**Source line:** 278
