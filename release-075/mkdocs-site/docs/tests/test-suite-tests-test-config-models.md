---
title: test-suite/tests/test_config_models.py
description: Source-derived reference for 2 collected test nodes.
---

# `test-suite/tests/test_config_models.py`

**Collected nodes:** 2  
**Source SHA-256:** `1720714230e28811c1bef9e525b9e972075a3d65aab4c8117af23611c97445c4`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_config_roundtrip_and_relative_resolution`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'relative-toolkit').resolve`, `HarnessConfig`, `config.to_dict`, `json.dumps`, `json.loads`, `load_config`, `loaded.to_dict`, `path.read_text`, `path.write_text`, `save_config`  
**Node ID:** `tests/test_config_models.py::test_config_roundtrip_and_relative_resolution`  
**Area:** Standalone verification harness  
**Source line:** 10

## `test_status_counts_and_strict_exit_code`

No test docstring is declared.

**Direct call names in source:** `HarnessResult`, `ProbeResult`, `RunSummary`, `RunSummary(strict=False, test_results=[result(Status.BLOCKED)], **base).exit_code`, `RunSummary(strict=False, test_results=[result(Status.ERROR)], **base).exit_code`, `RunSummary(strict=False, test_results=[result(Status.FAIL)], **base).exit_code`, `RunSummary(strict=True, test_results=[result(Status.BLOCKED)], **base).exit_code`, `dict`, `normalized_path`, `result`, `str`, `tmp_path.resolve`  
**Node ID:** `tests/test_config_models.py::test_status_counts_and_strict_exit_code`  
**Area:** Standalone verification harness  
**Source line:** 36
