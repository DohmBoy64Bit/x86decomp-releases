---
title: x86decomp worker
---

# `x86decomp worker`

Canonical worker commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp worker [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,list,register,select,status} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `doctor` | `usage: x86decomp worker doctor [-h] worker_id` |
| `list` | `usage: x86decomp worker list [-h] [--status STATUS]` |
| `register` | `usage: x86decomp worker register [-h] [--endpoint ENDPOINT] [--environment-sha256 ENVIRONMENT_SHA256] name capabilities_json` |
| `select` | `usage: x86decomp worker select [-h] required_json` |
| `status` | `usage: x86decomp worker status [-h] worker_id status` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp worker doctor` | `governance` |
| `x86decomp worker list` | `governance` |
| `x86decomp worker register` | `governance` |
| `x86decomp worker select` | `governance` |
| `x86decomp worker status` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
