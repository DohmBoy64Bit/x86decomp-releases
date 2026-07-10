---
title: x86decomp pe
description: Parser-derived command reference page for `pe`.
---

# `x86decomp pe`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `export-coff` | `native` |
| `export-sections` | `native` |
| `inventory` | `native` |
| `patch-apply` | `native` |
| `patch-plan` | `native` |
| `text-swap` | `native` |
## Parser help

```text
usage: x86decomp pe [-h] [--project PROJECT] [--actor ACTOR]
                    {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap} ...

Canonical pe commands implemented by the current capability subsystem.

positional arguments:
  {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap}
    export-coff         export-coff command
    export-sections     export-sections command
    inventory           inventory command
    patch-apply         patch-apply command
    patch-plan          patch-plan command
    text-swap           text-swap command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
