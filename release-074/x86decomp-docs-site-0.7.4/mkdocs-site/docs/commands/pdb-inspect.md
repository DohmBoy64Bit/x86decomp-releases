---
title: x86decomp pdb-inspect
description: inspect an MSF 7.0 PDB and optionally match it to a PE
original_path: commands/pdb-inspect.html
---

<a id="command-pdb-inspect"></a>

Section: Command reference

# `x86decomp pdb-inspect`

inspect an MSF 7.0 PDB and optionally match it to a PE

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp pdb-inspect --help
```

Metadata: current · core

## `x86decomp pdb-inspect`

inspect an MSF 7.0 PDB and optionally match it to a PE

### Usage

```
x86decomp pdb-inspect [-h] [--pe PE] pdb
```

### Syntax example

```
x86decomp pdb-inspect ./target.pdb
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `pdb` required · type: _path | No argument help text is declared; parser destination is `pdb`. |
| `--pe` type: _path | No argument help text is declared; parser destination is `pe`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
