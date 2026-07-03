---
title: x86decomp db-constraint-add
description: Exact parser-derived reference for x86decomp db-constraint-add in 0.7.5.
---

# `x86decomp db-constraint-add`

## `x86decomp db-constraint-add`

usage: x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID]

### Usage

```text
x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID]
                                   [--confidence CONFIDENCE]
                                   database subject relation object_value
                                   provenance
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `database` | required · type: `_path`. No help text is declared; parser destination is `database`. |
| `subject` | required. No help text is declared; parser destination is `subject`. |
| `relation` | required. No help text is declared; parser destination is `relation`. |
| `object_value` | required. No help text is declared; parser destination is `object_value`. |
| `provenance` | required. No help text is declared; parser destination is `provenance`. |
| `--evidence-id` | declared. No help text is declared; parser destination is `evidence_id`. |
| `--confidence` | type: `float`. No help text is declared; parser destination is `confidence`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
