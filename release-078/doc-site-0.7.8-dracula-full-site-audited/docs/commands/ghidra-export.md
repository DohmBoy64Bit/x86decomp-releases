---
title: x86decomp ghidra-export
description: Command reference for `x86decomp ghidra-export`.
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

| Argument | Details |
| --- | --- |
| `binary` | required · type: `path`. |
| `ghidra_project_dir` | required · type: `path`. |
| `ghidra_project_name` | required. |
| `output_dir` | required · type: `path`. |
| `--scripts-dir` | type: `path` · default: `PosixPath('ghidra_scripts')`. |
| `--ghidra-home` | type: `path`. |
| `--overwrite` | nargs: `0` · default: `False`. |
| `--selector` | default: `'all'`. |
| `--timeout` | type: `int` · default: `3600`. |
| `--report` | type: `path`. |
| `--print-command` | nargs: `0` · default: `False`. |


