---
title: x86decomp abi
description: Exact v0.7.8 parser-derived reference for `x86decomp abi`.
---


# `x86decomp abi`

Canonical abi commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp abi [-h] [--project PROJECT] [--actor ACTOR]
                     {compare,export,recover,shim,show,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compare` | `usage: x86decomp abi compare [-h] left_id right_id` | `reconstruction` |
| `export` | `usage: x86decomp abi export [-h] contract_id output` | `reconstruction` |
| `recover` | `usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON subject_kind subject_id architecture contract_json` | `reconstruction` |
| `shim` | `usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path` | `reconstruction` |
| `show` | `usage: x86decomp abi show [-h] contract_id` | `reconstruction` |
| `verify` | `usage: x86decomp abi verify [-h] contract_id` | `reconstruction` |

### `x86decomp abi compare`

```text
usage: x86decomp abi compare [-h] left_id right_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `left_id` | required · parser destination: `left_id`. No help text declared. |
| `right_id` | required · parser destination: `right_id`. No help text declared. |

### `x86decomp abi export`

```text
usage: x86decomp abi export [-h] contract_id output
```

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required · parser destination: `contract_id`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp abi recover`

```text
usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON
                             subject_kind subject_id architecture
                             contract_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required · parser destination: `subject_kind`. No help text declared. |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `architecture` | required · parser destination: `architecture`. No help text declared. |
| `contract_json` | required · parser destination: `contract_json`. No help text declared. |
| `--evidence-json` | required · parser destination: `evidence_json`. No help text declared. |

### `x86decomp abi shim`

```text
usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path
```

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required · parser destination: `contract_id`. No help text declared. |
| `source_path` | required · parser destination: `source_path`. No help text declared. |
| `--kind` | default: `'wrapped'` · parser destination: `kind`. No help text declared. |

### `x86decomp abi show`

```text
usage: x86decomp abi show [-h] contract_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required · parser destination: `contract_id`. No help text declared. |

### `x86decomp abi verify`

```text
usage: x86decomp abi verify [-h] contract_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `contract_id` | required · parser destination: `contract_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
