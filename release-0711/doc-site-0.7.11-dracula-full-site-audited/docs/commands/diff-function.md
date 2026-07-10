---
title: x86decomp diff-function
description: Parser-derived command reference page for `diff-function`.
---

# `x86decomp diff-function`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp diff-function [-h] [--report REPORT] pe rva size coff symbol

positional arguments:
  pe
  rva
  size
  coff
  symbol

options:
  -h, --help       show this help message and exit
  --report REPORT
```
