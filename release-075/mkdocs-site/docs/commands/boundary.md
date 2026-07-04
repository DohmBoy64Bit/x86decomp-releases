---
title: x86decomp boundary
description: Exact parser-derived reference for x86decomp boundary in 0.7.5.
---

# `x86decomp boundary`

Canonical capability group with 5 routes. Shared group options are shown in every exact usage string.

## `x86decomp boundary audit`

usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA]

### Usage

```text
x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA]
                                inventory_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `inventory_json` | required. No help text is declared; parser destination is `inventory_json`. |
| `--text-end-rva` | declared. No help text is declared; parser destination is `text_end_rva`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp boundary audit-project`

usage: x86decomp boundary audit-project [-h] artifact_project binary

### Usage

```text
x86decomp boundary audit-project [-h] artifact_project binary
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `artifact_project` | required. No help text is declared; parser destination is `artifact_project`. |
| `binary` | required. No help text is declared; parser destination is `binary`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp boundary export-ghidra-fixes`

usage: x86decomp boundary export-ghidra-fixes [-h] output

### Usage

```text
x86decomp boundary export-ghidra-fixes [-h] output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required. No help text is declared; parser destination is `output`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp boundary list`

usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]

### Usage

```text
x86decomp boundary list [-h] [--classification CLASSIFICATION]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--classification` | declared. No help text is declared; parser destination is `classification`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp boundary show`

usage: x86decomp boundary show [-h] function_id

### Usage

```text
x86decomp boundary show [-h] function_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required. No help text is declared; parser destination is `function_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
