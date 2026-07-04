---
title: x86decomp source
description: Exact v0.7.8 parser-derived reference for `x86decomp source`.
---


# `x86decomp source`

Canonical source commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source [-h] [--project PROJECT] [--actor ACTOR]
                        {impact,lock,reconcile,unlock} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `impact` | `usage: x86decomp source impact [-h] path` | `reconstruction` |
| `lock` | `usage: x86decomp source lock [-h] --reason REASON path` | `reconstruction` |
| `reconcile` | `usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256] [--semantic {true,false}] path` | `reconstruction` |
| `unlock` | `usage: x86decomp source unlock [-h] path` | `reconstruction` |

### `x86decomp source impact`

```text
usage: x86decomp source impact [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

### `x86decomp source lock`

```text
usage: x86decomp source lock [-h] --reason REASON path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |
| `--reason` | required · parser destination: `reason`. No help text declared. |

### `x86decomp source reconcile`

```text
usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256]
                                  [--semantic {true,false}]
                                  path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |
| `--before-sha256` | parser destination: `before_sha256`. No help text declared. |
| `--semantic` | choices: `true`, `false` · parser destination: `semantic`. No help text declared. |

### `x86decomp source unlock`

```text
usage: x86decomp source unlock [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
