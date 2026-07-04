---
title: x86decomp linker-plan
description: Command reference for `x86decomp linker-plan`.
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

| Argument | Details |
| --- | --- |
| `pe` | required · type: `path`. |
| `map` | required · type: `path`. |
| `objects` | required · nargs: `+` · type: `path`. |
| `--library` | type: `path` · default: `[]`. |
| `--linker` | default: `'lld-link'`. |
| `--output-image` | default: `'build/reconstructed.exe'`. |
| `--report` | type: `path`. |
| `--write-relink-manifest` | type: `path`. |


