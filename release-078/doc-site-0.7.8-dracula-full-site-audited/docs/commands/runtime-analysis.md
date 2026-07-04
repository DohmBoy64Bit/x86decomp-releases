---
title: x86decomp runtime-analysis
description: Exact v0.7.8 parser-derived reference for `x86decomp runtime-analysis`.
---


# `x86decomp runtime-analysis`

Canonical runtime-analysis commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp runtime-analysis [-h] [--project PROJECT] [--actor ACTOR]
                                  {identify,match-library,quarantine} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `identify` | `usage: x86decomp runtime-analysis identify [-h] [--output OUTPUT]` | `reconstruction` |
| `match-library` | `usage: x86decomp runtime-analysis match-library [-h] [--output OUTPUT] library_inventory` | `reconstruction` |
| `quarantine` | `usage: x86decomp runtime-analysis quarantine [-h] [--output OUTPUT] identification_report` | `reconstruction` |

### `x86decomp runtime-analysis identify`

```text
usage: x86decomp runtime-analysis identify [-h] [--output OUTPUT]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp runtime-analysis match-library`

```text
usage: x86decomp runtime-analysis match-library [-h] [--output OUTPUT]
                                                library_inventory
```

| Argument | Exact parser declaration |
| --- | --- |
| `library_inventory` | required · parser destination: `library_inventory`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp runtime-analysis quarantine`

```text
usage: x86decomp runtime-analysis quarantine [-h] [--output OUTPUT]
                                             identification_report
```

| Argument | Exact parser declaration |
| --- | --- |
| `identification_report` | required · parser destination: `identification_report`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
