---
title: x86decomp ghidra-export
description: Parser-derived command reference page for `ghidra-export`.
---

# `x86decomp ghidra-export`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp ghidra-export [-h] [--scripts-dir SCRIPTS_DIR]
                               [--ghidra-home GHIDRA_HOME] [--overwrite]
                               [--selector SELECTOR] [--timeout TIMEOUT]
                               [--report REPORT] [--print-command]
                               binary ghidra_project_dir ghidra_project_name
                               output_dir

positional arguments:
  binary
  ghidra_project_dir
  ghidra_project_name
  output_dir

options:
  -h, --help            show this help message and exit
  --scripts-dir SCRIPTS_DIR
  --ghidra-home GHIDRA_HOME
  --overwrite
  --selector SELECTOR
  --timeout TIMEOUT
  --report REPORT
  --print-command
```
