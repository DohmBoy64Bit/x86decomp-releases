---
title: x86decomp changeset
description: Parser-derived command reference page for `changeset`.
---

# `x86decomp changeset`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `add-operation` | `reconstruction` |
| `apply` | `governance` |
| `conflicts` | `reconstruction` |
| `create` | `reconstruction` |
| `export` | `governance` |
| `inspect` | `governance` |
| `merge` | `reconstruction` |
| `rebase` | `reconstruction` |
| `show` | `reconstruction` |
| `verify` | `reconstruction` |
## Parser help

```text
usage: x86decomp changeset [-h] [--project PROJECT] [--actor ACTOR]
                           {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify} ...

Canonical changeset commands implemented by the current capability subsystem.

positional arguments:
  {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify}
    add-operation       add-operation command
    apply               apply command
    conflicts           conflicts command
    create              create command
    export              export command
    inspect             inspect command
    merge               merge command
    rebase              rebase command
    show                show command
    verify              verify command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
