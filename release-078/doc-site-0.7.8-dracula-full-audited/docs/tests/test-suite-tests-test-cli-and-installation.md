---
title: test-suite/tests/test_cli_and_installation.py
description: Source-derived reference for 2 collected test nodes.
---

# `test-suite/tests/test_cli_and_installation.py`

**Collected nodes:** 2  
**Source SHA-256:** `b2d0c38e67585e901fc45d1a82839da0989a70d099ab9625d092b1d9c38dde4b`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_cli_init_config_catalog_and_missing_config`

No test docstring is declared.

**Direct call names in source:** `capsys.readouterr`, `cli.main`, `config.is_file`, `str`  
**Node ID:** `tests/test_cli_and_installation.py::test_cli_init_config_catalog_and_missing_config`  
**Area:** Standalone verification harness  
**Source line:** 15

## `test_install_python_command_and_failure`

No test docstring is declared.

**Direct call names in source:** `AdapterSpec`, `HarnessConfig`, `commands.append`, `installation.install_python_adapter`, `monkeypatch.setattr`, `pytest.raises`, `subprocess.CompletedProcess`  
**Node ID:** `tests/test_cli_and_installation.py::test_install_python_command_and_failure`  
**Area:** Standalone verification harness  
**Source line:** 24
