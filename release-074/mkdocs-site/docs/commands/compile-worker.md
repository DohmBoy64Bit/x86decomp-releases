---
title: x86decomp compile-worker
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/compile-worker.html
---

<a id="command-compile-worker"></a>

Section: Command reference

# `x86decomp compile-worker`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp compile-worker --help
```

Metadata: current · core

## `x86decomp compile-worker`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp compile-worker [-h] [--isolation {local_bounded,container}]
                                [--container-image CONTAINER_IMAGE]
                                [--cache CACHE] [--report REPORT]
                                profile source output
```

### Syntax example

```
x86decomp compile-worker ./input.json ./candidate.c ./output.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `profile` required · type: _path | No argument help text is declared; parser destination is `profile`. |
| `source` required · type: _path | No argument help text is declared; parser destination is `source`. |
| `output` required · type: _path | No argument help text is declared; parser destination is `output`. |
| `--isolation` default: 'local_bounded' · choices: local_bounded, container | No argument help text is declared; parser destination is `isolation`. |
| `--container-image` | No argument help text is declared; parser destination is `container_image`. |
| `--cache` type: _path | No argument help text is declared; parser destination is `cache`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
