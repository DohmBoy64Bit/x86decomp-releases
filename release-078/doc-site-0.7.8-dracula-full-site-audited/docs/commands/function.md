---
title: x86decomp function
description: Exact v0.7.8 parser-derived reference for `x86decomp function`.
---


# `x86decomp function`

Canonical function commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp function [-h] [--project PROJECT] [--actor ACTOR]
                          {classify,discover,reconcile,sort} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `classify` | `usage: x86decomp function classify [-h] [--output OUTPUT] functions_json` | `reconstruction` |
| `discover` | `usage: x86decomp function discover [-h] [--profile {prologue,ret-boundary}] [--architecture {x86,x86_64}] [--min-size MIN_SIZE] [--max-size MAX_SIZE] [--align ALIGN] [--output OUTPUT] image` | `reconstruction` |
| `reconcile` | `usage: x86decomp function reconcile [-h] [--output OUTPUT] reports [reports ...]` | `reconstruction` |
| `sort` | `usage: x86decomp function sort [-h] [--key KEY] [--output OUTPUT] functions_json` | `reconstruction` |

### `x86decomp function classify`

```text
usage: x86decomp function classify [-h] [--output OUTPUT] functions_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `functions_json` | required · parser destination: `functions_json`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp function discover`

```text
usage: x86decomp function discover [-h] [--profile {prologue,ret-boundary}]
                                   [--architecture {x86,x86_64}]
                                   [--min-size MIN_SIZE] [--max-size MAX_SIZE]
                                   [--align ALIGN] [--output OUTPUT]
                                   image
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |
| `--profile` | choices: `prologue`, `ret-boundary` · default: `'prologue'` · parser destination: `profile`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · default: `'x86'` · parser destination: `architecture`. No help text declared. |
| `--min-size` | type: `int` · default: `1` · parser destination: `min_size`. No help text declared. |
| `--max-size` | type: `int` · default: `1048576` · parser destination: `max_size`. No help text declared. |
| `--align` | type: `int` · default: `1` · parser destination: `align`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp function reconcile`

```text
usage: x86decomp function reconcile [-h] [--output OUTPUT]
                                    reports [reports ...]
```

| Argument | Exact parser declaration |
| --- | --- |
| `reports` | required · nargs: `+` · parser destination: `reports`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp function sort`

```text
usage: x86decomp function sort [-h] [--key KEY] [--output OUTPUT]
                               functions_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `functions_json` | required · parser destination: `functions_json`. No help text declared. |
| `--key` | default: `'rva'` · parser destination: `key`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
