---
title: x86decomp ghidra-export
description: Exact parser-derived reference for x86decomp ghidra-export in 0.7.5.
---

# `x86decomp ghidra-export`

## `x86decomp ghidra-export`

usage: x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR]

### Usage

```text
x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR]
                               [--ghidra-home GHIDRA_HOME] [--overwrite]
                               [--selector SELECTOR] [--timeout TIMEOUT]
                               [--report REPORT] [--print-command]
                               binary ghidra_project_dir ghidra_project_name
                               output_dir
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `binary` | required · type: `_path`. No help text is declared; parser destination is `binary`. |
| `ghidra_project_dir` | required · type: `_path`. No help text is declared; parser destination is `ghidra_project_dir`. |
| `ghidra_project_name` | required. No help text is declared; parser destination is `ghidra_project_name`. |
| `output_dir` | required · type: `_path`. No help text is declared; parser destination is `output_dir`. |
| `--scripts-dir` | default: `PosixPath('ghidra_scripts')` · type: `_path`. No help text is declared; parser destination is `scripts_dir`. |
| `--ghidra-home` | type: `_path`. No help text is declared; parser destination is `ghidra_home`. |
| `--overwrite` | default: `False` · nargs: `0`. No help text is declared; parser destination is `overwrite`. |
| `--selector` | default: `'all'`. No help text is declared; parser destination is `selector`. |
| `--timeout` | default: `3600` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |
| `--print-command` | default: `False` · nargs: `0`. No help text is declared; parser destination is `print_command`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
