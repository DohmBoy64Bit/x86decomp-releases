---
title: x86decomp memory-add
description: Exact v0.7.8 parser-derived reference for `x86decomp memory-add`.
---


# `x86decomp memory-add`

## Usage

```text
usage: x86decomp memory-add [-h] --actor ACTOR --category CATEGORY
                            --summary SUMMARY [--details-json DETAILS_JSON]
                            [--evidence EVIDENCE]
                            project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--actor` | required · parser destination: `actor`. No help text declared. |
| `--category` | required · parser destination: `category`. No help text declared. |
| `--summary` | required · parser destination: `summary`. No help text declared. |
| `--details-json` | default: `'{}'` · parser destination: `details_json`. No help text declared. |
| `--evidence` | default: `[]` · parser destination: `evidence`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
