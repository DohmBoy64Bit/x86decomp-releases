---
title: x86decomp work-claim
description: Parser-derived command reference page for `work-claim`.
---

# `x86decomp work-claim`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp work-claim [-h] database task_id assignee

positional arguments:
  database
  task_id
  assignee

options:
  -h, --help  show this help message and exit
```
