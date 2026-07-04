---
title: x86decomp capsule
description: Exact v0.7.8 parser-derived reference for `x86decomp capsule`.
---


# `x86decomp capsule`

Canonical capsule commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp capsule [-h] [--project PROJECT] [--actor ACTOR]
                         {create,inspect,reproduce,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `create` | `usage: x86decomp capsule create [-h] [--include INCLUDE] [--external-json EXTERNAL_JSON] name output` | `reconstruction` |
| `inspect` | `usage: x86decomp capsule inspect [-h] path` | `reconstruction` |
| `reproduce` | `usage: x86decomp capsule reproduce [-h] path destination` | `reconstruction` |
| `verify` | `usage: x86decomp capsule verify [-h] path` | `reconstruction` |

### `x86decomp capsule create`

```text
usage: x86decomp capsule create [-h] [--include INCLUDE]
                                [--external-json EXTERNAL_JSON]
                                name output
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--include` | default: `[]` · parser destination: `include`. No help text declared. |
| `--external-json` | parser destination: `external_json`. No help text declared. |

### `x86decomp capsule inspect`

```text
usage: x86decomp capsule inspect [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

### `x86decomp capsule reproduce`

```text
usage: x86decomp capsule reproduce [-h] path destination
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |
| `destination` | required · parser destination: `destination`. No help text declared. |

### `x86decomp capsule verify`

```text
usage: x86decomp capsule verify [-h] path
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
