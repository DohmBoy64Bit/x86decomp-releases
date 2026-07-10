---
title: x86decomp serve
description: Parser-derived command reference page for `serve`.
---

# `x86decomp serve`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp serve [-h] [--host HOST] [--port PORT] project

positional arguments:
  project

options:
  -h, --help   show this help message and exit
  --host HOST
  --port PORT
```
