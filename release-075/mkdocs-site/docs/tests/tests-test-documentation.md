---
title: tests/test_documentation.py
description: Source-derived reference for 3 collected test nodes.
---

# `tests/test_documentation.py`

**Collected nodes:** 3  
**Source SHA-256:** `701c362f9c6d06ec0c2c2464e1ca62e6a10ff7868f1dc9729aebd9227ed6041f`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_release_documents_and_maps_are_current`

No test docstring is declared.

**Direct call names in source:** `path.read_text`  
**Node ID:** `tests/test_documentation.py::test_release_documents_and_maps_are_current`  
**Area:** Toolkit behavior  
**Source line:** 9

## `test_test_plan_counts_match_feature_catalog`

No test docstring is declared.

**Direct call names in source:** `(ROOT / 'test-suite/docs/TEST_PLAN.md').read_text`, `(ROOT / 'test-suite/src/x86decomp_testkit/data/feature_catalog.json').read_text`, `expected.items`, `json.loads`, `len`, `str`  
**Node ID:** `tests/test_documentation.py::test_test_plan_counts_match_feature_catalog`  
**Area:** Toolkit behavior  
**Source line:** 30

## `test_four_architecture_artifacts_exist_and_cross_link`

No test docstring is declared.

**Direct call names in source:** `path.is_file`, `path.read_text`, `suite_mermaid.read_text`, `toolkit_mermaid.read_text`  
**Node ID:** `tests/test_documentation.py::test_four_architecture_artifacts_exist_and_cross_link`  
**Area:** Toolkit behavior  
**Source line:** 49
