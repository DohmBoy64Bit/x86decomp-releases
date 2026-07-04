---
title: x86decomp tests
---

# `x86decomp tests`

Canonical tests commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp tests [-h] [--project PROJECT] [--actor ACTOR]
                       {add,explain,list,promote-counterexample,synthesize} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add` | `usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON --evidence-json EVIDENCE_JSON name scope_kind scope_id test_kind relative_path content_file` |
| `explain` | `usage: x86decomp tests explain [-h] test_id` |
| `list` | `usage: x86decomp tests list [-h]` |
| `promote-counterexample` | `usage: x86decomp tests promote-counterexample [-h] [--name NAME] counterexample_id` |
| `synthesize` | `usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp tests add` | `reconstruction` |
| `x86decomp tests explain` | `reconstruction` |
| `x86decomp tests list` | `reconstruction` |
| `x86decomp tests promote-counterexample` | `reconstruction` |
| `x86decomp tests synthesize` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
