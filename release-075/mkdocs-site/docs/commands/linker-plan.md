---
title: x86decomp linker-plan
description: Exact parser-derived reference for x86decomp linker-plan in 0.7.5.
---

# `x86decomp linker-plan`

## `x86decomp linker-plan`

usage: x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER]

### Usage

```text
x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER]
                             [--output-image OUTPUT_IMAGE] [--report REPORT]
                             [--write-relink-manifest WRITE_RELINK_MANIFEST]
                             pe map objects [objects ...]
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `pe` | required · type: `_path`. No help text is declared; parser destination is `pe`. |
| `map` | required · type: `_path`. No help text is declared; parser destination is `map`. |
| `objects` | required · type: `_path` · nargs: `+`. No help text is declared; parser destination is `objects`. |
| `--library` | default: `[]` · type: `_path`. No help text is declared; parser destination is `library`. |
| `--linker` | default: `'lld-link'`. No help text is declared; parser destination is `linker`. |
| `--output-image` | default: `'build/reconstructed.exe'`. No help text is declared; parser destination is `output_image`. |
| `--report` | type: `_path`. No help text is declared; parser destination is `report`. |
| `--write-relink-manifest` | type: `_path`. No help text is declared; parser destination is `write_relink_manifest`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `core` | `src/x86decomp/cli.py` · `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c` |
