---
title: tests/test_artifacts.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_artifacts.py`

**Collected nodes:** 2  
**Source SHA-256:** `bcf7a774d955c365b701f002a37884e35babacc396f6a78188c6e2ada40bca67`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_import_and_verify`

No test docstring is declared.

**Direct call names in source:** `Path`, `import_function_artifact`, `self._export`, `self.assertTrue`, `tempfile.TemporaryDirectory`, `verify_function_artifact`  
**Node ID:** `tests/test_artifacts.py::ArtifactTests::test_import_and_verify`  
**Area:** Toolkit behavior  
**Source line:** 31

## `test_integrity_path_escape_is_rejected`

No test docstring is declared.

**Direct call names in source:** `Path`, `any`, `import_function_artifact`, `integrity['files'].append`, `integrity_path.read_text`, `integrity_path.write_text`, `json.dumps`, `json.loads`, `self._export`, `self.assertFalse`, `self.assertTrue`, `tempfile.TemporaryDirectory`, `verify_function_artifact`  
**Node ID:** `tests/test_artifacts.py::ArtifactTests::test_integrity_path_escape_is_rejected`  
**Area:** Toolkit behavior  
**Source line:** 38
