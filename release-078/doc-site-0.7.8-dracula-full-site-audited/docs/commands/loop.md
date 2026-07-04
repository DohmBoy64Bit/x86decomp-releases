---
title: x86decomp loop
description: Exact v0.7.8 parser-derived reference for `x86decomp loop`.
---


# `x86decomp loop`

Canonical loop commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp loop [-h] [--project PROJECT] [--actor ACTOR]
                      {list,run,show} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `list` | `usage: x86decomp loop list [-h]` | `native` |
| `run` | `usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY] [--timeout TIMEOUT] [--execute] function_id source compile_command_json candidate original rva slot_size` | `native` |
| `show` | `usage: x86decomp loop show [-h] loop_id` | `native` |

### `x86decomp loop list`

```text
usage: x86decomp loop list [-h]
```

### `x86decomp loop run`

```text
usage: x86decomp loop run [-h] [--symbol SYMBOL] [--policy POLICY]
                          [--timeout TIMEOUT] [--execute]
                          function_id source compile_command_json candidate
                          original rva slot_size
```

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required · parser destination: `function_id`. No help text declared. |
| `source` | required · parser destination: `source`. No help text declared. |
| `compile_command_json` | required · parser destination: `compile_command_json`. No help text declared. |
| `candidate` | required · parser destination: `candidate`. No help text declared. |
| `original` | required · parser destination: `original`. No help text declared. |
| `rva` | required · parser destination: `rva`. No help text declared. |
| `slot_size` | required · type: `int` · parser destination: `slot_size`. No help text declared. |
| `--symbol` | parser destination: `symbol`. No help text declared. |
| `--policy` | default: `'trailing-padding'` · parser destination: `policy`. No help text declared. |
| `--timeout` | type: `int` · default: `120` · parser destination: `timeout`. No help text declared. |
| `--execute` | nargs: `0` · default: `False` · parser destination: `execute`. No help text declared. |

### `x86decomp loop show`

```text
usage: x86decomp loop show [-h] loop_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `loop_id` | required · parser destination: `loop_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
