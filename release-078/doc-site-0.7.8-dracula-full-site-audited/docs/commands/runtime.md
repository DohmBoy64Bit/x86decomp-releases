---
title: x86decomp runtime
description: Exact v0.7.8 parser-derived reference for `x86decomp runtime`.
---


# `x86decomp runtime`

Canonical runtime commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp runtime [-h] [--project PROJECT] [--actor ACTOR]
                         {launch,map-crash,validate-image} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `launch` | `usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT] [--execute] image` | `native` |
| `map-crash` | `usage: x86decomp runtime map-crash [-h] rva` | `native` |
| `validate-image` | `usage: x86decomp runtime validate-image [-h] image` | `native` |

### `x86decomp runtime launch`

```text
usage: x86decomp runtime launch [-h] [--argument ARGUMENT] [--timeout TIMEOUT]
                                [--execute]
                                image
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |
| `--argument` | default: `[]` · parser destination: `argument`. No help text declared. |
| `--timeout` | type: `int` · default: `10` · parser destination: `timeout`. No help text declared. |
| `--execute` | nargs: `0` · default: `False` · parser destination: `execute`. No help text declared. |

### `x86decomp runtime map-crash`

```text
usage: x86decomp runtime map-crash [-h] rva
```

| Argument | Exact parser declaration |
| --- | --- |
| `rva` | required · parser destination: `rva`. No help text declared. |

### `x86decomp runtime validate-image`

```text
usage: x86decomp runtime validate-image [-h] image
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
