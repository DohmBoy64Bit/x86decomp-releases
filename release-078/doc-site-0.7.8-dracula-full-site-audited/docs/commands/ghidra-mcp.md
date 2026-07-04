---
title: x86decomp ghidra-mcp
description: Command reference for `x86decomp ghidra-mcp`.
---


# `x86decomp ghidra-mcp`

Canonical ghidra-mcp commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp ghidra-mcp [-h] [--project PROJECT] [--actor ACTOR]
                            {batch-decompile,decompile,functions,probe,sync-names} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `batch-decompile` | `usage: x86decomp ghidra-mcp batch-decompile [-h] [--timeout TIMEOUT] url addresses output` | `reconstruction` |
| `decompile` | `usage: x86decomp ghidra-mcp decompile [-h] [--timeout TIMEOUT] [--output OUTPUT] url address` | `reconstruction` |
| `functions` | `usage: x86decomp ghidra-mcp functions [-h] [--timeout TIMEOUT] [--output OUTPUT] url` | `reconstruction` |
| `probe` | `usage: x86decomp ghidra-mcp probe [-h] [--timeout TIMEOUT] [--output OUTPUT] url` | `reconstruction` |
| `sync-names` | `usage: x86decomp ghidra-mcp sync-names [-h] [--output OUTPUT] names_json` | `reconstruction` |

### `x86decomp ghidra-mcp batch-decompile`

```text
usage: x86decomp ghidra-mcp batch-decompile [-h] [--timeout TIMEOUT]
                                            url addresses output
```

| Argument | Details |
| --- | --- |
| `url` | required. |
| `addresses` | required. |
| `output` | required. |
| `--timeout` | type: `float` · default: `60.0`. |

### `x86decomp ghidra-mcp decompile`

```text
usage: x86decomp ghidra-mcp decompile [-h] [--timeout TIMEOUT]
                                      [--output OUTPUT]
                                      url address
```

| Argument | Details |
| --- | --- |
| `url` | required. |
| `address` | required. |
| `--timeout` | type: `float` · default: `60.0`. |
| `--output` | — |

### `x86decomp ghidra-mcp functions`

```text
usage: x86decomp ghidra-mcp functions [-h] [--timeout TIMEOUT]
                                      [--output OUTPUT]
                                      url
```

| Argument | Details |
| --- | --- |
| `url` | required. |
| `--timeout` | type: `float` · default: `30.0`. |
| `--output` | — |

### `x86decomp ghidra-mcp probe`

```text
usage: x86decomp ghidra-mcp probe [-h] [--timeout TIMEOUT] [--output OUTPUT]
                                  url
```

| Argument | Details |
| --- | --- |
| `url` | required. |
| `--timeout` | type: `float` · default: `5.0`. |
| `--output` | — |

### `x86decomp ghidra-mcp sync-names`

```text
usage: x86decomp ghidra-mcp sync-names [-h] [--output OUTPUT] names_json
```

| Argument | Details |
| --- | --- |
| `names_json` | required. |
| `--output` | — |


