---
title: x86decomp capsule
description: Parser-derived command reference page for `capsule`.
---

# `x86decomp capsule`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `create` | `reconstruction` |
| `inspect` | `reconstruction` |
| `reproduce` | `reconstruction` |
| `verify` | `reconstruction` |
## Parser help

```text
usage: x86decomp capsule [-h] [--project PROJECT] [--actor ACTOR]
                         {create,inspect,reproduce,verify} ...

Canonical capsule commands implemented by the current capability subsystem.

positional arguments:
  {create,inspect,reproduce,verify}
    create              create command
    inspect             inspect command
    reproduce           reproduce command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
