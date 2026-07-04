---
title: x86decomp ghidra-mcp
description: Exact v0.7.8 parser-derived reference for `x86decomp ghidra-mcp`.
---


# `x86decomp ghidra-mcp`

Canonical ghidra-mcp commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp ghidra-mcp [-h] [--project PROJECT] [--actor ACTOR]
                            {batch-decompile,decompile,functions,probe,sync-names} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `url` | required · parser destination: `url`. No help text declared. |
| `addresses` | required · parser destination: `addresses`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--timeout` | type: `float` · default: `60.0` · parser destination: `timeout`. No help text declared. |

### `x86decomp ghidra-mcp decompile`

```text
usage: x86decomp ghidra-mcp decompile [-h] [--timeout TIMEOUT]
                                      [--output OUTPUT]
                                      url address
```

| Argument | Exact parser declaration |
| --- | --- |
| `url` | required · parser destination: `url`. No help text declared. |
| `address` | required · parser destination: `address`. No help text declared. |
| `--timeout` | type: `float` · default: `60.0` · parser destination: `timeout`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp ghidra-mcp functions`

```text
usage: x86decomp ghidra-mcp functions [-h] [--timeout TIMEOUT]
                                      [--output OUTPUT]
                                      url
```

| Argument | Exact parser declaration |
| --- | --- |
| `url` | required · parser destination: `url`. No help text declared. |
| `--timeout` | type: `float` · default: `30.0` · parser destination: `timeout`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp ghidra-mcp probe`

```text
usage: x86decomp ghidra-mcp probe [-h] [--timeout TIMEOUT] [--output OUTPUT]
                                  url
```

| Argument | Exact parser declaration |
| --- | --- |
| `url` | required · parser destination: `url`. No help text declared. |
| `--timeout` | type: `float` · default: `5.0` · parser destination: `timeout`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp ghidra-mcp sync-names`

```text
usage: x86decomp ghidra-mcp sync-names [-h] [--output OUTPUT] names_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `names_json` | required · parser destination: `names_json`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
