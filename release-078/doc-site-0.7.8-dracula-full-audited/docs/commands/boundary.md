---
title: x86decomp boundary
---

# `x86decomp boundary`

Canonical boundary commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp boundary [-h] [--project PROJECT] [--actor ACTOR]
                          {audit,audit-project,export-ghidra-fixes,list,show} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `audit` | `usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA] inventory_json` |
| `audit-project` | `usage: x86decomp boundary audit-project [-h] artifact_project binary` |
| `export-ghidra-fixes` | `usage: x86decomp boundary export-ghidra-fixes [-h] output` |
| `list` | `usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]` |
| `show` | `usage: x86decomp boundary show [-h] function_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp boundary audit` | `native` |
| `x86decomp boundary audit-project` | `native` |
| `x86decomp boundary export-ghidra-fixes` | `native` |
| `x86decomp boundary list` | `native` |
| `x86decomp boundary show` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
