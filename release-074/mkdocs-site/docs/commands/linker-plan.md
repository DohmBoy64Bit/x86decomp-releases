---
title: x86decomp linker-plan
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/linker-plan.html
---

<a id="command-linker-plan"></a>

Section: Command reference

# `x86decomp linker-plan`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp linker-plan --help
```

Metadata: current · core

## `x86decomp linker-plan`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp linker-plan [-h] [--library LIBRARY] [--linker LINKER]
                             [--output-image OUTPUT_IMAGE] [--report REPORT]
                             [--write-relink-manifest WRITE_RELINK_MANIFEST]
                             pe map objects [objects ...]
```

### Syntax example

```
x86decomp linker-plan ./target.exe ./target.map ./candidate.obj
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `pe` required · type: _path | No argument help text is declared; parser destination is `pe`. |
| `map` required · type: _path | No argument help text is declared; parser destination is `map`. |
| `objects` required · nargs: + · type: _path | No argument help text is declared; parser destination is `objects`. |
| `--library` default: [] · type: _path | No argument help text is declared; parser destination is `library`. |
| `--linker` default: 'lld-link' | No argument help text is declared; parser destination is `linker`. |
| `--output-image` default: 'build/reconstructed.exe' | No argument help text is declared; parser destination is `output_image`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |
| `--write-relink-manifest` type: _path | No argument help text is declared; parser destination is `write_relink_manifest`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
