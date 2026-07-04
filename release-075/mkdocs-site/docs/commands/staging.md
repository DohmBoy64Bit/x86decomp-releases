---
title: x86decomp staging
description: Exact parser-derived reference for x86decomp staging in 0.7.5.
---

# `x86decomp staging`

Canonical capability group with 5 routes. Shared group options are shown in every exact usage string.

## `x86decomp staging compile-check`

usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT]

### Usage

```text
x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT]
                                       command_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `command_json` | required. No help text is declared; parser destination is `command_json`. |
| `--cwd` | declared. No help text is declared; parser destination is `cwd`. |
| `--timeout` | default: `120` · type: `int`. No help text is declared; parser destination is `timeout`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp staging generate-context`

usage: x86decomp staging generate-context [-h] output sources [sources ...]

### Usage

```text
x86decomp staging generate-context [-h] output sources [sources ...]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required. No help text is declared; parser destination is `output`. |
| `sources` | required · nargs: `+`. No help text is declared; parser destination is `sources`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp staging resolve`

usage: x86decomp staging resolve [-h] mapping_json

### Usage

```text
x86decomp staging resolve [-h] mapping_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `mapping_json` | required. No help text is declared; parser destination is `mapping_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp staging scan`

usage: x86decomp staging scan [-h] sources [sources ...]

### Usage

```text
x86decomp staging scan [-h] sources [sources ...]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `sources` | required · nargs: `+`. No help text is declared; parser destination is `sources`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp staging unresolved`

usage: x86decomp staging unresolved [-h]

### Usage

```text
x86decomp staging unresolved [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
