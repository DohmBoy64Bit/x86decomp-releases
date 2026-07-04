---
title: x86decomp source-map
description: Exact v0.7.8 parser-derived reference for `x86decomp source-map`.
---


# `x86decomp source-map`

Canonical source-map commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source-map [-h] [--project PROJECT] [--actor ACTOR]
                            {annotate,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `annotate` | `usage: x86decomp source-map annotate [-h] [--binary BINARY] [--report REPORT] source_root` | `reconstruction` |
| `verify` | `usage: x86decomp source-map verify [-h] [--report REPORT] source_root` | `reconstruction` |

### `x86decomp source-map annotate`

```text
usage: x86decomp source-map annotate [-h] [--binary BINARY] [--report REPORT]
                                     source_root
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_root` | required · parser destination: `source_root`. No help text declared. |
| `--binary` | default: `'GAME'` · parser destination: `binary`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |

### `x86decomp source-map verify`

```text
usage: x86decomp source-map verify [-h] [--report REPORT] source_root
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_root` | required · parser destination: `source_root`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
