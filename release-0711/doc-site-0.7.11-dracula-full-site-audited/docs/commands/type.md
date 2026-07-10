---
title: x86decomp type
description: Parser-derived command reference page for `type`.
---

# `x86decomp type`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `propagate` | `reconstruction` |
## Parser help

```text
usage: x86decomp type [-h] [--project PROJECT] [--actor ACTOR] {propagate} ...

Canonical type commands implemented by the current capability subsystem.

positional arguments:
  {propagate}
    propagate        emit a type-propagation plan only; no source edits are
                     performed

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
