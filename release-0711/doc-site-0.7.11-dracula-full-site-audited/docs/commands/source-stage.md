---
title: x86decomp source-stage
description: Parser-derived command reference page for `source-stage`.
---

# `x86decomp source-stage`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `classify` | `reconstruction` |
## Parser help

```text
usage: x86decomp source-stage [-h] [--project PROJECT] [--actor ACTOR]
                              {classify} ...

Canonical source-stage commands implemented by the current capability
subsystem.

positional arguments:
  {classify}
    classify         classify command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
