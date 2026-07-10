---
title: x86decomp artifact-import
description: Parser-derived command reference page for `artifact-import`.
---

# `x86decomp artifact-import`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp artifact-import [-h] project exported_dir

positional arguments:
  project
  exported_dir

options:
  -h, --help    show this help message and exit
```
