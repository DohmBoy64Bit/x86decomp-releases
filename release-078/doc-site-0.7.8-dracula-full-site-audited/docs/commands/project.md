---
title: x86decomp project
description: Exact v0.7.8 parser-derived reference for `x86decomp project`.
---


# `x86decomp project`

Canonical project commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp project [-h] [--project PROJECT] [--actor ACTOR]
                         {check,doctor-paths,explain-boundaries,export,health,init,synthesize-layout} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `check` | `usage: x86decomp project check [-h]` | `assembly` |
| `doctor-paths` | `usage: x86decomp project doctor-paths [-h] [--output OUTPUT] root` | `reconstruction` |
| `explain-boundaries` | `usage: x86decomp project explain-boundaries [-h] module_id` | `reconstruction` |
| `export` | `usage: x86decomp project export [-h] output` | `reconstruction` |
| `health` | `usage: x86decomp project health [-h] [--output OUTPUT]` | `reconstruction` |
| `init` | `usage: x86decomp project init [-h]` | `assembly` |
| `synthesize-layout` | `usage: x86decomp project synthesize-layout [-h] inventory_json` | `reconstruction` |

### `x86decomp project check`

```text
usage: x86decomp project check [-h]
```

### `x86decomp project doctor-paths`

```text
usage: x86decomp project doctor-paths [-h] [--output OUTPUT] root
```

| Argument | Exact parser declaration |
| --- | --- |
| `root` | required · parser destination: `root`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp project explain-boundaries`

```text
usage: x86decomp project explain-boundaries [-h] module_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `module_id` | required · parser destination: `module_id`. No help text declared. |

### `x86decomp project export`

```text
usage: x86decomp project export [-h] output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp project health`

```text
usage: x86decomp project health [-h] [--output OUTPUT]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp project init`

```text
usage: x86decomp project init [-h]
```

### `x86decomp project synthesize-layout`

```text
usage: x86decomp project synthesize-layout [-h] inventory_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `inventory_json` | required · parser destination: `inventory_json`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| assembly cli | `src/x86decomp/assembly/cli.py` | `6c8a227f8c1a9c48a83e1f048f6160f8740e97552fa6967dea122f42fab45f88` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
