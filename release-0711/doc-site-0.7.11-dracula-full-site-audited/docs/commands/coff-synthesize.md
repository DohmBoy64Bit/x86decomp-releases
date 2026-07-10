---
title: x86decomp coff-synthesize
description: Parser-derived command reference page for `coff-synthesize`.
---

# `x86decomp coff-synthesize`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp coff-synthesize [-h] [--architecture {x86,x86_64}]
                                 [--relocations RELOCATIONS]
                                 code symbol output

positional arguments:
  code
  symbol
  output

options:
  -h, --help            show this help message and exit
  --architecture {x86,x86_64}
  --relocations RELOCATIONS
```
