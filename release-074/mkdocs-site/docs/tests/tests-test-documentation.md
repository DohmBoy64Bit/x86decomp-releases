---
title: tests/test_documentation.py
description: 3 exact current test nodes
original_path: tests/tests-test-documentation.html
---

<a id="test-test-release-documents-and-maps-are-current"></a>
<a id="test-test-test-plan-counts-match-feature-catalog"></a>
<a id="test-test-four-architecture-artifacts-exist-and-cross-link"></a>

Section: Source-derived test reference

# `tests/test_documentation.py`

3 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `803da6706a55de973a498ef159c757d5c2bf7b7b9a023885c17b8671d6006e29`.

Metadata: Toolkit behavior · line 9

### `test_release_documents_and_maps_are_current`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `path.read_text`

**Node ID:** `tests/test_documentation.py::test_release_documents_and_maps_are_current`

Metadata: Toolkit behavior · line 30

### `test_test_plan_counts_match_feature_catalog`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `json.loads`, `read_text`, `expected.items`, `len`, `str`

**Node ID:** `tests/test_documentation.py::test_test_plan_counts_match_feature_catalog`

Metadata: Toolkit behavior · line 49

### `test_four_architecture_artifacts_exist_and_cross_link`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `path.is_file`, `toolkit_mermaid.read_text`, `suite_mermaid.read_text`, `path.read_text`

**Node ID:** `tests/test_documentation.py::test_four_architecture_artifacts_exist_and_cross_link`
