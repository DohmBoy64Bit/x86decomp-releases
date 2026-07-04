---
title: x86decomp module
---

# `x86decomp module`

Canonical module commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp module [-h] [--project PROJECT] [--actor ACTOR]
                        {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add-member` | `usage: x86decomp module add-member [-h] [--ordinal ORDINAL] [--evidence-json EVIDENCE_JSON] module_id member_kind member_id` |
| `add-unit-member` | `usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE] [--ordinal ORDINAL] unit_id member_kind member_id` |
| `assign` | `usage: x86decomp module assign [-h] --module MODULE [--class-name CLASS_NAME] [--header HEADER] [--source SOURCE] [--report REPORT] function_id` |
| `create` | `usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] name` |
| `create-unit` | `usage: x86decomp module create-unit [-h] [--module-id MODULE_ID] [--language LANGUAGE] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] source_path` |
| `list` | `usage: x86decomp module list [-h]` |
| `show` | `usage: x86decomp module show [-h] module_id` |
| `show-unit` | `usage: x86decomp module show-unit [-h] unit_id` |
| `suggest` | `usage: x86decomp module suggest [-h] [--output OUTPUT]` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp module add-member` | `reconstruction` |
| `x86decomp module add-unit-member` | `reconstruction` |
| `x86decomp module assign` | `reconstruction` |
| `x86decomp module create` | `reconstruction` |
| `x86decomp module create-unit` | `reconstruction` |
| `x86decomp module list` | `reconstruction` |
| `x86decomp module show` | `reconstruction` |
| `x86decomp module show-unit` | `reconstruction` |
| `x86decomp module suggest` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
