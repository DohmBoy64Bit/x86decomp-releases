---
title: x86decomp pattern
description: Exact v0.7.8 parser-derived reference for `x86decomp pattern`.
---


# `x86decomp pattern`

Canonical pattern commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp pattern [-h] [--project PROJECT] [--actor ACTOR]
                         {catalog,generate,match,promote,scan} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `catalog` | `usage: x86decomp pattern catalog [-h] [--output OUTPUT]` | `reconstruction` |
| `generate` | `usage: x86decomp pattern generate [-h] [--symbol-prefix SYMBOL_PREFIX] scan_report output` | `reconstruction` |
| `match` | `usage: x86decomp pattern match [-h] [--output OUTPUT] generation_report` | `reconstruction` |
| `promote` | `usage: x86decomp pattern promote [-h] --candidate CANDIDATE --report REPORT [--stage STAGE] [--output OUTPUT] [--overwrite] function_id` | `reconstruction` |
| `scan` | `usage: x86decomp pattern scan [-h] [--architecture {x86,x86_64}] [--output OUTPUT] root` | `reconstruction` |

### `x86decomp pattern catalog`

```text
usage: x86decomp pattern catalog [-h] [--output OUTPUT]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp pattern generate`

```text
usage: x86decomp pattern generate [-h] [--symbol-prefix SYMBOL_PREFIX]
                                  scan_report output
```

| Argument | Exact parser declaration |
| --- | --- |
| `scan_report` | required · parser destination: `scan_report`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--symbol-prefix` | default: `'sub'` · parser destination: `symbol_prefix`. No help text declared. |

### `x86decomp pattern match`

```text
usage: x86decomp pattern match [-h] [--output OUTPUT] generation_report
```

| Argument | Exact parser declaration |
| --- | --- |
| `generation_report` | required · parser destination: `generation_report`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp pattern promote`

```text
usage: x86decomp pattern promote [-h] --candidate CANDIDATE --report REPORT
                                 [--stage STAGE] [--output OUTPUT]
                                 [--overwrite]
                                 function_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required · parser destination: `function_id`. No help text declared. |
| `--candidate` | required · parser destination: `candidate`. No help text declared. |
| `--report` | required · parser destination: `report`. No help text declared. |
| `--stage` | default: `'pattern'` · parser destination: `stage`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp pattern scan`

```text
usage: x86decomp pattern scan [-h] [--architecture {x86,x86_64}]
                              [--output OUTPUT]
                              root
```

| Argument | Exact parser declaration |
| --- | --- |
| `root` | required · parser destination: `root`. No help text declared. |
| `--architecture` | choices: `x86`, `x86_64` · parser destination: `architecture`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
