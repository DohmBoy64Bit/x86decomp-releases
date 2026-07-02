---
title: test-suite/tests/test_cli_and_installation.py
description: 2 exact current test nodes
original_path: tests/test-suite-tests-test-cli-and-installation.html
---

<a id="test-test-cli-init-config-catalog-and-missing-config"></a>
<a id="test-test-install-python-command-and-failure"></a>

Section: Source-derived test reference

# `test-suite/tests/test_cli_and_installation.py`

2 current test nodes in the Standalone verifier inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `b2d0c38e67585e901fc45d1a82839da0989a70d099ab9625d092b1d9c38dde4b`.

Metadata: Standalone verifier · line 15

### `test_cli_init_config_catalog_and_missing_config`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `config.is_file`, `cli.main`, `capsys.readouterr`, `str`

**Node ID:** `test-suite/tests/test_cli_and_installation.py::test_cli_init_config_catalog_and_missing_config`

Metadata: Standalone verifier · line 24

### `test_install_python_command_and_failure`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `AdapterSpec`, `HarnessConfig`, `monkeypatch.setattr`, `installation.install_python_adapter`, `commands.append`, `subprocess.CompletedProcess`, `pytest.raises`

**Node ID:** `test-suite/tests/test_cli_and_installation.py::test_install_python_command_and_failure`
