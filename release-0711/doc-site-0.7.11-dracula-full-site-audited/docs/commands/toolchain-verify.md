---
title: x86decomp toolchain-verify
description: Parser-derived command reference page for `toolchain-verify`.
---

# `x86decomp toolchain-verify`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp toolchain-verify [-h] registry toolchain_id

positional arguments:
  registry
  toolchain_id

options:
  -h, --help    show this help message and exit
```
