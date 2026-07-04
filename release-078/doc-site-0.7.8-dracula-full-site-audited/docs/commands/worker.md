---
title: x86decomp worker
description: Exact v0.7.8 parser-derived reference for `x86decomp worker`.
---


# `x86decomp worker`

Canonical worker commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp worker [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,list,register,select,status} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `doctor` | `usage: x86decomp worker doctor [-h] worker_id` | `governance` |
| `list` | `usage: x86decomp worker list [-h] [--status STATUS]` | `governance` |
| `register` | `usage: x86decomp worker register [-h] [--endpoint ENDPOINT] [--environment-sha256 ENVIRONMENT_SHA256] name capabilities_json` | `governance` |
| `select` | `usage: x86decomp worker select [-h] required_json` | `governance` |
| `status` | `usage: x86decomp worker status [-h] worker_id status` | `governance` |

### `x86decomp worker doctor`

```text
usage: x86decomp worker doctor [-h] worker_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `worker_id` | required · parser destination: `worker_id`. No help text declared. |

### `x86decomp worker list`

```text
usage: x86decomp worker list [-h] [--status STATUS]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--status` | parser destination: `status`. No help text declared. |

### `x86decomp worker register`

```text
usage: x86decomp worker register [-h] [--endpoint ENDPOINT]
                                 [--environment-sha256 ENVIRONMENT_SHA256]
                                 name capabilities_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `capabilities_json` | required · parser destination: `capabilities_json`. No help text declared. |
| `--endpoint` | parser destination: `endpoint`. No help text declared. |
| `--environment-sha256` | parser destination: `environment_sha256`. No help text declared. |

### `x86decomp worker select`

```text
usage: x86decomp worker select [-h] required_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `required_json` | required · parser destination: `required_json`. No help text declared. |

### `x86decomp worker status`

```text
usage: x86decomp worker status [-h] worker_id status
```

| Argument | Exact parser declaration |
| --- | --- |
| `worker_id` | required · parser destination: `worker_id`. No help text declared. |
| `status` | required · parser destination: `status`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
