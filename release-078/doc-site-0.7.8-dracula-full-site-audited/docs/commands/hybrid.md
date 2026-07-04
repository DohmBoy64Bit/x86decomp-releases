---
title: x86decomp hybrid
description: Exact v0.7.8 parser-derived reference for `x86decomp hybrid`.
---


# `x86decomp hybrid`

Canonical hybrid commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp hybrid [-h] [--project PROJECT] [--actor ACTOR]
                        {compose,generate,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compose` | `usage: x86decomp hybrid compose [-h] run_id output` | `native` |
| `generate` | `usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}] [--asm-format {bytes,annotated,mnemonic}] [--image-base IMAGE_BASE] [--assembler-command-json ASSEMBLER_COMMAND_JSON] [--symbol-map SYMBOL_MAP] [--overwrite] source_project output` | `assembly` |
| `verify` | `usage: x86decomp hybrid verify [-h] composition_id` | `native` |

### `x86decomp hybrid compose`

```text
usage: x86decomp hybrid compose [-h] run_id output
```

| Argument | Exact parser declaration |
| --- | --- |
| `run_id` | required · parser destination: `run_id`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp hybrid generate`

```text
usage: x86decomp hybrid generate [-h] [--architecture {x86,x86_64}]
                                 [--asm-format {bytes,annotated,mnemonic}]
                                 [--image-base IMAGE_BASE]
                                 [--assembler-command-json ASSEMBLER_COMMAND_JSON]
                                 [--symbol-map SYMBOL_MAP] [--overwrite]
                                 source_project output
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_project` | required · parser destination: `source_project`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--asm-format` | choices: `bytes`, `annotated`, `mnemonic` · default: `'bytes'` · parser destination: `asm_format`. No help text declared. |
| `--image-base` | type: `_int` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--assembler-command-json` | parser destination: `assembler_command_json`. No help text declared. |
| `--symbol-map` | parser destination: `symbol_map`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp hybrid verify`

```text
usage: x86decomp hybrid verify [-h] composition_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `composition_id` | required · parser destination: `composition_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| assembly cli | `src/x86decomp/assembly/cli.py` | `6c8a227f8c1a9c48a83e1f048f6160f8740e97552fa6967dea122f42fab45f88` |
| native cli | `src/x86decomp/native/cli.py` | `13ff944cc50ff6ed433c32975a8edcd6318b4d4fd4c6c30580c27329a951dbf2` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
