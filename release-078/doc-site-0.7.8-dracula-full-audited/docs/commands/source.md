---
title: x86decomp source
---

# `x86decomp source`

Canonical source commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source [-h] [--project PROJECT] [--actor ACTOR]
                        {impact,lock,reconcile,unlock} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `impact` | `usage: x86decomp source impact [-h] path` |
| `lock` | `usage: x86decomp source lock [-h] --reason REASON path` |
| `reconcile` | `usage: x86decomp source reconcile [-h] [--before-sha256 BEFORE_SHA256] [--semantic {true,false}] path` |
| `unlock` | `usage: x86decomp source unlock [-h] path` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp source impact` | `reconstruction` |
| `x86decomp source lock` | `reconstruction` |
| `x86decomp source reconcile` | `reconstruction` |
| `x86decomp source unlock` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
