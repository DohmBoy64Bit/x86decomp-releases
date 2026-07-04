---
title: x86decomp match
---

# `x86decomp match`

Canonical match commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp match [-h] [--project PROJECT] [--actor ACTOR]
                       {batch,compare,mismatches,report} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `batch` | `usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}] [--pad-bytes-json PAD_BYTES_JSON] original candidates_json` |
| `compare` | `usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}] [--pad-bytes-json PAD_BYTES_JSON] [--protected-offsets-json PROTECTED_OFFSETS_JSON] original candidate` |
| `mismatches` | `usage: x86decomp match mismatches [-h] run_id` |
| `report` | `usage: x86decomp match report [-h] run_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp match batch` | `native` |
| `x86decomp match compare` | `native` |
| `x86decomp match mismatches` | `native` |
| `x86decomp match report` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
