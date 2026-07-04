---
title: x86decomp evidence-add
description: Exact v0.7.8 parser-derived reference for `x86decomp evidence-add`.
---


# `x86decomp evidence-add`

## Usage

```text
usage: x86decomp evidence-add [-h]
                              --kind {binary_bytes,static_analysis,dynamic_trace,compiler_output,debug_symbol,external_document,human_review}
                              --source SOURCE --locator LOCATOR
                              --assertion ASSERTION
                              --independent-group INDEPENDENT_GROUP
                              [--file FILE] [--id ID]
                              project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--kind` | required · choices: `binary_bytes`, `static_analysis`, `dynamic_trace`, `compiler_output`, `debug_symbol`, `external_document`, `human_review` · parser destination: `kind`. No help text declared. |
| `--source` | required · parser destination: `source`. No help text declared. |
| `--locator` | required · parser destination: `locator`. No help text declared. |
| `--assertion` | required · parser destination: `assertion`. No help text declared. |
| `--independent-group` | required · parser destination: `independent_group`. No help text declared. |
| `--file` | type: `_path` · parser destination: `file`. No help text declared. |
| `--id` | parser destination: `id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
