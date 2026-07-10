---
title: x86decomp linker-plan
description: Parser-derived command reference page for `linker-plan`.
---

# `x86decomp linker-plan`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER]
                             [--output-image OUTPUT_IMAGE] [--report REPORT]
                             [--write-relink-manifest WRITE_RELINK_MANIFEST]
                             pe map objects [objects ...]

positional arguments:
  pe
  map
  objects

options:
  -h, --help            show this help message and exit
  --library LIBRARY
  --linker LINKER
  --output-image OUTPUT_IMAGE
  --report REPORT
  --write-relink-manifest WRITE_RELINK_MANIFEST
```
