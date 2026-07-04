---
title: x86decomp plugin
---

# `x86decomp plugin`

Canonical plugin commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp plugin [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,install,invoke,list,validate} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `doctor` | `usage: x86decomp plugin doctor [-h] plugin_id` |
| `install` | `usage: x86decomp plugin install [-h] manifest` |
| `invoke` | `usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT] plugin_id capability request_json` |
| `list` | `usage: x86decomp plugin list [-h]` |
| `validate` | `usage: x86decomp plugin validate [-h] manifest` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp plugin doctor` | `governance` |
| `x86decomp plugin install` | `governance` |
| `x86decomp plugin invoke` | `governance` |
| `x86decomp plugin list` | `governance` |
| `x86decomp plugin validate` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
