---
title: x86decomp ghidra-export
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/ghidra-export.html
---

<a id="command-ghidra-export"></a>

Section: Command reference

# `x86decomp ghidra-export`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp ghidra-export --help
```

Metadata: current · core

## `x86decomp ghidra-export`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR]
                               [--ghidra-home GHIDRA_HOME] [--overwrite]
                               [--selector SELECTOR] [--timeout TIMEOUT]
                               [--report REPORT] [--print-command]
                               binary ghidra_project_dir ghidra_project_name
                               output_dir
```

### Syntax example

```
x86decomp ghidra-export ./target.exe ./work ./work ./output
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `binary` required · type: _path | No argument help text is declared; parser destination is `binary`. |
| `ghidra_project_dir` required · type: _path | No argument help text is declared; parser destination is `ghidra_project_dir`. |
| `ghidra_project_name` required | No argument help text is declared; parser destination is `ghidra_project_name`. |
| `output_dir` required · type: _path | No argument help text is declared; parser destination is `output_dir`. |
| `--scripts-dir` default: ghidra_scripts · type: _path | No argument help text is declared; parser destination is `scripts_dir`. |
| `--ghidra-home` type: _path | No argument help text is declared; parser destination is `ghidra_home`. |
| `--overwrite` nargs: 0 · default: False | No argument help text is declared; parser destination is `overwrite`. |
| `--selector` default: 'all' | No argument help text is declared; parser destination is `selector`. |
| `--timeout` default: 3600 · type: int | No argument help text is declared; parser destination is `timeout`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |
| `--print-command` nargs: 0 · default: False | No argument help text is declared; parser destination is `print_command`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
