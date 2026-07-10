---
title: x86decomp drcov-run
description: Parser-derived command reference page for `drcov-run`.
---

# `x86decomp drcov-run`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp drcov-run [-h] [--drrun DRRUN] [--program-arg PROGRAM_ARG]
                           [--timeout TIMEOUT] [--report REPORT]
                           executable output_directory

positional arguments:
  executable
  output_directory

options:
  -h, --help            show this help message and exit
  --drrun DRRUN
  --program-arg PROGRAM_ARG
  --timeout TIMEOUT
  --report REPORT
```
