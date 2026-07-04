---
title: x86decomp linker-plan
description: Exact v0.7.8 parser-derived reference for `x86decomp linker-plan`.
---


# `x86decomp linker-plan`

## Usage

```text
usage: x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER]
                             [--output-image OUTPUT_IMAGE] [--report REPORT]
                             [--write-relink-manifest WRITE_RELINK_MANIFEST]
                             pe map objects [objects ...]
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path` · parser destination: `pe`. No help text declared. |
| `map` | required · type: `_path` · parser destination: `map`. No help text declared. |
| `objects` | required · nargs: `+` · type: `_path` · parser destination: `objects`. No help text declared. |
| `--library` | type: `_path` · default: `[]` · parser destination: `library`. No help text declared. |
| `--linker` | default: `'lld-link'` · parser destination: `linker`. No help text declared. |
| `--output-image` | default: `'build/reconstructed.exe'` · parser destination: `output_image`. No help text declared. |
| `--report` | type: `_path` · parser destination: `report`. No help text declared. |
| `--write-relink-manifest` | type: `_path` · parser destination: `write_relink_manifest`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| root cli | `src/x86decomp/cli.py` | `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
