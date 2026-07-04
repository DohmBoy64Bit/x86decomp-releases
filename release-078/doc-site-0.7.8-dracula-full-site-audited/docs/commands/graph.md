---
title: x86decomp graph
description: Command reference for `x86decomp graph`.
---


# `x86decomp graph`

Canonical graph commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp graph [-h] [--project PROJECT] [--actor ACTOR]
                       {edge,impact,node} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

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

| Argument | Details |
| --- | --- |
| `source_id` | required. |
| `target_id` | required. |
| `relation` | required. |
| `--attributes-json` | — |

### `x86decomp graph impact`

```text
usage: x86decomp graph impact [-h] [--direction DIRECTION]
                              [--max-depth MAX_DEPTH] [--relations RELATIONS]
                              node_id
```

| Argument | Details |
| --- | --- |
| `node_id` | required. |
| `--direction` | default: `'outbound'`. |
| `--max-depth` | type: `int` · default: `8`. |
| `--relations` | — |

### `x86decomp graph node`

```text
usage: x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON]
                            node_id kind label
```

| Argument | Details |
| --- | --- |
| `node_id` | required. |
| `kind` | required. |
| `label` | required. |
| `--attributes-json` | — |


