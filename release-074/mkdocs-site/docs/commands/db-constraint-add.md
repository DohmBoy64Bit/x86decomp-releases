---
title: x86decomp db-constraint-add
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/db-constraint-add.html
---

<a id="command-db-constraint-add"></a>

Section: Command reference

# `x86decomp db-constraint-add`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp db-constraint-add --help
```

Metadata: current · core

## `x86decomp db-constraint-add`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID]
                                   [--confidence CONFIDENCE]
                                   database subject relation object_value
                                   provenance
```

### Syntax example

```
x86decomp db-constraint-add ./analysis.db example example ./candidate.obj example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `database` required · type: _path | No argument help text is declared; parser destination is `database`. |
| `subject` required | No argument help text is declared; parser destination is `subject`. |
| `relation` required | No argument help text is declared; parser destination is `relation`. |
| `object_value` required | No argument help text is declared; parser destination is `object_value`. |
| `provenance` required | No argument help text is declared; parser destination is `provenance`. |
| `--evidence-id` | No argument help text is declared; parser destination is `evidence_id`. |
| `--confidence` type: float | No argument help text is declared; parser destination is `confidence`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
