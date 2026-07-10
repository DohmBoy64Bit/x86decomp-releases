---
title: x86decomp playability
description: Parser-derived command reference page for `playability`.
---

# `x86decomp playability`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `smoke-plan` | `reconstruction` |
## Parser help

```text
usage: x86decomp playability [-h] [--project PROJECT] [--actor ACTOR]
                             {smoke-plan} ...

Canonical playability commands implemented by the current capability
subsystem.

positional arguments:
  {smoke-plan}
    smoke-plan       smoke-plan command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
