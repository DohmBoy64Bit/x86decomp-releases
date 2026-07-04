---
title: x86decomp graph
description: Exact v0.7.8 parser-derived reference for `x86decomp graph`.
---


# `x86decomp graph`

Canonical graph commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp graph [-h] [--project PROJECT] [--actor ACTOR]
                       {edge,impact,node} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `edge` | `usage: x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON] source_id target_id relation` | `governance` |
| `impact` | `usage: x86decomp graph impact [-h] [--direction DIRECTION] [--max-depth MAX_DEPTH] [--relations RELATIONS] node_id` | `governance` |
| `node` | `usage: x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON] node_id kind label` | `governance` |

### `x86decomp graph edge`

```text
usage: x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON]
                            source_id target_id relation
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_id` | required · parser destination: `source_id`. No help text declared. |
| `target_id` | required · parser destination: `target_id`. No help text declared. |
| `relation` | required · parser destination: `relation`. No help text declared. |
| `--attributes-json` | parser destination: `attributes_json`. No help text declared. |

### `x86decomp graph impact`

```text
usage: x86decomp graph impact [-h] [--direction DIRECTION]
                              [--max-depth MAX_DEPTH] [--relations RELATIONS]
                              node_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `node_id` | required · parser destination: `node_id`. No help text declared. |
| `--direction` | default: `'outbound'` · parser destination: `direction`. No help text declared. |
| `--max-depth` | type: `int` · default: `8` · parser destination: `max_depth`. No help text declared. |
| `--relations` | parser destination: `relations`. No help text declared. |

### `x86decomp graph node`

```text
usage: x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON]
                            node_id kind label
```

| Argument | Exact parser declaration |
| --- | --- |
| `node_id` | required · parser destination: `node_id`. No help text declared. |
| `kind` | required · parser destination: `kind`. No help text declared. |
| `label` | required · parser destination: `label`. No help text declared. |
| `--attributes-json` | parser destination: `attributes_json`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
