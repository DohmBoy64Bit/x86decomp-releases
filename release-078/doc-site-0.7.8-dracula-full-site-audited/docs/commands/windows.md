---
title: x86decomp windows
description: Command reference for `x86decomp windows`.
---


# `x86decomp windows`

Canonical windows commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp windows [-h] [--project PROJECT] [--actor ACTOR]
                         {discover-ghidra,doctor,response-file} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `discover-ghidra` | `usage: x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME] [--platform-name PLATFORM_NAME]` | `native` |
| `doctor` | `usage: x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]` | `native` |
| `response-file` | `usage: x86decomp windows response-file [-h] output arguments_json` | `native` |

### `x86decomp windows discover-ghidra`

```text
usage: x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME]
                                         [--platform-name PLATFORM_NAME]
```

| Argument | Details |
| --- | --- |
| `--ghidra-home` | — |
| `--platform-name` | — |

### `x86decomp windows doctor`

```text
usage: x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]
```

| Argument | Details |
| --- | --- |
| `--ghidra-home` | — |

### `x86decomp windows response-file`

```text
usage: x86decomp windows response-file [-h] output arguments_json
```

| Argument | Details |
| --- | --- |
| `output` | required. |
| `arguments_json` | required. |


