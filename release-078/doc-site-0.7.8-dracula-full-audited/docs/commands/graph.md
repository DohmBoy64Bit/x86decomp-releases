---
title: x86decomp graph
---

# `x86decomp graph`

Canonical graph commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp graph [-h] [--project PROJECT] [--actor ACTOR]
                       {edge,impact,node} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `edge` | `usage: x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON] source_id target_id relation` |
| `impact` | `usage: x86decomp graph impact [-h] [--direction DIRECTION] [--max-depth MAX_DEPTH] [--relations RELATIONS] node_id` |
| `node` | `usage: x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON] node_id kind label` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp graph edge` | `governance` |
| `x86decomp graph impact` | `governance` |
| `x86decomp graph node` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
