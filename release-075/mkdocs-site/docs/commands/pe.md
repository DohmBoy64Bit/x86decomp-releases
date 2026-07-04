---
title: x86decomp pe
description: Exact parser-derived reference for x86decomp pe in 0.7.5.
---

# `x86decomp pe`

Canonical capability group with 6 routes. Shared group options are shown in every exact usage string.

## `x86decomp pe export-coff`

usage: x86decomp pe export-coff [-h] [--section SECTION] image output

### Usage

```text
x86decomp pe export-coff [-h] [--section SECTION] image output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required. No help text is declared; parser destination is `image`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--section` | declared. No help text is declared; parser destination is `section`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp pe export-sections`

usage: x86decomp pe export-sections [-h] [--section SECTION] image output

### Usage

```text
x86decomp pe export-sections [-h] [--section SECTION] image output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required. No help text is declared; parser destination is `image`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--section` | declared. No help text is declared; parser destination is `section`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp pe inventory`

usage: x86decomp pe inventory [-h] image

### Usage

```text
x86decomp pe inventory [-h] image
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required. No help text is declared; parser destination is `image`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp pe patch-apply`

usage: x86decomp pe patch-apply [-h] plan_id

### Usage

```text
x86decomp pe patch-apply [-h] plan_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `plan_id` | required. No help text is declared; parser destination is `plan_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp pe patch-plan`

usage: x86decomp pe patch-plan [-h] original output operations_json

### Usage

```text
x86decomp pe patch-plan [-h] original output operations_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required. No help text is declared; parser destination is `original`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `operations_json` | required. No help text is declared; parser destination is `operations_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp pe text-swap`

usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME]

### Usage

```text
x86decomp pe text-swap [-h] [--section-name SECTION_NAME]
                              original replacement output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required. No help text is declared; parser destination is `original`. |
| `replacement` | required. No help text is declared; parser destination is `replacement`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--section-name` | default: `'.text'`. No help text is declared; parser destination is `section_name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
