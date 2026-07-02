---
title: tests/test_artifacts.py
description: 2 exact current test nodes
original_path: tests/tests-test-artifacts.html
---

<a id="test-artifacttests-test-import-and-verify"></a>
<a id="test-artifacttests-test-integrity-path-escape-is-rejected"></a>

Section: Source-derived test reference

# `tests/test_artifacts.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `bcf7a774d955c365b701f002a37884e35babacc396f6a78188c6e2ada40bca67`.

Metadata: Toolkit behavior · line 31

### `ArtifactTests::test_import_and_verify`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `Path`, `import_function_artifact`, `verify_function_artifact`, `self.assertTrue`, `self._export`

**Node ID:** `tests/test_artifacts.py::ArtifactTests::test_import_and_verify`

Metadata: Toolkit behavior · line 38

### `ArtifactTests::test_integrity_path_escape_is_rejected`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `Path`, `import_function_artifact`, `json.loads`, `append`, `integrity_path.write_text`, `verify_function_artifact`, `self.assertFalse`, `self.assertTrue`, `self._export`, `integrity_path.read_text`, `json.dumps`, `any`

**Node ID:** `tests/test_artifacts.py::ArtifactTests::test_integrity_path_escape_is_rejected`
