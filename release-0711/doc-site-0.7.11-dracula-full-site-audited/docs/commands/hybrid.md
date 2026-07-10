---
title: x86decomp hybrid
description: Parser-derived command reference page for `hybrid`.
---

# `x86decomp hybrid`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `compose` | `native` |
| `generate` | `assembly` |
| `verify` | `native` |
## Parser help

```text
usage: x86decomp hybrid [-h] [--project PROJECT] [--actor ACTOR]
                        {compose,generate,verify} ...

Canonical hybrid commands implemented by the current capability subsystem.

positional arguments:
  {compose,generate,verify}
    compose             compose command
    generate            generate command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
