---
title: x86decomp pipeline-recover
description: Exact v0.7.8 parser-derived reference for `x86decomp pipeline-recover`.
---


# `x86decomp pipeline-recover`

## Usage

```text
usage: x86decomp pipeline-recover [-h] [--pipeline-id PIPELINE_ID]
                                  [--stale-seconds STALE_SECONDS]
                                  project
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `project` | required · type: `_path` · parser destination: `project`. No help text declared. |
| `--pipeline-id` | parser destination: `pipeline_id`. No help text declared. |
| `--stale-seconds` | type: `int` · default: `600` · parser destination: `stale_seconds`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
