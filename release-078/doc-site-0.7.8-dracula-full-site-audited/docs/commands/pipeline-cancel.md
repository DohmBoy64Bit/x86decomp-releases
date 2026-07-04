---
title: x86decomp pipeline-cancel
description: Exact v0.7.8 parser-derived reference for `x86decomp pipeline-cancel`.
---


# `x86decomp pipeline-cancel`

## Usage

```text
usage: x86decomp pipeline-cancel [-h] [--stage-id STAGE_ID]
                                 project pipeline_id
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `pipeline_id` | required · parser destination: `pipeline_id`. No help text declared. |
| `--stage-id` | parser destination: `stage_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
