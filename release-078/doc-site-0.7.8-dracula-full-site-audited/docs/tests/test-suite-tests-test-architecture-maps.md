---
title: test-suite/tests/test_architecture_maps.py
description: Source-derived reference for 4 collected test nodes.
---

# `test-suite/tests/test_architecture_maps.py`

**Collected nodes:** 4  
**Source SHA-256:** `2d88761b464353e4b026dc159bb4421be045eb1ed8f48c261921abda8d3d3c23`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_all_architecture_map_artifacts_exist_and_are_versioned`

No test docstring is declared.

**Direct call names in source:** `_repository_root`, `path.is_file`, `path.read_text`  
**Node ID:** `tests/test_architecture_maps.py::test_all_architecture_map_artifacts_exist_and_are_versioned`  
**Area:** Standalone verification harness  
**Source line:** 22

## `test_toolkit_mermaid_and_ascii_maps_cover_same_major_planes_and_states`

No test docstring is declared.

**Direct call names in source:** `(root / 'docs/ARCHITECTURE_MAP.md').read_text`, `(root / 'docs/ARCHITECTURE_MAP_ASCII.txt').read_text`, `_normalized`, `_repository_root`  
**Node ID:** `tests/test_architecture_maps.py::test_toolkit_mermaid_and_ascii_maps_cover_same_major_planes_and_states`  
**Area:** Standalone verification harness  
**Source line:** 31

## `test_test_suite_mermaid_and_ascii_maps_cover_same_resolution_and_gate_contract`

No test docstring is declared.

**Direct call names in source:** `(root / 'test-suite/docs/ARCHITECTURE_MAP.md').read_text`, `(root / 'test-suite/docs/ARCHITECTURE_MAP_ASCII.txt').read_text`, `_normalized`, `_repository_root`  
**Node ID:** `tests/test_architecture_maps.py::test_test_suite_mermaid_and_ascii_maps_cover_same_resolution_and_gate_contract`  
**Area:** Standalone verification harness  
**Source line:** 57

## `test_architecture_map_cross_links_and_ascii_format_contract`

No test docstring is declared.

**Direct call names in source:** `(root / 'docs/ARCHITECTURE_MAP.md').read_text`, `(root / 'test-suite/docs/ARCHITECTURE_MAP.md').read_text`, `(root / relative).read_text`, `_repository_root`  
**Node ID:** `tests/test_architecture_maps.py::test_architecture_map_cross_links_and_ascii_format_contract`  
**Area:** Standalone verification harness  
**Source line:** 82
