---
title: tests/test_release_contract.py
description: 8 exact current test nodes
original_path: tests/tests-test-release-contract.html
---

<a id="test-test-current-command-and-schema-contract"></a>
<a id="test-test-schema-project-and-function-documents-remain-valid"></a>
<a id="test-test-ground-truth-sources-are-packaged-and-in-sync"></a>
<a id="test-test-current-public-surface-contract"></a>
<a id="test-test-exact-recursive-feature-catalog-matches-current-tree"></a>
<a id="test-test-repository-contains-only-the-current-release-contract"></a>
<a id="test-test-no-placeholder-implementations-in-current-python-sources"></a>
<a id="test-test-deterministic-source-hash-tool-detects-drift"></a>

Section: Source-derived test reference

# `tests/test_release_contract.py`

8 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `07d1e8f1825baea6ebb7014c9f1a1fb3cfd17b2794848c6f059e2fd62140f5c5`.

Metadata: Toolkit behavior · line 21

### `test_current_command_and_schema_contract`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `json.loads`, `issubset`, `all`, `read_text`, `_commands`, `len`, `set`, `is_file`, `canonical_groups`, `canonical_routes`

**Node ID:** `tests/test_release_contract.py::test_current_command_and_schema_contract`

Metadata: Toolkit behavior · line 29

### `test_schema_project_and_function_documents_remain_valid`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `json.loads`, `validate`, `read_text`, `Draft202012Validator`

**Node ID:** `tests/test_release_contract.py::test_schema_project_and_function_documents_remain_valid`

Metadata: Toolkit behavior · line 55

### `test_ground_truth_sources_are_packaged_and_in_sync`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `path.read_bytes`, `len`, `repository_sources.iterdir`, `path.is_file`, `package_sources.iterdir`

**Node ID:** `tests/test_release_contract.py::test_ground_truth_sources_are_packaged_and_in_sync`

Metadata: Toolkit behavior · line 64

### `test_current_public_surface_contract`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `json.loads`, `issubset`, `all`, `set`, `rglob`, `read_text`, `_commands`, `with_suffix`, `list`, `package_modules.add`, `is_file`, `parts.pop`, `adapter_catalog`, `path.relative_to`, `join`

**Node ID:** `tests/test_release_contract.py::test_current_public_surface_contract`

Metadata: Toolkit behavior · line 82

### `test_exact_recursive_feature_catalog_matches_current_tree`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `json.loads`, `audit_catalog`, `read_text`, `build_inventory`

**Node ID:** `tests/test_release_contract.py::test_exact_recursive_feature_catalog_matches_current_tree`

Metadata: Toolkit behavior · line 95

### `test_repository_contains_only_the_current_release_contract`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tuple`, `ROOT.rglob`, `any`, `as_posix`, `relative.lower`, `path.read_text`, `tomllib.loads`, `_commands`, `join`, `path.is_dir`, `re.search`, `forbidden_paths.append`, `path.is_file`, `read_text`, `path.relative_to`, `violations.append`, `str`, `part.endswith`, `path.name.lower`, `path.suffix.lower`

**Node ID:** `tests/test_release_contract.py::test_repository_contains_only_the_current_release_contract`

Metadata: Toolkit behavior · line 140

### `test_no_placeholder_implementations_in_current_python_sources`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `base.rglob`, `ast.parse`, `ast.walk`, `path.read_text`, `isinstance`, `str`, `findings.append`, `len`, `getattr`, `path.relative_to`

**Node ID:** `tests/test_release_contract.py::test_no_placeholder_implementations_in_current_python_sources`

Metadata: Toolkit behavior · line 165

### `test_deterministic_source_hash_tool_detects_drift`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `importlib.util.spec_from_file_location`, `importlib.util.module_from_spec`, `spec.loader.exec_module`, `mkdir`, `write_text`, `module.generate_all`, `module.verify_all`

**Node ID:** `tests/test_release_contract.py::test_deterministic_source_hash_tool_detects_drift`
