---
title: tests/reconstruction/test_project_headers_builds.py
description: 3 exact current test nodes
original_path: tests/tests-reconstruction-test-project-headers-builds.html
---

<a id="test-test-store-is-additive-and-layout-is-evidence-labeled"></a>
<a id="test-test-headers-reject-cycles-and-generate-compileable-shape"></a>
<a id="test-test-historical-and-portable-build-modes-remain-distinct"></a>

Section: Source-derived test reference

# `tests/reconstruction/test_project_headers_builds.py`

3 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `48264c55d224edf9ad5026b86eb4ef1ba7c900fe0e1ebe341c12c16aaec57d95`.

Metadata: Toolkit behavior · line 13

### `test_store_is_additive_and_layout_is_evidence_labeled`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `ReconstructionStore`, `store.check`, `ProjectLayout`, `layout.synthesize`, `layout.explain_boundaries`, `layout.create_translation_unit`, `layout.add_translation_unit_member`, `layout.export`, `is_file`, `len`, `Path`

**Node ID:** `tests/reconstruction/test_project_headers_builds.py::test_store_is_additive_and_layout_is_evidence_labeled`

Metadata: Toolkit behavior · line 32

### `test_headers_reject_cycles_and_generate_compileable_shape`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `HeaderManager`, `api.create`, `api.declare`, `api.include`, `api.synthesize`, `read_text`, `ReconstructionStore`, `pytest.raises`, `api.cycles`, `api.validate`, `Path`

**Node ID:** `tests/reconstruction/test_project_headers_builds.py::test_headers_reject_cycles_and_generate_compileable_shape`

Metadata: Toolkit behavior · line 45

### `test_historical_and_portable_build_modes_remain_distinct`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `mkdir`, `write_text`, `BuildManager`, `api.create`, `api.add_target`, `api.add_variant`, `api.generate`, `api.compare_modes`, `ReconstructionStore`, `api.validate`, `Path`, `api.matrix`

**Node ID:** `tests/reconstruction/test_project_headers_builds.py::test_historical_and_portable_build_modes_remain_distinct`
