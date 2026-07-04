---
title: x86decomp dynamic-validate
description: Exact v0.7.8 parser-derived reference for `x86decomp dynamic-validate`.
---


# `x86decomp dynamic-validate`

## Usage

```text
usage: x86decomp dynamic-validate [-h] [--target-base TARGET_BASE]
                                  [--candidate-base CANDIDATE_BASE]
                                  [--report REPORT]
                                  target candidate harness
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `target` | required · type: `_path` · parser destination: `target`. No help text declared. |
| `candidate` | required · type: `_path` · parser destination: `candidate`. No help text declared. |
| `harness` | required · type: `_path` · parser destination: `harness`. No help text declared. |
| `--target-base` | type: `_int` · parser destination: `target_base`. No help text declared. |
| `--candidate-base` | type: `_int` · parser destination: `candidate_base`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
