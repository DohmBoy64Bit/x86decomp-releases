---
title: tests/test_release_contract.py
description: Source-derived reference for 8 collected test nodes.
---

# `tests/test_release_contract.py`

**Collected nodes:** 8  
**Source SHA-256:** `970058e4554e3b48ce0cd426a6037847577a9e6eb5981bb3995dc735dce9e8b4`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_current_command_and_schema_contract`

No test docstring is declared.

**Direct call names in source:** `(ROOT / 'examples/contracts/command-surface.json').read_text`, `(ROOT / 'schemas' / name).is_file`, `_commands`, `all`, `canonical_groups`, `canonical_routes`, `json.loads`, `len`, `set`, `set(contract['commands']).issubset`  
**Node ID:** `tests/test_release_contract.py::test_current_command_and_schema_contract`  
**Area:** Toolkit behavior  
**Source line:** 21

## `test_schema_project_and_function_documents_remain_valid`

No test docstring is declared.

**Direct call names in source:** `(ROOT / 'schemas/function.schema.json').read_text`, `(ROOT / 'schemas/project.schema.json').read_text`, `Draft202012Validator`, `Draft202012Validator(function_schema).validate`, `Draft202012Validator(project_schema).validate`, `json.loads`  
**Node ID:** `tests/test_release_contract.py::test_schema_project_and_function_documents_remain_valid`  
**Area:** Toolkit behavior  
**Source line:** 29

## `test_ground_truth_sources_are_packaged_and_in_sync`

No test docstring is declared.

**Direct call names in source:** `len`, `package_sources.iterdir`, `path.is_file`, `path.read_bytes`, `repository_sources.iterdir`  
**Node ID:** `tests/test_release_contract.py::test_ground_truth_sources_are_packaged_and_in_sync`  
**Area:** Toolkit behavior  
**Source line:** 55

## `test_current_public_surface_contract`

No test docstring is declared.

**Direct call names in source:** `'.'.join`, `(ROOT / 'examples/contracts/public-surface.json').read_text`, `(ROOT / 'ghidra_scripts' / name).is_file`, `(ROOT / 'schemas' / name).is_file`, `(ROOT / 'src/x86decomp').rglob`, `_commands`, `adapter_catalog`, `all`, `json.loads`, `list`, `package_modules.add`, `parts.pop`, `path.relative_to`, `path.relative_to(ROOT / 'src/x86decomp').with_suffix`, `set`, `set(contract['adapter_ids']).issubset`, `set(contract['commands']).issubset`, `set(contract['modules']).issubset`  
**Node ID:** `tests/test_release_contract.py::test_current_public_surface_contract`  
**Area:** Toolkit behavior  
**Source line:** 64

## `test_exact_recursive_feature_catalog_matches_current_tree`

No test docstring is declared.

**Direct call names in source:** `(ROOT / 'test-suite/src/x86decomp_testkit/data/feature_catalog.json').read_text`, `audit_catalog`, `build_inventory`, `json.loads`  
**Node ID:** `tests/test_release_contract.py::test_exact_recursive_feature_catalog_matches_current_tree`  
**Area:** Toolkit behavior  
**Source line:** 82

## `test_repository_contains_only_the_current_release_contract`

No test docstring is declared.

**Direct call names in source:** `'.'.join`, `(ROOT / 'pyproject.toml').read_text`, `(ROOT / 'test-suite/pyproject.toml').read_text`, `ROOT.rglob`, `_commands`, `any`, `forbidden_paths.append`, `part.endswith`, `path.is_dir`, `path.is_file`, `path.name.lower`, `path.read_text`, `path.relative_to`, `path.relative_to(ROOT).as_posix`, `path.suffix.lower`, `re.search`, `relative.lower`, `str`, `tomllib.loads`, `tuple`, `violations.append`  
**Node ID:** `tests/test_release_contract.py::test_repository_contains_only_the_current_release_contract`  
**Area:** Toolkit behavior  
**Source line:** 95

## `test_no_placeholder_implementations_in_current_python_sources`

No test docstring is declared.

**Direct call names in source:** `ast.parse`, `ast.walk`, `base.rglob`, `findings.append`, `getattr`, `isinstance`, `len`, `path.read_text`, `path.relative_to`, `str`  
**Node ID:** `tests/test_release_contract.py::test_no_placeholder_implementations_in_current_python_sources`  
**Area:** Toolkit behavior  
**Source line:** 140

## `test_deterministic_source_hash_tool_detects_drift`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'PKG-INFO').write_text`, `(tmp_path / 'current.txt').write_text`, `(tmp_path / 'test-suite').mkdir`, `(tmp_path / 'test-suite/current.txt').write_text`, `importlib.util.module_from_spec`, `importlib.util.spec_from_file_location`, `module.generate_all`, `module.verify_all`, `spec.loader.exec_module`  
**Node ID:** `tests/test_release_contract.py::test_deterministic_source_hash_tool_detects_drift`  
**Area:** Toolkit behavior  
**Source line:** 165
