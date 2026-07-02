---
title: tests/test_linker_metadata_corpus.py
description: 10 exact current test nodes
original_path: tests/tests-test-linker-metadata-corpus.html
---

<a id="test-test-bigobj-and-comdat-resolution"></a>
<a id="test-test-map-parser-and-layout-reconstruction"></a>
<a id="test-test-target-specific-image-normalization"></a>
<a id="test-test-msvc-rtti-unwind-and-static-initializer-recovery"></a>
<a id="test-test-compiler-ground-truth-corpus"></a>
<a id="test-test-symbolic-memory-alias-model"></a>
<a id="test-test-real-clang-weak-external-and-tls-coff"></a>
<a id="test-test-builtin-corpus-manifest-is-expanded-and-sources-compile"></a>
<a id="test-test-ground-truth-cross-report-comparison"></a>
<a id="test-test-image-profile-can-explicitly-normalize-debug-records"></a>

Section: Source-derived test reference

# `tests/test_linker_metadata_corpus.py`

10 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `aa88771eecf6bbd2a6fcc6230848165884fea583b48688061d61c14756f9a1de`.

Metadata: Toolkit behavior · line 58

### `test_bigobj_and_comdat_resolution`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `parse_coff_bytes`, `resolve_comdats`, `_minimal_bigobj`, `build_comdat_coff`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_bigobj_and_comdat_resolution`

Metadata: Toolkit behavior · line 82

### `test_map_parser_and_layout_reconstruction`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `parse_msvc_map_text`, `map_path.write_text`, `reconstruct_linker_layout`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_map_parser_and_layout_reconstruction`

Metadata: Toolkit behavior · line 109

### `test_target_specific_image_normalization`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `bytearray`, `struct.pack_into`, `candidate.write_bytes`, `derive_layout_profile`, `compare_whole_images`, `reference.read_bytes`, `struct.unpack_from`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_target_specific_image_normalization`

Metadata: Toolkit behavior · line 126

### `test_msvc_rtti_unwind_and_static_initializer_recovery`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `source.write_text`, `subprocess.run`, `analyze_msvc_metadata`, `scan_static_initializers`, `any`, `len`, `str`, `startswith`, `shutil.which`, `upper`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_msvc_rtti_unwind_and_static_initializer_recovery`

Metadata: Toolkit behavior · line 162

### `test_compiler_ground_truth_corpus`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `source.write_text`, `manifest.write_text`, `build_ground_truth_corpus`, `all`, `json.dumps`, `verify_ground_truth_corpus`, `shutil.which`, `get`, `build.get`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_compiler_ground_truth_corpus`

Metadata: Toolkit behavior · line 185

### `test_symbolic_memory_alias_model`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `pytest.importorskip`, `bytes.fromhex`, `angr_memory_alias_compare`, `shutil.which`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_symbolic_memory_alias_model`

Metadata: Toolkit behavior · line 208

### `test_real_clang_weak_external_and_tls_coff`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `weak_source.write_text`, `subprocess.run`, `parse_coff`, `next`, `tls_source.write_text`, `scan_coff_tls`, `any`, `shutil.which`, `str`, `__import__`, `weak_symbol.weak_external.to_dict`, `startswith`, `upper`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_real_clang_weak_external_and_tls_coff`

Metadata: Toolkit behavior · line 239

### `test_builtin_corpus_manifest_is_expanded_and_sources_compile`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `create_builtin_manifest`, `len`, `set`, `is_file`, `resolve`, `shutil.which`, `Path`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_builtin_corpus_manifest_is_expanded_and_sources_compile`

Metadata: Toolkit behavior · line 251

### `test_ground_truth_cross_report_comparison`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `enumerate`, `compare_ground_truth_corpora`, `path.write_text`, `reports.append`, `json.dumps`, `str`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_ground_truth_cross_report_comparison`

Metadata: Toolkit behavior · line 278

### `test_image_profile_can_explicitly_normalize_debug_records`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.mark.skipif`, `source.write_text`, `subprocess.run`, `parse_pe`, `bytearray`, `candidate.write_bytes`, `derive_layout_profile`, `profile_path.write_text`, `compare_whole_images`, `any`, `reference.read_bytes`, `json.dumps`, `str`, `startswith`, `shutil.which`

**Node ID:** `tests/test_linker_metadata_corpus.py::test_image_profile_can_explicitly_normalize_debug_records`
