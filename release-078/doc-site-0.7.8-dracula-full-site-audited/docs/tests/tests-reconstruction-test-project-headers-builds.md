---
title: tests/reconstruction/test_project_headers_builds.py
description: Source-derived reference for 3 collected test nodes.
---

# `tests/reconstruction/test_project_headers_builds.py`

**Collected nodes:** 3  
**Source SHA-256:** `48264c55d224edf9ad5026b86eb4ef1ba7c900fe0e1ebe341c12c16aaec57d95`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_store_is_additive_and_layout_is_evidence_labeled`

No test docstring is declared.

**Direct call names in source:** `Path`, `Path(exported['path']).is_file`, `ProjectLayout`, `ReconstructionStore`, `layout.add_translation_unit_member`, `layout.create_translation_unit`, `layout.explain_boundaries`, `layout.export`, `layout.synthesize`, `len`, `store.check`  
**Node ID:** `tests/reconstruction/test_project_headers_builds.py::test_store_is_additive_and_layout_is_evidence_labeled`  
**Area:** Toolkit behavior  
**Source line:** 13

## `test_headers_reject_cycles_and_generate_compileable_shape`

No test docstring is declared.

**Direct call names in source:** `HeaderManager`, `Path`, `Path(generated['written_to']).read_text`, `ReconstructionStore`, `api.create`, `api.cycles`, `api.declare`, `api.include`, `api.synthesize`, `api.validate`, `pytest.raises`  
**Node ID:** `tests/reconstruction/test_project_headers_builds.py::test_headers_reject_cycles_and_generate_compileable_shape`  
**Area:** Toolkit behavior  
**Source line:** 32

## `test_historical_and_portable_build_modes_remain_distinct`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'src').mkdir`, `(tmp_path / 'src/main.c').write_text`, `BuildManager`, `Path`, `ReconstructionStore`, `api.add_target`, `api.add_variant`, `api.compare_modes`, `api.create`, `api.generate`, `api.matrix`, `api.validate`  
**Node ID:** `tests/reconstruction/test_project_headers_builds.py::test_historical_and_portable_build_modes_remain_distinct`  
**Area:** Toolkit behavior  
**Source line:** 45
