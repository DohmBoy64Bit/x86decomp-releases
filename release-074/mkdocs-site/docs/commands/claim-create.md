---
title: x86decomp claim-create
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/claim-create.html
---

<a id="command-claim-create"></a>

Section: Command reference

# `x86decomp claim-create`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp claim-create --help
```

Metadata: current · core

## `x86decomp claim-create`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE
                              --object OBJECT_VALUE [--evidence EVIDENCE]
                              [--id ID]
                              project
```

### Syntax example

```
x86decomp claim-create ./work --subject example --predicate matches --object ./candidate.obj
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--subject` required | No argument help text is declared; parser destination is `subject`. |
| `--predicate` required | No argument help text is declared; parser destination is `predicate`. |
| `--object` required | No argument help text is declared; parser destination is `object_value`. |
| `--evidence` default: [] | No argument help text is declared; parser destination is `evidence`. |
| `--id` | No argument help text is declared; parser destination is `id`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
