---
title: x86decomp work-validate
description: Parser-derived command reference page for `work-validate`.
---

# `x86decomp work-validate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp work-validate [-h] [--passed]
                               database task_id validator report_path

positional arguments:
  database
  task_id
  validator
  report_path

options:
  -h, --help   show this help message and exit
  --passed
```
