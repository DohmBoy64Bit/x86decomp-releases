---
title: x86decomp windows
description: Exact parser-derived reference for x86decomp windows in 0.7.5.
---

# `x86decomp windows`

Canonical capability group with 3 routes. Shared group options are shown in every exact usage string.

## `x86decomp windows discover-ghidra`

usage: x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME]

### Usage

```text
x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME]
                                         [--platform-name PLATFORM_NAME]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--ghidra-home` | declared. No help text is declared; parser destination is `ghidra_home`. |
| `--platform-name` | declared. No help text is declared; parser destination is `platform_name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp windows doctor`

usage: x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]

### Usage

```text
x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--ghidra-home` | declared. No help text is declared; parser destination is `ghidra_home`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
## `x86decomp windows response-file`

usage: x86decomp windows response-file [-h] output arguments_json

### Usage

```text
x86decomp windows response-file [-h] output arguments_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required. No help text is declared; parser destination is `output`. |
| `arguments_json` | required. No help text is declared; parser destination is `arguments_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `native` | `src/x86decomp/native/cli.py` · `9d7246998171e0b7e1d5940cc9225c3474b0c7f898951042a1f080d71a687ba2` |
