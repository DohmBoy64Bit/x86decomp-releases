---
title: x86decomp layout-reconstruct
description: Parser-derived command reference page for `layout-reconstruct`.
---

# `x86decomp layout-reconstruct`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp layout-reconstruct [-h] [--report REPORT]
                                    pe map [objects ...]

positional arguments:
  pe
  map
  objects

options:
  -h, --help       show this help message and exit
  --report REPORT
```
