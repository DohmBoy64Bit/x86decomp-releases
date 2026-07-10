---
title: x86decomp coff-extract
description: Parser-derived command reference page for `coff-extract`.
---

# `x86decomp coff-extract`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp coff-extract [-h] [--size SIZE] object symbol output

positional arguments:
  object
  symbol
  output

options:
  -h, --help   show this help message and exit
  --size SIZE
```
