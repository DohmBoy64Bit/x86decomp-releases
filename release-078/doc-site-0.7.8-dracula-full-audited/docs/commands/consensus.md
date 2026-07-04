---
title: x86decomp consensus
---

# `x86decomp consensus`

Canonical consensus commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp consensus [-h] [--project PROJECT] [--actor ACTOR]
                           {conflicts,explain,record,resolve,scan} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `conflicts` | `usage: x86decomp consensus conflicts [-h]` |
| `explain` | `usage: x86decomp consensus explain [-h] subject_kind subject_id property_name` |
| `record` | `usage: x86decomp consensus record [-h] --adapter ADAPTER --adapter-version ADAPTER_VERSION --evidence-id EVIDENCE_ID --group GROUP [--confidence CONFIDENCE] subject_kind subject_id property_name value_json` |
| `resolve` | `usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE [--lock] subject_kind subject_id property_name selected_value_json` |
| `scan` | `usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND] [--subject-id SUBJECT_ID]` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp consensus conflicts` | `governance` |
| `x86decomp consensus explain` | `governance` |
| `x86decomp consensus record` | `governance` |
| `x86decomp consensus resolve` | `governance` |
| `x86decomp consensus scan` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
