---
title: x86decomp match
description: Exact parser-derived reference for x86decomp match in 0.7.5.
---

# `x86decomp match`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp match batch`

usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}]

### Usage

```text
x86decomp match batch [-h] [--policy {exact,trailing-padding}]
                             [--pad-bytes-json PAD_BYTES_JSON]
                             original candidates_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required. No help text is declared; parser destination is `original`. |
| `candidates_json` | required. No help text is declared; parser destination is `candidates_json`. |
| `--policy` | default: `'trailing-padding'` · choices: `exact`, `trailing-padding`. No help text is declared; parser destination is `policy`. |
| `--pad-bytes-json` | declared. No help text is declared; parser destination is `pad_bytes_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp match compare`

usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}]

### Usage

```text
x86decomp match compare [-h] [--policy {exact,trailing-padding}]
                               [--pad-bytes-json PAD_BYTES_JSON]
                               [--protected-offsets-json PROTECTED_OFFSETS_JSON]
                               original candidate
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required. No help text is declared; parser destination is `original`. |
| `candidate` | required. No help text is declared; parser destination is `candidate`. |
| `--policy` | default: `'trailing-padding'` · choices: `exact`, `trailing-padding`. No help text is declared; parser destination is `policy`. |
| `--pad-bytes-json` | declared. No help text is declared; parser destination is `pad_bytes_json`. |
| `--protected-offsets-json` | declared. No help text is declared; parser destination is `protected_offsets_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp match mismatches`

usage: x86decomp match mismatches [-h] run_id

### Usage

```text
x86decomp match mismatches [-h] run_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required. No help text is declared; parser destination is `run_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp match report`

usage: x86decomp match report [-h] run_id

### Usage

```text
x86decomp match report [-h] run_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required. No help text is declared; parser destination is `run_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
