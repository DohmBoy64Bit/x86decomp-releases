---
title: x86decomp corpus-generate
description: Parser-derived command reference page for `corpus-generate`.
---

# `x86decomp corpus-generate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp corpus-generate [-h] [--cases-per-family CASES_PER_FAMILY]
                                 [--seed SEED] [--c-only] [--cpp-only]
                                 [--report REPORT]
                                 output_directory

positional arguments:
  output_directory

options:
  -h, --help            show this help message and exit
  --cases-per-family CASES_PER_FAMILY
  --seed SEED
  --c-only
  --cpp-only
  --report REPORT
```
