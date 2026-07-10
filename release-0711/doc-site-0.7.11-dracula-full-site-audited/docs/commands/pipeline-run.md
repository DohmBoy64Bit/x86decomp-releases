---
title: x86decomp pipeline-run
description: Parser-derived command reference page for `pipeline-run`.
---

# `x86decomp pipeline-run`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp pipeline-run [-h] [--continue-on-failure] project manifest

positional arguments:
  project
  manifest

options:
  -h, --help            show this help message and exit
  --continue-on-failure
```
