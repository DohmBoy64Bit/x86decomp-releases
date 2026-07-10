---
title: x86decomp mod
description: Parser-derived command reference page for `mod`.
---

# `x86decomp mod`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `branch-init` | `reconstruction` |
## Parser help

```text
usage: x86decomp mod [-h] [--project PROJECT] [--actor ACTOR]
                     {branch-init} ...

Canonical mod commands implemented by the current capability subsystem.

positional arguments:
  {branch-init}
    branch-init      branch-init command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
