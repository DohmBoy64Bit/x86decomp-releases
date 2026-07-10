---
title: x86decomp staging
description: Parser-derived command reference page for `staging`.
---

# `x86decomp staging`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `compile-check` | `native` |
| `generate-context` | `native` |
| `resolve` | `native` |
| `scan` | `native` |
| `unresolved` | `native` |
## Parser help

```text
usage: x86decomp staging [-h] [--project PROJECT] [--actor ACTOR]
                         {compile-check,generate-context,resolve,scan,unresolved} ...

Canonical staging commands implemented by the current capability subsystem.

positional arguments:
  {compile-check,generate-context,resolve,scan,unresolved}
    compile-check       compile-check command
    generate-context    generate-context command
    resolve             resolve command
    scan                scan command
    unresolved          unresolved command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
