---
title: x86decomp function
---

# `x86decomp function`

Canonical function commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp function [-h] [--project PROJECT] [--actor ACTOR]
                          {classify,discover,reconcile,sort} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `classify` | `usage: x86decomp function classify [-h] [--output OUTPUT] functions_json` |
| `discover` | `usage: x86decomp function discover [-h] [--profile {prologue,ret-boundary}] [--architecture {x86,x86_64}] [--min-size MIN_SIZE] [--max-size MAX_SIZE] [--align ALIGN] [--output OUTPUT] image` |
| `reconcile` | `usage: x86decomp function reconcile [-h] [--output OUTPUT] reports [reports ...]` |
| `sort` | `usage: x86decomp function sort [-h] [--key KEY] [--output OUTPUT] functions_json` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp function classify` | `reconstruction` |
| `x86decomp function discover` | `reconstruction` |
| `x86decomp function reconcile` | `reconstruction` |
| `x86decomp function sort` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
