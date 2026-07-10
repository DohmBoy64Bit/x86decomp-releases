---
title: x86decomp consensus
description: Parser-derived command reference page for `consensus`.
---

# `x86decomp consensus`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `conflicts` | `governance` |
| `explain` | `governance` |
| `record` | `governance` |
| `resolve` | `governance` |
| `scan` | `governance` |
## Parser help

```text
usage: x86decomp consensus [-h] [--project PROJECT] [--actor ACTOR]
                           {conflicts,explain,record,resolve,scan} ...

Canonical consensus commands implemented by the current capability subsystem.

positional arguments:
  {conflicts,explain,record,resolve,scan}
    conflicts           conflicts command
    explain             explain command
    record              record command
    resolve             resolve command
    scan                scan command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
