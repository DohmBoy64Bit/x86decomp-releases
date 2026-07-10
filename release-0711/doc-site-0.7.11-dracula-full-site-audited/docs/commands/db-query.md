---
title: x86decomp db-query
description: Parser-derived command reference page for `db-query`.
---

# `x86decomp db-query`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp db-query [-h] [--parameters-json PARAMETERS_JSON]
                          database sql

positional arguments:
  database
  sql

options:
  -h, --help            show this help message and exit
  --parameters-json PARAMETERS_JSON
```
