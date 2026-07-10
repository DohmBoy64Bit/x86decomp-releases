---
title: x86decomp release-manifest-verify
description: Parser-derived command reference page for `release-manifest-verify`.
---

# `x86decomp release-manifest-verify`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp release-manifest-verify [-h] [--manifest MANIFEST] root

positional arguments:
  root

options:
  -h, --help           show this help message and exit
  --manifest MANIFEST
```
