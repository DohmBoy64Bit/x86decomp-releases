---
title: x86decomp pattern
---

# `x86decomp pattern`

Canonical pattern commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp pattern [-h] [--project PROJECT] [--actor ACTOR]
                         {catalog,generate,match,promote,scan} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `catalog` | `usage: x86decomp pattern catalog [-h] [--output OUTPUT]` |
| `generate` | `usage: x86decomp pattern generate [-h] [--symbol-prefix SYMBOL_PREFIX] scan_report output` |
| `match` | `usage: x86decomp pattern match [-h] [--output OUTPUT] generation_report` |
| `promote` | `usage: x86decomp pattern promote [-h] --candidate CANDIDATE --report REPORT [--stage STAGE] [--output OUTPUT] [--overwrite] function_id` |
| `scan` | `usage: x86decomp pattern scan [-h] [--architecture {x86,x86_64}] [--output OUTPUT] root` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp pattern catalog` | `reconstruction` |
| `x86decomp pattern generate` | `reconstruction` |
| `x86decomp pattern match` | `reconstruction` |
| `x86decomp pattern promote` | `reconstruction` |
| `x86decomp pattern scan` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
