---
title: x86decomp script-port
description: Parser-derived command reference page for `script-port`.
---

# `x86decomp script-port`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `audit` | `reconstruction` |
## Parser help

```text
usage: x86decomp script-port [-h] [--project PROJECT] [--actor ACTOR]
                             {audit} ...

Canonical script-port commands implemented by the current capability
subsystem.

positional arguments:
  {audit}
    audit            audit command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
