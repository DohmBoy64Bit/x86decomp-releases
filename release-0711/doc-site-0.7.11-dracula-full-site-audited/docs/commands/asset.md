---
title: x86decomp asset
description: Parser-derived command reference page for `asset`.
---

# `x86decomp asset`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `inventory` | `reconstruction` |
## Parser help

```text
usage: x86decomp asset [-h] [--project PROJECT] [--actor ACTOR]
                       {inventory} ...

Canonical asset commands implemented by the current capability subsystem.

positional arguments:
  {inventory}
    inventory        inventory command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
