---
title: x86decomp convergence-analyze
description: Parser-derived command reference page for `convergence-analyze`.
---

# `x86decomp convergence-analyze`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp convergence-analyze [-h] [--profile PROFILE]
                                     [--previous PREVIOUS] [--report REPORT]
                                     [--history HISTORY]
                                     reference candidate

positional arguments:
  reference
  candidate

options:
  -h, --help           show this help message and exit
  --profile PROFILE
  --previous PREVIOUS
  --report REPORT
  --history HISTORY
```
