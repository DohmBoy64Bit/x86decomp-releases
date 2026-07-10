---
title: x86decomp match
description: Parser-derived command reference page for `match`.
---

# `x86decomp match`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `batch` | `native` |
| `compare` | `native` |
| `mismatches` | `native` |
| `report` | `native` |
## Parser help

```text
usage: x86decomp match [-h] [--project PROJECT] [--actor ACTOR]
                       {batch,compare,mismatches,report} ...

Canonical match commands implemented by the current capability subsystem.

positional arguments:
  {batch,compare,mismatches,report}
    batch               batch command
    compare             compare command
    mismatches          mismatches command
    report              report command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
