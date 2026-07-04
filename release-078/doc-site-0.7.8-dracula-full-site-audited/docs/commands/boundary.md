---
title: x86decomp boundary
description: Exact v0.7.8 parser-derived reference for `x86decomp boundary`.
---


# `x86decomp boundary`

Canonical boundary commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp boundary [-h] [--project PROJECT] [--actor ACTOR]
                          {audit,audit-project,export-ghidra-fixes,list,show} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `audit` | `usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA] inventory_json` | `native` |
| `audit-project` | `usage: x86decomp boundary audit-project [-h] artifact_project binary` | `native` |
| `export-ghidra-fixes` | `usage: x86decomp boundary export-ghidra-fixes [-h] output` | `native` |
| `list` | `usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]` | `native` |
| `show` | `usage: x86decomp boundary show [-h] function_id` | `native` |

### `x86decomp boundary audit`

```text
usage: x86decomp boundary audit [-h] [--text-end-rva TEXT_END_RVA]
                                inventory_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `inventory_json` | required · parser destination: `inventory_json`. No help text declared. |
| `--text-end-rva` | parser destination: `text_end_rva`. No help text declared. |

### `x86decomp boundary audit-project`

```text
usage: x86decomp boundary audit-project [-h] artifact_project binary
```

| Argument | Exact parser declaration |
| --- | --- |
| `artifact_project` | required · parser destination: `artifact_project`. No help text declared. |
| `binary` | required · parser destination: `binary`. No help text declared. |

### `x86decomp boundary export-ghidra-fixes`

```text
usage: x86decomp boundary export-ghidra-fixes [-h] output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp boundary list`

```text
usage: x86decomp boundary list [-h] [--classification CLASSIFICATION]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--classification` | parser destination: `classification`. No help text declared. |

### `x86decomp boundary show`

```text
usage: x86decomp boundary show [-h] function_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required · parser destination: `function_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
