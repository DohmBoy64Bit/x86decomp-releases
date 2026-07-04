---
title: x86decomp boundary
description: Command reference for `x86decomp boundary`.
---


# `x86decomp boundary`

Canonical boundary commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp boundary [-h] [--project PROJECT] [--actor ACTOR]
                          {audit,audit-project,export-ghidra-fixes,list,show} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `audit` | `usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA] inventory_json` | `native` |
| `audit-project` | `usage: x86decomp boundary audit-project [-h] artifact_project binary` | `native` |
| `export-ghidra-fixes` | `usage: x86decomp boundary export-ghidra-fixes [-h] output` | `native` |
| `list` | `usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]` | `native` |
| `show` | `usage: x86decomp boundary show [-h] function_id` | `native` |

### `x86decomp boundary audit`

```text
usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA]
                                inventory_json
```

| Argument | Details |
| --- | --- |
| `inventory_json` | required. |
| `--text-end-rva` | — |

### `x86decomp boundary audit-project`

```text
usage: x86decomp boundary audit-project [-h] artifact_project binary
```

| Argument | Details |
| --- | --- |
| `artifact_project` | required. |
| `binary` | required. |

### `x86decomp boundary export-ghidra-fixes`

```text
usage: x86decomp boundary export-ghidra-fixes [-h] output
```

| Argument | Details |
| --- | --- |
| `output` | required. |

### `x86decomp boundary list`

```text
usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]
```

| Argument | Details |
| --- | --- |
| `--classification` | — |

### `x86decomp boundary show`

```text
usage: x86decomp boundary show [-h] function_id
```

| Argument | Details |
| --- | --- |
| `function_id` | required. |


