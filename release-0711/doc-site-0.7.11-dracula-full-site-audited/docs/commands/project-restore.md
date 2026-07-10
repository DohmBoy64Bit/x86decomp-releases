---
title: x86decomp project-restore
description: Parser-derived command reference page for `project-restore`.
---

# `x86decomp project-restore`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp project-restore [-h] archive destination

positional arguments:
  archive
  destination

options:
  -h, --help   show this help message and exit
```
