---
title: x86decomp project
---

# `x86decomp project`

Canonical project commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp project [-h] [--project PROJECT] [--actor ACTOR]
                         {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `check` | `usage: x86decomp project check [-h]` |
| `doctor-paths` | `usage: x86decomp project doctor-paths [-h] [--output OUTPUT] root` |
| `explain-boundaries` | `usage: x86decomp project explain-boundaries [-h] module_id` |
| `export` | `usage: x86decomp project export [-h] output` |
| `health` | `usage: x86decomp project health [-h] [--output OUTPUT]` |
| `init` | `usage: x86decomp project init [-h]` |
| `synthesize-layout` | `usage: x86decomp project synthesize-layout [-h] inventory_json` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp project check` | `assembly` |
| `x86decomp project doctor-paths` | `reconstruction` |
| `x86decomp project explain-boundaries` | `reconstruction` |
| `x86decomp project export` | `reconstruction` |
| `x86decomp project health` | `reconstruction` |
| `x86decomp project init` | `assembly` |
| `x86decomp project synthesize-layout` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
