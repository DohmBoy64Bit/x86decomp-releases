---
title: x86decomp windows
description: Exact v0.7.8 parser-derived reference for `x86decomp windows`.
---


# `x86decomp windows`

Canonical windows commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp windows [-h] [--project PROJECT] [--actor ACTOR]
                         {discover-ghidra,doctor,response-file} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `--ghidra-home` | parser destination: `ghidra_home`. No help text declared. |
| `--platform-name` | parser destination: `platform_name`. No help text declared. |

### `x86decomp windows doctor`

```text
usage: x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--ghidra-home` | parser destination: `ghidra_home`. No help text declared. |

### `x86decomp windows response-file`

```text
usage: x86decomp windows response-file [-h] output arguments_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |
| `arguments_json` | required · parser destination: `arguments_json`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
