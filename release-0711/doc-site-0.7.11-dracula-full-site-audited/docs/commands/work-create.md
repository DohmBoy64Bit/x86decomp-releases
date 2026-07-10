---
title: x86decomp work-create
description: Parser-derived command reference page for `work-create`.
---

# `x86decomp work-create`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp work-create [-h] --validator VALIDATOR [--priority PRIORITY]
                             database function_id {matching,functional} kind
                             instructions

positional arguments:
  database
  function_id
  {matching,functional}
  kind
  instructions

options:
  -h, --help            show this help message and exit
  --validator VALIDATOR
  --priority PRIORITY
```
