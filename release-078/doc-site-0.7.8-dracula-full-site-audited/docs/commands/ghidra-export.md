---
title: x86decomp ghidra-export
description: Exact v0.7.8 parser-derived reference for `x86decomp ghidra-export`.
---


# `x86decomp ghidra-export`

## Usage

```text
usage: x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR]
                               [--ghidra-home GHIDRA_HOME] [--overwrite]
                               [--selector SELECTOR] [--timeout TIMEOUT]
                               [--report REPORT] [--print-command]
                               binary ghidra_project_dir ghidra_project_name
                               output_dir
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `binary` | required · type: `_path` · parser destination: `binary`. No help text declared. |
| `ghidra_project_dir` | required · type: `_path` · parser destination: `ghidra_project_dir`. No help text declared. |
| `ghidra_project_name` | required · parser destination: `ghidra_project_name`. No help text declared. |
| `output_dir` | required · type: `_path` · parser destination: `output_dir`. No help text declared. |
| `--scripts-dir` | type: `_path` · default: `PosixPath('ghidra_scripts')` · parser destination: `scripts_dir`. No help text declared. |
| `--ghidra-home` | type: `_path` · parser destination: `ghidra_home`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |
| `--selector` | default: `'all'` · parser destination: `selector`. No help text declared. |
| `--timeout` | type: `int` · default: `3600` · parser destination: `timeout`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |
| `--print-command` | nargs: `0` · default: `False` · parser destination: `print_command`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
