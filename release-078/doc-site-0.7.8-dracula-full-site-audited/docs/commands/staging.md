---
title: x86decomp staging
description: Exact v0.7.8 parser-derived reference for `x86decomp staging`.
---


# `x86decomp staging`

Canonical staging commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp staging [-h] [--project PROJECT] [--actor ACTOR]
                         {compile-check,generate-context,resolve,scan,unresolved} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compile-check` | `usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT] command_json` | `native` |
| `generate-context` | `usage: x86decomp staging generate-context [-h] output sources [sources ...]` | `native` |
| `resolve` | `usage: x86decomp staging resolve [-h] mapping_json` | `native` |
| `scan` | `usage: x86decomp staging scan [-h] sources [sources ...]` | `native` |
| `unresolved` | `usage: x86decomp staging unresolved [-h]` | `native` |

### `x86decomp staging compile-check`

```text
usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT]
                                       command_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `command_json` | required · parser destination: `command_json`. No help text declared. |
| `--cwd` | parser destination: `cwd`. No help text declared. |
| `--timeout` | type: `int` · default: `120` · parser destination: `timeout`. No help text declared. |

### `x86decomp staging generate-context`

```text
usage: x86decomp staging generate-context [-h] output sources [sources ...]
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |
| `sources` | required · nargs: `+` · parser destination: `sources`. No help text declared. |

### `x86decomp staging resolve`

```text
usage: x86decomp staging resolve [-h] mapping_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `mapping_json` | required · parser destination: `mapping_json`. No help text declared. |

### `x86decomp staging scan`

```text
usage: x86decomp staging scan [-h] sources [sources ...]
```

| Argument | Exact parser declaration |
| --- | --- |
| `sources` | required · nargs: `+` · parser destination: `sources`. No help text declared. |

### `x86decomp staging unresolved`

```text
usage: x86decomp staging unresolved [-h]
```

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
