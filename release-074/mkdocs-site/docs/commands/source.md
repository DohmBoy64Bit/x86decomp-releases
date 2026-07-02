---
title: x86decomp source
description: Canonical source commands implemented by the current capability subsystem.
original_path: commands/source.html
---

<a id="command-source-impact"></a>
<a id="command-source-lock"></a>
<a id="command-source-reconcile"></a>
<a id="command-source-unlock"></a>

Section: Command reference

# `x86decomp source`

Canonical source commands implemented by the current capability subsystem.

Metadata: current · canonical group · 4 runnable paths

## Help

```
x86decomp source --help
```

Metadata: current · reconstruction

## `x86decomp source impact`

impact command

### Usage

```
x86decomp source impact [-h] path
```

### Syntax example

```
x86decomp source impact ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp source lock`

lock command

### Usage

```
x86decomp source lock [-h] --reason REASON path
```

### Syntax example

```
x86decomp source lock ./input.json --reason reviewed-change
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |
| `--reason` required | No argument help text is declared; parser destination is `reason`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp source reconcile`

reconcile command

### Usage

```
x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256]
                                  [--semantic {true,false}]
                                  path
```

### Syntax example

```
x86decomp source reconcile ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |
| `--before-sha256` | No argument help text is declared; parser destination is `before_sha256`. |
| `--semantic` choices: true, false | No argument help text is declared; parser destination is `semantic`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · reconstruction

## `x86decomp source unlock`

unlock command

### Usage

```
x86decomp source unlock [-h] path
```

### Syntax example

```
x86decomp source unlock ./input.json
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `path` required | No argument help text is declared; parser destination is `path`. |

> **Source basis.** Parser definition: `src/x86decomp/reconstruction/cli.py`; SHA-256 `9535cc526a12ee85a8e41c836c800a4591f3935f9ef7f5a3c3f14f9277356027`. Descriptions above use only parser-declared text or an explicit no-help notice.
