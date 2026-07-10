---
title: x86decomp project-migrate
description: Parser-derived command reference page for `project-migrate`.
---

# `x86decomp project-migrate`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp project-migrate [-h] [--dry-run] [--backup BACKUP] project

positional arguments:
  project

options:
  -h, --help       show this help message and exit
  --dry-run
  --backup BACKUP
```
