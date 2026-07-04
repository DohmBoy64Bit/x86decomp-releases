---
title: x86decomp proof
---

# `x86decomp proof`

Canonical proof commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp proof [-h] [--project PROJECT] [--actor ACTOR]
                       {evaluate,export,inspect,obligation,result,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `evaluate` | `usage: x86decomp proof evaluate [-h] obligation_id` |
| `export` | `usage: x86decomp proof export [-h] [--include INCLUDE] output` |
| `inspect` | `usage: x86decomp proof inspect [-h] path` |
| `obligation` | `usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON] scope_kind scope_id property_name required_status` |
| `result` | `usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256] obligation_id status validator report_json` |
| `verify` | `usage: x86decomp proof verify [-h] path` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp proof evaluate` | `governance` |
| `x86decomp proof export` | `governance` |
| `x86decomp proof inspect` | `governance` |
| `x86decomp proof obligation` | `governance` |
| `x86decomp proof result` | `governance` |
| `x86decomp proof verify` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
