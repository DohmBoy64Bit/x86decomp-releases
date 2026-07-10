---
title: x86decomp cpp-recover
description: Parser-derived command reference page for `cpp-recover`.
---

# `x86decomp cpp-recover`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp cpp-recover [-h] [--metadata-report METADATA_REPORT]
                             [--object OBJECT] [--map MAP] [--report REPORT]
                             pe

positional arguments:
  pe

options:
  -h, --help            show this help message and exit
  --metadata-report METADATA_REPORT
  --object OBJECT
  --map MAP
  --report REPORT
```
