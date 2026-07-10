---
title: x86decomp lib-inspect
description: Parser-derived command reference page for `lib-inspect`.
---

# `x86decomp lib-inspect`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp lib-inspect [-h] library

positional arguments:
  library

options:
  -h, --help  show this help message and exit
```
