---
title: x86decomp reproduce-create
description: Parser-derived command reference page for `reproduce-create`.
---

# `x86decomp reproduce-create`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp reproduce-create [-h] [--required-tool REQUIRED_TOOL]
                                  project output

positional arguments:
  project
  output

options:
  -h, --help            show this help message and exit
  --required-tool REQUIRED_TOOL
```
