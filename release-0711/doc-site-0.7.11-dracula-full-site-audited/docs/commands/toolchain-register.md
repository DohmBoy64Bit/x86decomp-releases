---
title: x86decomp toolchain-register
description: Parser-derived command reference page for `toolchain-register`.
---

# `x86decomp toolchain-register`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp toolchain-register [-h] --executable EXECUTABLE
                                    registry toolchain_id family version

positional arguments:
  registry
  toolchain_id
  family
  version

options:
  -h, --help            show this help message and exit
  --executable EXECUTABLE
                        role=path
```
