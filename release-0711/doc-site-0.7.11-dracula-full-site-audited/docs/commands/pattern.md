---
title: x86decomp pattern
description: Parser-derived command reference page for `pattern`.
---

# `x86decomp pattern`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `catalog` | `reconstruction` |
| `generate` | `reconstruction` |
| `match` | `reconstruction` |
| `promote` | `reconstruction` |
| `scan` | `reconstruction` |
## Parser help

```text
usage: x86decomp pattern [-h] [--project PROJECT] [--actor ACTOR]
                         {catalog,generate,match,promote,scan} ...

Canonical pattern commands implemented by the current capability subsystem.

positional arguments:
  {catalog,generate,match,promote,scan}
    catalog             catalog command
    generate            generate command
    match               match command
    promote             promote command
    scan                scan command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
