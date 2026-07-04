---
title: x86decomp capsule
---

# `x86decomp capsule`

Canonical capsule commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp capsule [-h] [--project PROJECT] [--actor ACTOR]
                         {create,inspect,reproduce,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `create` | `usage: x86decomp capsule create [-h] [--include INCLUDE] [--external-json EXTERNAL_JSON] name output` |
| `inspect` | `usage: x86decomp capsule inspect [-h] path` |
| `reproduce` | `usage: x86decomp capsule reproduce [-h] path destination` |
| `verify` | `usage: x86decomp capsule verify [-h] path` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp capsule create` | `reconstruction` |
| `x86decomp capsule inspect` | `reconstruction` |
| `x86decomp capsule reproduce` | `reconstruction` |
| `x86decomp capsule verify` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
