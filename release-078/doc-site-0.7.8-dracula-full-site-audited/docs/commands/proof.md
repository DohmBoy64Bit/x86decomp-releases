---
title: x86decomp proof
description: Exact v0.7.8 parser-derived reference for `x86decomp proof`.
---


# `x86decomp proof`

Canonical proof commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp proof [-h] [--project PROJECT] [--actor ACTOR]
                       {evaluate,export,inspect,obligation,result,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `evaluate` | `usage: x86decomp proof evaluate [-h] obligation_id` | `governance` |
| `export` | `usage: x86decomp proof export [-h] [--include INCLUDE] output` | `governance` |
| `inspect` | `usage: x86decomp proof inspect [-h] path` | `governance` |
| `obligation` | `usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON] scope_kind scope_id property_name required_status` | `governance` |
| `result` | `usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256] obligation_id status validator report_json` | `governance` |
| `verify` | `usage: x86decomp proof verify [-h] path` | `governance` |

### `x86decomp proof evaluate`

```text
usage: x86decomp proof evaluate [-h] obligation_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `obligation_id` | required · parser destination: `obligation_id`. No help text declared. |

### `x86decomp proof export`

```text
usage: x86decomp proof export [-h] [--include INCLUDE] output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |
| `--include` | default: `[]` · parser destination: `include`. No help text declared. |

### `x86decomp proof inspect`

```text
usage: x86decomp proof inspect [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

### `x86decomp proof obligation`

```text
usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON]
                                  scope_kind scope_id property_name
                                  required_status
```

| Argument | Exact parser declaration |
| --- | --- |
| `scope_kind` | required · parser destination: `scope_kind`. No help text declared. |
| `scope_id` | required · parser destination: `scope_id`. No help text declared. |
| `property_name` | required · parser destination: `property_name`. No help text declared. |
| `required_status` | required · parser destination: `required_status`. No help text declared. |
| `--assumptions-json` | parser destination: `assumptions_json`. No help text declared. |

### `x86decomp proof result`

```text
usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256]
                              obligation_id status validator report_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `obligation_id` | required · parser destination: `obligation_id`. No help text declared. |
| `status` | required · parser destination: `status`. No help text declared. |
| `validator` | required · parser destination: `validator`. No help text declared. |
| `report_json` | required · parser destination: `report_json`. No help text declared. |
| `--artifact-sha256` | parser destination: `artifact_sha256`. No help text declared. |

### `x86decomp proof verify`

```text
usage: x86decomp proof verify [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
