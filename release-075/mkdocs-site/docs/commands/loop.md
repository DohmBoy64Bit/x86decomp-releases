---
title: x86decomp loop
description: Exact parser-derived reference for x86decomp loop in 0.7.5.
---

# `x86decomp loop`

Canonical capability group with 3 routes. Shared group options are shown in every exact usage string.

## `x86decomp loop list`

usage: x86decomp loop list [-h]

### Usage

```text
x86decomp loop list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp loop run`

usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY]

### Usage

```text
x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY]
                          [--timeout TIMEOUT] [--execute]
                          function_id source compile_command_json candidate
                          original rva slot_size
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required. No help text is declared; parser destination is `function_id`. |
| `source` | required. No help text is declared; parser destination is `source`. |
| `compile_command_json` | required. No help text is declared; parser destination is `compile_command_json`. |
| `candidate` | required. No help text is declared; parser destination is `candidate`. |
| `original` | required. No help text is declared; parser destination is `original`. |
| `rva` | required. No help text is declared; parser destination is `rva`. |
| `slot_size` | required · type: `int`. No help text is declared; parser destination is `slot_size`. |
| `--symbol` | declared. No help text is declared; parser destination is `symbol`. |
| `--policy` | default: `'trailing-padding'`. No help text is declared; parser destination is `policy`. |
| `--timeout` | default: `120` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--execute` | default: `False` · nargs: `0`. No help text is declared; parser destination is `execute`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp loop show`

usage: x86decomp loop show [-h] loop_id

### Usage

```text
x86decomp loop show [-h] loop_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `loop_id` | required. No help text is declared; parser destination is `loop_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
