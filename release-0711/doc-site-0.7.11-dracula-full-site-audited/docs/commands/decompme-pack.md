---
title: x86decomp decompme-pack
description: Parser-derived command reference page for `decompme-pack`.
---

# `x86decomp decompme-pack`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp decompme-pack [-h] [--overwrite] artifact_dir output_dir

positional arguments:
  artifact_dir
  output_dir

options:
  -h, --help    show this help message and exit
  --overwrite
```
