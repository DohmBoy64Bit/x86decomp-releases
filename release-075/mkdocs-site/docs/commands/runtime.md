---
title: x86decomp runtime
description: Exact parser-derived reference for x86decomp runtime in 0.7.5.
---

# `x86decomp runtime`

Canonical capability group with 3 routes. Shared group options are shown in every exact usage string.

## `x86decomp runtime launch`

usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT]

### Usage

```text
x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT]
                                [--execute]
                                image
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required. No help text is declared; parser destination is `image`. |
| `--argument` | default: `[]`. No help text is declared; parser destination is `argument`. |
| `--timeout` | default: `10` · type: `int`. No help text is declared; parser destination is `timeout`. |
| `--execute` | default: `False` · nargs: `0`. No help text is declared; parser destination is `execute`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp runtime map-crash`

usage: x86decomp runtime map-crash [-h] rva

### Usage

```text
x86decomp runtime map-crash [-h] rva
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `rva` | required. No help text is declared; parser destination is `rva`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp runtime validate-image`

usage: x86decomp runtime validate-image [-h] image

### Usage

```text
x86decomp runtime validate-image [-h] image
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required. No help text is declared; parser destination is `image`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
