---
title: x86decomp init
description: Parser-derived command reference page for `init`.
---

# `x86decomp init`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp init [-h] [--reference-binary] binary project

positional arguments:
  binary
  project

options:
  -h, --help          show this help message and exit
  --reference-binary
```
