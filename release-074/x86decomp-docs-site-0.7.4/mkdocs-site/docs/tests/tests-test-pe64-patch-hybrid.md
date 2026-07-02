---
title: tests/test_pe64_patch_hybrid.py
description: 3 exact current test nodes
original_path: tests/tests-test-pe64-patch-hybrid.html
---

<a id="test-test-pe64-project"></a>
<a id="test-test-patch-image"></a>
<a id="test-test-hybrid-project-builds-assembly-objects"></a>

Section: Source-derived test reference

# `tests/test_pe64_patch_hybrid.py`

3 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f`.

Metadata: Toolkit behavior · line 12

### `test_pe64_project`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe64`, `parse_pe`, `initialize_project`, `verify_project`, `image.to_dict`

**Node ID:** `tests/test_pe64_patch_hybrid.py::test_pe64_project`

Metadata: Toolkit behavior · line 22

### `test_patch_image`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `candidate.write_bytes`, `patch_pe_function`, `candidate.read_bytes`, `output.read_bytes`, `parse_pe`

**Node ID:** `tests/test_pe64_patch_hybrid.py::test_patch_image`

Metadata: Toolkit behavior · line 33

### `test_hybrid_project_builds_assembly_objects`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `initialize_project`, `mkdir`, `write_bytes`, `write_text`, `generate_hybrid_project`, `is_file`, `subprocess.run`, `json.dumps`, `len`

**Node ID:** `tests/test_pe64_patch_hybrid.py::test_hybrid_project_builds_assembly_objects`
