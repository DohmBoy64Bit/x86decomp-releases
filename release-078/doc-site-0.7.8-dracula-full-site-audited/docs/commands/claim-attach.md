---
title: x86decomp claim-attach
description: Exact v0.7.8 parser-derived reference for `x86decomp claim-attach`.
---


# `x86decomp claim-attach`

## Usage

```text
usage: x86decomp claim-attach [-h] project claim_id evidence_id
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `claim_id` | required · parser destination: `claim_id`. No help text declared. |
| `evidence_id` | required · parser destination: `evidence_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
