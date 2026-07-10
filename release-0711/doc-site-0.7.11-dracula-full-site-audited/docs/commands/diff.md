---
title: x86decomp diff
description: Parser-derived command reference page for `diff`.
---

# `x86decomp diff`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `explain` | `reconstruction` |
## Parser help

```text
usage: x86decomp diff [-h] [--project PROJECT] [--actor ACTOR] {explain} ...

Canonical diff commands implemented by the current capability subsystem.

positional arguments:
  {explain}
    explain          explain command

options:
  -h, --help         show this help message and exit
  --project PROJECT  project root used by the capability implementation
                     (default: current directory)
  --actor ACTOR
```
