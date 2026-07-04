---
title: x86decomp db-constraint-add
description: Exact v0.7.8 parser-derived reference for `x86decomp db-constraint-add`.
---


# `x86decomp db-constraint-add`

## Usage

```text
usage: x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID]
                                   [--confidence CONFIDENCE]
                                   database subject relation object_value
                                   provenance
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path` · parser destination: `database`. No help text declared. |
| `subject` | required · parser destination: `subject`. No help text declared. |
| `relation` | required · parser destination: `relation`. No help text declared. |
| `object_value` | required · parser destination: `object_value`. No help text declared. |
| `provenance` | required · parser destination: `provenance`. No help text declared. |
| `--evidence-id` | parser destination: `evidence_id`. No help text declared. |
| `--confidence` | type: `float` · parser destination: `confidence`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
