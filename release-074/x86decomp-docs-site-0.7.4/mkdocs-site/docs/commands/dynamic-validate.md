---
title: x86decomp dynamic-validate
description: The v0.7.4 parser declares this command without additional descriptive
  help text.
original_path: commands/dynamic-validate.html
---

<a id="command-dynamic-validate"></a>

Section: Command reference

# `x86decomp dynamic-validate`

The v0.7.4 parser declares this command without additional descriptive help text.

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp dynamic-validate --help
```

Metadata: current · core

## `x86decomp dynamic-validate`

The v0.7.4 parser declares this command without additional descriptive help text.

### Usage

```
x86decomp dynamic-validate [-h] [--target-base TARGET_BASE]
                                  [--candidate-base CANDIDATE_BASE]
                                  [--report REPORT]
                                  target candidate harness
```

### Syntax example

```
x86decomp dynamic-validate ./target.exe ./candidate.bin example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `target` required · type: _path | No argument help text is declared; parser destination is `target`. |
| `candidate` required · type: _path | No argument help text is declared; parser destination is `candidate`. |
| `harness` required · type: _path | No argument help text is declared; parser destination is `harness`. |
| `--target-base` type: _int | No argument help text is declared; parser destination is `target_base`. |
| `--candidate-base` type: _int | No argument help text is declared; parser destination is `candidate_base`. |
| `--report` type: _path | No argument help text is declared; parser destination is `report`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
