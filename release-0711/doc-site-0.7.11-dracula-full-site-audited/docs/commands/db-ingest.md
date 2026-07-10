---
title: x86decomp db-ingest
description: Parser-derived command reference page for `db-ingest`.
---

# `x86decomp db-ingest`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp db-ingest [-h] [--image-base IMAGE_BASE] database artifact

positional arguments:
  database
  artifact

options:
  -h, --help            show this help message and exit
  --image-base IMAGE_BASE
```
