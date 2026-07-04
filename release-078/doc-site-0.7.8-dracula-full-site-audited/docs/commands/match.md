---
title: x86decomp match
description: Exact v0.7.8 parser-derived reference for `x86decomp match`.
---


# `x86decomp match`

Canonical match commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp match [-h] [--project PROJECT] [--actor ACTOR]
                       {batch,compare,mismatches,report} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `batch` | `usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}] [--pad-bytes-json PAD_BYTES_JSON] original candidates_json` | `native` |
| `compare` | `usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}] [--pad-bytes-json PAD_BYTES_JSON] [--protected-offsets-json PROTECTED_OFFSETS_JSON] original candidate` | `native` |
| `mismatches` | `usage: x86decomp match mismatches [-h] run_id` | `native` |
| `report` | `usage: x86decomp match report [-h] run_id` | `native` |

### `x86decomp match batch`

```text
usage: x86decomp match batch [-h] [--policy {exact,trailing-padding}]
                             [--pad-bytes-json PAD_BYTES_JSON]
                             original candidates_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · parser destination: `original`. No help text declared. |
| `candidates_json` | required · parser destination: `candidates_json`. No help text declared. |
| `--policy` | choices: `exact`, `trailing-padding` · default: `'trailing-padding'` · parser destination: `policy`. No help text declared. |
| `--pad-bytes-json` | parser destination: `pad_bytes_json`. No help text declared. |

### `x86decomp match compare`

```text
usage: x86decomp match compare [-h] [--policy {exact,trailing-padding}]
                               [--pad-bytes-json PAD_BYTES_JSON]
                               [--protected-offsets-json PROTECTED_OFFSETS_JSON]
                               original candidate
```

| Argument | Exact parser declaration |
| --- | --- |
| `original` | required · parser destination: `original`. No help text declared. |
| `candidate` | required · parser destination: `candidate`. No help text declared. |
| `--policy` | choices: `exact`, `trailing-padding` · default: `'trailing-padding'` · parser destination: `policy`. No help text declared. |
| `--pad-bytes-json` | parser destination: `pad_bytes_json`. No help text declared. |
| `--protected-offsets-json` | parser destination: `protected_offsets_json`. No help text declared. |

### `x86decomp match mismatches`

```text
usage: x86decomp match mismatches [-h] run_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required · parser destination: `run_id`. No help text declared. |

### `x86decomp match report`

```text
usage: x86decomp match report [-h] run_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required · parser destination: `run_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
