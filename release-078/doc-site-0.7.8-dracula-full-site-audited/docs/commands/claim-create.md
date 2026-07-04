---
title: x86decomp claim-create
description: Exact v0.7.8 parser-derived reference for `x86decomp claim-create`.
---


# `x86decomp claim-create`

## Usage

```text
usage: x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE
                              --object OBJECT_VALUE [--evidence EVIDENCE]
                              [--id ID]
                              project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--subject` | required · parser destination: `subject`. No help text declared. |
| `--predicate` | required · parser destination: `predicate`. No help text declared. |
| `--object` | required · parser destination: `object_value`. No help text declared. |
| `--evidence` | default: `[]` · parser destination: `evidence`. No help text declared. |
| `--id` | parser destination: `id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
